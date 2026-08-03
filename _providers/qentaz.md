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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API for generating collections (cobros), disbursing funds (dispersiones), managing teams and administered accounts, reconciliation and webhooks. Two-step bearer-token authentication; JSON over HT
  name: Trazo API
  slug: trazo-api
artifact_total: 5
asyncapis:
- description: Outbound webhook events Trazo delivers to a merchant-configured endpoint for collections (cobros / payment), disbursements (dispersiones / payout) and team (equipo) state changes. Trazo signs each del
  name: Trazo (Qentaz) Webhooks
  slug: qentaz-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.trazo.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qentaz.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qentaz.com/documentation/introduccion
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qentaz.com/documentation/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qentaz.com/documentation/autenticacion/token
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qentaz-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/qentaz-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qentaz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qentaz-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qentaz-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qentaz.com
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qentaz-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/qentaz-webhooks-asyncapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qentaz-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qentaz-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qentaz-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qentaz-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qentaz
- group: operate
  title: ''
  type: Support
  url: mailto:hola@trazo.co
- group: company
  title: ''
  type: Blog
  url: https://www.trazo.co/blog
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.trazo.co
- group: start
  title: ''
  type: Login
  url: https://dashboard.trazo.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trazo.co/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trazo.co/privacidad
created: '2026-07-17'
description: Qentaz (now operating under the brand Trazo) is a Colombian fintech providing collections, payments, disbursements, fraud control and reconciliation infrastructure for modern operations. Its REST API lets businesses generate charges (cobros), send payment links over WhatsApp, email or a hosted link, disburse funds to third parties (dispersiones), manage collector teams and administered (child) accounts, and reconcile cash and digital payments in real time. Authentication is a two-step bearer model (a static auth key exchanged for a short-lived access token), and webhooks push payment, payout and team events with a signed header. The API is versioned under /v1 and returns a custom JSON error envelope with Q-prefixed codes.
image: https://qentaz.com/logo-trazo.svg
layout: provider
modified: '2026-07-20'
name: Qentaz
nav: Providers
network: true
overview: 'Qentaz publishes 1 API on the [APIs.io](https://apis.io/) network: Trazo API. Tagged areas include Company, Payments, Collections, Disbursements, and Reconciliation.


  The Qentaz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qentaz''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 17 more developer resources.'
random_paper: 89
score:
  band: developing
  composite: 43.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.4
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 43.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Qentaz Authentication
  slug: qentaz-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Qentaz Domain Security
  slug: qentaz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Qentaz Trust Center
  slug: qentaz-trust-center
  summary_line: trust center published
slug: qentaz
tags:
- Company
- Payments
- Collections
- Disbursements
- Reconciliation
- Fintech
- Colombia
- Webhooks
- Fraud Prevention
- WhatsApp Payments
website: https://www.trazo.co
---
