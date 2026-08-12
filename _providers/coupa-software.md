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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Coupa Core API is a UTF-8, RESTful interface (XML and JSON) for creating, updating, and acting on individual records within a Coupa instance — including purchase orders, requisitions, invoices, su
  name: Coupa Core API
  slug: coupa-core-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coupa-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coupa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api
- group: docs
  title: ''
  type: APIReference
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources
- group: start
  title: ''
  type: GettingStarted
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api
- group: operate
  title: ''
  type: Support
  url: https://compass.coupa.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/coupa-software-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coupa-software-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coupa-software-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coupa-software-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc
- group: design
  title: ''
  type: Conformance
  url: conformance/coupa-software-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coupa-software-llms.txt
created: '2026-07-17'
description: Coupa Software is a business spend management (BSM) platform that unifies procurement, invoicing, expense management, payments, supplier management, sourcing, contract lifecycle management, and supply-chain design into a single cloud suite. The Coupa Core API is a RESTful, UTF-8 interface (XML and JSON) that lets integrators create, read, update, and take action on individual records — purchase orders, requisitions, invoices, suppliers, users, expenses, contracts, receipts and more — within a Coupa instance. Authentication is via OAuth 2.0 and OpenID Connect (OIDC); legacy API keys are deprecated. Coupa was acquired by Thoma Bravo in 2023 and serves large enterprises worldwide.
image: https://www.coupa.com/wp-content/themes/coupa/assets/images/coupa-logo.svg
layout: provider
modified: '2026-07-18'
name: Coupa Software
nav: Providers
network: true
overview: 'Coupa Software publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Spend Management, Invoicing, and Expenses.


  Coupa Software''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 9 more developer resources.'
random_paper: 64
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 21.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coupa-software/refs/heads/main/screenshots/coupa-software-2026-07-25T210511.png
security:
- kind: authentication
  name: Coupa Software Authentication
  slug: coupa-software-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Coupa Software Domain Security
  slug: coupa-software-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coupa-software
tags:
- Company
- Procurement
- Spend Management
- Invoicing
- Expenses
- Payments
- Supply Chain
- Sourcing
- Contracts
- ERP
website: https://www.coupa.com
---
