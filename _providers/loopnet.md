---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Access commercial real estate property listings including office, retail, industrial, multifamily, land, and hospitality properties for sale and lease across the US, Canada, and UK. Data includes prop
  name: LoopNet Listings API
  slug: loopnet-listings-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loopnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loopnet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.loopnet.com/solutions/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/loopnet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loopnet
- group: company
  title: ''
  type: Blog
  url: https://www.loopnet.com/learn/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loopnet.com/solutions/ad-packages/silver-listing-plan
- group: operate
  title: ''
  type: StatusPage
  url: https://loopservice.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/loopnet
- group: commercial
  title: ''
  type: Plans
  url: plans/loopnet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loopnet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loopnet-finops.yml
created: '2026-06-13'
description: LoopNet is the leading commercial real estate marketplace, owned by CoStar Group, offering access to property listings, sale comparables, lease rates, market analytics, and CRE investment data. Brokers, owners, and investors use LoopNet to market and discover office, retail, industrial, multifamily, land, and hospitality properties across the US, Canada, and the UK. Integration is available via LoopLink for embedding property search on third-party websites, and data access for enterprise clients is arranged through CoStar Group agreements.
finops:
- name: Loopnet Finops
  service_category: ''
  slug: loopnet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loopnet.png
layout: provider
modified: '2026-06-13'
name: LoopNet
nav: Providers
network: true
overview: 'LoopNet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Commercial Real Estate, Property Listings, CRE, Real Estate, and Market Analytics.


  LoopNet''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Loopnet Plans Pricing
  plan_count: 5
  slug: loopnet-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Loopnet Rate Limits
  slug: loopnet-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Loopnet Domain Security
  slug: loopnet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: loopnet
tags:
- Commercial Real Estate
- Property Listings
- CRE
- Real Estate
- Market Analytics
- CoStar
- Lease Rates
- Sale Comparables
website: https://www.loopnet.com/
---
