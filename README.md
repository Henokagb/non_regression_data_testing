# non_regression_data_testing

Non-regression black box tests

This script compares all rows of two tables to identify unexpected changes, missing or additional rows, value differences, etc.

## Tools

- [Poetry](https://python-poetry.org/docs/) – for Python environment and dependency management  
- [DuckDB](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct) – for local test databases  
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) – for accessing BigQuery setting up bigquery env in command line

## Setup

### Install dependencies

```bash
poetry install
```

### Activate the virtual environment

```bash
poetry shell
```

## How to use it

### Using DuckDB

1. Generate sample tables:

```bash
./generate_sample_duckdb.sh
```
It will create the file: example.duckdb

2. Set environment variables:

```bash
export DB="duckdb"
export DUCKDBPATH="example.duckdb"
```

### Using BigQuery

1. Generate sample tables:

```bash
./generate_sample_duckdb.sh your-project-id dataset1.table1 dataset2.table2
```

2. Set environment variables:

```bash
export DB="bigquery"
export BQ_PROJECT_ID="your-project-id"
export BQ_TABLE1="dataset1.table1"
export BQ_TABLE2="dataset2.table2"
```

**Note!!!:** For bigquery, I did not test the script on a real project since the free tiers needs a billing account to insert data. The script needs to be improved for this part.

## Run the script

```bash
python my_script/main.py [--limit LIMIT] [--pk-cols PK_COLS] [--ignore-cols COL1,COL2] table1 table2
```

### Options

- `--limit`: maximum number of differences to display
- `--pk-cols`: primary key column
- `--ignore-cols`: comma-separated list of columns to ignore
- `-h`, `--help`: show help message

### Example

```bash
python my_script/main.py --pk-cols id --ignore-cols updated_at dataset1.table1 dataset2.table2
```