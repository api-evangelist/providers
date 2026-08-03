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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.level.money/
- group: docs
  title: ''
  type: Documentation
  url: https://level-money.gitbook.io/level-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://level-money.gitbook.io/level-documentation/user-guides/how-to-get-lvlusd
- group: other
  title: ''
  type: Application
  url: https://app.level.money/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/levelusd
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Level-Money
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Level-Money/contracts
- group: commercial
  title: ''
  type: TermsOfService
  url: https://level-money.gitbook.io/level-documentation/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://level-money.gitbook.io/level-documentation/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://level-money.gitbook.io/level-documentation/technical-documentation/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/level-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/level-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/level-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/level-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/level-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/level-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/level-conformance.yml
created: '2026-07-17'
description: 'Level is a stablecoin protocol that issued lvlUSD, a stablecoin fully backed by USDC and USDT which were deployed into blue-chip lending protocols (Aave and the Morpho Steakhouse USDC vault) to generate yield. Lending yield was passed back to holders through an ERC-4626 staking mechanism: lvlUSD could be staked for slvlUSD, a yield-accruing token that appreciates as the protocol distributes yield into the staking contract. Both tokens were transferable and integrated across DeFi venues including Morpho, Pendle, Spectra and Curve, with LayerZero OFT adapters bridging them to Base. Level exposes no public HTTP API — its programmable surface is a set of audited Ethereum mainnet smart contracts (lvlUSD, slvlUSD, LevelMinting, LevelStakingPool, LevelUsdPointsFarm, LevelReserveLens) documented in GitBook and published on GitHub. In September 2025 the team announced it was joining the Sky (fka MakerDAO) ecosystem as part of Grove and that the Level protocol is being sunset: mints
  paused, redemptions made public and fixed 1:1, cooldowns cut to two seconds, final yield distribution on 2025-10-02, and the front end retired on 2025-12-15 with contract-level redemption remaining available indefinitely.'
image: https://www.level.money/favicon.ico
layout: provider
modified: '2026-07-19'
name: Level
nav: Providers
network: true
overview: 'Level is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stablecoins, DeFi, Cryptocurrency, and Financial Services.


  Level''s developer surface includes documentation, getting-started guide, support, and 14 more developer resources.'
random_paper: 61
score:
  band: emerging
  composite: 20.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 20.4
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/level/refs/heads/main/screenshots/level-2026-07-25T224942.png
security:
- kind: domain-security
  name: Level Domain Security
  slug: level-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Level Vulnerability Disclosure
  slug: level-vulnerability-disclosure
  summary_line: disclosure policy published
slug: level
tags:
- Company
- Stablecoins
- DeFi
- Cryptocurrency
- Financial Services
- Blockchain
- Ethereum
- Smart Contracts
- Yield
website: https://www.level.money/
---
