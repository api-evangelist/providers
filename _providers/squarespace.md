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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Squarespace Agentic Access
  operation_count: 30
  slug: squarespace-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 7
apis:
- description: The Squarespace Orders API provides access to order history for a Squarespace merchant site, supporting both one-time purchases and subscription orders. Developers can retrieve, create, and manage ord
  name: Squarespace Orders API
  slug: squarespace-orders-api
- description: The Squarespace Products API allows developers to manage the product catalog of a Squarespace merchant site. It supports physical products, service products, gift cards, and digital downloads, along w
  name: Squarespace Products API
  slug: squarespace-products-api
- description: The Squarespace Inventory API enables developers to retrieve and update inventory quantities for product variants on a Squarespace merchant site. It supports bulk inventory queries and individual vari
  name: Squarespace Inventory API
  slug: squarespace-inventory-api
- description: The Squarespace Profiles API allows reading customer profiles, mailing list subscribers, and donors for a Squarespace site. It supports filtering by profile type and retrieving individual profile deta
  name: Squarespace Profiles API
  slug: squarespace-profiles-api
- description: The Squarespace Transactions API provides access to financial transaction records for a Squarespace merchant site. Developers can retrieve transaction history, including payment amounts, fees, and ass
  name: Squarespace Transactions API
  slug: squarespace-transactions-api
- description: The Squarespace Webhook Subscriptions API allows developers to manage webhook endpoint subscriptions for a merchant site. It supports creating, listing, updating, and deleting subscriptions that trigg
  name: Squarespace Webhook Subscriptions API
  slug: squarespace-webhook-subscriptions-api
- description: Basic site information and metadata
  name: Squarespace Site API
  slug: squarespace-site-api
artifact_total: 33
asyncapis:
- description: The Squarespace webhook system delivers real-time event notifications to registered endpoint URLs when commerce activity occurs on a merchant site. Supported events include order creation, order updat
  name: Squarespace Webhook Events
  slug: squarespace-webhooks-asyncapi
collections:
- collection_type: open
  name: Squarespace Commerce API
  slug: open-squarespace-commerce-api
- collection_type: open
  name: Squarespace Inventory API
  slug: open-squarespace-inventory-api
- collection_type: open
  name: Squarespace Orders API
  slug: open-squarespace-orders-api
- collection_type: open
  name: Squarespace Products API
  slug: open-squarespace-products-api
- collection_type: open
  name: Squarespace Profiles API
  slug: open-squarespace-profiles-api
- collection_type: open
  name: Squarespace Transactions API
  slug: open-squarespace-transactions-api
- collection_type: open
  name: Squarespace Webhook Subscriptions API
  slug: open-squarespace-webhook-subscriptions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/squarespace-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/squarespace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squarespace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/squarespace-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squarespace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/squarespace
- group: company
  title: ''
  type: Website
  url: https://www.squarespace.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.squarespace.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.squarespace.com/commerce-apis/overview
- group: auth
  title: ''
  type: APIKeys
  url: https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.squarespace.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.squarespace.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.squarespace.com
- group: company
  title: ''
  type: Blog
  url: https://www.squarespace.com/blog
created: '2026-05-02'
description: Squarespace is an all-in-one website building and e-commerce platform that enables individuals and businesses to create, manage, and scale their online presence. Squarespace provides a suite of Commerce APIs for developers to build integrations managing products, orders, inventory, customer profiles, transactions, and webhook notifications. All APIs use HTTPS REST conventions with API key or OAuth authentication.
examples:
- key_count: 4
  name: Squarespace List Orders Example
  slug: squarespace-list-orders-example
- key_count: 4
  name: Squarespace List Products Example
  slug: squarespace-list-products-example
finops:
- name: Squarespace Finops
  service_category: E-Commerce
  slug: squarespace-finops
image: https://static1.squarespace.com/static/ta/5134cbefe4b0c6fb04df8065/10007/assets/logomark.svg
json_schemas:
- name: Squarespace Order
  property_count: 17
  slug: squarespace-order
- name: Squarespace Product
  property_count: 13
  slug: squarespace-product
- name: Squarespace Webhook Notification
  property_count: 6
  slug: squarespace-webhook-notification
json_structures:
- name: Squarespace Order Structure
  property_count: 0
  slug: squarespace-order-structure
- name: Squarespace Product Structure
  property_count: 0
  slug: squarespace-product-structure
jsonld:
- class_count: 0
  name: Squarespace Context
  property_count: 12
  slug: squarespace-context
layout: provider
modified: '2026-05-19'
name: Squarespace
nav: Providers
network: true
overview: 'Squarespace publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Products API, Inventory API, and 4 more. Tagged areas include Commerce, E-Commerce, Marketing, Payments, and Retail.


  The Squarespace catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Squarespace''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Squarespace Plans Pricing
  plan_count: 1
  slug: squarespace-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Squarespace Rate Limits
  slug: squarespace-rate-limits
rules:
- name: Squarespace API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: squarespace-asyncapi-spectral-rules
- name: Squarespace API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: squarespace-jsonschema-spectral-rules
- name: Squarespace API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: squarespace-rules
score:
  band: developing
  composite: 47.1
  delta: -5.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 77.6
    developer_ergonomics: 30.4
    discoverability: 57.4
    governance: 41.7
    operational_transparency: 28.9
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/squarespace/refs/heads/main/screenshots/squarespace-2026-06-20T194430.png
security:
- kind: authentication
  name: Squarespace Authentication
  slug: squarespace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Squarespace Domain Security
  slug: squarespace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Squarespace Vulnerability Disclosure
  slug: squarespace-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: squarespace
tags:
- Commerce
- E-Commerce
- Marketing
- Payments
- Retail
- Website Builder
- Webhooks
website: https://www.squarespace.com
---
