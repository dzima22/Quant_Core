from io import BytesIO
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt


def figure_to_png(chart):
    buffer = BytesIO()
    try:
        chart.savefig(buffer, format="png", bbox_inches="tight")

        buffer.seek(0)

        return StreamingResponse(
            buffer,
            media_type="image/png",
            headers={"Content-Disposition": "attachment; filename=chart.png"},
        )
    finally:
        plt.close(chart)
