from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions, StartInventoryPool


@dataclass
class KryptOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    # DeathLink is always on. Always.
    # death_link: DeathLink
