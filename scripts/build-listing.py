#!/usr/bin/env python3
"""
Build the API Evangelist Providers listing.

Sources:
  - ../../all/*                                      : one git repo per company
  - ../../api-search/providers/_providers/<slug>.md  : enriched provider data
                                                       (score.band, tags, etc.)

Output:
  - _data/companies.json               : alphabetical { letter: [...] }
  - _data/companies-fortune1000.json   : flat list of Fortune 1000 providers
  - _data/companies-federal.json       : flat list of Federal Government providers
  - _data/companies-{band}.json        : flat list per apis.io rating band
  - index.html                         : home with category cards (includes home.html)
  - alphabetical/index.html + alphabetical/<letter>/index.html
  - fortune-1000/index.html
  - federal-government/index.html
  - {exemplar,strong,developing,thin,minimal}/index.html
"""
import json
import os
import re
import string

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))
ALL = os.path.join(ROOT, "all")
PROVIDERS = os.path.join(ROOT, "api-search", "providers", "_providers")

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")
DESC_RE = re.compile(r"^description:\s*(.*?)\s*$")

FORTUNE_TAGS = {"Fortune 100", "Fortune 500", "Fortune 1000"}
FEDERAL_TAGS = {"Federal Government", "United States Government", "Federal"}
BANDS = ["exemplar", "strong", "developing", "thin", "minimal"]

# Matches Fortune classification in apis.yml source files:
# Fortune F1000 (rank N), Fortune 500, x-fortune:, fortune-rank:, Fortune Global N
# Excludes: Wheel-of-Fortune, Fortune-500-grade (hyphenated), FortuneReview
FORTUNE_YML_RE = re.compile(
    r'(?:x-fortune|fortune-rank|Fortune\s+(?:Global\s+)?\s*F?\d+)',
    re.IGNORECASE,
)

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

def company_slugs():
    """Every directory in all/* that is a real git repo."""
    out = []
    for entry in os.listdir(ALL):
        path = os.path.join(ALL, entry)
        if not os.path.isdir(path):
            continue
        if not os.path.isdir(os.path.join(path, ".git")):
            continue
        out.append(entry)
    return sorted(out, key=str.lower)


def titleize(slug):
    parts = slug.replace("_", "-").split("-")
    return " ".join(p[:1].upper() + p[1:] if p else p for p in parts)


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
            if band in band_lists:
                band_lists[band].append(entry)

    # Sort
    for g in groups:
        groups[g].sort(key=lambda x: x["name"].lower())
    fortune1000.sort(key=lambda x: x["name"].lower())
    federal.sort(key=lambda x: x["name"].lower())
    for b in BANDS:
        band_lists[b].sort(key=lambda x: x["name"].lower())

    # Write data files
    data_dir = os.path.join(SITE, "_data")
    os.makedirs(data_dir, exist_ok=True)

    with open(os.path.join(data_dir, "companies.json"), "w", encoding="utf-8") as fh:
        json.dump(groups, fh, ensure_ascii=False, indent=1, sort_keys=True)
    with open(os.path.join(data_dir, "companies-fortune1000.json"), "w", encoding="utf-8") as fh:
        json.dump(fortune1000, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(data_dir, "companies-federal.json"), "w", encoding="utf-8") as fh:
        json.dump(federal, fh, ensure_ascii=False, indent=1)
    for b in BANDS:
        with open(os.path.join(data_dir, "companies-%s.json" % b), "w", encoding="utf-8") as fh:
            json.dump(band_lists[b], fh, ensure_ascii=False, indent=1)

    total = sum(len(v) for v in groups.values())
    print("alphabetical: %d (providers=%d, repos=%d)" % (total, counts["provider"], counts["repo"]))
    print("fortune1000:  %d" % len(fortune1000))
    print("federal:      %d" % len(federal))
    for b in BANDS:
        print("band/%-12s %d" % (b + ":", len(band_lists[b])))

    return groups, fortune1000, federal, band_lists


# ---------------------------------------------------------------------------
# Page generation
# ---------------------------------------------------------------------------

def write_pages(groups, fortune1000, federal, band_lists):
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
            "{% include company-listing-simple.html %}",
            "",
        ])

    d = os.path.join(SITE, "fortune-1000")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "Fortune 1000",
            "companies-fortune1000",
            "Fortune 100, 500, and 1000 companies with APIs on the network.",
            "Fortune 100, Fortune 500, and Fortune 1000 companies with APIs on the network.",
        ))

    d = os.path.join(SITE, "federal-government")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(flat_page(
            "Federal Government",
            "companies-federal",
            "US Federal Government agencies with APIs.",
            "United States Federal Government agencies and departments publishing APIs on the network.",
        ))

    for b in BANDS:
        label, desc = BAND_META[b]
        d = os.path.join(SITE, b)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(flat_page(
                "APIs.io Rating: %s" % label,
                "companies-%s" % b,
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
    g, f1000, fed, bands = main()
    write_pages(g, f1000, fed, bands)
