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
  band: human-only
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Public HTTP gateway that serves signed data packages and historical token prices aggregated by the RedStone oracle network. Read-only and unauthenticated; responses carry ECDSA signatures and the prov
  name: RedStone Cache / Price API
  slug: redstone-cache-price-api
- description: Production data-package gateway exposing the latest signed data packages per data-service (e.g. redstone-primary-prod) for the Pull model and SDK consumption.
  name: RedStone Oracle Gateway
  slug: redstone-oracle-gateway
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.redstone.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.redstone.finance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redstone.finance
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redstone.finance/docs/category/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.redstone.finance
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redstone-finance
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/redstone
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redstone.finance/documents/RedStone---Privacy-Policy.pdf
- group: build
  title: ''
  type: Packages
  url: packages/redstone-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/redstone-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/redstone-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redstone-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redstone-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/redstone-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redstone-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redstone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/redstone-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/redstone-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redstone-llms.txt
created: '2026-07-17'
description: 'RedStone is a modular blockchain oracle infrastructure provider delivering tamper-proof price feeds and off-chain data to smart contracts across 100+ EVM and non-EVM networks. It aggregates data from 20+ centralized and decentralized exchanges, signs each data package with the provider''s key, and delivers it through three models: Pull (Core, on-demand data injected into a transaction via the EVM connector), Push (on-chain relayers that write prices to a feed contract), and a Hybrid ERC-7412 flow. RedStone also runs a public HTTP cache/gateway API for reading signed data packages and historical prices, publishes SDKs (TypeScript, Rust), chain connectors (EVM, Starknet, TON, Fuel, Radix, Casper), a CLI, and on-chain example contracts. It secures billions of dollars of value for 200+ DeFi protocols and supports Proof of Reserve and MEV-resistant (OEV) products.'
image: https://cdn.prod.website-files.com/67519197ce9eaef4601a6287/677f9f8bb6ae73e45b28a6fb_Variant2%20(3).png
layout: provider
modified: '2026-07-21'
name: RedStone
nav: Providers
network: true
overview: 'RedStone publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Blockchain, Oracle, and DeFi.


  RedStone''s developer surface includes documentation, getting-started guide, engineering blog, support, CLI, authentication, and 13 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 24.3
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redstone/refs/heads/main/screenshots/redstone-2026-09-02T153202.png
security:
- kind: authentication
  name: Redstone Authentication
  slug: redstone-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Redstone Domain Security
  slug: redstone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Redstone Vulnerability Disclosure
  slug: redstone-vulnerability-disclosure
  summary_line: disclosure policy published
slug: redstone
tags:
- Company
- Infrastructure
- Blockchain
- Oracle
- DeFi
- Price Feeds
- Data
- Web3
- Smart Contracts
website: https://www.redstone.finance
---
