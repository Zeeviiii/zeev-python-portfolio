"""בדיקות ל-zeev_hospital.py

הרצה מתיקיית השורש של הפרויקט:
    pytest
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from zeev_hospital import FLOORS, floor_of, is_correct_floor, parse_floor


# ---------- floor_of ----------

def test_known_department_returns_its_floor():
    assert floor_of("חדר ניתוח") == 2
    assert floor_of("מחלקת לב") == 10


def test_unknown_department_returns_none():
    assert floor_of("מחלקה שאינה קיימת") is None


def test_surrounding_spaces_are_ignored():
    assert floor_of("  מטבח  ") == 1


def test_departments_may_share_a_floor():
    assert floor_of("אף אוזן וגרון") == floor_of("הנדסה רפואית") == 3
    assert floor_of("אספקה סטרילית") == floor_of("מטבח") == 1


# ---------- is_correct_floor ----------

def test_correct_pair():
    assert is_correct_floor("יולדות", 9) is True


def test_wrong_pair():
    assert is_correct_floor("יולדות", 3) is False


def test_unknown_department_is_never_correct():
    assert is_correct_floor("מחלקה שאינה קיימת", 4) is False


# ---------- רגרסיה: באג קדימות and/or ----------
# בגרסה הקודמת התנאי נכתב כך:
#     department == "אף אוזן וגרון" or department == "הנדסה רפואית" and floor == 3
# פייתון קושר and חזק מ-or, ולכן זה נקרא:
#     (department == "אף אוזן וגרון") or (department == "הנדסה רפואית" and floor == 3)
# התוצאה: "אף אוזן וגרון" החזיר "הקומה נכונה" בכל קומה שהיא.

def test_ent_department_is_rejected_on_the_wrong_floor():
    assert is_correct_floor("אף אוזן וגרון", 3) is True
    assert is_correct_floor("אף אוזן וגרון", 99) is False
    assert is_correct_floor("אף אוזן וגרון", 1) is False


def test_sterile_supply_is_rejected_on_the_wrong_floor():
    assert is_correct_floor("אספקה סטרילית", 1) is True
    assert is_correct_floor("אספקה סטרילית", 7) is False


def test_shops_are_rejected_on_the_wrong_floor():
    assert is_correct_floor("חנויות", 4) is True
    assert is_correct_floor("חנויות", 2) is False


# ---------- parse_floor ----------

def test_parse_floor_accepts_a_number():
    assert parse_floor("9") == 9
    assert parse_floor("  7  ") == 7


def test_parse_floor_rejects_text():
    assert parse_floor("תשע") is None
    assert parse_floor("") is None
    assert parse_floor("3.5") is None


# ---------- שלמות הנתונים ----------

def test_every_floor_is_within_the_building():
    assert all(1 <= floor <= 10 for floor in FLOORS.values())


def test_no_department_name_has_stray_spaces():
    assert all(name == name.strip() for name in FLOORS)
