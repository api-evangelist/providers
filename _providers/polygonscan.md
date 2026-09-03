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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Polygonscan Agentic Access
  operation_count: 1
  slug: polygonscan-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.etherscan.io/v2/api
  baseurl_source: declared
  description: The API API from PolygonScan — 1 operation(s) for api.
  name: PolygonScan API API
  slug: polygonscan-api-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PolygonScan API API
  slug: open-polygonscan-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polygonscan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/polygonscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polygonscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polygonscan-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://polygonscan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.etherscan.io/etherscan-v2
- group: start
  title: ''
  type: Signup
  url: https://polygonscan.com/register
- group: start
  title: ''
  type: Login
  url: https://polygonscan.com/login
- group: company
  title: ''
  type: Blog
  url: https://polygonscan.com/blogs
- group: operate
  title: ''
  type: Status
  url: https://etherscan.freshstatus.io/
- group: commercial
  title: ''
  type: Terms
  url: https://polygonscan.com/terms
- group: commercial
  title: ''
  type: Privacy
  url: https://polygonscan.com/privacypolicy
- group: operate
  title: ''
  type: Contact
  url: https://polygonscan.com/contactus
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/polygonscan
created: '2026-06-13'
description: PolygonScan is the leading blockchain explorer, search, API, and analytics platform for the Polygon PoS network. It provides a REST API for querying transactions, token transfers, smart contract source code, ERC-20/ERC-721/ERC-1155 balances, gas prices, and network statistics on the Polygon blockchain (Chain ID 137). API access is unified under Etherscan API V2, enabling access with a single API key across 60+ EVM-compatible chains.
examples:
- key_count: 5
  name: Get Balance
  slug: get-balance
- key_count: 5
  name: Get Contract Abi
  slug: get-contract-abi
- key_count: 5
  name: Get Gas Oracle
  slug: get-gas-oracle
- key_count: 5
  name: Get Transactions
  slug: get-transactions
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://polygonscan.com/images/svg/brands/main.svg?v=24.1.2.0
json_schemas:
- name: PolygonScan API Response
  property_count: 3
  slug: api-response
layout: provider
modified: '2026-06-13'
name: PolygonScan
nav: Providers
network: true
overview: 'PolygonScan publishes 1 API on the [APIs.io](https://apis.io/) network: API API. Tagged areas include Blockchain, Polygon, Explorer, Web3, and EVM.


  The PolygonScan catalog on APIs.io includes 1 Spectral governance ruleset.


  PolygonScan''s developer surface includes authentication, documentation, signup flow, engineering blog, status page, terms of service, privacy policy, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 0
rate_limits:
- limit_count: 7
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: PolygonScan API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: polygonscan-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 9.8
    contract_quality: 51.0
    developer_ergonomics: 11.9
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polygonscan/refs/heads/main/screenshots/polygonscan-2026-06-20T191911.png
security:
- kind: authentication
  name: Polygonscan Authentication
  slug: polygonscan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Polygonscan Domain Security
  slug: polygonscan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Polygonscan Vulnerability Disclosure
  slug: polygonscan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: polygonscan
tags:
- Blockchain
- Polygon
- Explorer
- Web3
- EVM
- Smart Contracts
- DeFi
- Cryptocurrency
website: https://polygonscan.com/
---
