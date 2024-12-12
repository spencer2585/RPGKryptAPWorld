from typing import Dict, List, NamedTuple


class KryptRegionData(NamedTuple):
    connecting_regions: List[str] = []
    locations: List[str] = []
    access_rules:List[str] = []


region_data_table: Dict[str, KryptRegionData] = {
    "Menu": KryptRegionData(["A1"]),
    "A1": KryptRegionData(["Menu","B1","A2"],["A1_Chest"],["A1_Key"]),
    "A2": KryptRegionData(["A1","B2","A3"],["A2_Chest"],["A2_Key"]),
}
