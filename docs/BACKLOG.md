# Backlog

Paste each into a GitHub Issue. One branch per ticket, one PR per branch.

---

# Sprint 0 — remaining

The scaffold is done. These three are yours. They're chosen because each one
requires understanding something in the codebase rather than copying it.

---

## CB-1 · Get the environment running and prove it

**Goal:** a fresh clone runs, migrations apply, tests pass, and you can log
into the admin.

**Acceptance criteria**
- [ ] `docker compose up` starts web, db and redis with no errors
- [ ] `makemigrations users` produces `0001_initial.py` and it is committed
- [ ] `migrate` applies cleanly
- [ ] `pytest` passes
- [ ] `createsuperuser` works and you can reach `/admin/`
- [ ] Anything that was painful is fixed in the README

**Notes:** the migration is *not* in the repo. Generating it yourself is the
point — look at what Django produces and read it before committing.

---

## CB-2 · Write ADR 0002: why a custom user model with email login

**Goal:** a decision record explaining a choice already made in the code.

**Acceptance criteria**
- [ ] `docs/decisions/0002-custom-user-model.md` following the 0001 format
- [ ] Explains why `AUTH_USER_MODEL` must be set before the first migration
- [ ] Explains `AbstractBaseUser` vs `AbstractUser` and why the latter was
      rejected
- [ ] Names at least one consequence or cost of the decision

**Notes:** read `apps/users/models.py` first. The reasoning is in the
docstrings, but writing it as an ADR forces you to state the alternatives.

---

## CB-3 · Complete the email uniqueness test

**Goal:** finish the TODO at the bottom of `tests/test_users.py`.

**Acceptance criteria**
- [ ] A test proving two users cannot share an email
- [ ] A test covering the case where emails differ only by letter case
- [ ] Both pass; you can articulate which layer raises, and why

**Notes:** think about whether the case-insensitivity is enforced by the
database or by `UserManager`. They are not the same guarantee, and the
difference matters. Your answer goes in the PR description.

---

## CB-4 · Complete production settings

**Goal:** `config/settings/production.py` is currently a stub with a TODO.
Make it deployment-ready.

**Acceptance criteria**
- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` from the environment, required, fails loudly if absent
- [ ] `ALLOWED_HOSTS` from the environment, never `"*"`
- [ ] Security headers appropriate to health data
- [ ] Browsable API renderer disabled
- [ ] `python manage.py check --deploy --settings=config.settings.production`
      passes with zero warnings
- [ ] A test asserting `DEBUG` is False under production settings

**Notes:** `check --deploy` will tell you exactly what's missing. Work through
its warnings one at a time and understand what each is protecting against —
don't just silence them.

---

# Sprint 1 — Data model

Not started. Do not begin until Sprint 0 is merged.

## CB-5 · Organization model (the tenant)
## CB-6 · Extend User with role and organization
## CB-7 · Provider profile and working hours
## CB-8 · AppointmentType with duration
## CB-9 · Appointment model with constraints
## CB-10 · AuditLog, append-only
## CB-11 · ADR 0003: tenant isolation strategy

Full descriptions when Sprint 0 closes.
