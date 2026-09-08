# 1. Record architecture decisions

**Status:** Accepted
**Date:** Sprint 0

## Context

Six months from now, someone — probably me — will look at a non-obvious choice
in this codebase and wonder why. Reconstructing reasoning from a diff is slow
and usually wrong.

## Decision

Every non-obvious architectural choice gets a short record in this folder:
context, the options considered, the decision, and the consequences. Numbered
sequentially, never edited after acceptance — superseded by a new record
instead.

An ADR is not needed for routine work. It is needed when a future reader would
reasonably ask "why is it like this?"

## Consequences

Writing these takes ten minutes and makes the reasoning reviewable, not just
the code. It also forces the alternatives to be named, which occasionally
changes the decision.
