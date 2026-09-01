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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-sciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://epicsciences.com
coverage:
  checked: '2026-08-12'
  detail: epicsciences.com — the site every third-party record still lists as the company website — serves a blanket HTTP 301 to an unrelated third-party domain (awaji-musicisland.com) on every path including /robots.txt and every /.well-known/ location, and the domain publishes no MX, SPF, DMARC, CAA or DNSSEC records, so there is no live Epic Sciences web presence left to profile, let alone a developer surface.
  evidence:
  - status: 301
    url: https://www.epicsciences.com/
  - status: 301
    url: https://www.epicsciences.com/.well-known/agent-card.json
  - status: 301
    url: https://www.epicsciences.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/epic-sciences
  reason: defunct
  state: none
created: '2026-08-12'
description: Epic Sciences is a San Diego, California clinical diagnostics company founded in 2008 that develops blood-based "liquid biopsy" tests for oncology. Its platform, licensed from the Peter Kuhn laboratory at Scripps Research, isolates and characterizes rare circulating tumor cells (CTCs) from whole blood using specialized assays and digital pathology algorithms, and is paired with circulating tumor DNA (ctDNA) sequencing to inform treatment selection and track how a tumor evolves. Its lead product, DefineMBC, is a comprehensive blood biopsy for metastatic breast cancer whose 56-gene ctDNA panel received Medicare coverage in April 2023. The company also runs its platform as a service for pharmaceutical partners measuring outcomes in clinical trials, and in 2020 partnered with Predicine to combine CTC and ctDNA analysis in a single offering. Epic Sciences is privately held and has raised roughly $204M across seven rounds through a Series G in April 2023. It is a laboratory diagnostics
  provider, not a software vendor, and publishes no public API, developer program, SDK or machine-readable specification.
layout: provider
modified: '2026-08-12'
name: Epic Sciences
nav: Providers
network: true
overview: Epic Sciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Oncology, and Life Sciences.
random_paper: 5
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Epic Sciences Domain Security
  slug: epic-sciences-domain-security
  summary_line: TLSv1.3
slug: epic-sciences
tags:
- Company
- Healthcare
- Diagnostics
- Oncology
- Life Sciences
- Biotechnology
- Laboratory
- Precision Medicine
website: https://epicsciences.com
---
