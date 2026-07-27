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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 49.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Credit underwriting and risk scoring for partner card issuance.
  name: alt.bank Underwriting API
  slug: altbank-underwriting-api
artifact_total: 5
asyncapis:
- description: ''
  name: Altbank Guard Webhooks
  slug: altbank-guard-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://altbank.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.altbank.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.altbank.ai/docs/guard-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.altbank.ai/docs/guard-api
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/altbank-guard-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/altbank-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/altbank-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/altbank-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/altbank-guard-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/altbank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/altbank-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altbank-domain-security.yml
created: '2026-07-17'
description: alt.bank is a Brazilian fintech offering a turnkey credit-card platform that lets partners launch their own prepaid and postpaid credit cards in Brazil without holding a banking license. The company provides white-label card issuance, Visa BIN sponsorship, digital onboarding with KYC/AML, and fraud/chargeback management. Its developer surface centers on GUARD, a credit-underwriting and risk-scoring API that scores applicants (by CPF) against traditional and alternative data and returns a risk band and a suggested initial credit line asynchronously via partner callback, alongside the CLIMB limit-management system and the Pix Crédito product. Founded in 2018 and backed by Union Square Ventures, Anthemis, and others, alt.bank targets the underbanked across Brazil and Latin America.
image: https://altbank.ai/wp-content/uploads/2020/08/cropped-alt.bank-logo-square-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: altbank-mcp.yml
  slug: altbank-mcpyml
modified: '2026-07-17'
name: alt.bank
nav: Providers
network: true
overview: 'alt.bank publishes 1 API on the [APIs.io](https://apis.io/) network: Underwriting API. Tagged areas include Company, Fintech, Banking, Credit Cards, and Card Issuing.


  The alt.bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  alt.bank''s developer surface includes documentation, API reference, authentication, sandbox, and 9 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 69.0
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 36.9
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altbank/refs/heads/main/screenshots/altbank-2026-07-25T195815.png
security:
- kind: authentication
  name: Altbank Authentication
  slug: altbank-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Altbank Domain Security
  slug: altbank-domain-security
  summary_line: TLSv1.3
slug: altbank
tags:
- Company
- Fintech
- Banking
- Credit Cards
- Card Issuing
- Underwriting
- Payments
- Brazil
- KYC
website: https://altbank.ai
---
