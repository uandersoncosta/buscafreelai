from pydantic import BaseModel


class MatchingRequest(BaseModel):
  profile_id: int


class MatchingResponse(BaseModel):
  profile_id: int
  message: str