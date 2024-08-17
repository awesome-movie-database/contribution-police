from dataclasses import dataclass
from typing import Iterable
from uuid import UUID

from .role import Role


@dataclass(frozen=True, slots=True)
class AddMovieContribution:
    id: UUID
    eng_title: str
    original_title: str
    summary: str
    description: str
    roles: Iterable[Role]
    photo_urls: Iterable[str]
