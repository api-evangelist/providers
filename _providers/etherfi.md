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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etherfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ether.fi
- group: other
  title: ''
  type: App
  url: https://app.ether.fi
- group: other
  title: ''
  type: Stake
  url: https://www.ether.fi/stake
- group: other
  title: ''
  type: Restake
  url: https://www.ether.fi/restake
- group: other
  title: ''
  type: Liquid
  url: https://www.ether.fi/liquid
- group: other
  title: ''
  type: Cash
  url: https://www.ether.fi/cash
- group: other
  title: ''
  type: Club
  url: https://www.ether.fi/the-club
- group: other
  title: ''
  type: Institutional
  url: https://www.ether.fi/institutional
- group: docs
  title: ''
  type: Documentation
  url: https://etherfi.gitbook.io/etherfi
- group: docs
  title: ''
  type: TechnicalDocumentation
  url: https://etherfi.gitbook.io/etherfi/ether.fi-whitepaper/technical-documentation
- group: other
  title: ''
  type: Contracts
  url: https://etherfi.gitbook.io/etherfi/contracts-and-integrations/contracts
- group: other
  title: ''
  type: NodeOperators
  url: https://etherfi.gitbook.io/etherfi/node-operators/node-operators-guide
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ether.fi
- group: other
  title: ''
  type: Governance
  url: https://governance.ether.fi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etherfi-protocol
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/etherfi-protocol/smart-contracts
- group: auth
  title: ''
  type: BugBounty
  url: https://immunefi.com/bug-bounty/etherfi/
- group: other
  title: ''
  type: DefiLlama
  url: https://defillama.com/protocol/ether.fi
- group: other
  title: ''
  type: Dune
  url: https://dune.com/etherfi_team/etherfi
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ether_fi
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/ether-fi
- group: other
  title: ''
  type: Medium
  url: https://medium.com/etherfi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ether-fi
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/etherfi
created: '2026-05-24'
description: 'ether.fi is a non-custodial, decentralized Ethereum liquid restaking protocol where stakers retain control of their validator keys. Users deposit ETH to mint eETH, a rebasing liquid restaking token (LRT), or wrap it into weETH, the non-rebasing ERC-20 used across DeFi and bridged cross-chain via LayerZero to networks including Arbitrum, Optimism, Base, Linea, Mode, Scroll, BNB Chain, Blast, Mantle, and Solana. Beyond ETH liquid restaking, ether.fi has expanded into eBTC (Bitcoin restaking) and eUSD (stablecoin restaking), Liquid auto- balancing strategy vaults, the ether.fi Cash non-custodial credit card with cashback, "The Club" membership tier program, and an AVS operator stack that runs services on EigenLayer, Symbiotic, and Karak. The protocol is governed by the ETHFI token via governance.ether.fi. ether.fi has no public REST API or developer SDK — its public surface is on-chain: open-source Solidity smart contracts on Ethereum mainnet (eETH, weETH, LiquidityPool, EtherFiNodesManager,
  EtherFiOracle, MembershipManager, ETHFI), cross-chain bridge contracts (weETH-cross-chain via LayerZero, ETHFI via Wormhole NTT), AVS operator contracts, plus operator tooling (etherfi-avs-operator, eigenpod-proofs-generation) and a public subgraph indexing protocol events. ether.fi is one of the largest LRT protocols by TVL with deep integrations across Aave, Pendle, Gearbox, Morpho, and other DeFi venues.'
features:
- Non-custodial Ethereum liquid restaking — stakers retain validator keys
- eETH rebasing liquid restaking token (LRT)
- weETH non-rebasing ERC-20 wrapped version of eETH used across DeFi
- eBTC Bitcoin restaking token
- eUSD stablecoin restaking token
- Liquid auto-balancing strategy vaults
- ether.fi Cash non-custodial Visa credit card with cashback
- The Club tiered membership and financial services program
- Native restaking integration with EigenLayer, Symbiotic, and Karak
- AVS operator infrastructure (etherfi-avs-operator) running services on top of restaked ETH
- Cross-chain weETH via LayerZero on Arbitrum, Optimism, Base, Linea, Mode, Scroll, BNB Chain, Blast, Mantle, Solana
- ETHFI governance token (cross-chain via Wormhole NTT)
- Membership NFTs and loyalty points program
- Distributed Validator Technology (DVT) via SSV Network
- EigenPod proof generation tooling (Go)
- EtherFiOracle off-chain oracle for validator state and rewards
- Public subgraph indexing protocol contract events
- Deep DeFi integrations with Aave, Pendle, Gearbox, Morpho, Curve, Balancer, Uniswap
- Audited by CertiK, Certora, Hats Finance, Nethermind, Omniscia, Solidified
- Open-source under MIT license on GitHub (etherfi-protocol)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/etherfi.png
layout: provider
modified: '2026-05-24'
name: ether.fi
nav: Providers
network: true
overview: 'ether.fi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Ethereum, Liquid Restaking, Liquid Staking, Restaking, and LRT.


  ether.fi''s developer surface includes documentation, engineering blog, and 23 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.7
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etherfi/refs/heads/main/screenshots/etherfi-2026-06-20T180837.png
security:
- kind: domain-security
  name: Etherfi Domain Security
  slug: etherfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: etherfi
tags:
- Ethereum
- Liquid Restaking
- Liquid Staking
- Restaking
- LRT
- EigenLayer
- Symbiotic
- Karak
- DeFi
- Smart Contracts
- eETH
- weETH
- eBTC
- eUSD
- ETHFI
- AVS
- LayerZero
- Cross-Chain
- Cash Card
- Liquid Vaults
- Open Source
website: https://www.ether.fi
---
