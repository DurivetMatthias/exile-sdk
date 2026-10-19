from app import filter
from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from app.toggles import *

rules = []

# =============================================================================
# Other
# =============================================================================

rules.append(Show([Class("Quest Items"), TierStyle(TIER.EPIC)]))
rules.append(Show([Class("Instance Local Items"), TierStyle(TIER.EPIC)]))

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Collarbone",
                    "Jawbone",
                    "Rib",
                    "Cranium",
                    "Abyss Tablet",
                    "Omen of Light",
                    "Omen of Putrefaction",
                    "Omen of Abyssal Echoes",
                    "Omen of the Liege",
                    "Essence of the Abyss",
                    "Omen of the Sovereign",
                    "Omen of the Blackblooded",
                    "Omen of Dextral Necromancy",
                    "Omen of Sinistral Necromancy",
                    "Kulemak's Invitation",
                ],
                OPERATOR.CONTAINS,
            ),
            AbyssStyle(),
            MultiBaseType(["Tribal"], OPERATOR.NOT_EQUAL),
        ]
    )
)

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Ore",
                    "Flux",
                    "Saga",
                    "Alloy",
                    "Crest",
                    "Verisium",
                    "Expedition Tablet",
                    "Expedition Logbook",
                    "Shattered Triskelion",
                ],
                OPERATOR.CONTAINS,
            ),
            MultiClass(
                [
                    "Boots",
                    "Helmets",
                    "Gloves",
                    "Body Armours",
                    "Crossbows",
                    "Spears",
                    "Shields",
                ],
                OPERATOR.NOT_EQUAL,
            ),
            MultiBaseType(["Core"], OPERATOR.NOT_EQUAL),
            ExpeditionStyle(),
        ]
    )
)

rules.append(Show([Class("Omen", OPERATOR.CONTAINS), RitualStyle()]))
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Sacred Bloom",
                    "Ritual tablet",
                    "Head of the King",
                    "Call of the Shadows",
                    "An Audience with the King",
                ],
            ),
            RitualStyle(),
        ]
    )
)

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Wombgift",
                    "Catalyst",
                    "Breachstone",
                    "Breach Ring",
                    "Breach Tablet",
                    "Breachlord Sac",
                    "Breach Splinter",
                    "Essence of the Breach",
                ],
                OPERATOR.CONTAINS,
            ),
            BreachStyle(),
        ]
    )
)

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Liquid",
                    "Delirium Tablet",
                    "Simulacrum",
                    "Simulacrum Splinter",
                ],
                OPERATOR.CONTAINS,
            ),
            DeliriumStyle(),
        ]
    )
)

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Infuser",
                    "Temple Tablet",
                    "Vaal Siphoner",
                    "Architect's Orb",
                    "Orb of Sacrifice",
                    "Orb of Extraction",
                    "Core Destabiliser",
                    "Atziri's Medallion",
                    "Vaal Cultivation Orb",
                    "Crystallised Corruption",
                ],
                OPERATOR.CONTAINS,
            ),
            VaalStyle(),
        ]
    )
)

rules.append(
    Show(
        [
            MultiBaseType(["Overseer Tablet", "Irradiated Tablet"]),
            TierStyle(TIER.EPIC),
        ]
    )
)

if OTHER_TOGGLES.CHAOS in toggles:
    rules.append(
        Show(
            [
                ItemLevel(75),
                BaseType("Inscribed Ultimatum"),
                TierStyle(TIER.COMMON),
            ]
        )
    )
if OTHER_TOGGLES.SEKHEMA in toggles:
    rules.append(
        Show(
            [
                ItemLevel(75),
                BaseType("Djinn Barya"),
                TierStyle(TIER.COMMON),
            ]
        )
    )
rules.append(
    Show(
        [
            MultiBaseType(["Gold Key", "Silver Key", "Bronze Key"]),
            TierStyle(TIER.COMMON),
        ]
    ),
)
rules.append(
    Show(
        [
            MultiBaseType(["Victorious Fate", "Cowardly Fate", "Deadly Fate"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Essence",
                    "Cryptic Key",
                    "Reliquary Key",
                ],
                OPERATOR.CONTAINS,
            ),
            TierStyle(TIER.EPIC),
        ]
    )
)
rules.append(Show([Class("Pinnacle Keys"), TierStyle(TIER.EPIC)]))

rules.append(Hide([Class("Augment")]))
rules.append(
    Show(
        [
            InCampaign(),
            MultiBaseType(
                [
                    "Iron Rune",
                    "Desert Rune",
                    "Storm Rune",
                    "Glacial Rune",
                ],
                OPERATOR.CONTAINS,
            ),
            TierStyle(TIER.RARE),
        ]
    )
)

if OTHER_TOGGLES.GREATER_RUNE in toggles:
    rules.append(
        Show(
            [
                MultiBaseType(
                    [
                        "Greater Iron Rune",
                        "Greater Desert Rune",
                        "Greater Storm Rune",
                        "Greater Glacial Rune",
                    ]
                ),
                TierStyle(TIER.EPIC),
            ]
        )
    )

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Greater Rune of Alacrity",
                    "Farrul's Rune of the Chase",
                    "Farrul's Rune of the Hunt",
                    "Courtesan Mannan's Rune of Cruelty",
                    "Masterwork Rune",
                    "Idol of Sirrius",
                    "Bear Idol",
                    "Fox Idol",
                    "Raven-Touched Shard",
                    "Passion of Aldur",
                    "Aldur's Legacy",
                    "Ancient Rune of Shattering",
                    "Cadigan's Epiphany",
                    "Astrid's Creativity",
                    "Soul Core of Tacati",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)

rules.append(
    Show(
        [
            MultiClass(["Gloves", "Boots", "Helmets"]),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)
rules.append(
    Show(
        [
            MultiClass(["Body Armours"]),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)
rules.append(
    Show(
        [
            OffhandClasses(),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)
rules.append(
    Show(
        [
            TwoHandedWeaponClasses(),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)
rules.append(
    Show(
        [
            OneHandedWeaponClasses(),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)

rules.append(
    Show(
        [
            InActOne(),
            Rarity(RARITY.RARE),
            Height(3),
            VendorStyle(),
        ]
    ),
)

rules.append(Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]))
rules.append(Show([Class("Waystone"), TierStyle(TIER.EPIC)]))

# =============================================================================
# Gem
# =============================================================================

rules.append(
    Hide([MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"])])
)

rules.append(
    Show(
        [
            MultiClass(["Support Gems", "Skill Gems"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)

if GEM_TOGGLES.ANY in toggles:
    rules.append(
        Show(
            [
                MultiClass(
                    [
                        "Uncut Skill Gems",
                        "Uncut Spirit Gems",
                        "Uncut Support Gems",
                    ]
                ),
                TierStyle(TIER.COMMON),
            ]
        )
    )

gem_map = {
    GEM_TOGGLES.SUPPORT_5: {
        "class": "Uncut Support Gems",
        "level": "Level 5",
        "tier": TIER.COMMON,
    },
    GEM_TOGGLES.SKILL_16: {
        "class": "Uncut Skill Gems",
        "level": "Level 16",
        "tier": TIER.EPIC,
    },
    GEM_TOGGLES.SKILL_17: {
        "class": "Uncut Skill Gems",
        "level": "Level 17",
        "tier": TIER.EPIC,
    },
    GEM_TOGGLES.SKILL_18: {
        "class": "Uncut Skill Gems",
        "level": "Level 18",
        "tier": TIER.EPIC,
    },
    GEM_TOGGLES.SKILL_19: {
        "class": "Uncut Skill Gems",
        "level": "Level 19",
        "tier": TIER.LEGENDARY,
    },
    GEM_TOGGLES.SKILL_20: {
        "class": "Uncut Skill Gems",
        "level": "Level 20",
        "tier": TIER.LEGENDARY,
    },
    GEM_TOGGLES.SPIRIT_16: {
        "class": "Uncut Spirit Gems",
        "level": "Level 16",
        "tier": TIER.EPIC,
    },
    GEM_TOGGLES.SPIRIT_17: {
        "class": "Uncut Spirit Gems",
        "level": "Level 17",
        "tier": TIER.EPIC,
    },
    GEM_TOGGLES.SPIRIT_18: {
        "class": "Uncut Spirit Gems",
        "level": "Level 18",
        "tier": TIER.EPIC,
    },
    GEM_TOGGLES.SPIRIT_19: {
        "class": "Uncut Spirit Gems",
        "level": "Level 19",
        "tier": TIER.LEGENDARY,
    },
    GEM_TOGGLES.SPIRIT_20: {
        "class": "Uncut Spirit Gems",
        "level": "Level 20",
        "tier": TIER.LEGENDARY,
    },
}

for toggle, gem in gem_map.items():
    if toggle in toggles:
        rules.append(
            Show(
                [
                    Class(gem["class"]),
                    BaseType(gem["level"], operator=OPERATOR.CONTAINS),
                    TierStyle(gem["tier"]),
                ]
            ),
        )

# =============================================================================
# Currency
# =============================================================================

rules.append(
    Hide(
        [
            MultiBaseType(
                [
                    "Gold",
                    "Regal Shard",
                    "Scroll of Wisdom",
                    "Artificer's Orb",
                    "Arcanist's Etcher",
                    "Armourer's Scrap",
                    "Blacksmith's Whetstone",
                    "Lesser Jeweller's Orb",
                    "Greater Jeweller's Orb",
                ]
            )
        ]
    )
)

currency_map = {
    "Orb of Transmutation": TIER.RARE,
    "Greater Orb of Transmutation": TIER.EPIC,
    "Perfect Orb of Transmutation": TIER.LEGENDARY,
    "Orb of Augmentation": TIER.RARE,
    "Greater Orb of Augmentation": TIER.EPIC,
    "Perfect Orb of Augmentation": TIER.LEGENDARY,
    "Regal Orb": TIER.EPIC,
    "Greater Regal Orb": TIER.LEGENDARY,
    "Perfect Regal Orb": TIER.LEGENDARY,
    "Exalted Orb": TIER.EPIC,
    "Greater Exalted Orb": TIER.LEGENDARY,
    "Perfect Exalted Orb": TIER.LEGENDARY,
    "Chaos Orb": TIER.EPIC,
    "Greater Chaos Orb": TIER.LEGENDARY,
    "Perfect Chaos Orb": TIER.LEGENDARY,
    "Orb of Alchemy": TIER.EPIC,
    "Vaal Orb": TIER.EPIC,
    "Gemcutter's Prism": TIER.EPIC,
    "Glassblower's Bauble": TIER.EPIC,
    "Chance Shard": TIER.EPIC,
    "Perfect Jeweller's Orb": TIER.LEGENDARY,
    "Divine Orb": TIER.LEGENDARY,
    "Orb of Chance": TIER.LEGENDARY,
    "Fracturing Orb": TIER.LEGENDARY,
    "Orb of Annulment": TIER.LEGENDARY,
    "Hinekora's Lock": TIER.LEGENDARY,
    "Mirror of Kalandra": TIER.LEGENDARY,
}

rules.extend(
    Show([BaseType(currency), TierStyle(tier)])
    for currency, tier in currency_map.items()
)

if CURRENCY_TOGGLES.SCROLL_OF_WISDOM in toggles:
    rules.append(Show([BaseType("Scroll of Wisdom"), TierStyle(TIER.COMMON)]))
if CURRENCY_TOGGLES.ARTIFICER in toggles:
    rules.append(Show([BaseType("Artificer's Orb"), TierStyle(TIER.RARE)]))
if CURRENCY_TOGGLES.ARCANIST in toggles:
    rules.append(Show([BaseType("Arcanist's Etcher"), TierStyle(TIER.RARE)]))
if CURRENCY_TOGGLES.ARMOURER in toggles:
    rules.append(Show([BaseType("Armourer's Scrap"), TierStyle(TIER.RARE)]))
if CURRENCY_TOGGLES.BLACKSMITH in toggles:
    rules.append(Show([BaseType("Blacksmith's Whetstone"), TierStyle(TIER.RARE)]))
if CURRENCY_TOGGLES.LESSER_JEWELLER in toggles:
    rules.append(Show([BaseType("Lesser Jeweller's Orb"), TierStyle(TIER.LEGENDARY)]))
if CURRENCY_TOGGLES.GREATER_JEWELLER in toggles:
    rules.append(Show([BaseType("Greater Jeweller's Orb"), TierStyle(TIER.LEGENDARY)]))

# =============================================================================
# Jewel
# =============================================================================

rules.append(Hide([Rarity(RARITY.UNIQUE, OPERATOR.NOT_EQUAL), Class("Jewels")]))

jewel_map = {
    JEWEL_TOGGLES.RUBY: {"base": "Ruby"},
    JEWEL_TOGGLES.SAPPHIRE: {"base": "Sapphire"},
    JEWEL_TOGGLES.EMERALD: {"base": "Emerald"},
}

for toggle, jewel in jewel_map.items():
    if toggle in toggles:
        rules.append(Show([BaseType(jewel["base"]), TierStyle(TIER.EPIC)]))

rules.append(
    Show(
        [
            MultiBaseType(
                ["Time-Lost Ruby", "Time-Lost Emerald", "Time-Lost Sapphire"]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)

rules.append(Show([Class("Jewels"), Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY)]))

# =============================================================================
# Charm
# =============================================================================

rules.append(Hide([Class("Charms")]))

if CHARM_TOGGLES.ANY in toggles:
    rules.append(Show([Class("Charms"), TierStyle(TIER.EPIC)]))

charm_map = {
    CHARM_TOGGLES.ANTIDOTE: {"base": "Antidote Charm"},
    CHARM_TOGGLES.DOUSING: {"base": "Dousing Charm"},
    CHARM_TOGGLES.STAUNCHING: {"base": "Staunching Charm"},
    CHARM_TOGGLES.THAWING: {"base": "Thawing Charm"},
}

for toggle, charm in charm_map.items():
    if toggle in toggles:
        rules.append(
            Show(
                [
                    Rarity(RARITY.MAGIC, OPERATOR.LTE),
                    BaseType(charm["base"]),
                    TierStyle(TIER.EPIC),
                ]
            )
        )

charm_map = {
    CHARM_TOGGLES.T1_ANTIDOTE: {"base": "Antidote Charm"},
    CHARM_TOGGLES.T1_DOUSING: {"base": "Dousing Charm"},
    CHARM_TOGGLES.T1_STAUNCHING: {"base": "Staunching Charm"},
    CHARM_TOGGLES.T1_THAWING: {"base": "Thawing Charm"},
}

for toggle, charm in charm_map.items():
    if toggle in toggles:
        rules.append(
            Show(
                [
                    Rarity(RARITY.MAGIC, OPERATOR.LTE),
                    ItemLevel(83),
                    BaseType(charm["base"]),
                    TierStyle(TIER.LEGENDARY),
                ]
            )
        )

if CHARM_TOGGLES.UNIQUE_ANTIDOTE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.UNIQUE),
                BaseType("Antidote Charm"),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

if CHARM_TOGGLES.RITE_OF_PASSAGE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.UNIQUE),
                BaseType("Golden Charm"),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

# =============================================================================
# Flask
# =============================================================================

rules.append(Hide([MultiClass(["Life Flasks", "Mana Flasks"])]))

if FLASK_TOGGLES.ANY in toggles:
    rules.append(
        Show(
            [
                MultiClass(["Life Flasks", "Mana Flasks"]),
                TierStyle(TIER.COMMON),
            ]
        )
    )

if FLASK_TOGGLES.ULTIMATE_LIFE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.UNIQUE, OPERATOR.NOT_EQUAL),
                BaseType("Ultimate Life Flask"),
                TierStyle(TIER.COMMON),
            ]
        )
    )

if FLASK_TOGGLES.T1_ULTIMATE_LIFE in toggles:
    rules.append(
        Show(
            [
                ItemLevel(83),
                Rarity(RARITY.UNIQUE, OPERATOR.NOT_EQUAL),
                BaseType("Ultimate Life Flask"),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

if FLASK_TOGGLES.ULTIMATE_MANA in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.UNIQUE, OPERATOR.NOT_EQUAL),
                BaseType("Ultimate Life Flask"),
                TierStyle(TIER.COMMON),
            ]
        )
    )

if FLASK_TOGGLES.T1_ULTIMATE_MANA in toggles:
    rules.append(
        Show(
            [
                ItemLevel(83),
                Rarity(RARITY.UNIQUE, OPERATOR.NOT_EQUAL),
                BaseType("Ultimate Life Flask"),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

if FLASK_TOGGLES.LAVIAGNAS_SPIRITS in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.UNIQUE),
                BaseType("Gargantuan Mana Flask"),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

# =============================================================================
# Amulet
# =============================================================================

rules.append(Hide([Class("Amulets")]))

if AMULET_TOGGLES.ANY in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.RARE, OPERATOR.LTE),
                Class("Amulets"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

good_bases = [
    "Jade Amulet",
    "Amber Amulet",
    "Lapis Amulet",
    "Stellar Amulet",
    "Solar Amulet",
    "Bloodstone Amulet",
]

if AMULET_TOGGLES.GOOD_BASE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.RARE, OPERATOR.LTE),
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if AMULET_TOGGLES.T1_GOOD_BASE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.RARE, OPERATOR.LTE),
                ItemLevel(82),
                MultiBaseType(good_bases),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

# =============================================================================
# Belt
# =============================================================================

rules.append(Hide([Class("Belts")]))

if BELT_TOGGLES.ANY in toggles:
    rules.append(Show([Class("Belts"), TierStyle(TIER.EPIC)]))

if BELT_TOGGLES.FINE in toggles:
    rules.append(Show([BaseType("Fine Belt"), TierStyle(TIER.EPIC)]))

if BELT_TOGGLES.T1_FINE in toggles:
    rules.append(
        Show([ItemLevel(82), BaseType("Fine Belt"), TierStyle(TIER.LEGENDARY)])
    )

if BELT_TOGGLES.MAGEBLOOD in toggles:
    rules.append(Show([UniqueBase("Utility Belt")]))
    rules.append(Show([ChanceBase("Utility Belt")]))

if BELT_TOGGLES.HEADHUNTER in toggles:
    rules.append(Show([UniqueBase("Heavy Belt")]))
    rules.append(Show([ChanceBase("Heavy Belt")]))

# =============================================================================
# Ring
# =============================================================================

rules.append(Hide([Class("Rings")]))

if RING_TOGGLES.ANY in toggles:
    rules.append(Show([Class("Rings"), TierStyle(TIER.EPIC)]))

resistance_bases = [
    "Ruby Ring",
    "Sapphire Ring",
    "Topaz Ring",
    "Amethyst Ring",
    "Prismatic Ring",
]

if RING_TOGGLES.RESISTANCE_BASE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(resistance_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if RING_TOGGLES.T1_RESISTANCE_BASE in toggles:
    rules.append(
        Show(
            [
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                ItemLevel(82),
                MultiBaseType(resistance_bases),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

if RING_TOGGLES.KALANDRAS_TOUCH in toggles:
    rules.append(
        Show([Rarity(RARITY.UNIQUE), BaseType("Ring"), TierStyle(TIER.LEGENDARY)])
    )

# =============================================================================
# Helmet
# =============================================================================

rules.append(Hide([Class("Helmets")]))

if HELMET_TOGGLES.ANY in toggles:
    rules.append(Show([PureArmour(), Class("Helmets"), TierStyle(TIER.EPIC)]))

if HELMET_TOGGLES.IMPERIAL in toggles:
    rules.append(Show([CraftingBase("Imperial Greathelm")]))

if HELMET_TOGGLES.T1_IMPERIAL in toggles:
    rules.append(Show([PerfectCraftingBase("Imperial Greathelm")]))

if HELMET_TOGGLES.CONSTRICTING_COMMAND in toggles:
    rules.append(Show([UniqueBase("Viper Cap")]))
    rules.append(Show([ChanceBase("Viper Cap")]))

# =============================================================================
# Gloves
# =============================================================================

rules.append(Hide([Class("Gloves")]))

rules.append(
    Show(
        [
            InActOne(),
            Rarity(RARITY.MAGIC, OPERATOR.GTE),
            MultiBaseType(
                [
                    "Suede Bracers",
                    "Torn Gloves",
                    "Ringmail Gauntlets",
                    "Rope Cuffs",
                    "Gauze Wraps",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    )
)

if GLOVES_TOGGLES.ANY in toggles:
    rules.append(Show([PureArmour(), Class("Gloves"), TierStyle(TIER.EPIC)]))

if GLOVES_TOGGLES.MASSIVE in toggles:
    rules.append(Show([CraftingBase("Massive Mitts")]))

if GLOVES_TOGGLES.T1_MASSIVE in toggles:
    rules.append(Show([PerfectCraftingBase("Massive Mitts")]))

# =============================================================================
# Boots
# =============================================================================

rules.append(Hide([Class("Boots")]))

rules.append(
    Show(
        [
            InActOne(),
            Rarity(RARITY.MAGIC, OPERATOR.GTE),
            MultiBaseType(
                [
                    "Rawhide Boots",
                    "Straw Sandals",
                    "Mail Sabatons",
                    "Padded Leggings",
                    "Frayed Shoes",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    )
)

if BOOTS_TOGGLES.ANY in toggles:
    rules.append(Show([PureArmour(), Class("Boots"), TierStyle(TIER.EPIC)]))

if BOOTS_TOGGLES.TASALIAN in toggles:
    rules.append(Show([CraftingBase("Tasalian Greaves")]))

if BOOTS_TOGGLES.T1_TASALIAN in toggles:
    rules.append(Show([PerfectCraftingBase("Tasalian Greaves")]))

# =============================================================================
# Body Armour
# =============================================================================

rules.append(Hide([Class("Body Armours")]))

if BODY_TOGGLES.ANY in toggles:
    rules.append(Show([PureArmour(), Class("Body Armours"), TierStyle(TIER.EPIC)]))

if BODY_TOGGLES.SOLDIER in toggles:
    rules.append(Show([CraftingBase("Soldier Cuirass")]))

if BODY_TOGGLES.T1_SOLDIER in toggles:
    rules.append(Show([PerfectCraftingBase("Soldier Cuirass")]))

if BODY_TOGGLES.BRASS_DOME in toggles:
    rules.append(Show([UniqueBase("Champion Cuirass")]))
    rules.append(Show([ChanceBase("Champion Cuirass")]))

# =============================================================================
# Mace
# =============================================================================

rules.append(Hide([WeaponClasses()]))

if MACE_TOGGLES.ANY in toggles:
    rules.append(Show([Class("One Hand Maces"), TierStyle(TIER.EPIC)]))

daze_base_types = ["Fortified Hammer", "Structured Hammer"]

if MACE_TOGGLES.DAZE in toggles:
    rules.append(Show([MultiBaseType(daze_base_types), TierStyle(TIER.EPIC)]))

if MACE_TOGGLES.T1_DAZE in toggles:
    rules.append(
        Show([ItemLevel(81), MultiBaseType(daze_base_types), TierStyle(TIER.LEGENDARY)])
    )

# =============================================================================
# Shield
# =============================================================================

rules.append(Hide([OffhandClasses()]))

if SHIELD_TOGGLES.ANY in toggles:
    rules.append(Show([PureArmour(), Class("Shields"), TierStyle(TIER.EPIC)]))

if SHIELD_TOGGLES.TAWHOAN in toggles:
    rules.append(Show([CraftingBase("Tawhoan Tower Shield")]))

if SHIELD_TOGGLES.T1_TAWHOAN in toggles:
    rules.append(Show([PerfectCraftingBase("Tawhoan Tower Shield")]))

# =============================================================================
# Bow
# =============================================================================

# =============================================================================
# Quiver
# =============================================================================

# =============================================================================
# Generate filter
# =============================================================================

filter.generate(rules, "shield-wall")
