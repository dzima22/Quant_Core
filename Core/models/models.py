from datetime import date
from pydantic import BaseModel,ConfigDict, Field,model_validator
import re
from datetime import date
from typing import Any
from datetime import date
from enum import Enum


class IgnoreExtraModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        populate_by_name=True)

class DailyDate(BaseModel):
    value: date
    @classmethod
    def validate(cls, value: str) -> "DailyDate":
        return cls(value=date.fromisoformat(value))


class PeriodDate(BaseModel):
    value: str

    @classmethod
    def validate_for_frequency(
        cls,
        value: str,
        frequency: "Frequency",
    ) -> "PeriodDate":
        patterns = {
            Frequency.MONTH: r"^\d{4}-(0[1-9]|1[0-2])$",
            Frequency.QUARTER: r"^\d{4}-Q[1-4]$",
            Frequency.YEAR: r"^\d{4}$",
        }

        if not re.fullmatch(patterns[frequency], value):
            raise ValueError(
                f"Invalid period format for frequency '{frequency}'"
            )

        return cls(value=value)



class Variation(str, Enum):
    ANNUAL = "A"
    ENDOFYEAR = "E"


class Frequency(str, Enum):
    DAILY = "D"
    MONTH = "M"
    QUARTER = "Q"
    YEAR = "A"


class InterestRate(str, Enum):
    DFR = "DFR"
    MLFR = "MLFR"
    MRR_FR = "MRR_FR"
    MRR_RT = "MRR_RT"
    MRR_MBR = "MRR_MBR"


class Measure(str, Enum):
    LEVEL = "LEV"
    CHANGE = "CHG"


class YieldCurveInstrument(str, Enum):
    G_N_A = "G_N_A"
    G_N_C = "G_N_C"


class Maturity(str, Enum):
    SR_3M = "SR_3M"
    SR_6M = "SR_6M"
    SR_1Y = "SR_1Y"
    SR_2Y = "SR_2Y"
    SR_5Y = "SR_5Y"
    SR_10Y = "SR_10Y"
    SR_30Y = "SR_30Y"


class GetDailyExchangeRateParams(IgnoreExtraModel):
    currency: str
    start_date: date = Field(alias="startPeriod")
    end_date: date = Field(alias="endPeriod")
    reference_currency: str = "EUR"

class GetPeriodExchangeRateParams(IgnoreExtraModel):
    currency: str
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    reference_currency: str = "EUR"

    variation: Variation = Variation.ANNUAL
    frequency: Frequency

    @model_validator(mode="after")
    def validate_period_format(self):
        patterns = {
            Frequency.MONTH: r"^\d{4}-(0[1-9]|1[0-2])$",
            Frequency.QUARTER: r"^\d{4}-Q[1-4]$",
            Frequency.YEAR: r"^\d{4}$",}
        pattern = patterns[self.frequency]
        for field in ("start_date", "end_date"):
            value = getattr(self, field)
            if not re.fullmatch(pattern, value):
                raise ValueError(
                    f"{field} must be in the correct format "
                    f"for frequency '{self.frequency.value}'")

        return self

class GetBasicFinancialsParams(BaseModel):
    symbol: str

class GetUSASpeandingPlusLobbingParams(BaseModel):
    symbol: str
    from_: str
    to: str 

class YachooSymbol(BaseModel):
    symbol: str

class YachooGetHistory(BaseModel):
    symbol: str
    period: str = "1y"
    interval: str = "1d"

class GetInterestRateParams(IgnoreExtraModel):
    start_date: date = Field(alias="startPeriod")
    end_date: date = Field(alias="endPeriod")

    frequency: Frequency = Frequency.DAILY
    currency: str = "EUR"

    rate: InterestRate = InterestRate.DFR
    measure: Measure = Measure.LEVEL

    @model_validator(mode="after")
    def validate_measure(self):
        if (
            self.rate in {
                InterestRate.MRR_FR,
                InterestRate.MRR_RT,
                InterestRate.MRR_MBR,
            }
            and self.measure == Measure.CHANGE
        ):
            raise ValueError(
                f"measure='CHG' is not available for "
                f"rate='{self.rate.value}'"
            )
        return self


class GetYieldCurveParams(IgnoreExtraModel):
    currency: str = "EUR"

    instrument: YieldCurveInstrument = (
        YieldCurveInstrument.G_N_A
    )

    maturity: Maturity = Maturity.SR_3M

    start_date: date = Field(alias="startPeriod")
    end_date: date = Field(alias="endPeriod")



class ECBObservation(IgnoreExtraModel):
    TIME_PERIOD: str
    value: float | None = None

class USASpendingRecord(IgnoreExtraModel):
    recipientName: str | None = None
    recipientParentName: str | None = None
    totalValue: float | None = None
    actionDate: str | None = None
    awardingAgencyName: str | None = None
    awardingSubAgencyName: str | None = None
    awardDescription: str | None = None
    performanceCountry: str | None = None
    performanceCity: str | None = None
    performanceState: str | None = None
    permalink: str | None = None


class USASpendingResponse(IgnoreExtraModel):
    symbol: str | None = None
    data: list[USASpendingRecord] = Field(default_factory=list)


class LobbyingRecord(IgnoreExtraModel):
    name: str | None = None
    description: str | None = None
    country: str | None = None
    year: int | None = None
    period: str | None = None
    income: float | None = None
    expenses: float | None = None
    documentUrl: str | None = None
    senateId: str | None = None


class LobbyingResponse(IgnoreExtraModel):
    symbol: str | None = None
    data: list[LobbyingRecord] = Field(default_factory=list)

class ValuationMetrics(IgnoreExtraModel):
    marketCapitalization: float | None = None
    enterpriseValue: float | None = None
    peAnnual: float | None = None
    peTTM: float | None = None
    forwardPE: float | None = None
    psAnnual: float | None = None
    psTTM: float | None = None
    pbAnnual: float | None = None
    pbQuarterly: float | None = None
    evEbitdaAnnual: float | None = None
    evEbitdaTTM: float | None = None
    evRevenueAnnual: float | None = None
    evRevenueTTM: float | None = None
    pfcfShareAnnual: float | None = None
    pfcfShareTTM: float | None = None
    pcfShareAnnual: float | None = None
    pcfShareTTM: float | None = None

class ProfitabilityMetrics(IgnoreExtraModel):
    epsAnnual: float | None = None
    epsTTM: float | None = None
    revenuePerShareAnnual: float | None = None
    revenuePerShareTTM: float | None = None
    cashFlowPerShareAnnual: float | None = None
    cashFlowPerShareTTM: float | None = None
    ebitdPerShareAnnual: float | None = None
    ebitdPerShareTTM: float | None = None
    grossMarginAnnual: float | None = None
    grossMarginTTM: float | None = None
    operatingMarginAnnual: float | None = None
    operatingMarginTTM: float | None = None
    pretaxMarginAnnual: float | None = None
    pretaxMarginTTM: float | None = None
    netProfitMarginAnnual: float | None = None
    netProfitMarginTTM: float | None = None
    roeAnnual: float | None = None
    roeTTM: float | None = None
    roaAnnual: float | None = None
    roaTTM: float | None = None
    roiAnnual: float | None = None
    roiTTM: float | None = None

class GrowthMetrics(IgnoreExtraModel):
    revenueGrowth3Y: float | None = None
    revenueGrowth5Y: float | None = None
    revenueGrowthTTMYoy: float | None = None
    revenueGrowthQuarterlyYoy: float | None = None
    epsGrowth3Y: float | None = None
    epsGrowth5Y: float | None = None
    epsGrowthTTMYoy: float | None = None
    epsGrowthQuarterlyYoy: float | None = None
    ebitdaCagr3Y: float | None = None
    ebitdaCagr5Y: float | None = None
    capexCagr3Y: float | None = None
    capexCagr5Y: float | None = None
    focfCagr3Y: float | None = None
    focfCagr5Y: float | None = None

class BalanceSheetMetrics(IgnoreExtraModel):
    bookValuePerShareAnnual: float | None = None
    bookValuePerShareQuarterly: float | None = None
    tangibleBookValuePerShareAnnual: float | None = None
    tangibleBookValuePerShareQuarterly: float | None = None
    currentRatioAnnual: float | None = None
    currentRatioQuarterly: float | None = None
    quickRatioAnnual: float | None = None
    quickRatioQuarterly: float | None = None
    cashPerSharePerShareAnnual: float | None = None
    cashPerSharePerShareQuarterly: float | None = None

totalDebt_equityAnnual: float | None = Field(
    default=None,
    alias="totalDebt/totalEquityAnnual",
)

totalDebt_equityQuarterly: float | None = Field(
    default=None,
    alias="totalDebt/totalEquityQuarterly",
)

longTermDebt_equityAnnual: float | None = Field(
    default=None,
    alias="longTermDebt/equityAnnual",
)

longTermDebt_equityQuarterly: float | None = Field(
    default=None,
    alias="longTermDebt/equityQuarterly",
)

longtermDebtTotalAssetAnnual: float | None = None
longtermDebtTotalAssetQuarterly: float | None = None
longtermDebtTotalCapitalAnnual: float | None = None
longtermDebtTotalCapitalQuarterly: float | None = None
longtermDebtTotalEquityAnnual: float | None = None
longtermDebtTotalEquityQuarterly: float | None = None
netDebtToTotalCapitalAnnual: float | None = None
netDebtToTotalCapitalQuarterly: float | None = None
netDebtToTotalEquityAnnual: float | None = None
netDebtToTotalEquityQuarterly: float | None = None


class DividendMetrics(IgnoreExtraModel):
    dividendPerShareAnnual: float | None = None
    dividendPerShareTTM: float | None = None
    dividendIndicatedAnnual: float | None = None
    currentDividendYieldTTM: float | None = None
    dividendYieldIndicatedAnnual: float | None = None
    payoutRatioAnnual: float | None = None
    payoutRatioTTM: float | None = None
    dividendGrowthRate5Y: float | None = None

class MarketMetrics(IgnoreExtraModel):
    beta: float | None = None

field_52WeekHigh: float | None = Field(
    default=None,
    alias="52WeekHigh",
)

field_52WeekHighDate: str | None = Field(
    default=None,
    alias="52WeekHighDate",
)

field_52WeekLow: float | None = Field(
    default=None,
    alias="52WeekLow",
)

field_52WeekLowDate: str | None = Field(
    default=None,
    alias="52WeekLowDate",
)

field_52WeekPriceReturnDaily: float | None = Field(
    default=None,
    alias="52WeekPriceReturnDaily",
)

yearToDatePriceReturnDaily: float | None = None
monthToDatePriceReturnDaily: float | None = None

field_3MonthPriceReturnDaily: float | None = Field(
    default=None,
    alias="3MonthPriceReturnDaily",
)

field_10DayAverageTradingVolume: float | None = Field(
    default=None,
    alias="10DayAverageTradingVolume",
)

field_3MonthAverageTradingVolume: float | None = Field(
    default=None,
    alias="3MonthAverageTradingVolume",
)


class FinancialSeries(IgnoreExtraModel):
    revenue: list[Any] | None = None
    netIncome: list[Any] | None = None
    eps: list[Any] | None = None
    ebitda: list[Any] | None = None
    ebitPerShare: list[Any] | None = None
    cashFlow: list[Any] | None = None
    freeCashFlow: list[Any] | None = None
    grossMargin: list[Any] | None = None
    operatingMargin: list[Any] | None = None
    netMargin: list[Any] | None = None
    fcfMargin: list[Any] | None = None
    bookValue: list[Any] | None = None
    currentRatio: list[Any] | None = None
    quickRatio: list[Any] | None = None
    payoutRatio: list[Any] | None = None
    pb: list[Any] | None = None
    evEbitda: list[Any] | None = None
    evRevenue: list[Any] | None = None

class FinancialSeriesContainer(IgnoreExtraModel):
    annual: FinancialSeries | None = None

class BasicFinancialsResponse(IgnoreExtraModel):
    valuation: ValuationMetrics
    profitability: ProfitabilityMetrics
    growth: GrowthMetrics
    balance_sheet: BalanceSheetMetrics
    dividends: DividendMetrics
    market: MarketMetrics
    series: FinancialSeries | None = None

class HistoryRecord(BaseModel):
    date: str
    open: float | None = None
    high: float | None = None
    low: float | None = None
    close: float | None = None
    volume: int | None = None
    dividends: float | None = None
    stock_splits: float | None = None

class SeriesRecord(BaseModel):
    date: str
    value: float | None = None

class DataFrameRecord(IgnoreExtraModel):
    date: str
    model_config = ConfigDict(
    extra="allow")