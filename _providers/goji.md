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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 40.4
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'The Goji Platform API for private-markets investing: create and KYC/KYB investors, open and administer IF ISAs, move funds via investor and manager payment APIs, settle debt and equity investments, ma'
  name: Goji Platform API
  slug: goji-platform-api
artifact_total: 5
asyncapis:
- description: ''
  name: Goji Webhooks
  slug: goji-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goji-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.docs.goji.investments/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.goji.investments/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.goji.investments/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.goji.investments/
- group: company
  title: ''
  type: Website
  url: https://goji.investments
- group: start
  title: ''
  type: SignUp
  url: https://platform.goji.investments/investments/account/register
- group: operate
  title: ''
  type: Support
  url: https://goji.investments/contact
- group: company
  title: ''
  type: Blog
  url: https://goji.investments/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goji.investments/disclosures
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goji.investments/disclosures
- group: auth
  title: ''
  type: Authentication
  url: authentication/goji-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goji-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/goji-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/goji-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goji-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goji-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goji-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goji-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goji-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goji-llms.txt
created: '2026-07-17'
description: Goji is a private-fund digitisation platform, part of the Euroclear group and regulated by the UK Financial Conduct Authority. Founded in 2015 and backed by Anthemis, Goji provides end-to-end infrastructure for asset managers, fund administrators and distributors to digitise access to private markets -- investor onboarding, KYC/KYB and AML, ISA administration, payments, and debt and equity settlement. Its Platform API exposes investor, payment, settlement, bond and ISA operations over HTTPS with HMAC-signed requests and a webhook event stream, letting distributors offer investors a fully digital investment journey into private market funds.
image: https://goji.investments/hubfs/Goji%20favicon.png
layout: provider
mcp_servers:
- description: ''
  name: goji-mcp.yml
  slug: goji-mcpyml
modified: '2026-07-19'
name: Goji
nav: Providers
network: true
overview: 'Goji publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Private Markets, Investments, and Funds.


  The Goji catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goji''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 40.1
  delta: 2.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 37.5
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Goji Authentication
  slug: goji-authentication
  summary_line: http/hmac · 2 schemes
- kind: domain-security
  name: Goji Domain Security
  slug: goji-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goji
tags:
- Company
- Fintech
- Private Markets
- Investments
- Funds
- KYC
- Payments
- ISA
- Settlement
- Webhooks
- Euroclear
website: https://goji.investments
---
