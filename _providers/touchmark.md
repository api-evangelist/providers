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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The pricing surface behind @touchmark/sdk - open a session per scope, emit events fire-and-forget with an idempotent event_id, and consume quality-adjusted valuations (absolute fair_price_usd per even
  name: Touchmark Sessions API
  slug: touchmark-sessions-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/touchmark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://touchmark.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.touchmark.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.touchmark.ai/sdk/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.touchmark.ai/sdk/quickstart
- group: start
  title: ''
  type: Login
  url: https://app.touchmark.ai/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Touchmark-AI
- group: company
  title: ''
  type: XTwitter
  url: https://x.com/TouchmarkAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/touchmark-ai
- group: build
  title: ''
  type: Packages
  url: packages/touchmark-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/touchmark-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/touchmark-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/touchmark-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/touchmark-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/touchmark-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/touchmark-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/touchmark-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/touchmark-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/touchmark-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/touchmark-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/touchmark-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/touchmark-data-model.yml
created: '2026-07-17'
description: Touchmark is solving AI pricing - instead of AI being priced per token regardless of quality, Touchmark prices it by the quality, efficiency, and value of the output, so spend is fair, predictable, and tied to what you actually get. Applications emit the events they already produce (model outputs, tool calls, code diffs) with a base price, and Touchmark's out-of-band judge returns a quality-adjusted fair price for each event on a separate valuation stream. A Y Combinator Summer 2026 company founded by Ilia Bolgov and Roman Yanushevskyi in San Francisco; the TypeScript SDK (@touchmark/sdk) is in private beta.
image: https://touchmark.ai/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: touchmark-mcp.yml
  slug: touchmark-mcpyml
modified: '2026-07-21'
name: Touchmark
nav: Providers
network: true
overview: 'Touchmark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Pricing, Billing, and Monetization.


  Touchmark''s developer surface includes documentation, API reference, getting-started guide, authentication, and 18 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 23.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Touchmark Authentication
  slug: touchmark-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Touchmark Domain Security
  slug: touchmark-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: touchmark
tags:
- Company
- Artificial Intelligence
- AI Pricing
- Billing
- Monetization
- Evals
- Usage-Based Billing
- Quality Scoring
website: https://touchmark.ai
---
