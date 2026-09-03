---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Exactly Agentic Access
  operation_count: 40
  slug: exactly-agentic-access
  summary_line: 40 operations · 36 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Read-only smart contract interface for previewing deposits, borrows, withdrawals, and repayments across all market maturity pools. Returns projected yields, repayment amounts, and comprehensive accoun
  name: Exactly Protocol Previewer API
  slug: exactly-protocol-previewer-api
- description: ERC-4626-compliant smart contract interface for the core Market contract exposing view and write methods for depositing, borrowing, withdrawing, repaying, minting, redeeming, and liquidating positions
  name: Exactly Protocol Market API
  slug: exactly-protocol-market-api
- description: Smart contract interface for the Auditor, the central risk management component that manages market listings, collateral factors, account liquidity checks, and liquidation eligibility. Provides method
  name: Exactly Protocol Auditor API
  slug: exactly-protocol-auditor-api
- description: Smart contract interface for querying and claiming EXA and esEXA token rewards distributed to depositors and borrowers. Supports querying claimable rewards, reward configurations, distribution timelin
  name: Exactly Protocol RewardsController API
  slug: exactly-protocol-rewardscontroller-api
- description: GraphQL subgraph API powered by The Graph for querying indexed on-chain data from Exactly Protocol on Ethereum mainnet and Optimism. Supports advanced queries including aggregation, filtering, relatio
  name: Exactly Protocol Subgraph API (The Graph)
  slug: exactly-protocol-subgraph-api-the-graph
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: ERC-4626 vault standard methods
  name: Exactly Protocol ERC-4626 API
  slug: exactly-erc-4626-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Fixed rate maturity pool operations
  name: Exactly Protocol Fixed Rate API
  slug: exactly-fixed-rate-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Liquidation eligibility and seizure calculations
  name: Exactly Protocol Liquidations API
  slug: exactly-liquidations-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Account liquidity and collateral checks
  name: Exactly Protocol Liquidity API
  slug: exactly-liquidity-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Write methods for market configuration (admin only)
  name: Exactly Protocol Market Management API
  slug: exactly-market-management-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: View methods for querying market state
  name: Exactly Protocol Market State API
  slug: exactly-market-state-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Market listing and configuration queries
  name: Exactly Protocol Markets API
  slug: exactly-markets-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Read-only preview methods for Exactly Protocol markets
  name: Exactly Protocol Previewer API
  slug: exactly-previewer-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Reward program configuration and indexes
  name: Exactly Protocol Reward Configuration API
  slug: exactly-reward-configuration-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Write methods for claiming earned rewards
  name: Exactly Protocol Rewards Claims API
  slug: exactly-rewards-claims-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: View methods for querying reward state and amounts
  name: Exactly Protocol Rewards Query API
  slug: exactly-rewards-query-api
- baseURL: https://app.exact.ly
  baseurl_source: declared
  description: Floating/variable rate deposit and borrow operations
  name: Exactly Protocol Variable Rate API
  slug: exactly-variable-rate-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 API
  slug: open-exactly-erc-4626-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Fixed Rate API
  slug: open-exactly-fixed-rate-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Liquidations API
  slug: open-exactly-liquidations-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Liquidity API
  slug: open-exactly-liquidity-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Market Management API
  slug: open-exactly-market-management-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Market State API
  slug: open-exactly-market-state-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Markets API
  slug: open-exactly-markets-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Reward Configuration API
  slug: open-exactly-reward-configuration-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Rewards Claims API
  slug: open-exactly-rewards-claims-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Rewards Query API
  slug: open-exactly-rewards-query-api
- collection_type: open
  name: Exactly Protocol Auditor ERC-4626 Variable Rate API
  slug: open-exactly-variable-rate-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exactly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exactly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://exact.ly
- group: docs
  title: ''
  type: Documentation
  url: https://docs.exact.ly
- group: build
  title: ''
  type: GitHub
  url: https://github.com/exactly
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/exactly
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/exactlyprotocol
- group: other
  title: ''
  type: Telegram
  url: https://t.me/exactlyprotocol
- group: other
  title: ''
  type: Medium
  url: https://medium.com/exactly-protocol
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exact.ly/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exact.ly/privacy
- group: auth
  title: ''
  type: BugBounty
  url: https://immunefi.com/bounty/exactly
- group: operate
  title: ''
  type: StatusPage
  url: https://exact.ly
- group: other
  title: ''
  type: Governance
  url: https://docs.exact.ly/governance/protocol-governance
- group: other
  title: ''
  type: WhitePaper
  url: https://docs.exact.ly/resources/white-paper
- group: other
  title: ''
  type: Audits
  url: https://docs.exact.ly/security/audits
- group: other
  title: ''
  type: SmartContracts
  url: https://docs.exact.ly/guides/smart-contract-addresses.md
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/exactly/refs/heads/main/finops/finops.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/@exactly_protocol
created: '2026-06-14'
description: Exactly Protocol is a decentralized, non-custodial, open-source protocol providing autonomous fixed and variable interest rate credit markets on Ethereum, Optimism, and Base. It enables users to deposit and borrow crypto assets at both variable rates and fixed rates through maturity pools, using a continuous non-linear interest rate model, dynamic close factor liquidations, and a rewards distribution system with the EXA governance token.
examples:
- key_count: 5
  name: Claim All Rewards
  slug: claim-all-rewards
- key_count: 5
  name: Get Market Accounts
  slug: get-market-accounts
- key_count: 5
  name: Preview Deposit At Maturity
  slug: preview-deposit-at-maturity
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: 'Exactly Protocol provides a GraphQL subgraph API powered by The Graph, enabling developers to query indexed on-chain event data from the Exactly Protocol lending protocol deployed on Ethereum mainnet '
  name: Exactly Protocol GraphQL API (The Graph Subgraph)
  slug: exactly-graphql
image: https://exact.ly/favicon.ico
json_schemas:
- name: FixedPreview
  property_count: 3
  slug: fixed-preview
- name: MarketAccount
  property_count: 19
  slug: market-account
- name: RewardConfig
  property_count: 14
  slug: reward-config
jsonld:
- class_count: 12
  name: Exactly Context
  property_count: 42
  slug: exactly-context
layout: provider
modified: '2026-06-14'
name: Exactly Protocol
nav: Providers
network: true
overview: 'Exactly Protocol publishes 12 APIs on the [APIs.io](https://apis.io/) network, including ERC-4626 API, Fixed Rate API, Liquidations API, and 9 more. Tagged areas include DeFi, Lending, Borrowing, Fixed Rate, and Variable Rate.


  The Exactly Protocol catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Exactly Protocol''s developer surface includes documentation, GitHub presence, engineering blog, and 16 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Exactly Protocol API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: exactly-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.7
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exactly/refs/heads/main/screenshots/exactly-2026-06-20T180920.png
security:
- kind: domain-security
  name: Exactly Domain Security
  slug: exactly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: exactly
tags:
- DeFi
- Lending
- Borrowing
- Fixed Rate
- Variable Rate
- Ethereum
- Optimism
- Base
- ERC-4626
- Credit Markets
website: https://exact.ly
---
