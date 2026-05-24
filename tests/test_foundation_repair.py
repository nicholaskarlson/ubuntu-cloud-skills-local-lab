from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TestFoundationRepair(unittest.TestCase):
    def test_make_help_runs_and_lists_series_targets(self):
        result = subprocess.run(
            ["make", "help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            f"make help failed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )
        self.assertIn("make doctor", result.stdout)
        self.assertIn("make repo-map", result.stdout)
        self.assertIn("make series-status", result.stdout)
        self.assertIn("print book-by-book software status", result.stdout)

    def test_local_env_files_are_ignored_before_book2(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn(".env.local", text)
        self.assertIn(".env.*.local", text)

    def test_secret_safety_uses_redacted_examples_not_scanner_like_values(self):
        text = (ROOT / "docs/secret-safety.md").read_text(encoding="utf-8")
        self.assertIn("Bad receipt content", text)
        self.assertIn("[redacted", text.lower())
        scanner_like_examples = [
            "STRIPE_SECRET_KEY=...",
            "AWS_SECRET_ACCESS_KEY=...",
            "-----BEGIN OPENSSH PRIVATE KEY-----",
        ]
        for example in scanner_like_examples:
            self.assertNotIn(example, text)

    def test_doctor_tracks_foundation_repair_test(self):
        text = (ROOT / "scripts/doctor.sh").read_text(encoding="utf-8")
        self.assertIn("tests/test_foundation_repair.py", text)

    def test_repo_map_lists_foundation_repair_test(self):
        text = (ROOT / "scripts/repo_map.sh").read_text(encoding="utf-8")
        self.assertIn("tests/test_foundation_repair.py", text)


if __name__ == "__main__":
    unittest.main()
