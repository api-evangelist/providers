---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apibara Tech Agentic Access
  operation_count: 13
  slug: apibara-tech-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Available filters metadata.
  name: Apibara.tech Filters API
  slug: apibara-tech-filters-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Proxy supported auction vehicle images.
  name: Apibara.tech Image Proxy API
  slug: apibara-tech-image-proxy-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Auction facility and location search.
  name: Apibara.tech Locations API
  slug: apibara-tech-locations-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Related and similar auction vehicles.
  name: Apibara.tech Related Vehicles API
  slug: apibara-tech-related-vehicles-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Auction-to-port delivery prices.
  name: Apibara.tech Shipping API
  slug: apibara-tech-shipping-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Resolve vehicle details from auction URLs.
  name: Apibara.tech URL Tools API
  slug: apibara-tech-url-tools-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: API usage and plan limit information.
  name: Apibara.tech Usage API
  slug: apibara-tech-usage-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: VIN and lot auction history.
  name: Apibara.tech Vehicle History API
  slug: apibara-tech-vehicle-history-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Search and retrieve vehicle auction records.
  name: Apibara.tech Vehicles API
  slug: apibara-tech-vehicles-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: Durable, sequence-ordered material vehicle changes for reliable synchronization and replay.
  name: Apibara.tech Change Stream API
  slug: apibara-tech-change-stream-api
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: The Market API from Apibara.tech — 1 operation(s) for market.
  name: Apibara.tech Market API
  slug: apibara-tech-market-api
arazzos:
- description: Retrieve recently updated Copart and IAAI auction records with cursor pagination.
  name: Apibara incremental vehicle-auction synchronization
  slug: apibara-tech-incremental-sync.arazzo
- description: Retrieve a supported vehicle record and then its retained auction history.
  name: Apibara VIN auction research
  slug: apibara-tech-vin-research.arazzo
artifact_total: 35
asyncapis:
- description: ''
  name: Apibara Tech Webhooks
  slug: apibara-tech-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/apibara-tech/agentic-access/apibara-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apibara-tech-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/apibara-tech/finops/apibara-tech-finops.yml
  title: ''
  type: FinOps
  url: finops/apibara-tech-finops.yml
- group: design
  href: https://artifacts.apis.io/apibara-tech/rules/apibara-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/apibara-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/apibara-tech/json-ld/apibara-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apibara-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/apibara-tech/vocabulary/apibara-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apibara-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apibara-tech/asyncapi/apibara-tech-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apibara-tech-webhooks.yml
- group: other
  href: https://artifacts.apis.io/apibara-tech/hosts/apibara-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apibara-tech-hosts.yml
- group: build
  href: https://artifacts.apis.io/apibara-tech/integrations/apibara-tech-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/apibara-tech-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/apibara-tech/vendors/apibara-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apibara-tech-vendors.yml
- group: other
  href: https://artifacts.apis.io/apibara-tech/capabilities/apibara-tech-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apibara-tech-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/apibara-tech/plans/apibara-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apibara-tech-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/apibara-tech/rate-limits/apibara-tech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apibara-tech-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://apibara.tech/en/blog
- group: agent
  title: ''
  type: MCPServer
  url: https://apibara.tech/mcp
- group: company
  title: ''
  type: Website
  url: https://apibara.tech/en
- group: company
  title: ''
  type: About
  url: https://apibara.tech/en/about
- group: docs
  title: ''
  type: Documentation
  url: https://apibara.tech/en/products/vehicle-auction-data-api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://apibara.tech/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apibara.tech/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apibara.tech/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apibara.tech/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://apibara.tech/en/contact
- group: auth
  title: ''
  type: Security
  url: https://apibara.tech/en/security
- group: operate
  title: ''
  type: StatusPage
  url: https://apibara.tech/en/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://apibara.tech/en/changelog
- group: operate
  href: https://artifacts.apis.io/apibara-tech/changelog/apibara-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apibara-tech-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://apibara.tech/llms.txt
- group: agent
  href: https://artifacts.apis.io/apibara-tech/well-known/apibara-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apibara-tech-well-known.yml
- group: design
  href: https://artifacts.apis.io/apibara-tech/conformance/apibara-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apibara-tech-conformance.yml
- group: design
  href: https://artifacts.apis.io/apibara-tech/conventions/apibara-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apibara-tech-conventions.yml
- group: design
  href: https://artifacts.apis.io/apibara-tech/lifecycle/apibara-tech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apibara-tech-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/apibara-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/apibara-tech/security/apibara-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apibara-tech-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/apibara-tech/authentication/apibara-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apibara-tech-authentication.yml
created: '2026-09-18'
description: Independent developer platform providing structured vehicle auction data (normalized JSON for Copart and IAA/IAAI current and historical auction records), including vehicle search, VIN/lot details, photos, prices, sale history, filter metadata, auction locations, shipping calculation, and an image proxy. Offers both a REST/JSON API and a hosted read-only MCP server. Not affiliated with the similarly named apibara.com blockchain indexer.
finops:
- has_sources: true
  method: derived
  name: Apibara Tech Finops
  primary_unit: requests
  service_category: ''
  slug: apibara-tech-finops
  template: false
image: https://apibara.tech/seo/1783599358_p64LSzUP.png
json_schemas:
- name: FiltersResponse
  property_count: 1
  slug: apibara-tech-filters-response
- name: LocationsResponse
  property_count: 2
  slug: apibara-tech-locations-response
- name: MarketSoldPriceStatsResponse
  property_count: 2
  slug: apibara-tech-market-sold-price-stats-response
- name: ShippingResponse
  property_count: 1
  slug: apibara-tech-shipping-response
- name: UsageResponse
  property_count: 1
  slug: apibara-tech-usage-response
- name: VehicleChangesResponse
  property_count: 3
  slug: apibara-tech-vehicle-changes-response
- name: VehicleDetailsResponse
  property_count: 1
  slug: apibara-tech-vehicle-details-response
- name: VehicleHistoryResponse
  property_count: 2
  slug: apibara-tech-vehicle-history-response
- name: VehicleListResponse
  property_count: 2
  slug: apibara-tech-vehicle-list-response
jsonld:
- class_count: 26
  name: Apibara Tech Context
  property_count: 120
  slug: apibara-tech-context
layout: provider
mcp_servers:
- description: ''
  name: Apibara.tech MCP Server
  slug: mcp
modified: '2026-10-06'
name: Apibara.tech
nav: Providers
network: true
overview: 'Apibara.tech publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Filters API, Image Proxy API, Locations API, and 8 more. Tagged areas include Automotive, vehicle-auction-data, Copart, IAAI, and vin-history.


  The Apibara.tech catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Apibara.tech''s developer surface includes engineering blog, documentation, pricing, signup flow, support, changelog, authentication, and 27 more developer resources.'
plans:
- name: Apibara Tech Plans Pricing
  plan_count: 8
  slug: apibara-tech-plans-pricing
- name: Apibara Tech Price Estimates
  plan_count: 0
  slug: apibara-tech-price-estimates
random_paper: 9
rate_limits:
- limit_count: 9
  name: Apibara Tech Rate Limits
  slug: apibara-tech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Apibara.tech API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: apibara-tech-rules
score:
  band: exemplar
  composite: 69.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 78.0
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 81.6
  previous_composite: 68.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 52.4
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/apibara-tech/apibara-tech-2026-10-11T095920.png
security:
- kind: authentication
  name: Apibara Tech Authentication
  slug: apibara-tech-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apibara Tech Domain Security
  slug: apibara-tech-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: apibara-incremental-vehicle-sync
  slug: apibara-tech-incremental-sync
- name: apibara-vin-auction-research
  slug: apibara-tech-vin-research
slug: apibara-tech
tags:
- Automotive
- vehicle-auction-data
- Copart
- IAAI
- vin-history
- Marketplace
- REST API
- Vehicle Auctions
- Salvage Auctions
- VIN Data
- Used-Car Marketplace Data
- Data Infrastructure
- Data as a Service
- REST
- JSON:API
- MCP
- Agent-Native
website: https://apibara.tech/en
---
