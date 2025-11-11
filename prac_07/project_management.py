"""
CP1404 Practical – Project Management Program
"""

import csv
from datetime import datetime
from pathlib import Path
from project import Project, DATE_FORMAT, COMPLETION_TARGET

# ───────────────────────── Constants ────────────────────────── #
DEFAULT_FILE = Path("projects.txt")
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
YES = "y"
NO = "n"

DELIMITER = "\t"
FILE_HEADER = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]

# ─────────────────────────── main() ─────────────────────────── #
def main():
    """Run the interactive menu loop."""
    projects = load_projects(DEFAULT_FILE)
    print(f"Welcome – {len(projects)} projects loaded from {DEFAULT_FILE}")
    _menu_loop(projects)


# ───────────────────────── Menu & actions ───────────────────── #
def _menu_loop(projects: list[Project]) -> None:
    """Show the main menu until user quits."""
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            projects[:] = load_projects(Path(input("Filename: ")))
        elif choice == "s":
            save_projects(Path(input("Filename: ")), projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_by_date(projects)
        elif choice == "a":
            projects.append(prompt_new_project())
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()

    if input(f"Save to {DEFAULT_FILE}? ({YES}/{NO}): ").lower() == YES:
        save_projects(DEFAULT_FILE, projects)
    print("Good-bye.")


# ──────────────────────── File I/O helpers ──────────────────── #
def load_projects(filename: Path) -> list[Project]:
    """Return Project objects read from a tab-separated file."""
    projects: list[Project] = []
    if filename.exists():
        with filename.open(newline="") as file:
            reader = csv.reader(file, delimiter=DELIMITER)
            next(reader, None)          # skip header
            for name, start, pri, cost, pct in reader:
                projects.append(Project(name, start, int(pri), float(cost), int(pct)))
    else:
        print(f"{filename} not found – starting with empty list.")
    return projects


def save_projects(filename: Path, projects: list[Project]) -> None:
    """Write projects to a tab-separated file."""
    with filename.open("w", newline="") as file:
        writer = csv.writer(file, delimiter=DELIMITER)
        writer.writerow(FILE_HEADER)
        for p in projects:
            writer.writerow(
                [p.name, p.start_date.strftime(DATE_FORMAT), p.priority,
                 f"{p.cost_estimate:.2f}", p.completion_percent]
            )
    print(f"{len(projects)} projects saved to {filename}")


# ───────────────────────── Display logic ────────────────────── #
def display_projects(projects: list[Project]) -> None:
    """Print incomplete then completed projects (by priority)."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for proj in incomplete:
        print(f"  {proj}")

    print("Completed projects:")
    for proj in complete:
        print(f"  {proj}")


def filter_by_date(projects: list[Project]) -> None:
    """Show projects starting after a user-entered date."""
    date_obj = _prompt_date("Filter date (dd/mm/yyyy): ")
    filtered = sorted((p for p in projects if p.start_date > date_obj),
                      key=lambda p: p.start_date)
    for proj in filtered:
        print(proj)


# ───────────────────── Add / Update operations ───────────────── #
def prompt_new_project() -> Project:
    """Collect user data and return a new Project."""
    name = input("Name: ")
    start_date = _prompt_date("Start date (dd/mm/yyyy): ")
    priority = _prompt_int("Priority: ")
    cost = _prompt_float("Cost estimate: $")
    percent = _prompt_int("Percent complete: ")
    return Project(name, start_date.strftime(DATE_FORMAT), priority, cost, percent)


def update_project(projects: list[Project]) -> None:
    """Let the user update completion and/or priority of a project."""
    for i, proj in enumerate(projects):
        print(f"{i} {proj}")
    index = _prompt_int("Project number: ")
    if 0 <= index < len(projects):
        proj = projects[index]
        print(proj)
        new_pct = input("New percentage (blank = keep): ")
        if new_pct:
            proj.completion_percent = _safe_int(new_pct, proj.completion_percent)
        new_pri = input("New priority (blank = keep): ")
        if new_pri:
            proj.priority = _safe_int(new_pri, proj.priority)
    else:
        print("Invalid project number.")


# ───────────────────────── Input helpers ─────────────────────── #
def _prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid integer.")


def _prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def _prompt_date(prompt: str):
    while True:
        try:
            return datetime.strptime(input(prompt), DATE_FORMAT).date()
        except ValueError:
            print("Enter date as dd/mm/yyyy.")


def _safe_int(text: str, current: int) -> int:
    try:
        return int(text)
    except ValueError:
        return current


if __name__ == "__main__":
    main()
