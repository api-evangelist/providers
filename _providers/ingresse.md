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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Versioned REST API (v1 and v2) for event ticketing — events, tickets, checkout/payments, users, and access control — authenticated with an individually issued API key passed as the `apikey` query para
  name: Ingresse API
  slug: ingresse-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://ingresse.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ingresse.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ingresse.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ingresse.com/reference
- group: operate
  title: ''
  type: Support
  url: https://developer.ingresse.com/discuss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ingresse
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ingresse-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ingresse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ingresse-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ingresse-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ingresse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ingresse-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ingresse-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ingresse-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ingresse-domain-security.yml
created: '2026-07-17'
description: Ingresse is a Brazilian ticketing-as-a-service (TaaS) platform that powers event ticket sales, access control, and the attendee experience for organizers and partners. Its public developer platform lets integrators build tools and services on top of Ingresse — creating events, selling and validating tickets, managing users, and handling payments — through a versioned REST API (v1 and v2) authenticated with an individually issued API key. Ingresse publishes first-party SDKs for JavaScript/Node, Android, iOS, and PHP, plus message-queue libraries, and hosts its reference documentation on a ReadMe developer portal. Ingresse is backed by 500 Global.
image: https://ingresse.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Ingresse
nav: Providers
network: true
overview: 'Ingresse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Event, Ticketing as a Service, and Payments.


  Ingresse''s developer surface includes documentation, API reference, support, authentication, sandbox, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 41.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ingresse/refs/heads/main/screenshots/ingresse-2026-07-25T222431.png
security:
- kind: authentication
  name: Ingresse Authentication
  slug: ingresse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ingresse Domain Security
  slug: ingresse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ingresse
tags:
- Company
- Ticketing
- Event
- Ticketing as a Service
- Payments
- Entertainment
- Event Management
- Brazil
- SDK
website: https://ingresse.com
---
