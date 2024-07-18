# About this project

Repository for the klarna ml engineering challenge.

This case consists of a supervised learning example. The task is to predict the probability of default for the datapoints where the `default` variable is not set. The answer should contain the resulting predictions in a csv file with two columns, `uuid` and `pd` (probability of `default==1`).


| Column Name                         | Column Type |
|-------------------------------------|-------------|
| uuid                                | text        |
| default                             | categorical |
| account_amount_added_12_24m         | numeric     |
| account_days_in_dc_12_24m           | numeric     |
| account_days_in_rem_12_24m          | numeric     |
| account_days_in_term_12_24m         | numeric     |
| account_incoming_debt_vs_paid_0_24m | numeric     |
| account_status                      | categorical |
| account_worst_status_0_3m           | categorical |
| account_worst_status_12_24m         | categorical |
| account_worst_status_3_6m           | categorical |
| account_worst_status_6_12m          | categorical |
| age                                 | numeric     |
| avg_payment_span_0_12m              | numeric     |
| avg_payment_span_0_3m               | numeric     |
| merchant_category                   | categorical |
| merchant_group                      | categorical |
| has_paid                            | boolean     |
| max_paid_inv_0_12m                  | numeric     |
| max_paid_inv_0_24m                  | numeric     |
| name_in_email                       | categorical |
| num_active_div_by_paid_inv_0_12m    | numeric     |
| num_active_inv                      | numeric     |
| num_arch_dc_0_12m                   | numeric     |
| num_arch_dc_12_24m                  | numeric     |
| num_arch_ok_0_12m                   | numeric     |
| num_arch_ok_12_24m                  | numeric     |
| num_arch_rem_0_12m                  | numeric     |
| num_arch_written_off_0_12m          | numeric     |
| num_arch_written_off_12_24m         | numeric     |
| num_unpaid_bills                    | numeric     |
| status_last_archived_0_24m          | categorical |
| status_2nd_last_archived_0_24m      | categorical |
| status_3rd_last_archived_0_24m      | categorical |
| status_max_archived_0_6_months      | categorical |
| status_max_archived_0_12_months     | categorical |
| status_max_archived_0_24_months     | categorical |
| recovery_debt                       | numeric     |
| sum_capital_paid_account_0_12m      | numeric     |
| sum_capital_paid_account_12_24m     | numeric     |
| sum_paid_inv_0_12m                  | numeric     |
| time_hours                          | numeric     |
| worst_status_active_inv             | categorical |


# Getting started

## Prerequisites
The following are prerequisites to run this codebase:
 - Python
 - Poetry


 ## Installation
1. Install the poetry environment
	```sh
	poetry install
	```

# General documentation

## `data` vs `static` directories
The `data` directory is for storing raw data, processed data (produced by this code but not final) and output data.
The contents of these folders should not be tracked by git,
because they may contain sensitive information and may be large in size.

The `static` directory is for static (unchanging) data that is needed for the code to run and is not sensitive,
such as lookup tables. These need to be shared between developers using the code, and should be tracked by git.
