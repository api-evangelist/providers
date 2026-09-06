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
  url: security/pinduoduo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pddholdings.com
created: '2026-07-17'
description: 'Pinduoduo is a China-focused social commerce and agriculture-first e-commerce marketplace operated by PDD Holdings (Nasdaq: PDD), the multinational commerce group that also runs the cross-border marketplace Temu. Pinduoduo pioneered the "team purchase" (group-buy) model, connecting hundreds of millions of consumers directly with farmers, manufacturers, and merchants at scale. For developers, Pinduoduo runs a merchant-facing Open Platform (open.pinduoduo.com) that exposes gateway-style APIs for goods, orders, logistics, promotions, and store management to ISVs and merchant tools; that platform is geo-restricted to mainland China and was not directly reachable for artifact capture in this pass. This profile was surfaced as a portfolio company of Hongshan (formerly Sequoia Capital China) and enriched with verifiable corporate identity and domain security posture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pinduoduo.png
layout: provider
modified: '2026-07-20'
name: Pinduoduo
nav: Providers
network: true
overview: Pinduoduo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, E-Commerce, Marketplace, and Retail.
random_paper: 17
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinduoduo/refs/heads/main/screenshots/pinduoduo-2026-09-02T151256.png
security:
- kind: domain-security
  name: Pinduoduo Domain Security
  slug: pinduoduo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinduoduo
tags:
- Company
- Technology
- E-Commerce
- Marketplace
- Retail
- Social Commerce
- China
website: https://pddholdings.com
---
