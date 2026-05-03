# Project Status Report
> Authored by Jonathan Miller using AI assistance, feel free to update.

## Backlog Progress
| User Story | Status | Contributor(s) |
|------------|--------|----------------|
| Clerk: Enter new reservation | Done (add_reservation in edit.py; JSON via data.py) | Braden Salter, Dylan Kelleher, Nick Kulju, team PRs |
| Clerk: Check out reservation | Done (close_reservation + close_reservation_cli in miller.py; wired in main.py) | Jonathan Miller |
| Clerk: Search by guest name | Done (ReservationSearch.py + Clerk menu) | Wesley Murray |
| Clerk: View current reservations | Done (read via edit.py / main.py; data.py) | McKinley Lowery, Jonathan Miller |
| Clerk: Change reservation | Done (edit_reservation in edit.py + Clerk menu) | Team (edit.py PRs) |
| Manager: Search reservations | Done (same search path as Clerk + Manager menu) | Wesley Murray |
| Manager: View room availability | Partial (check_availability in garris.py; view_occupied_rooms for housekeeping) | Rush Garris, Holladay Industries |
| Manager: Daily occupancy report | Todo | - |
| Housekeeping: See occupied/vacant rooms | Done (view_occupied_rooms loads JSON + garris.check_availability) | Rush Garris |
| Housekeeping: Update room status | Done (update_room_status → room_status.txt) | Rush Garris |
| Others (assign room, deeper availability UI, etc.) | Partial/WIP | Various |

**Notes**: Clerk and Manager share book/show/change/find/close flows against `reservations.json`. Housekeeping uses `room_status.txt` plus reservation JSON for occupancy. `availability.py` is not invoked from `main.py` today (booking uses `edit.py` + `garris.validate_date`). Strong branching/PRs. Team: Braden Salter (res logic), Rush Garris (housekeeping/avail), Dylan Kelleher (file ops), Wesley Murray (search), Jonathan Miller (dates/close/persistence/tests), Holladay (dates/avail).

> Some people have likely made noticable changes and have not been noted here, please edit this if you have contributed to the project and are not listed here.

## Current Structure
```
User Input (CLI menus) 
    ↓
main.py (Menus: Clerk / Manager / Housekeeping)
    ├── data.py (loads/saves reservations in reservations.json)
    ├── edit.py (add / edit / read reservations + validation)
    ├── garris.py (validate_date, check_availability)
    ├── miller.py (close reservation, date string helpers, CLI close flow)
    ├── ReservationSearch.py (search by property)
    ├── reservations.json (reservation records: guest, room, dates, confirmation)
    ├── room_status.txt (housekeeping clean/dirty room status)
    └── (standalone: tests.py — not imported by menus)
```
- Loads/Saves: Reservations are stored in `reservations.json`; room clean/dirty status is stored in `room_status.txt`.
- Issues: `availability.py` still has legacy/global-style patterns and is unused by the runtime menu path; optional helpers (`save_load_file.py`, `list_write.py`) exist but are not part of `main.py`; room data split across JSON + TXT.

## Files Not Currently Used by `main.py`
- `date_after_dh.py`
- `tests.py`
- `availability.py`
- `save_load_file.py`
- `list_write.py`

## Compliance Check
- ✅ Modular files, branching/PRs.
- ✅ Full persistence (JSON load/save for reservations).
- ⚠️ Clear interfaces (some hardcoded paths/room counts).
- ✅ 5+ exercised paths in tests.py (create, read, list, search by name/confirm, close, restore).
- ✅ Backlog exists.
- ✅ Diagram (below).
- ✅ Descriptive commits.

**Simple System Diagram**
```
                              ┌──────────────┐
                              │  User (CLI)  │
                              └──────┬───────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │       main.py         │
                         │  Clerk / Mgr / Hskp   │
                         └───────────┬───────────┘
                                     │
         ┌───────────────────────────┼────────────────────────────┐
         │ menu actions call         │                            │
         ▼                           │                            │
┌────────────────────────────┐       │     Housekeeping menus     │
│    Helper utilities        │       │     (in main.py)           │
│                            │       │                            │
│  data.py      ─┐           │       │  · show / update lines     │
│  edit.py       ├── JSON   │       │    in room_status.txt      │
│  miller.py     │   I/O    │       │  · “occupied” also loads   │
│  ReservationSearch.py      │       │    JSON + calls garris     │
│  garris.py    ─┘           │       │                            │
│  (dates, check_availability│       │                            │
│   on reservation lists)    │       │                            │
└──────────────┬─────────────┘       └─────────────┬────────────┘
               │                                    │
               │ load / save                        │ read / write
               │ reservation records                │ clean | dirty
               ▼                                    ▼
     ┌─────────────────────┐              ┌─────────────────────┐
     │  reservations.json  │              │  room_status.txt    │
     │  guests, rooms,     │              │  one line per room   │
     │  dates, confirm #   │              │  (e.g. Room 1: …)    │
     └─────────────────────┘              └─────────────────────┘
```

Flow in words: **Clerk and Manager** go through the helper modules, which read and write **`reservations.json`**. **Housekeeping** updates **`room_status.txt`** directly from `main.py`; the “occupied rooms” option still uses **`reservations.json`** (loaded in code) together with **`garris.check_availability`**.

## Fixes Needed
**Remaining**:
1. Use or drop: wire `availability.py` into menus or keep it as a standalone helper only.
2. Convert `room_status.txt` → JSON (optional consistency with reservations).
3. Automated tests: overlap dates, invalid rooms, confirmation collisions (beyond manual tests.py script).
4. Manager: daily occupancy report user story.

**Maintainability**: Small functions and docstrings in core modules; persistence centralized in `data.py`; align or retire `availability.py` if the live menu path should use it.
