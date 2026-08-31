---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://blockfi.com/
- group: company
  title: ''
  type: Blog
  url: https://blockfi.com/category/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://blockfi.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://blockfi.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blockfi.com/category/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blockfi.com/privacy/
- group: commercial
  title: ''
  type: Licenses
  url: https://blockfi.com/licenses/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/BlockFi
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/blockfi_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockfi-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/blockfi-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blockfi-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blockfi-llms.txt
coverage:
  checked: '2026-08-07'
  detail: BlockFi is a Chapter 11 wind-down estate, not an operating company - blockfi.com is a noindex WordPress notice site whose newest post is a 2025 distribution deadline, the historical api.blockfi.com host and every other developer, docs and app subdomain have been removed from DNS, and the company GitHub organization returns zero public repositories.
  evidence:
  - status: 200
    url: https://blockfi.com/
  - status: 404
    url: https://blockfi.com/openapi.json
  - status: 404
    url: https://blockfi.com/llms.txt
  - status: 404
    url: https://blockfi.com/.well-known/agent-card.json
  - status: 404
    url: https://blockfi.com/.well-known/security.txt
  - status: 404
    url: https://blockfi.com/developers
  - status: 200
    url: https://api.github.com/orgs/blockfi/repos
  reason: defunct
  state: none
created: '2026-08-07'
description: 'BlockFi was a Jersey City, New Jersey crypto-financial-services company founded in 2017 by Zac Prince and Flori Marquez that offered retail and institutional clients interest-bearing crypto accounts (the BlockFi Interest Account), USD loans collateralized by bitcoin and other digital assets, spot trading, and a bitcoin-rewards credit card, growing on a USD 350 million Series D in March 2021 that valued it at roughly USD 3 billion. The company filed for Chapter 11 bankruptcy protection in November 2022 in the wake of the FTX and Alameda Research collapse, and emerged in October 2023 not as an operating business but as a wind-down estate. Its customer web platform and mobile apps have been shut down, in-kind crypto distributions are administered through Coinbase and cash distributions through Kroll Restructuring Administration and Digital Disbursements, and blockfi.com is now a WordPress notice site carrying noindex/nofollow and dated estate updates rather than a product. There
  is no operating developer program: api.blockfi.com and every other developer, docs and app subdomain no longer resolve in DNS, the company GitHub organization holds zero public repositories, and no OpenAPI, GraphQL, AsyncAPI, MCP or agent-card document is served from any surviving BlockFi host.'
image: https://avatars.githubusercontent.com/u/38138582?v=4
layout: provider
modified: '2026-08-07'
name: BlockFi
nav: Providers
network: true
overview: 'BlockFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Digital Assets, Crypto Lending, and Financial-Services.


  BlockFi''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockfi/refs/heads/main/screenshots/blockfi-2026-08-07T162629.png
security:
- kind: domain-security
  name: Blockfi Domain Security
  slug: blockfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockfi
tags:
- Company
- Cryptocurrency
- Digital Assets
- Crypto Lending
- Financial-Services
- Fintech
- Blockchain
- Bankruptcy Estate
- Defunct
- United States
website: https://blockfi.com/
---
