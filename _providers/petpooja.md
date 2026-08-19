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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Petpooja Online Ordering Menu API
  slug: open-petpooja-menu-api
- collection_type: open
  name: Petpooja Online Ordering Menu Orders API
  slug: open-petpooja-orders-api
- collection_type: open
  name: Petpooja Online Ordering Menu Stock API
  slug: open-petpooja-stock-api
- collection_type: open
  name: Petpooja Online Ordering Menu Stores API
  slug: open-petpooja-stores-api
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
random_paper: 121
rate_limits:
- limit_count: 3
  name: Petpooja Rate Limits
  slug: petpooja-rate-limits
score:
  band: thin
  composite: 36.5
  delta: -1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
