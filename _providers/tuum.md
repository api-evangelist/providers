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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-05'
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
random_paper: 18
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 33.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tuum/refs/heads/main/screenshots/tuum-2026-09-02T164559.png
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
- Financial-Services
website: https://tuum.com/
---
