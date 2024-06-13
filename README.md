## DataPrepKit

**DataPrepKit** is a comprehensive Python package designed to simplify and streamline the preprocessing of datasets. Whether you're a data scientist, analyst, or machine learning engineer, DataPrepKit offers a suite of tools to prepare your data efficiently for analysis and modeling.

### Key Features

- **Data Reading**: Seamlessly read data from various file formats including CSV, Excel, and JSON.
- **Data Summary Generation**: Quickly generate descriptive statistics and summaries to understand your data better.
- **Handling Missing Values**: Robust methods to detect, handle, and impute missing values in your dataset.
- **Categorical Data Encoding**: Efficiently encode categorical data using techniques like one-hot encoding and label encoding.
- **Data Normalization and Scaling**: Standardize and normalize your data to ensure it is ready for machine learning models.
- **Outlier Detection and Treatment**: Identify and handle outliers to improve the quality of your data.
- **Automated Data Cleaning**: Perform common data cleaning tasks with simple function calls.
- **User-Friendly API**: Intuitive and easy-to-use functions to make preprocessing quick and straightforward.
- **Extensive Documentation**: Comprehensive documentation and examples to help you get started quickly.

### Installation

You can install DataPrepKit from PyPI using pip:

```bash
pip install dataprepkit
```

### Usage

Here's a quick example to demonstrate how to use DataPrepKit:
```python
import dataprepkit as dpk

# Read data
data = dpk.read_data('data.csv')

# Generate summary
summary = dpk.data_summary.summary(data)
print(summary)

# Handle missing values
data_cleaned = dpk.missing_values.remove_missing(data)

# Encode categorical data
data_encoded = dpk.categorical_encoding.one_hot_encoding(data_cleaned)


# Your data is now ready for analysis and modeling!

```


### Testing
DataPrepKit includes a suite of tests to ensure the reliability and accuracy of its functions. The tests are located in the tests directory. To run the tests, you can use the following command:

```bash
pytest tests
```

You can find this package on Pypi using this link: [DataPrepKitV2](https://pypi.org/project/DataPrepKitV2/2.0/)
