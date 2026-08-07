---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Chargebee Agentic Access
  operation_count: 13
  slug: chargebee-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 8
apis:
- description: The Customers API from Chargebee — 2 operation(s) for customers.
  name: Chargebee Customers API
  slug: chargebee-customers-api
- description: The Invoices API from Chargebee — 2 operation(s) for invoices.
  name: Chargebee Invoices API
  slug: chargebee-invoices-api
- description: The Items API from Chargebee — 1 operation(s) for items.
  name: Chargebee Items API
  slug: chargebee-items-api
- description: The Orders API from Chargebee — 1 operation(s) for orders.
  name: Chargebee Orders API
  slug: chargebee-orders-api
- description: The Payments API from Chargebee — 1 operation(s) for payments.
  name: Chargebee Payments API
  slug: chargebee-payments-api
- description: The Plans API from Chargebee — 1 operation(s) for plans.
  name: Chargebee Plans API
  slug: chargebee-plans-api
- description: The Quotes API from Chargebee — 1 operation(s) for quotes.
  name: Chargebee Quotes API
  slug: chargebee-quotes-api
- description: The Subscriptions API from Chargebee — 2 operation(s) for subscriptions.
  name: Chargebee Subscriptions API
  slug: chargebee-subscriptions-api
artifact_total: 14
asyncapis:
- description: AsyncAPI description of Chargebee's webhook (event) surface. When a notable change occurs on a Chargebee site (customer created, subscription cancelled, invoice generated, payment failed, etc.) Charge
  name: Chargebee Webhooks
  slug: chargebee-asyncapi
collections:
- collection_type: open
  name: Chargebee API v2
  slug: open-chargebee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chargebee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chargebee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chargebee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chargebee
- group: company
  title: ''
  type: Website
  url: https://www.chargebee.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.chargebee.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.chargebee.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chargebee.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.chargebee.com/trial-signup/
- group: start
  title: ''
  type: Login
  url: https://app.chargebee.com/login
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.chargebee.com/docs/api/auth
- group: operate
  title: ''
  type: RateLimits
  url: https://apidocs.chargebee.com/docs/api/api-rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chargebee.com
- group: operate
  title: ''
  type: Support
  url: https://support.chargebee.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargebee
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/chargebee/openapi
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/chargebee/chargebee-node
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/chargebee/chargebee-python
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/chargebee/chargebee-php
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/chargebee/chargebee-java
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/chargebee/chargebee-ruby
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/chargebee/chargebee-go
- group: build
  title: ''
  type: .NET SDK
  url: https://github.com/chargebee/chargebee-dotnet
- group: company
  title: ''
  type: Blog
  url: https://www.chargebee.com/blog/feed/
created: '2026-05-11'
description: Chargebee is a subscription billing and revenue management platform that enables SaaS and subscription businesses to automate recurring billing, invoicing, payments, dunning, and revenue recognition. The Chargebee REST API v2 provides programmatic access to subscriptions, customers, invoices, payments, plans, addons, coupons, and usage metering, with HTTP Basic Auth using API keys scoped to each Chargebee site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargebee.png
layout: provider
modified: '2026-05-30'
name: Chargebee
nav: Providers
network: true
overview: 'Chargebee publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Invoices API, Items API, and 5 more. Tagged areas include Billing, Subscriptions, Recurring Billing, Revenue, and Payments.


  The Chargebee catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chargebee''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
random_paper: 14
rules:
- name: Chargebee API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: chargebee-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 66.7
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 21.1
  previous_composite: 42.0
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
    score: 18.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chargebee/refs/heads/main/screenshots/chargebee-2026-06-20T174220.png
security:
- kind: authentication
  name: Chargebee Authentication
  slug: chargebee-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chargebee Domain Security
  slug: chargebee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargebee
tags:
- Billing
- Subscriptions
- Recurring Billing
- Revenue
- Payments
- SaaS
website: https://www.chargebee.com
---
