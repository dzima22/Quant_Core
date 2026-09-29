import sys

import pandas as pd

from Core.exceptions.exceptions import QuantTerminalException
from Core.models.response_models import (
USASpendingResponse,
LobbyingResponse,
ValuationMetrics,
ProfitabilityMetrics,
GrowthMetrics,
BalanceSheetMetrics,
DividendMetrics,
MarketMetrics,
FinancialSeries,
BasicFinancialsResponse,
HistoryRecord,
SeriesRecord,
)

def parse_ecb(data: dict) -> list[dict]:
    try:
            series_dimensions = data["structure"]["dimensions"]["series"]
            observation_dimensions = data["structure"]["dimensions"]["observation"]
            series_dim_names = [
                dim["id"]
                for dim in series_dimensions
            ]

            time_dim = next(
                dim
                for dim in observation_dimensions
                if dim["id"] == "TIME_PERIOD"
            )

            time_periods = [
                value["id"]
                for value in time_dim["values"]
            ]

            result = []

            for series_key, series_data in data["dataSets"][0]["series"].items():
                indexes = map(
                    int,
                    series_key.split(":")
                )

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
        response = USASpendingResponse.model_validate(data)
        return response.model_dump()
    except Exception as e:
        raise QuantTerminalException(e, sys)


def parse_lobbying(data: dict) -> dict:
    try:
        response = LobbyingResponse.model_validate(data)
        return response.model_dump()

    except Exception as e:
        raise QuantTerminalException(e, sys)


def parse_basic_financials(data: dict) -> dict:
    try:
        metric = data.get("metric", {})
        annual = data.get("series", {}).get("annual", {})

        result = BasicFinancialsResponse(
        valuation=ValuationMetrics.model_validate(metric),
        profitability=ProfitabilityMetrics.model_validate(metric),
        growth=GrowthMetrics.model_validate(metric),
        balance_sheet=BalanceSheetMetrics.model_validate(metric),
        dividends=DividendMetrics.model_validate(metric),
        market=MarketMetrics.model_validate(metric),
        series=FinancialSeries.model_validate(annual))

        return result.model_dump(
        by_alias=True)

    except Exception as e:
        raise QuantTerminalException(e, sys)


def data_parse_dataframes(df: pd.DataFrame) -> list[dict]:
    try:
        result = []
        for date, values in df.to_dict().items():
            record = {"date": date.strftime("%Y-%m-%d")}
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
            record = SeriesRecord(
                date=date.strftime("%Y-%m-%d"),
                value=None if pd.isna(value) else value,)
            result.append(
                record.model_dump()
            )

        return result
    except Exception as e:
        raise QuantTerminalException(e, sys)


def data_parse_history(df: pd.DataFrame) -> list[dict]:
    try:
        result = []

        for date, values in df.iterrows():
            record = HistoryRecord(
                date=date.strftime("%Y-%m-%d"),
                open=None if pd.isna(values["Open"]) else float(values["Open"]),
                high=None if pd.isna(values["High"]) else float(values["High"]),
                low=None if pd.isna(values["Low"]) else float(values["Low"]),
                close=None if pd.isna(values["Close"]) else float(values["Close"]),
                volume=None if pd.isna(values["Volume"]) else int(values["Volume"]),
                dividends=None if pd.isna(values["Dividends"]) else float(values["Dividends"]),
                stock_splits=None if pd.isna(values["Stock Splits"]) else float(values["Stock Splits"]),
            )

            result.append(record.model_dump())

        return result

    except Exception as e:
        raise QuantTerminalException(e, sys)