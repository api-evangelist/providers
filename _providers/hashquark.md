---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Institutional staking API to onboard broker users, generate and track deposits, assign/exit validators, drive pooled staking and Babylon BTC staking across supported proof-of-stake protocols. Authenti
  name: HashKey Cloud Staking API
  slug: hashkey-cloud-staking-api
- description: Reporting API for node status and staking reward data (daily, monthly, quarterly and annual rewards) for integrated staking users. Shares the Quark-Keccak256-ECDSA authentication and the {code,msg,dat
  name: HashKey Cloud Data API
  slug: hashkey-cloud-data-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashquark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hashkey.cloud
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hashkeycloud.gitbook.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://hashkeycloud.gitbook.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hashkeycloud.gitbook.io/docs/api/data-api/api-specs
- group: start
  title: ''
  type: GettingStarted
  url: https://hashkeycloud.gitbook.io/docs/api/staking-api/get-started
- group: company
  title: ''
  type: Blog
  url: https://hashkeycloud.medium.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashquark-staking
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://group.hashkey.com/en/privacy-policy
- group: other
  title: ''
  type: X
  url: https://twitter.com/HashKeyCloud
- group: auth
  title: ''
  type: Authentication
  url: authentication/hashquark-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hashquark-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hashquark-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/hashquark-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hashquark-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hashquark-llms.txt
created: '2026-07-17'
description: 'HashKey Cloud, formerly HashQuark, is a Hong Kong-based blockchain infrastructure and Web3 staking provider (part of HashKey Group) that runs enterprise-grade validator nodes across 50+ mainstream proof-of-stake public chains including Ethereum, Cosmos, Solana, Polkadot, Avalanche, Sui and BNB Chain. It exposes a developer platform for institutional staking: a Staking API to onboard users, generate deposits, assign and exit validators and drive pooled staking; a Data API to track node status and daily/monthly/quarterly/ annual reward data; plus a dashboard, a Babylon BTC staking flow and a first-party Go SDK. Requests are authenticated with a custom Quark-Keccak256-ECDSA request-signing scheme keyed to an Ethereum keypair. Originally added to the API Evangelist network as a portfolio-lead stub (surfaced via Qiming), now enriched from HashKey Cloud''s public developer surface.'
image: https://avatars.githubusercontent.com/u/138440702?v=4
layout: provider
modified: '2026-07-19'
name: HashKey Cloud (HashQuark)
nav: Providers
network: true
overview: 'HashKey Cloud (HashQuark) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Staking, Web3, and Validators.


  HashKey Cloud (HashQuark)''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 21.6
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hashquark/refs/heads/main/screenshots/hashquark-2026-07-25T220753.png
security:
- kind: authentication
  name: Hashquark Authentication
  slug: hashquark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hashquark Domain Security
  slug: hashquark-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: hashquark
tags:
- Company
- Blockchain
- Staking
- Web3
- Validators
- Cryptocurrency
- Node Infrastructure
- Proof of Stake
- Ethereum
- DeFi
website: https://www.hashkey.cloud
---
