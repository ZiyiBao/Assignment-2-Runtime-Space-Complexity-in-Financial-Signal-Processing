

from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


@dataclass(frozen=True)
class MarketDataPoint:
    """
    Immutable market tick.
    Space: O(1) per tick
    """
    timestamp: datetime
    symbol: str
    price: float


@dataclass(frozen=True)
class Signal:
    timestamp: datetime
    symbol: str
    action: str
    price: float
    ma: float


class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> List[Signal]:
        pass
