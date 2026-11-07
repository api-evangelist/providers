---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Foreign Agricultural Service Agentic Access
  operation_count: 35
  slug: foreign-agricultural-service-agentic-access
  summary_line: 35 operations
api_count: 2
apis:
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: The ESR Data API - United States Weekly Export Sales of Agricultural Commodity Data API from Foreign Agricultural Service — 7 operation(s) for esr data api - united states weekly export sales of agric
  name: Foreign Agricultural Service ESR Data API - United States Weekly Export Sales of Agricultural Commodity Data API
  slug: foreign-agricultural-service-esr-data-api-united-states-weekly-export-sales-of-agricultural-commodity-data-api
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: The GATS Data API - US Census and UN ComTrade Import Export & Re-Export Data API from Foreign Agricultural Service — 19 operation(s) for gats data api - us census and un comtrade import export & re-ex
  name: Foreign Agricultural Service GATS Data API - US Census and UN ComTrade Import Export & Re-Export Data API
  slug: foreign-agricultural-service-gats-data-api-us-census-and-un-comtrade-import-export-re-export-data-api
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: 'The PSD Data API - Production, Supply and Distribution Forecast Data of World Agricultural Commodities API from Foreign Agricultural Service — 9 operation(s) for psd data api - production, supply and '
  name: Foreign Agricultural Service PSD Data API - Production, Supply and Distribution Forecast Data of World Agricultural Commodities API
  slug: foreign-agricultural-service-psd-data-api-production-supply-and-distribution-forecast-data-of-world-agricultural-commodities-api
artifact_total: 18
collections:
- collection_type: open
  name: USDA FAS Open Data Services ESR API
  slug: open-foreign-agricultural-service-esr-api
- collection_type: open
  name: USDA FAS Open Data Services ESR GATS API
  slug: open-foreign-agricultural-service-gats-api
- collection_type: open
  name: USDA FAS Open Data Services ESR PSD API
  slug: open-foreign-agricultural-service-psd-api
- collection_type: open
  name: USDA FAS Open Data Services
  slug: open-foreign-agricultural-service
common:
- group: commercial
  href: https://artifacts.apis.io/foreign-agricultural-service/finops/foreign-agricultural-service-finops.yml
  title: ''
  type: FinOps
  url: finops/foreign-agricultural-service-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://apps.fas.usda.gov/opendataweb/home
- group: other
  href: https://artifacts.apis.io/foreign-agricultural-service/overlays/foreign-agricultural-service-esr-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/foreign-agricultural-service-esr-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/foreign-agricultural-service/overlays/foreign-agricultural-service-gats-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/foreign-agricultural-service-gats-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/foreign-agricultural-service/overlays/foreign-agricultural-service-psd-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/foreign-agricultural-service-psd-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/foreign-agricultural-service/agentic-access/foreign-agricultural-service-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/foreign-agricultural-service-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/foreign-agricultural-service/security/foreign-agricultural-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foreign-agricultural-service-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/foreign-agricultural-service/authentication/foreign-agricultural-service-authentication.yml
  title: ''
  type: Authentication
  url: authentication/foreign-agricultural-service-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-foreign-agricultural-service
- group: company
  title: ''
  type: Website
  url: https://www.fas.usda.gov/
- group: build
  href: https://artifacts.apis.io/foreign-agricultural-service/packages/foreign-agricultural-service-packages.yml
  title: ''
  type: Packages
  url: packages/foreign-agricultural-service-packages.yml
- group: agent
  href: https://artifacts.apis.io/foreign-agricultural-service/llms/foreign-agricultural-service-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foreign-agricultural-service-llms.txt
- group: agent
  href: https://artifacts.apis.io/foreign-agricultural-service/mcp/foreign-agricultural-service-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/foreign-agricultural-service-mcp.yml
- group: design
  href: https://artifacts.apis.io/foreign-agricultural-service/conformance/foreign-agricultural-service-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foreign-agricultural-service-conformance.yml
- group: design
  href: https://artifacts.apis.io/foreign-agricultural-service/errors/foreign-agricultural-service-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/foreign-agricultural-service-problem-types.yml
- group: design
  href: https://artifacts.apis.io/foreign-agricultural-service/lifecycle/foreign-agricultural-service-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/foreign-agricultural-service-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/foreign-agricultural-service/conventions/foreign-agricultural-service-conventions.yml
  title: ''
  type: Conventions
  url: conventions/foreign-agricultural-service-conventions.yml
- group: design
  href: https://artifacts.apis.io/foreign-agricultural-service/data-model/foreign-agricultural-service-data-model.yml
  title: ''
  type: DataModel
  url: data-model/foreign-agricultural-service-data-model.yml
- group: agent
  href: https://artifacts.apis.io/foreign-agricultural-service/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/foreign-agricultural-service/plans/foreign-agricultural-service-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/foreign-agricultural-service-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/foreign-agricultural-service/rate-limits/foreign-agricultural-service-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/foreign-agricultural-service-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/foreign-agricultural-service/security/foreign-agricultural-service-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/foreign-agricultural-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usda.gov/vulnerability-disclosure-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apps.fas.usda.gov/opendataweb/home
- group: docs
  title: ''
  type: APIReference
  url: https://apps.fas.usda.gov/opendata/swagger/ui/index
- group: start
  title: ''
  type: SignUp
  url: https://apps.fas.usda.gov/opendatawebv2/#/signup
- group: operate
  title: ''
  type: Support
  url: https://apps.fas.usda.gov/opendatawebv2/#/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
created: '2024-12-25'
description: 'The Foreign Agricultural Service (FAS) is the trade and export agency of the United States Department of Agriculture (USDA), working to promote U.S. agricultural exports and expand global markets for American agricultural products. FAS runs the Open Data Services at apps.fas.usda.gov, a free, key-gated HTTPS/JSON API publishing three datasets on U.S. and world agricultural trade: ESR (Export Sales Reporting — weekly U.S. export sales by commodity, destination and market year), GATS (the Global Agricultural Trade System — U.S. Census and UN ComTrade import, export and re-export flows, including trade by U.S. customs district), and PSD (Production, Supply and Distribution — world commodity production, supply and use forecasts). The surface is 35 read-only GET operations behind a single API_KEY header, described by a live Swagger 2.0 contract and rendered in Swagger UI.'
finops:
- has_sources: true
  method: derived
  name: Foreign Agricultural Service Finops
  primary_unit: ''
  service_category: ''
  slug: foreign-agricultural-service-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foreign-agricultural-service.png
layout: provider
modified: '2026-09-10'
name: Foreign Agricultural Service
nav: Providers
network: true
overview: 'Foreign Agricultural Service publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: ESR Data API - United States Weekly Export Sales of Agricultural Commodity Data API, GATS Data API - US Census and UN ComTrade Import Export & Re-Export Data API, and PSD Data API - Production, Supply and Distribution Forecast Data of World Agricultural Commodities API. Tagged areas include Agriculture, Federal Government, Trade, Open Data, and Commodities.


  The Foreign Agricultural Service catalog on APIs.io includes 1 Spectral governance ruleset.


  Foreign Agricultural Service''s developer surface includes pricing, authentication, API reference, signup flow, support, and 23 more developer resources.'
plans:
- name: Foreign Agricultural Service Plans Pricing
  plan_count: 1
  slug: foreign-agricultural-service-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Foreign Agricultural Service Rate Limits
  slug: foreign-agricultural-service-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Foreign Agricultural Service API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 2
  slug: foreign-agricultural-service-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 44.6
    discoverability: 66.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/foreign-agricultural-service/foreign-agricultural-service-2026-06-20T181418.png
security:
- kind: authentication
  name: Foreign Agricultural Service Authentication
  slug: foreign-agricultural-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Foreign Agricultural Service Domain Security
  slug: foreign-agricultural-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Foreign Agricultural Service Vulnerability Disclosure
  slug: foreign-agricultural-service-vulnerability-disclosure
  summary_line: Bugcrowd
skill_count: 3
skills:
- name: Query global agricultural trade flows (GATS)
  slug: foreign-agricultural-service-query-global-trade-flows
- name: Read world production and supply forecasts (PSD)
  slug: foreign-agricultural-service-read-psd-forecasts
- name: Track weekly US export sales for a commodity
  slug: foreign-agricultural-service-track-weekly-export-sales
slug: foreign-agricultural-service
tags:
- Agriculture
- Federal Government
- Trade
- Open Data
- Commodities
- Export
- Government
website: https://www.fas.usda.gov/
---
