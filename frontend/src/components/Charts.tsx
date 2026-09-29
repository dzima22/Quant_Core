import { useEffect, useRef } from "react";
import {
    createChart,
    ColorType,
    CandlestickSeries,
    LineSeries,
} from "lightweight-charts";
import type { Time } from "lightweight-charts";

export type Point = {
    time: string;
    value: number;
};

function formatChartDate(time: Time): string {
    let date: Date;

    if (typeof time === "string") {
        date = new Date(`${time}T00:00:00Z`);
    } else if (typeof time === "number") {
        date = new Date(time * 1000);
    } else {
        date = new Date(
            Date.UTC(
                time.year,
                time.month - 1,
                time.day
            )
        );
    }

    if (Number.isNaN(date.getTime())) {
        return "";
    }

    return date.toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
    });
}

function normalizeLineData(data: Point[]) {
    return data
        .filter(
            (x) =>
                x.time &&
                Number.isFinite(x.value)
        )
        .sort(
            (a, b) =>
                new Date(a.time).getTime() -
                new Date(b.time).getTime()
        )
        .filter(
            (item, index, array) =>
                index === 0 ||
                item.time !== array[index - 1].time
        )
        .map((x) => ({
            time: x.time as Time,
            value: x.value,
        }));
}

function normalizeCandleData(
    data: {
        time: string;
        open: number;
        high: number;
        low: number;
        close: number;
    }[]
) {
    return data
        .filter(
            (x) =>
                x.time &&
                Number.isFinite(x.open) &&
                Number.isFinite(x.high) &&
                Number.isFinite(x.low) &&
                Number.isFinite(x.close)
        )
        .sort(
            (a, b) =>
                new Date(a.time).getTime() -
                new Date(b.time).getTime()
        )
        .filter(
            (item, index, array) =>
                index === 0 ||
                item.time !== array[index - 1].time
        )
        .map((x) => ({
            time: x.time as Time,
            open: x.open,
            high: x.high,
            low: x.low,
            close: x.close,
        }));
}

export function LineChart({
    data,
    height = 440,
    format,
}: {
    data: Point[];
    height?: number;
    format?: (n: number) => string;
}) {
    const ref = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (!ref.current) return;

        const chart = createChart(ref.current, {
            width: ref.current.clientWidth,
            height,

            layout: {
                background: {
                    type: ColorType.Solid,
                    color: "#0b0f14",
                },
                textColor: "#91a4b7",
            },

            grid: {
                vertLines: {
                    color: "#18212a",
                },
                horzLines: {
                    color: "#18212a",
                },
            },

            rightPriceScale: {
                borderColor: "#25313b",
            },

            timeScale: {
                borderColor: "#25313b",

                tickMarkFormatter: (time: Time) => {
                    return formatChartDate(time);
                },
            },

            localization: {
                priceFormatter: format,

                // IMPORTANT:
                // This controls the date shown when
                // hovering over the chart.
                timeFormatter: (time: Time) => {
                    return formatChartDate(time);
                },
            },
        });

        const series = chart.addSeries(LineSeries, {
            color: "#00d084",
            lineWidth: 2,
        });

        const normalizedData = normalizeLineData(data);

        series.setData(normalizedData);

        chart.timeScale().fitContent();

        const resizeObserver = new ResizeObserver(() => {
            if (!ref.current) return;

            chart.applyOptions({
                width: ref.current.clientWidth,
            });
        });

        resizeObserver.observe(ref.current);

        return () => {
            resizeObserver.disconnect();
            chart.remove();
        };
    }, [data, height, format]);

    return <div className="chart" ref={ref} />;
}


export function CandleChart({
    data,
    height = 500,
}: {
    data: {
        time: string;
        open: number;
        high: number;
        low: number;
        close: number;
    }[];
    height?: number;
}) {
    const ref = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (!ref.current) return;

        const chart = createChart(ref.current, {
            width: ref.current.clientWidth,
            height,

            layout: {
                background: {
                    type: ColorType.Solid,
                    color: "#0b0f14",
                },
                textColor: "#91a4b7",
            },

            grid: {
                vertLines: {
                    color: "#18212a",
                },
                horzLines: {
                    color: "#18212a",
                },
            },

            rightPriceScale: {
                borderColor: "#25313b",
            },

            timeScale: {
                borderColor: "#25313b",

                tickMarkFormatter: (time: Time) => {
                    return formatChartDate(time);
                },
            },

            localization: {
                // IMPORTANT:
                // This controls the date shown on hover.
                timeFormatter: (time: Time) => {
                    return formatChartDate(time);
                },
            },
        });

        const series = chart.addSeries(CandlestickSeries, {
            upColor: "#00c853",
            downColor: "#ff1744",
            borderVisible: false,
            wickUpColor: "#00c853",
            wickDownColor: "#ff1744",
        });

        const normalizedData = normalizeCandleData(data);

        series.setData(normalizedData);

        chart.timeScale().fitContent();

        const resizeObserver = new ResizeObserver(() => {
            if (!ref.current) return;

            chart.applyOptions({
                width: ref.current.clientWidth,
            });
        });

        resizeObserver.observe(ref.current);

        return () => {
            resizeObserver.disconnect();
            chart.remove();
        };
    }, [data, height]);

    return <div className="chart" ref={ref} />;
}