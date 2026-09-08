# CareBridge — scope

## What it is

A white-label virtual care portal. Each **organization** gets an isolated
tenant; **patients** book appointments with **providers**; **org admins**
manage staff and settings.

## Sprints

| # | Focus | Status |
|---|---|---|
| 0 | Foundations — settings, Docker, tooling, CI, custom user model | in progress |
| 1 | Data model and migrations | |
| 2 | Multi-tenancy and auth | |
| 3 | Appointment API | |
| 4 | Async and integration pipeline | |
| 5 | React frontend | |
| 6 | Production concerns | |

## Explicitly out of scope

Real video, real payments, real FHIR parsing, Kubernetes, microservices, mobile
apps. All stubbed or omitted. The engineering interest is in tenancy,
concurrency, and the async pipeline.

## Definition of done

Every ticket:

- [ ] Tests pass, types check, lint clean
- [ ] Migration included if a model changed
- [ ] README updated if setup or behaviour changed
- [ ] PR description explains *why*, not *what*
- [ ] No PHI or secrets in logs, fixtures, or test data
