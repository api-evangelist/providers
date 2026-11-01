---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Eagleview Agentic Access
  operation_count: 21
  slug: eagleview-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 1
apis:
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: Occasionally, a report will need to be adjusted by the customer before it can continue processing. This could be due to a necessary upgrade/downgrade due to the image quality available.
  name: EagleView Order Adjustments API
  slug: eagleview-order-adjustments-api
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: Once the report has been created in the Ordering stage, it is possible to query the status of the order via Order Status API methods.
  name: EagleView Order Status API
  slug: eagleview-order-status-api
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: The EagleView ordering process offers many API methods which allow for varying degrees of customization. Ordering is the first step in the EagleView structure measurement process, as it kickstarts the
  name: EagleView Ordering API
  slug: eagleview-ordering-api
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: Once a report has completed processing, it is possible to retrieve it via Retrieving Files API methods.
  name: EagleView Retrieving Files API
  slug: eagleview-retrieving-files-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: Find images and their corresponding metadata.
  name: EagleView Discovery API
  slug: eagleview-discovery-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The EviwAPI API from EagleView — 2 operation(s) for eviwapi.
  name: EagleView Eviw API
  slug: eagleview-eviwapi-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: TrueDesign's Export APIs allow you to retrieve data, images, reports, and CAD files from your design.
  name: EagleView Exports API
  slug: eagleview-exports-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The GetCapabilities request is the starting point for a client. It returns information about the WMTS service parameters. By default, a GetCapabilities request will return a “Latest” basemap layer, “L
  name: EagleView Get Capabilities API
  slug: eagleview-get-capabilities-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: When EagleView has pre-processed an address the customer will receive a full response in real time.
  name: EagleView Get Property Data API
  slug: eagleview-get-property-data-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Get Property Data (Bulk) API from EagleView — 1 operation(s) for get property data (bulk).
  name: EagleView Get Property Data (Bulk) API
  slug: eagleview-get-property-data-bulk-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Get Property Summary Data API from EagleView — 1 operation(s) for get property summary data.
  name: EagleView Get Property Summary Data API
  slug: eagleview-get-property-summary-data-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Get Property Summary Data (Bulk) API from EagleView — 1 operation(s) for get property summary data (bulk).
  name: EagleView Get Property Summary Data (Bulk) API
  slug: eagleview-get-property-summary-data-bulk-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: The GET /property/v1/attributes/request/{requestId} endpoint allows the customer to check the status of a property data request and retrieve the complete dataset once it's ready. This endpoint will be
  name: EagleView Get Request Status API
  slug: eagleview-get-request-status-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Get Results API from EagleView — 1 operation(s) for get results.
  name: EagleView Get Results API
  slug: eagleview-get-results-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: Using the service parameters returned by the GetCapabilities request, the client can utilise the GetTile request to retrieve a 256x256px slippy-map aligned tile.
  name: EagleView Get Tile API
  slug: eagleview-gettile-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Image Retrieval API from EagleView — 1 operation(s) for image retrieval.
  name: EagleView Image Retrieval API
  slug: eagleview-image-retrieval-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: TrueDesign is an iFrame application and this API will allow you to initialize your session with varying degrees of customization.
  name: EagleView Launch API
  slug: eagleview-launch-api
- baseURL: https://api.opper.ai
  baseurl_source: declared
  description: Programmatic project and API-key management. Authenticates with an `op-mak-…` management token; available on the control_plane and enterprise plans.
  name: EagleView Management API
  slug: eagleview-management-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: The OAuth2 API from EagleView — 3 operation(s) for oauth2.
  name: EagleView O Auth2 API
  slug: eagleview-oauth2-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: TrueDesign's Optimization APIs enables you to access current System Details based on the PV layout and make changes like adjusting to production (kWh) offsets, system size (kW), module count (#), or m
  name: EagleView Optimization API
  slug: eagleview-optimization-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: 'The Product Availability API allows you to check to see if Eagleview has the required imagery to process one or more Solar Products. This process only checks if imagery is available and only after an '
  name: EagleView Product Availability API
  slug: eagleview-product-availability-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Request Property Data API from EagleView — 1 operation(s) for request property data.
  name: EagleView Request Property Data API
  slug: eagleview-request-property-data-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Request Property Data (Bulk) API from EagleView — 1 operation(s) for request property data (bulk).
  name: EagleView Request Property Data (Bulk) API
  slug: eagleview-request-property-data-bulk-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Request Property Summary Data API from EagleView — 1 operation(s) for request property summary data.
  name: EagleView Request Property Summary Data API
  slug: eagleview-request-property-summary-data-api
- baseURL: https://apis.eagleview.com
  baseurl_source: declared
  description: The Request Property Summary Data (Bulk) API from EagleView — 1 operation(s) for request property summary data (bulk).
  name: EagleView Request Property Summary Data (Bulk) API
  slug: eagleview-request-property-summary-data-bulk-api
- baseURL: https://apicenter.eagleview.com
  baseurl_source: declared
  description: Truedesign's Roof API allows you to retrieve roof summary data and control facets (mounting planes) that can support design.
  name: EagleView Roof API
  slug: eagleview-roof-api
- baseURL: https://app.metricool.com/api
  baseurl_source: declared
  description: The Settings API from EagleView — 6 operation(s) for settings.
  name: EagleView Settings API
  slug: eagleview-settings-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/eagleview/agentic-access/eagleview-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eagleview-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/eagleview/rate-limits/eagleview-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eagleview-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/eagleview/plans/eagleview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eagleview-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eagleview/rules/eagleview-rules.yml
  title: ''
  type: Spectral
  url: rules/eagleview-rules.yml
- group: design
  href: https://artifacts.apis.io/eagleview/vocabulary/eagleview-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eagleview-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eagleview/data-model/eagleview-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eagleview-data-model.yml
- group: design
  href: https://artifacts.apis.io/eagleview/conventions/eagleview-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eagleview-conventions.yml
- group: start
  href: https://artifacts.apis.io/eagleview/sandbox/eagleview-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/eagleview-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/eagleview/authentication/eagleview-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eagleview-authentication.yml
- group: design
  href: https://artifacts.apis.io/eagleview/errors/eagleview-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eagleview-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eagleview/conformance/eagleview-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eagleview-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eagleview/llms/eagleview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eagleview-llms.txt
- group: other
  href: https://artifacts.apis.io/eagleview/hosts/eagleview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eagleview-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eagleview.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eagleview.com/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.eagleview.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.eagleview.com/leadership/
- group: auth
  href: https://artifacts.apis.io/eagleview/security/eagleview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eagleview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eagleview.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.eagleview.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.eagleview.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eagleview.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.eagleview.com/blogs/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.eagleview.com/help-center/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.eagleview.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: EagleView provides geospatial intelligence, aerial imagery, and data solutions for property intelligence. Their platform offers high‑resolution aerial imagery, 3D models, property reports, and AI‑driven analytics for residential, commercial, and government customers. EagleView serves industries such as roofing, solar, insurance, utilities, and emergency management, delivering actionable insights through cloud‑based applications and APIs.
finops:
- has_sources: true
  method: derived
  name: Eagleview Finops
  primary_unit: seat
  service_category: ''
  slug: eagleview-finops
  template: false
image: https://www.eagleview.com/wp-content/uploads/2025/06/EV-Opengraph-Thumbnail-Logo.png
layout: provider
modified: '2026-10-13'
name: EagleView
nav: Providers
network: true
overview: 'EagleView publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Order Adjustments API, Order Status API, Ordering API, and 24 more. Tagged areas include Geospatial, Aerial Imagery, Data Analytics, Real Estate, and Insurance.


  The EagleView catalog on APIs.io includes 1 Spectral governance ruleset.


  EagleView''s developer surface includes sandbox, authentication, API reference, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Eagleview Plans Pricing
  plan_count: 24
  slug: eagleview-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Eagleview Rate Limits
  slug: eagleview-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: EagleView API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: eagleview-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 20.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 42.9
    discoverability: 69.6
    operational_transparency: 21.1
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eagleview Authentication
  slug: eagleview-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eagleview Domain Security
  slug: eagleview-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eagleview
tags:
- Geospatial
- Aerial Imagery
- Data Analytics
- Real Estate
- Insurance
website: https://www.eagleview.com/
---
