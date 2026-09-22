# How much Jev is in the ten "Jev blueprints" — 2026-09-22

On 2026-09-22 a post listing ten GitHub repositories as "complete Jev blueprints"
reached ~71,000 views and ~900 bookmarks. The list is accurate about *what* each
repository does. It says nothing about *how much* of each one is Jev, and that turns
out to vary by more than two orders of magnitude.

This folder measures that, and the measurement runs on any repo and any keyword.

## What is counted

`./howmuch owner/repo jev typesafe` shallow-clones a repository, reads every source
file, and reports the share that mentions the terms at all — then splits those files by
where they sit in the tree, because a keyword that appears only under `tests/` or
`bench/` is not something the repository ships.

**Counting files that *mention* a term is deliberately generous.** A file that names Jev
once counts the same as a file built around it. Every share below is therefore an upper
bound on how much of the repo is about Jev, never an under-count.

Source extensions only (`.py .ts .tsx .js .jsx .rs .go .mjs …`); `node_modules`,
`target`, `dist`, `build`, `.venv` and `vendor` excluded. Read at HEAD on 2026-09-22.

## Result

| repo | ★ | share of source files | Jev in product code |
|---|---|---|---|
| jexp/neo4jev | 91 | 86.7% | 5 files |
| AkashPriyadarshii/jev-curate | 24 | 80.0% | 6 |
| fhshaik/typesafe-mario | 352 | 77.8% | 5 |
| emrickgarrett/OneVOneJev | 20 | 76.2% | 16 |
| RomanSlack/jev-drone | 129 | 58.8% | 10 |
| monteduro/killmyidea | 94 | 50.0% | 17 |
| jarrodwatts/jev-trader | 2042 | 23.5% | 8 |
| qkal/Canny | 38 | 15.4% | 5 |
| irfndi/prism-liquidity-agent | 72 | 1.9% | 4 |
| lahfir/agent-desktop | 1503 | 0.4% | **0** |

Full rows, including commit counts and first/last commit dates, in `data/repos.csv`.

**The list is not padded.** All ten repositories are real and public, and every one of
them reaches the TypeSafe API. The post's own descriptions are accurate — it flags
Prism as judging state and handing off rather than placing orders.

**Two of them predate the SDK.** `agent-desktop` first committed 2026-02-19 and
`prism-liquidity-agent` 2026-06-01; the first SDK release was 2026-09-09 on PyPI and
2026-09-12 on npm. In both, Jev is a layer added to an existing codebase. In
`agent-desktop` it is four files under `scripts/jev/` and appears in no product file.

**Stars do not track Jev content.** The most-starred repo on the list carries 666 lines
in files mentioning Jev; the least-starred carries 3,640.

## Checked and not used

- **No typosquatting.** Three packages carry the name: `typesafe-sdk` (PyPI) and
  `@typesafe-ai/sdk` (npm) from the typesafe-ai org, and `@ai-sdk/typesafe-ai`,
  published by `vercel-release-bot` as part of `vercel/ai`. All three legitimate.
- **GitHub code search was unusable.** It returned 0 hits for `jev` in `jev-curate`,
  whose own `Cargo.toml` contains the word. Every figure here comes from a local clone.
- **Dependency manifests alone were misleading.** Reading only `package.json` /
  `pyproject.toml` / `Cargo.toml` suggested 5 of 10 used Jev. Reading the source showed
  all 10 do — four reach the HTTP API directly without declaring an SDK dependency.
  That first answer was wrong and is recorded here because it was nearly published.

## What this does not show

- It does not show a thin integration is a bad one. A small adapter onto a mature
  codebase may be the right design.
- Mention-share is not usage depth.
- This is HEAD on a single day. Eight of these repositories are under a week old.

## Reproduce

```
./howmuch lahfir/agent-desktop jev typesafe
```

Needs `git` and Python 3. No API key, no network beyond the clone.

---

# Second list, and a claim about both — 2026-09-22

The same account posted a **different** ten-repo checklist on 21.09 (181,000 views,
2,193 bookmarks). Zero overlap with the 22.09 list above. `data/both-lists.csv` holds
all twenty rows, measured the same way.

| repo | ★ | share | Jev in product code |
|---|---|---|---|
| itsmostafa/typesafe-mcp | 258 | 100.0% | 7 files |
| jkudish/jev-mcp | 282 | 100.0% | 3 |
| browser-use/jev-ultrafast | 17962 | 88.2% | 6 |
| tamaratran/fast-jev-compaction | 6289 | 76.9% | 7 |
| ellipsis-dev/blink | 61 | 58.3% | 4 |
| sharziki/semdecide | 36 | 50.0% | 4 |
| GhalebDweikat/winnow | 66 | 27.9% | 9 |
| devagrawal09/jev-review | 544 | 15.8% | 3 |
| 0xNatoshi/jev-codex-router | 219 | 4.7% | 16 |
| vercel-labs/json-render | 18085 | 1.2% | 10 |

The star inversion is sharper here than on the first list. `json-render` (18,085★) and
`jev-ultrafast` (17,962★) carry almost identical star counts and differ by a factor of
seventy in Jev share — 1.2% against 88.2%. `json-render` is also the one repo across
both lists whose first commit predates 2026-09 by months: 2026-01-14.

## The claim this answers

On 2026-09-22 a post with 159,890 followers behind it said: *"i've been looking deeper
into jev 'use-cases' people shared on X and can confirm at least 90% are just larping."*

Across the twenty repos in the two most-shared checklists:

| | |
|---|---|
| reference Jev somewhere in source | 20 / 20 |
| in product code, not only tests or scripts | 19 / 20 |
| have a test file touching Jev | 13 / 20 |
| median share of the codebase | 54.1% |
| over half the codebase | 12 / 20 |

The single exception is `lahfir/agent-desktop`: four files under `scripts/`, nothing in
what it ships.

**This is not a refutation of that post, and is not offered as one.** Its population is
use-cases shared on X, most of which are screenshots, and a screenshot cannot be cloned.
This population is the twenty repos in the two biggest lists — a subset, chosen because
it is the part of the claim that can be checked at all.

It also separates two readings that the word "larping" merges. *The code does not really
call Jev* is measurable, and it is 1 in 20. *The use case is a toy* is a different
statement, is not tested here, and is reasonable to hold: four of the twenty are games
or demos.
