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
            "docs/book1-companion-code.md",
            "lessons/01-local-publishing-stack.md",
            "lessons/02-files-logs-container-lifecycle.md",
            "lessons/03-local-backups-and-restore.md",
            "scripts/check_env.sh",
            "scripts/write_receipt.sh",
            "scripts/show_local_stack.sh",
            "scripts/logs_receipt.sh",
            "scripts/container_lifecycle_receipt.sh",
            "scripts/backup_public.sh",
            "scripts/backup_receipt.sh",
            "scripts/restore_public_backup.sh",
            ".github/workflows/verify.yml",
            "receipts/samples/docker-version-example.txt",
            "receipts/samples/local-web-smoke-example.txt",
            "receipts/samples/local-publishing-stack-receipt-example.txt",
            "receipts/samples/container-lifecycle-receipt-example.txt",
            "receipts/samples/backup-restore-receipt-example.txt",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_readme_states_no_paid_cloud_required(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("paid cloud account", text)
        self.assertIn("local-first", text)

    def test_readme_links_lessons_and_receipts(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[Quickstart](docs/quickstart.md)", text)
        self.assertIn("[Lesson 1: Local Publishing Stack](lessons/01-local-publishing-stack.md)", text)
        self.assertIn(
            "[Lesson 2: Files, Logs, and the Container Lifecycle](lessons/02-files-logs-container-lifecycle.md)",
            text,
        )
        self.assertIn("[Lesson 3: Local Backups and Restore](lessons/03-local-backups-and-restore.md)", text)
        self.assertIn("[Proof Receipts](docs/proof-receipts.md)", text)


    def test_book1_companion_code_pin_is_documented(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = (ROOT / "docs/book1-companion-code.md").read_text(encoding="utf-8")
        for text in [readme, doc]:
            self.assertIn("book1-v1.0.0", text)
            self.assertIn("88ff6452419bd027f31cb6e7a6799f5ed0695765", text)
            self.assertIn("Book 1", text)
        self.assertIn("main branch may continue to change", doc)
        self.assertIn("git checkout book1-v1.0.0", doc)

    def test_compose_uses_local_web_port(self):
        text = (ROOT / "compose.yaml").read_text(encoding="utf-8")
        self.assertIn('"8080:80"', text)
        self.assertIn("nginx:", text)

    def test_makefile_has_non_docker_verify_and_docker_receipt_targets(self):
        text = (ROOT / "Makefile").read_text(encoding="utf-8")
        self.assertIn("verify:", text)
        self.assertIn("lab-smoke:", text)
        self.assertIn("lab-smoke-receipt:", text)
        self.assertIn("logs-receipt:", text)
        self.assertIn("lifecycle-receipt:", text)
        self.assertIn("backup-public:", text)
        self.assertIn("backup-receipt:", text)
        self.assertIn("restore-public:", text)
        self.assertIn("backup-list:", text)
        self.assertIn("inspect-stack:", text)
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

    def test_lesson_2_teaches_logs_and_lifecycle(self):
        text = (ROOT / "lessons/02-files-logs-container-lifecycle.md").read_text(encoding="utf-8")
        self.assertIn("make inspect-stack", text)
        self.assertIn("make logs-receipt", text)
        self.assertIn("make lifecycle-receipt", text)
        self.assertIn("start -> request -> status -> logs -> stop -> receipt", text)


    def test_lesson_3_teaches_backup_and_restore(self):
        text = (ROOT / "lessons/03-local-backups-and-restore.md").read_text(encoding="utf-8")
        self.assertIn("make backup-public", text)
        self.assertIn("make backup-receipt", text)
        self.assertIn("make restore-public", text)
        self.assertIn("site files -> backup archive -> checksum -> restore test -> receipt", text)

    def test_proof_receipts_warns_against_secrets(self):
        text = (ROOT / "docs/proof-receipts.md").read_text(encoding="utf-8").lower()
        self.assertIn("never put", text)
        self.assertIn("api tokens", text)
        self.assertIn("ssh private keys", text)

    def test_public_site_is_creator_publishing_demo(self):
        text = (ROOT / "public/index.html").read_text(encoding="utf-8")
        self.assertIn("Independent creator publishing demo", text)
        self.assertIn("The Local Cloud Notebook", text)
        self.assertIn("Logs and Lifecycle", text)
        self.assertIn("Backups and Restore", text)
        self.assertIn("styles.css", text)

    def test_write_receipt_script_is_safe_shell_script(self):
        text = (ROOT / "scripts/write_receipt.sh").read_text(encoding="utf-8")
        self.assertIn("set -euo pipefail", text)
        self.assertIn("receipts/", text)
        self.assertIn("date -Iseconds", text)

    def test_lifecycle_scripts_are_safe_shell_scripts(self):
        for rel in [
            "scripts/show_local_stack.sh",
            "scripts/logs_receipt.sh",
            "scripts/container_lifecycle_receipt.sh",
        ]:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("set -euo pipefail", text)
        lifecycle = (ROOT / "scripts/container_lifecycle_receipt.sh").read_text(encoding="utf-8")
        self.assertIn("docker compose down", lifecycle)
        self.assertIn("trap cleanup EXIT", lifecycle)


    def test_backup_restore_scripts_are_safe_shell_scripts(self):
        for rel in [
            "scripts/backup_public.sh",
            "scripts/backup_receipt.sh",
            "scripts/restore_public_backup.sh",
        ]:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("set -euo pipefail", text)
        backup = (ROOT / "scripts/backup_public.sh").read_text(encoding="utf-8")
        self.assertIn("tar -czf", backup)
        self.assertIn("sha256sum", backup)
        restore = (ROOT / "scripts/restore_public_backup.sh").read_text(encoding="utf-8")
        self.assertIn("tar -tzf", restore)
        self.assertIn("public/index.html", restore)
        self.assertIn("public/styles.css", restore)

    def test_gitignore_ignores_local_backups(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("backups/*.tar.gz", text)
        self.assertIn("backups/*.tar.gz.sha256", text)

    def test_github_actions_runs_make_verify(self):
        text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("make verify", text)


if __name__ == "__main__":
    unittest.main()
