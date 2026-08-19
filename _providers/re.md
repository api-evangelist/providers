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
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Health, APY, NAV, and price series
  name: Re General API
  slug: re-general-api
- description: Re Points leaderboard and opportunities
  name: Re Points API
  slug: re-points-api
- description: Token supply metrics
  name: Re Supply API
  slug: re-supply-api
- description: Total value locked and capital metrics
  name: Re TVL API
  slug: re-tvl-api
- description: Per-wallet balances and points
  name: Re Wallet API
  slug: re-wallet-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Re Protocol General API
  slug: open-re-general-api
- collection_type: open
  name: Re Protocol General Points API
  slug: open-re-points-api
- collection_type: open
  name: Re Protocol General Supply API
  slug: open-re-supply-api
- collection_type: open
  name: Re Protocol General TVL API
  slug: open-re-tvl-api
- collection_type: open
  name: Re Protocol General Wallet API
  slug: open-re-wallet-api
common:
- group: company
  title: ''
  type: Website
  url: https://re.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.re.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.re.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.re.xyz/products/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.re.xyz/getting-started-with-re/readme.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/re-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/re-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/re-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/re-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/re-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/re-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/re-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/re-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/re-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/re-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/reprotocol
- group: commercial
  title: ''
  type: TermsOfService
  url: https://re.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://re.xyz/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.re.xyz
- group: company
  title: ''
  type: Twitter
  url: https://x.com/re
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/reprotocol
- group: other
  title: ''
  type: Telegram
  url: https://t.me/re_protocol
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/re-protocol
created: '2026-07-17'
description: Re (Re Protocol) is an onchain reinsurance platform that channels stablecoin capital into fully collateralized, regulated reinsurance contracts. It issues two yield-bearing tokens — reUSD, the senior tranche, and reUSDe, the mezzanine tranche — backed by real reinsurance premiums from a diversified book (homeowners, commercial and personal auto, small business, and workers compensation). Re describes itself as "the internet capital market for insurance risk," giving onchain participants access to the ~$800B global reinsurance market with onchain attestations, audits, and a transparent loss waterfall. Re operates a public, read-only HTTP API (https://api.re.xyz) serving APY/NAV, price history, token supply, protocol TVL, the Re Points leaderboard, and per-wallet data, plus a hosted MCP server that exposes the same data to AI agents. Backed by Electric Capital.
image: https://re.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: re-mcp.yml
  slug: re-mcpyml
modified: '2026-07-20'
name: Re
nav: Providers
network: true
overview: 'Re publishes 5 APIs on the [APIs.io](https://apis.io/) network, including General API, Points API, Supply API, and 2 more. Tagged areas include Company, Fintech, Reinsurance, Insurance, and DeFi.


  Re''s developer surface includes documentation, API reference, getting-started guide, authentication, support, signup flow, and 18 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 40.9
  delta: 0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 40.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Re Authentication
  slug: re-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Re Domain Security
  slug: re-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: re
tags:
- Company
- Fintech
- Reinsurance
- Insurance
- DeFi
- Blockchain
- Real World Assets
- Stablecoin
- Yield
- Onchain
website: https://re.xyz/
---
