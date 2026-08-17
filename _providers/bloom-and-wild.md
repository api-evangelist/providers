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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloom-and-wild-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloom-and-wild-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: well-known/bloom-and-wild-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloom-and-wild-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloom-and-wild-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.bloomandwild.com
- group: operate
  title: ''
  type: Support
  url: https://www.bloomandwild.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.bloomandwild.com/the-blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomandwild.com/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomandwild.com/terms-and-privacy
created: '2026-07-17'
description: Bloom & Wild is a UK-founded direct-to-consumer flower delivery and gifting company, known for pioneering letterbox flowers that fit through a standard mail slot. Founded in 2013 and headquartered in London, it operates across the UK and Europe under a family of brands including Bloom & Wild, Bloomon and Bergamotte, offering one-off bouquets, plants, gifts and flower subscriptions through its website and mobile apps. Backed by General Catalyst and Index Ventures, it is a consumer e-commerce business rather than a public API provider; this profile captures its public web, security and domain posture. It publishes a /.well-known/security.txt security contact but no public developer program, OpenAPI, or API documentation was found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloom-and-wild.png
layout: provider
modified: '2026-07-18'
name: Bloom & Wild
nav: Providers
network: true
overview: 'Bloom & Wild is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Flowers, Gifting, and E-Commerce.


  Bloom & Wild''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 25
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloom-and-wild/refs/heads/main/screenshots/bloom-and-wild-2026-07-25T203354.png
security:
- kind: domain-security
  name: Bloom And Wild Domain Security
  slug: bloom-and-wild-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloom And Wild Vulnerability Disclosure
  slug: bloom-and-wild-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloom-and-wild
tags:
- Company
- Consumer
- Flowers
- Gifting
- E-Commerce
- Subscription
- Delivery
- Retail
website: https://www.bloomandwild.com
---
