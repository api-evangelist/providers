---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Arbiscan Agentic Access
  operation_count: 1
  slug: arbiscan-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.etherscan.io/v2/api
  baseurl_source: declared
  description: Address balances, transactions, token holdings, and funding origins
  name: Arbiscan Accounts API
  slug: arbiscan-accounts-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arbiscan Accounts API
  slug: open-arbiscan-accounts-api
- collection_type: open
  name: Arbiscan Accounts Blocks API
  slug: open-arbiscan-blocks-api
- collection_type: open
  name: Arbiscan Accounts Contracts API
  slug: open-arbiscan-contracts-api
- collection_type: open
  name: Arbiscan Accounts Gas Tracker API
  slug: open-arbiscan-gas-tracker-api
- collection_type: open
  name: Arbiscan Accounts Logs API
  slug: open-arbiscan-logs-api
- collection_type: open
  name: Arbiscan Accounts Stats API
  slug: open-arbiscan-stats-api
- collection_type: open
  name: Arbiscan Accounts Tokens API
  slug: open-arbiscan-tokens-api
- collection_type: open
  name: Arbiscan Accounts Transactions API
  slug: open-arbiscan-transactions-api
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
overview: 'Arbiscan publishes 1 API on the [APIs.io](https://apis.io/) network: Accounts API. Tagged areas include Blockchain, Cryptocurrency, Arbitrum, Layer 2, and EVM.


  The Arbiscan catalog on APIs.io includes 1 JSON-LD context.


  Arbiscan''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, and 6 more developer resources.'
plans:
- name: Arbiscan Plans Pricing
  plan_count: 7
  slug: arbiscan-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 14
  name: Arbiscan Rate Limits
  slug: arbiscan-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 77.0
    catalog_earned_first_party: 0.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 15.2
    contract_quality: 61.9
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 15.2
    operational_transparency: 34.2
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
