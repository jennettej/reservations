# Project Status Report
> Authored by Jonathan Miller using AI, feel free to update.

## Backlog Progress
| User Story | Status | Contributor(s) |
|------------|--------|----------------|
| Clerk: Enter new reservation | Partial (name/date/room/cost in availability.py; add to txt in main.py) | Braden Salter, Dylan Kelleher |
| Clerk: Check out reservation | Done (close_reservation in miller.py) | Jonathan Miller |
| Clerk: Search by guest name | Done (ReservationSearch.py) | Wesley Murray |
| Clerk: View current reservations | Done (data.py load + main.py read) | McKinley Lowery, Jonathan Miller |
| Manager: View room availability | Partial (check_availability in garris.py; view_occupied_rooms) | Rush Garris, Holladay Industries |
| Manager: Daily occupancy report | Todo | - |
| Housekeeping: See occupied/vacant rooms | Done (view_occupied_rooms uses garris.py) | Rush Garris |
| Housekeeping: Update room status | Done (update_room_status) | Rush Garris |
| Others (modify, assign room, etc.) | Todo/WIP | Various |

**Notes**: Clerk CRUD (create/read/search/close) tested/working via data.py/utils. Housekeeping complete. Strong branching/PRs. Team: Braden Salter (res logic), Rush Garris (housekeeping/avail), Dylan Kelleher (file ops), Wesley Murray (search), Jonathan Miller (dates/close/persistence/tests), Holladay (dates/avail).

> Some people made noticable changes and have not been noted here, please edit this if you have contributed to the project and are not listed here.

## Current Structure
```
User Input (CLI menus) 
    ↓
main.py (Menus: Clerk/Manager/Housekeeping)
    ├── data.py (JSON load/save reservations.json)
    ├── utils: garris.py (dates/avail), miller.py (dates/close), ReservationSearch.py
    ├── availability.py (room logic - needs integration)
    └── tests.py (low-level tests)
```
- Loads/Saves: ✅ JSON persistence after mods.
- Issues: Globals/hardcoded in availability.py; partial main.py integration; room_status.txt still txt.

## Compliance Check
- ✅ Modular files, branching/PRs.
- ✅ Full persistence (JSON load/save).
- ⚠️ Clear interfaces (some globals/hardcoded).
- ✅ 5+ tests (tests.py: CRUD + dates/edges).
- ✅ Backlog exists.
- ✅ Diagram (below).
- ✅ Descriptive commits.

**Simple System Diagram**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│   main.py Menus  │───▶│ Data Files      │
│ (CLI login)     │    │ (Clerk/Mgr/Hskp) │    │ (JSON/TXT)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                       ┌──────▼──────┐
                       │ Utils: dates │
                       │ avail check  │
                       └──────────────┘
```

## Fixes Needed
**Remaining**:
1. Integrate availability.py into main.py (no globals).
2. Convert room_status.txt → JSON.
3. Edge tests: Overlap dates, invalid rooms.
4. 

**Maintainability**: Small funcs, docstrings present, no globals → easy pickup.
