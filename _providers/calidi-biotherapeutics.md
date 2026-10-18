---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation not publicly available; no machine-readable contract found.
  name: Calidi Biotherapeutics API
  slug: calidi-biotherapeutics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calidi-biotherapeutics/refs/heads/main/hosts/calidi-biotherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calidi-biotherapeutics-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ir.calidibio.com/news/default.aspx
- group: other
  title: ''
  type: Leadership
  url: https://www.calidibio.com/company/team/
- group: company
  title: ''
  type: Blog
  url: https://www.calidibio.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calidi-biotherapeutics/refs/heads/main/security/calidi-biotherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calidi-biotherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calidibio.com/
coverage:
  checked: '2026-10-06'
  detail: No public API documentation or machine‑readable spec was found on the company’s website or API host.
  evidence:
  - status: 0
    url: https://api.calidibio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Calidi Biotherapeutics is a biotechnology company focused on developing genetically engineered cell therapies for cancer and other complex diseases. Based in the United States, Calidi leverages its proprietary platform to deliver precise genetic medicines to disease sites, advancing pipelines in oncology and beyond. The company provides detailed scientific information, pipeline updates, and investor relations through its corporate website.
layout: provider
modified: '2026-10-06'
name: Calidi Biotherapeutics
nav: Providers
network: true
overview: 'Calidi Biotherapeutics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Calidi Biotherapeutics'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calidi Biotherapeutics Domain Security
  slug: calidi-biotherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calidi-biotherapeutics
tags:
- Company
website: https://www.calidibio.com/
---
