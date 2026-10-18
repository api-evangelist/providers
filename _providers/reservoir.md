---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 35
  human_in_the_loop: 5
  name: Reservoir Agentic Access
  operation_count: 93
  slug: reservoir-agentic-access
  summary_line: 93 operations · 35 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Accounts API from Reservoir — 5 operation(s) for accounts.
  name: Reservoir Accounts API
  slug: reservoir-accounts-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Activity API from Reservoir — 3 operation(s) for activity.
  name: Reservoir Activity API
  slug: reservoir-activity-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Attributes API from Reservoir — 2 operation(s) for attributes.
  name: Reservoir Attributes API
  slug: reservoir-attributes-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Chain API from Reservoir — 1 operation(s) for chain.
  name: Reservoir Chain API
  slug: reservoir-chain-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Collections API from Reservoir — 10 operation(s) for collections.
  name: Reservoir Collections API
  slug: reservoir-collections-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Events API from Reservoir — 3 operation(s) for events.
  name: Reservoir Events API
  slug: reservoir-events-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Manage Orders API from Reservoir — 3 operation(s) for manage orders.
  name: Reservoir Manage Orders API
  slug: reservoir-manage-orders-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Management API from Reservoir — 15 operation(s) for management.
  name: Reservoir Management API
  slug: reservoir-management-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The marketplace API from Reservoir — 7 operation(s) for marketplace.
  name: Reservoir Marketplace API
  slug: reservoir-marketplace-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Misc API from Reservoir — 9 operation(s) for misc.
  name: Reservoir Misc API
  slug: reservoir-misc-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Orders API from Reservoir — 3 operation(s) for orders.
  name: Reservoir Orders API
  slug: reservoir-orders-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Owners API from Reservoir — 5 operation(s) for owners.
  name: Reservoir Owners API
  slug: reservoir-owners-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Redirects API from Reservoir — 5 operation(s) for redirects.
  name: Reservoir Redirects API
  slug: reservoir-redirects-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Sales API from Reservoir — 1 operation(s) for sales.
  name: Reservoir Sales API
  slug: reservoir-sales-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Sources API from Reservoir — 1 operation(s) for sources.
  name: Reservoir Sources API
  slug: reservoir-sources-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Stats API from Reservoir — 2 operation(s) for stats.
  name: Reservoir Stats API
  slug: reservoir-stats-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Tokens API from Reservoir — 9 operation(s) for tokens.
  name: Reservoir Tokens API
  slug: reservoir-tokens-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The Transfers API from Reservoir — 1 operation(s) for transfers.
  name: Reservoir Transfers API
  slug: reservoir-transfers-api
- baseURL: https://api.reservoir.tools
  baseurl_source: declared
  description: The x-deprecated API from Reservoir — 8 operation(s) for x-deprecated.
  name: Reservoir X Deprecated API
  slug: reservoir-x-deprecated-api
artifact_total: 33
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/agentic-access/reservoir-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reservoir-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/rules/reservoir-rules.yml
  title: ''
  type: Spectral
  url: rules/reservoir-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/json-ld/reservoir-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/reservoir-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/vocabulary/reservoir-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reservoir-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/data-model/reservoir-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reservoir-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/errors/reservoir-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reservoir-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/conformance/reservoir-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reservoir-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/hosts/reservoir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reservoir-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/vendors/reservoir-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reservoir-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/authentication/reservoir-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reservoir-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/security/reservoir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reservoir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reservoir.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://nft.reservoir.tools/reference/overview
- group: build
  title: ''
  type: GitHub
  url: https://github.com/reservoirprotocol
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uneven-labs
- group: company
  title: ''
  type: Blog
  url: https://reservoir.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://reservoir.tools/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reservoir.tools/
- group: other
  title: ''
  type: X
  url: https://x.com/reservoir0x
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/plans/reservoir-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reservoir-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/rate-limits/reservoir-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reservoir-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/finops/reservoir-finops.yml
  title: ''
  type: FinOps
  url: finops/reservoir-finops.yml
created: '2026-06-12'
description: NFT marketplace infrastructure and data API for aggregating listings, bids, and sales across OpenSea, Blur, and other markets — powers buying, selling, and analytics across 30+ EVM chains. Reservoir provided a complete suite of APIs, SDKs, and UI kits abstracting the complexity of interacting with the NFT market. The service was sunset on October 15, 2025.
finops:
- has_sources: false
  method: generated
  name: Reservoir Finops
  primary_unit: ''
  service_category: ''
  slug: reservoir-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reservoir.png
json_schemas:
- name: Model538
  property_count: 4
  slug: reservoir-model538
- name: Model564
  property_count: 26
  slug: reservoir-model564
- name: Model584
  property_count: 8
  slug: reservoir-model584
- name: Model600
  property_count: 4
  slug: reservoir-model600
- name: Model611
  property_count: 11
  slug: reservoir-model611
- name: Model624
  property_count: 18
  slug: reservoir-model624
jsonld:
- class_count: 11
  name: Reservoir Context
  property_count: 37
  slug: reservoir-context
layout: provider
modified: '2026-06-12'
name: Reservoir
nav: Providers
network: true
overview: 'Reservoir publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Activity API, Attributes API, and 16 more. Tagged areas include NFT, Blockchain, Marketplace, Ethereum, and EVM.


  The Reservoir catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Reservoir''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Reservoir Plans Pricing
  plan_count: 3
  slug: reservoir-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Reservoir Rate Limits
  slug: reservoir-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Reservoir API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: reservoir-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.6
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 59.1
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 19
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/screenshots/reservoir-2026-06-20T193029.png
security:
- kind: authentication
  name: Reservoir Authentication
  slug: reservoir-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reservoir Domain Security
  slug: reservoir-domain-security
  summary_line: DMARC
slug: reservoir
tags:
- NFT
- Blockchain
- Marketplace
- Ethereum
- EVM
- Liquidity
- Order Book
- Web3
- DeFi
- Trading
- Data API
website: https://reservoir.dev/
---
