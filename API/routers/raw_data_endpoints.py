from fastapi import APIRouter, Depends
from API.terminal_repo.repository import Repository
from Core.configs.models import YachooSymbol,GetDailyExchangeRateParams,GetUSASpeandingPlusLobbingParams
from API.dependencies.repo_dependencies import get_repository
from typing import Annotated
from fastapi import Query

raw_data_router = APIRouter(
    prefix="/api/raw_data",
    tags=["Raw_Data"],
)

@raw_data_router.get("/daily_exchange_rate_data")
def daily_exchange_rate_data(params: Annotated[GetDailyExchangeRateParams, Query()],repo:Repository = Depends(get_repository)):
    data=repo.get_daily_exchange_rate_data(params=params)
    return data


@raw_data_router.get("/balance_sheet_data")
def balance_sheet_data(symbol:Annotated[YachooSymbol, Query()],repo:Repository = Depends(get_repository)):
    data=repo.get_balance_sheet_data(symbol=symbol)
    return data

@raw_data_router.get("/usa_spending")
def usa_spending(params:Annotated[GetUSASpeandingPlusLobbingParams, Query()],repo:Repository = Depends(get_repository)):
    data=repo.get_usa_spending(params=params)
    return data


@raw_data_router.get("/lobbying_data")
def lobbying_data(params:Annotated[GetUSASpeandingPlusLobbingParams, Query()],repo:Repository = Depends(get_repository)):
    data=repo.get_lobbying_data(params=params)
    return data