#!/usr/bin/env python3
"""Emit the two interactive market tools for every ranked listing page.

A market has a buy side and a sell side and both arrive on the same page.
Each ranked listing with a banded cohort gets:

    /<section>/priorities.html     for buyers   — weight what you are optimizing
                                                  for, the shortlist re-sorts
    /<section>/opportunities.html  for providers — every check in the rubric, who
                                                  in this market already passes it,
                                                  and what shipping it is worth

Both pages are seven-line stubs. The entire body lives in _includes/tool-*.html
and renders from site.data — the SAME data the ranked listing underneath renders
from — so a rescore moves the listing and the tools together and they can never
disagree. The first version of the buyer tool pasted CSVs out of a report bundle
and froze on the day it shipped; that is the mistake this shape exists to prevent.

THIS RUNS AS A POST-PASS, not inline in listing_page(), because the tool notes are
computed from the data file that the listing writes moments earlier and from the
rubric, and because the `tools:` block has to land in pages built by five different
call sites. Anything a section page needs must be GENERATED or it does not survive
the next rebuild — the first hand-added tools block was silently deleted exactly
that way.

Idempotent: re-running rewrites the same bytes.
"""

import io
import json
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
DATA = os.path.join(SITE, "_data")

# A cohort this small cannot carry the tools honestly: "who else in this market
# holds it" is not a market statement across a handful of providers, and a buyer
# weighting facets over six rows is just re-reading the listing. Both tools are
# skipped below this and the page keeps its promo band alone.
MIN_COHORT = 8


def load_rubric():
    with open(os.path.join(DATA, "scoring.yml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def credit(dim, hit, prov_credit):
    """Resolve earned credit for one dimension — the rubric's own table.

    Mirrors the JS in _includes/tool-opportunities.html exactly. The graded
    dimensions carry STRINGS ('derived', 'documented', 'partial') and every
    non-empty string is truthy, which is the bug that once paid full points for
    partial credit. Nothing here tests truthiness.
    """
    if hit is True:
        return 1.0
    if hit is False or hit is None or hit == "":
        return 0.0
    table = (dim or {}).get("credit") or {}
    if hit in table:
        return float(table[hit])
    if hit in prov_credit:
        return float(prov_credit[hit])
    return 1.0


def frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        return yaml.safe_load(parts[1]) or {}, text
    except yaml.YAMLError:
        return None, text


def cohort_stats(data_key, rubric):
    """(n, total, unclaimed_points, n_checks) for a listing, or None if unusable."""
    path = os.path.join(DATA, "%s.json" % data_key)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if "bands" not in data:
        return None

    providers = [
        p
        for band in data["bands"]
        for p in band.get("providers") or []
        if p.get("score") is not None and p.get("agent_dims")
    ]
    n = len(providers)
    if n < MIN_COHORT:
        return None

    dims = rubric["agent_readiness"]["dimensions"]
    prov_credit = (rubric.get("provenance") or {}).get("credit") or {}

    # Points in this model that NOBODY in the cohort holds at any credit at all.
    # This is the headline of the provider tool, so it is computed here rather
    # than asserted, and it is what the card note quotes.
    unclaimed = 0
    for d in dims:
        if not any(credit(d, (p["agent_dims"] or {}).get(d["id"]), prov_credit) > 0
                   for p in providers):
            unclaimed += d["points"]

    return n, data.get("total") or n, unclaimed, len(dims)


def tools_for(section_url, data_key, stats):
    n, total, unclaimed, checks = stats
    truncated = total > n

    scope = ("the top %s of %s ranked" % (f"{n:,}", f"{total:,}")) if truncated \
        else ("%s providers" % f"{n:,}")
    whom = "the top %s" % f"{n:,}" if truncated else "the %s" % f"{n:,}"

    return [
        {
            "side": "For buyers",
            "label": "Pick your priorities",
            "icon": "tune",
            "blurb": "Weight what your team is actually optimizing for and the "
                     "shortlist of %s re-sorts underneath you." % f"{n:,}",
            "note": "%s · one public rubric" % scope,
            "url": section_url + "priorities.html",
        },
        {
            "side": "For providers",
            "label": "Find your opening",
            "icon": "target",
            "blurb": "See every check in the rubric, who in this market already "
                     "passes it, and what shipping it is worth to your score.",
            # The second half of this note is the sales pitch and it has to be
            # true: quote the unclaimed total only when there IS one.
            "note": ("%d checks · %d points nobody holds" % (checks, unclaimed))
                    if unclaimed else
                    ("%d checks · %s scored against them" % (checks, whom)),
            "url": section_url + "opportunities.html",
        },
    ]


def esc(text):
    return str(text).replace('"', "'")


def tools_block(tools):
    lines = ["tools:"]
    for t in tools:
        lines.append('  - side: "%s"' % esc(t["side"]))
        lines.append('    label: "%s"' % esc(t["label"]))
        for key in ("icon", "blurb", "note", "url"):
            if t.get(key):
                lines.append('    %s: "%s"' % (key, esc(t[key])))
    return "\n".join(lines)


def splice_tools(text, tools):
    """Replace or append the `tools:` block in a page's front matter."""
    head, fm, body = text.split("---", 2)
    # Drop any existing block: `tools:` through the last of its indented lines.
    fm = re.sub(r"(?m)^tools:\n(?:[ \t]+.*\n)*", "", fm)
    fm = fm.rstrip("\n") + "\n" + tools_block(tools) + "\n"
    return "---".join([head, fm, body])


STUB = """---
layout: null
# GENERATED by scripts/build-section-tools.py — do not hand-edit, it is overwritten.
#
# The body is _includes/tool-%(kind)s.html, shared by every ranked market, and it
# renders from site.data[data_key] — the same file the ranked listing on
# %(section_url)s renders from. The site-wide `permalink` pattern would
# otherwise rewrite this to a pretty directory, so it is pinned to keep the two
# tools as siblings.
permalink: %(permalink)s
data_key: %(data_key)s
cohort: "%(cohort)s"
section_url: %(section_url)s
---
{%% include tool-%(kind)s.html %%}
"""


def write(path, content):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            if fh.read() == content:
                return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return True


def main():
    rubric = load_rubric()
    built = skipped = 0
    notes = []

    for root, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if not d.startswith(("_site", ".", "node_modules"))]
        if "index.html" not in files:
            continue
        path = os.path.join(root, "index.html")
        fm, text = frontmatter(path)
        if not fm:
            continue

        # Opt-in, not inferred. The gate used to be "this market sells a Trend
        # Report"; that line was retired on 2026-08-21, so a listing states it
        # carries the tools. Flip `market_tools: true` on to wire a new one.
        data_key = fm.get("data_key")
        if not data_key or not fm.get("market_tools"):
            continue

        stats = cohort_stats(data_key, rubric)
        if not stats:
            # Either not a banded listing (the VC portfolio page) or too small a
            # cohort to say anything about a market. Named, not silent.
            skipped += 1
            notes.append("  skip  %-46s %s" % (
                os.path.relpath(root, SITE), "no banded cohort or under %d providers" % MIN_COHORT))
            continue

        section_url = "/" + os.path.relpath(root, SITE).replace(os.sep, "/") + "/"
        if section_url == "/./":
            section_url = "/"

        tools = tools_for(section_url, data_key, stats)
        if write(path, splice_tools(text, tools)):
            built += 1

        for kind, tool in (("priorities", tools[0]), ("opportunities", tools[1])):
            name = "%s.html" % kind
            write(os.path.join(root, name), STUB % {
                "kind": kind,
                "permalink": section_url + name,
                "data_key": data_key,
                "cohort": esc(fm.get("title") or ""),
                "section_url": section_url,
                "section": section_url,
            })

    print("Section tools: %d listings wired, %d skipped" % (built, skipped))
    for line in notes:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
