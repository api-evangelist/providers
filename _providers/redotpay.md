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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Production RedotPay HTTP API surface behind the redotpay CLI and the redotpay-payment MCP server. Provides OAuth2 device-flow authentication and the agentic Machine Payments Protocol (MPP) endpoint th
  name: RedotPay Agentic Payments API
  slug: redotpay-agentic-payments-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redotpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redotpay.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/redotpay/redotpay-cli
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.redotpay.com
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.redotpay.com
- group: company
  title: ''
  type: Blog
  url: https://blog.redotpay.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redotpay
- group: start
  title: ''
  type: SignUp
  url: https://www.redotpay.com
- group: build
  title: ''
  type: Packages
  url: packages/redotpay-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/redotpay-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/redotpay-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redotpay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/redotpay-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redotpay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/redotpay-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redotpay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redotpay-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redotpay-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redotpay-well-known.yml
created: '2026-07-17'
description: 'RedotPay is a global stablecoin-based payment fintech that integrates blockchain solutions with traditional banking and finance infrastructures. The platform lets millions of people spend and send digital assets through a crypto-backed Visa card, a multi-currency wallet, P2P trading, international transfers, and stablecoin earning. Its developer-facing surface is agentic: a first-party Rust CLI (redotpay) and a local MCP server / Agent Skill (redotpay-payment) that let AI agents settle HTTP 402 "Payment Required" challenges over the Machine Payments Protocol (MPP), using OAuth2 device-flow login and per-payment idempotency against the production RedotPay API.'
image: https://www.redotpay.com/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: redotpay-mcp.yml
  slug: redotpay-mcpyml
modified: '2026-07-21'
name: Redotpay
nav: Providers
network: true
overview: 'Redotpay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Stablecoin, and Cryptocurrency.


  Redotpay''s developer surface includes documentation, support, engineering blog, signup flow, CLI, authentication, and 14 more developer resources.'
random_paper: 60
scopes:
- name: Redotpay Scopes
  scope_count: 0
  slug: redotpay-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 25.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Redotpay Authentication
  slug: redotpay-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Redotpay Domain Security
  slug: redotpay-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: redotpay
tags:
- Company
- Payments
- Fintech
- Stablecoin
- Cryptocurrency
- Wallet
- Agentic Payments
- Machine Payments Protocol
- x402
- OAuth
website: https://www.redotpay.com
---
