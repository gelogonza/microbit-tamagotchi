# Project Resilience Trials

Optional detailed protocols, results, evidence, and decisions for this
individual project. The filename is retained for template compatibility.

A Resilience Trial names a boundary, gives repeatable steps, records a
measurable or observable result, and leads to a decision. The question is not
"can I break it?" — it is *what conditions must this handle, where does it
fail, and what does that failure teach me?*

---

## Template — copy this for each new trial

```
## Trial: [short, specific name]

**Question or boundary:** What must this project handle? What might fail?

**Prototype version:** Commit ID or date

**Protocol:**
1. [exact setup]
2. [exact input or action]
3. [repeat count, duration, or other controlled condition]

**Measure or observation:** What will I count, time, measure, or look for? Include units when useful.

**Pass criterion:** What result would be acceptable for this version of the prototype?

**Results:** Record each trial or a clear summary of repeated trials.

**Evidence:** Link to a photo, video, screenshot, serial log, or other repository file.

**What I learned and next action:** What will I revise, test next, leave unchanged, or ask about?
```

---

## Trial RT-01: Rapid press accuracy

**Question or boundary:** Button A must increase the count by exactly one per
press. `basic.show_number` blocks while it displays. What happens to presses
that arrive during that block — are they queued, or lost?

**Prototype version:** `code/hello_microbit.py`, commit ______

**Protocol:**
1. Flash `hello_microbit.py`. Power on and wait for the heart icon to clear.
2. Press button A exactly 20 times, as fast as you can, counting aloud.
3. Stop. Wait 10 seconds for the display to finish.
4. Read the final number.
5. Repeat the full sequence 3 times, resetting with button B between runs.

**Measure or observation:** Presses made (20) vs. final count displayed, per
run. Also note how far behind the display is when you stop pressing.

**Pass criterion:** Final count is within 1 of 20 on all three runs.

**Results:**

| Run | Presses | Final count | Display lag when I stopped | Notes |
|---|---|---|---|---|
| 1 | 20 |  |  |  |
| 2 | 20 |  |  |  |
| 3 | 20 |  |  |  |

**Supporting record:** a named folder beneath `curriculum/`, created if needed — photo of final display, one per run.
**Contemporaneous observation:** `curriculum/notes/YYYY-MM-DD-rt01-run.md`, written and committed the day you run this.

**What I learned and next action:**

---

## Trial RT-02: Heartbeat and number collision

**Question or boundary:** The forever loop plots a pixel at (4,0) every 500 ms
while button handlers write numbers to the same display. Both are correct on
their own. Do they interfere, and is the result confusing to a user?

**Prototype version:** `code/hello_microbit.py`, commit ______

**Protocol:**
1. Power on and let the heartbeat run alone for 10 seconds. Confirm the corner
   pixel blinks about once per second.
2. Press button A once. Watch the full display cycle without touching anything.
3. Record whether the corner pixel appears on top of the digit, interrupts it,
   or disappears.
4. Press A until the count reaches 10 or more, so the number scrolls. Repeat
   the observation.
5. Do steps 2–4 three times.

**Measure or observation:** Is the digit readable? Does the heartbeat survive?
Describe what a person who has never seen the device would think is happening.

**Pass criterion:** The digit is readable and the heartbeat is still
recognizable as a repeating signal.

**Results:**

| Condition | Digit readable? | Heartbeat visible? | What it looks like |
|---|---|---|---|
| Single digit |  |  |  |
| Scrolling (10+) |  |  |  |

**Supporting record:** a named folder beneath `curriculum/`, created if needed — short video or a sequence of photos.
**Contemporaneous observation:** `curriculum/notes/YYYY-MM-DD-rt02-run.md`

**What I learned and next action:**

---

## Trial RT-03: Restart recovery

**Question or boundary:** `count` is held in RAM. What does a user see and
believe after an unexpected power loss?

**Prototype version:** `code/hello_microbit.py`, commit ______

**Protocol:**
1. Press A until the count reads 7. Confirm the display.
2. Unplug USB power. Wait 5 seconds.
3. Reconnect power. Do not press anything.
4. Record what the display shows, and how long until the device is responsive.
5. Press A once. Record the number displayed.
6. Repeat 3 times.

**Measure or observation:** Displayed value after restart; time from power-on to
first response, in seconds; value shown after the first press.

**Pass criterion:** Define one before running. Is silently resetting to zero
acceptable for this version, or must the user be told?

**Results:**

| Run | Count before | Shown after restart | Time to responsive (s) | After first press |
|---|---|---|---|---|
| 1 | 7 |  |  |  |
| 2 | 7 |  |  |  |
| 3 | 7 |  |  |  |

**Supporting record:** a named folder beneath `curriculum/`, created if needed.
**Contemporaneous observation:** `curriculum/notes/YYYY-MM-DD-rt03-run.md`

**What I learned and next action:**

---

## Add your trials below

Write the observation in an evidence note **while you run the trial**, commit
it that day, and link it from the trial. The results table here is the summary;
the note is the primary record.

As your project becomes specific, these starter trials should be retired and
replaced. A trial that no longer tests a real boundary of your prototype is
not worth running.
