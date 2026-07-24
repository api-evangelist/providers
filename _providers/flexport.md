---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
- acting_count: 11
  human_in_the_loop: 0
  name: Flexport Agentic Access
  operation_count: 30
  slug: flexport-agentic-access
  summary_line: 30 operations · 11 acting
api_count: 10
apis:
- description: Flexport REST API exposes shipment status, purchase orders, bookings, customs entries, invoices, products, network entities, ports, documents, and webhooks. Uses JSON request/response with v2 endpoint
  name: Flexport REST API
  slug: flexport-rest-api
- description: The Bookings API from Flexport — 4 operation(s) for bookings.
  name: Flexport Bookings API
  slug: flexport-bookings-api
- description: The Customs API from Flexport — 2 operation(s) for customs.
  name: Flexport Customs API
  slug: flexport-customs-api
- description: The Documents API from Flexport — 1 operation(s) for documents.
  name: Flexport Documents API
  slug: flexport-documents-api
- description: The Invoices API from Flexport — 1 operation(s) for invoices.
  name: Flexport Invoices API
  slug: flexport-invoices-api
- description: The Network API from Flexport — 3 operation(s) for network.
  name: Flexport Network API
  slug: flexport-network-api
- description: The Products API from Flexport — 1 operation(s) for products.
  name: Flexport Products API
  slug: flexport-products-api
- description: The PurchaseOrders API from Flexport — 2 operation(s) for purchaseorders.
  name: Flexport PurchaseOrders API
  slug: flexport-purchaseorders-api
- description: The Shipments API from Flexport — 6 operation(s) for shipments.
  name: Flexport Shipments API
  slug: flexport-shipments-api
- description: The Webhooks API from Flexport — 1 operation(s) for webhooks.
  name: Flexport Webhooks API
  slug: flexport-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: Flexport REST API
  slug: open-flexport
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flexport-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flexport-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flexport-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flexport-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flexport
- group: company
  title: ''
  type: Website
  url: https://www.flexport.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.flexport.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/flexport-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flexport-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flexport-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.flexport.com/blog
created: '2026-05-08'
description: Flexport is a digital freight forwarder and logistics platform that orchestrates global ocean, air, ground, and customs operations for shippers.
finops:
- name: Flexport Finops
  service_category: Logistics
  slug: flexport-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flexport.png
layout: provider
modified: '2026-05-08'
name: Flexport
nav: Providers
network: true
overview: 'Flexport publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Customs API, Documents API, and 6 more. Tagged areas include Logistics, Freight, Supply Chain, Customs, and B2B.


  Flexport''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Flexport Plans Pricing
  plan_count: 1
  slug: flexport-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Flexport Rate Limits
  slug: flexport-rate-limits
scopes:
- name: Flexport Scopes
  scope_count: 22
  slug: flexport-scopes
  summary_line: 22 scopes · clientCredentials
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 47.8
    developer_ergonomics: 21.7
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 31.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flexport/refs/heads/main/screenshots/flexport-2026-06-20T181310.png
security:
- kind: authentication
  name: Flexport Authentication
  slug: flexport-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Flexport Domain Security
  slug: flexport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flexport Vulnerability Disclosure
  slug: flexport-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: flexport
tags:
- Logistics
- Freight
- Supply Chain
- Customs
- B2B
website: https://www.flexport.com/
---
