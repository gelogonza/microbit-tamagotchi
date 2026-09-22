# Changelog

Project-level update log. One entry per meaningful change to code, structure, or
approach. The human-readable companion to `git log` — this records *why*, git
records *what*.

Add an entry when you change behavior, retire or add a trial, restructure a
folder, or reach a version boundary. Not for typo fixes.

Tag version boundaries in git so they are findable:

```
git tag -a v1 -m "First working prototype"
git push origin v1
```

Do **not** version by copying folders (`code/v1/`, `code/v2/`). Git already holds
every prior state. Copies drift, and reviewers cannot tell which one is live.

Format: newest first.

---

## [Unreleased]

### Added
-

### Changed
-

### Learned
-

---

## [v0.1] — YYYY-MM-DD — Template as cloned

### Added
- Starter code in `code/`.
- Learning Manual index with main goal, understanding map, and one setup pass.
- Testing plan with three planned trials, RT-01 to RT-03, none yet run.

### Learned
- Nothing yet. This entry exists so the next one has something to differ from.
