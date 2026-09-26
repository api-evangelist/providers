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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abibaa
coverage:
  checked: '2026-09-06'
  detail: Abibaa's own domain abibaa.com no longer belongs to the company — it is registered to the reseller TurnCommerce/NameBright and every path, including /openapi.json and every /.well-known/ document, returns the same HugeDomains "for sale" HTML page, with no Internet Archive capture of a working site after March 2022.
  evidence:
  - status: 200
    url: https://abibaa.com/
  - status: 200
    url: https://abibaa.com/openapi.json
  - status: 200
    url: https://abibaa.com/.well-known/agent-card.json
  - status: 200
    url: https://equityzen.com/company/abibaa
  - status: 200
    url: https://www.linkedin.com/company/abibaa
  reason: defunct
  state: none
created: '2026-09-06'
description: 'Abibaa was a global online B2B/B2C/C2C e-marketplace headquartered in North Brunswick, New Jersey, founded around 2011-2012 and led by Benjamin Koufie Akomeah, built to help small and medium-sized businesses trade across borders through a multi-language buyer-and-seller marketplace. It was surfaced through the API Evangelist harvest backlog from a secondary-market (EquityZen) pre-IPO listing. As of the 2026-09-06 enrichment pass the company has no live web presence: abibaa.com is registered to the domain reseller TurnCommerce/NameBright and serves a HugeDomains "this domain is for sale" page, the Internet Archive holds no capture of a working site after March 2022, and no alternate company domain resolves. No API, developer program, documentation or machine-readable contract of any kind was found.'
layout: provider
modified: '2026-09-06'
name: Abibaa
nav: Providers
network: true
overview: Abibaa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, E-Commerce, B2B, and Cross-Border Trade.
random_paper: 20
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: abibaa
tags:
- Company
- Marketplace
- E-Commerce
- B2B
- Cross-Border Trade
- Small Business
- Defunct
---
