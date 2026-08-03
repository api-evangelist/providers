---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: The App API from Quikr — 1 operation(s) for app.
  name: Quikr App API
  slug: quikr-app-api
- description: The Platform API from Quikr — 1 operation(s) for platform.
  name: Quikr Platform API
  slug: quikr-platform-api
- description: The Public API from Quikr — 7 operation(s) for public.
  name: Quikr Public API
  slug: quikr-public-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://quikr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.quikr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.quikr.com/index.php/documentation
- group: company
  title: ''
  type: Blog
  url: https://blog.quikr.com
- group: build
  title: ''
  type: SDKs
  url: packages/quikr-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quikr-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quikr-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quikr-llms.txt
created: '2026-07-17'
description: Quikr is India's leading online classifieds platform, describing itself as "India's no. 1 online classifieds platform" for buying, selling, and renting across vehicles, real estate, jobs, mobiles, electronics, furniture, and 300+ service categories, plus education, events, pets, and matrimonial listings. Quikr operates a portfolio of brands including CommonFloor, Hiree, IndiaProperty, and Zefo. The Quikr Developer Platform (QDP) exposes classifieds data and actions to approved partner apps through an invitation-only beta API at api.quikr.com, using custom HMAC-SHA1 signed request headers rather than OAuth. Quikr is backed by Norwest Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quikr.png
layout: provider
modified: '2026-07-20'
name: Quikr
nav: Providers
network: true
overview: 'Quikr publishes 3 APIs on the [APIs.io](https://apis.io/) network: App API, Platform API, and Public API. Tagged areas include Company, Classifieds, Marketplace, Real Estate, and Automotive.


  Quikr''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 81
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 57.4
    developer_ergonomics: 26.1
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Quikr Authentication
  slug: quikr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Quikr Domain Security
  slug: quikr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quikr
tags:
- Company
- Classifieds
- Marketplace
- Real Estate
- Automotive
- Jobs
- Ecommerce
- India
- Developer Platform
website: https://quikr.com
---
