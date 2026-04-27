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

    def test_redshift_empty_partitions_checked_before_logging_range(self):
        macro = read_macro("macros/plugins/redshift/helpers/add_partitions.sql")

        empty_guard = macro.index("if partitions|length > 0")
        first_partition_lookup = macro.index("partitions[0]")
        self.assertLess(empty_guard, first_partition_lookup)
