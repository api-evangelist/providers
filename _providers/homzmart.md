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
  url: security/homzmart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/homzmart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homzmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://homzmart.com
created: '2026-07-17'
description: Homzmart is a Cairo, Egypt-based online marketplace for furniture, home decor, appliances, and workspace products that connects thousands of local manufacturers, brands, and merchants with consumers across Egypt and the wider MENA region. Founded in 2019 by Mahmoud Ibrahim and Ibrahim Mohamed, the platform lists more than 55,000 products and layers in flexible financing, delivery, and assembly services. Homzmart runs consumer web and mobile storefronts alongside merchant-facing "Sell With Us" and "Homzmart For Business" programs, and has raised roughly $40M in venture funding including a $15M Series A, with 500 Global among its backers. No public developer API program, SDK, or API documentation was found during enrichment; the company publishes a vulnerability-disclosure page and standard trust/policy pages.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homzmart.png
layout: provider
modified: '2026-07-19'
name: Homzmart
nav: Providers
network: true
overview: Homzmart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Furniture, Marketplace, and Home Goods.
random_paper: 0
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homzmart/refs/heads/main/screenshots/homzmart-2026-08-07T170311.png
security:
- kind: domain-security
  name: Homzmart Domain Security
  slug: homzmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Homzmart Vulnerability Disclosure
  slug: homzmart-vulnerability-disclosure
  summary_line: Hackerone
slug: homzmart
tags:
- Company
- E-Commerce
- Furniture
- Marketplace
- Home Goods
- Retail
- MENA
- Egypt
website: https://homzmart.com
---
