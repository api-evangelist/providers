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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Server and client API for on-ramp, off-ramp, swaps, quotes, sessions, customers (KYC), payment methods, transactions, and virtual accounts.
  name: MoonPay Platform API
  slug: moonpay-platform-api
- description: Widget integration API for buy/sell/swap quotes and transactions, supported currencies and countries, DeFi tokens, network fees, and virtual accounts.
  name: MoonPay Widget API
  slug: moonpay-widget-api
artifact_total: 8
asyncapis:
- description: ''
  name: Moonpay Webhooks
  slug: moonpay-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.moonpay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.moonpay.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.moonpay.com
- group: docs
  title: ''
  type: APIReference
  url: https://dev.moonpay.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.moonpay.com/api-reference/platform/documentation/using-the-api
- group: operate
  title: ''
  type: Support
  url: https://support.moonpay.com
- group: company
  title: ''
  type: Blog
  url: https://www.moonpay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moonpay
- group: start
  title: ''
  type: Login
  url: https://dashboard.moonpay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moonpay.com/legal/terms_of_use_row
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moonpay.com/legal/privacy_policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moonpay.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/moonpay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moonpay-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moonpay-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moonpay-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moonpay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/moonpay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moonpay-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/moonpay-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moonpay-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moonpay-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/moonpay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moonpay-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moonpay-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moonpay-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moonpay-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moonpay-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/moonpay-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moonpay-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moonpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/moonpay
- group: auth
  title: ''
  type: TrustCenter
  url: security/moonpay-trust-center.yml
created: '2026-07-17'
description: MoonPay is a crypto payments infrastructure company that lets businesses and their users buy, sell, and swap digital assets. Its developer platform exposes a Platform API and a Widget API over https://api.moonpay.com covering fiat-to-crypto on-ramp, crypto-to-fiat off-ramp, token swaps and cross-chain bridging, virtual bank accounts for programmatic banking, DeFi token data, KYC/customer management, and a rich webhook event surface. MoonPay ships first-party JavaScript SDKs (the moonpay-js widget SDK and login SDK), web and React Native inline components, a CLI (@moonpay/cli), a published MCP server, and an official Agent Skills library ("skills for AI agents to move money"). Surfaced as a portfolio company of Paradigm and Speedinvest and enriched from its public developer surface.
image: https://github.com/moonpay.png
layout: provider
mcp_servers:
- description: ''
  name: moonpay-mcp.yml
  slug: moonpay-mcpyml
modified: '2026-07-20'
name: MoonPay
nav: Providers
network: true
overview: 'MoonPay publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Infrastructure, Payments, Cryptocurrency, and On-Ramp.


  The MoonPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MoonPay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 27 more developer resources.'
random_paper: 42
score:
  band: strong
  composite: 57.6
  delta: 5.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 87.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 52.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Moonpay Authentication
  slug: moonpay-authentication
  summary_line: apiKey/http-bearer/request-signing · 4 schemes
- kind: domain-security
  name: Moonpay Domain Security
  slug: moonpay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moonpay Vulnerability Disclosure
  slug: moonpay-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Moonpay Trust Center
  slug: moonpay-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: moonpay
tags:
- Company
- Crypto Infrastructure
- Payments
- Cryptocurrency
- On-Ramp
- Off-Ramp
- Fintech
- Digital Wallet
- Blockchain
- KYC
website: https://www.moonpay.com
---
