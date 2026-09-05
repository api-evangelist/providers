---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 6
apis:
- description: Core REST API for managing Tenderly projects including smart contract simulations, alerts, Web3 Actions, contract management, wallet tracking, and virtual test environments.
  name: Tenderly REST API
  slug: tenderly-rest-api
- description: Dry-run Ethereum and EVM transactions before execution to preview outcomes including asset and balance changes, gas estimates, decoded traces, state diffs, and human-readable error messages across 100
  name: Tenderly Simulation API
  slug: tenderly-simulation-api
- description: Provision and manage production-mirroring virtual blockchain environments with state sync, unlimited faucets, cheatcodes, cross-chain bridge simulation, and a shareable block explorer for safe dapp de
  name: Tenderly Virtual TestNets REST API
  slug: tenderly-virtual-testnets-rest-api
- description: Production-grade JSON-RPC node infrastructure supporting 80+ EVM networks including Ethereum, Arbitrum, Optimism, Polygon, Base, BSC, and Avalanche with built-in simulation, smart multi-region routing
  name: Tenderly Node RPC
  slug: tenderly-node-rpc
- description: Configure real-time on-chain event monitoring for smart contracts and wallets, and route alert notifications to email, Slack, Discord, webhooks, PagerDuty, and Web3 Actions.
  name: Tenderly Alerts API
  slug: tenderly-alerts-api
- description: Deploy and manage serverless JavaScript/TypeScript functions triggered by on-chain or off-chain events, enabling custom monitoring automation, incident response, and backend integrations without manag
  name: Tenderly Web3 Actions API
  slug: tenderly-web3-actions-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenderly-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://tenderly.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenderly.co
- group: commercial
  title: ''
  type: Pricing
  url: https://tenderly.co/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://docs.tenderly.co/tenderly-plans
- group: start
  title: ''
  type: Signup
  url: https://dashboard.tenderly.co/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.tenderly.co/login
- group: company
  title: ''
  type: Blog
  url: https://blog.tenderly.co
- group: operate
  title: ''
  type: Status
  url: https://status.tenderly.co
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tenderly
- group: build
  title: ''
  type: CLI
  url: https://github.com/Tenderly/tenderly-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tenderly/tenderly-docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tenderly.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tenderly.co/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://tenderly.co/contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TenderlyApp
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/fBvDJYR
- group: auth
  title: ''
  type: Authentication
  url: https://docs.tenderly.co/other/platform-access/how-to-generate-api-access-tokens
created: '2026-06-13'
description: Tenderly is a Web3 development platform offering smart contract debugging, transaction simulation, virtual test environments, node RPC infrastructure, alerting, Web3 Actions serverless functions, and gas profiling across 80+ EVM-compatible blockchain networks.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tenderly.png
layout: provider
modified: '2026-06-13'
name: Tenderly
nav: Providers
network: true
overview: 'Tenderly publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Web3, Blockchain, Smart Contracts, Ethereum, and EVM.


  Tenderly''s developer surface includes developer portal, documentation, pricing, signup flow, engineering blog, status page, GitHub presence, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 10
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 39.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenderly/refs/heads/main/screenshots/tenderly-2026-06-20T195106.png
security:
- kind: domain-security
  name: Tenderly Domain Security
  slug: tenderly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tenderly
tags:
- Web3
- Blockchain
- Smart Contracts
- Ethereum
- EVM
- Debugging
- Simulation
- Developer Tools
website: https://tenderly.co
---
