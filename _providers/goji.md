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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-17'
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
random_paper: 127
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 40.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goji/refs/heads/main/screenshots/goji-2026-07-25T220023.png
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
