from enum import StrEnum


class AMULET_TOGGLES(StrEnum):
    ANY = "Any"
    MELEE_LEVEL = "Melee Level"
    MELEE_LEVEL_AND_RES = "Melee level and resistances"


class BELT_TOGGLES(StrEnum):
    ANY = "Any"
    FINE = "Fine"
    FINE_RES = "Fine Resistance"
    UNIQUE = "Unique"


class BODY_TOGGLES(StrEnum):
    ANY = "Any"
    SOLDIER = "Soldier Cuirass"
    SOLDIER_RES = "Soldier with Resistance"
    BRASS_DOME = "Brass Dome"


class BOOTS_TOGGLES(StrEnum):
    ANY = "Any"
    TASALIAN = "Tasalian"
    FRACTURE = "Tasalian for fracturing"


class CURRENCY_TOGGLES(StrEnum):
    ARTIFICER = "Artificer's Orb"
    ARMOURER = "Armourer's Scrap"
    GEMCUTTER = "Gemcutter's Prism"
    GLASSBLOWER = "Glassblower's Bauble"
    LESSER_JEWELLER = "Lesser Jeweller's Orb"
    GREATER_JEWELLER = "Greater Jeweller's Orb"


class SHIELD_TOGGLES(StrEnum):
    ANY = "Any"
    TAWHOAN = "Tawhoan Tower Shield"
    TAWHOAN_RES = "Tawhoan with res"


class FLASK_TOGGLES(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good base"
    GOOD_ILVL = "Good item level"
    UNIQUE = "Unique"


class RING_TOGGLES(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good bases"
    RES = "Resistances"
    UNIQUE = "unique"


class OTHER_TOGGLES(StrEnum):
    SEKHEMA = "trial of sekhema key"
    CHAOS = "trial of chaos key"
    BASIC_AUGMENT = "basic augment"


class MACE_TOGGLES(StrEnum):
    ANY = "Any"
    DAZE = "Fortified or Structured"
    DAZE_4 = "Fortified or Structured and +4"


class HELMET_TOGGLES(StrEnum):
    ANY = "Any"
    IMPERIAL = "Imperial"
    IMPERIAL_RES = "Imperial with Resistance"
    CONSTRICTING_COMMAND = "Constricting Command"


class GLOVES_TOGGLES(StrEnum):
    ANY = "Any"
    MASSIVE = "Massive Mitts"
    MASSIVE_RES = "Massive Mitts with res"


class GEM_TOGGLES(StrEnum):
    ANY = "Any"
    SUPPORT = "Uncut support lvl 5"
    _18 = "18"
    _19 = "19"
    _20 = "20"


active_gem_rules = [
    # GEM_TOGGLES.ANY,
    # GEM_TOGGLES.SUPPORT,
    # GEM_TOGGLES._18,
    GEM_TOGGLES._19,
    GEM_TOGGLES._20,
]
active_currency_rules = [
    # CURRENCY_TOGGLES.ARTIFICER,
    # CURRENCY_TOGGLES.ARMOURER,
    # CURRENCY_TOGGLES.GEMCUTTER,
    CURRENCY_TOGGLES.GLASSBLOWER,
    # CURRENCY_TOGGLES.LESSER_JEWELLER,
    # CURRENCY_TOGGLES.GREATER_JEWELLER,
]
active_flask_rules = [
    # FLASK_TOGGLES.ANY,
    # FLASK_TOGGLES.GOOD_BASE,
    FLASK_TOGGLES.GOOD_ILVL,
    FLASK_TOGGLES.UNIQUE,
]
active_other_rules = [
    OTHER_TOGGLES.SEKHEMA,
    OTHER_TOGGLES.CHAOS,
    # OTHER_TOGGLES.BASIC_AUGMENT,
]
active_amulet_rules = [
    # AMULET_TOGGLES.ANY,
    # AMULET_TOGGLES.MELEE_LEVEL,
    AMULET_TOGGLES.MELEE_LEVEL_AND_RES,
]
active_belt_rules = [
    # BELT_TOGGLES.ANY,
    # BELT_TOGGLES.FINE,
    BELT_TOGGLES.FINE_RES,
    BELT_TOGGLES.UNIQUE,
]
active_ring_rules = [
    # RING_TOGGLES.ANY,
    # RING_TOGGLES.GOOD_BASE,
    RING_TOGGLES.RES,
    RING_TOGGLES.UNIQUE,
]
active_helmet_rules = [
    # HELMET_TOGGLES.ANY,
    # HELMET_TOGGLES.IMPERIAL,
    # HELMET_TOGGLES.IMPERIAL_RES,
    HELMET_TOGGLES.CONSTRICTING_COMMAND,
]
active_gloves_rules = [
    # GLOVES_TOGGLES.ANY,
    # GLOVES_TOGGLES.MASSIVE,
    GLOVES_TOGGLES.MASSIVE_RES,
]
active_body_rules = [
    # BODY_TOGGLES.ANY,
    # BODY_TOGGLES.SOLDIER,
    BODY_TOGGLES.SOLDIER_RES,
    BODY_TOGGLES.BRASS_DOME,
]
active_boots_rules = [
    # BOOTS_TOGGLES.ANY,
    # BOOTS_TOGGLES.TASALIAN,
    BOOTS_TOGGLES.FRACTURE,
]
active_mace_rules = [
    # MACE_TOGGLES.ANY,
    # MACE_TOGGLES.DAZE,
    MACE_TOGGLES.DAZE_4,
]
active_shield_rules = [
    # SHIELD_TOGGLES.ANY,
    # SHIELD_TOGGLES.TAWHOAN,
    SHIELD_TOGGLES.TAWHOAN_RES,
]
