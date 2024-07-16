from pydantic import BaseModel
from typing import Any, Optional

class ReturnValue(BaseModel):
    success: bool
    message: str
    code: str
    argument: Optional[str] = None
    data: Optional[Any] = None