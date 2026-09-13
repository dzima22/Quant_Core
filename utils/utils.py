from Core.exceptions.exceptions import QuantTerminalException
import sys
def parse_ecb(data: dict) -> list[dict]:
    try:
        series_dimensions = data["structure"]["dimensions"]["series"]
        observation_dimensions = data["structure"]["dimensions"]["observation"]
        series_dim_names = [dim["id"] for dim in series_dimensions]
        time_dim = next(
            dim for dim in observation_dimensions
            if dim["id"] == "TIME_PERIOD"
        )

        time_periods = [value["id"] for value in time_dim["values"]]

        result = []

        for series_key, series_data in data["dataSets"][0]["series"].items():
            indexes = map(int, series_key.split(":"))

            series_info = {
                dim_name: series_dimensions[i]["values"][index]["id"]
                for i, (dim_name, index) in enumerate(
                    zip(series_dim_names, indexes)
                )
            }

            for obs_index, observation in series_data["observations"].items():
                period = time_periods[int(obs_index)]
                value = observation[0]

                result.append({
                    **series_info,
                    "TIME_PERIOD": period,
                    "value": value,
                })

        return result
    except Exception as e:
        raise QuantTerminalException(e, sys)