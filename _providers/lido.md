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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: Read-only HTTP API returning the latest stETH staking APR and a 7-day simple moving average APR. Used by integrators, dashboards, and DeFi protocols to display Lido's current annualized yield. The Lid
  name: Lido APR API
  slug: lido-apr-api
- description: Read-only HTTP API returning a per-address stETH reward history including USD/EUR/GBP fiat conversions, with options to filter to rewards-only, sort, paginate, and choose archival rate sources. Used b
  name: Lido Reward History API
  slug: lido-reward-history-api
- description: Read-only HTTP API for the Lido stETH withdrawal queue. Returns estimated finalization times for one or more withdrawal request IDs, and can forecast the expected wait time for a hypothetical withdraw
  name: Lido Withdrawals API
  slug: lido-withdrawals-api
- description: Service that exposes node operator validator keys from each Lido staking module (Curated, Simple DVT, CSM) for use by deposit security infrastructure, validator monitoring, and integrators. Open-sourc
  name: Lido Keys API
  slug: lido-keys-api
artifact_total: 24
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/lidofinance/lido-keys-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/lidofinance/lido-keys-api/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/lidofinance/lido-keys-api/blob/develop/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lido-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lido-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lido.fi
- group: other
  title: ''
  type: StakingApp
  url: https://stake.lido.fi
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi
- group: start
  title: ''
  type: Portal
  url: https://docs.lido.fi/integrations/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lidofinance
- group: company
  title: ''
  type: Blog
  url: https://blog.lido.fi
- group: operate
  title: ''
  type: Forums
  url: https://research.lido.fi
- group: other
  title: ''
  type: Governance
  url: https://vote.lido.fi
- group: other
  title: ''
  type: Grants
  url: https://lego.lido.fi
- group: start
  title: ''
  type: NodeOperatorPortal
  url: https://operatorportal.lido.fi
- group: other
  title: ''
  type: Scorecard
  url: https://scorecard.lido.fi
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lido.fi
- group: auth
  title: ''
  type: BugBounty
  url: https://immunefi.com/bug-bounty/lido/
- group: other
  title: ''
  type: Audits
  url: https://github.com/lidofinance/audits
- group: other
  title: ''
  type: SmartContracts
  url: https://github.com/lidofinance/core
- group: other
  title: ''
  type: SmartContracts
  url: https://github.com/lidofinance/community-staking-module
- group: other
  title: ''
  type: SmartContracts
  url: https://github.com/lidofinance/dual-governance
- group: other
  title: ''
  type: SmartContracts
  url: https://github.com/lidofinance/lido-l2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/lidofinance/lido-ethereum-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@lidofinance/lido-ethereum-sdk
- group: build
  title: ''
  type: SDKs
  url: https://lidofinance.github.io/lido-ethereum-sdk/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/lidofinance/lido-js-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/lidofinance/lido-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/lido-oracle
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/ethereum-validators-monitoring
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/ethereum-head-watcher
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/onchain-mon
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/depositor-bot
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/lido-council-daemon
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/validator-ejector
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/easy-track
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/diffyscan
- group: build
  title: ''
  type: Tools
  url: https://github.com/lidofinance/state-mate
- group: other
  title: ''
  type: Subgraph
  url: https://github.com/lidofinance/lido-subgraph
- group: design
  title: ''
  type: UIComponents
  url: https://github.com/lidofinance/ui
- group: other
  title: ''
  type: Widget
  url: https://github.com/lidofinance/ethereum-staking-widget
- group: other
  title: ''
  type: Widget
  url: https://github.com/lidofinance/csm-widget
- group: other
  title: ''
  type: Template
  url: https://github.com/lidofinance/lido-frontend-template
- group: other
  title: ''
  type: ImprovementProposals
  url: https://github.com/lidofinance/lido-improvement-proposals
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/deployed-contracts/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/contracts/lido
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/contracts/wsteth
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/contracts/withdrawal-queue-erc721
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/contracts/staking-router
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/staking-modules/csm/intro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/guides/node-operators/general-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/guides/oracle-operator-manual
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LidoFinance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lidofinance
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/lido
- group: other
  title: ''
  type: Telegram
  url: https://t.me/lidofinance
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@LidoFinance
- group: auth
  title: ''
  type: TokenContract
  url: https://etherscan.io/token/0xae7ab96520de3a18e5e111b5eaab095312d7fe84
- group: auth
  title: ''
  type: TokenContract
  url: https://etherscan.io/token/0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0
- group: auth
  title: ''
  type: TokenContract
  url: https://etherscan.io/token/0x5a98fcbea516cf06857215779fd812ca3bef1b32
created: '2026-05-24'
description: 'Lido is the leading liquid staking protocol on Ethereum, allowing anyone to stake ETH without locking it or running validator infrastructure. Stakers deposit ETH and receive stETH — a rebasing ERC-20 that earns daily staking rewards — or its non-rebasing wrapped form wstETH used widely across DeFi. Lido is governed by the Lido DAO via the LDO token, Snapshot signaling, on-chain Aragon voting, and a Dual Governance timelock that gives stETH holders a dynamic veto over the DAO. The protocol''s validator set is delegated across multiple Staking Modules — the Curated Module (professional node operators), Simple DVT (distributed validator technology via Obol and SSV), the Community Staking Module (permissionless solo stakers backed by bonded stETH), and stVaults (modular tailored setups). At over $18B TVL and 8.8M+ ETH staked, Lido is the #1 liquid staking provider by total value locked. Lido previously operated on Polygon (stMATIC, sunset June 2025) and Solana (stSOL, sunset February
  2024); the protocol is now Ethereum-only. Lido publishes the open-source core smart contracts, a TypeScript SDK (`@lidofinance/lido-ethereum-sdk`), a Python oracle daemon, validator monitoring tooling, frontend widgets, and three public read-only HTTP APIs for protocol APR, reward history, and withdrawal queue timing.'
features:
- stETH liquid staking token — rebasing ERC-20 tracking 1 ETH 1:1, daily rewards via on-chain rebase
- wstETH wrapped non-rebasing ERC-20 used widely across DeFi (Aave, Maker, Curve, Balancer, etc.)
- Curated Staking Module — DAO-approved professional node operators
- Simple DVT Module — distributed validator technology powered by Obol and SSV
- Community Staking Module (CSM) — permissionless solo-staker module with bonded stETH
- stVaults — modular tailored validator setups
- Dual Governance — stETH holder veto with dynamic timelock over the LDO DAO
- Withdrawals (since Lido V2 / Shapella) via WithdrawalQueueERC721 NFTs
- Lido Oracle — Python daemon submitting consensus layer accounting reports
- Validator Ejector and Council Daemon for deposit security and forced exits
- Public read-only HTTP APIs for APR, reward history, and withdrawal queue
- Lido Ethereum SDK in TypeScript for staking, wrapping, withdrawals, rewards
- Lido CLI, Diffyscan, State Mate and Ethereum Validators Monitoring tooling
- Easy Track for delegated DAO motions and treasury operations
- LEGO grants program funding ecosystem and integration work
- Over $18B TVL and 8.8M+ ETH staked —
- Previously supported Polygon (stMATIC) and Solana (stSOL), both sunset
graphqls:
- description: Lido Finance exposes on-chain protocol data through a subgraph on The Graph protocol. The subgraph indexes Ethereum mainnet events from the Lido stETH contract, the Withdrawal Queue, the Node Operator
  name: Lido Finance GraphQL API
  slug: lido-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lido.png
layout: provider
modified: '2026-05-24'
name: Lido
nav: Providers
network: true
overview: 'Lido publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Liquid Staking, Ethereum, Staking, DeFi, and stETH.


  Lido''s developer surface includes documentation, developer portal, engineering blog, CLI, tooling, YouTube channel, and 54 more developer resources.'
random_paper: 126
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.2
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lido/refs/heads/main/screenshots/lido-2026-06-20T184507.png
security:
- kind: domain-security
  name: Lido Domain Security
  slug: lido-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lido Vulnerability Disclosure
  slug: lido-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lido
tags:
- Liquid Staking
- Ethereum
- Staking
- DeFi
- stETH
- wstETH
- Validators
- Node Operators
- DAO
- Governance
- LDO
- Oracle
- Open Source
- Web3
- Smart Contracts
- Distributed Validator Technology
- Community Staking Module
website: https://lido.fi
---
