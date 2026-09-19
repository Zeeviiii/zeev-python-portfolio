"""בדיקת התאמה בין מחלקה לקומה — בית החולים שערי צדק.

התוכנית קוראת זוגות של שם מחלקה ומספר קומה, ובודקת אם הקומה נכונה.
מפת המחלקות יושבת במילון אחד, ולכן הוספת מחלקה היא שורה אחת של נתונים
ולא ענף elif נוסף.

הרצה:
    python3 zeev_hospital.py

הרצה עם קובץ קלט:
    python3 zeev_hospital.py < departments.txt

בדיקות:
    pytest
"""

# מקור האמת היחיד של התוכנית: מחלקה -> קומה.
# שתי מחלקות יכולות לחלוק קומה, וזה נשמר כאן באופן טבעי.
FLOORS: dict[str, int] = {
    "אספקה סטרילית": 1,
    "מטבח": 1,
    "חדר ניתוח": 2,
    "אף אוזן וגרון": 3,
    "הנדסה רפואית": 3,
    "מרפאת חוץ": 4,
    "חנויות": 4,
    "יציאה": 4,
    "אורטופדיה": 5,
    "כירורגיה כללית": 6,
    "מחלקת ילדים": 7,
    "פנימית": 8,
    "יולדות": 9,
    "מחלקת לב": 10,
}


def floor_of(department: str) -> int | None:
    """מחזיר את הקומה של המחלקה, או None אם המחלקה אינה ברשימה.

    רווחים מיותרים בקצוות הקלט מנוקים, כך שגם "  מטבח " יימצא.
    """
    return FLOORS.get(department.strip())


def is_correct_floor(department: str, floor: int) -> bool:
    """בודק אם המחלקה אכן נמצאת בקומה שנמסרה.

    מחלקה שאינה ברשימה מחזירה False — לא מניחים שהיא נכונה.
    """
    return floor_of(department) == floor


def parse_floor(raw: str) -> int | None:
    """ממיר טקסט למספר קומה. מחזיר None אם הקלט אינו מספר שלם."""
    try:
        return int(raw.strip())
    except ValueError:
        return None


def main() -> None:
    """לולאת הבדיקה: קוראת זוגות עד שנגמר הקלט, ומסכמת בסוף."""
    checked = 0
    correct = 0

    print("בדיקת מחלקה מול קומה. סיום — כשנגמר הקלט.\n")

    while True:
        try:
            department = input("הכנס שם מחלקה: ")
            raw_floor = input("הכנס מספר קומה: ")
        except EOFError:
            break

        floor = parse_floor(raw_floor)
        if floor is None:
            print(f"  '{raw_floor.strip()}' אינו מספר קומה תקין.\n")
            continue

        expected = floor_of(department)
        if expected is None:
            print(f"  המחלקה '{department.strip()}' אינה ברשימה.\n")
            continue

        checked += 1
        if floor == expected:
            correct += 1
            print("  הקומה נכונה\n")
        else:
            print(f"  הקומה שגויה — {department.strip()} נמצאת בקומה {expected}\n")

    if checked == 0:
        print("לא התקבלו בדיקות. הזינו זוגות של שם מחלקה ומספר קומה.")
    else:
        print(f"סיכום: {correct} נכונות מתוך {checked} בדיקות.")


if __name__ == "__main__":
    main()
