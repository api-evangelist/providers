---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://wealthville.net/api/v1
  baseurl_source: declared
  description: The Scores API from WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) — 2 operation(s) for scores.
  name: WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) Scores API
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-scores-api
- baseURL: https://wealthville.net/api/v1
  baseurl_source: declared
  description: The Signals API from WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) — 2 operation(s) for signals.
  name: WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) Signals API
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-signals-api
- baseURL: https://wealthville.net/api/v1
  baseurl_source: declared
  description: The Track Record API from WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) — 1 operation(s) for track record.
  name: WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) Track Record API
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-track-record-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wealthville Public Data Scores API
  slug: open-wealthville-defi-liquidity-pool-scores-api-solana-evm-scores-api
- collection_type: open
  name: Wealthville Public Data Signals API
  slug: open-wealthville-defi-liquidity-pool-scores-api-solana-evm-signals-api
- collection_type: open
  name: Wealthville Public Data Track Record API
  slug: open-wealthville-defi-liquidity-pool-scores-api-solana-evm-track-record-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wealthville-defi-liquidity-pool-scores-api-solana-evm-public-data-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wealthville-defi-liquidity-pool-scores-api-solana-evm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://wealthville.net/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealthville-defi-liquidity-pool-scores-api-solana-evm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wealthville-defi-liquidity-pool-scores-api-solana-evm-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wealthville-defi-liquidity-pool-scores-api-solana-evm-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/wealthville-defi-liquidity-pool-scores-api-solana-evm-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/wealthville-defi-liquidity-pool-scores-api-solana-evm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wealthville-defi-liquidity-pool-scores-api-solana-evm-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wealthville-defi-liquidity-pool-scores-api-solana-evm-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wealthville-defi-liquidity-pool-scores-api-solana-evm-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wealthville-defi-liquidity-pool-scores-api-solana-evm-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/wealthville-defi-liquidity-pool-scores-api-solana-evm-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wealthville-defi-liquidity-pool-scores-api-solana-evm-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wealthville-defi-liquidity-pool-scores-api-solana-evm-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wealthville-defi-liquidity-pool-scores-api-solana-evm-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wealthville-defi-liquidity-pool-scores-api-solana-evm-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wealthville-defi-liquidity-pool-scores-api-solana-evm-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wealthville.net/developers
- group: docs
  title: ''
  type: APIReference
  url: https://wealthville.net/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amitesh-m/wealthville-integrations
- group: operate
  title: ''
  type: Support
  url: https://wealthville.net/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.wealthville.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://wealthville.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wealthville.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wealthville.net/privacy
created: '2026-07-27'
description: WealthVille provides a public, keyless REST API and agent-native surfaces for DeFi liquidity-pool scoring and signals across Solana and EVM chains. It exposes a composite Wealthville Score (0-100) with Enter/Hold/Exit verdicts, per-protocol confidence, Solana sub-scores (Risk, Scout, Farmer), an outcome-labeled track record, and a signals feed. Coverage includes Solana (Meteora, Orca, Raydium) and EVM chains (Ethereum, Arbitrum, Base, Optimism, Polygon, BNB Chain). The API is anonymous by default at 60 requests/min per IP, CORS-open, and read-only — every published operation is a GET. Alongside the REST contract WealthVille publishes an OpenAPI 3.0.3 document at the API host root, an llms.txt, a hosted Streamable-HTTP MCP server with four ungated tools, and a first-party MIT-licensed connector family (MCP server, ElizaOS plugin, Solana Agent Kit plugin, MCPB bundle, Gemini extension) plus its own Agent Skill.
examples:
- key_count: 3
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Scores Top
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-scores-top
- key_count: 4
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Signals Feed
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-signals-feed
- key_count: 7
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Track Record
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-track-record
image: https://raw.githubusercontent.com/amitesh-m/wealthville-integrations/main/assets/logo.png
layout: provider
mcp_servers:
- description: Solana + EVM liquidity-pool scores - Enter/Hold/Exit verdicts and a 0-100 Wealthville Score.
  name: WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) MCP Server
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-mcp-server
modified: '2026-08-09'
name: WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM)
nav: Providers
network: true
overview: 'WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Scores API, Signals API, and Track Record API. Tagged areas include DeFi, Liquidity Pools, Blockchain Analytics, Solana, and EVM.


  WealthVille — DeFi Liquidity Pool Scores API (Solana & EVM)''s developer surface includes authentication, API reference, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 2
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Rate Limits
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-rate-limits
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 53.5
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 44.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wealthville-defi-liquidity-pool-scores-api-solana-evm/refs/heads/main/screenshots/wealthville-defi-liquidity-pool-scores-api-solana-evm-2026-08-17T082848.png
security:
- kind: authentication
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Authentication
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Domain Security
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wealthville Defi Liquidity Pool Scores Api Solana Evm Vulnerability Disclosure
  slug: wealthville-defi-liquidity-pool-scores-api-solana-evm-vulnerability-disclosure
  summary_line: contact published
slug: wealthville-defi-liquidity-pool-scores-api-solana-evm
tags:
- DeFi
- Liquidity Pools
- Blockchain Analytics
- Solana
- EVM
- Ethereum
- Yield Farming
- Risk Scoring
- MCP
- AI Agents
- Financial Data
website: https://wealthville.net/developers
---
