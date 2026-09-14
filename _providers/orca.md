---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Orca Agentic Access
  operation_count: 11
  slug: orca-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://api.orca.so/v2/solana
  baseurl_source: declared
  description: Orca protocol information endpoints
  name: Orca protocol API
  slug: orca-protocol-api
- baseURL: https://api.orca.so/v2/solana
  baseurl_source: declared
  description: Token information endpoints
  name: Orca tokens API
  slug: orca-tokens-api
- baseURL: https://api.orca.so/v2/solana
  baseurl_source: declared
  description: Whirlpool information endpoints
  name: Orca whirlpools API
  slug: orca-whirlpools-api
arazzos:
- description: Search Orca Whirlpools for a token pair, then fetch full state for the top-matching pool. Read-only; runs against the open Orca Public REST API.
  name: Find an Orca pool by token pair and read its stats
  slug: orca-find-pool
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orca Public protocol API
  slug: open-orca-protocol-api
- collection_type: open
  name: Orca Public protocol tokens API
  slug: open-orca-tokens-api
- collection_type: open
  name: Orca Public protocol whirlpools API
  slug: open-orca-whirlpools-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orca-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orca.so
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.orca.so/developers/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orca.so
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orca.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orca.so/liquidity/getting-started/beginner-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orca-so
- group: operate
  title: ''
  type: Support
  url: https://docs.orca.so/support/faqs
- group: auth
  title: ''
  type: Authentication
  url: authentication/orca-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/orca-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/orca-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orca-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orca-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orca-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orca-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orca-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orca-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orca-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orca-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orca-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/orca-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/orca-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/orca-find-pool.yml
created: '2026-07-17'
description: Orca is the leading user-friendly concentrated-liquidity automated market maker (AMM) on Solana, built around Whirlpools. Liquidity providers concentrate capital within custom price ranges for higher capital efficiency, traders swap tokens with dynamic Adaptive Fees, and creators launch tokens and lock liquidity for launches. Developers and autonomous agents integrate via the open Whirlpools SDKs (TypeScript, Rust, and a Python option) and the read-only Orca Public REST API (api.orca.so) for pool, token, lock, and protocol-wide data.
image: https://mintcdn.com/orca-ccf67c1f/K618mEucxJ6w73gh/logo/orca-logo.png
layout: provider
mcp_servers:
- description: Orca operates a live, hosted MCP (Model Context Protocol) server for native AI tool-use access to its documentation. No API key required; connect via any MCP-compatible client (Claude Desktop, Cursor,
  name: Orca MCP Server
  slug: orca-mcp-server
modified: '2026-07-20'
name: Orca
nav: Providers
network: true
overview: 'Orca publishes 3 APIs on the [APIs.io](https://apis.io/) network: protocol API, tokens API, and whirlpools API. Tagged areas include Company, Defi Dex, DeFi, DEX, and Solana.


  Orca''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 18 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/orca/refs/heads/main/screenshots/orca-2026-08-07T190854.png
security:
- kind: authentication
  name: Orca Authentication
  slug: orca-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Orca Domain Security
  slug: orca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orca
tags:
- Company
- Defi Dex
- DeFi
- DEX
- Solana
- AMM
- Liquidity
- Concentrated Liquidity
- Blockchain
- Crypto
website: https://orca.so
---
