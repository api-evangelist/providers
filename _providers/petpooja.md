---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Petpooja Agentic Access
  operation_count: 4
  slug: petpooja-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: Fetch a mapped restaurant's menu / catalog from Petpooja.
  name: Petpooja Menu API
  slug: petpooja-menu-api
- description: Push online orders into the Petpooja POS.
  name: Petpooja Orders API
  slug: petpooja-orders-api
- description: Item stock and availability.
  name: Petpooja Stock API
  slug: petpooja-stock-api
- description: Store / restaurant online-ordering availability.
  name: Petpooja Stores API
  slug: petpooja-stores-api
artifact_total: 12
collections:
- collection_type: open
  name: Petpooja Online Ordering API
  slug: open-petpooja
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/petpooja-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/petpooja-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petpooja-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/petpooja-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/petpooja
- group: company
  title: ''
  type: Website
  url: https://www.petpooja.com
- group: docs
  title: ''
  type: Documentation
  url: https://onlineorderingapisv210.docs.apiary.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/petpooja-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/petpooja-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/petpooja-finops.yml
created: '2026-06-21'
description: Petpooja is a restaurant point-of-sale (POS) and management platform serving 75,000+ restaurants across India, the Middle East, Canada, and South Africa. Its Online Ordering API lets aggregators and partner ordering platforms sync a restaurant's menu/catalog, push orders into the Petpooja POS, receive order-status callbacks, and toggle item stock and store availability.
finops:
- name: Petpooja Finops
  service_category: Business Application Software
  slug: petpooja-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petpooja.png
layout: provider
modified: '2026-06-21'
name: Petpooja
nav: Providers
network: true
overview: 'Petpooja publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Menu API, Orders API, Stock API, and 1 more. Tagged areas include Restaurant, POS, Online Ordering, Menu, and Food Delivery.


  Petpooja''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Petpooja Plans Pricing
  plan_count: 3
  slug: petpooja-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 3
  name: Petpooja Rate Limits
  slug: petpooja-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Petpooja Authentication
  slug: petpooja-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Petpooja Domain Security
  slug: petpooja-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Petpooja Vulnerability Disclosure
  slug: petpooja-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: petpooja
tags:
- Restaurant
- POS
- Online Ordering
- Menu
- Food Delivery
website: https://www.petpooja.com
---
