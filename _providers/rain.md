---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Rain Webhooks
  slug: rain-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rain.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rain.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rain.xyz
- group: company
  title: ''
  type: Blog
  url: https://www.rain.xyz/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rain.xyz
- group: operate
  title: ''
  type: Support
  url: https://www.rain.xyz/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://use.rain.xyz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rain.xyz/legal-center/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rain.xyz/legal-center/legal
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rain.xyz
- group: auth
  title: ''
  type: Compliance
  url: https://trust.rain.xyz
- group: design
  title: ''
  type: Conformance
  url: conformance/rain-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rain-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rain-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rain-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rain-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rain-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rain-mcp.yml
created: '2026-07-17'
description: Rain is an enterprise stablecoin payments platform that lets companies embed digital-dollar money movement into their products through a single API. Its infrastructure spans stablecoin wallets and virtual accounts, card issuing (Rain is a Visa and Mastercard Principal Member, settling Visa card transactions daily in stablecoins across multiple blockchains), and money movement via fiat on-ramps, off-ramps, and cross-border payment orchestration. Rain abstracts the back-end complexity of making on-chain stablecoins interoperable with traditional card networks, and maintains PCI DSS and SOC 2 compliance. Customers include Western Union, Nuvei, and ether.fi. Rain has raised over $338M, including a $250M Series C led by ICONIQ and a Series B led by Sapphire Ventures.
image: https://cdn.prod.website-files.com/69af05389f32bed4dc0b35e0/6a556490090af8abcdcfcd24_rain-favicon-2026.png
layout: provider
mcp_servers:
- description: ''
  name: Rain docs MCP
  slug: rain-docs-mcp
modified: '2026-07-20'
name: Rain
nav: Providers
network: true
overview: 'Rain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Stablecoins, Payments, Card Issuing, Fintech, and Cross-Border Payments.


  The Rain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rain''s developer surface includes documentation, engineering blog, support, signup flow, sandbox, and 14 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 41.5
  delta: -1.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 43.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Rain Domain Security
  slug: rain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rain Trust Center
  slug: rain-trust-center
  summary_line: PCI DSS, SOC 2
slug: rain
tags:
- Stablecoins
- Payments
- Card Issuing
- Fintech
- Cross-Border Payments
- Crypto
- Wallets
- Money Movement
- API
website: https://www.rain.xyz
---
