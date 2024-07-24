---
configs:
- config_name: default
  data_files:
  - split: train
    path: "train.csv"
  - split: validate
    path: "validate.csv"
  - split: test
    path: "test.csv"
---

# Dataset Description:

The data is partitioned according to a 75/15/15 train/test/validate split.
Each entry has an abstract (which is the input text for classification), a domain (a label from the list below), and an area (a subdomain of the paper, such as CS -> computer graphics, which takes on one of 134 possible values).
All the attributes are strings.

Domain labels:

    - Computer Science
    - Electrical Engineering
    - Psychology
    - Mechanical Engineering,
    - Civil Engineering
    - Medical Science
    - biochemistry

Dataset overview:

```python
DatasetDict({
    train: Dataset({
        features: ['abstract', 'domain', 'area'],
        num_rows: 32890
    })
    validate: Dataset({
        features: ['abstract', 'domain', 'area'],
        num_rows: 7048
    })
    test: Dataset({
        features: ['abstract', 'domain', 'area'],
        num_rows: 7047
    })
})
```
    
# Copyright notice

Copyright (c) 2017 Kamran Kowsari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this dataset and associated documentation files (the "Dataset"), to deal
in the dataset without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Dataset, and to permit persons to whom the dataset is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Dataset.

If you use this dataset, please cite:

```bibtex
@inproceedings{kowsari2017HDLTex,
  title={HDLTex: Hierarchical Deep Learning for Text Classification},
  author={Kowsari, Kamran and Brown, Donald E and Heidarysafa, Mojtaba and Jafari Meimandi, Kiana and and Gerber, Matthew S and Barnes, Laura E},
  booktitle={Machine Learning and Applications (ICMLA), 2017 16th IEEE International Conference on},
  year={2017},
  organization={IEEE}
}
```

# Related pages

The GitHub repository for the project that produced the original dataset:
<https://github.com/kk7nc/HDLTex>

The raw excel file containing the abstracts, domain labels and area labels is available at:
<https://data.mendeley.com/datasets/9rw3vkcfy4/6>