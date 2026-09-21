from Core.exceptions.exceptions import QuantTerminalException
import sys
from configs.constants import fields_spending,fields_lobbing,VALUATION_FIELDS,PROFITABILITY_FIELDS,GROWTH_FIELDS,BALANCE_SHEET_FIELDS,DIVIDEND_FIELDS,MARKET_FIELDS,SERIES_FIELDS
import pandas as pd 
def parse_ecb(data: dict) -> list[dict]:
    try:
        series_dimensions = data["structure"]["dimensions"]["series"]
        observation_dimensions = data["structure"]["dimensions"]["observation"]
        series_dim_names = [dim["id"] for dim in series_dimensions]
        time_dim = next(
            dim for dim in observation_dimensions
            if dim["id"] == "TIME_PERIOD"
        )

        time_periods = [value["id"] for value in time_dim["values"]]

        result = []

        for series_key, series_data in data["dataSets"][0]["series"].items():
            indexes = map(int, series_key.split(":"))

            series_info = {
                dim_name: series_dimensions[i]["values"][index]["id"]
                for i, (dim_name, index) in enumerate(
                    zip(series_dim_names, indexes)
                )
            }

            for obs_index, observation in series_data["observations"].items():
                period = time_periods[int(obs_index)]
                value = observation[0]

                result.append({
                    **series_info,
                    "TIME_PERIOD": period,
                    "value": value,
                })

        return result
    except Exception as e:
        raise QuantTerminalException(e, sys)

def parse_usaspending(data: dict) -> dict:
    try:
        records = [
            {
                field: record[field]
                for field in fields_spending
                if field in record
            }
            for record in data.get("data", [])
        ]

        return {
            "symbol": data.get("symbol"),
            "data": records,
        }
    except Exception as e:
        raise QuantTerminalException(e, sys)

def parse_lobbying(data: dict) -> dict:
    try:
        return {
            "symbol": data.get("symbol"),
            "data": [
                {
                    field: record[field]
                    for field in fields_lobbing
                    if field in record
                }
                for record in data.get("data", [])
            ],
        }
    except Exception as e:
        raise QuantTerminalException(e, sys)
    
def parse_financial_fields(data: dict, fields: set[str]) -> dict:
    return {
        key: data[key]
        for key in fields
        if key in data
    }

def parse_basic_financials(data: dict) -> dict:
    metric = data.get("metric", {})
    annual = data.get("series", {}).get("annual", {})

    return {
        "valuation": parse_financial_fields(
            metric,
            VALUATION_FIELDS,
        ),
        "profitability": parse_financial_fields(
            metric,
            PROFITABILITY_FIELDS,
        ),
        "growth": parse_financial_fields(
            metric,
            GROWTH_FIELDS,
        ),
        "balance_sheet": parse_financial_fields(
            metric,
            BALANCE_SHEET_FIELDS,
        ),
        "dividends": parse_financial_fields(
            metric,
            DIVIDEND_FIELDS,
        ),
        "market": parse_financial_fields(
            metric,
            MARKET_FIELDS,
        ),
        "series": parse_financial_fields(
            annual,
            SERIES_FIELDS,
        ),
    }
def data_parse_dataframes(df: pd.DataFrame) -> list[dict]:
    try:
        result = []

        for date, values in df.to_dict().items():
            record = {
                "date": date.strftime("%Y-%m-%d")
            }

            for key, value in values.items():
                if pd.isna(value):
                    record[key] = None
                else:
                    record[key] = value

            result.append(record)

        return result

    except Exception as e:
        raise QuantTerminalException(e, sys)

def data_parse_series(series: pd.Series) -> list[dict]:
    try:
        result = []

        for date, value in series.items():
            result.append({
                "date": date.strftime("%Y-%m-%d"),
                "value": None if pd.isna(value) else value
            })

        return result

    except Exception as e:
        raise QuantTerminalException(e, sys)
    
def data_parse_history(df: pd.DataFrame) -> list[dict]:
    try:
        result = []

        for date, values in df.iterrows():
            result.append({
                "date": date.strftime("%Y-%m-%d"),
                "open": None if pd.isna(values["Open"]) else float(values["Open"]),
                "high": None if pd.isna(values["High"]) else float(values["High"]),
                "low": None if pd.isna(values["Low"]) else float(values["Low"]),
                "close": None if pd.isna(values["Close"]) else float(values["Close"]),
                "volume": None if pd.isna(values["Volume"]) else int(values["Volume"]),
                "dividends": None if pd.isna(values["Dividends"]) else float(values["Dividends"]),
                "stock_splits": None if pd.isna(values["Stock Splits"]) else float(values["Stock Splits"])
            })

        return result

    except Exception as e:
        raise QuantTerminalException(e, sys)