#!/usr/bin/env python3
"""
Build the API Evangelist Companies listing.

Source of truth:
  - ../../all/*            : one git repo per company (the canonical company list)
  - ../../api-search/providers/_providers/<slug>.md : companies that have an
                            apis.io provider listing (i.e. they have an API)

Output:
  - _data/companies.json  : { "<group>": [ {name, slug, url, type}, ... ] }
                            group is the first letter (a-z) or "0-9".
  - index.html + <letter>/index.html + 0-9/index.html : per-letter pages.

Linking rule (no detail pages on this site):
  - has apis.io provider listing -> https://providers.apis.io/providers/<slug>/
  - otherwise                    -> https://github.com/api-evangelist/<slug>
"""
import json
import os
import re
import string

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))  # /Users/kinlane/GitHub
ALL = os.path.join(ROOT, "all")
PROVIDERS = os.path.join(ROOT, "api-search", "providers", "_providers")

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")


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


def provider_slugs():
    out = set()
    if not os.path.isdir(PROVIDERS):
        return out
    for f in os.listdir(PROVIDERS):
        if f.endswith(".md"):
            out.add(f[:-3])
    return out


def titleize(slug):
    parts = slug.replace("_", "-").split("-")
    return " ".join(p[:1].upper() + p[1:] if p else p for p in parts)


def display_name(slug):
    """Prefer the top-level `name:` in the company's apis.yml; fall back to a
    titleized slug."""
    apis_yml = os.path.join(ALL, slug, "apis.yml")
    if os.path.isfile(apis_yml):
        try:
            with open(apis_yml, "r", encoding="utf-8", errors="ignore") as fh:
                for line in fh:
                    # top-level key only (no leading whitespace)
                    if line and line[0] not in " \t#":
                        m = NAME_RE.match(line)
                        if m:
                            val = m.group(1).strip().strip("'\"").strip()
                            if val and val.lower() not in ("null", "~"):
                                return val
        except OSError:
            pass
    return titleize(slug)


def group_for(name):
    c = name.strip()[0:1].lower()
    if c in string.ascii_lowercase:
        return c
    return "0-9"


def main():
    providers = provider_slugs()
    groups = {}
    counts = {"provider": 0, "repo": 0}
    for slug in company_slugs():
        name = display_name(slug)
        if slug in providers:
            url = "https://providers.apis.io/providers/%s/" % slug
            typ = "API Provider"
            counts["provider"] += 1
        else:
            url = "https://github.com/api-evangelist/%s" % slug
            typ = "Repository"
            counts["repo"] += 1
        groups.setdefault(group_for(name), []).append(
            {"name": name, "slug": slug, "url": url, "type": typ}
        )

    for g in groups:
        groups[g].sort(key=lambda x: x["name"].lower())

    data_dir = os.path.join(SITE, "_data")
    os.makedirs(data_dir, exist_ok=True)
    with open(os.path.join(data_dir, "companies.json"), "w", encoding="utf-8") as fh:
        json.dump(groups, fh, ensure_ascii=False, indent=1, sort_keys=True)

    total = sum(len(v) for v in groups.values())
    print("companies: %d (providers=%d, repos=%d) across %d groups"
          % (total, counts["provider"], counts["repo"], len(groups)))
    return groups


def write_pages(groups):
    letters = list(string.ascii_uppercase)

    def page(letter_display, group_key, summary, permalink=None):
        n = len(groups.get(group_key, []))
        fm = [
            "---",
            "layout: default",
            "section: Companies",
            'title: "Companies - %s"' % letter_display,
            'summary: "%s"' % summary,
            "nav: Companies",
            'letter: "%s"' % letter_display,
        ]
        if permalink:
            fm.append("permalink: %s" % permalink)
        fm += ["---", "{% include company-listing.html %}", ""]
        return "\n".join(fm)

    # Home page = letter A
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page("A", "a",
                      "Alphabetical listing of every company tracked across the API Evangelist network, starting with A."))

    # Per-letter folder pages
    for L in letters:
        key = L.lower()
        d = os.path.join(SITE, key)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(page(L, key, "Companies starting with %s." % L))

    # 0-9 page
    d = os.path.join(SITE, "0-9")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page("0-9", "0-9", "Companies starting with a number."))

    # Remove legacy root <letter>.html duplicates (canonical pages live at /<letter>/)
    for L in letters:
        legacy = os.path.join(SITE, "%s.html" % L.lower())
        if os.path.isfile(legacy):
            os.remove(legacy)


if __name__ == "__main__":
    g = main()
    write_pages(g)
    print("pages written.")
