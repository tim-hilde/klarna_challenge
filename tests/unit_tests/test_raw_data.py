from klarna_challenge.data import load_data, clean_data
import pandas as pd
import pytest

@pytest.fixture(scope="session")
def data():
    data = load_data()
    return data

def test_loaded_data(data):
    assert type(data) is pd.DataFrame, "Output is not of type pd.Dataframe"
    assert data.shape == (99976, 43), "Output has wrong shape"

def test_cleaned_data(data):
    cleaned_data = clean_data(data)

    assert type(cleaned_data) is pd.DataFrame, "Output is not of type pd.Dataframe"
    assert cleaned_data.shape == (99976, 28), "Output has wrong shape"

    required_columns = {
        "uuid": "object",
        "default": "category",
        "account_amount_added_12_24m": "int64",
        "age": "int64",
        "merchant_category": "category",
        "merchant_group": "category",
        "has_paid": "bool",
        "max_paid_inv_0_12m": "float64",
        "max_paid_inv_0_24m": "float64",
        "name_in_email": "category",
        "num_active_inv": "int64",
        "num_arch_dc_0_12m": "int64",
        "num_arch_dc_12_24m": "int64",
        "num_arch_ok_0_12m": "int64",
        "num_arch_ok_12_24m": "int64",
        "num_arch_rem_0_12m": "int64",
        "num_unpaid_bills": "int64",
        "status_last_archived_0_24m": "category",
        "status_2nd_last_archived_0_24m": "category",
        "status_3rd_last_archived_0_24m": "category",
        "status_max_archived_0_6_months": "category",
        "status_max_archived_0_12_months": "category",
        "status_max_archived_0_24_months": "category",
        "recovery_debt": "int64",
        "sum_capital_paid_account_0_12m": "int64",
        "sum_capital_paid_account_12_24m": "int64",
        "sum_paid_inv_0_12m": "int64",
        "time_hours": "float64"
    }
    # This line asserts that the DataFrame's columns include at least the keys in the required_columns dictionary.
    assert set(cleaned_data.columns.values).issuperset(set(required_columns.keys()))

    #iterates over each required column and its corresponding type verification function. It checks if the column's data type matches the expected type using the verification function.
    for col_name, expected_type in required_columns.items():
        assert cleaned_data[col_name].dtype == expected_type, \
            f"Column {col_name} failed test {expected_type}. Is {cleaned_data[col_name].dtype}"
