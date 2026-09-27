from Core.exceptions.exceptions import QuantTerminalException
import sys
from Core.models.models import GetInterestRateParams,GetYieldCurveParams,YachooGetHistory,YachooSymbol
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from datetime import datetime
from matplotlib.figure import Figure
from Core.configs.constants import METRICS_FOR_GRAPH
import numpy as np


class ChartServices:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise QuantTerminalException(e, sys)

    
    def yield_curve_chart_generation(
        self,
        data: list[dict],
        request_info: GetYieldCurveParams
    ) -> Figure:
        try:
            fig, ax = plt.subplots(figsize=(14, 7))

            dates = [
                datetime.strptime(item["TIME_PERIOD"], "%Y-%m-%d")
                for item in data
            ]

            values = [
                item["value"]
                for item in data
            ]

            ax.plot(
                dates,
                values,
                linewidth=2.5
            )

            ax.set_title(
                f"Yield Curve for {request_info.instrument} instrument, "
                f"maturity: {request_info.maturity} in {request_info.currency}"
            )

            ax.set_xlabel("Date")
            ax.set_ylabel("Yield (%)")

            ax.xaxis.set_major_formatter(
                mdates.DateFormatter("%Y-%m-%d")
            )

            # Remove grid
            ax.grid(False)

            # Remove all borders
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.spines["left"].set_visible(False)

            ax.tick_params(
                axis="both",
                which="both",
                length=0
            )

            fig.autofmt_xdate()

            plt.tight_layout()

            return fig

        except Exception as e:
            raise QuantTerminalException(e, sys)

        
    def interest_rate_chart_generation(self,data:list[dict],request_info:GetInterestRateParams)->Figure:
        try:
            fig, ax = plt.subplots(figsize=(14, 7))

            dates = [
                datetime.strptime(item["TIME_PERIOD"], "%Y-%m-%d")
                for item in data]

            values = [
                item["value"]
                for item in data]

            ax.plot(dates, values,linewidth=2.5)

            ax.set_title(
                f"{request_info.currency} Interest Rate"
            )
            ax.set_xlabel("Date")
            ax.set_ylabel("Interest Rate (%)")

            ax.xaxis.set_major_formatter(
                mdates.DateFormatter("%Y-%m-%d")
            )

            fig.autofmt_xdate()
            ax.grid(False)

            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.spines["left"].set_visible(False)


            plt.tight_layout()

            return fig

        except Exception as e:
            raise QuantTerminalException(e, sys)

        
    def candles_chart_generation(
        self,
        data: list[dict],
        request_info: YachooGetHistory
    ) -> Figure:
        try:
            fig, ax = plt.subplots(figsize=(14, 7))

            # Dark theme
            fig.patch.set_facecolor("#0b0f14")
            ax.set_facecolor("#0b0f14")

            # Candle width
            if request_info.interval in ["1d", "5d"]:
                candle_width = 0.6
            elif request_info.interval in ["1mo", "3mo"]:
                candle_width = 20
            elif request_info.interval in ["6mo", "1y"]:
                candle_width = 30
            elif request_info.interval in ["2y", "5y"]:
                candle_width = 50

            dates = []

            for item in data:
                date = datetime.strptime(
                    item["date"],
                    "%Y-%m-%d"
                )

                dates.append(date)

                x = mdates.date2num(date)

                open_price = item["open"]
                high_price = item["high"]
                low_price = item["low"]
                close_price = item["close"]

                # Candle color
                if close_price >= open_price:
                    candle_color = "#00c853"
                else:
                    candle_color = "#ff1744"

                # Wick
                ax.plot(
                    [x, x],
                    [low_price, high_price],
                    color=candle_color,
                    linewidth=1
                )

                # Body
                body_bottom = min(open_price, close_price)
                body_height = abs(close_price - open_price)

                rectangle = Rectangle(
                    (
                        x - candle_width / 2,
                        body_bottom
                    ),
                    candle_width,
                    body_height if body_height > 0 else 0.01,
                    facecolor=candle_color,
                    edgecolor=candle_color,
                    linewidth=0.8
                )

                ax.add_patch(rectangle)

            # X axis
            ax.xaxis_date()

            # Number of dates displayed on X axis
            if request_info.period in ["1d", "5d"]:
                number_of_ticks = 5

            elif request_info.period == "1mo":
                number_of_ticks = 6

            elif request_info.period == "3mo":
                number_of_ticks = 10

            elif request_info.period == "6mo":
                number_of_ticks = 20

            elif request_info.period == "1y":
                number_of_ticks = 30

            elif request_info.period == "2y":
                number_of_ticks = 50

            elif request_info.period == "5y":
                number_of_ticks = 60
            else:
                number_of_ticks = 5

            # Select dates evenly across the whole period
            if len(dates) <= number_of_ticks:
                tick_dates = dates
            else:
                tick_indices = np.linspace(
                    0,
                    len(dates) - 1,
                    number_of_ticks,
                    dtype=int
                )

                tick_dates = [
                    dates[i]
                    for i in tick_indices
                ]

            ax.set_xticks(tick_dates)

            # Date format
            if request_info.interval in ["1mo", "3mo","6mo","1y","2y","5y"]:
                formatter = mdates.DateFormatter("%b %Y")
            else:
                formatter = mdates.DateFormatter("%b %d")

            ax.xaxis.set_major_formatter(formatter)

            # Tick labels
            ax.tick_params(
                axis="both",
                colors="white",
                length=0
            )

            plt.setp(
                ax.get_xticklabels(),
                rotation=0,
                ha="center"
            )

            # Labels
            ax.set_xlabel(
                "Date",
                color="white"
            )

            ax.set_ylabel(
                "Price",
                color="white"
            )

            # Title
            ax.set_title(
                f"{request_info.symbol} — "
                f"{request_info.period} / {request_info.interval}",
                color="white",
                fontsize=15,
                fontweight="bold"
            )

            # Remove borders
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.spines["left"].set_visible(False)

            # Subtle grid
            ax.grid(
                True,
                color="#252a30",
                linewidth=0.5,
                alpha=0.5
            )

            plt.tight_layout()

            return fig

        except Exception as e:
            raise QuantTerminalException(e, sys)


        
    def financials_chart_generation(self,data:list[dict],request_info:YachooSymbol)->Figure:
        try:
            rows = []

            for item in data:
                row = [item["date"]]

                for key in METRICS_FOR_GRAPH:
                    value = item.get(key)

                    if value is None:
                        row.append("-")
                    elif key == "Diluted EPS":
                        row.append(f"{value:.2f}")
                    else:
                        row.append(f"{value / 1_000_000_000:.2f} B")

                rows.append(row)

            fig, ax = plt.subplots(figsize=(14, 5))

            ax.axis("off")

            table = ax.table(
                cellText=rows,
                colLabels=["Date"] + list(METRICS_FOR_GRAPH.values()),
                loc="center",
                cellLoc="center"
            )

            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1, 2.0)

            number_of_columns = len(METRICS_FOR_GRAPH) + 1

            # Header
            for col in range(number_of_columns):
                cell = table[(0, col)]
                cell.set_text_props(
                    weight="bold",
                    fontsize=10
                )
                cell.set_linewidth(0.8)

            # Body
            for row in range(1, len(rows) + 1):
                for col in range(number_of_columns):
                    cell = table[(row, col)]
                    cell.set_linewidth(0.5)

                    if row % 2 == 0:
                        cell.set_facecolor("#F5F5F5")


            ax.set_title(
                f"{request_info.symbol} Financial Summary",
                fontsize=16,
                fontweight="bold",
                pad=20
            )

            plt.tight_layout()

            return fig

        except Exception as e:
            raise QuantTerminalException(e, sys)