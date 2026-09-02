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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Token risk scanning for Solana mints — authority state, liquidity, holder concentration, Token-2022 extension flags and sell simulation. 26 operations, API-key authentication.
  name: HostDeFi Token Risk API
  slug: hostdefi-token-risk-api
- description: The Analyze Token API from HostDeFi — 1 operation(s) for analyze token.
  name: HostDeFi Analyze Token API
  slug: hostdefi-analyze-token-api
- description: The Health API from HostDeFi — 1 operation(s) for health.
  name: HostDeFi Health API
  slug: hostdefi-health-api
- description: The Keys API from HostDeFi — 1 operation(s) for keys.
  name: HostDeFi Keys API
  slug: hostdefi-keys-api
- description: The Scan API from HostDeFi — 1 operation(s) for scan.
  name: HostDeFi Scan API
  slug: hostdefi-scan-api
- description: The Usage API from HostDeFi — 1 operation(s) for usage.
  name: HostDeFi Usage API
  slug: hostdefi-usage-api
- description: 'Pay-per-call lane for AI agents (x402 protocol): no key, no account - pay USDC per request and get the same A+-F Safety Read. Free tier and API-key plans are unchanged and remain the better per-call p'
  name: HostDeFi x402 (machine-payable) API
  slug: hostdefi-x402-machine-payable-api
artifact_total: 8
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
overview: HostDeFi publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Token Risk API, Analyze Token API, Health API, and 4 more. Tagged areas include Solana, Token Risk, DeFi, rug pull, and x402.
random_paper: 14
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 26.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: hostdefi
tags:
- Solana
- Token Risk
- DeFi
- rug pull
- x402
website: https://hostdefi.com
---
