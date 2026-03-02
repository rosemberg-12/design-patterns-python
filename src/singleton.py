from typing import Self, TypeVar

T = TypeVar("T")


class DependencyManager:
    _instance = None

    def __init__(self) -> None:
        if not hasattr(self, "_dependency_map"):
            self._dependency_map: dict = {}

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def register(self, cls: type[T], dependency: T) -> None:
        self._dependency_map[cls] = dependency

    def resolve(self, cls: type[T]) -> T | None:
        return self._dependency_map.get(cls, None)
