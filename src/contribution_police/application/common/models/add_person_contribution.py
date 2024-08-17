from dataclasses import dataclass
from typing import Iterable
from uuid import UUID


@dataclass(frozen=True, slots=True)
class AddPersonContribution:
    id: UUID
    first_name: str
    last_name: str
    photo_urls: Iterable[str]
