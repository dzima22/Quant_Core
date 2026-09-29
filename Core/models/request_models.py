from Core.models.models import IgnoreExtraModel
from datetime import date
import re
from enums import Variation,Frequency,InterestRate,YieldCurveInstrument,Measure,Maturity
from pydantic import Field,model_validator

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

class GetBasicFinancialsParams(IgnoreExtraModel):
    symbol: str

class GetUSASpeandingPlusLobbingParams(IgnoreExtraModel):
    symbol: str
    from_: str
    to: str 

class YachooSymbol(IgnoreExtraModel):
    symbol: str

class YachooGetHistory(IgnoreExtraModel):
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

