"""Contract tests for the Book 2 planning scaffold.

These tests intentionally verify documentation and safety boundaries before
any live server automation is added.
"""

from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class TestBook2Scaffold(unittest.TestCase):
    def test_book2_scaffold_files_exist(self) -> None:
        required = [
            "docs/book2-companion-code.md",
            "docs/book2-lan-server-lab.md",
            "docs/book2-server-safety-boundary.md",
            "docs/book2-vps-checklist.md",
            "lessons/04-first-ubuntu-server-safety.md",
        ]
        for path in required:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_readme_links_book2_scaffold(self) -> None:
        readme = read_text("README.md")
        self.assertIn("Book 2 LAN-first pivot", readme)
        self.assertIn("docs/book2-companion-code.md", readme)
        self.assertIn("docs/book2-lan-server-lab.md", readme)
        self.assertIn("docs/book2-server-safety-boundary.md", readme)
        self.assertIn("docs/book2-vps-checklist.md", readme)
        self.assertIn("lessons/04-first-ubuntu-server-safety.md", readme)

    def test_book2_docs_keep_safety_boundary_before_automation(self) -> None:
        companion = read_text("docs/book2-companion-code.md")
        lan = read_text("docs/book2-lan-server-lab.md")
        boundary = read_text("docs/book2-server-safety-boundary.md")
        checklist = read_text("docs/book2-vps-checklist.md")
        combined = "\n".join([companion, lan, boundary, checklist]).lower()

        self.assertIn("no live vps automation is included yet", combined)
        self.assertIn("provider portable", combined)
        self.assertIn("ssh private keys", combined)
        self.assertIn("receipts", combined)
        self.assertIn("backup", combined)
        self.assertIn("restore", combined)
        self.assertIn("cleanup", combined)
        self.assertIn("lan-first", combined)
        self.assertIn("router port forwarding", combined)

    def test_book2_lesson_is_non_mutating_scaffold(self) -> None:
        lesson = read_text("lessons/04-first-ubuntu-server-safety.md").lower()
        self.assertIn("does not require a vps yet", lesson)
        self.assertIn("no book 2 command in this scaffold connects to a server", lesson)
        self.assertIn("make verify", lesson)
        self.assertIn("make doctor", lesson)
        self.assertIn("make book2-doctor", lesson)
        self.assertNotIn("apt install", lesson)
        self.assertNotIn("ufw allow", lesson)

    def test_repo_map_lists_book2_scaffold(self) -> None:
        output = subprocess.check_output(
            ["bash", "scripts/repo_map.sh"],
            cwd=ROOT,
            text=True,
        )
        self.assertIn("Book 2 LAN-first scaffold", output)
        self.assertIn("docs/book2-companion-code.md", output)
        self.assertIn("docs/book2-lan-server-lab.md", output)
        self.assertIn("lessons/04-first-ubuntu-server-safety.md", output)
        self.assertIn("tests/test_book2_scaffold.py", output)

    def test_series_status_says_book2_is_lan_first_not_automated(self) -> None:
        output = subprocess.check_output(
            ["bash", "scripts/repo_map.sh", "--series-status"],
            cwd=ROOT,
            text=True,
        )
        self.assertIn("Book 2 — Your First Ubuntu Server Lab", output)
        self.assertIn("Status: LAN-first pivot added", output)
        self.assertIn("no live SSH or deployment automation yet", output)

    def test_doctor_tracks_book2_scaffold(self) -> None:
        doctor = read_text("scripts/doctor.sh")
        self.assertIn("docs/book2-companion-code.md", doctor)
        self.assertIn("docs/book2-lan-server-lab.md", doctor)
        self.assertIn("docs/book2-server-safety-boundary.md", doctor)
        self.assertIn("docs/book2-vps-checklist.md", doctor)
        self.assertIn("lessons/04-first-ubuntu-server-safety.md", doctor)
        self.assertIn("tests/test_book2_scaffold.py", doctor)


if __name__ == "__main__":
    unittest.main()
