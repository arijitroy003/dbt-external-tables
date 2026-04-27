from pathlib import Path
from unittest import TestCase


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_macro(path: str) -> str:
    return (REPO_ROOT / path).read_text()


class JinjaMacroContractsTest(TestCase):
    def test_bigquery_connection_name_does_not_mutate_options(self):
        macro = read_macro("macros/plugins/bigquery/create_external_table.sql")

        self.assertNotIn(".pop(", macro)
        self.assertIn("key not in excluded_options", macro)
