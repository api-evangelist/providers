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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Arbiscan Agentic Access
  operation_count: 1
  slug: arbiscan-agentic-access
  summary_line: 1 operation
api_count: 8
apis:
- description: Address balances, transactions, token holdings, and funding origins
  name: Arbiscan Accounts API
  slug: arbiscan-accounts-api
- description: Block details, rewards, countdown, and block-by-timestamp lookup
  name: Arbiscan Blocks API
  slug: arbiscan-blocks-api
- description: Smart contract source code, ABI, creation info, and verification
  name: Arbiscan Contracts API
  slug: arbiscan-contracts-api
- description: Arbitrum One gas oracle and gas price estimates
  name: Arbiscan Gas Tracker API
  slug: arbiscan-gas-tracker-api
- description: Event log queries by address, topic, and block range
  name: Arbiscan Logs API
  slug: arbiscan-logs-api
- description: Arbitrum One network statistics, supply data, and daily metrics
  name: Arbiscan Stats API
  slug: arbiscan-stats-api
- description: ERC-20, ERC-721, and ERC-1155 token supply, holders, and metadata
  name: Arbiscan Tokens API
  slug: arbiscan-tokens-api
- description: Transaction status, receipts, counts, and advanced filtering
  name: Arbiscan Transactions API
  slug: arbiscan-transactions-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arbiscan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arbiscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arbiscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arbiscan-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://arbiscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arbiscan.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://arbiscan.io/apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arbiscan.io/apiterms
- group: start
  title: ''
  type: Signup
  url: https://arbiscan.io/myapikey
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.etherscan.io/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arbiscan
created: '2026-06-13'
description: Arbiscan is the official blockchain explorer, search, API, and analytics platform for Arbitrum One, the leading Ethereum Layer 2 scaling network. It enables developers and users to query Arbitrum One transaction histories, token transfers (ERC-20, ERC-721, ERC-1155), smart contract source code and ABIs, block data, and L2 network statistics. The Arbiscan API is part of the Etherscan unified V2 platform, accessible across 60+ EVM-compatible chains with a single API key. A free tier provides 100,000 daily calls at 3 requests per second; paid tiers scale up to enterprise with unmetered access.
finops:
- name: Arbiscan Finops
  service_category: API
  slug: arbiscan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arbiscan.png
jsonld:
- class_count: 48
  name: Arbiscan Context
  property_count: 6
  slug: arbiscan-context
layout: provider
modified: '2026-06-13'
name: Arbiscan
nav: Providers
network: true
overview: 'Arbiscan publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Contracts API, and 5 more. Tagged areas include Blockchain, Cryptocurrency, Arbitrum, Layer 2, and EVM.


  The Arbiscan catalog on APIs.io includes 1 JSON-LD context.


  Arbiscan''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, and 6 more developer resources.'
plans:
- name: Arbiscan Plans Pricing
  plan_count: 7
  slug: arbiscan-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 14
  name: Arbiscan Rate Limits
  slug: arbiscan-rate-limits
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.5
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arbiscan/refs/heads/main/screenshots/arbiscan-2026-06-20T172358.png
security:
- kind: authentication
  name: Arbiscan Authentication
  slug: arbiscan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Arbiscan Domain Security
  slug: arbiscan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Arbiscan Vulnerability Disclosure
  slug: arbiscan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: arbiscan
tags:
- Blockchain
- Cryptocurrency
- Arbitrum
- Layer 2
- EVM
- Web3
- L2
website: https://arbiscan.io/
---
