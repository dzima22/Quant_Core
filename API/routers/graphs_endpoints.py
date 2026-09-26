from fastapi import APIRouter, Depends
from io import BytesIO
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from API.terminal_repo.repository import Repository
from Core.configs.models import GetInterestRateParams,GetYieldCurveParams,YachooGetHistory,YachooSymbol,GetDailyExchangeRateParams
from API.dependencies.repo_dependencies import get_repository


graph_router = APIRouter(
    prefix="/api/graphs",
    tags=["Graphs"],)

@graph_router.post("/yield-curve")
def yield_curve(request_info:GetYieldCurveParams,repo:Repository = Depends(get_repository)):
    chart=repo.yield_curve(request_info=request_info)
    buffer = BytesIO()
    chart.savefig(buffer, format="png")
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/png")

@graph_router.post("/interest-rate")
def interest_rate(request_info:GetInterestRateParams,repo:Repository = Depends(get_repository)):
    chart=repo.interest_rate(request_info=request_info)
    buffer = BytesIO()
    chart.savefig(buffer, format="png")
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/png")

@graph_router.post("/candles")
def candles(request_info:YachooGetHistory,repo:Repository = Depends(get_repository)):
    chart=repo.candles(request_info=request_info)
    buffer = BytesIO()
    chart.savefig(buffer, format="png")
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/png")

@graph_router.post("/financials_table")
def main_financials(request_info:YachooSymbol,repo:Repository = Depends(get_repository)):
    chart=repo.main_financials(request_info=request_info)
    buffer = BytesIO()
    chart.savefig(buffer, format="png")
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/png")