from typing import Dict, List, NamedTuple


class KryptRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, KryptRegionData] = {
    "Menu": KryptRegionData(["The Button Realm"]),
    "The Button Realm": KryptRegionData(),
}
