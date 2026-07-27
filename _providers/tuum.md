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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 27.9
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Tuum's modular, API-first core banking platform. Per-module REST APIs (auth, person, employee, account, payment, card, loan, deposit, data-import, notification) versioned independently in the URL path
  name: Tuum Core Banking API
  slug: tuum-core-banking-api
artifact_total: 4
asyncapis:
- description: ''
  name: Tuum Notification Webhooks
  slug: tuum-notification-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tuum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tuum.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tuumplatform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tuum.com/tuum-developer-docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tuumplatform.com/explore
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tuum.com/tuum-developer-docs/getting-started/get-started
- group: company
  title: ''
  type: Blog
  url: https://tuum.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://tuum.com/get-in-touch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tuumplatform.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tuum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tuum-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tuum-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tuum-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tuum-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tuum-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tuum-notification-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tuum-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tuum-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tuum-llms.txt
created: '2026-07-17'
description: Tuum is a cloud-native, modular core banking platform that lets banks, fintechs, and other financial institutions launch and modernise financial products without legacy constraints. Its API-first platform is organised into independent modules — accounts, payments, cards, lending, deposits, and more — covering Banking-as-a-Service, payments processing, lending, and Islamic banking. Developers integrate over per-module REST APIs (auth-api, person-api, account-api, payment-api, card-api, loan-api, deposit-api, notification-api), authenticating with a JWT presented in the x-auth-token header (with a standards OAuth 2.0 authorization server also available), and receive near-real-time events via the Notification API's webhooks. Founded in Estonia (formerly Modularbank), Tuum is backed by investors including Speedinvest.
image: https://tuum.com/wp-content/uploads/2023/07/img-coverTuum.png
layout: provider
modified: '2026-07-21'
name: Tuum
nav: Providers
network: true
overview: 'Tuum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Core Banking, Banking as a Service, Payments, and Lending.


  The Tuum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tuum''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 12 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 22.6
    developer_ergonomics: 58.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 33.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 45.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tuum Authentication
  slug: tuum-authentication
  summary_line: http/oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Tuum Domain Security
  slug: tuum-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tuum
tags:
- Company
- Core Banking
- Banking as a Service
- Payments
- Lending
- Cards
- Fintech
- Financial Services
- API
website: https://tuum.com/
---
