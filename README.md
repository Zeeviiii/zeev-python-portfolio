# Python — Zeev Tapoohi

[![tests](https://github.com/Zeeviiii/zeev-python-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/Zeeviiii/zeev-python-portfolio/actions/workflows/tests.yml)

Python I write while moving from hospital sterile supply into software.
Practical Engineer in Software, with a background in C, C++, Java, C# and Assembly.

**Every program here runs live in the browser:** [zeeviiii.github.io](https://zeeviiii.github.io/)

---

## From the sterile supply department

I have worked in the sterile supply department at Shaare Zedek Medical Center
for 14 years. These programs come from problems I actually run into there.

| Program | Problem it solves |
|---|---|
| [`zeev_hospital.py`](zeev_hospital.py) | Checks a department against the floor it belongs on. Dictionary-driven, type hints, handles bad input. **Covered by 14 tests.** |
| [`zeev_sterilizer_check.py`](zeev_sterilizer_check.py) | Reads a batch of autoclave cycle temperatures and counts how many fell inside the 121–134°C window. |
| [`zeev_checklist.py`](zeev_checklist.py) | Walks the four machines in turn and reports which are up to temperature. |
| [`zeev_heat.py`](zeev_heat.py) | Validates a machine number and its temperature together, and says what is wrong when they disagree. |
| [`zeev_badge_check.py`](zeev_badge_check.py) | Reads an employee badge and grants access from the site prefix. |

---

## Everything else

The rest of the repository is the coursework behind those programs — conditionals,
loops, strings, lists and functions, written by hand one topic at a time while
working through **Google IT Automation with Python**. PCAP is next.

I am keeping them here on purpose. They are not polished, and they are not meant
to be: they are the record of how I got from the first line to the programs above.

---

## Running a program

```bash
python3 zeev_hospital.py
```

Programs that read input also accept a file:

```bash
python3 zeev_hospital.py < departments.txt
```

## Running the tests

```bash
pip install pytest
pytest -v
```

The same tests run automatically on every push, on Python 3.10 and 3.12 —
that is the badge at the top of this page.

---

## Contact

Open to junior Python, automation and QA roles in Israel.

- Email — <zv.tapoohii@gmail.com>
- LinkedIn — [zeevtapoohi](https://www.linkedin.com/in/zeevtapoohi)
- Site — [zeeviiii.github.io](https://zeeviiii.github.io/)
