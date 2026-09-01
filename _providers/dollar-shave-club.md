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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dollar-shave-club-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dollar-shave-club-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.dollarshaveclub.com
created: '2026-07-17'
description: Dollar Shave Club is a direct-to-consumer men's grooming brand founded in 2011 and best known for its subscription razor and blade service that ships razors, blades, shave butter, and personal-care products to members on a recurring schedule. Acquired by Unilever in 2016 and later sold to Nexus Capital Management in 2023, the company sells online through its storefront at dollarshaveclub.com. Its e-commerce experience runs on Shopify; the storefront host exposes Shopify Customer Account OAuth2/OIDC discovery documents (including Shopify's customer-account-api and customer-account-mcp-api scopes) but Dollar Shave Club publishes no first-party public developer API, SDKs, or API documentation of its own. It was added to the API Evangelist network as a portfolio-lead stub of a16z, Cowboy Ventures, Dragoneer, and Forerunner Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dollar-shave-club.png
layout: provider
modified: '2026-07-18'
name: Dollar Shave Club
nav: Providers
network: true
overview: Dollar Shave Club is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Subscription, and Direct to Consumer.
random_paper: 5
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dollar-shave-club/refs/heads/main/screenshots/dollar-shave-club-2026-08-07T164507.png
security:
- kind: domain-security
  name: Dollar Shave Club Domain Security
  slug: dollar-shave-club-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dollar-shave-club
tags:
- Company
- Consumer
- E-Commerce
- Subscription
- Direct to Consumer
- Retail
- Grooming
- Personal Care
website: https://www.dollarshaveclub.com
---
