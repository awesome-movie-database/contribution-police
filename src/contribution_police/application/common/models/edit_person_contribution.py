from dataclasses import dataclass
from typing import Iterable, Optional
from uuid import UUID


@dataclass(frozen=True, slots=True)
class EditPersonContribution:
    id: UUID
    first_name: Optional[str]
    last_name: Optional[str]
    photo_urls_to_add: Iterable[str]
