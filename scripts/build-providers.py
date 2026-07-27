#!/usr/bin/env python3
"""
Build the API Evangelist provider detail pages.

Reintroduces a first-class, NARRATIVE detail page for every provider in the
API Evangelist network at providers.apievangelist.com/providers/<slug>/.

Every provider on the network gets a page. The heavy derivation work — parsing
each provider's OpenAPI/AsyncAPI/GraphQL/scopes/security/etc. into the artifact
lists, the Kin Score, agent readiness, and the access model — already happens in
the apis.io build (api-search/providers/_providers/<slug>.md). Rather than
re-derive any of it, this script REUSES that data: it reads each apis.io
provider file, trims it to the fields the narrative page needs (dropping the
large source_yaml blob, the per-spec api_specs list, and the subway map), and
writes a lightweight collection document into this repo's _providers/.

Providers that exist in all/* but have not yet been picked up by the apis.io
build (a couple hundred, mostly VC firms) get a minimal page built straight from
their all/<slug>/apis.yml so the coverage is complete — "loop through all/* and
make sure every provider is represented."

It also writes _data/papers.json (the API Evangelist white-paper catalogue, for
the random paper feature in the right sidebar) and stamps a deterministic
`random_paper` onto every provider so each page features one, varying by slug.

Sources
  - ../../all/*/apis.yml                              : the canonical provider list
  - ../../api-search/providers/_providers/<slug>.md   : derived artifact + score data
  - ../../papers/_papers/*.md                         : white-paper catalogue

Output
  - _providers/<slug>.md         : one narrative provider page per provider
  - _data/papers.json            : white-paper catalogue for the sidebar feature

Idempotent and re-runnable. Pass --limit N to build only the first N (for a
quick local render check).
"""
import argparse
import glob
import json
import os
import re
import shutil

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))
ALL = os.path.join(ROOT, "all")
APISIO = os.path.join(ROOT, "api-search", "providers", "_providers")
PAPERS = os.path.join(ROOT, "api-evangelist", "papers", "_papers")
OUT = os.path.join(SITE, "_providers")
DATA = os.path.join(SITE, "_data")

# Fields carried from the apis.io provider file onto the API Evangelist page.
# Everything the narrative + artifact cards + sidebar need, and nothing heavy:
# source_yaml (the biggest field by far), api_specs (a per-spec duplicate of
# `apis`), subway_map, and the source_* pointers are deliberately dropped.
KEEP = [
    # identity
    "name", "slug", "description", "overview", "website", "image", "screenshot",
    "tags", "api_count", "created", "modified", "deprecated", "deprecated_note",
    # rating
    "score", "agent_readiness", "access_model",
    # artifact collections (each is a list the page renders as cards)
    "apis", "arazzos", "asyncapis", "collections", "examples", "features",
    "finops", "graphqls", "json_schemas", "json_structures", "jsonld",
    "plans", "rate_limits", "rules", "scopes", "security", "skills",
    "solutions", "use_cases", "integrations", "agentic_access",
    "mcp_servers", "skill_count", "press", "crds", "common",
]

# The artifact collections, in the order the page tells the story. Each entry:
# (frontmatter_key, human label) — used to compute which specs a provider has
# for the intro narrative and the "artifacts" count.
ARTIFACT_KEYS = [
    ("apis", "APIs"), ("collections", "collections"), ("arazzos", "Arazzo workflows"),
    ("mcp_servers", "MCP servers"), ("skills", "agent skills"), ("graphqls", "GraphQL schemas"),
    ("plans", "pricing plans"), ("rate_limits", "rate limits"), ("finops", "FinOps profiles"),
    ("features", "features"), ("asyncapis", "event specifications"), ("jsonld", "semantic vocabularies"),
    ("rules", "Spectral rulesets"), ("json_schemas", "JSON Schema definitions"),
    ("json_structures", "JSON Structure definitions"), ("examples", "examples"),
    ("security", "security signals"), ("scopes", "OAuth scope sets"),
    ("agentic_access", "agentic-access contracts"), ("use_cases", "use cases"),
    ("integrations", "integrations"), ("solutions", "solutions"),
]


def read_frontmatter(path):
    """Return the YAML front matter of a Jekyll doc as a dict (or None).

    The apis.io provider files carry `source_yaml`, a double-quoted scalar
    holding the provider's whole raw apis.yml. YAML wraps long quoted scalars
    across physical lines, so a bare `---` can and does land INSIDE that value.
    Splitting on the first `---` therefore cuts mid-scalar, YAML raises, and the
    caller silently falls back to a minimal page with no score or agent_readiness
    — which is how 975 providers (Stripe among them) lost their Kin Score panels.

    So: walk every candidate closing delimiter and take the first that actually
    parses into a mapping.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    for match in re.finditer(r"^---[ \t]*$", text[4:], re.MULTILINE):
        block = text[4:4 + match.start()]
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            return data
    return None


def load_papers():
    """Build the white-paper catalogue used by the random-paper sidebar feature."""
    papers = []
    for path in sorted(glob.glob(os.path.join(PAPERS, "*.md"))):
        fm = read_frontmatter(path)
        if not fm or not fm.get("slug"):
            continue
        cover = fm.get("cover") or "/assets/covers/%s.png" % fm["slug"]
        if cover.startswith("/"):
            cover = "https://papers.apievangelist.com" + cover
        papers.append({
            "slug": fm["slug"],
            "title": fm.get("title", fm["slug"]),
            "tagline": (fm.get("tagline") or fm.get("summary") or "").strip(),
            "area": fm.get("area", "White Paper"),
            "price": str(fm.get("price", "")).replace(".00", ""),
            "cover": cover,
        })
    return papers


def artifact_summary(fm):
    """List of 'N label' phrases for the collections a provider actually has."""
    phrases = []
    total = 0
    for key, label in ARTIFACT_KEYS:
        val = fm.get(key)
        n = len(val) if isinstance(val, list) else 0
        if n:
            total += n
            phrases.append((n, label))
    return phrases, total


def trim(fm):
    """Keep only the fields the narrative page needs."""
    out = {}
    for k in KEEP:
        if k in fm and fm[k] not in (None, "", [], {}):
            out[k] = fm[k]
    return out


def minimal_from_all(slug):
    """Fallback page data from all/<slug>/apis.yml for providers the apis.io
    build has not yet picked up."""
    # A bare page from the slug alone — the last-resort stub so a provider whose
    # apis.yml won't parse still gets a page rather than a 404.
    stub = {"name": slug.replace("-", " ").title(), "slug": slug}
    path = os.path.join(ALL, slug, "apis.yml")
    try:
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
    except (OSError, yaml.YAMLError):
        return stub
    if not isinstance(doc, dict):
        return stub
    apis = doc.get("apis") or []
    out = {
        "name": doc.get("name", slug),
        "slug": slug,
        "description": doc.get("description", ""),
        "tags": doc.get("tags") or [],
        "image": doc.get("image"),
        "created": doc.get("created"),
        "modified": doc.get("modified"),
        "api_count": len(apis) if isinstance(apis, list) else 0,
    }
    am = doc.get("accessModel")
    if isinstance(am, dict):
        out["access_model"] = am
    return {k: v for k, v in out.items() if v not in (None, "", [], {})}


def dump(slug, data, papers_len):
    """Write _providers/<slug>.md with trimmed front matter + narrative body seed."""
    data["layout"] = "provider"
    data["nav"] = "Providers"
    data["network"] = True
    # Deterministic per-provider paper pick — varies by slug, stable across runs.
    if papers_len:
        data["random_paper"] = sum(ord(c) for c in slug) % papers_len
    phrases, total = artifact_summary(data)
    data["artifact_total"] = total
    body = ""  # the layout renders everything from front matter
    with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as fh:
        fh.write("---\n")
        yaml.safe_dump(data, fh, sort_keys=True, allow_unicode=True, default_flow_style=False, width=1000)
        fh.write("---\n")
        fh.write(body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="build only the first N providers")
    ap.add_argument("--only", help="comma-separated slugs to build")
    args = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)
    os.makedirs(DATA, exist_ok=True)

    # Mirror the resource-group taxonomy from the apis.io build so the Resources
    # section groups the same way it does there.
    rg_src = os.path.join(ROOT, "api-search", "providers", "_data", "resource_groups.yml")
    if os.path.isfile(rg_src):
        shutil.copyfile(rg_src, os.path.join(DATA, "resource_groups.yml"))

    papers = load_papers()
    with open(os.path.join(DATA, "papers.json"), "w", encoding="utf-8") as fh:
        json.dump(papers, fh, ensure_ascii=False, indent=2)
    print("papers.json: %d white papers" % len(papers))

    slugs = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ALL, "*", "apis.yml")))
    if args.only:
        want = set(args.only.split(","))
        slugs = [s for s in slugs if s in want]
    if args.limit:
        slugs = slugs[:args.limit]

    reused = minimal = skipped = 0
    for i, slug in enumerate(slugs):
        apisio_path = os.path.join(APISIO, slug + ".md")
        fm = read_frontmatter(apisio_path)
        if fm:
            data = trim(fm)
            data["slug"] = slug
            if not data.get("name"):
                data["name"] = slug
            reused += 1
        else:
            data = minimal_from_all(slug)
            if not data:
                skipped += 1
                continue
            minimal += 1
        dump(slug, data, len(papers))
        if (i + 1) % 2000 == 0:
            print("  ... %d/%d" % (i + 1, len(slugs)))

    print("providers written: %d (reused apis.io: %d, minimal from all/: %d, skipped: %d)"
          % (reused + minimal, reused, minimal, skipped))


if __name__ == "__main__":
    main()
