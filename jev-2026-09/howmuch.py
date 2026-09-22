#!/usr/bin/env python3
"""How much of a repository is actually about X?

    python3 howmuch.py owner/repo keyword [keyword ...]

Shallow-clones the repo, reads every source file, and reports what share of the
code mentions the keyword at all -- split by where those files sit in the tree,
because a keyword that appears only under tests/ or bench/ is not something the
repo ships.

Counts files that MENTION the term. That is deliberately generous: it is an
upper bound on how much of the repo is about X, never an under-count.
"""
import os, re, subprocess, sys, tempfile

SRC = {".py",".ts",".tsx",".js",".jsx",".rs",".go",".java",".rb",".mjs",".cjs",
       ".svelte",".vue",".kt",".swift",".c",".cc",".cpp",".h",".hpp",".cs",".php"}
SKIP = {".git","node_modules","target","dist","build",".venv","venv","vendor",
        ".next",".nuxt","__pycache__"}

def role(path):
    p = path.lower(); base = os.path.basename(p)
    if re.search(r"(^|/)bench(mark)?s?/", p):                       return "bench"
    if (re.search(r"(^|/)(tests?|spec|__tests__)/", p)
        or re.search(r"\.(test|spec)\.", base)
        or base.startswith("test_")):                               return "test"
    if re.search(r"(^|/)(scripts?|tools?|examples?|demos?|docs?)/", p): return "script"
    return "product"

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    repo, terms = sys.argv[1], [t.lower() for t in sys.argv[2:]]
    rx = re.compile("|".join(re.escape(t) for t in terms), re.I)

    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run(["git","clone","--depth","1","--quiet",
                            f"https://github.com/{repo}.git", tmp+"/r"],
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"clone failed: {r.stderr.strip()[:200]}")

        files = loc = mfiles = mloc = 0
        by_role = {"product":0, "test":0, "bench":0, "script":0}
        hits = []
        for root, dirs, fs in os.walk(tmp+"/r"):
            dirs[:] = [d for d in dirs if d not in SKIP]
            for f in fs:
                if os.path.splitext(f)[1] not in SRC:
                    continue
                full = os.path.join(root, f)
                rel  = full[len(tmp)+3:]
                try:
                    text = open(full, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                n = text.count("\n") + 1
                files += 1; loc += n
                k = len(rx.findall(text))
                if k:
                    mfiles += 1; mloc += n
                    by_role[role(rel)] += 1
                    hits.append((rel, role(rel), k))

    if not files:
        sys.exit("no source files found")
    print(f"\n{repo}   terms: {', '.join(terms)}")
    print(f"  source files   {files:>7}      mentioning   {mfiles:>7}   "
          f"{100*mfiles/files:5.1f}%")
    print(f"  lines of code  {loc:>7}      in those     {mloc:>7}   "
          f"{100*mloc/loc:5.1f}%")
    print(f"  where          product {by_role['product']}   test {by_role['test']}   "
          f"bench {by_role['bench']}   script/docs {by_role['script']}")
    if by_role["product"] == 0 and mfiles:
        print("  NOTE: never appears in product code -- only tests, benchmarks or scripts.")
    for rel, rl, k in sorted(hits, key=lambda h: -h[2])[:12]:
        print(f"      [{rl:7}] {rel}  ({k})")

if __name__ == "__main__":
    main()
