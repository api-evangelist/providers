#!/usr/bin/env python3
"""
Build the API Evangelist Providers listing.

Sources:
  - ../../all/*                                      : one git repo per company
  - ../../api-search/providers/_providers/<slug>.md  : enriched provider data
                                                       (score.band, tags, etc.)

Output:
  - _data/providers.json               : alphabetical { letter: [...] }
  - _data/providers-fortune1000.json   : flat list of Fortune 1000 providers
  - _data/providers-federal.json       : flat list of Federal Government providers
  - _data/providers-universities.json  : flat list of universities
  - _data/providers-{band}.json        : flat list per apis.io rating band
  - index.html                         : home with category cards (includes home.html)
  - alphabetical/index.html + alphabetical/<letter>/index.html
  - fortune-1000/index.html
  - federal-government/index.html
  - universities/index.html
  - {exemplar,strong,developing,thin,minimal}/index.html
"""
import json
import os
import re
import string

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))
ALL = os.path.join(ROOT, "all")
PROVIDERS = os.path.join(ROOT, "api-search", "providers", "_providers")
SCORING_YML = os.path.join(ROOT, "api-search", "signals", "_data", "scoring.yml")
DELISTED_YML = os.path.join(ROOT, "api-search", "network", "_data", "delisted.yml")

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")
DESC_RE = re.compile(r"^description:\s*(.*?)\s*$")

# Jekyll 3.x reads _data/*.json with Psych (YAML), which has no \uD83E-style
# surrogate escape. A single one anywhere in these files aborts the whole site
# build with an unhelpful "Page build failed", so scrub them on the way out.
SURROGATE_RE = re.compile("[\ud800-\udfff]")


def desurrogate(obj):
    """Recursively fold surrogate pairs back into real characters."""
    if isinstance(obj, str):
        if not SURROGATE_RE.search(obj):
            return obj
        try:
            return obj.encode("utf-16", "surrogatepass").decode("utf-16")
        except (UnicodeDecodeError, UnicodeEncodeError):
            # Lone surrogate with no partner — not a representable character.
            return SURROGATE_RE.sub("", obj)
    if isinstance(obj, list):
        return [desurrogate(v) for v in obj]
    if isinstance(obj, dict):
        return {k: desurrogate(v) for k, v in obj.items()}
    return obj


def dump_json(obj, fh, **kwargs):
    """json.dump, with surrogates repaired first. Use for every _data/*.json."""
    json.dump(desurrogate(obj), fh, ensure_ascii=False, **kwargs)


FORTUNE_TAGS = {"Fortune 100", "Fortune 500", "Fortune 1000"}
FEDERAL_TAGS = {"Federal Government", "United States Government", "Federal"}
APACHE_TAGS = {"Apache"}
CNCF_TAGS = {"CNCF"}

# Universities = degree-granting institutions only. Deliberately keyed on the
# "University" tag alone and NOT on "Higher Education", which the enrichment
# pipeline also hangs on the ed-tech vendors that SELL to universities —
# Canvas LMS, Handshake, 2U, Barnes & Noble Education, Piazza, Top Hat. Those
# are suppliers to the sector, not institutions in it, and mixing them in
# would make the collection a market listing rather than an institution one.
UNIVERSITY_TAGS = {"University"}

# European Government = a provider carrying BOTH a government tag and a
# European location tag (country / region / European Union).
GOV_TAGS = {
    "Government", "Government Data", "Government Agency", "Government Services",
    "Open Government", "Digital Government", "Federal Government",
    "National Government", "Regional Government", "Provincial Government",
    "State Government", "Municipal Government", "County Government",
    "Territorial Government",
}
EUROPE_TAGS = {
    "Europe", "European", "European Union",
    "United Kingdom", "Ireland", "France", "Germany", "Spain", "Portugal",
    "Italy", "Netherlands", "Belgium", "Luxembourg", "Switzerland", "Austria",
    "Sweden", "Norway", "Denmark", "Finland", "Iceland", "Poland", "Czechia",
    "Czech Republic", "Slovakia", "Slovenia", "Hungary", "Romania", "Bulgaria",
    "Croatia", "Serbia", "Bosnia and Herzegovina", "Montenegro", "Kosovo",
    "Albania", "North Macedonia", "Greece", "Cyprus", "Malta", "Moldova",
    "Ukraine", "Estonia", "Latvia", "Lithuania", "Liechtenstein", "Monaco",
    "Andorra", "San Marino",
}

BANDS = ["exemplar", "strong", "developing", "thin", "minimal"]

# Matches Fortune classification in apis.yml source files:
# Fortune F1000 (rank N), Fortune 500, x-fortune:, fortune-rank:, Fortune Global N
# Excludes: Wheel-of-Fortune, Fortune-500-grade (hyphenated), FortuneReview
FORTUNE_YML_RE = re.compile(
    r'(?:x-fortune|fortune-rank|Fortune\s+(?:Global\s+)?\s*F?\d+)',
    re.IGNORECASE,
)

# Slugs that match the Fortune regex but are not Fortune companies:
#   apis-io               — its apis.yml describes the Fortune 1000 as data
#                           coverage ("what ~5,800 companies (Fortune 1000 +
#                           API providers) build, buy, and hire for"), prose the
#                           regex can't tell from a classification.
#   api-evangelist-network — the network's own index repo. It aggregates every
#                           other company's entries, so it carries real
#                           `x-fortune:` blocks — hundreds of them, belonging to
#                           the companies it indexes, not to itself.
NOT_FORTUNE = {"apis-io", "api-evangelist-network"}

BAND_META = {
    "exemplar":   ("Exemplar",   "Top-tier providers with comprehensive API programs, full governance, and excellent developer experience."),
    "strong":     ("Strong",     "Well-rounded API providers with solid governance, documentation, and developer tooling."),
    "developing": ("Developing", "API providers making good progress toward a complete and well-governed API program."),
    "thin":       ("Thin",       "API providers with basic presence but limited governance, tooling, or documentation."),
    "minimal":    ("Minimal",    "API providers with minimal API program signals detected on the network."),
}


# ---------------------------------------------------------------------------
# Source readers
# ---------------------------------------------------------------------------

def delisted_slugs():
    """Slugs a company has asked us to remove — never list these, ever.

    The registry at network/_data/delisted.yml is the network-wide source of
    truth for takedown requests. A delisted provider keeps a bare repo under
    all/<slug>/ (README only, so the GitHub URL does not dangle), which means
    the repo scan below would happily list it again. This guard is what stops
    that; it must not depend on which files a takedown happened to delete.
    """
    if not os.path.isfile(DELISTED_YML):
        print("WARNING: %s not found — delisting guard is INACTIVE" % DELISTED_YML)
        return set()
    with open(DELISTED_YML, "r", encoding="utf-8") as fh:
        doc = yaml.safe_load(fh) or []
    rows = doc if isinstance(doc, list) else doc.get("delisted", doc.get("providers", []))
    return {r["slug"] for r in rows if isinstance(r, dict) and r.get("slug")}


def company_slugs():
    """Every directory in all/* that is a real, listable company repo.

    Two things disqualify a repo. It is delisted (see delisted_slugs), or it
    carries no apis.yml — the canonical provider descriptor. The latter drops
    the workbench repo (0-working) and the scrape artifacts that got captured
    as companies off partner pages (logo-1..7, footer, spinner, log-in, ...).
    Keying on apis.yml is what build-providers.py and build-sections.py
    already do; this makes the listing agree with them.
    """
    skip = delisted_slugs()
    out, dropped_delisted, dropped_nodesc = [], [], []
    for entry in os.listdir(ALL):
        path = os.path.join(ALL, entry)
        if not os.path.isdir(path):
            continue
        if not os.path.isdir(os.path.join(path, ".git")):
            continue
        if entry in skip:
            dropped_delisted.append(entry)
            continue
        if not os.path.isfile(os.path.join(path, "apis.yml")):
            dropped_nodesc.append(entry)
            continue
        out.append(entry)
    if dropped_delisted:
        print("delisted, excluded: %d (%s)" % (len(dropped_delisted), ", ".join(sorted(dropped_delisted))))
    if dropped_nodesc:
        print("no apis.yml, excluded: %d" % len(dropped_nodesc))
    return sorted(out, key=str.lower)


def titleize(slug):
    parts = slug.replace("_", "-").split("-")
    return " ".join(p[:1].upper() + p[1:] if p else p for p in parts)


RAW_BASE = "https://raw.githubusercontent.com/api-evangelist/%s/refs/heads/main/screenshots/%s"


def newest_screenshot(slug):
    """Return the raw.githubusercontent URL of the newest screenshot for a
    company, or None. Prefers screenshots/index.json; falls back to the
    newest *.png by filename (timestamps sort lexically)."""
    shots = os.path.join(ALL, slug, "screenshots")
    if not os.path.isdir(shots):
        return None
    fname = None
    idx = os.path.join(shots, "index.json")
    if os.path.isfile(idx):
        try:
            with open(idx, "r", encoding="utf-8", errors="ignore") as fh:
                entries = json.load(fh)
            files = [e.get("file") for e in entries if e.get("file")]
            if files:
                fname = sorted(files)[-1]
        except (OSError, ValueError):
            fname = None
    if not fname:
        pngs = [f for f in os.listdir(shots) if f.lower().endswith(".png")]
        if pngs:
            fname = sorted(pngs)[-1]
    if not fname:
        return None
    return RAW_BASE % (slug, fname)


def display_name_and_description(slug):
    """Return (name, description) from the top-level fields of apis.yml."""
    name = titleize(slug)
    description = ""
    apis_yml = os.path.join(ALL, slug, "apis.yml")
    if not os.path.isfile(apis_yml):
        return name, description
    try:
        with open(apis_yml, "r", encoding="utf-8", errors="ignore") as fh:
            in_desc = False
            desc_lines = []
            for line in fh:
                if line and line[0] not in " \t#":
                    if in_desc:
                        break
                    m = NAME_RE.match(line)
                    if m:
                        val = m.group(1).strip().strip("'\"").strip()
                        if val and val.lower() not in ("null", "~"):
                            name = val
                    m2 = DESC_RE.match(line)
                    if m2:
                        inline = m2.group(1).strip()
                        if inline and inline not in (">-", "|", ">"):
                            description = inline
                        else:
                            in_desc = True
                elif in_desc and line.strip():
                    desc_lines.append(line.strip())
            if desc_lines:
                description = " ".join(desc_lines)
    except OSError:
        pass
    return name, description


def fortune_slugs():
    """Slugs in all/* whose apis.yml carries a Fortune classification."""
    out = set()
    for slug in os.listdir(ALL):
        if slug in NOT_FORTUNE:
            continue
        yml = os.path.join(ALL, slug, "apis.yml")
        if not os.path.isfile(yml):
            continue
        try:
            content = open(yml, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        if FORTUNE_YML_RE.search(content):
            out.add(slug)
    return out


def read_provider_metadata():
    """Read band and tags from each provider markdown file.
    Returns {slug: {band, tags}}."""
    meta = {}
    if not os.path.isdir(PROVIDERS):
        return meta
    for fname in os.listdir(PROVIDERS):
        if not fname.endswith(".md"):
            continue
        slug = fname[:-3]
        band = None
        tags = []
        try:
            with open(os.path.join(PROVIDERS, fname), "r", encoding="utf-8", errors="ignore") as fh:
                fm_content = fh.read()
        except OSError:
            continue
        bm = re.search(r"^\s{2}band:\s*(\w+)", fm_content, re.MULTILINE)
        if bm:
            band = bm.group(1)
        tm = re.search(r"^tags:\n((?:- .+\n)+)", fm_content, re.MULTILINE)
        if tm:
            tags = re.findall(r"- (.+)", tm.group(1))
        meta[slug] = {"band": band, "tags": tags}
    return meta


def group_for(name):
    c = name.strip()[0:1].lower()
    if c in string.ascii_lowercase:
        return c
    return "0-9"


# ---------------------------------------------------------------------------
# Kin Score band grouping — mirrors build-sections.py so every listing renders
# the same band-grouped layout via _includes/company-listing-rated.html.
# ---------------------------------------------------------------------------

BAND_LABELS = {
    "exemplar": "Exemplar", "strong": "Strong", "developing": "Developing",
    "thin": "Thin", "emerging": "Emerging", "minimal": "Minimal",
}

_DETAILS_CACHE = {}


def _fm_block(content, key):
    """Return the parsed value of a top-level frontmatter block (score /
    agent_readiness) plus its indented lines — same shape score.rb writes."""
    m = re.search(r"^%s:\n((?:[ \t]+.*\n|\n)*)" % key, content, re.MULTILINE)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(0)).get(key)
    except yaml.YAMLError:
        return None


def read_score_details(slug):
    """Full score + agent_readiness blocks for one provider, or None. Cached."""
    if slug in _DETAILS_CACHE:
        return _DETAILS_CACHE[slug]
    path = os.path.join(PROVIDERS, slug + ".md")
    details = None
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
            details = {
                "score": _fm_block(content, "score"),
                "agent": _fm_block(content, "agent_readiness"),
            }
        except OSError:
            details = None
    _DETAILS_CACHE[slug] = details
    return details


def make_rated(entry):
    """Augment a flat listing entry with its Kin Score composite/band/facets and
    agent-readiness, matching build-sections.py's rated_entry."""
    e = dict(entry)
    details = read_score_details(e["slug"])
    if details:
        sc = details.get("score") or {}
        if sc.get("composite") is not None:
            e["score"] = sc["composite"]
        band = sc.get("band")
        if band:
            e["band"] = band
            e["band_label"] = BAND_LABELS.get(band, band.title())
        if sc.get("facets"):
            e["facets"] = sc["facets"]
        if sc.get("scored_at"):
            e["scored_at"] = str(sc["scored_at"])
        if sc.get("schema_version") is not None:
            e["schema_version"] = sc["schema_version"]
        if sc.get("regulatory"):
            e["regulatory"] = sc["regulatory"]
        ag = details.get("agent") or {}
        if ag.get("score") is not None:
            e["agent_score"] = ag["score"]
            e["agent_band"] = ag.get("band", "")
            e["agent_dims"] = ag.get("dimensions", {})
    return e


def band_grouped(entries):
    """Turn a flat list of rated entries into the {total, bands} shape the
    rated listing include consumes. Sorts by composite descending, ranks, and
    groups by Kin Score band (unscored providers land in 'Not Yet Rated')."""
    entries = [make_rated(e) for e in entries]
    entries.sort(key=lambda e: (-e.get("score", -1), e["name"].lower()))
    for rank, e in enumerate(entries, 1):
        e["rank"] = rank
    band_ladder = [
        ("exemplar",   "Exemplar",   "70+",     "Reference-quality API operations across every facet."),
        ("strong",     "Strong",     "60–69.9", "Solid contracts, transparent operations, and an easy start."),
        ("developing", "Developing", "45–59.9", "Real signal across most facets with visible, nameable gaps."),
        ("thin",       "Thin",       "30–44.9", "Limited machine-readable signal beyond documentation a human can read."),
        ("emerging",   "Emerging",   "15–29.9", "More than an index entry but still mostly links rather than artifacts."),
        ("minimal",    "Minimal",    "0–14.9",  "Index entry only; little beyond a description and a link."),
        ("unrated",    "Not Yet Rated", "",     "Providers we have not scored yet — unknown, not zero."),
    ]
    groups = []
    for band, label, band_range, blurb in band_ladder:
        members = [e for e in entries if e.get("band", "unrated") == band or (band == "unrated" and "band" not in e)]
        if not members:
            continue
        groups.append({
            "band": band, "label": label, "range": band_range, "blurb": blurb,
            "count": len(members), "providers": members,
        })
    for g in groups[:2]:
        g["open"] = True
    return {"total": len(entries), "bands": groups}


def mirror_scoring(data_dir):
    """Mirror the rating rubric so the listing's rating panels can render the
    exact same facet/dimension layout as apis.io provider detail pages."""
    if not os.path.isfile(SCORING_YML):
        return
    with open(SCORING_YML, "r", encoding="utf-8") as fh:
        rubric_raw = fh.read()
    with open(os.path.join(data_dir, "scoring.yml"), "w", encoding="utf-8") as fh:
        fh.write("# Mirrored from api-search/signals/_data/scoring.yml by build-listing.py — do not edit here.\n")
        fh.write(rubric_raw)


# ---------------------------------------------------------------------------
# Main data build
# ---------------------------------------------------------------------------

def main():
    slugs = company_slugs()
    provider_meta = read_provider_metadata()
    provider_slug_set = set(provider_meta.keys())
    fortune_slug_set = fortune_slugs()

    groups = {}               # alphabetical
    fortune1000 = []
    federal = []
    european = []
    apache = []
    cncf = []
    universities = []
    band_lists = {b: [] for b in BANDS}
    counts = {"provider": 0, "repo": 0}

    for slug in slugs:
        name, description = display_name_and_description(slug)
        is_provider = slug in provider_slug_set

        if is_provider:
            url = "https://providers.apis.io/providers/%s/" % slug
            typ = "API Provider"
            counts["provider"] += 1
        else:
            url = "https://github.com/api-evangelist/%s" % slug
            typ = "Repository"
            counts["repo"] += 1

        entry = {"name": name, "slug": slug, "url": url, "type": typ}
        if description:
            entry["description"] = description
        shot = newest_screenshot(slug)
        if shot:
            entry["screenshot"] = shot

        # Alphabetical
        groups.setdefault(group_for(name), []).append(entry)

        # Fortune 1000: any company classified in all/* apis.yml, not just providers
        if slug in fortune_slug_set:
            fortune1000.append(entry)

        # Other category listings (providers only — require apis.io profile)
        if is_provider:
            meta = provider_meta[slug]
            tag_set = set(meta.get("tags", []))
            band = meta.get("band")
            if tag_set & FEDERAL_TAGS:
                federal.append(entry)
            if (tag_set & GOV_TAGS) and (tag_set & EUROPE_TAGS):
                european.append(entry)
            if tag_set & APACHE_TAGS:
                apache.append(entry)
            if tag_set & CNCF_TAGS:
                cncf.append(entry)
            if tag_set & UNIVERSITY_TAGS:
                universities.append(entry)
            if band in band_lists:
                band_lists[band].append(entry)

    # Sort
    for g in groups:
        groups[g].sort(key=lambda x: x["name"].lower())
    fortune1000.sort(key=lambda x: x["name"].lower())
    federal.sort(key=lambda x: x["name"].lower())
    european.sort(key=lambda x: x["name"].lower())
    apache.sort(key=lambda x: x["name"].lower())
    cncf.sort(key=lambda x: x["name"].lower())
    universities.sort(key=lambda x: x["name"].lower())
    for b in BANDS:
        band_lists[b].sort(key=lambda x: x["name"].lower())

    # Write data files
    data_dir = os.path.join(SITE, "_data")
    os.makedirs(data_dir, exist_ok=True)

    # Alphabetical stays a flat { letter: [...] } map for the A–Z browse pages.
    with open(os.path.join(data_dir, "providers.json"), "w", encoding="utf-8") as fh:
        dump_json(groups, fh, indent=1, sort_keys=True)

    # Every other section is grouped by Kin Score band, matching Market Data
    # and the banking pages (rendered by company-listing-rated.html).
    mirror_scoring(data_dir)
    with open(os.path.join(data_dir, "providers-fortune1000.json"), "w", encoding="utf-8") as fh:
        dump_json(band_grouped(fortune1000), fh, indent=1)
    with open(os.path.join(data_dir, "providers-federal.json"), "w", encoding="utf-8") as fh:
        dump_json(band_grouped(federal), fh, indent=1)
    with open(os.path.join(data_dir, "providers-european.json"), "w", encoding="utf-8") as fh:
        dump_json(band_grouped(european), fh, indent=1)
    with open(os.path.join(data_dir, "providers-apache.json"), "w", encoding="utf-8") as fh:
        dump_json(band_grouped(apache), fh, indent=1)
    with open(os.path.join(data_dir, "providers-cncf.json"), "w", encoding="utf-8") as fh:
        dump_json(band_grouped(cncf), fh, indent=1)
    with open(os.path.join(data_dir, "providers-universities.json"), "w", encoding="utf-8") as fh:
        dump_json(band_grouped(universities), fh, indent=1)
    for b in BANDS:
        with open(os.path.join(data_dir, "providers-%s.json" % b), "w", encoding="utf-8") as fh:
            dump_json(band_grouped(band_lists[b]), fh, indent=1)

    total = sum(len(v) for v in groups.values())
    print("alphabetical: %d (providers=%d, repos=%d)" % (total, counts["provider"], counts["repo"]))
    print("fortune1000:  %d" % len(fortune1000))
    print("federal:      %d" % len(federal))
    print("european:     %d" % len(european))
    print("apache:       %d" % len(apache))
    print("cncf:         %d" % len(cncf))
    print("universities: %d" % len(universities))
    for b in BANDS:
        print("band/%-12s %d" % (b + ":", len(band_lists[b])))

    return groups, fortune1000, federal, european, apache, cncf, universities, band_lists


# ---------------------------------------------------------------------------
# Page generation
# ---------------------------------------------------------------------------

def write_pages(groups, fortune1000, federal, european, apache, cncf, universities, band_lists):
    letters = list(string.ascii_uppercase)

    # --- Home page ---
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as fh:
        fh.write("\n".join([
            "---",
            "layout: default",
            "section: Providers",
            'title: "API Providers"',
            'summary: "Browse API providers across the APIs.io network by category."',
            "nav: Providers",
            "---",
            "{% include home.html %}",
            "",
        ]))

    # --- Alphabetical pages (under /alphabetical/) ---
    def alpha_page(letter_display, group_key, summary):
        return "\n".join([
            "---",
            "layout: default",
            "section: Providers",
            'title: "Providers - %s"' % letter_display,
            'summary: "%s"' % summary,
            "nav: Providers",
            'letter: "%s"' % letter_display,
            "---",
            "{% include company-listing.html %}",
            "",
        ])

    alpha_dir = os.path.join(SITE, "alphabetical")
    os.makedirs(alpha_dir, exist_ok=True)
    with open(os.path.join(alpha_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(alpha_page("A", "a",
            "Alphabetical listing of every provider tracked across the API Evangelist network, starting with A."))
    for L in letters:
        key = L.lower()
        d = os.path.join(alpha_dir, key)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(alpha_page(L, key, "Providers starting with %s." % L))
    d = os.path.join(alpha_dir, "0-9")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(alpha_page("0-9", "0-9", "Providers starting with a number."))

    # --- Flat listing pages ---
    def flat_page(title, data_key, summary, description):
        return "\n".join([
            "---",
            "layout: default",
            "section: Providers",
            'title: "%s"' % title,
            'summary: "%s"' % summary,
            "nav: Providers",
            'data_key: "%s"' % data_key,
            'description: "%s"' % description,
            "---",
            "{% include company-listing-rated.html %}",
            "",
        ])

    d = os.path.join(SITE, "fortune-1000")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "Fortune 1000",
            "providers-fortune1000",
            "Fortune 100, 500, and 1000 companies with APIs on the network.",
            "Fortune 100, Fortune 500, and Fortune 1000 companies with APIs on the network.",
        ))

    d = os.path.join(SITE, "federal-government")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "U.S. Federal Government",
            "providers-federal",
            "U.S. Federal Government agencies with APIs.",
            "United States Federal Government agencies and departments publishing APIs on the network.",
        ))

    d = os.path.join(SITE, "european-government")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "European Government",
            "providers-european",
            "European national, regional, and EU government agencies with APIs.",
            "European national, regional, and European Union government agencies and departments publishing APIs on the network.",
        ))

    d = os.path.join(SITE, "apache")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "Apache",
            "providers-apache",
            "Apache Software Foundation projects with APIs.",
            "Apache Software Foundation projects publishing APIs on the network.",
        ))

    d = os.path.join(SITE, "cncf")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "CNCF",
            "providers-cncf",
            "Cloud Native Computing Foundation projects with APIs.",
            "Cloud Native Computing Foundation (CNCF) projects publishing APIs on the network.",
        ))

    d = os.path.join(SITE, "universities")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "Universities",
            "providers-universities",
            "Universities and research institutions with APIs, ranked by their Kin Score.",
            "Universities and research institutions publishing APIs on the network — course and campus data, library and repository catalogs, open research data, identity, and the OAI-PMH and IIIF endpoints behind their scholarly collections.",
        ))

    for b in BANDS:
        label, desc = BAND_META[b]
        d = os.path.join(SITE, b)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(flat_page(
                "Kin Score: %s" % label,
                "providers-%s" % b,
                "%s — %s" % (label, desc),
                desc,
            ))

    # Remove legacy root <letter>.html files
    for L in letters:
        legacy = os.path.join(SITE, "%s.html" % L.lower())
        if os.path.isfile(legacy):
            os.remove(legacy)

    print("pages written.")


if __name__ == "__main__":
    g, f1000, fed, eur, apa, cn, uni, bands = main()
    write_pages(g, f1000, fed, eur, apa, cn, uni, bands)
