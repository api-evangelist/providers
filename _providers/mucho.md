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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://mucho.asia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mucho/refs/heads/main/security/mucho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mucho-domain-security.yml
created: '2026-07-17'
description: Mucho (Mucho Indonesia) was an Indonesian social-commerce startup founded in 2018 and headquartered in South Jakarta, positioned as Indonesia's first social online shopping application and often described as an aspiring "Pinduoduo for Indonesia." Its mobile app let users buy together with friends to unlock group-buying discounts, cutting distribution layers by working directly with brand owners and pairing frictionless payment with logistics support. The company raised early / seed funding with participation from Qiming Venture Partners. Mucho has since shut down; its app is no longer distributed and the mucho.asia domain now resolves to a parked placeholder page with no product, API, or developer surface. This profile is retained as a defunct-company record surfaced through the Qiming portfolio graph.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mucho.png
layout: provider
modified: '2026-07-20'
name: mucho
nav: Providers
network: true
overview: mucho is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Commerce, E-Commerce, Group Buying, and Retail.
random_paper: 12
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
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
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mucho Domain Security
  slug: mucho-domain-security
  summary_line: TLSv1.3
slug: mucho
tags:
- Company
- Social Commerce
- E-Commerce
- Group Buying
- Retail
- Indonesia
- Mobile Shopping
- Defunct
website: https://mucho.asia
---
