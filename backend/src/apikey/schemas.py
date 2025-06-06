import datetime
from enum import StrEnum
from typing import List, Optional

from pydantic import BaseModel

from src.schema import FilterParams


class ApiKeySortField(StrEnum):
    ID = "id"
    NAME = "name"
    CREATED_AT = "created_at"
    LAST_USED_AT = "last_used_at"
    USER_ID = "user_id"


class ApiKeyFilterParams(FilterParams[ApiKeySortField]):
    pass


class ApiKeyCreate(BaseModel):
    """Schema for creating a new API key"""

    name: str


class ApiKeyResponse(BaseModel):
    """Schema for API key response"""

    id: int
    key: str
    name: str
    created_at: datetime.datetime
    last_used_at: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True


class ApiKeyInfo(BaseModel):
    """Schema for API key info without the actual key"""

    id: int
    name: str
    created_at: datetime.datetime
    last_used_at: Optional[datetime.datetime] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None

    class Config:
        from_attributes = True


class ApiKeyUsageLogResponse(BaseModel):
    """Schema for API key usage log response"""

    id: int
    timestamp: datetime.datetime
    endpoint: str
    method: str
    model: Optional[str] = None
    status_code: int

    class Config:
        from_attributes = True


class ApiKeyUsageStats(BaseModel):
    """Schema for API key usage statistics"""

    total_requests: int
    last_30_days_requests: int
    requests_today: int
    successful_requests: int
    failed_requests: int
    requests_per_day: List[dict]
