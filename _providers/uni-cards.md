---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uni-cards-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uni-cards-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.uni.cards/
created: '2026-07-17'
description: Uni Cards (Uniorbit Technologies) is a Bangalore-based Indian consumer fintech backed by Accel that builds credit-card and pay-later products, best known for its Uni Pay 1/3rd Card and co-branded credit cards delivered through its consumer mobile app. Uni Cards publishes no public developer portal, API documentation, or SDKs; its api.uni.cards and docs.uni.cards hosts resolve but are closed behind a Cloudflare challenge, so its API surface is internal-only today.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uni-cards.png
layout: provider
modified: '2026-07-21'
name: Uni Cards
nav: Providers
network: true
overview: Uni Cards is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit Cards, Payments, and Consumer Finance.
random_paper: 20
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uni-cards/refs/heads/main/screenshots/uni-cards-2026-09-02T164906.png
security:
- kind: domain-security
  name: Uni Cards Domain Security
  slug: uni-cards-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uni-cards
tags:
- Company
- Fintech
- Credit Cards
- Payments
- Consumer Finance
- India
website: https://www.uni.cards/
---
