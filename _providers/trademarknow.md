---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.trademarknow.com/'', ''status'': 301, ''note'': ''declared website redirects to https://corsearch.com/trademarknow — a different registrable domain (trademarknow.com -> corsearch.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/trademarknow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trademarknow.com/
- group: start
  title: ''
  type: Login
  url: https://tm.corsearch.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corsearch.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corsearch.com/user-agreement
created: '2026-07-17'
description: TrademarkNow is an AI-native trademark clearance, screening, and watching platform, now part of Corsearch. It helps brand owners and legal teams create, launch, and defend trademarks globally using neural-network models that analyze phonetics, spelling, meaning, and visuals to surface conflicts across trademark registries. Its modules include ExaMatch for preliminary screening across 190+ registries with phonetic matching, NameCheck for instant trademark risk assessment, LogoCheck for deep-learning image-based logo conflict clearance, and Portfolio Analyzer for portfolio-strength benchmarking and coverage-gap analysis. TrademarkNow is delivered as a SaaS web platform (login at tm.corsearch.com) and does not publish a public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trademarknow.png
layout: provider
modified: '2026-07-21'
name: TrademarkNow
nav: Providers
network: true
overview: TrademarkNow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trademark, Intellectual Property, Legal Tech, and Brand Protection.
random_paper: 14
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trademarknow/refs/heads/main/screenshots/trademarknow-2026-09-02T164059.png
security:
- kind: domain-security
  name: Trademarknow Domain Security
  slug: trademarknow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trademarknow
tags:
- Company
- Trademark
- Intellectual Property
- Legal Tech
- Brand Protection
- Trademark Search
- Artificial Intelligence
- Software-as-a-Service
website: https://www.trademarknow.com/
---
