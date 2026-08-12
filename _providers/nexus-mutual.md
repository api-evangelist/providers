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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 27.9
  scored_at: '2026-08-11'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/NexusMutual/cover-router/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/NexusMutual/cover-router/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/NexusMutual/.github/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/NexusMutual/cover-router/blob/dev/LICENSE
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


  Nexus Mutual''s developer surface includes documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 112
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
  composite: 45.5
  delta: 1.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.1
    developer_ergonomics: 17.4
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
