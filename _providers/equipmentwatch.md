---
access_model:
  confidence: medium
  label: Request access — API key issued via a HubSpot form; no published API pricing
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://equipmentwatch.com/api/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 25.2
  scored_at: '2026-09-07'
api_count: 1
apis:
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: Foundational API providing access to EquipmentWatch's manufacturer and model database, covering the taxonomy used across the broader API suite for construction and heavy equipment. Published operation
  name: EquipmentWatch Taxonomy API
  slug: taxonomy
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: 'Access to the industry''s most comprehensive database of rich machine specifications for construction and heavy equipment, covering more than 33,000 models, parsed into spec families including weights '
  name: EquipmentWatch Specs API
  slug: specs
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: Serial number verification API supporting approximately 30,000 models of construction and heavy equipment, returning year of manufacture from a supplied serial number along with manufacturer interpret
  name: EquipmentWatch Verification API
  slug: verification
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: Ownership and operating cost recovery rates derived from the Rental Rate Blue Book, supporting equipment cost benchmarking, internal charge rate calculation and FHWA rate lookup.
  name: EquipmentWatch Costs API
  slug: costs
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: Current and trended market values for heavy equipment — Fair Market Value (FMV), Forced Liquidation Value (FLV) and Orderly Liquidation Value (OLV) — supporting valuation, appraisal and resale pricing
  name: EquipmentWatch Values API
  slug: values
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: 'National, regional and rental-house specific equipment rental rates for thousands of models across nearly every equipment rental house in North America, supporting rate optimization for rental fleets '
  name: EquipmentWatch Retail Rental API
  slug: retail-rental
- description: 'Raw equipment sales activity (auction and resale transactions) and market-derived utilization and popularity benchmarks for the heavy equipment industry. Documented on the EquipmentWatch site but NOT '
  name: EquipmentWatch Market Data API
  slug: market-data
- description: Read and write access to user-saved asset and group data inside the EquipmentWatch application, allowing saved models and groups to be moved into and out of third-party platforms. The only EquipmentWa
  name: EquipmentWatch Integration API
  slug: integration
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.equipmentwatch.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equipmentwatch
- group: start
  title: ''
  type: DeveloperPortal
  url: https://equipmentwatch.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.equipmentwatchapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.equipmentwatchapi.com/
- group: company
  title: ''
  type: Blog
  url: https://equipmentwatch.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://equipmentwatch.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://share.hsforms.com/12W-aoSkmR5eYntgAyyiPsAqjl7f
- group: start
  title: ''
  type: Login
  url: https://app.equipmentwatch.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://equipmentwatch.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://equipmentwatch.com/legal/website-terms-and-privacy-notice/
- group: auth
  title: ''
  type: Authentication
  url: authentication/equipmentwatch-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/equipmentwatch-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/equipmentwatch-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/equipmentwatch-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/equipmentwatch-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/equipmentwatch-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/equipmentwatch-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/equipmentwatch-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/equipmentwatch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/equipmentwatch-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/equipmentwatch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/equipmentwatch-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equipmentwatch-domain-security.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/equipmentwatch-finops.yml
created: '2026-03-16'
description: EquipmentWatch (a Fusable brand, operated by Randall-Reilly, LLC) provides construction and equipment data APIs that deliver rental rates, ownership and operating costs, market values, machine specifications, serial-number verification and raw market transaction data for heavy equipment. Their data is used by contractors, equipment dealers, rental houses, lenders and insurance professionals to make informed decisions about equipment valuation, procurement, cost recovery and rental rate setting. The EquipmentWatch API is published as a single OpenAPI 3.0.3 contract at docs.equipmentwatchapi.com covering the Taxonomy, Values, Specifications, Rental, Verification, Cost and Bulk surfaces, served from equipmentwatchapi.com with a documented sandbox host, and authenticated with an x-api-key header issued through a request-an-API-key form.
finops:
- name: Equipmentwatch Finops
  service_category: API
  slug: equipmentwatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equipmentwatch.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the EquipmentWatch OpenAPI. Every tool below binds 1:1 to a real published GET operation. No endpoint is asserted, because none exists.
  name: Equipmentwatch MCP Server
  slug: equipmentwatch-mcp-server
modified: '2026-09-06'
name: Equipmentwatch
nav: Providers
network: true
overview: 'Equipmentwatch publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Taxonomy API, Specs API, Verification API, and 3 more. Tagged areas include Construction, Equipment, Rental Rates, Valuation, and Heavy Equipment.


  Equipmentwatch''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Equipmentwatch Plans Pricing
  plan_count: 0
  slug: equipmentwatch-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Equipmentwatch Rate Limits
  slug: equipmentwatch-rate-limits
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 42.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/screenshots/equipmentwatch-2026-06-20T180808.png
security:
- kind: authentication
  name: Equipmentwatch Authentication
  slug: equipmentwatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Equipmentwatch Domain Security
  slug: equipmentwatch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: equipmentwatch
tags:
- Construction
- Equipment
- Rental Rates
- Valuation
- Heavy Equipment
- Equipment Data
- Market Data
website: https://www.equipmentwatch.com/
---
