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
  url: security/vipthink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vipthink.net
created: '2026-07-17'
description: VIPThink (豌豆思维) is a Chinese online education company operated by Guangdong Happy Seeds Technology Co., Ltd. (广东快乐种子科技有限公司), delivering small-class live-streaming courses in mathematical thinking and logic for young children (roughly ages 3-8). It is part of a family of consumer education brands that also includes Hualala drawing classes (画啦啦), Wandou speech training (豌豆口才), Gubi early-learning (咕比启蒙), and Little Lighthouse (小灯塔). The company was surfaced as a portfolio company of SoftBank Vision Fund and added to the API Evangelist network. As of this enrichment pass, VIPThink operates only consumer-facing web and mobile learning products and publishes no public developer portal, API documentation, SDKs, or machine-readable API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vipthink.png
layout: provider
modified: '2026-07-21'
name: VIPThink
nav: Providers
network: true
overview: VIPThink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EdTech, Education, Online Learning, and Mathematics.
random_paper: 16
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vipthink/refs/heads/main/screenshots/vipthink-2026-09-02T165952.png
security:
- kind: domain-security
  name: Vipthink Domain Security
  slug: vipthink-domain-security
  summary_line: TLSv1.2
slug: vipthink
tags:
- Company
- EdTech
- Education
- Online Learning
- Mathematics
- Early Childhood Education
- China
- Consumer
website: https://vipthink.net
---
