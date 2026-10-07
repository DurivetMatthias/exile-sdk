from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([WeaponClasses()]),
)

rules.append(
    Show(
        [
            Class("Wands"),
            TierStyle(TIER.EPIC),
        ]
    )
)
