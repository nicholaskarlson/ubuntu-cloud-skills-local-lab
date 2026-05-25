from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TestSeriesFoundation(unittest.TestCase):
    def test_series_foundation_docs_exist(self):
        required = [
            "docs/series-roadmap.md",
            "docs/software-architecture.md",
            "docs/release-and-tagging-policy.md",
            "docs/secret-safety.md",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_readme_links_series_foundation_docs(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[Series Roadmap](docs/series-roadmap.md)", text)
        self.assertIn("[Software Architecture](docs/software-architecture.md)", text)
        self.assertIn("[Release and Tagging Policy](docs/release-and-tagging-policy.md)", text)
        self.assertIn("[Secret Safety](docs/secret-safety.md)", text)
        self.assertIn("make doctor", text)
        self.assertIn("make repo-map", text)
        self.assertIn("make series-status", text)

    def test_makefile_has_series_foundation_targets(self):
        text = (ROOT / "Makefile").read_text(encoding="utf-8")
        for target in ["doctor:", "repo-map:", "series-status:"]:
            self.assertIn(target, text)
        self.assertIn("bash scripts/doctor.sh", text)
        self.assertIn("bash scripts/repo_map.sh", text)
        self.assertIn("bash scripts/repo_map.sh --series-status", text)

    def test_doctor_script_is_safe_and_non_deploying(self):
        text = (ROOT / "scripts/doctor.sh").read_text(encoding="utf-8")
        self.assertIn("set -euo pipefail", text)
        self.assertIn("python3 -m unittest discover -s tests -v", text)
        self.assertIn("does not start Docker", text)
        self.assertNotIn("docker compose up", text)
        self.assertNotIn("docker compose down", text)
        self.assertNotIn("bash scripts/write_receipt.sh", text)
        self.assertNotIn("backup_public.sh", text)

    def test_repo_map_script_documents_series_status(self):
        text = (ROOT / "scripts/repo_map.sh").read_text(encoding="utf-8")
        self.assertIn("book1-v1.0.0", text)
        self.assertIn("book2-v1.0.0", text)
        self.assertIn("book6-v1.0.0", text)
        self.assertIn("tests/test_series_foundation.py", text)

    def test_release_policy_preserves_book1_tag_and_main_evolution(self):
        text = (ROOT / "docs/release-and-tagging-policy.md").read_text(encoding="utf-8")
        self.assertIn("book1-v1.0.0", text)
        self.assertIn("88ff6452419bd027f31cb6e7a6799f5ed0695765", text)
        self.assertIn("main", text)
        self.assertIn("Do not move a published book tag casually", text)

    def test_series_roadmap_covers_all_six_book_tags(self):
        text = (ROOT / "docs/series-roadmap.md").read_text(encoding="utf-8")
        for tag in [
            "book1-v1.0.0",
            "book2-v1.0.0",
            "book3-v1.0.0",
            "book4-v1.0.0",
            "book5-v1.0.0",
            "book6-v1.0.0",
        ]:
            self.assertIn(tag, text)
        self.assertIn("No secrets in Git", text)
        self.assertIn("No paid cloud required for Book 1", text)
        self.assertIn("Backup plus restore", text)

    def test_secret_safety_mentions_receipts_logs_and_payments(self):
        text = (ROOT / "docs/secret-safety.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "do not put secrets in git",
            "receipts",
            "logs",
            "stripe secrets",
            "ssh private keys",
            "cloud access keys",
            "customer",
        ]:
            self.assertIn(phrase, text)

    def test_book_series_plan_is_refined_for_coherent_software_line(self):
        text = (ROOT / "docs/book-series-plan.md").read_text(encoding="utf-8")
        self.assertIn("one coherent proof-first software line", text)
        self.assertIn("[Series Roadmap](series-roadmap.md)", text)
        self.assertIn("[Release and Tagging Policy](release-and-tagging-policy.md)", text)
        self.assertIn("book5-v1.0.0", text)
        self.assertIn("hosted checkout", text)
        self.assertIn("no card storage", text)


if __name__ == "__main__":
    unittest.main()
