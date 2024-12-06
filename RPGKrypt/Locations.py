from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import KryptWorld


class KryptLocation(Location):
    game = "Krypt"


class KryptLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["KryptWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, KryptLocationData] = {
    "A1_Chest": KryptLocationData(
        region="A1",
        address=80000001,
    ),
    "A2_Chest": KryptLocationData(
        region="A2",
        address=80000002,
    ),
    "A3_Chest": KryptLocationData(
        region="A3",
        address=80000003,
    ),
    "A4_Chest": KryptLocationData(
        region="A4",
        address=80000004,
    ),
    "A5_Chest": KryptLocationData(
        region="A5",
        address=80000005,
    ),
    "A6_Chest": KryptLocationData(
        region="A6",
        address=80000006,
    ),
    "A7_Chest": KryptLocationData(
        region="A7",
        address=80000007,
    ),
    "A8_Chest": KryptLocationData(
        region="A8",
        address=80000008,
    ),
    "A9_Chest": KryptLocationData(
        region="A9",
        address=80000009,
    ),
    "A10_Chest": KryptLocationData(
        region="A10",
        address=800000010,
    ),
    
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
