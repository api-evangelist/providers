"""Kin Score bands, read from the rubric instead of retyped.

THE SINGLE SOURCE OF TRUTH IS `api-search/signals/_data/scoring.yml` — the same file
`score.rb` scores against. Everything about a band except this site's own prose comes
from there: which bands exist, their order, their labels, and their score ranges.

Why this module exists. The band list and the thresholds beside it were hand-copied into
several places, and every copy drifted:

  * `build-sections.py` printed the pre-calibration ladder (70+, 60–69.9, 45–59.9,
    30–44.9, 15–29.9) long after the rubric was recalibrated to 66+/56–65.9/42–55.9/
    28–41.9/13–27.9. Grouping was right; the label under it was wrong on every section
    page. That was fixed locally in that one file.
  * `build-listing.py` kept its own copy of the same stale ladder AND a five-entry
    `BANDS` list that predated `emerging` (added in rubric v0.4). Because `BANDS` was
    used as a filter, all 6,142 emerging providers were dropped from the per-band
    export and appeared in no band listing at all — invisible for weeks, because the
    *other* ladder in the same file already knew about the band.

One file, one reader. Adding or recalibrating a band is now an edit to scoring.yml.

The prose stays here on purpose: it is written for this site, and the rubric's own
`description:` is written for the rubric.
"""

import os

import yaml

# scripts/ -> providers/ -> api-evangelist/ -> GitHub/, which holds api-search/ alongside.
# Matches build-listing.py and build-sections.py's own ROOT.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

# Prefer the canonical rubric; fall back to the mirror build.py writes for apis.io.
# _mirror_rubric() keeps them identical, so either answers correctly — but if the
# canonical one is missing we would rather read the mirror than invent thresholds.
SCORING_CANDIDATES = [
    os.path.join(ROOT, "api-search", "signals", "_data", "scoring.yml"),
    os.path.join(ROOT, "api-search", "network", "_data", "scoring.yml"),
]

# Short line under each band header on a rated listing.
BAND_BLURBS = {
    "exemplar":   "Reference-quality API operations across every facet.",
    "strong":     "Solid contracts, transparent operations, and an easy start.",
    "developing": "Real signal across most facets with visible, nameable gaps.",
    "thin":       "Limited machine-readable signal beyond documentation a human can read.",
    "emerging":   "More than an index entry but still mostly links rather than artifacts.",
    "minimal":    "Index entry only; little beyond a description and a link.",
}

# Longer description for each band's own /<band>/ page.
BAND_PAGE_DESC = {
    "exemplar":   "Top-tier providers with comprehensive API programs, full governance, and excellent developer experience.",
    "strong":     "Well-rounded API providers with solid governance, documentation, and developer tooling.",
    "developing": "API providers making good progress toward a complete and well-governed API program.",
    "thin":       "API providers with basic presence but limited governance, tooling, or documentation.",
    "emerging":   "API providers with more than an index entry, but still mostly links rather than machine-readable artifacts.",
    "minimal":    "API providers with minimal API program signals detected on the network.",
}

UNRATED = ("unrated", "Not Yet Rated", "",
           "Providers we have not scored yet — unknown, not zero.")

_CACHE = []


def _load():
    """[(id, label, range), …] in rubric order. Empty list if unreadable."""
    for path in SCORING_CANDIDATES:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                bands = (yaml.safe_load(fh) or {}).get("bands") or []
        except (OSError, yaml.YAMLError):
            continue
        out = []
        for b in bands:
            if not isinstance(b, dict):
                continue
            bid = str(b.get("id") or "")
            if bid:
                out.append((bid, b.get("label") or bid.title(), str(b.get("range") or "")))
        if out:
            return out
    return []


def _bands():
    if not _CACHE:
        _CACHE.extend(_load())
    return _CACHE


def band_ids():
    """Scored band ids, best first. Never includes 'unrated'.

    Falls back to the prose dict's own keys so a reshaped scoring.yml degrades to
    "we know these bands exist" rather than to an empty list — an empty list here
    would silently drop every provider from the per-band export.
    """
    ids = [b[0] for b in _bands() if b[0] in BAND_PAGE_DESC]
    return ids or list(BAND_PAGE_DESC.keys())


def band_meta():
    """{id: (label, page description)} for the per-band listing pages."""
    labels = {b[0]: b[1] for b in _bands()}
    return {bid: (labels.get(bid, bid.title()), BAND_PAGE_DESC[bid]) for bid in band_ids()}


def band_ladder():
    """[(id, label, range, blurb), …] best first, with 'Not Yet Rated' last.

    On an unreadable or reshaped rubric the range is emitted EMPTY rather than
    guessed: grouping without a threshold is honest, printing a threshold that may
    be wrong is not.
    """
    known = {b[0]: b for b in _bands()}
    ladder = []
    for bid in band_ids():
        _, label, rng = known.get(bid, (bid, bid.title(), ""))
        ladder.append((bid, label, rng, BAND_BLURBS.get(bid, "")))
    ladder.append(UNRATED)
    return ladder
