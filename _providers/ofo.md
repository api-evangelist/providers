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
artifact_total: 1
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ofo/refs/heads/main/packages/ofo-packages.yml
  title: ''
  type: Packages
  url: packages/ofo-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Ofo stopped operating bikes by 2020 and its own host ofo.com now refuses TCP connections on both port 80 and port 443 despite still resolving, so every /.well-known/, /openapi.json and /llms.txt probe fails to connect rather than returning a status; the company never published a developer program in the first place, and the only surviving documentation of its endpoints is third-party reverse-engineering of the private mobile-app API at one.ofo.com.
  evidence:
  - status: 0
    url: https://ofo.com/
  - status: 0
    url: https://ofo.com/openapi.json
  - status: 0
    url: https://one.ofo.com/.well-known/agent-card.json
  - status: 0
    url: https://ofobike.com/
  - status: 404
    url: https://ofo.so/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/ofo
  - status: 403
    url: https://forgeglobal.com/ofo_stock/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Ofo (Chinese: 小黄车, "little yellow bike") was a Beijing dockless bicycle-sharing company founded in 2014 by Dai Wei and four classmates from the Peking University cycling club, and launched publicly on 7 September 2015. At its 2017 peak it had deployed more than 10 million bicycles across roughly 250 cities in 20 countries, reported over 60 million monthly active users, and was valued at around US$2 billion; in March 2018 it raised an $866M round led by Alibaba. Ofo''s bikes were unlocked exclusively through its own consumer iOS and Android app. The company never operated a developer portal, never published a machine-readable API contract, and never shipped official client SDKs — the only documentation of its endpoints is third-party reverse-engineering of the private mobile-app API at one.ofo.com. Ofo withdrew from most international markets in July 2018, collapsed under a deposit-refund backlog that left more than 10 million users queuing for refunds from December 2018, and
  had ceased bike-rental operations by 2020. ofo.com is still registered through Alibaba Cloud and still resolves, but its origin refuses connections on ports 80 and 443; the historic ofo.so host dropped and was re-registered by an unrelated party in April 2025 and now serves a parked arcade-game lander. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-26'
name: Ofo
nav: Providers
network: true
overview: Ofo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Transportation, Mobility, and Micromobility.
random_paper: 16
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
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
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
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
security:
- kind: domain-security
  name: Ofo Domain Security
  slug: ofo-domain-security
  summary_line: no transport/DNS hardening detected
slug: ofo
tags:
- Company
- Defunct
- Transportation
- Mobility
- Micromobility
- Bike Sharing
- Sharing Economy
- Consumer
- China
---
