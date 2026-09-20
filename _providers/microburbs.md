---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-09-19'
api_count: 1
apis:
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Account info — caller identity, prepaid balance and usage.
  name: Microburbs Account API
  slug: microburbs-account-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: The Area Statistics API from Microburbs — 3 operation(s) for area statistics.
  name: Microburbs Area Statistics API
  slug: microburbs-area-statistics-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Address → GNAF and suburb autocomplete. The entry point before you have an identifier.
  name: Microburbs Geocode API
  slug: microburbs-geocode-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: ABS geo profile for a Local Government Area.
  name: Microburbs LGA - Profile API
  slug: microburbs-lga-profile-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: ABS geo profile for a mesh block — upward chain.
  name: Microburbs Mesh Block - Profile API
  slug: microburbs-mesh-block-profile-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Nearby amenities and transport within 1km.
  name: Microburbs Property - Amenities API
  slug: microburbs-property-amenities-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Bedroom, bathroom, parking, dwelling type, lot size.
  name: Microburbs Property - Basics API
  slug: microburbs-property-basics-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: CMA comp sets and recent nearby sales.
  name: Microburbs Property - Comparables API
  slug: microburbs-property-comparables-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: The 1km around the property — mesh-block stats, street series, nearby listings.
  name: Microburbs Property - Context API
  slug: microburbs-property-context-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Zoning code and overlays.
  name: Microburbs Property - Development API
  slug: microburbs-property-development-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Sale and rental transaction history.
  name: Microburbs Property - History API
  slug: microburbs-property-history-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: ABS geo profile — mesh block + SA1–SA4 + LGA + state.
  name: Microburbs Property - Profile API
  slug: microburbs-property-profile-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Bushfire, flood, heritage, landslide, erosion, etc.
  name: Microburbs Property - Risks API
  slug: microburbs-property-risks-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Nearby schools and rankings.
  name: Microburbs Property - Schools API
  slug: microburbs-property-schools-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: The 200m around the property — neighbours, tenure, parcels, housing.
  name: Microburbs Property - Surroundings API
  slug: microburbs-property-surroundings-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Cadastral attributes — neighbours, owner.
  name: Microburbs Property - Title API
  slug: microburbs-property-title-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Automated valuation model output.
  name: Microburbs Property - Valuation API
  slug: microburbs-property-valuation-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: ABS geo profile for a Statistical Area Level 4.
  name: Microburbs SA4 - Profile API
  slug: microburbs-sa4-profile-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Crime benchmark, breakdown and mesh-block map values.
  name: Microburbs Suburb - Crime API
  slug: microburbs-suburb-crime-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: ABS census age, dwelling, household, income.
  name: Microburbs Suburb - Demographics API
  slug: microburbs-suburb-demographics-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Development applications.
  name: Microburbs Suburb - Development API
  slug: microburbs-suburb-development-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Ancestry, birthplace, language at home.
  name: Microburbs Suburb - Ethnicity API
  slug: microburbs-suburb-ethnicity-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Cross-suburb range-filter search — filter on ~36 metrics, sort, paginate.
  name: Microburbs Suburb - Finder API
  slug: microburbs-suburb-finder-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: 12-month sale-price forecast.
  name: Microburbs Suburb - Forecast API
  slug: microburbs-suburb-forecast-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Headline summary — geography, population, growth, neighbours.
  name: Microburbs Suburb - Hero API
  slug: microburbs-suburb-hero-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: POIs, livability, landmarks, narrative.
  name: Microburbs Suburb - Lifestyle API
  slug: microburbs-suburb-lifestyle-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Current for-sale listings snapshot.
  name: Microburbs Suburb - Listings API
  slug: microburbs-suburb-listings-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Medians, growth, yield, days on market.
  name: Microburbs Suburb - Market API
  slug: microburbs-suburb-market-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: ABS geo profile — admin chain + mesh-block inventory.
  name: Microburbs Suburb - Profile API
  slug: microburbs-suburb-profile-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Suburb-aggregated risk coverages.
  name: Microburbs Suburb - Risks API
  slug: microburbs-suburb-risks-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Recent sold properties and sales summary.
  name: Microburbs Suburb - Sales API
  slug: microburbs-suburb-sales-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Suburb-level school list and catchment.
  name: Microburbs Suburb - Schools API
  slug: microburbs-suburb-schools-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: GeoJSON — boundary, neighbours, mesh blocks, hazard overlays, noise.
  name: Microburbs Suburb - Shapes API
  slug: microburbs-suburb-shapes-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Most-similar suburb recommendations.
  name: Microburbs Suburb - Similar API
  slug: microburbs-suburb-similar-api
- baseURL: https://api.microburbs.com.au
  baseurl_source: declared
  description: Street-level price forecasts.
  name: Microburbs Suburb - Street Forecasts API
  slug: microburbs-suburb-street-forecasts-api
artifact_total: 40
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/mcp/microburbs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microburbs-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/overlays/microburbs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microburbs-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/security/microburbs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microburbs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/authentication/microburbs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microburbs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.microburbs.com.au
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microburbs/refs/heads/main/well-known/microburbs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microburbs-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.microburbs.com.au/developers/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microburbs.com.au/api-access
- group: start
  title: ''
  type: SignUp
  url: https://www.microburbs.com.au/developers/keys
- group: operate
  title: ''
  type: Support
  url: https://www.microburbs.com.au/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microburbs.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microburbs.com.au/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://www.microburbs.com.au/faqs
created: '2026-09-14'
description: 'Microburbs is an Australian property and location-intelligence API: 173 read-only operations spanning property valuations (AVM), sale and rent history, comparable sales, environmental and neighbourhood risk overlays, zoning and development, schools, transport, demographics and suburb screening -- keyed to ABS statistical geography and G-NAF addresses, and mirrored as a hosted MCP server of 174 tools with per-call cent metering.'
layout: provider
mcp_servers:
- description: Australian property and suburb data as native MCP tools -- valuations, sale and rent history, comparables, risk overlays, zoning, schools, transport and demographics for every Australian address (GNAF
  name: Microburbs MCP Server
  slug: microburbs-mcp-server
modified: '2026-09-14'
name: Microburbs
nav: Providers
network: true
overview: 'Microburbs publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Account API, Area Statistics API, Geocode API, and 32 more. Tagged areas include Property Data, Real-Estate, Australia, Demographics, and Location Intelligence.


  Microburbs'' developer surface includes authentication, pricing, signup flow, support, FAQ, and 9 more developer resources.'
plans:
- name: Microburbs Plans Pricing
  plan_count: 0
  slug: microburbs-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Microburbs Rate Limits
  slug: microburbs-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 58.9
    developer_ergonomics: 44.6
    discoverability: 66.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Microburbs Authentication
  slug: microburbs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microburbs Domain Security
  slug: microburbs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microburbs
tags:
- Property Data
- Real-Estate
- Australia
- Demographics
- Location Intelligence
website: https://www.microburbs.com.au
---
