# בדיקת מחלקה מול קומה — בית החולים שערי צדק
# התוכנית שואלת שם מחלקה ומספר קומה, ובודקת אם הקומה נכונה.


# מילון: שם מחלקה -> מספר קומה
# במקום 12 ענפי elif, כל מחלקה היא שורה אחת כאן.
FLOORS = {
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


def floor_of(department):
    # מוריד רווחים מההתחלה ומהסוף: "  מטבח " -> "מטבח"
    department = department.strip()

    # אם המחלקה נמצאת במילון — מחזירים את הקומה שלה
    if department in FLOORS:
        return FLOORS[department]

    # אם לא — מחזירים None, כלומר "אין תשובה"
    return None


def is_correct_floor(department, floor):
    # נכון רק אם הקומה שבמילון שווה לקומה שהמשתמש הקליד
    return floor_of(department) == floor


def parse_floor(text):
    # מנסה להפוך טקסט למספר.
    # אם זה לא מספר (למשל "תשע") — מחזיר None במקום לקרוס.
    try:
        return int(text.strip())
    except ValueError:
        return None


def main():
    times = parse_floor(input("כמה מחלקות לבדוק? "))
    if times is None:
        print("צריך להקליד מספר.")
        return

    correct = 0
    count = 0
    while count < times:
        department = input("הכנס שם מחלקה: ")
        floor = parse_floor(input("הכנס מספר קומה: "))
        count += 1

        if floor is None:
            print("  זה לא מספר קומה.")
        elif floor_of(department) is None:
            print("  המחלקה לא ברשימה.")
        elif is_correct_floor(department, floor):
            print("  הקומה נכונה")
            correct += 1
        else:
            print("  הקומה שגויה — המחלקה נמצאת בקומה", floor_of(department))

    print("סיכום:", correct, "נכונות מתוך", times)


# מפעיל את main רק כשמריצים את הקובץ ישירות.
# בלי השורה הזו, הבדיקות (pytest) היו מפעילות את התוכנית ונתקעות על input.
if __name__ == "__main__":
    main()
