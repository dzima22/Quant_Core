from fastapi import APIRouter, Depends
from API.terminal_repo.repository import Repository
from Core.models.request_models import (
    YachooSymbol,
    GetDailyExchangeRateParams,
    GetUSASpeandingPlusLobbingParams,
    GetPeriodExchangeRateParams,
    YachooGetHistory,
    GetYieldCurveParams,
    GetInterestRateParams,
)
from API.dependencies.repo_dependencies import get_repository

raw_data_router = APIRouter(
    prefix="/api/raw_data",
    tags=["Raw_Data"],
)


@raw_data_router.get("/daily_exchange_rate_data")
def daily_exchange_rate_data(
    params: GetDailyExchangeRateParams = Depends(),
    repo: Repository = Depends(get_repository),
):
    data = repo.get_daily_exchange_rate_data(params=params)
    return data


@raw_data_router.get("/exchange_rate_data")
def exchange_rate_data(
    params: GetPeriodExchangeRateParams = Depends(),
    repo: Repository = Depends(get_repository),
):
    data = repo.get_exchange_rate_data(params=params)
    return data


@raw_data_router.get("/balance_sheet_data")
def balance_sheet_data(
    symbol: YachooSymbol = Depends(), repo: Repository = Depends(get_repository)
):
    data = repo.get_balance_sheet_data(symbol=symbol)
    return data


@raw_data_router.get("/usa_spending")
def usa_spending(
    params: GetUSASpeandingPlusLobbingParams = Depends(),
    repo: Repository = Depends(get_repository),
):
    data = repo.get_usa_spending(params=params)
    return data


@raw_data_router.get("/lobbying_data")
def lobbying_data(
    params: GetUSASpeandingPlusLobbingParams = Depends(),
    repo: Repository = Depends(get_repository),
):
    data = repo.get_lobbying_data(params=params)
    return data


@raw_data_router.get("/cashflow_data")
def cashflow_data(
    symbol: YachooSymbol = Depends(), repo: Repository = Depends(get_repository)
):
    data = repo.get_cashflow_data(symbol=symbol)
    return data


@raw_data_router.get("/dividends_data")
def dividends_data(
    symbol: YachooSymbol = Depends(), repo: Repository = Depends(get_repository)
):
    data = repo.get_dividents_data(symbol=symbol)
    return data


@raw_data_router.get("/history_data")
def history_data(
    params: YachooGetHistory = Depends(), repo: Repository = Depends(get_repository)
):
    data = repo.get_history_data(params=params)
    return data


@raw_data_router.get("/financials_data")
def financials_data(
    symbol: YachooSymbol = Depends(), repo: Repository = Depends(get_repository)
):
    data = repo.get_financials(symbol=symbol)
    return data


@raw_data_router.get("/yield_curve")
def yield_curve_data(
    params: GetYieldCurveParams = Depends(), repo: Repository = Depends(get_repository)
):
    data = repo.get_yield_curve_data(params=params)
    return data


@raw_data_router.get("/interest_rate")
def interest_rate_data(
    params: GetInterestRateParams = Depends(),
    repo: Repository = Depends(get_repository),
):
    data = repo.get_interest_rate_data(params=params)
    return data
