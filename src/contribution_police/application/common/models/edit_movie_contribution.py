from dataclasses import dataclass
from typing import Iterable, Optional
from uuid import UUID

from .role import Role


@dataclass(frozen=True, slots=True)
class EditMovieContribution:
    id: UUID
    eng_title: Optional[str]
    original_title: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    roles_to_add: Iterable[Role]
    photo_urls_to_add: Iterable[str]
