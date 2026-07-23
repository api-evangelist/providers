#!/usr/bin/env python3
"""
Build the Industries, Countries, and Australian Banks sections of the
API Evangelist Providers site.

Sources:
  - ../../signals-jobs/_data/industries.yml              : industry taxonomy
                                                           (companies per industry)
  - ../../all/*/apis.yml                                 : top-level tags
                                                           (country + Banks matching)
  - ../../api-search/providers/_providers/<slug>.md      : enriched provider data
                                                           (score.composite, score.band)

Output:
  - _data/sections-industries.json          : card data for /industries/
  - _data/sections-countries.json           : card data for /countries/
  - _data/companies-industry-<slug>.json    : provider list per industry
  - _data/companies-country-<slug>.json     : provider list per country
  - _data/companies-australian-banks.json   : AU banks sorted by rating score
  - industries/index.html + industries/<slug>/index.html
  - countries/index.html + countries/<slug>/index.html
  - australian-banks/index.html

Listings deliberately carry no per-provider links yet — provider detail
pages and apis.io links come later.
"""
import json
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))
ALL = os.path.join(ROOT, "all")
PROVIDERS = os.path.join(ROOT, "api-search", "providers", "_providers")
INDUSTRIES_YML = os.path.join(ROOT, "signals-jobs", "_data", "industries.yml")
SCORING_YML = os.path.join(ROOT, "api-search", "signals", "_data", "scoring.yml")

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")
DESC_RE = re.compile(r"^description:\s*(.*?)\s*$")
TAGS_RE = re.compile(r"^tags:\n((?:\s*- .+\n)+)", re.MULTILINE)

# Top industrial countries, roughly ordered by manufacturing output. Each maps
# to the tag aliases used across all/* apis.yml files. A provider is filed
# under a country when one of its top-level tags matches an alias exactly.
COUNTRIES = [
    ("china",          "China",          "🇨🇳", ["China"]),
    ("united-states",  "United States",  "🇺🇸", ["United States", "USA", "U.S.", "United States of America"]),
    ("japan",          "Japan",          "🇯🇵", ["Japan"]),
    ("germany",        "Germany",        "🇩🇪", ["Germany"]),
    ("india",          "India",          "🇮🇳", ["India"]),
    ("south-korea",    "South Korea",    "🇰🇷", ["South Korea", "Korea"]),
    ("italy",          "Italy",          "🇮🇹", ["Italy"]),
    ("france",         "France",         "🇫🇷", ["France"]),
    ("united-kingdom", "United Kingdom", "🇬🇧", ["United Kingdom", "UK", "Great Britain", "Britain"]),
    ("brazil",         "Brazil",         "🇧🇷", ["Brazil"]),
    ("mexico",         "Mexico",         "🇲🇽", ["Mexico"]),
    ("indonesia",      "Indonesia",      "🇮🇩", ["Indonesia"]),
    ("canada",         "Canada",         "🇨🇦", ["Canada"]),
    ("russia",         "Russia",         "🇷🇺", ["Russia", "Russian Federation"]),
    ("spain",          "Spain",          "🇪🇸", ["Spain"]),
    ("turkey",         "Turkey",         "🇹🇷", ["Turkey", "Türkiye"]),
    ("taiwan",         "Taiwan",         "🇹🇼", ["Taiwan"]),
    ("switzerland",    "Switzerland",    "🇨🇭", ["Switzerland"]),
    ("netherlands",    "Netherlands",    "🇳🇱", ["Netherlands"]),
    ("australia",      "Australia",      "🇦🇺", ["Australia"]),
    ("saudi-arabia",   "Saudi Arabia",   "🇸🇦", ["Saudi Arabia"]),
    ("poland",         "Poland",         "🇵🇱", ["Poland"]),
    ("sweden",         "Sweden",         "🇸🇪", ["Sweden"]),
    ("ireland",        "Ireland",        "🇮🇪", ["Ireland"]),
    ("singapore",      "Singapore",      "🇸🇬", ["Singapore"]),
]

# Material symbol per industry slug; anything unlisted gets `domain`.
INDUSTRY_ICONS = {
    "aerospace": "flight", "agriculture": "agriculture", "automotive": "directions_car",
    "cannabis": "spa", "cloud-data-platform": "cloud", "cpaas": "forum",
    "communications-platform-as-a-service-cpaas": "forum", "construction": "construction",
    "consumer-goods": "shopping_basket", "cruise-lines": "directions_boat",
    "customer-relationship-management-crm": "support_agent", "cybersecurity": "security",
    "defense": "shield", "e-commerce-platform": "shopping_cart", "energy": "bolt",
    "enterprise-software": "business_center", "entertainment": "theaters",
    "environmental-services": "recycling", "event-management-software": "event",
    "financial-services": "account_balance", "financial-technology": "payments",
    "fitness-wellness": "fitness_center", "food-delivery": "delivery_dining",
    "food-service": "restaurant", "gaming": "sports_esports", "healthcare": "medical_services",
    "hospitality": "hotel", "human-capital-management": "groups", "industrial": "factory",
    "insurance": "verified_user", "life-sciences": "biotech", "logistics": "local_shipping",
    "maritime": "anchor", "media": "newspaper", "mining": "landslide", "pet-care": "pets",
    "pharmaceutical": "medication", "productivity-software": "task_alt",
    "professional-services": "work", "rail": "train", "real-estate": "home_work",
    "retail": "storefront", "sports": "sports_soccer", "tax-compliance-software": "receipt_long",
    "technology": "memory", "telecommunications": "cell_tower", "transportation": "commute",
    "travel-technology": "travel", "utilities": "water_drop", "video-streaming": "smart_display",
    "waste-management": "delete",
}

RAW_BASE = "https://raw.githubusercontent.com/api-evangelist/%s/refs/heads/main/screenshots/%s"

BAND_LABELS = {
    "exemplar": "Exemplar", "strong": "Strong", "developing": "Developing",
    "thin": "Thin", "emerging": "Emerging", "minimal": "Minimal",
}


def slugify(name):
    s = name.lower()
    s = re.sub(r"\(([^)]*)\)", r" \1 ", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def newest_screenshot(slug):
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


def titleize(slug):
    parts = slug.replace("_", "-").split("-")
    return " ".join(p[:1].upper() + p[1:] if p else p for p in parts)


def read_apis_yml(slug):
    """Return (name, description, tags) from the top-level of all/<slug>/apis.yml,
    or None if the repo has no apis.yml."""
    apis_yml = os.path.join(ALL, slug, "apis.yml")
    if not os.path.isfile(apis_yml):
        return None
    name = titleize(slug)
    description = ""
    tags = []
    try:
        with open(apis_yml, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
    except OSError:
        return None
    m = TAGS_RE.search(content)
    if m:
        tags = [t.strip() for t in re.findall(r"-\s*(.+)", m.group(1))]
    in_desc = False
    desc_lines = []
    for line in content.splitlines(keepends=True):
        if line and line[0] not in " \t#":
            if in_desc:
                break
            mn = NAME_RE.match(line)
            if mn:
                val = mn.group(1).strip().strip("'\"").strip()
                if val and val.lower() not in ("null", "~"):
                    name = val
            md = DESC_RE.match(line)
            if md:
                inline = md.group(1).strip()
                if inline and inline not in (">-", "|", ">"):
                    description = inline
                else:
                    in_desc = True
        elif in_desc and line.strip():
            desc_lines.append(line.strip())
    if desc_lines:
        description = " ".join(desc_lines)
    return name, description, tags


def read_scores():
    """Read {slug: {composite, band}} from enriched provider frontmatter."""
    scores = {}
    if not os.path.isdir(PROVIDERS):
        return scores
    sc_re = re.compile(r"^score:\n\s{2}composite:\s*([\d.]+)\n\s{2}band:\s*(\S+)", re.MULTILINE)
    for fname in os.listdir(PROVIDERS):
        if not fname.endswith(".md"):
            continue
        try:
            with open(os.path.join(PROVIDERS, fname), "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            continue
        m = sc_re.search(content)
        if m:
            scores[fname[:-3]] = {"composite": float(m.group(1)), "band": m.group(2)}
    return scores


# Matches a top-level frontmatter block (`score:` / `agent_readiness:`) plus
# all following indented lines — same shape signals/score.rb writes.
def _fm_block(content, key):
    m = re.search(r"^%s:\n((?:[ \t]+.*\n|\n)*)" % key, content, re.MULTILINE)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(0)).get(key)
    except yaml.YAMLError:
        return None


def read_score_details(slug):
    """Full score + agent_readiness blocks for one provider, or None."""
    path = os.path.join(PROVIDERS, slug + ".md")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
    except OSError:
        return None
    return {
        "score": _fm_block(content, "score"),
        "agent": _fm_block(content, "agent_readiness"),
    }


def entry_for(slug, meta, scores):
    name, description, _tags = meta
    entry = {"name": name, "slug": slug}
    if description:
        entry["description"] = description
    shot = newest_screenshot(slug)
    if shot:
        entry["screenshot"] = shot
    sc = scores.get(slug)
    if sc:
        entry["score"] = sc["composite"]
        entry["band"] = sc["band"]
        entry["band_label"] = BAND_LABELS.get(sc["band"], sc["band"].title())
    return entry


# ---------------------------------------------------------------------------
# Page templates
# ---------------------------------------------------------------------------

def cards_page(title, summary, cards_key, base_path, intro):
    return "\n".join([
        "---",
        "layout: default",
        "section: Providers",
        'title: "%s"' % title,
        'summary: "%s"' % summary,
        "nav: Providers",
        'cards_key: "%s"' % cards_key,
        'cards_base: "%s"' % base_path,
        'intro: "%s"' % intro,
        "---",
        "{% include section-cards.html %}",
        "",
    ])


def listing_page(title, summary, data_key, rated=False, paper=None):
    include = "company-listing-rated.html" if rated else "company-listing-plain.html"
    lines = [
        "---",
        "layout: default",
        "section: Providers",
        'title: "%s"' % title,
        'summary: "%s"' % summary,
        "nav: Providers",
        'data_key: "%s"' % data_key,
    ]
    body = []
    # Optional sector-report promo band (see _includes/paper-promo.html). Emitted
    # here so it survives every rebuild rather than being hand-added to the page.
    if paper:
        lines += [
            "paper:",
            "  slug: %s" % paper["slug"],
            '  title: "%s"' % paper["title"],
            '  blurb: "%s"' % paper["blurb"].replace('"', "'"),
            '  price: "%s"' % paper.get("price", "500"),
        ]
        body.append("{% include paper-promo.html %}")
    lines.append("---")
    body.append("{%% include %s %%}" % include)
    return "\n".join(lines + body + [""])


def write_page(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def esc(text):
    return text.replace('"', "'")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    data_dir = os.path.join(SITE, "_data")
    os.makedirs(data_dir, exist_ok=True)
    scores = read_scores()

    # Mirror the rating rubric so the listing's rating panels can render the
    # exact same facet/dimension layout as apis.io provider detail pages.
    if os.path.isfile(SCORING_YML):
        with open(SCORING_YML, "r", encoding="utf-8") as fh:
            rubric_raw = fh.read()
        with open(os.path.join(data_dir, "scoring.yml"), "w", encoding="utf-8") as fh:
            fh.write("# Mirrored from api-search/signals/_data/scoring.yml by build-sections.py — do not edit here.\n")
            fh.write(rubric_raw)

    apis_cache = {}

    def meta_of(slug):
        if slug not in apis_cache:
            apis_cache[slug] = read_apis_yml(slug)
        return apis_cache[slug]

    # --- Industries -------------------------------------------------------
    with open(INDUSTRIES_YML, "r", encoding="utf-8") as fh:
        taxonomy = yaml.safe_load(fh)

    industry_cards = []
    for ind in taxonomy:
        ind_slug = slugify(ind["name"])
        comps = set()
        for sub in ind.get("industries") or []:
            for c in sub.get("companies") or []:
                comps.add(c)
        entries = []
        for c in sorted(comps):
            meta = meta_of(c)
            if meta is None:
                continue
            entries.append(entry_for(c, meta, scores))
        entries.sort(key=lambda e: e["name"].lower())
        with open(os.path.join(data_dir, "companies-industry-%s.json" % ind_slug), "w", encoding="utf-8") as fh:
            json.dump(entries, fh, ensure_ascii=False, indent=1)
        industry_cards.append({
            "slug": ind_slug,
            "name": ind["name"],
            "description": ind.get("description", ""),
            "icon": INDUSTRY_ICONS.get(ind_slug, "domain"),
            "count": len(entries),
        })
        write_page(
            os.path.join(SITE, "industries", ind_slug, "index.html"),
            listing_page(
                esc(ind["name"]),
                esc("%s providers in the %s industry." % (len(entries), ind["name"])),
                "companies-industry-%s" % ind_slug,
            ),
        )
    industry_cards.sort(key=lambda c: c["name"].lower())
    with open(os.path.join(data_dir, "sections-industries.json"), "w", encoding="utf-8") as fh:
        json.dump(industry_cards, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "industries", "index.html"),
        cards_page(
            "Industries",
            "Browse API providers by the industries they operate in.",
            "sections-industries",
            "/industries/",
            "Providers across the API Evangelist network organized by the %d industries tracked as part of ongoing industry research." % len(industry_cards),
        ),
    )

    # --- Countries --------------------------------------------------------
    alias_to_country = {}
    for slug, name, flag, aliases in COUNTRIES:
        for a in aliases:
            alias_to_country[a] = slug
    country_entries = {slug: [] for slug, _, _, _ in COUNTRIES}

    for repo in sorted(os.listdir(ALL), key=str.lower):
        if not os.path.isdir(os.path.join(ALL, repo)):
            continue
        meta = meta_of(repo)
        if meta is None:
            continue
        hit = set()
        for t in meta[2]:
            c = alias_to_country.get(t)
            if c and c not in hit:
                hit.add(c)
                country_entries[c].append(entry_for(repo, meta, scores))

    country_cards = []
    for slug, name, flag, _aliases in COUNTRIES:
        entries = country_entries[slug]
        entries.sort(key=lambda e: e["name"].lower())
        with open(os.path.join(data_dir, "companies-country-%s.json" % slug), "w", encoding="utf-8") as fh:
            json.dump(entries, fh, ensure_ascii=False, indent=1)
        country_cards.append({
            "slug": slug,
            "name": name,
            "flag": flag,
            "count": len(entries),
        })
        write_page(
            os.path.join(SITE, "countries", slug, "index.html"),
            listing_page(
                name,
                esc("%s providers operating in %s." % (len(entries), name)),
                "companies-country-%s" % slug,
            ),
        )
    country_cards.sort(key=lambda c: -c["count"])
    with open(os.path.join(data_dir, "sections-countries.json"), "w", encoding="utf-8") as fh:
        json.dump(country_cards, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "countries", "index.html"),
        cards_page(
            "Countries",
            "Browse API providers across the top industrial countries in the world.",
            "sections-countries",
            "/countries/",
            "Providers across the API Evangelist network organized by the top industrial countries, matched using the country tags providers carry.",
        ),
    )

    # --- Rated listings (Australian Banks, Market Data) -------------------

    def rated_entry(slug, meta):
        entry = entry_for(slug, meta, scores)
        details = read_score_details(slug)
        if details:
            sc = details.get("score") or {}
            if sc.get("facets"):
                entry["facets"] = sc["facets"]
            if sc.get("scored_at"):
                entry["scored_at"] = str(sc["scored_at"])
            if sc.get("schema_version") is not None:
                entry["schema_version"] = sc["schema_version"]
            if sc.get("regulatory"):
                entry["regulatory"] = sc["regulatory"]
            ag = details.get("agent") or {}
            if ag.get("score") is not None:
                entry["agent_score"] = ag["score"]
                entry["agent_band"] = ag.get("band", "")
                entry["agent_dims"] = ag.get("dimensions", {})
        return entry

    def band_grouped(entries):
        # Rating sort: scored providers by composite descending; unscored last,
        # alphabetically (unscored is "not yet rated", not a zero).
        entries.sort(key=lambda e: (-e.get("score", -1), e["name"].lower()))
        for rank, e in enumerate(entries, 1):
            e["rank"] = rank
        # Group by composite band, same ladder as apis.io/providers/. Only bands
        # with at least one member are emitted; the top two present open by default.
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
                "count": len(members), "companies": members,
            })
        for g in groups[:2]:
            g["open"] = True
        return {"total": len(entries), "bands": groups}

    # --- Australian Banks -------------------------------------------------
    au_banks = []
    for repo in sorted(os.listdir(ALL), key=str.lower):
        meta = meta_of(repo)
        if meta is None:
            continue
        tags = set(meta[2])
        if "Australia" in tags and "Banks" in tags:
            au_banks.append(rated_entry(repo, meta))
    au_banks_grouped = band_grouped(au_banks)
    with open(os.path.join(data_dir, "companies-australian-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(au_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "australian-banks", "index.html"),
        listing_page(
            "Australian Banks",
            "Australian banks ranked by their Kin Score.",
            "companies-australian-banks",
            rated=True,
            paper={
                "slug": "state-of-australian-banking-apis",
                "title": "The State of Australian Banking APIs",
                "blurb": "Fifty Consumer Data Right banks scored — and not one breaks 51. The anatomy of a mandated-but-mediocre ecosystem: uniform resources, the Kin Score facet-by-facet, the agent-readiness paradox, the FAPI/consent posture, provider-by-provider intelligence, and the investable thesis.",
                "price": "500",
            },
        ),
    )

    # --- Market Data ------------------------------------------------------
    # Roster-driven (not tag-matched): the curated market data vendor list
    # lives in all/0-working/market-data-roster.json with a tier per provider.
    MD_TIER_LABELS = {
        "enterprise-platform":  "Enterprise Platform",
        "exchange-data":        "Exchange Data Arm",
        "feed-infrastructure":  "Feed & Infrastructure",
        "developer-first":      "Developer-First",
        "crypto":               "Crypto Market Data",
    }
    market_data = []
    roster_path = os.path.join(ALL, "0-working", "market-data-roster.json")
    with open(roster_path, "r", encoding="utf-8") as fh:
        roster = json.load(fh)
    for p in roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = MD_TIER_LABELS.get(tier, titleize(tier))
        market_data.append(entry)
    market_data_grouped = band_grouped(market_data)
    with open(os.path.join(data_dir, "companies-market-data.json"), "w", encoding="utf-8") as fh:
        json.dump(market_data_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "market-data", "index.html"),
        listing_page(
            "Market Data",
            "Financial market data providers ranked by their Kin Score, from terminal and feed incumbents to API-first challengers.",
            "companies-market-data",
            rated=True,
            paper={
                "slug": "state-of-market-data-apis",
                "title": "The State of Market Data APIs",
                "blurb": "Fifty-eight providers scored. The feed is the commodity, the operation is the moat — the resource taxonomy, the Kin Score facet-by-facet, agent-readiness, security posture, provider-by-provider intelligence, and the investable thesis for operators and investors.",
                "price": "500",
            },
        ),
    )

    # --- UK Banking -------------------------------------------------------
    # Roster-driven (like Market Data): the curated UK banking list lives in
    # all/0-working/uk-banks-roster.json with a tier per provider.
    UK_TIER_LABELS = {
        "cma9":              "CMA9 (Mandated Open Banking)",
        "high-street":       "High-Street & Retail",
        "challenger":        "Challenger & Neobank",
        "baas-clearing":     "BaaS & Clearing",
        "building-society":  "Building Society",
        "sme":               "SME & Business",
        "specialist-lender": "Specialist & Mid-Tier Lender",
        "private-bank":      "Private Bank",
        "payments":          "Payments",
        "savings":           "Savings",
    }
    uk_banks = []
    uk_roster_path = os.path.join(ALL, "0-working", "uk-banks-roster.json")
    with open(uk_roster_path, "r", encoding="utf-8") as fh:
        uk_roster = json.load(fh)
    for p in uk_roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = UK_TIER_LABELS.get(tier, titleize(tier))
        uk_banks.append(entry)
    uk_banks_grouped = band_grouped(uk_banks)
    with open(os.path.join(data_dir, "companies-uk-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(uk_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "uk-banks", "index.html"),
        listing_page(
            "UK Banking",
            "UK banks and building societies ranked by their Kin Score, from the CMA9 Open Banking mandate to challengers, building societies, and private banks.",
            "companies-uk-banks",
            rated=True,
        ),
    )

    # --- US Banking -------------------------------------------------------
    # Roster-driven (like Market Data / UK): the curated US banking list lives
    # in all/0-working/us-banks-roster.json with a tier per provider.
    US_TIER_LABELS = {
        "money-center":    "Money-Center & Custody",
        "super-regional":  "Super-Regional",
        "regional":        "Regional",
        "digital":         "Digital & Neobank",
        "baas":            "Banking-as-a-Service",
        "credit-union":    "Credit Union",
        "aggregator":      "Aggregator & FDX",
    }
    us_banks = []
    us_roster_path = os.path.join(ALL, "0-working", "us-banks-roster.json")
    with open(us_roster_path, "r", encoding="utf-8") as fh:
        us_roster = json.load(fh)
    for p in us_roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = US_TIER_LABELS.get(tier, titleize(tier))
        us_banks.append(entry)
    us_banks_grouped = band_grouped(us_banks)
    with open(os.path.join(data_dir, "companies-us-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(us_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "us-banks", "index.html"),
        listing_page(
            "US Banking",
            "US banks, credit unions, neobanks, and banking-as-a-service providers ranked by their Kin Score — from the money-center banks and the BaaS layer to the aggregators wiring the CFPB 1033 / FDX open-finance era.",
            "companies-us-banks",
            rated=True,
        ),
    )

    print("industries:       %d (providers matched: %d)" % (
        len(industry_cards), sum(c["count"] for c in industry_cards)))
    print("countries:        %d (providers matched: %d)" % (
        len(country_cards), sum(c["count"] for c in country_cards)))
    print("australian banks: %d (scored: %d)" % (
        len(au_banks), sum(1 for b in au_banks if "score" in b)))
    print("market data:      %d (scored: %d)" % (
        len(market_data), sum(1 for e in market_data if "score" in e)))
    print("uk banks:         %d (scored: %d)" % (
        len(uk_banks), sum(1 for e in uk_banks if "score" in e)))
    print("us banks:         %d (scored: %d)" % (
        len(us_banks), sum(1 for e in us_banks if "score" in e)))


if __name__ == "__main__":
    main()
