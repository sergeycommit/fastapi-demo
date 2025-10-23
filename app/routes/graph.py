from fastapi import APIRouter, Depends
import plotly.graph_objects as go

from app.config import *
from ..dependencies import oauth2_scheme


router = APIRouter(
            tags=["Graph"],
            responses={404: {"description": "Not found"}},
)


@router.get("/graph",
         tags=["Graph", ],
         summary="Create graph",
         dependencies=[Depends(oauth2_scheme)],
            )
async def get_plotly_graph():
    fig = go.Figure(data=[go.Bar(x=[USERNAME, ], y=[100])])
    return fig.to_html()