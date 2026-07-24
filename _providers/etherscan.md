---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Etherscan Agentic Access
  operation_count: 1
  slug: etherscan-agentic-access
  summary_line: 1 operation
api_count: 7
apis:
- description: Address balances, transactions, and token holdings
  name: Etherscan Accounts API
  slug: etherscan-accounts-api
- description: Block details, rewards, and uncles
  name: Etherscan Blocks API
  slug: etherscan-blocks-api
- description: Smart contract source, ABI, and verification
  name: Etherscan Contracts API
  slug: etherscan-contracts-api
- description: Network gas oracle and gas price estimates
  name: Etherscan Gas Tracker API
  slug: etherscan-gas-tracker-api
- description: Network and supply statistics
  name: Etherscan Stats API
  slug: etherscan-stats-api
- description: ERC-20, ERC-721, and ERC-1155 token data
  name: Etherscan Tokens API
  slug: etherscan-tokens-api
- description: Transaction status and receipts
  name: Etherscan Transactions API
  slug: etherscan-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: Etherscan API
  slug: open-etherscan
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/etherscan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/etherscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etherscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/etherscan-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etherscan
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/etherscan
- group: start
  title: ''
  type: Portal
  url: https://etherscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.etherscan.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://etherscan.io/apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://etherscan.io/apiterms
- group: start
  title: ''
  type: Signup
  url: https://etherscan.io/myapikey
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.etherscan.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/etherscan-blog
created: '2025-02-17'
description: Etherscan is the leading blockchain explorer, search, API, and analytics platform for Ethereum and other EVM-compatible chains. It allows users to easily access and explore blockchain data, including transaction histories, smart contracts, token balances, and network activity. Etherscan's unified V2 API covers 60+ chains under a single account and API key, with a free tier offering 100,000 daily calls and paid tiers up to enterprise.
finops:
- name: Etherscan Finops
  service_category: API
  slug: etherscan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/etherscan.png
layout: provider
modified: '2026-05-19'
name: Etherscan
nav: Providers
network: true
overview: 'Etherscan publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Contracts API, and 4 more. Tagged areas include Blockchain, Cryptocurrency, Ethereum, EVM, and Web3.


  Etherscan''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Etherscan Plans Pricing
  plan_count: 3
  slug: etherscan-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Etherscan Rate Limits
  slug: etherscan-rate-limits
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etherscan/refs/heads/main/screenshots/etherscan-2026-06-20T180843.png
security:
- kind: authentication
  name: Etherscan Authentication
  slug: etherscan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Etherscan Domain Security
  slug: etherscan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Etherscan Vulnerability Disclosure
  slug: etherscan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: etherscan
tags:
- Blockchain
- Cryptocurrency
- Ethereum
- EVM
- Web3
website: https://etherscan.io/
---
