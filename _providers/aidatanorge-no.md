---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aidatanorge-no/hosts/aidatanorge-no-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidatanorge-no-hosts.yml
- group: other
  href: https://artifacts.apis.io/aidatanorge-no/vendors/aidatanorge-no-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aidatanorge-no-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aidatanorge-no/security/aidatanorge-no-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidatanorge-no-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidatanorge.no/
coverage:
  checked: '2026-10-29'
  detail: No machine‑readable API specification was found on the provider's site.
  evidence:
  - status: 200
    url: https://aidatanorge.no/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Aidata Norge provides a Nordic financial data platform for AI agents, offering semantic search across company filings, macroeconomic data, energy prices, and commodities. The service aggregates and indexes over a million data points, delivering real-time day-ahead power prices for all Nordic bidding zones, detailed company information for Norway, Denmark, and Finland, and comprehensive macro context. It enables analysts and AI applications to perform due‑diligence‑ready queries, cross‑referencing financial reports with market trends, all without requiring an API key.
layout: provider
modified: '2026-10-29'
name: aidatanorge-no
nav: Providers
network: true
overview: aidatanorge-no is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Artificial Intelligence, Data, and Nordic.
random_paper: 1
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aidatanorge-no/aidatanorge-no-2026-11-03T120451.png
security:
- kind: domain-security
  name: Aidatanorge No Domain Security
  slug: aidatanorge-no-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aidatanorge-no
tags:
- Company
- Finance
- Artificial Intelligence
- Data
- Nordic
website: https://aidatanorge.no/
---
