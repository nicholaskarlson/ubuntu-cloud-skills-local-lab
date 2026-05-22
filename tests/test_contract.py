from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TestLocalLabContract(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "LICENSE",
            "Makefile",
            "compose.yaml",
            "public/index.html",
            "public/styles.css",
            "docs/learning-contract.md",
            "docs/book-series-plan.md",
            "docs/quickstart.md",
            "docs/proof-receipts.md",
            "lessons/01-local-publishing-stack.md",
            "scripts/check_env.sh",
            "scripts/write_receipt.sh",
            ".github/workflows/verify.yml",
            "receipts/samples/docker-version-example.txt",
            "receipts/samples/local-web-smoke-example.txt",
            "receipts/samples/local-publishing-stack-receipt-example.txt",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_readme_states_no_paid_cloud_required(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("paid cloud account", text)
        self.assertIn("local-first", text)

    def test_readme_links_quickstart_and_lesson_1(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[Quickstart](docs/quickstart.md)", text)
        self.assertIn("[Lesson 1: Local Publishing Stack](lessons/01-local-publishing-stack.md)", text)
        self.assertIn("[Proof Receipts](docs/proof-receipts.md)", text)

    def test_compose_uses_local_web_port(self):
        text = (ROOT / "compose.yaml").read_text(encoding="utf-8")
        self.assertIn('"8080:80"', text)
        self.assertIn("nginx:", text)

    def test_makefile_has_non_docker_verify_and_docker_receipt_smoke(self):
        text = (ROOT / "Makefile").read_text(encoding="utf-8")
        self.assertIn("verify:", text)
        self.assertIn("lab-smoke:", text)
        self.assertIn("lab-smoke-receipt:", text)
        self.assertIn("check-env:", text)
        self.assertIn("receipt-note:", text)

    def test_learning_contract_says_no_paid_docker_features(self):
        text = (ROOT / "docs/learning-contract.md").read_text(encoding="utf-8").lower()
        self.assertIn("docker pro", text)
        self.assertIn("not be required", text)

    def test_quickstart_is_not_truncated(self):
        text = (ROOT / "docs/quickstart.md").read_text(encoding="utf-8")
        self.assertIn("## 8. Stop the lab", text)
        self.assertIn("## Troubleshooting", text)
        self.assertIn("### You want to reset the lab", text)

    def test_lesson_1_teaches_receipts_and_cleanup(self):
        text = (ROOT / "lessons/01-local-publishing-stack.md").read_text(encoding="utf-8")
        self.assertIn("make lab-smoke-receipt", text)
        self.assertIn("make down", text)
        self.assertIn("site files -> web server container", text)

    def test_proof_receipts_warns_against_secrets(self):
        text = (ROOT / "docs/proof-receipts.md").read_text(encoding="utf-8").lower()
        self.assertIn("never put", text)
        self.assertIn("api tokens", text)
        self.assertIn("ssh private keys", text)

    def test_public_site_is_creator_publishing_demo(self):
        text = (ROOT / "public/index.html").read_text(encoding="utf-8")
        self.assertIn("Independent creator publishing demo", text)
        self.assertIn("The Local Cloud Notebook", text)
        self.assertIn("styles.css", text)

    def test_write_receipt_script_is_safe_shell_script(self):
        text = (ROOT / "scripts/write_receipt.sh").read_text(encoding="utf-8")
        self.assertIn("set -euo pipefail", text)
        self.assertIn("receipts/", text)
        self.assertIn("date -Iseconds", text)

    def test_github_actions_runs_make_verify(self):
        text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("make verify", text)


if __name__ == "__main__":
    unittest.main()
