from enum import StrEnum


class GEM_TOGGLES(StrEnum):
    ANY = "Any"
    SUPPORT_5 = "lvl 5 support gem"
    SKILL_16 = "lvl 16 skill gem"
    SKILL_17 = "lvl 17 skill gem"
    SKILL_18 = "lvl 18 skill gem"
    SKILL_19 = "lvl 19 skill gem"
    SKILL_20 = "lvl 20 skill gem"
    SPIRIT_16 = "lvl 16 spirit gem"
    SPIRIT_17 = "lvl 17 spirit gem"
    SPIRIT_18 = "lvl 18 spirit gem"
    SPIRIT_19 = "lvl 19 spirit gem"
    SPIRIT_20 = "lvl 20 spirit gem"


class CURRENCY_TOGGLES(StrEnum):
    SCROLL_OF_WISDOM = "Scroll of Wisdom"
    ARTIFICER = "Artificer's Orb"
    ARCANIST = "Arcanist's Etcher"
    ARMOURER = "Armourer's Scrap"
    BLACKSMITH = "Blacksmith's Whetstone"
    LESSER_JEWELLER = "Lesser Jeweller's Orb"
    GREATER_JEWELLER = "Greater Jeweller's Orb"


class JEWEL_TOGGLES(StrEnum):
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    EMERALD = "Emerald"


class CHARM_TOGGLES(StrEnum):
    ANY = "Any"
    ANTIDOTE = "Antidote Charm"
    T1_ANTIDOTE = "Antidote Charm with maximum Item Level"
    UNIQUE_ANTIDOTE = "Arakaali's Gift"
    DOUSING = "Dousing Charm"
    T1_DOUSING = "Dousing Charm with maximum Item Level"
    STAUNCHING = "Staunching Charm"
    T1_STAUNCHING = "Staunching Charm with maximum Item Level"
    THAWING = "Thawing Charm"
    T1_THAWING = "Thawing Charm with maximum Item Level"
    RITE_OF_PASSAGE = "Rite of Passage"


class FLASK_TOGGLES(StrEnum):
    ANY = "Any"
    ULTIMATE_LIFE = "Ultimate Life Flask"
    T1_ULTIMATE_LIFE = "Ultimate Life Flask with maximum Item Level"
    ULTIMATE_MANA = "Ultimate Mana Flask"
    T1_ULTIMATE_MANA = "Ultimate Mana Flask with maximum Item Level"
    LAVIAGNAS_SPIRITS = "Lavianga's Spirits"


class AMULET_TOGGLES(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good base type"
    T1_GOOD_BASE = "Good base type with maximum Item Level"


class BELT_TOGGLES(StrEnum):
    ANY = "Any"
    FINE = "Fine Belt"
    T1_FINE = "Fine Belt with maximum Item Level"
    MAGEBLOOD = "Mageblood"
    HEADHUNTER = "Headhunter"


class RING_TOGGLES(StrEnum):
    ANY = "Any"
    RESISTANCE_BASE = "Bases with resistances"
    T1_RESISTANCE_BASE = "Bases with resistances with maximum Item Level"
    KALANDRAS_TOUCH = "Kalandra's Touch"


class HELMET_TOGGLES(StrEnum):
    ANY_ARMOUR = "Any Armour base"
    ANY_EVASION = "Any Evasion base"
    IMPERIAL = "Imperial Helmet"
    T1_IMPERIAL = "Imperial Helmet with maximum Item Level"
    CONSTRICTING_COMMAND = "Constricting Command"


class GLOVES_TOGGLES(StrEnum):
    ANY_ARMOUR = "Any Armour base"
    ANY_EVASION = "Any Evasion base"
    MASSIVE = "Massive Mitts"
    T1_MASSIVE = "Massive Mitts with maximum Item Level"


class BOOTS_TOGGLES(StrEnum):
    ANY_ARMOUR = "Any Armour base"
    ANY_EVASION = "Any Evasion base"
    TASALIAN = "Tasalian Boots"
    T1_TASALIAN = "Tasalian Boots with maximum Item Level"


class BODY_TOGGLES(StrEnum):
    ANY_ARMOUR = "Any Armour base"
    ANY_EVASION = "Any Evasion base"
    SOLDIER = "Soldier Cuirass"
    T1_SOLDIER = "Soldier Cuirass with maximum Item Level"
    BRASS_DOME = "Brass Dome"


class MACE_TOGGLES(StrEnum):
    ANY = "Any"
    DAZE = "Fortified or Structured"
    T1_DAZE = "Fortified or Structured and T1 Melee Levels"


class SHIELD_TOGGLES(StrEnum):
    ANY = "Any"
    TAWHOAN = "Tawhoan Tower Shield"
    T1_TAWHOAN = "Tawhoan Tower Shield with maximum Item Level"


class BOW_TOGGLES(StrEnum):
    ANY = "Any"
    OBLITERATOR = "Obliterator Bow"
    T1_OBLITERATOR = "Obliterator Bow with maximum Item Level"


class QUIVER_TOGGLES(StrEnum):
    ANY = "Any"
    VISCERAL = "Visceral Quiver"
    T1_VISCERAL = "Visceral Quiver with maximum Item Level"


class OTHER_TOGGLES(StrEnum):
    SEKHEMA = "trial of sekhema key"
    CHAOS = "trial of chaos key"
    GREATER_RUNE = "good greater runes"
    UNIQUES = "Any unique"


toggles = [
    # Other
    OTHER_TOGGLES.SEKHEMA,
    OTHER_TOGGLES.CHAOS,
    OTHER_TOGGLES.GREATER_RUNE,
    OTHER_TOGGLES.UNIQUES,
    # Gem
    GEM_TOGGLES.ANY,
    GEM_TOGGLES.SUPPORT_5,
    GEM_TOGGLES.SKILL_16,
    GEM_TOGGLES.SKILL_17,
    GEM_TOGGLES.SKILL_18,
    GEM_TOGGLES.SKILL_19,
    GEM_TOGGLES.SKILL_20,
    GEM_TOGGLES.SPIRIT_16,
    GEM_TOGGLES.SPIRIT_17,
    GEM_TOGGLES.SPIRIT_18,
    GEM_TOGGLES.SPIRIT_19,
    GEM_TOGGLES.SPIRIT_20,
    # Currency
    CURRENCY_TOGGLES.SCROLL_OF_WISDOM,
    CURRENCY_TOGGLES.ARTIFICER,
    # CURRENCY_TOGGLES.ARCANIST,
    CURRENCY_TOGGLES.ARMOURER,
    CURRENCY_TOGGLES.BLACKSMITH,
    CURRENCY_TOGGLES.LESSER_JEWELLER,
    CURRENCY_TOGGLES.GREATER_JEWELLER,
    # Jewel
    JEWEL_TOGGLES.RUBY,
    JEWEL_TOGGLES.SAPPHIRE,
    JEWEL_TOGGLES.EMERALD,
    # Charm
    CHARM_TOGGLES.ANY,
    CHARM_TOGGLES.ANTIDOTE,
    CHARM_TOGGLES.DOUSING,
    CHARM_TOGGLES.STAUNCHING,
    CHARM_TOGGLES.THAWING,
    CHARM_TOGGLES.T1_ANTIDOTE,
    CHARM_TOGGLES.T1_DOUSING,
    CHARM_TOGGLES.T1_STAUNCHING,
    CHARM_TOGGLES.T1_THAWING,
    CHARM_TOGGLES.UNIQUE_ANTIDOTE,
    CHARM_TOGGLES.RITE_OF_PASSAGE,
    # Flask
    FLASK_TOGGLES.ANY,
    FLASK_TOGGLES.ULTIMATE_LIFE,
    FLASK_TOGGLES.T1_ULTIMATE_LIFE,
    FLASK_TOGGLES.ULTIMATE_MANA,
    FLASK_TOGGLES.T1_ULTIMATE_MANA,
    FLASK_TOGGLES.LAVIAGNAS_SPIRITS,
    # Amulet
    AMULET_TOGGLES.ANY,
    AMULET_TOGGLES.GOOD_BASE,
    AMULET_TOGGLES.T1_GOOD_BASE,
    # Belt
    BELT_TOGGLES.ANY,
    BELT_TOGGLES.FINE,
    BELT_TOGGLES.T1_FINE,
    BELT_TOGGLES.MAGEBLOOD,
    BELT_TOGGLES.HEADHUNTER,
    # Ring
    RING_TOGGLES.ANY,
    RING_TOGGLES.RESISTANCE_BASE,
    RING_TOGGLES.T1_RESISTANCE_BASE,
    RING_TOGGLES.KALANDRAS_TOUCH,
    # Helmet
    # HELMET_TOGGLES.ANY_ARMOUR,
    HELMET_TOGGLES.ANY_EVASION,
    # HELMET_TOGGLES.IMPERIAL,
    # HELMET_TOGGLES.T1_IMPERIAL,
    HELMET_TOGGLES.CONSTRICTING_COMMAND,
    # Gloves
    # GLOVES_TOGGLES.ANY_ARMOUR,
    GLOVES_TOGGLES.ANY_EVASION,
    # GLOVES_TOGGLES.MASSIVE,
    # GLOVES_TOGGLES.T1_MASSIVE,
    # Boots
    # BOOTS_TOGGLES.ANY_ARMOUR,
    BOOTS_TOGGLES.ANY_EVASION,
    # BOOTS_TOGGLES.TASALIAN,
    # BOOTS_TOGGLES.T1_TASALIAN,
    # Body Armour
    # BODY_TOGGLES.ANY_ARMOUR,
    BODY_TOGGLES.ANY_EVASION,
    # BODY_TOGGLES.SOLDIER,
    # BODY_TOGGLES.T1_SOLDIER,
    # BODY_TOGGLES.BRASS_DOME,
    # Mace
    # MACE_TOGGLES.ANY,
    # MACE_TOGGLES.DAZE,
    # MACE_TOGGLES.T1_DAZE,
    # Shield
    # SHIELD_TOGGLES.ANY,
    # SHIELD_TOGGLES.TAWHOAN,
    # SHIELD_TOGGLES.T1_TAWHOAN,
    # Bow
    BOW_TOGGLES.ANY,
    BOW_TOGGLES.OBLITERATOR,
    BOW_TOGGLES.T1_OBLITERATOR,
    # Quiver
    QUIVER_TOGGLES.ANY,
    QUIVER_TOGGLES.VISCERAL,
    QUIVER_TOGGLES.T1_VISCERAL,
]
