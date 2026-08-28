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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Qover''s REST API for embedded insurance: a Claims API (file, retrieve, track status history, and download claim reports), a Policy API (manage policies and dynamically add/remove risk items), and a Do'
  name: Qover Embedded Insurance API
  slug: qover-embedded-insurance-api
artifact_total: 6
asyncapis:
- description: ''
  name: Qover Webhooks
  slug: qover-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/qover-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qover-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qover.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qover.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qover.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.qover.com/api-access
- group: build
  title: ''
  type: Postman
  url: https://docs.qover.com/
- group: company
  title: ''
  type: Blog
  url: https://qover.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://qover.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qover.com/api-access
- group: operate
  title: ''
  type: Support
  url: https://qover.com/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://storage.googleapis.com/qover-assets/documents/terms/Terms-of-use_EN.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://storage.googleapis.com/qover-assets/documents/policies/Privacy%20Policy_EN_v.04_2026.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qover.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.qover.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qover-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qover-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qover-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qover-llms.txt
created: '2026-07-17'
description: Qover is a Brussels-based insurtech providing an API-first embedded insurance orchestration platform used across 32 European countries. Its modular platform lets brands, fintechs and insurers configure and distribute insurance products (travel, mobility, bike, purchase protection, accident, property) and run the full lifecycle from policy configuration and issuance through AI-assisted claims and multilingual customer care. Qover exposes REST APIs - a Claims API, a Policy API and a Document Asset Management API - secured with API keys, with a sandbox environment, configurable webhooks for claim status changes, and per-partner product configuration. Founded in 2016, Qover reports serving 440+ brands and insurers covering millions of people, and is an ISO-certified company with a Vanta-hosted trust center.
image: https://qover.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Qover MCP Server
  slug: qover-mcp-server
modified: '2026-07-20'
name: Qover
nav: Providers
network: true
overview: 'Qover publishes 1 API on the [APIs.io](https://apis.io/) network: Embedded Insurance API. Tagged areas include Company, Insurtech, Insurance, Embedded Insurance, and Claims.


  The Qover catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qover''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 12 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 50.5
  delta: 2.8
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 47.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qover/refs/heads/main/screenshots/qover-2026-08-17T081419.png
security:
- kind: authentication
  name: Qover Authentication
  slug: qover-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qover Domain Security
  slug: qover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qover Trust Center
  slug: qover-trust-center
  summary_line: ISO 27001
slug: qover
tags:
- Company
- Insurtech
- Insurance
- Embedded Insurance
- Claims
- Policy
- Fintech
- Belgium
website: https://docs.qover.com/
---
