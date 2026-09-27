from fastapi import APIRouter, Depends
from API.terminal_repo.repository import Repository
from API.dependencies.repo_dependencies import get_repository
from Core.models.models import (
    GetInterestRateParams,
    GetYieldCurveParams,
    YachooGetHistory,
    YachooSymbol)
from Data.Visualization.ChartServices import ChartServices
from  Core.utils.chart_export import figure_to_png
from API.dependencies.chart_dependencies import get_chart_service
from Data.Services.DataService import DataService
from API.dependencies.data_dependencies import get_data_service

graph_router = APIRouter(
    prefix="/api/export",
    tags=["Export"]
)


@graph_router.post("/yield-curve")
def export_yield_curve(
    request_info: GetYieldCurveParams,
    repo: DataService = Depends(get_data_service),
    chart_service: ChartServices = Depends(get_chart_service)):
    data = repo.data_parse_yield_curve(params=request_info)
    chart = chart_service.yield_curve_chart_generation(
        data=data,
        request_info=request_info
    )

    return figure_to_png(chart)


@graph_router.post("/interest-rate")
def export_interest_rate(
    request_info: GetInterestRateParams,
    repo: DataService = Depends(get_data_service),
    chart_service: ChartServices = Depends(get_chart_service)):
    data = repo.data_parse_interest_rate(params=request_info)
    chart = chart_service.interest_rate_chart_generation(
        data=data,
        request_info=request_info)

    return figure_to_png(chart)


@graph_router.post("/candles")
def export_candles(
    request_info: YachooGetHistory,
    repo: DataService = Depends(get_data_service),
    chart_service: ChartServices = Depends(get_chart_service)):
    data = repo.data_parse_history(params=request_info)
    chart = chart_service.candles_chart_generation(
        data=data,
        request_info=request_info)

    return figure_to_png(chart)


@graph_router.post("/financials")
def export_financials(
    request_info: YachooSymbol,
    repo: DataService = Depends(get_data_service),
    chart_service: ChartServices = Depends(get_chart_service)):
    data = repo.data_parse_financials_yachoo(symbol=request_info)
    chart = chart_service.financials_chart_generation(
        data=data,
        request_info=request_info)

    return figure_to_png(chart)