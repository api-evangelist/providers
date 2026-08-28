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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://maple.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.maple.finance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maple.finance
- group: docs
  title: ''
  type: APIReference
  url: https://docs.maple.finance/technical-resources/interfaces
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.maple.finance/integrate/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maple-labs
- group: start
  title: ''
  type: SignUp
  url: https://maple.finance/app
- group: operate
  title: ''
  type: Support
  url: https://docs.maple.finance/contact-us/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.maple.finance/legal/interface-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.maple.finance/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maple-finance-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/maple-finance-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/maple-finance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/maple-finance-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/maple-finance-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maple-finance-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/maple-finance-well-known.yml
created: '2026-07-17'
description: Maple Finance is an onchain asset management and institutional DeFi lending protocol launched in 2019 (Maple Labs Pty Ltd) that has facilitated over $23 billion in loan originations. It offers digital-asset lending and yield products for individuals and institutions, including the syrupUSDC, syrupUSDT and syrupUSDG ERC-4626 vaults, institutional secured lending, and a cash management pool, spanning Ethereum mainnet and crosschain deployments (Solana, Arbitrum, Base, Plasma) via Chainlink CCIP. Maple's integration surface is onchain smart contracts plus the official @maplelabs/maple-js SDK, a GitBook documentation MCP server, and an extensive technical reference covering loans, pools, strategies, withdrawal managers, and the SYRUP token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maple-finance.png
layout: provider
mcp_servers:
- description: 'Maple''s documentation MCP server (GitBook-hosted). Gives AI agents and MCP-enabled tools (Cursor, Claude Code, etc.) access to the full Maple protocol and integration context for syrupUSD integration '
  name: Maple Docs MCP Server
  slug: maple-docs-mcp-server
modified: '2026-07-20'
name: Maple Finance
nav: Providers
network: true
overview: 'Maple Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defi Lending, DeFi, Onchain Asset Management, and Institutional Lending.


  Maple Finance''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 25.1
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maple-finance/refs/heads/main/screenshots/maple-finance-2026-07-25T230119.png
security:
- kind: domain-security
  name: Maple Finance Domain Security
  slug: maple-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: maple-finance
tags:
- Company
- Defi Lending
- DeFi
- Onchain Asset Management
- Institutional Lending
- Stablecoin Yield
- Ethereum
- SDK
- MCP
website: https://maple.finance
---
