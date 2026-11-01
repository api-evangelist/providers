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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: InfinitySwap provides a Layer‑2 EVM compatible API for developers, documented at the Bitfinity network docs site.
  name: InfinitySwap API
  slug: infinityswap-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/infinityswap-one/hosts/infinityswap-one-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infinityswap-one-hosts.yml
- group: other
  href: https://artifacts.apis.io/infinityswap-one/vendors/infinityswap-one-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infinityswap-one-vendors.yml
- group: build
  href: https://artifacts.apis.io/infinityswap-one/packages/infinityswap-one-packages.yml
  title: ''
  type: SDKs
  url: packages/infinityswap-one-packages.yml
- group: build
  href: https://artifacts.apis.io/infinityswap-one/packages/infinityswap-one-packages.yml
  title: ''
  type: Packages
  url: packages/infinityswap-one-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blog.bitfinity.network/privacy-vs-regulatory-compliance-examining-the-tension-between-privacy-and-regulatory-requirements/
- group: auth
  href: https://artifacts.apis.io/infinityswap-one/security/infinityswap-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infinityswap-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infinityswap.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitfinity.network/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bitfinity.network/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitfinity.network/getting-started/starting-with-development
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blog.bitfinity.network/tag/developers/
- group: company
  title: ''
  type: Blog
  url: https://www.blog.bitfinity.network/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitfinity-network
coverage:
  checked: '2026-10-30'
  detail: Docs are served as a JavaScript‑rendered site with no direct OpenAPI file, only interactive pages.
  evidence:
  - status: 404
    url: https://docs.bitfinity.network/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: InfinitySwap is a blockchain infrastructure provider operating under the Bitfinity network, offering a Layer‑2 EVM compatible solution that bridges Bitcoin and Ethereum ecosystems. It enables developers to build, test, and deploy smart contracts with fast finality and low fees, while providing comprehensive documentation, developer portals, and community resources. The platform supports token bridging, DeFi applications, and NFT projects, aiming to expand Bitcoin’s utility through scalable EVM capabilities.
image: https://storage.ghost.io/c/16/95/169585d7-b6fd-49d7-9dd2-9723e632aa0a/content/images/size/w1200/2023/04/cover-bg.webp
layout: provider
modified: '2026-10-28'
name: InfinitySwap
nav: Providers
network: true
overview: 'InfinitySwap is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Infrastructure, EVM, and Layer2.


  InfinitySwap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Infinityswap One Domain Security
  slug: infinityswap-one-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: infinityswap-one
tags:
- Company
- Blockchain
- Infrastructure
- EVM
- Layer2
website: https://infinityswap.one
---
