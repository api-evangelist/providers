---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://brytercx.com/'', ''status'': 302, ''note'': ''declared website redirects to https://ignitetech.ai:443/ — a different registrable domain (brytercx.com -> ignitetech.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://brytercx.com/
coverage:
  checked: '2026-08-08'
  detail: Every BryterCX host — brytercx.com, api./docs./developer.brytercx.com and the legacy clickfox.com — 302s to the IgniteTech homepage after the 2022 asset acquisition, and IgniteTech's own software library 404s on /softwarelibrary/brytercx, so no BryterCX surface, developer portal or spec remains to profile.
  evidence:
  - status: 302
    url: https://brytercx.com/openapi.json
  - status: 302
    url: https://api.brytercx.com/.well-known/agent-card.json
  - status: 302
    url: https://docs.brytercx.com/llms.txt
  - status: 404
    url: https://ignitetech.ai/softwarelibrary/brytercx
  - status: 404
    url: https://api.github.com/orgs/brytercx
  reason: defunct
  state: none
created: '2026-08-08'
description: 'BryterCX was a customer journey intelligence company based in Greenwood Village, Colorado, formerly known as ClickFox. Its Journey Intelligence platform stitched siloed digital, contact-center and back-office data into a single omnichannel view of the customer journey, with journey mapping, monitoring, analytics and orchestration, later extended with the Iris Insights AI/ML anomaly-detection layer. IgniteTech acquired the BryterCX assets from Arrowroot Capital in January 2022. The BryterCX brand no longer operates independently: brytercx.com and the legacy clickfox.com both 302 to the IgniteTech homepage, and IgniteTech''s own software library returns 404 for the BryterCX and ClickFox product slugs. No public API, developer portal or machine-readable contract survives the acquisition.'
layout: provider
modified: '2026-08-08'
name: BryterCX
nav: Providers
network: true
overview: BryterCX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Experience, Customer Journey Analytics, Journey Intelligence, and Analytics.
random_paper: 1
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brytercx/refs/heads/main/screenshots/brytercx-2026-09-02T144950.png
slug: brytercx
tags:
- Company
- Customer Experience
- Customer Journey Analytics
- Journey Intelligence
- Analytics
- Contact Center
- Acquired
website: https://brytercx.com/
---
