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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-17'
api_count: 9
apis:
- description: The Application API from Romit — 1 operation(s) for application.
  name: Romit Application API
  slug: romit-application-api
- description: The Banking API from Romit — 8 operation(s) for banking.
  name: Romit Banking API
  slug: romit-banking-api
- description: The Identity API from Romit — 9 operation(s) for identity.
  name: Romit Identity API
  slug: romit-identity-api
- description: The Invoice API from Romit — 3 operation(s) for invoice.
  name: Romit Invoice API
  slug: romit-invoice-api
- description: The OAuth API from Romit — 2 operation(s) for oauth.
  name: Romit OAuth API
  slug: romit-oauth-api
- description: The Plan API from Romit — 3 operation(s) for plan.
  name: Romit Plan API
  slug: romit-plan-api
- description: The Subscription API from Romit — 3 operation(s) for subscription.
  name: Romit Subscription API
  slug: romit-subscription-api
- description: The Transfer API from Romit — 5 operation(s) for transfer.
  name: Romit Transfer API
  slug: romit-transfer-api
- description: The User API from Romit — 2 operation(s) for user.
  name: Romit User API
  slug: romit-user-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Romit Application API
  slug: open-romit-application-api
- collection_type: open
  name: Romit Application Banking API
  slug: open-romit-banking-api
- collection_type: open
  name: Romit Application Identity API
  slug: open-romit-identity-api
- collection_type: open
  name: Romit Application Invoice API
  slug: open-romit-invoice-api
- collection_type: open
  name: Romit Application OAuth API
  slug: open-romit-oauth-api
- collection_type: open
  name: Romit Application Plan API
  slug: open-romit-plan-api
- collection_type: open
  name: Romit Application Subscription API
  slug: open-romit-subscription-api
- collection_type: open
  name: Romit Application Transfer API
  slug: open-romit-transfer-api
- collection_type: open
  name: Romit Application User API
  slug: open-romit-user-api
common:
- group: company
  title: ''
  type: Website
  url: https://romit.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/romit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/romit-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/romit-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/romit-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/romit-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/romit-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/romit-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/romit-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/romit-domain-security.yml
created: '2026-07-17'
description: Romit was a bank-agnostic digital wallet and payment-gateway platform for the card-not-present merchant-acquiring industry, built by a team of ex-Robocoin (bitcoin ATM) founders and backed by the 500 Global (500 Startups) accelerator. The Romit Merchant Suite let merchants stop chargebacks, reduce fraud and resolve disputes, while its consumer wallet let customers securely store payment methods, view transactions and communicate with merchants. Its OAuth2 REST API (api.romit.io/v1) exposed Banking (cards + linked bank accounts), Identity/KYC, Transfer (authorize/capture/refund/void money movement), Subscription, Plan and Invoice resources. Romit (romit.io) has since ceased operations; this profile captures the API surface derived from the surviving public evidence.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/romit.png
layout: provider
modified: '2026-07-21'
name: Romit
nav: Providers
network: true
overview: 'Romit publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Application API, Banking API, Identity API, and 6 more. Tagged areas include Company, Payments, Fintech, Digital Wallet, and Payment Gateway.


  Romit''s developer surface includes authentication, sandbox, and 8 more developer resources.'
random_paper: 108
scopes:
- name: Romit Scopes
  scope_count: 15
  slug: romit-scopes
  summary_line: 15 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 26.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.2
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 26.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Romit Authentication
  slug: romit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Romit Domain Security
  slug: romit-domain-security
  summary_line: no transport/DNS hardening detected
slug: romit
tags:
- Company
- Payments
- Fintech
- Digital Wallet
- Payment Gateway
- Merchant Services
- Chargebacks
- Fraud Prevention
- Invoicing
- Subscriptions
website: https://romit.io
---
