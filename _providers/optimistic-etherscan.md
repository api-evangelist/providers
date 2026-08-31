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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Optimistic Etherscan Agentic Access
  operation_count: 1
  slug: optimistic-etherscan-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Address balances, transaction lists, and token holdings on OP Mainnet
  name: Optimism Etherscan Accounts API
  slug: optimistic-etherscan-accounts-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Optimism Etherscan Accounts API
  slug: open-optimistic-etherscan-accounts-api
- collection_type: open
  name: Optimism Etherscan Accounts Blocks API
  slug: open-optimistic-etherscan-blocks-api
- collection_type: open
  name: Optimism Etherscan Accounts Contracts API
  slug: open-optimistic-etherscan-contracts-api
- collection_type: open
  name: Optimism Etherscan Accounts Geth Proxy API
  slug: open-optimistic-etherscan-geth-proxy-api
- collection_type: open
  name: Optimism Etherscan Accounts Stats API
  slug: open-optimistic-etherscan-stats-api
- collection_type: open
  name: Optimism Etherscan Accounts Tokens API
  slug: open-optimistic-etherscan-tokens-api
- collection_type: open
  name: Optimism Etherscan Accounts Transactions API
  slug: open-optimistic-etherscan-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optimistic-etherscan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optimistic-etherscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimistic-etherscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optimistic-etherscan-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://optimistic.etherscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.optimism.etherscan.io/
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
  url: https://optimistic.etherscan.io/myapikey
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.optimism.etherscan.io/support/rate-limits
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.etherscan.io/llms.txt
- group: start
  title: ''
  type: Sandbox
  url: https://docs.optimism.etherscan.io/optimism-sepolia-etherscan
created: '2026-06-13'
description: Optimism Etherscan is the official blockchain explorer and API platform for the Optimism L2 network (OP Mainnet, chain ID 10). It provides REST APIs for querying Optimism transactions, token events, smart contract source code, account balances, block data, and OP Mainnet statistics. API subscriptions have migrated to Etherscan API V2, enabling a single API key to access Optimism alongside 60+ EVM chains. The free tier covers select chains with 3 calls/second and 100,000 calls/day; paid plans start at $49/month for full multichain access.
finops:
- name: Optimistic Etherscan Finops
  service_category: API
  slug: optimistic-etherscan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimistic-etherscan.png
jsonld:
- class_count: 0
  name: Optimistic Etherscan Context
  property_count: 39
  slug: optimistic-etherscan-context
layout: provider
modified: '2026-06-13'
name: Optimism Etherscan
nav: Providers
network: true
overview: 'Optimism Etherscan publishes 1 API on the [APIs.io](https://apis.io/) network: Accounts API. Tagged areas include Blockchain, Optimism, Layer 2, Ethereum, and EVM.


  The Optimism Etherscan catalog on APIs.io includes 1 JSON-LD context.


  Optimism Etherscan''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, sandbox, and 6 more developer resources.'
plans:
- name: Optimistic Etherscan Plans Pricing
  plan_count: 7
  slug: optimistic-etherscan-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 13
  name: Optimistic Etherscan Rate Limits
  slug: optimistic-etherscan-rate-limits
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 38.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 15.2
    contract_quality: 61.9
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 15.2
    operational_transparency: 31.6
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optimistic-etherscan/refs/heads/main/screenshots/optimistic-etherscan-2026-08-17T124250.png
security:
- kind: authentication
  name: Optimistic Etherscan Authentication
  slug: optimistic-etherscan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Optimistic Etherscan Domain Security
  slug: optimistic-etherscan-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optimistic Etherscan Vulnerability Disclosure
  slug: optimistic-etherscan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: optimistic-etherscan
tags:
- Blockchain
- Optimism
- Layer 2
- Ethereum
- EVM
- Web3
- Cryptocurrency
website: https://optimistic.etherscan.io/
---
