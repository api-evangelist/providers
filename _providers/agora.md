---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Agora Agentic Access
  operation_count: 12
  slug: agora-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.agora.finance
  baseurl_source: declared
  description: The Accounts API from Agora — 2 operation(s) for accounts.
  name: Agora Accounts API
  slug: agora-accounts-api
- baseURL: https://api.agora.finance
  baseurl_source: declared
  description: The Auth API from Agora — 1 operation(s) for auth.
  name: Agora Auth API
  slug: agora-auth-api
- baseURL: https://api.agora.finance
  baseurl_source: declared
  description: The Metrics API from Agora — 3 operation(s) for metrics.
  name: Agora Metrics API
  slug: agora-metrics-api
- baseURL: https://api.agora.finance
  baseurl_source: declared
  description: The Routes API from Agora — 2 operation(s) for routes.
  name: Agora Routes API
  slug: agora-routes-api
- baseURL: https://api.agora.finance
  baseurl_source: declared
  description: The Transactions API from Agora — 2 operation(s) for transactions.
  name: Agora Transactions API
  slug: agora-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Endpoints Accounts API
  slug: open-agora-accounts-api
- collection_type: open
  name: Endpoints Accounts Auth API
  slug: open-agora-auth-api
- collection_type: open
  name: Endpoints Accounts Metrics API
  slug: open-agora-metrics-api
- collection_type: open
  name: Endpoints Accounts Routes API
  slug: open-agora-routes-api
- collection_type: open
  name: Endpoints Accounts Transactions API
  slug: open-agora-transactions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.agora.finance/
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
- description: Agora publishes a hosted MCP server over its developer documentation for AI clients (Claude Code, Cursor, etc.), advertised in llms.txt. It exposes the docs corpus (AUSD contract, Public API, stable s
  name: Agora MCP Server
  slug: agora-mcp-server
modified: '2026-07-17'
name: Agora
nav: Providers
network: true
overview: 'Agora publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Metrics API, and 2 more. Tagged areas include Company, Fintech, Stablecoins, Digital Dollar, and Payments.


  Agora''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 18
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
- Stablecoins
- Digital Dollar
- Payments
- Cryptocurrency
- Blockchain
- AUSD
website: https://www.agora.finance/
---
