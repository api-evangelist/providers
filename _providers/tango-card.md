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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Tango Card Agentic Access
  operation_count: 46
  slug: tango-card-agentic-access
  summary_line: 46 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Manage customer accounts and balances
  name: Tango Card Accounts API
  slug: tango-card-accounts-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Reward brand category information
  name: Tango Card Brand Categories API
  slug: tango-card-brand-categories-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Reward catalog access
  name: Tango Card Catalog API
  slug: tango-card-catalog-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Choice product management
  name: Tango Card Choice Products API
  slug: tango-card-choice-products-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Supported reward countries
  name: Tango Card Countries & Currencies API
  slug: tango-card-countries-currencies-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Credential type definitions
  name: Tango Card Credential Types API
  slug: tango-card-credential-types-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Manage platform customers
  name: Tango Card Customers API
  slug: tango-card-customers-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Email and digital template management
  name: Tango Card Digital Templates API
  slug: tango-card-digital-templates-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Currency exchange rates
  name: Tango Card Exchange Rates API
  slug: tango-card-exchange-rates-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Credit card deposits, registrations, and fund transfers
  name: Tango Card Fund Management API
  slug: tango-card-fund-management-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Order line item management and actions
  name: Tango Card Line Items API
  slug: tango-card-line-items-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Account low balance alert configuration
  name: Tango Card Low Balance Alerts API
  slug: tango-card-low-balance-alerts-api
- baseURL: https://api.tangocard.com/raas/v2
  baseurl_source: declared
  description: Reward order creation and management
  name: Tango Card Orders API
  slug: tango-card-orders-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tango RaaS Accounts API
  slug: open-tango-card-accounts-api
- collection_type: open
  name: Tango RaaS Accounts Brand Categories API
  slug: open-tango-card-brand-categories-api
- collection_type: open
  name: Tango RaaS Accounts Catalog API
  slug: open-tango-card-catalog-api
- collection_type: open
  name: Tango RaaS Accounts Choice Products API
  slug: open-tango-card-choice-products-api
- collection_type: open
  name: Tango RaaS Accounts Countries & Currencies API
  slug: open-tango-card-countries-currencies-api
- collection_type: open
  name: Tango RaaS Accounts Credential Types API
  slug: open-tango-card-credential-types-api
- collection_type: open
  name: Tango RaaS Accounts Customers API
  slug: open-tango-card-customers-api
- collection_type: open
  name: Tango RaaS Accounts Digital Templates API
  slug: open-tango-card-digital-templates-api
- collection_type: open
  name: Tango RaaS Accounts Exchange Rates API
  slug: open-tango-card-exchange-rates-api
- collection_type: open
  name: Tango RaaS Accounts Fund Management API
  slug: open-tango-card-fund-management-api
- collection_type: open
  name: Tango RaaS Accounts Line Items API
  slug: open-tango-card-line-items-api
- collection_type: open
  name: Tango RaaS Accounts Low Balance Alerts API
  slug: open-tango-card-low-balance-alerts-api
- collection_type: open
  name: Tango RaaS Accounts Orders API
  slug: open-tango-card-orders-api
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
random_paper: 5
rate_limits:
- limit_count: 2
  name: Tango Card Rate Limits
  slug: tango-card-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tango Card API Rules
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
  composite: 41.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.9
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 38.2
  previous_composite: 40.4
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
