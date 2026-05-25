"""Contract tests for the Book 2 LAN-first pivot."""

from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class TestBook2LanPivot(unittest.TestCase):
    def test_book2_lan_pivot_files_exist(self) -> None:
        required = [
            "docs/book2-lan-server-lab.md",
            "book2/env.example",
            "scripts/book2_doctor.sh",
            "scripts/book2_check_inputs.sh",
            "scripts/book2_lan_ip_help.sh",
            "tests/test_book2_lan_pivot.py",
        ]
        for path in required:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_makefile_has_book2_safe_targets(self) -> None:
        text = read_text("Makefile")
        for target in ["book2-doctor:", "book2-check-inputs:", "book2-lan-ip-help:"]:
            self.assertIn(target, text)
        self.assertIn("bash scripts/book2_doctor.sh", text)
        self.assertIn("bash scripts/book2_check_inputs.sh", text)
        self.assertIn("bash scripts/book2_lan_ip_help.sh", text)

    def test_book2_doctor_is_non_mutating(self) -> None:
        text = read_text("scripts/book2_doctor.sh")
        self.assertIn("set -euo pipefail", text)
        self.assertIn("does not connect by SSH", text)
        forbidden = [
            "scp ",
            "rsync ",
            "apt install",
            "ufw allow",
            "docker compose up",
            "write_receipt.sh",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, text)

    def test_book2_check_inputs_does_not_connect(self) -> None:
        text = read_text("scripts/book2_check_inputs.sh")
        self.assertIn("BOOK2_MODE", text)
        self.assertIn("BOOK2_HOST", text)
        self.assertIn("BOOK2_USER", text)
        self.assertIn("BOOK2_SSH_PORT", text)
        self.assertIn("private LAN IPv4", text)
        forbidden = ["scp ", "rsync ", "apt install", "ufw allow"]
        for phrase in forbidden:
            self.assertNotIn(phrase, text)

    def test_env_example_is_lan_first_and_has_no_secrets(self) -> None:
        text = read_text("book2/env.example")
        self.assertIn("BOOK2_MODE=lan", text)
        self.assertIn("BOOK2_HOST=10.0.0.113", text)
        self.assertIn("BOOK2_USER=nick", text)
        self.assertIn("BOOK2_SSH_PORT=22", text)
        secret_markers = [
            "PASSWORD=",
            "TOKEN=",
            "SECRET=",
            "PRIVATE KEY",
            "AWS_SECRET_ACCESS_KEY",
            "STRIPE_SECRET_KEY",
        ]
        for marker in secret_markers:
            self.assertNotIn(marker, text)

    def test_series_docs_pivot_away_from_required_cloud_providers(self) -> None:
        combined = "\n".join(
            read_text(path)
            for path in [
                "README.md",
                "docs/book-series-plan.md",
                "docs/series-roadmap.md",
                "docs/software-architecture.md",
                "docs/book2-companion-code.md",
                "docs/book2-lan-server-lab.md",
            ]
        ).lower()
        self.assertIn("lan-first", combined)
        self.assertIn("your first ubuntu server lab", combined)
        self.assertIn("digitalocean", combined)
        self.assertIn("aws", combined)
        self.assertIn("not required", combined)
        self.assertIn("router port forwarding", combined)
        self.assertIn("optional", combined)

    def test_safe_book2_commands_run(self) -> None:
        commands = [
            ["make", "book2-doctor"],
            ["make", "book2-check-inputs"],
            ["make", "book2-lan-ip-help"],
        ]
        for command in commands:
            with self.subTest(command=" ".join(command)):
                result = subprocess.run(
                    command,
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    f"Command failed: {' '.join(command)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
                )

    def test_make_help_lists_book2_safe_targets(self) -> None:
        result = subprocess.run(
            ["make", "help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("make book2-doctor", result.stdout)
        self.assertIn("make book2-check-inputs", result.stdout)
        self.assertIn("make book2-lan-ip-help", result.stdout)


if __name__ == "__main__":
    unittest.main()
