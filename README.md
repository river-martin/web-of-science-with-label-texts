# Web of Science with Label Texts

The dataset produced by this project is available at <https://huggingface.co/datasets/river-martin/web-of-science-with-label-texts>.

## Preqrequisites

Download the `WebOfScience.zip` from <https://data.mendeley.com/datasets/9rw3vkcfy4/6> and extract it to `data/`, to produce the following directory structure:
    - data/
        - WebOfScience/
            -Meta-data/
                - Data.xlsx

## Installation

Create a virtual environment for Python 3.10, activate it and then run:

```bash
# The -e flag makes the installed package editable
pip install -e .
```

## Testing

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Execution

```bash
python src/dataset_splitter/restructure_data.py
```