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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful JSON API for accepting crypto, stock, and card donations on behalf of nonprofits in The Giving Block network. Provides organization management, currency and exchange-rate lookups, crypto depos
  name: The Giving Block Public API
  slug: the-giving-block-public-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://thegivingblock.com
- group: start
  title: ''
  type: Portal
  url: https://thegivingblock.com/developer-resources/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thegivingblock.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thegivingblock.com/reference/getting-started-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thegivingblock.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://thegivingblock.com/about/contact/
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-giving-block-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-giving-block-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-giving-block-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-giving-block-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-giving-block-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/the-giving-block-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/the-giving-block-components.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/the-giving-block-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-giving-block-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-giving-block-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-giving-block-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-giving-block-well-known.yml
created: '2026-07-17'
description: The Giving Block is a crypto-native fundraising platform that lets nonprofits and enterprises accept cryptocurrency, stock, and card donations. Through its Public API and embeddable donation widget, partners can build their own donation experiences or embed The Giving Block's donation form to route gifts to more than 1,000 nonprofit organizations in its network. The API securely accepts Bitcoin, Ethereum, and 100+ other cryptocurrencies, instantly converts crypto donations to cash so nonprofits never have to touch crypto, and also supports stock and donor-advised-fund (DAF) giving. It is a RESTful, JSON API with JWT-based authentication, AES-256 encrypted webhook notifications, and separate production and sandbox environments. The Giving Block was surfaced as a portfolio company of Multicoin Capital and enriched into the API Evangelist network from its published developer documentation.
image: https://thegivingblock.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: the-giving-block-mcp.yml
  slug: the-giving-block-mcpyml
modified: '2026-07-21'
name: The Giving Block
nav: Providers
network: true
overview: 'The Giving Block publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Donations, Fundraising, and Nonprofit.


  The Giving Block''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, authentication, sandbox, and 12 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 22.8
  delta: -3.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 26.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: The Giving Block Authentication
  slug: the-giving-block-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: The Giving Block Domain Security
  slug: the-giving-block-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-giving-block
tags:
- Company
- Crypto Web3
- Donations
- Fundraising
- Nonprofit
- Payments
- Cryptocurrency
- Stock Donations
- Webhooks
- Widgets
website: https://thegivingblock.com
---
