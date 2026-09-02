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
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Etherscan Agentic Access
  operation_count: 1
  slug: etherscan-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Address balances, transactions, and token holdings
  name: Etherscan Accounts API
  slug: etherscan-accounts-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Etherscan Accounts API
  slug: open-etherscan-accounts-api
- collection_type: open
  name: Etherscan Accounts Blocks API
  slug: open-etherscan-blocks-api
- collection_type: open
  name: Etherscan Accounts Contracts API
  slug: open-etherscan-contracts-api
- collection_type: open
  name: Etherscan Accounts Gas Tracker API
  slug: open-etherscan-gas-tracker-api
- collection_type: open
  name: Etherscan Accounts Stats API
  slug: open-etherscan-stats-api
- collection_type: open
  name: Etherscan Accounts Tokens API
  slug: open-etherscan-tokens-api
- collection_type: open
  name: Etherscan Accounts Transactions API
  slug: open-etherscan-transactions-api
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
overview: 'Etherscan publishes 1 API on the [APIs.io](https://apis.io/) network: Accounts API. Tagged areas include Blockchain, Cryptocurrency, Ethereum, EVM, and Web3.


  Etherscan''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Etherscan Plans Pricing
  plan_count: 3
  slug: etherscan-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Etherscan Rate Limits
  slug: etherscan-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
