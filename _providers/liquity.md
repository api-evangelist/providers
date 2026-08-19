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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Liquity Agentic Access
  operation_count: 12
  slug: liquity-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: Provides JSON snapshots of Liquity V2 (BOLD) protocol state including total BOLD supply, collateral values, stability pool deposits, TVL, per-branch (WETH/wstETH/rETH) metrics, token prices, and yield
  name: Liquity V2 Protocol Stats API
  slug: liquity-v2-protocol-stats-api
- description: Provides JSON data feeds used by the Liquity website including yield venue listings for BOLD, protocol fork venues, points leaderboard rankings, and collateral borrow rate comparisons versus DeFi aver
  name: Liquity V2 Website Data API
  slug: liquity-v2-website-data-api
- description: 'Provides JSON snapshots of Liquity V2 governance state including active initiatives, epoch allocation data, and the latest completed governance epoch number. Updated via The Graph subgraph queries on '
  name: Liquity V2 Governance API
  slug: liquity-v2-governance-api
- description: Liquity V1 circulating supply and BAMM stats endpoints.
  name: Liquity V1 Supply API
  slug: liquity-v1-supply-api
- description: Liquity V2 governance state including initiatives and epoch data.
  name: Liquity V2 Governance API
  slug: liquity-v2-governance-api
- description: Liquity V2 (BOLD) protocol state snapshots for mainnet and testnet.
  name: Liquity V2 Protocol Stats API
  slug: liquity-v2-protocol-stats-api
- description: Data feeds for the Liquity website including yield venues, leaderboard, and borrow rates.
  name: Liquity V2 Website Data API
  slug: liquity-v2-website-data-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Liquity Protocol V1 Supply API
  slug: open-liquity-v1-supply-api
- collection_type: open
  name: Liquity Protocol V1 Supply V2 Governance API
  slug: open-liquity-v2-governance-api
- collection_type: open
  name: Liquity Protocol V1 Supply V2 Protocol Stats API
  slug: open-liquity-v2-protocol-stats-api
- collection_type: open
  name: Liquity Protocol V1 Supply V2 Website Data API
  slug: open-liquity-v2-website-data-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/liquity/V2-gov/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/liquity/V2-gov/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liquity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquity-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liquity.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liquity.org/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liquity
- group: operate
  title: ''
  type: StatusPage
  url: https://api.liquity.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liquity.org/
- group: company
  title: ''
  type: Blog
  url: https://www.liquity.org/blog
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/2up5U32
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LiquityProtocol
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/liquity/dev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/liquity/bold
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/liquity/api.liquity.org
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/@liquity/lib-ethers
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/@liquity/lib-base
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/@liquity/lib-react
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/@liquity/lib-subgraph
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/liquity
created: '2026-06-14'
description: Liquity is a decentralized borrowing protocol that allows users to draw interest-free loans against Ether and liquid staking tokens as collateral. The protocol (V1) issues LUSD stablecoin backed by ETH, while V2 (BOLD) supports multi-collateral borrowing with WETH, wstETH, and rETH. Liquity exposes a static JSON API at api.liquity.org covering circulating supplies, protocol stats, stability pool data, prices, governance epochs, yield opportunities, borrow rates, and a points leaderboard — all generated on-chain and published as flat files to GitHub Pages.
examples:
- key_count: 11
  name: Ethereum Protocol Stats
  slug: ethereum-protocol-stats
- key_count: 4
  name: Governance Initiatives
  slug: governance-initiatives
- key_count: 2
  name: Leaderboard
  slug: leaderboard
image: https://liquity.org/favicon.ico
json_schemas:
- name: GovernanceSchemas
  property_count: 0
  slug: governance
- name: Leaderboard
  property_count: 2
  slug: leaderboard
- name: ProtocolStats
  property_count: 11
  slug: protocol-stats
jsonld:
- class_count: 6
  name: Liquity Context
  property_count: 33
  slug: liquity-context
layout: provider
modified: '2026-06-14'
name: Liquity
nav: Providers
network: true
overview: 'Liquity publishes 7 APIs on the [APIs.io](https://apis.io/) network, including V2 Protocol Stats API, V2 Website Data API, V2 Governance API, and 4 more. Tagged areas include DeFi, Decentralized Finance, Lending, Stablecoin, and Ethereum.


  The Liquity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Liquity''s developer surface includes documentation, engineering blog, and 18 more developer resources.'
random_paper: 40
rules:
- effective_rule_count: 6
  extends: []
  name: Liquity API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: liquity-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.2
  delta: -10.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 9.8
    contract_quality: 60.7
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/liquity/refs/heads/main/screenshots/liquity-2026-06-20T184559.png
security:
- kind: domain-security
  name: Liquity Domain Security
  slug: liquity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: liquity
tags:
- DeFi
- Decentralized Finance
- Lending
- Stablecoin
- Ethereum
- LUSD
- BOLD
- Liquidity Protocol
website: https://www.liquity.org/
---
