# SE239-Smart-Home-Control

# SE239 Smart-Home Control — Deliverable 2

A simple Python TCP client-server foundation for Topic 2.9 (Smart-Home Control).

## Scope (Weeks 6 and 8)
- One client connects and exchanges a message with the server.
- Three or more clients connect simultaneously.
- Each client joins using `LOGIN <username>`.
- The server tracks logged-in users and responds to `PING`, `LIST`, and `QUIT`.

Device controls are planned for a later milestone; no physical devices are required.

## Team
Replace with your four names and contributions:
- Seham Alattar 202500091 — server setup
- Hala Almadi 202501615 — client and login
- Moudhi Aljabr 202402481 — concurrent client handling
- Aljoharah Almajhad 202402481 — testing, documentation, integration

## Requirements
Python 3 (standard library only). No `pip install` needed.

## Run on one computer (macOS)
Open four separate Terminal windows in this folder.

Terminal 1:
```bash
python3 server.py
```

Terminals 2, 3, and 4 (one client per terminal):
```bash
python3 client.py
```

Use different usernames. In each client, type `PING` to exchange a message and `LIST` to view connected users. Keep all three clients open together to demonstrate concurrent connections. Use `QUIT` to leave.

The server binds to `127.0.0.1` on port `5091`, so all terminals must run on the same computer. If that port is occupied, change `PORT` in both files to the same unused port.

## Message format
Messages are UTF-8 text, one command per line (`\n` terminated).

| Client message | Server response | Purpose |
| --- | --- | --- |
| `LOGIN <username>` | `OK Logged in as ...` or `ERROR ...` | Join the system |
| `PING` | `PONG ...` | Confirm a message exchange |
| `LIST` | `USERS ...` | Show logged-in clients |
| `QUIT` | `BYE` | Disconnect cleanly |
| Invalid input | `ERROR ...` | Reject invalid commands |

## Evidence to capture
1. Screenshot of server and one client successfully exchanging `PING`/`PONG` (Week 6).
2. Screenshot showing server and three clients logged in simultaneously (Week 8).
3. Screenshot of `LIST` returning all three usernames.
4. Record actual test outcomes in `evidence.md`; do not mark a test passed until verified.

## Git workflow
Each team member should clone the shared repository, contribute their own work, and push commits from their own GitHub account. Review and integrate changes before capturing final evidence.

## Future work
Later milestones will add simulated light, fan, and door-lock state management and device-control commands.
