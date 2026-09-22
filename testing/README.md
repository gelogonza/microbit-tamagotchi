# Testing Plan — Individual Project Strategy

Keep this file current. It is the short version: what matters, what is likely
to break, what you test next. Detailed protocols and results live in
`team-resilience-trials.md`.

This folder is optional support for the Week 4 checkpoint. The required Week 4
work is simpler: let two people use the artifact, record what happened in your
notes, and show the revisions that followed. Use a full Resilience Trial when a
repeatable boundary test will help you make a better decision.

> The starter content below describes `code/hello_microbit.py`. Replace it with
> your own project as soon as your project has its own behaviors.

---

## Most important behaviors

| # | The prototype must... | Most likely way it fails |
|---|---|---|
| 1 | Increase the count by exactly one per button A press, and display it | Presses during `show_number` are queued or lost; count and display disagree |
| 2 | Reset to zero on button B | Reset lands mid-display and the old number is still visible |
| 3 | Show a visible "still alive" signal at all times | The heartbeat pixel and the number both write to the display and erase each other |

## Known brittleness

- `basic.show_number` **blocks** while it scrolls. Anything a user does during
  that time is queued or dropped. The starter project has no debounce.
- The forever loop and the button handlers share one 5×5 display with no
  coordination. Whichever ran last wins.
- `count` lives only in RAM. Power loss resets it and the prototype gives the
  user no indication that it did.
- Numbers of 10 or more scroll rather than appearing at once, which changes how
  long the display is blocked and how long input is queued.

## Next trials

1. RT-01 Rapid press accuracy — planned
2. RT-02 Heartbeat and number collision — planned
3. RT-03 Restart recovery — planned

## Safety boundaries for this project

Low risk: USB power only, no external circuit, no moving parts. Rapid button
pressing is the only physical stress and is within normal use.

Re-check this section before adding any external component. Motors, mains
power, heat, and anything with stored energy change the answer.
