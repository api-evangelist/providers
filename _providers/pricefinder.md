---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-03'
api_count: 10
apis:
- description: Property record retrieval for Australian properties — core and extended property detail, images, floorplans, street view, maps, schools, radial searches for nearby sales, rentals, listings, properties
  name: Pricefinder Property API
  slug: pricefinder-property-api
- description: Automated valuation model output for a property, returned as JSON via GET /properties/{propertyId}/avm against the AVM schema, and as a rendered PDF via /properties/{propertyId}/avm/pdf. Auto-CMA sale
  name: Pricefinder AVM & Valuation API
  slug: pricefinder-avm-api
- description: Retrieval of individual sale, rental and listing records by identifier, and enumeration of sales, rentals and listings scoped by suburb, postcode, street or spatial boundary. Backed by Domain and Allh
  name: Pricefinder Sales, Rentals & Listings API
  slug: pricefinder-sales-rentals-listings-api
- description: Suburb-level market intelligence — suburb detail and summary, demographics, flyover reports and PDFs, street enumeration, peak selling periods, sale price segmentation, and time series for sales, rent
  name: Pricefinder Suburb & Market Statistics API
  slug: pricefinder-suburb-statistics-api
- description: 'State-by-state resolution of Australian land title references to Pricefinder property records — NSW, VIC, QLD, SA, WA, TAS, NT and ACT plan/planType, lot, section, volume, folio and division lookups, '
  name: Pricefinder Title & Land Reference API
  slug: pricefinder-title-reference-api
- description: Address, street, suburb and typeahead suggestion endpoints, lon/lat reverse suggestion, owner-name search across properties and sales, and spatial queries returning properties, sales, rentals and list
  name: Pricefinder Search & Suggest API
  slug: pricefinder-search-api
- description: Comparative market analysis and appraisal artifacts — sales CMA, rental CMA and statement-of-information retrieval by appraisal share identifier (standard and extended), appraisal listing and insights
  name: Pricefinder Appraisals & CMA API
  slug: pricefinder-appraisals-api
- description: Subscribe, list and delete property event alerts for ForSale, ForRent, Sold and SoldVerified event types, per property or for the current user. The documentation states these are delivered as email no
  name: Pricefinder Property Event Subscriptions API
  slug: pricefinder-event-subscriptions-api
- description: 'Single sign-on deep links that hand an authenticated user into the Pricefinder web application at a specific context — a property, its CMA, sales or rental appraisal, statement of information, radial '
  name: Pricefinder SSO API
  slug: pricefinder-sso-api
- description: 'POST /oauth2/token issuing access and refresh tokens for three documented grant types: client_credentials (API user''s own username and password, HTTP Basic accepted as an alternative to form parameter'
  name: Pricefinder OAuth 2.0 Token API
  slug: pricefinder-oauth2-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pricefinder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pricefinder.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.pricefinder.com.au/v1/swagger/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.pricefinder.com.au/v1/swagger/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.pricefinder.com.au/v1/swagger.json
- group: start
  title: ''
  type: SignUp
  url: https://www.pricefinder.com.au/get-started/
- group: operate
  title: ''
  type: Support
  url: https://help.pricefinder.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pricefinder.com.au/our-data/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domain.com.au/group/api-terms-and-conditions/
- group: build
  title: ''
  type: Packages
  url: packages/pricefinder-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pricefinder-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pricefinder-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pricefinder-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/pricefinder-api-swagger-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/pricefinder-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pricefinder-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pricefinder-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pricefinder-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pricefinder-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pricefinder-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domain.com.au/group/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.pricefinder.com.au/portal/app?page=ExternalLogin&service=page
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.pricefinder.com.au/resources-and-support/
created: '2026-07-26'
description: Pricefinder is an Australian property intelligence and valuation platform operating at pricefinder.com.au, supplying property records, comparable sales and rental history, suburb statistics, AVM-powered price estimates and CMA/appraisal reports to real estate agencies, mortgage brokers, banks and lenders, valuers, property developers, advisory firms and government. Its home market is Australia and it sits on the data side of the value chain rather than the portal side — it blends Domain and Allhomes first-party listing feeds with state and territory government land valuation and sales data plus third-party mapping, then resells that as reports, a web application and an API. Pricefinder is a brand of Domain Holdings Australia, which CoStar Group completed the acquisition of in August 2025, so it now sits inside the same group as Domain, Allhomes and Commercial Real Estate. Its API posture is unusually honest for this sector — the full machine-readable contract is genuinely public.
  A complete Swagger 2.0 document (v1.13.1, 112 paths, 188 definitions, 19 tags) and an interactive Swagger UI are served anonymously from api.pricefinder.com.au, and OAuth 2.0 client_credentials, authorization_code and refresh_token flows are documented in full. But every data path returns 401 without credentials, and credentials are not self-serve — there is no developer signup, only industry "Get started" forms that route to sales for a custom, minimum-one-month commercial subscription governed by the Domain Group API Terms and Conditions. Australia has no MLS system and no RESO regime — no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier appears anywhere in Pricefinder's contract or documentation. The land-registry seam shows up instead as state-specific title reference lookups (NSW/VIC/QLD/SA/WA/TAS/NT/ACT plan, lot, section, volume and folio paths).
image: https://www.pricefinder.com.au/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: pricefinder-mcp.yml
  slug: pricefinder-mcpyml
modified: '2026-07-26'
name: Pricefinder
nav: Providers
network: true
overview: 'Pricefinder publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Property API, AVM & Valuation API, Sales, Rentals & Listings API, and 7 more. Tagged areas include Real Estate, Australia, PropTech, Property Data, and Valuation.


  Pricefinder''s developer surface includes API reference, signup flow, support, documentation, authentication, and 19 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 37.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pricefinder/refs/heads/main/screenshots/pricefinder-2026-07-27T125408.png
security:
- kind: authentication
  name: Pricefinder Authentication
  slug: pricefinder-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pricefinder Domain Security
  slug: pricefinder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pricefinder
tags:
- Real Estate
- Australia
- PropTech
- Property Data
- Valuation
- AVM
- Property Listings
- Rentals
- Land Registry
- Title
- Mortgage
- Market Data
website: https://www.pricefinder.com.au/
---
