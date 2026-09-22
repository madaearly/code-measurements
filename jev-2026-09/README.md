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
