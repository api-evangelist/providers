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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Public investor REST API for the Bitbond Offering Manager securities-issuance platform. Covers offerings lookup, orders, checkout/payments, KYC, investor profiles, and GDPR data export/erase. Protecte
  name: Bitbond Offering Manager API
  slug: bitbond-offering-manager-api
- description: Programmatic token and smart-contract deployment API for Token Tool. Enables minting, burning, transferring, pausing, and metadata updates on CertiK-audited ERC-20/ERC-1400/ERC-721 contracts, plus tok
  name: Bitbond Token Tool API
  slug: bitbond-token-tool-api
artifact_total: 6
asyncapis:
- description: ''
  name: Bitbond Offering Manager Webhooks
  slug: bitbond-offering-manager-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.bitbond.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bitbond.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitbond.com/asset-tokenization-suite
- group: docs
  title: ''
  type: APIReference
  url: https://om.bitbond.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitbond.com/asset-tokenization-suite/offering-manager/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.bitbond.com/resources
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bitbond.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitbond
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitbond.com
- group: operate
  title: ''
  type: Support
  url: mailto:service@bitbond.com
- group: commercial
  title: ''
  type: Pricing
  url: https://tokentool.bitbond.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tokentool.bitbond.com
- group: start
  title: ''
  type: Login
  url: https://om.bitbond.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tokentool.bitbond.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitbond.com/legal
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitbond-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitbond-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/bitbond-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bitbond-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitbond-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitbond-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitbond-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitbond-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitbond-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitbond-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitbond-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitbond-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bitbond-offering-manager-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bitbond is a Berlin-based tokenization technology company (Bitbond GmbH) that provides an Asset Tokenization Suite for issuing, managing, and distributing digital assets on public blockchains. Its two developer-facing products are Token Tool, a self-serve platform and API for deploying and managing compliant ERC-20, ERC-1400, and ERC-721 smart contracts (minting, burning, transfers, vesting, token sales, airdrops, and payment automation) across 11+ EVM and non-EVM chains; and Offering Manager, an end-to-end securities-issuance platform with a public investor REST API covering offerings, orders, payments, KYC/AML, and investor profiles. Bitbond also ships an official Token Tool MCP server so AI agents can deploy and manage tokens, plus documented webhooks, testnet faucets, and a status page.
image: https://www.bitbond.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: bitbond-mcp.yml
  slug: bitbond-mcpyml
modified: '2026-07-18'
name: Bitbond
nav: Providers
network: true
overview: 'Bitbond publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tokenization, Blockchain, Digital Assets, and Smart Contracts.


  The Bitbond catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitbond''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 142
score:
  band: developing
  composite: 45.3
  delta: -1.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 47.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitbond/refs/heads/main/screenshots/bitbond-2026-07-25T203131.png
security:
- kind: authentication
  name: Bitbond Authentication
  slug: bitbond-authentication
  summary_line: http-bearer/apiKey/wallet · 4 schemes
- kind: domain-security
  name: Bitbond Domain Security
  slug: bitbond-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitbond
tags:
- Company
- Tokenization
- Blockchain
- Digital Assets
- Smart Contracts
- Web3
- Securities
- Payments
- MCP
website: https://www.bitbond.com
---
