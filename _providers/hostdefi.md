---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Token risk scanning for Solana mints — authority state, liquidity, holder concentration, Token-2022 extension flags and sell simulation. 26 operations, API-key authentication.
  name: HostDeFi Token Risk API
  slug: hostdefi-token-risk-api
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hostdefi-tools-list.json
- group: commercial
  title: ''
  type: FinOps
  url: finops/hostdefi-x402-manifest.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hostdefi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://hostdefi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hostdefi.com/docs/api/
created: '2026-08-21'
description: 'HostDeFi is a non-custodial Solana token-risk service that scans a mint before a purchase — mint and freeze authority state, liquidity depth and lock status, holder concentration, dangerous Token-2022 extensions, sell simulation and contract flags. The public contract is an OpenAPI 3.1 document of 26 operations served from hostdefi.com/api with API-key authentication. HostDeFi also exposes an x402 machine-payment surface: an authority quick-check endpoint that returns HTTP 402 with a signed payment challenge, priced in USDC and payable on either Solana or Base, so an agent can buy a single check without an account.'
layout: provider
mcp_servers:
- description: ''
  name: HostDeFi MCP Server
  slug: hostdefi-mcp-server
modified: '2026-08-21'
name: HostDeFi
nav: Providers
network: true
overview: 'HostDeFi publishes 1 API on the [APIs.io](https://apis.io/) network: Token Risk API. Tagged areas include Solana, Blockchain, Token Risk, Security, and DeFi.'
random_paper: 14
score:
  band: emerging
  composite: 21.3
  delta: 3.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 54.7
    developer_ergonomics: 26.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
slug: hostdefi
tags:
- Solana
- Blockchain
- Token Risk
- Security
- DeFi
- x402
- Agent Commerce
- Crypto
- MCP
- Machine Payments
website: https://hostdefi.com
---
