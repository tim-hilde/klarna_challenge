from klarna_challenge.config import *
from klarna_challenge import utils
import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Loads csv file from web or from local drive

    Returns
    -------
    pd.DataFrame
        Raw data
    """
    import pandas as pd
    raw_path = utils.get_raw_path()
    try:
        data = pd.read_csv(f"{raw_path}/raw.csv")
    except:
        data = pd.read_csv("https://file.notion.so/f/f/2b6dea13-478f-4f00-aff1-afd11ed5a03f/f3156a74-df03-415e-9684-f24f099ca195/dataset.csv?id=7e5f2aef-4768-4b75-a3e2-3254ba620fdb&table=block&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&expirationTimestamp=1721916000000&signature=sdn7VQPD7hpHVmTnsSJZxQqLXxiSVdOpypdkiAPy88A&downloadName=dataset.csv", sep=";")
        data.to_csv(f"{raw_path}/raw.csv", index=False)
    return data

def clean_data(data:pd.DataFrame) -> pd.DataFrame:
    """
    Sets correct dtypes and removes columns that contain too many NA value.

    Parameters
    ----------
    data : pd.DataFrame
        Input data

    Returns
    -------
    pd.DataFrame
        Cleaned data
    """
    clean_data = (data
        .astype({col: "category" for col in [
            "default",
            "account_status",
            "account_worst_status_0_3m",
            "account_worst_status_12_24m",
            "account_worst_status_3_6m",
            "account_worst_status_6_12m",
            "merchant_category",
            "merchant_group",
            "name_in_email",
            "status_last_archived_0_24m",
            "status_2nd_last_archived_0_24m",
            "status_3rd_last_archived_0_24m",
            "status_max_archived_0_6_months",
            "status_max_archived_0_12_months",
            "status_max_archived_0_24_months",
            "worst_status_active_inv"
            ]})
        .pipe(lambda _df: _df.drop(columns = _df.columns[data.isna().any()].drop("default"), axis=1))
    )
    return clean_data
