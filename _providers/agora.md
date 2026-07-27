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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Agora Agentic Access
  operation_count: 12
  slug: agora-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 5
apis:
- description: The Accounts API from Agora — 2 operation(s) for accounts.
  name: Agora Accounts API
  slug: agora-accounts-api
- description: The Auth API from Agora — 1 operation(s) for auth.
  name: Agora Auth API
  slug: agora-auth-api
- description: The Metrics API from Agora — 3 operation(s) for metrics.
  name: Agora Metrics API
  slug: agora-metrics-api
- description: The Routes API from Agora — 2 operation(s) for routes.
  name: Agora Routes API
  slug: agora-routes-api
- description: The Transactions API from Agora — 2 operation(s) for transactions.
  name: Agora Transactions API
  slug: agora-transactions-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agora-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agora-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agora.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agora.finance/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agora.finance/api/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agora.finance/api
- group: company
  title: ''
  type: Blog
  url: https://www.agora.finance/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agora-finance
- group: commercial
  title: ''
  type: TermsOfService
  url: https://static.agora.finance/termsofuse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.agora.finance/privacypolicy.pdf
- group: start
  title: ''
  type: SignUp
  url: https://www.agora.finance/contact
- group: operate
  title: ''
  type: Support
  url: https://www.agora.finance/contact
- group: auth
  title: ''
  type: Authentication
  url: authentication/agora-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agora-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agora-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agora-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agora-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agora-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agora-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/agora-endpoints-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agora-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agora-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agora-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Agora (agora.finance) is a stablecoin infrastructure company building "money and payments for internet markets." Its core product is AUSD, the Agora Dollar — a digital dollar minted 1:1 with USD and backed 100% by cash, overnight repurchase agreements, and short-term U.S. Treasuries. AUSD is an ERC-20 token live across 12+ EVM and Solana networks, with reserves managed by VanEck and State Street. Agora also offers white-labeled stablecoins (launch your own branded token on an ERC-4626 vault architecture over AUSD), instant liquidity (atomic minting against USDC/USDT), and Stable Swaps (a fixed-price, zero-slippage swap protocol for verified users). The Agora Public API (Beta, v0) exposes real-time AUSD supply metrics plus authenticated Accounts, Routes, and Transactions endpoints for mint/redeem flows. Founded by Nick van Eck; backed by General Catalyst, Paradigm, and Dragonfly.
image: https://www.agora.finance/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: agora-mcp.yml
  slug: agora-mcpyml
modified: '2026-07-17'
name: Agora
nav: Providers
network: true
overview: 'Agora publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Metrics API, and 2 more. Tagged areas include Company, Fintech, Stablecoin, Digital Dollar, and Payments.


  Agora''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 47.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.0
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 47.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agora/refs/heads/main/screenshots/agora-2026-07-25T195314.png
security:
- kind: authentication
  name: Agora Authentication
  slug: agora-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Agora Domain Security
  slug: agora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agora
tags:
- Company
- Fintech
- Stablecoin
- Digital Dollar
- Payments
- Cryptocurrency
- Blockchain
- API
- AUSD
website: https://docs.agora.finance/
---
