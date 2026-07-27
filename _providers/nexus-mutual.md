---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nexus Mutual Agentic Access
  operation_count: 6
  slug: nexus-mutual-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: The Capacity API from Nexus Mutual — 4 operation(s) for capacity.
  name: Nexus Mutual Capacity API
  slug: nexus-mutual-capacity-api
- description: The Pricing API from Nexus Mutual — 1 operation(s) for pricing.
  name: Nexus Mutual Pricing API
  slug: nexus-mutual-pricing-api
- description: The Quote API from Nexus Mutual — 1 operation(s) for quote.
  name: Nexus Mutual Quote API
  slug: nexus-mutual-quote-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexus-mutual-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexus-mutual-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://nexusmutual.io/plans/
- group: operate
  title: ''
  type: RateLimits
  url: https://nexusmutual.io/rate-limits/
- group: commercial
  title: ''
  type: FinOps
  url: https://nexusmutual.io/finops/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NexusMutual
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://v2.nexusmutual.io/assets/Privacy-Policy.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://v2.nexusmutual.io/assets/Terms-of-Use.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://dune.com/nexus_mutual
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexusmutual.io/
- group: build
  title: ''
  type: SDKs
  url: https://sdk.nexusmutual.io/
- group: auth
  title: ''
  type: BugBounty
  url: https://immunefi.com/bounty/nexusmutual/
- group: auth
  title: ''
  type: Security
  url: https://docs.nexusmutual.io/resources/audits-and-security/
- group: other
  title: ''
  type: DataAnalytics
  url: https://dune.com/nexus_mutual
- group: other
  title: ''
  type: Application
  url: https://app.nexusmutual.io/
- group: company
  title: ''
  type: Blog
  url: https://nexusmutual.io/blog
created: '2019-01-01'
description: Nexus Mutual is a decentralized insurance protocol built on Ethereum that enables members to share risk through a discretionary mutual structure. Since 2019 it has provided over 10,000 covers protecting more than $6 billion in crypto assets against smart contract hacks, custody failure, slashing events, depeg occurrences, and bespoke protocol risks. The public Cover Router REST API exposes endpoints for querying quote pricing, per-product and per-pool capacity, and the full product catalogue, enabling third-party frontends and integrators to build point-of-sale cover purchase flows on top of the Nexus Mutual protocol.
examples:
- key_count: 3
  name: Get Capacity All Products
  slug: get-capacity-all-products
- key_count: 3
  name: Get Pool Capacity
  slug: get-pool-capacity
- key_count: 3
  name: Get Pricing
  slug: get-pricing
- key_count: 3
  name: Get Product Capacity
  slug: get-product-capacity
- key_count: 3
  name: Get Quote
  slug: get-quote
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Nexus Mutual exposes on-chain protocol data through a community-maintained subgraph
  name: Nexus Mutual GraphQL (The Graph Subgraph)
  slug: nexus-mutual-graphql
image: https://nexusmutual.io/favicon.ico
json_schemas:
- name: CapacityResult
  property_count: 5
  slug: CapacityResult
- name: PricingResult
  property_count: 3
  slug: PricingResult
- name: QuoteResponse
  property_count: 1
  slug: QuoteResponse
jsonld:
- class_count: 0
  name: context Context
  property_count: 35
  slug: context
layout: provider
modified: '2026-06-14'
name: Nexus Mutual
nav: Providers
network: true
overview: 'Nexus Mutual publishes 3 APIs on the [APIs.io](https://apis.io/) network: Capacity API, Pricing API, and Quote API. Tagged areas include Decentralized Insurance, DeFi, Ethereum, Smart Contract Cover, and Crypto Insurance.


  The Nexus Mutual catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nexus Mutual''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 48
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Nexus Mutual API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nexus-mutual-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.4
    developer_ergonomics: 17.4
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 47.2
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 41.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexus-mutual/refs/heads/main/screenshots/nexus-mutual-2026-06-20T190302.png
security:
- kind: domain-security
  name: Nexus Mutual Domain Security
  slug: nexus-mutual-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nexus-mutual
tags:
- Decentralized Insurance
- DeFi
- Ethereum
- Smart Contract Cover
- Crypto Insurance
- Protocol Protection
- Staking
- Claims
website: https://nexusmutual.io
---
