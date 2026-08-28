---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Reloadly Agentic Access
  operation_count: 17
  slug: reloadly-agentic-access
  summary_line: 17 operations · 4 acting
api_count: 8
apis:
- description: Obtain OAuth 2.0 access tokens for API authorization.
  name: Reloadly Authentication API
  slug: reloadly-authentication-api
- description: Check your Reloadly account balance.
  name: Reloadly Balance API
  slug: reloadly-balance-api
- description: Retrieve discount rates available on gift card products.
  name: Reloadly Discounts API
  slug: reloadly-discounts-api
- description: Browse mobile network operators and their coverage.
  name: Reloadly Operators API
  slug: reloadly-operators-api
- description: Place and manage gift card orders.
  name: Reloadly Orders API
  slug: reloadly-orders-api
- description: Browse and search the gift card product catalog.
  name: Reloadly Products API
  slug: reloadly-products-api
- description: Send airtime top-ups to mobile phones worldwide.
  name: Reloadly Top-Ups API
  slug: reloadly-top-ups-api
- description: List and retrieve top-up transaction history.
  name: Reloadly Transactions API
  slug: reloadly-transactions-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reloadly Airtime API
  slug: open-reloadly-airtime
- collection_type: open
  name: Reloadly Airtime Authentication API
  slug: open-reloadly-authentication-api
- collection_type: open
  name: Reloadly Airtime Authentication Balance API
  slug: open-reloadly-balance-api
- collection_type: open
  name: Reloadly Airtime Authentication Discounts API
  slug: open-reloadly-discounts-api
- collection_type: open
  name: Reloadly Gift Cards API
  slug: open-reloadly-gift-cards
- collection_type: open
  name: Reloadly Airtime Authentication Operators API
  slug: open-reloadly-operators-api
- collection_type: open
  name: Reloadly Airtime Authentication Orders API
  slug: open-reloadly-orders-api
- collection_type: open
  name: Reloadly Airtime Authentication Products API
  slug: open-reloadly-products-api
- collection_type: open
  name: Reloadly Airtime Authentication Top-Ups API
  slug: open-reloadly-top-ups-api
- collection_type: open
  name: Reloadly Airtime Authentication Transactions API
  slug: open-reloadly-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reloadly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reloadly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reloadly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.reloadly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reloadly.com
- group: auth
  title: ''
  type: Authentication
  url: https://auth.reloadly.com/oauth/token
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.reloadly.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reloadly
- group: operate
  title: ''
  type: Support
  url: https://support.reloadly.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reloadly.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.reloadly.com/register
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reloadly
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/reloadly
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.reloadly.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.reloadly.com/blog/feed/
created: '2025-02-08'
description: Reloadly is a global digital rewards and payments platform providing APIs for sending digital gift cards, airtime top-ups, and data bundles worldwide. The platform connects businesses to 3,000+ gift card brands across 14,000+ products in 140+ countries and 800+ mobile operators in 170+ countries. Reloadly's REST APIs use OAuth 2.0 client credentials authentication with separate sandbox and production environments.
examples:
- key_count: 2
  name: Reloadly List Products Example
  slug: reloadly-list-products-example
- key_count: 2
  name: Reloadly Place Order Example
  slug: reloadly-place-order-example
- key_count: 2
  name: Reloadly Send Topup Example
  slug: reloadly-send-topup-example
finops:
- name: Reloadly Finops
  service_category: API
  slug: reloadly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reloadly.png
json_schemas:
- name: Reloadly Gift Card Order
  property_count: 11
  slug: reloadly-order
- name: Reloadly Gift Card Product
  property_count: 18
  slug: reloadly-product
json_structures:
- name: Reloadly Product Structure
  property_count: 0
  slug: reloadly-product-structure
jsonld:
- class_count: 9
  name: Reloadly Context
  property_count: 17
  slug: reloadly-context
layout: provider
modified: '2026-05-19'
name: Reloadly
nav: Providers
network: true
overview: 'Reloadly publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balance API, Discounts API, and 5 more. Tagged areas include Gift Cards, Payments, Airtime, Mobile Top-Up, and Rewards.


  The Reloadly catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Reloadly''s developer surface includes authentication, documentation, support, pricing, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Reloadly Plans Pricing
  plan_count: 3
  slug: reloadly-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Reloadly Rate Limits
  slug: reloadly-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Reloadly API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: reloadly-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Reloadly API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: reloadly-rules
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 65.9
    developer_ergonomics: 13.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reloadly/refs/heads/main/screenshots/reloadly-2026-06-20T192834.png
security:
- kind: authentication
  name: Reloadly Authentication
  slug: reloadly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reloadly Domain Security
  slug: reloadly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reloadly
tags:
- Gift Cards
- Payments
- Airtime
- Mobile Top-Up
- Rewards
- Incentives
website: https://www.reloadly.com
---
