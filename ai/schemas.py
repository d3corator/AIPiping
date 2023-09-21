from pydantic import BaseModel, Field


class Information(BaseModel):
    country: str = Field(description="The country", min_length=2, default=None)
    season: str = Field(description="The season", min_length=5, default=None)
