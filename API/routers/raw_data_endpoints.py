from fastapi import APIRouter, Depends
from API.terminal_repo.repository import Repository
from Core.models.models import YachooSymbol,GetDailyExchangeRateParams,USASpendingResponse,LobbyingResponse,GetUSASpeandingPlusLobbingParams
from API.dependencies.repo_dependencies import get_repository

raw_data_router = APIRouter(
    prefix="/api/raw_data",
    tags=["Raw_Data"],
)

@raw_data_router.get("/daily_exchange_rate_data")
def daily_exchange_rate_data(params: GetDailyExchangeRateParams = Depends(),repo:Repository = Depends(get_repository)):
    data=repo.get_daily_exchange_rate_data(params=params)
    return data


@raw_data_router.get("/balance_sheet_data")
def balance_sheet_data(symbol:YachooSymbol = Depends(),repo:Repository = Depends(get_repository)):
    data=repo.get_balance_sheet_data(symbol=symbol)
    return data

@raw_data_router.get("/usa_spending")
def usa_spending(params:GetUSASpeandingPlusLobbingParams = Depends(),repo:Repository = Depends(get_repository)):
    data=repo.get_usa_spending(params=params)
    return data


@raw_data_router.get("/lobbying_data")
def lobbying_data(params:GetUSASpeandingPlusLobbingParams = Depends(),repo:Repository = Depends(get_repository)):
    data=repo.get_lobbying_data(params=params)
    return data