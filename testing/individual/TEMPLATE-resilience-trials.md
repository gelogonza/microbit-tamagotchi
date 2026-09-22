# Additional Resilience Trials — [Your Name]

> Unit 1 is an individual project. You usually do not need this extra file.
> Copy and rename it only if your main project-trials file becomes too long.

**Username:** [your GitHub username]
**Role on this project:** Designer, programmer, fabricator, tester, and documentarian
**Learning objectives:** [the two from your Learning Manual]

Record trials tied to your implementation and learning objectives. Do not copy
results from the main project-trials file.

---

## Trial IND-01: Does the block tour actually convert? (worked example)

> This example uses `code/reference/block_tour.py`. It is here to show the level
> of specificity expected. Replace it with a trial on your own work.

**Question or boundary:** MakeCode Python → Blocks conversion is
all-or-nothing: one unsupported construct hides every block in the file. The
tour file's section 9 contains two identifiers that have **not** been verified
against the current editor. Which one, if either, breaks conversion?

**Prototype version:** `code/reference/block_tour.py` as cloned, commit ______

**Protocol:**
1. Paste the whole file into the MakeCode Python tab. Click **Blocks**.
2. Record the exact error text and line number, or "converted" if it works.
3. Delete section 9 entirely (everything below the V2 banner). Click Blocks again.
4. Restore section 9. Delete only the `input.on_logo_event(...)` line and its
   handler. Click Blocks again.
5. Restore. Delete only the `soundExpression.giggle.play()` line. Click Blocks again.
6. For whichever identifier failed: drag the equivalent block onto the canvas
   from the toolbox, switch to the Python tab, and record the name MakeCode
   actually generates.

**Measure or observation:** Converts or does not, per condition. Exact error
text. The generated identifier from step 6.

**Pass criterion:** I can state which identifier is wrong and what the correct
one is, with the editor's own generated code as evidence.

**Results:**

| Condition | Converted? | Error text |
|---|---|---|
| Whole file as cloned |  |  |
| Section 9 removed |  |  |
| `on_logo_event` line removed |  |  |
| `soundExpression` line removed |  |  |

Correct identifier from step 6: ______

Board version I am testing on (V1 / V2): ______

**Supporting record:** a named folder beneath `curriculum/` — screenshot of the error, screenshot of the
generated Python from step 6.

**What I learned and next action:**

---

## Trial IND-02: [your own]

**Question or boundary:**

**Prototype version:**

**Protocol:**
1.
2.
3.

**Measure or observation:**

**Pass criterion:**

**Results:**

**Evidence:**

**What I learned and next action:**
