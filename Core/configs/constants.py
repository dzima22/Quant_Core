import os 
FINHUB_BASE_URL= "https://finnhub.io/api/v1"
FINHUB_WEBSOCKET_URL="wss://ws.finnhub.io"
FINHUB_WEBSOCKET_FINAL_URL=f"{FINHUB_WEBSOCKET_URL}?token={os.getenv('FINNHUB_API_KEY')}"
ECB_BASE_URL="https://data-api.ecb.europa.eu/service/data"
fields_spending = [
        "recipientName",
        "recipientParentName",
        "totalValue",
        "actionDate",
        "awardingAgencyName",
        "awardingSubAgencyName",
        "awardDescription",
        "performanceCountry",
        "performanceCity",
        "performanceState",
        "permalink",]
fields_lobbing = [
        "name",
        "description",
        "country",
        "year",
        "period",
        "income",
        "expenses",
        "documentUrl",
        "senateId",]

VALUATION_FIELDS = [
    "marketCapitalization",
    "enterpriseValue",
    "peAnnual",
    "peTTM",
    "forwardPE",
    "psAnnual",
    "psTTM",
    "pbAnnual",
    "pbQuarterly",
    "evEbitdaAnnual",
    "evEbitdaTTM",
    "evRevenueAnnual",
    "evRevenueTTM",
    "pfcfShareAnnual",
    "pfcfShareTTM",
    "pcfShareAnnual",
    "pcfShareTTM",]


PROFITABILITY_FIELDS = [
    "epsAnnual",
    "epsTTM",
    "revenuePerShareAnnual",
    "revenuePerShareTTM",
    "cashFlowPerShareAnnual",
    "cashFlowPerShareTTM",
    "ebitdPerShareAnnual",
    "ebitdPerShareTTM",
    "grossMarginAnnual",
    "grossMarginTTM",
    "operatingMarginAnnual",
    "operatingMarginTTM",
    "pretaxMarginAnnual",
    "pretaxMarginTTM",
    "netProfitMarginAnnual",
    "netProfitMarginTTM",
    "roeAnnual",
    "roeTTM",
    "roaAnnual",
    "roaTTM",
    "roiAnnual",
    "roiTTM",]


GROWTH_FIELDS = [
    "revenueGrowth3Y",
    "revenueGrowth5Y",
    "revenueGrowthTTMYoy",
    "revenueGrowthQuarterlyYoy",
    "epsGrowth3Y",
    "epsGrowth5Y",
    "epsGrowthTTMYoy",
    "epsGrowthQuarterlyYoy",
    "ebitdaCagr3Y",
    "ebitdaCagr5Y",
    "capexCagr3Y",
    "capexCagr5Y",
    "focfCagr3Y",
    "focfCagr5Y",]


BALANCE_SHEET_FIELDS = [
    "bookValuePerShareAnnual",
    "bookValuePerShareQuarterly",
    "tangibleBookValuePerShareAnnual",
    "tangibleBookValuePerShareQuarterly",
    "currentRatioAnnual",
    "currentRatioQuarterly",
    "quickRatioAnnual",
    "quickRatioQuarterly",
    "cashPerSharePerShareAnnual",
    "cashPerSharePerShareQuarterly",
    "totalDebt/totalEquityAnnual",
    "totalDebt/totalEquityQuarterly",
    "longTermDebt/equityAnnual",
    "longTermDebt/equityQuarterly",
    "longtermDebtTotalAssetAnnual",
    "longtermDebtTotalAssetQuarterly",
    "longtermDebtTotalCapitalAnnual",
    "longtermDebtTotalCapitalQuarterly",
    "longtermDebtTotalEquityAnnual",
    "longtermDebtTotalEquityQuarterly",
    "netDebtToTotalCapitalAnnual",
    "netDebtToTotalCapitalQuarterly",
    "netDebtToTotalEquityAnnual",
    "netDebtToTotalEquityQuarterly",]

DIVIDEND_FIELDS = [
    "dividendPerShareAnnual",
    "dividendPerShareTTM",
    "dividendIndicatedAnnual",
    "currentDividendYieldTTM",
    "dividendYieldIndicatedAnnual",
    "payoutRatioAnnual",
    "payoutRatioTTM",
    "dividendGrowthRate5Y",]


MARKET_FIELDS = [
    "beta",
    "52WeekHigh",
    "52WeekHighDate",
    "52WeekLow",
    "52WeekLowDate",
    "52WeekPriceReturnDaily",
    "yearToDatePriceReturnDaily",
    "monthToDatePriceReturnDaily",
    "3MonthPriceReturnDaily",
    "10DayAverageTradingVolume",
    "3MonthAverageTradingVolume",]


SERIES_FIELDS = [
    "revenue",
    "netIncome",
    "eps",
    "ebitda",
    "ebitPerShare",
    "cashFlow",
    "freeCashFlow",
    "grossMargin",
    "operatingMargin",
    "netMargin",
    "fcfMargin",
    "bookValue",
    "currentRatio",
    "quickRatio",
    "payoutRatio",
    "pb",
    "evEbitda",
    "evRevenue",]

METRICS_FOR_GRAPH = {
    "Total Revenue": "Revenue",
    "Gross Profit": "Gross Profit",
    "Operating Income": "Operating Income",
    "EBITDA": "EBITDA",
    "Net Income": "Net Income",
    "Diluted EPS": "Diluted EPS",
}