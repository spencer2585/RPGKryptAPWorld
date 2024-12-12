from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import KryptWorld


class KryptItem(Item):
    game = "RPGKrypt"


class KryptItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    db_id: int
    can_create: Callable[["KryptWorld"], bool] = lambda world: True


item_data_table: Dict[str, KryptItemData] = {
    "A2_Key": KryptItemData(
        code=80000002,
        type=ItemClassification.progression,
        db_id=2,
    ),
    "A3_Key": KryptItemData(
        code=80000003,
        type=ItemClassification.progression,
        db_id=3,
    ),
    "A4_Key": KryptItemData(
        code=80000004,
        type=ItemClassification.progression,
        db_id=4,
    ),
    "A5_Key": KryptItemData(
        code=80000005,
        type=ItemClassification.progression,
        db_id=5,
    ),
    "A6_Key": KryptItemData(
        code=80000006,
        type=ItemClassification.progression,
        db_id=6,
    ),
    "A7_Key": KryptItemData(
        code=80000007,
        type=ItemClassification.progression,
        db_id=7,
    ),
    "A8_Key": KryptItemData(
        code=80000008,
        type=ItemClassification.progression,
        db_id=8,
    ),
    "A9_Key": KryptItemData(
        code=80000009,
        type=ItemClassification.progression,
        db_id=9,
    ),
    "A10_Key": KryptItemData(
        code=800000010,
        type=ItemClassification.progression,
        db_id=10,
    ),
    "B1_Key": KryptItemData(
        code=80000011,
        type=ItemClassification.progression,
        db_id=11,
    ),
    "B2_Key": KryptItemData(
        code=80000012,
        type=ItemClassification.progression,
        db_id=12,
    ),
    "B3_Key": KryptItemData(
        code=80000013,
        type=ItemClassification.progression,
        db_id=13,
    ),
    "B4_Key": KryptItemData(
        code=80000014,
        type=ItemClassification.progression,
        db_id=14,
    ),
    "B5_Key": KryptItemData(
        code=80000015,
        type=ItemClassification.progression,
        db_id=15,
    ),
    "B6_Key": KryptItemData(
        code=80000016,
        type=ItemClassification.progression,
        db_id=16,
    ),
    "B7_Key": KryptItemData(
        code=80000017,
        type=ItemClassification.progression,
        db_id=17,
    ),
    "B8_Key": KryptItemData(
        code=80000018,
        type=ItemClassification.progression,
        db_id=18,
    ),
    "B9_Key": KryptItemData(
        code=80000019,
        type=ItemClassification.progression,
        db_id=19,
    ),
    "B10_Key": KryptItemData(
        code=80000020,
        type=ItemClassification.progression,
        db_id=20,
    ),
    "C1_Key": KryptItemData(
        code=80000021,
        type=ItemClassification.progression,
        db_id=21,
    ),
    "C2_Key": KryptItemData(
        code=80000022,
        type=ItemClassification.progression,
        db_id=22,
    ),
    "C3_Key": KryptItemData(
        code=80000023,
        type=ItemClassification.progression,
        db_id=23,
    ),
    "C4_Key": KryptItemData(
        code=80000024,
        type=ItemClassification.progression,
        db_id=24,
    ),
    "C5_Key": KryptItemData(
        code=80000025,
        type=ItemClassification.progression,
        db_id=25,
    ),
    "C6_Key": KryptItemData(
        code=80000026,
        type=ItemClassification.progression,
        db_id=26,
    ),
    "C7_Key": KryptItemData(
        code=80000027,
        type=ItemClassification.progression,
        db_id=27,
    ),
    "C8_Key": KryptItemData(
        code=80000028,
        type=ItemClassification.progression,
        db_id=28,
    ),
    "C9_Key": KryptItemData(
        code=80000029,
        type=ItemClassification.progression,
        db_id=29,
    ),
    "C10_Key": KryptItemData(
        code=80000030,
        type=ItemClassification.progression,
        db_id=30,
    ),
    "D1_Key": KryptItemData(
        code=80000031,
        type=ItemClassification.progression,
        db_id=31,
    ),
    "D2_Key": KryptItemData(
        code=80000032,
        type=ItemClassification.progression,
        db_id=32,
    ),
    "D3_Key": KryptItemData(
        code=80000033,
        type=ItemClassification.progression,
        db_id=33,
    ),
    "D4_Key": KryptItemData(
        code=80000034,
        type=ItemClassification.progression,
        db_id=34,
    ),
    "D5_Key": KryptItemData(
        code=80000035,
        type=ItemClassification.progression,
        db_id=35,
    ),
    "D6_Key": KryptItemData(
        code=80000036,
        type=ItemClassification.progression,
        db_id=36,
    ),
    "D7_Key": KryptItemData(
        code=80000037,
        type=ItemClassification.progression,
        db_id=37,
    ),
    "D8_Key": KryptItemData(
        code=80000038,
        type=ItemClassification.progression,
        db_id=38,
    ),
    "D9_Key": KryptItemData(
        code=80000039,
        type=ItemClassification.progression,
        db_id=39,
    ),
    "D10_Key": KryptItemData(
        code=80000040,
        type=ItemClassification.progression,
        db_id=40,
    ),
    "E1_Key": KryptItemData(
        code=80000041,
        type=ItemClassification.progression,
        db_id=41,
    ),
    "E2_Key": KryptItemData(
        code=80000042,
        type=ItemClassification.progression,
        db_id=42,
    ),
    "E3_Key": KryptItemData(
        code=80000043,
        type=ItemClassification.progression,
        db_id=43,
    ),
    "E4_Key": KryptItemData(
        code=80000044,
        type=ItemClassification.progression,
        db_id=44,
    ),
    "E5_Key": KryptItemData(
        code=80000045,
        type=ItemClassification.progression,
        db_id=45,
    ),
    "E6_Key": KryptItemData(
        code=80000046,
        type=ItemClassification.progression,
        db_id=46,
    ),
    "E7_Key": KryptItemData(
        code=80000047,
        type=ItemClassification.progression,
        db_id=47,
    ),
    "E8_Key": KryptItemData(
        code=80000048,
        type=ItemClassification.progression,
        db_id=48,
    ),
    "E9_Key": KryptItemData(
        code=80000049,
        type=ItemClassification.progression,
        db_id=49,
    ),
    "E10_Key": KryptItemData(
        code=80000050,
        type=ItemClassification.progression,
        db_id=50,
    ),
    "F1_Key": KryptItemData(
        code=80000051,
        type=ItemClassification.progression,
        db_id=51,
    ),
    "F2_Key": KryptItemData(
        code=80000052,
        type=ItemClassification.progression,
        db_id=52,
    ),
    "F3_Key": KryptItemData(
        code=80000053,
        type=ItemClassification.progression,
        db_id=53,
    ),
    "F4_Key": KryptItemData(
        code=80000054,
        type=ItemClassification.progression,
        db_id=54,
    ),
    "F5_Key": KryptItemData(
        code=80000055,
        type=ItemClassification.progression,
        db_id=55,
    ),
    "F6_Key": KryptItemData(
        code=80000056,
        type=ItemClassification.progression,
        db_id=56,
    ),
    "F7_Key": KryptItemData(
        code=80000057,
        type=ItemClassification.progression,
        db_id=57,
    ),
    "F8_Key": KryptItemData(
        code=80000058,
        type=ItemClassification.progression,
        db_id=58,
    ),
    "F9_Key": KryptItemData(
        code=80000059,
        type=ItemClassification.progression,
        db_id=59,
    ),
    "F10_Key": KryptItemData(
        code=80000060,
        type=ItemClassification.progression,
        db_id=60,
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
