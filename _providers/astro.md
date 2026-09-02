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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/astro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.astronauts.id/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/astro-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/astro-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.astronauts.id/
- group: company
  title: ''
  type: Blog
  url: https://www.astronauts.id/blog
- group: operate
  title: ''
  type: Support
  url: https://www.astronauts.id/sites/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astronauts.id/sites/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astronauts.id/sites/syarat-ketentuan
- group: company
  title: ''
  type: About
  url: https://www.astronauts.id/sites/tentang-astro
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astro-domain-security.yml
created: '2026-07-17'
description: Astro (PT Astro Technologies Indonesia, astronauts.id) is an Indonesian quick-commerce grocery and daily-needs delivery service that fulfills orders in as little as fifteen minutes across the Greater Jakarta (Jadetabek) area. The consumer mobile app offers more than 15,000 SKUs spanning fresh produce, meat and seafood, frozen and prepared meals, beverages, snacks, baby and maternal care, personal care and beauty, household supplies, and the private-label Astro Goods line, operating 24/7 from a network of dark stores. Astro is venture-backed by Accel, Lightspeed Venture Partners, and Redpoint Ventures. It is a consumer B2C app and publishes no public developer API; this API Evangelist profile tracks the company as a portfolio lead.
image: https://www.astronauts.id/mobile-web-assets/img/astro-lite-og.jpg
layout: provider
modified: '2026-07-18'
name: Astro
nav: Providers
network: true
overview: 'Astro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Quick Commerce, Grocery Delivery, and E-Commerce.


  Astro''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astro/refs/heads/main/screenshots/astro-2026-07-25T201507.png
security:
- kind: domain-security
  name: Astro Domain Security
  slug: astro-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Astro Vulnerability Disclosure
  slug: astro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: astro
tags:
- Company
- Consumer
- Quick Commerce
- Grocery Delivery
- E-Commerce
- Retail
- Indonesia
- On-Demand Delivery
website: https://www.astronauts.id/
---
