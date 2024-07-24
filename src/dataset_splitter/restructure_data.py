import pandas as pd
from dataset_splitter.config import PROJECT_ROOT

def remove_intro_and_trailing_whitespace(text):
    return text.lstrip().rstrip()

def prepare_datasets():
    dataset_df = pd.read_excel(f"{PROJECT_ROOT}/data/WebOfScience/Meta-data/Data.xlsx")
    columns_to_keep = ["Abstract", "Domain", "area"]
    dataset_df = dataset_df[columns_to_keep].dropna()
    dataset_df["abstract"] = dataset_df["Abstract"]
    dataset_df['domain'] = dataset_df['Domain'].apply(remove_intro_and_trailing_whitespace)
    dataset_df['area'] = dataset_df['area'].apply(remove_intro_and_trailing_whitespace)
    dataset_df = dataset_df[["abstract", "domain", "area"]]
    dataset_df = dataset_df.dropna()

    # Split the dataset into train, validate and test datasets
    original_df = dataset_df.copy()
    train_df = dataset_df.sample(frac=0.7, random_state=42)
    dataset_df = dataset_df.drop(train_df.index)
    validate_df = dataset_df.sample(frac=0.5, random_state=42)
    test_df = dataset_df.drop(validate_df.index)
    assert len(original_df) == len(train_df) + len(validate_df) + len(test_df)

    return train_df, validate_df, test_df

def write_datasets_to_json():
    train_df, validate_df, test_df = prepare_datasets()
    train_df.to_csv(f"{PROJECT_ROOT}/results/train.csv", index=False)
    validate_df.to_csv(f"{PROJECT_ROOT}/results/validate.csv", index=False)
    test_df.to_csv(f"{PROJECT_ROOT}/results/test.csv", index=False)

if __name__ == "__main__":
    write_datasets_to_json()