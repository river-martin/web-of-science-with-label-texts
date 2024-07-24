import pandas as pd
import unittest
from dataset_splitter.restructure_data import prepare_datasets, write_datasets_to_json
from dataset_splitter.config import PROJECT_ROOT


class TestPrepareDatasets(unittest.TestCase):
    def test_prepare_datasets(self):
        # Check if the returned datasets have the expected columns
        train_df, validate_df, test_df = prepare_datasets()
        expected_columns = ["abstract", "domain", "area"]
        self.assertListEqual(list(train_df.columns), expected_columns)
        self.assertListEqual(list(validate_df.columns), expected_columns)
        self.assertListEqual(list(test_df.columns), expected_columns)

        # Check if the length of the original dataset is preserved
        original_df = pd.read_excel(f"{PROJECT_ROOT}/data/WebOfScience/Meta-data/Data.xlsx")
        original_length = len(original_df)
        self.assertEqual(len(train_df) + len(validate_df) + len(test_df), original_length)

        # Check if the train, validate, and test datasets are disjoint
        train_indices = set(train_df.index)
        validate_indices = set(validate_df.index)
        test_indices = set(test_df.index)
        self.assertTrue(train_indices.isdisjoint(validate_indices))
        self.assertTrue(train_indices.isdisjoint(test_indices))
        self.assertTrue(validate_indices.isdisjoint(test_indices))

    def test_write_datasets_to_json(self):
        # Check if the datasets are written to the expected files
        write_datasets_to_json()
        train_df = pd.read_csv(f"{PROJECT_ROOT}/results/train.csv")
        validate_df = pd.read_csv(f"{PROJECT_ROOT}/results/validate.csv")
        test_df = pd.read_csv(f"{PROJECT_ROOT}/results/test.csv")
        self.assertTrue(len(train_df) > 0)
        self.assertTrue(len(validate_df) > 0)
        self.assertTrue(len(test_df) > 0)

if __name__ == '__main__':
    unittest.main()