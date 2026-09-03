---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-02'
api_count: 26
apis:
- baseURL: https://access.api.cotality.com.au
  baseurl_source: declared
  description: OAuth 2.0 token service for every Cotality Australia and New Zealand API. Issues JWT access tokens via client_credentials, authorization_code and refresh_token grants. The developer portal documents P
  name: CoreLogic Australia Access API
  slug: corelogic-au-access-api
- baseURL: https://property-details.api.cotality.com.au
  baseurl_source: declared
  description: Per-property record retrieval keyed on the CoreLogic property identifier — core and additional attributes, site detail, features, occupancy, sales history and last sale, on-the-market sales and rental
  name: CoreLogic Australia Property Details API
  slug: corelogic-au-property-details-api
- baseURL: https://property-au.api.cotality.com.au
  baseurl_source: declared
  description: The older versioned property services family — comparables, geo sales search by polygon, locality, postcode and street, property and parcel suggest, point search, for-sale and for-rent advertisements,
  name: CoreLogic Australia Property Services API
  slug: corelogic-au-property-services-api
- baseURL: https://search.api.cotality.com.au
  baseurl_source: declared
  description: Property search and address matching across Australia — radius search by latitude/longitude, and filtered search by council area, locality, postcode and street, each in four flavours (current attribut
  name: CoreLogic Australia Search API
  slug: corelogic-au-search-api
- baseURL: https://avm.api.cotality.com.au
  baseurl_source: declared
  description: IntelliVal automated valuation model — the valuation engine at the centre of CoreLogic Australia's mortgage and lending business. The sandbox collection publishes consumer and origination AVM variants
  name: CoreLogic Australia AVM API
  slug: corelogic-au-avm-api
- baseURL: https://auction.api.cotality.com.au
  baseurl_source: declared
  description: Australian auction results and clearance rates — the weekly number the Australian property press runs on. Publishes state-level summaries and results with capital-city filtering, suburb and postcode d
  name: CoreLogic Australia Auction API
  slug: corelogic-au-auction-api
- baseURL: https://statistics.api.cotality.com.au
  baseurl_source: declared
  description: Suburb, locality and region statistics plus ABS census summaries, driven by location and location-type identifiers and metric-type identifiers. Four operations are published in the sandbox collection,
  name: CoreLogic Australia Statistics API
  slug: corelogic-au-statistics-api
- baseURL: https://charts.api.cotality.com.au
  baseurl_source: declared
  description: Server-rendered PNG chart images for market trends and census data, driven by location, property-type and metric-type identifiers with extensive presentation parameters (chart size, colours, titles, a
  name: CoreLogic Australia Charts API
  slug: corelogic-au-charts-api
- baseURL: https://property-timeline.api.cotality.com.au
  baseurl_source: declared
  description: 'Chronological event timeline for a single property — sales, listing campaigns, rental campaigns and, with the withBuildingConsents flag, building consent events. Three operations are published in the '
  name: CoreLogic Australia Property Timeline API
  slug: corelogic-au-property-timeline-api
- baseURL: https://content.api.cotality.com.au
  baseurl_source: declared
  description: Serves the legal disclaimers that licensees are contractually required to display alongside CoreLogic data, retrieved by disclaimer key (for example /legal/disclaimers/auction_au and /legal/disclaimer
  name: CoreLogic Australia Content API
  slug: corelogic-au-content-api
- description: PSX is CoreLogic Australia's valuation ordering exchange, connecting lenders and brokers to panels of licensed valuers. The Cotality Developer Portal defines nine documented PSX operations — panel loo
  name: CoreLogic Australia PSX API
  slug: corelogic-au-psx-api
- description: 'Commercial property data delivered into a licensee''s own systems — market research, commercial valuations and comparable sales analysis, sharing the Cotality property identifier so commercial records '
  name: CoreLogic Australia Commercial API
  slug: corelogic-au-commercial-api
- description: Live Cordell construction cost and project intelligence — project activity, builder profiles and contact information — delivered into customer-facing platforms, apps and quoting or planning tools. The
  name: CoreLogic Australia Construction API
  slug: corelogic-au-construction-api
- description: Insurance-facing property data service. Named and hosted in the Cotality Developer Portal environment-details guide, and included in the sandbox at api-sbox.corelogic.asia/insurance. Probed anonymousl
  name: CoreLogic Australia Insurance API
  slug: corelogic-au-insurance-api
- description: Property risk services — the API behind Cotality's Australian hazard and resilience products. Named and hosted in the environment-details guide (sandbox api-sbox.corelogic.asia/risk); probed anonymous
  name: CoreLogic Australia Property Risk API
  slug: corelogic-au-property-risk-api
- description: Places of interest attached to a property. The portal FAQ is explicit about its scope — "Currently, only Schools and School Catchments are available" — and that NAPLAN data is not available, with scho
  name: CoreLogic Australia Places API
  slug: corelogic-au-places-api
- description: Location search services — the successor surface for resolving the locality, postcode, street, council-area and state identifiers every Cotality search, statistic and chart is keyed on. Named and host
  name: CoreLogic Australia Location Search API
  slug: corelogic-au-location-search-api
- description: Property Bureau service. Named and hosted in the Cotality Developer Portal environment-details guide and included in the sandbox at api-sbox.corelogic.asia/propertybureau; probed anonymously on 2026-0
  name: CoreLogic Australia Property Bureau API
  slug: corelogic-au-property-bureau-api
- description: Report rendering for IntelliVal automated valuations — the document form of the AVM number rather than the raw estimate. Named and hosted in the environment-details guide (sandbox api-sbox.corelogic.a
  name: CoreLogic Australia AVM Report API
  slug: corelogic-au-avm-report-api
- description: Property profile report generation — the API behind Cotality's Australian property, suburb and investment report products. Named and hosted in the environment-details guide (sandbox api-sbox.corelogic
  name: CoreLogic Australia Property Profile Report API
  slug: corelogic-au-property-profile-report-api
- description: Reporting services. Named and hosted in the Cotality Developer Portal environment-details guide and included in the sandbox at api-sbox.corelogic.asia/reporting; probed anonymously on 2026-07-26 and r
  name: CoreLogic Australia Reporting API
  slug: corelogic-au-reporting-api
- description: Property monitoring — watch a property or portfolio for change. Named and hosted in the environment-details guide, and explicitly excluded from the sandbox ("Property Monitor and Notification" is on C
  name: CoreLogic Australia Property Monitor API
  slug: corelogic-au-property-monitor-api
- description: Notification services. Named and hosted in the environment-details guide and excluded from the sandbox alongside Property Monitor; probed anonymously on 2026-07-26 and returned HTTP 401. No event cata
  name: CoreLogic Australia Notification API
  slug: corelogic-au-notification-api
- description: Property owner verification services. Named and hosted in the environment-details guide and excluded from the sandbox ("Property Owner Verification"), so it is reachable only after promotion to UAT un
  name: CoreLogic Australia Owner Verification API
  slug: corelogic-au-owner-verification-api
- description: 'Update services — the write-shaped surface of the Cotality Australian estate. Named and hosted in the environment-details guide and excluded from the sandbox ("Update"), so it is reachable only after '
  name: CoreLogic Australia Update API
  slug: corelogic-au-update-api
- description: Cordell Sum Sure — building and contents rebuild-cost estimation, the calculator Australian insurers and brokers use for sum-insured adequacy. Named and hosted in the environment-details guide with se
  name: CoreLogic Australia Cordell Sum Sure API
  slug: corelogic-au-cordell-sum-sure-api
artifact_total: 33
asyncapis:
- description: ''
  name: Corelogic Au Psx Webhooks
  slug: corelogic-au-psx-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/corelogic-au-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corelogic-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cotality.com/au
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.corelogic.asia/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.corelogic.asia/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.corelogic.asia/guides/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://developer.corelogic.asia/signup
- group: start
  title: ''
  type: Login
  url: https://developer.corelogic.asia/user/register
- group: auth
  title: ''
  type: Authentication
  url: https://developer.corelogic.asia/guides/api-authentication
- group: agent
  title: ''
  type: WellKnown
  url: https://auth.corelogic.asia/.well-known/openid-configuration
- group: design
  title: ''
  type: Conventions
  url: https://developer.corelogic.asia/guides/standards-and-conventions
- group: start
  title: ''
  type: Sandbox
  url: https://developer.corelogic.asia/guides/sandbox-test-data
- group: operate
  title: ''
  type: Support
  url: https://developer.corelogic.asia/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://developer.corelogic.asia/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.corelogic.asia/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.corelogic.asia/legal/privacy-policy
- group: build
  title: ''
  type: PostmanCollection
  url: collections/corelogic-au-sample-sandbox.postman_collection.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/corelogic-au-rp-inside-auth-example.postman_collection.json
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/7051651/S1EJWfxt
- group: docs
  title: ''
  type: APIReference
  url: https://developer.corelogic.asia/apis
- group: company
  title: ''
  type: Blog
  url: https://www.cotality.com/au/insights
- group: docs
  title: ''
  type: Documentation
  url: https://developer.corelogic.asia/guides/environment-details
- group: docs
  title: ''
  type: Documentation
  url: https://developer.corelogic.asia/guides/metric-types
- group: docs
  title: ''
  type: Documentation
  url: https://developer.corelogic.asia/guides/enterprise-apis/property-types
- group: docs
  title: ''
  type: Documentation
  url: https://developer.corelogic.asia/guides/mapping-services
- group: auth
  title: ''
  type: Authentication
  url: authentication/corelogic-au-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/corelogic-au-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corelogic-au-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corelogic-au-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/corelogic-au-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corelogic-au-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.corelogic.asia/faq
- group: start
  title: ''
  type: Sandbox
  url: sandbox/corelogic-au-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/corelogic-au-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/corelogic-au-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corelogic-au-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/corelogic-au-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corelogic-au-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/corelogic-au-psx-webhooks.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/corelogic-au-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cotality.com/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corelogic-au-authenticate-and-call.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corelogic-au-address-to-property-record.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corelogic-au-value-a-property.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corelogic-au-auction-clearance-and-market-trends.md
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cotalityaustralia
- group: company
  title: ''
  type: Twitter
  url: https://x.com/cotality_au
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/cotalityau/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/cotality_au/
created: '2026-07-26'
description: 'CoreLogic Australia — trading as Cotality since the 2025 global rebrand, and operating the RP Data platform through RP Data Pty Ltd — is the dominant independent property data, analytics and valuation provider in Australia and New Zealand. It sits in the middle of the Australian property value chain: it aggregates state land-registry and valuer-general records, agent and portal listing campaigns, auction results and rental campaigns into a single property spine, then sells that spine back to banks, mortgage brokers, valuers, insurers, agents and government. Its commercial products include the RP Data / RP Professional desktop, the IntelliVal automated valuation model, the CoreLogic Home Value Index, Cordell construction cost data, Cityscope commercial property data, and the PSX valuation ordering exchange. Its API posture is genuinely developer-facing but commercially licensed: a live Backstage-based Cotality Developer Portal at developer.corelogic.asia offers self-serve signup
  and self-serve creation of sandbox OAuth clients against a deliberately restricted evaluation dataset with request quotas, while every production API host in the *.api.cotality.com.au family answers 401 "Access token is missing" and requires a signed commercial data licence. Australia has no MLS and no RESO mandate — CoreLogic''s RESO Web API and Data Dictionary certifications belong to Trestle, its United States MLS platform, not to this Australian surface. The Australian APIs are proprietary REST/JSON over an Apigee gateway with OAuth 2.0 client credentials; no OData $metadata, no RESO endpoint, and no RESO Universal Property Identifier appears anywhere in the Australian developer portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/corelogic-au.png
layout: provider
mcp_servers:
- description: ''
  name: Cotality MCP Server
  slug: cotality-mcp-server
modified: '2026-07-26'
name: CoreLogic Australia
nav: Providers
network: true
overview: 'CoreLogic Australia publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Access API, Property Details API, Property Services API, and 7 more. Tagged areas include Real-Estate, Australia, Property Data, Valuation, and AVM.


  The CoreLogic Australia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CoreLogic Australia''s developer surface includes documentation, getting-started guide, signup flow, authentication, sandbox, support, FAQ, and 43 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 0
  name: Corelogic Au Rate Limits
  slug: corelogic-au-rate-limits
scopes:
- name: Corelogic Au Scopes
  scope_count: 5
  slug: corelogic-au-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/implicit
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 18.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 27.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corelogic-au/refs/heads/main/screenshots/corelogic-au-2026-07-27T125335.png
security:
- kind: authentication
  name: Corelogic Au Authentication
  slug: corelogic-au-authentication
  summary_line: oauth2/openIdConnect/http · 5 schemes
- kind: domain-security
  name: Corelogic Au Domain Security
  slug: corelogic-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Corelogic Au Vulnerability Disclosure
  slug: corelogic-au-vulnerability-disclosure
  summary_line: Hackerone
slug: corelogic-au
tags:
- Real-Estate
- Australia
- Property Data
- Valuation
- AVM
- PropTech
- Property Listings
- Rentals
- Auction Data
- Commercial Real Estate
- Mortgage
- Land Registry
- Cotality
- RP Data
website: https://www.cotality.com/au
---
