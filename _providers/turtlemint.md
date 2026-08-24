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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST APIs for embedded insurance distribution — lookups/master data, quotes, proposals and payments — built to OpenAPI 3.0 (Swagger), secured with Bearer access tokens, and testable in a sandbox "Deve
  name: Turtlefin OneAPI
  slug: turtlefin-oneapi
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.turtlemint.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.turtlefin.com/dev-portal/login
- group: docs
  title: ''
  type: Documentation
  url: https://developers.turtlefin.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.turtlefin.com/dev-portal/login
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.turtlefin.com/docs/quickstart
- group: start
  title: ''
  type: Login
  url: https://app.turtlefin.com/dev-portal/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@turtlefin.com
- group: company
  title: ''
  type: Blog
  url: https://www.turtlefin.com/blog-post
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.turtlefin.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.turtlefin.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/turtlemint-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/turtlemint-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/turtlemint-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/turtlemint-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/turtlemint-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/turtlemint-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/turtlemint-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/turtlemint-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/turtlemint-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/turtlemint-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turtlemint-domain-security.yml
created: '2026-07-17'
description: 'Turtlemint is an Indian insurtech that sells and services insurance (health, motor, life) and financial products to consumers and, through its advisor platform TurtlemintPro, to a large network of point-of-sale agents. Its B2B arm, Turtlefin, productizes that stack as embedded-insurance technology: the OneAPI platform exposes REST APIs (OpenAPI 3.0 / Swagger) for lookups/master data, quotes, proposals and payments so that banks, fintechs and e-commerce partners can embed insurance purchase into their own journeys, alongside the white-labeled DigitalCore platform and a sales-certification LMS.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turtlemint.png
layout: provider
mcp_servers:
- description: ''
  name: Turtlemint MCP Server
  slug: turtlemint-mcp-server
modified: '2026-07-21'
name: Turtlemint
nav: Providers
network: true
overview: 'Turtlemint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Insurance, Embedded Insurance, and Insurance Distribution.


  Turtlemint''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 14 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 53.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 30.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Turtlemint Authentication
  slug: turtlemint-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Turtlemint Domain Security
  slug: turtlemint-domain-security
  summary_line: TLSv1.2 · DMARC
slug: turtlemint
tags:
- Company
- Insurtech
- Insurance
- Embedded Insurance
- Insurance Distribution
- Fintech
- Payments
website: https://www.turtlemint.com/
---
