# Third Party Imports
import openai

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from decouple import config

# Relative Imports
from .schemas import Information
from .utils import get_validation_and_country, get_validation_and_season


router = APIRouter(prefix="/api", tags=['ai'])


@router.post("/recommend")
def get_data(info: Information):
    info = jsonable_encoder(info)

    country = info.get("country")
    if country is None:
        return JSONResponse(content="Country-Name is required: 'country'.", status_code=404)

    season = info.get("season")
    if season is None:
        return JSONResponse(content="Season-Name is required: 'season'.", status_code=404)

    is_country, country = get_validation_and_country(country_name=info.get("country"))
    is_season, season = get_validation_and_season(season_name=info.get("season"))

    if not is_country:
        return JSONResponse(content=f'Invalid Country-Name.', status_code=406)

    if not is_season:
        return JSONResponse(content=f'Invalid Season-Name.', status_code=406)

    openai.api_key = config("OPENAI_KEY")
    all_recommendations = []
    messages = [
        {"role": "system", "content": 'You are an AI assistant responsible for generating concise travel recommendations based on user requests. Each request will provide input parameters such as country and season, and your task is to respond with a one-line recommendation of the most famous places to visit in that country during the specified season. Your response should be between 10 and 40 words.'},
        {"role": "user", "content": f"country: Canada, season: Winter"},
        {"role": "assistant", "content": "Go skiing in Whistler."},
        {"role": "user", "content": f"country: Canada, season: Winter"},
        {"role": "assistant", "content": "Experience the Northern Lights in Yukon."},
        {"role": "user", "content": f"country: Canada, season: Winter"},
        {"role": "assistant", "content": "Visit the Quebec Winter Carnival."},
    ]
    for _ in range(3):
        messages.append({"role": "user", "content": f"country: {country}, season: {season}"},)
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        recommended_content = chat_completion['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": recommended_content})
        all_recommendations.append(recommended_content)
    response_data = {
        "country" : country,
        "season" : season,
        "recommendations" : all_recommendations
    }
    return JSONResponse(content=response_data)
