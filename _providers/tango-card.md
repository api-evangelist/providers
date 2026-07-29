---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Tango Card Agentic Access
  operation_count: 46
  slug: tango-card-agentic-access
  summary_line: 46 operations · 20 acting
api_count: 13
apis:
- description: Manage customer accounts and balances
  name: Tango Card Accounts API
  slug: tango-card-accounts-api
- description: Reward brand category information
  name: Tango Card Brand Categories API
  slug: tango-card-brand-categories-api
- description: Reward catalog access
  name: Tango Card Catalog API
  slug: tango-card-catalog-api
- description: Choice product management
  name: Tango Card Choice Products API
  slug: tango-card-choice-products-api
- description: Supported reward countries
  name: Tango Card Countries & Currencies API
  slug: tango-card-countries-currencies-api
- description: Credential type definitions
  name: Tango Card Credential Types API
  slug: tango-card-credential-types-api
- description: Manage platform customers
  name: Tango Card Customers API
  slug: tango-card-customers-api
- description: Email and digital template management
  name: Tango Card Digital Templates API
  slug: tango-card-digital-templates-api
- description: Currency exchange rates
  name: Tango Card Exchange Rates API
  slug: tango-card-exchange-rates-api
- description: Credit card deposits, registrations, and fund transfers
  name: Tango Card Fund Management API
  slug: tango-card-fund-management-api
- description: Order line item management and actions
  name: Tango Card Line Items API
  slug: tango-card-line-items-api
- description: Account low balance alert configuration
  name: Tango Card Low Balance Alerts API
  slug: tango-card-low-balance-alerts-api
- description: Reward order creation and management
  name: Tango Card Orders API
  slug: tango-card-orders-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tango-card-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tango-card-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tango-card-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tango-card-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.tangocard.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tangocard.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tangocard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tango-card-inc
- group: company
  title: ''
  type: Blog
  url: https://www.tangocard.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tangocard.com/solutions/raas-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tango.us/
- group: other
  title: ''
  type: X
  url: https://x.com/tangocard
- group: commercial
  title: ''
  type: Plans
  url: plans/tango-card-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tango-card-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tango-card-finops.yml
created: '2026-06-13'
description: Tango Card is a digital rewards and gift card distribution platform providing a REST API (Rewards as a Service, RaaS) for sending gift cards, managing reward orders, tracking delivery, and accessing a global catalog of 3,100+ reward options including e-gift cards, prepaid cards, and charitable donations.
examples:
- key_count: 13
  name: Catalog Item Example
  slug: catalog-item-example
- key_count: 3
  name: Create Account Request
  slug: create-account-request
- key_count: 2
  name: Create Customer Request
  slug: create-customer-request
- key_count: 9
  name: Create Order Request
  slug: create-order-request
- key_count: 13
  name: Create Order Response
  slug: create-order-response
finops:
- name: Tango Card Finops
  service_category: ''
  slug: tango-card-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tango-card.png
json_schemas:
- name: Tango RaaS Catalog Item
  property_count: 13
  slug: tango-raas-catalog-item
- name: Tango RaaS Order
  property_count: 13
  slug: tango-raas-order
jsonld:
- class_count: 11
  name: Tango Raas Context
  property_count: 34
  slug: tango-raas-context
layout: provider
modified: '2026-06-13'
name: Tango Card
nav: Providers
network: true
overview: 'Tango Card publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Brand Categories API, Catalog API, and 10 more. Tagged areas include Gift Cards, Rewards, Incentives, Digital Rewards, and Prepaid Cards.


  The Tango Card catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tango Card''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Tango Card Plans Pricing
  plan_count: 1
  slug: tango-card-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 2
  name: Tango Card Rate Limits
  slug: tango-card-rate-limits
rules:
- name: Tango Card API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tango-card-jsonschema-spectral-rules
scopes:
- name: Tango Card Scopes
  scope_count: 1
  slug: tango-card-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 48.8
  delta: -5.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tango-card/refs/heads/main/screenshots/tango-card-2026-06-20T194915.png
security:
- kind: authentication
  name: Tango Card Authentication
  slug: tango-card-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Tango Card Domain Security
  slug: tango-card-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tango-card
tags:
- Gift Cards
- Rewards
- Incentives
- Digital Rewards
- Prepaid Cards
- Payments
website: https://www.tangocard.com
---
