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
  url: security/pocket-protector-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pocketprotector.xyz/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pocketprotector.xyz/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pocketprotector.xyz/terms-of-service
created: '2026-07-17'
description: Pocket Protector is a consumer peer-to-peer trading application operated by Pocket Protector Inc. Under the tagline "Trade Better Together," it lets users trade items and assets with one another through an iOS app and an accompanying Telegram bot (@pocketprotectorbot). The company was surfaced as a portfolio company of Electric Capital and added to the API Evangelist network for enrichment; as of this pass it publishes a marketing site with privacy and terms pages but no public developer API, SDK, documentation, or OpenAPI surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pocket-protector.png
layout: provider
modified: '2026-07-20'
name: Pocket Protector
nav: Providers
network: true
overview: Pocket Protector is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading, Consumer App, Mobile, and iOS.
random_paper: 5
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pocket-protector/refs/heads/main/screenshots/pocket-protector-2026-09-02T151845.png
security:
- kind: domain-security
  name: Pocket Protector Domain Security
  slug: pocket-protector-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pocket-protector
tags:
- Company
- Trading
- Consumer App
- Mobile
- iOS
- Telegram
- Peer-to-Peer
website: https://www.pocketprotector.xyz/
---
