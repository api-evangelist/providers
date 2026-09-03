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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/metacrine_stock/
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/metacrine-well-known.yml
coverage:
  checked: '2026-08-25'
  detail: Metacrine, Inc. was a clinical-stage biopharmaceutical developer that never shipped software, and it filed a Certificate of Dissolution with the Delaware Secretary of State on 2023-03-24; its original domain metacrine.com has since lapsed onto Network Solutions' PENDINGRENEWALDELETION nameservers and a Media.net parking wildcard that answers HTTP 200 with the same 122-byte "Error. Page cannot be displayed" stub for every path and every subdomain, including a control path that cannot exist, so none of those 200s is a document.
  evidence:
  - status: 200
    url: https://www.sec.gov/Archives/edgar/data/1634379/000119312523079293/d453945d8k.htm
  - status: 200
    url: http://metacrine.com/
  - status: 200
    url: http://metacrine.com/openapi.json
  - status: 200
    url: http://metacrine.com/.well-known/agent-card.json
  - status: 200
    url: http://metacrine.com/control-path-does-not-exist-98765
  - status: 0
    url: https://metacrine.com/
  - status: 404
    url: https://api.github.com/orgs/metacrine
  - status: 404
    url: https://registry.npmjs.org/metacrine
  - status: 403
    url: https://forgeglobal.com/metacrine_stock/
  reason: defunct
  state: none
created: '2026-08-25'
description: Metacrine, Inc. was a San Diego, California clinical-stage biopharmaceutical company founded in 2014 to develop differentiated therapies for liver and gastrointestinal disease. It built a proprietary farnesoid X receptor (FXR) platform on a distinct chemical scaffold and advanced two oral, once-daily FXR agonists — MET409 and MET642 — through Phase 1 and Phase 2 trials in non-alcoholic steatohepatitis (NASH), alongside exploratory work in inflammatory bowel disease. Backed by ARCH Venture Partners, Polaris Partners, venBio and EcoR1 Capital, it raised a $36M round in 2015 and a $65M Series C in June 2018 before pricing an initial public offering on 2020-09-15 of 6,540,000 shares at $13.00, for roughly $85.0M gross, and listing on the Nasdaq Capital Market as MTCR. Equillium, Inc. agreed to acquire the company in an all-stock transaction announced 2022-09-06, but the two mutually terminated the merger agreement on 2022-12-23. The board approved a Plan of Dissolution on 2023-01-24;
  Nasdaq issued a minimum-bid-price delisting notice on 2023-01-31, trading was suspended on 2023-02-09 and delisting took effect 2023-03-13; the FXR program assets were sold under a February 2023 term sheet for up to $4.0M in cash plus assumed liabilities; stockholders approved the dissolution on 2023-03-23; and the company filed a Certificate of Dissolution with the Delaware Secretary of State on 2023-03-24, effective on filing under DGCL Section 275. Metacrine was a drug developer, not a software vendor, and it never published a developer program, public API, SDK, webhook surface, or machine-readable specification of any kind. Its domain metacrine.com has since lapsed and is parked. This profile is retained as a historical record; there is no API surface to enrich.
layout: provider
modified: '2026-08-25'
name: Metacrine
nav: Providers
network: true
overview: Metacrine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Biotechnology, Pharmaceuticals, and Life Sciences.
random_paper: 7
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 1
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
      reason: no_resolvable_host
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: metacrine
tags:
- Company
- Defunct
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Drug Discovery
- Therapeutics
- Healthcare
---
