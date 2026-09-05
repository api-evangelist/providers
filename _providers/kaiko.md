---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 27.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kaiko Agentic Access
  operation_count: 5
  slug: kaiko-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: REST endpoints for trades, order books, OHLCV, market reference, trade flows, FX rates, and derivatives across 100+ exchanges. Historical depth back to 2014. Authentication via X-Api-Key header.
  name: Kaiko REST API
  slug: rest-api
- description: Real-time crypto market data delivered over gRPC server-streaming. Feeds include tick-level trades, top-of-book (best bid/ask), level-2 order book updates, level-1 aggregations (OHLCV, VWAP), derivati
  name: Kaiko Stream
  slug: stream
- description: On-chain metrics including DEX trades, liquidity, lending markets, and MEV signals across major chains.
  name: Kaiko On-chain API
  slug: on-chain-api
- description: Regulated benchmark crypto indices designed for fund administrators and ETF/ETP issuers.
  name: Kaiko Indices
  slug: indices
- baseURL: https://us.market-api.kaiko.io/v2
  baseurl_source: declared
  description: Canton oracle pricing endpoints.
  name: Kaiko Canton Oracle API
  slug: kaiko-canton-oracle-api
- baseURL: https://us.market-api.kaiko.io/v2
  baseurl_source: declared
  description: Reference-rate data for Kaiko indices.
  name: Kaiko Index Reference Data API
  slug: kaiko-index-reference-data-api
- baseURL: https://us.market-api.kaiko.io/v2
  baseurl_source: declared
  description: Index composition and replication data.
  name: Kaiko Indices API
  slug: kaiko-indices-api
- baseURL: https://us.market-api.kaiko.io/v2
  baseurl_source: declared
  description: Asset supply and market-capitalization rankings.
  name: Kaiko Supply API
  slug: kaiko-supply-api
artifact_total: 25
collections:
- collection_type: postman
  name: Kaiko Market Data REST Canton Oracle API
  slug: postman-kaiko-canton-oracle-api
- collection_type: postman
  name: Kaiko Market Data REST Canton Oracle Index Reference Data API
  slug: postman-kaiko-index-reference-data-api
- collection_type: postman
  name: Kaiko Market Data REST Canton Oracle Indices API
  slug: postman-kaiko-indices-api
- collection_type: postman
  name: Kaiko Market Data REST Canton Oracle Supply API
  slug: postman-kaiko-supply-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kaiko Market Data REST Canton Oracle API
  slug: open-kaiko-canton-oracle-api
- collection_type: open
  name: Kaiko Market Data REST Canton Oracle Index Reference Data API
  slug: open-kaiko-index-reference-data-api
- collection_type: open
  name: Kaiko Market Data REST Canton Oracle Indices API
  slug: open-kaiko-indices-api
- collection_type: open
  name: Kaiko Market Data REST Canton Oracle Supply API
  slug: open-kaiko-supply-api
- collection_type: open
  name: Kaiko Market Data REST API
  slug: open-kaiko
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kaiko/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kaiko-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaiko-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kaiko-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kaikodata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kaikodata
- group: start
  title: ''
  type: Portal
  url: https://www.kaiko.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kaiko.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/kaiko-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kaiko-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kaiko-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kaiko-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kaiko.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/kaiko-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kaiko-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/kaiko-equities.proto
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kaiko-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kaiko-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.kaiko.com/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/kaiko-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kaiko-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kaiko-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kaiko.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/kaiko-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kaiko-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/kaiko.postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kaiko.com/about-kaiko/pricing-and-contracts
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kaiko.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marketing.kaiko.com/hubfs/Website%20documents/Kaiko%20-%20Privacy%20Policy%20(v.1.0).pdf
- group: company
  title: ''
  type: Blog
  url: https://www.kaiko.com/resources/categories/data-blog
- group: operate
  title: ''
  type: Support
  url: https://www.kaiko.com/contact-kaiko
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kaiko.com/rest-api/general/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kaiko.com/rest-api/general/introduction
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-05-08'
description: Kaiko is an institutional-grade crypto market data provider. Its product line spans Kaiko REST (historical and reference data), Kaiko Stream (real-time WebSocket and gRPC), Cloud Delivery (S3 and Snowflake direct shares), Kaiko On-chain, and Kaiko Indices (regulated benchmark indices). Authentication uses API keys; access is sales-led.
finops:
- name: Kaiko Finops
  service_category: Crypto Market Data
  slug: kaiko-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kaiko.png
layout: provider
modified: '2026-07-22'
name: Kaiko
nav: Providers
network: true
overview: 'Kaiko publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Canton Oracle API, Index Reference Data API, Indices API, and 1 more. Tagged areas include Web3, Crypto, Market Data, Institutional, and FX.


  Kaiko''s developer surface includes authentication, developer portal, documentation, changelog, pricing, engineering blog, support, and 28 more developer resources.'
plans:
- name: Kaiko Plans Pricing
  plan_count: 2
  slug: kaiko-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Kaiko Rate Limits
  slug: kaiko-rate-limits
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 67.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaiko/refs/heads/main/screenshots/kaiko-2026-06-20T183855.png
security:
- kind: authentication
  name: Kaiko Authentication
  slug: kaiko-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kaiko Domain Security
  slug: kaiko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kaiko Trust Center
  slug: kaiko-trust-center
  summary_line: SOC 2 Type II
slug: kaiko
tags:
- Web3
- Crypto
- Market Data
- Institutional
- FX
- Indices
- Onchain
- Streaming
website: https://www.kaiko.com/
---
