# Learning passes

One file per pass. Append-only.

Naming: `YYYY-MM-DD-NN-slug.html` — `2026-09-15-03-scheduler-collision.html`
(`NN` is the pass number, so same-day passes sort correctly.)

## The rule that makes these worth keeping

**Do not edit a pass after you commit it.**

A pass is what you understood on that date. When you later discover you were
wrong, that is not a defect to be patched — it is the most valuable thing in the
manual. Write the correction in a *new* pass that links back:

> Pass 07 corrects pass 03. I claimed the forever loop always yields to button
> handlers. RT-02 showed the opposite under scrolling. What I got wrong was
> assuming `show_number` is non-blocking.

That sequence is a record of learning. An edited pass 03 is a record of nothing.

Fixing a typo or a broken link is fine. Changing a claim, a result, or a
conclusion is not.

## Linking

Each pass should link to any Resilience Trial it draws on
(`../../../testing/team-resilience-trials.md`) and any observation it
rests on (`../../notes/...`, if you created that folder). The trial holds the protocol and
result; the note holds the contemporaneous observation; the pass holds what you
concluded. Keeping them separate is what lets a reader check your reasoning
against your data.
