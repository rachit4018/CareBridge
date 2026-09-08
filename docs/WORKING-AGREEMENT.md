# Working agreement

I'm acting as your tech lead and scrum master. This is how we work.

## The loop

1. **You pick the next ticket** from `docs/BACKLOG.md`, top of the list.
2. **Branch** — `feat/CB-3-email-uniqueness-test`.
3. **Build it.** Commit in logical steps, conventional commit messages.
4. **Open a PR** against `main` with a real description.
5. **Submit for review** — paste the diff, or share the PR link.
6. **I review** — blocking comments vs suggestions, clearly marked.
7. **You address feedback**, I re-review, you merge.

Never push straight to `main`. Even alone. Especially alone.

## What I review for

In this order, because that's the order that matters:

**Correctness.** Does it do what the ticket asked? What happens on the empty
case, the concurrent case, the downstream-is-down case?

**Django idiom.** Are you writing Django, or FastAPI in Django's clothing?
This is the main thing you're here to learn and where most of my comments will
land early on.

**Tests.** Do they test behaviour or implementation? Would they catch a
regression? Is the failure message useful?

**Data model and migrations.** Reversible? Safe on a large table? Constraints
in the database where they belong?

**Git hygiene.** Atomic commits, readable messages, PR description that
explains *why*.

**Security and compliance.** No PHI in logs. No secrets in code. Deny by
default.

## Comment format

- **[BLOCKING]** — must change before merge.
- **[SUGGESTION]** — I'd do it differently; your call.
- **[QUESTION]** — I don't understand something; explain and I may withdraw it.
- **[PRAISE]** — genuinely good, so you repeat it.

If you disagree with a blocking comment, say so and argue. Being talked out of
a review comment is a normal outcome, and pushing back well is a senior skill.

## Standups

Post before each session:

```
Yesterday: CB-3, got uniqueness test passing at the DB layer
Today:     CB-4, production settings
Blocked:   unsure whether case-insensitive uniqueness should be a
           constraint or a manager concern
```

Keep it to three lines. The blocker line is the one that matters.

## Progress tracking

At the end of each sprint I'll give you a written review covering:

- **Velocity** — tickets closed vs planned, and whether estimates are honest
- **Code quality trend** — are the same comments recurring?
- **Django fluency** — measured by how often I have to say "that's the
  FastAPI way"
- **Testing** — coverage matters less than whether tests catch real bugs
- **What to work on next sprint** — one or two things, specific

I'll be direct. If something is weak, I'll say it's weak and tell you what
good looks like. That's more useful to you than encouragement.

## Rules

**Don't skip the ticket.** If you find yourself building something not in a
ticket, stop and write the ticket first.

**Don't batch.** One ticket per PR. A PR touching four unrelated things can't
be reviewed properly.

**Ask before you're stuck for an hour.** "I don't understand how Django
resolves this" is a fine message. Grinding alone for a day is not efficient
learning.

**When you copy a pattern from somewhere, say so in the PR.** Understanding
where it came from is part of the review.
