from fastapi import APIRouter, Depends
from API.terminal_repo.repository import Repository
from API.dependencies.repo_dependencies import get_repository
from Core.models.models import (
    GetInterestRateParams,
    GetYieldCurveParams,
    YachooGetHistory,
    YachooSymbol)
from Data.Services.Visualization.ChartServices import ChartServices
from  Core.utils.chart_export import figure_to_png

graph_router = APIRouter(
    prefix="/api/export",
    tags=["Export"]
)


@graph_router.post("/yield-curve")
def export_yield_curve(
    request_info: GetYieldCurveParams,
    repo: Repository = Depends(get_repository)
):
    data = repo.get_yield_curve_data(
        params=request_info
    )

    chart_service = ChartServices()

    chart = chart_service.yield_curve_chart_generation(
        data=data,
        request_info=request_info
    )

    return figure_to_png(chart)


@graph_router.post("/interest-rate")
def export_interest_rate(
    request_info: GetInterestRateParams,
    repo: Repository = Depends(get_repository)
):
    data = repo.get_interest_rate_data(
        params=request_info
    )

    chart_service = ChartServices()

    chart = chart_service.interest_rate_chart_generation(
        data=data,
        request_info=request_info
    )

    return figure_to_png(chart)


@graph_router.post("/candles")
def export_candles(
    request_info: YachooGetHistory,
    repo: Repository = Depends(get_repository)
):
    data = repo.get_history_data(
        params=request_info
    )

    chart_service = ChartServices()

    chart = chart_service.candles_chart_generation(
        data=data,
        request_info=request_info
    )

    return figure_to_png(chart)


@graph_router.post("/financials")
def export_financials(
    request_info: YachooSymbol,
    repo: Repository = Depends(get_repository)
):
    data = repo.get_financials_data(
        symbol=request_info
    )

    chart_service = ChartServices()

    chart = chart_service.financials_chart_generation(
        data=data,
        request_info=request_info
    )

    return figure_to_png(chart)