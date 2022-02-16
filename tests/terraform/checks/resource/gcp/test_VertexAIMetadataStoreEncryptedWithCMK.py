import unittest
import os

from checkov.terraform.checks.resource.gcp.VertexAIMetadataStoreEncryptedWithCMK import check
from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner


class TestVertexAIMetadataStoreEncryptedWithCMK(unittest.TestCase):

    def test(self):
        runner = Runner()
        current_dir = os.path.dirname(os.path.realpath(__file__))

        test_files_dir = current_dir + "/example_VertexAIMetadataStoreEncryptedWithCMK"
        report = runner.run(root_folder=test_files_dir, runner_filter=RunnerFilter(checks=[check.id]))
        summary = report.get_summary()

        passing_resources = {
            'google_vertex_ai_metadata_store.pass',
        }
        failing_resources = {
            'google_vertex_ai_metadata_store.fail',
        }

        passed_check_resources = set([c.resource for c in report.passed_checks])
        failed_check_resources = set([c.resource for c in report.failed_checks])

        self.assertEqual(summary['passed'], 1)
        self.assertEqual(summary['failed'], 1)
        self.assertEqual(summary['skipped'], 0)
        self.assertEqual(summary['parsing_errors'], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)


if __name__ == '__main__':
    unittest.main()
