from typing import Protocol, TypeVar


E = TypeVar("E", contravariant=True)


class OnEventOccurred(Protocol[E]):
    async def __call__(self, event: E) -> None:
        raise NotImplementedError
