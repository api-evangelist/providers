---
access_model:
  confidence: high
  label: Paid · Commercial agreement required · Documentation and OpenAPI contracts public, data gated behind Auth0 client credentials issued by Hometrack
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - developer-portal
  - api-authentication
  - gateway-probe
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Hometrack Agentic Access
  operation_count: 59
  slug: hometrack-agentic-access
  summary_line: 59 operations · 18 acting
api_count: 6
apis:
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Authentication API from Hometrack — 2 operation(s) for authentication.
  name: Hometrack Authentication API
  slug: hometrack-authentication-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Brands API from Hometrack — 1 operation(s) for brands.
  name: Hometrack Brands API
  slug: hometrack-brands-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Broker API from Hometrack — 10 operation(s) for broker.
  name: Hometrack Broker API
  slug: hometrack-broker-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Epc Hometrack API from Hometrack — 1 operation(s) for epc hometrack.
  name: Hometrack Epc Hometrack API
  slug: hometrack-epc-hometrack-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Flood Twinn API from Hometrack — 1 operation(s) for flood twinn.
  name: Hometrack Flood Twinn API
  slug: hometrack-flood-twinn-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Ground Coastalerosion Twinn API from Hometrack — 1 operation(s) for ground coastalerosion twinn.
  name: Hometrack Ground Coastalerosion Twinn API
  slug: hometrack-ground-coastalerosion-twinn-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Ground Subsidence Twinn API from Hometrack — 1 operation(s) for ground subsidence twinn.
  name: Hometrack Ground Subsidence Twinn API
  slug: hometrack-ground-subsidence-twinn-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Ground Terrafirma API from Hometrack — 1 operation(s) for ground terrafirma.
  name: Hometrack Ground Terrafirma API
  slug: hometrack-ground-terrafirma-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Internal API from Hometrack — 2 operation(s) for internal.
  name: Hometrack Internal API
  slug: hometrack-internal-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Licences API from Hometrack — 1 operation(s) for licences.
  name: Hometrack Licences API
  slug: hometrack-licences-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Organisation API from Hometrack — 16 operation(s) for organisation.
  name: Hometrack Organisation API
  slug: hometrack-organisation-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Partners API from Hometrack — 2 operation(s) for partners.
  name: Hometrack Partners API
  slug: hometrack-partners-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Pvrplugin API from Hometrack — 4 operation(s) for pvrplugin.
  name: Hometrack Pvrplugin API
  slug: hometrack-pvrplugin-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Reporting API from Hometrack — 7 operation(s) for reporting.
  name: Hometrack Reporting API
  slug: hometrack-reporting-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Status API from Hometrack — 1 operation(s) for status.
  name: Hometrack Status API
  slug: hometrack-status-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Trial API from Hometrack — 2 operation(s) for trial.
  name: Hometrack Trial API
  slug: hometrack-trial-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Valuation API from Hometrack — 1 operation(s) for valuation.
  name: Hometrack Valuation API
  slug: hometrack-valuation-api
- baseURL: https://api.hometrack.com/valuation/v2
  baseurl_source: declared
  description: The Zoopla API from Hometrack — 1 operation(s) for zoopla.
  name: Hometrack Zoopla API
  slug: hometrack-zoopla-api
artifact_total: 28
collections:
- collection_type: open
  name: Hometrack API Public
  slug: open-hometrack-api-public
- collection_type: open
  name: Broker Avm API
  slug: open-hometrack-broker-avm-api
- collection_type: open
  name: Climate API (v2)
  slug: open-hometrack-climate-api-v2
- collection_type: open
  name: Climate GraphQL
  slug: open-hometrack-climate-graphql-api
- collection_type: open
  name: (PRH) - Core External Client API v2.0
  slug: open-hometrack-prh-core-external-client-api-v2
- collection_type: open
  name: Valuation API
  slug: open-hometrack-valuation-api-v1
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hometrack-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hometrack-broker-avm-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hometrack-climate-graphql-api-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hometrack.com/apis
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.hometrack.com/api-changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hometrack-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.hometrack.com/
- group: start
  title: ''
  type: Console
  url: https://developer.hometrack.com/apis
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hometrack-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hometrack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hometrack-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hometrack-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hometrack-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hometrack-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hometrack-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/hometrack-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hometrack-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/hometrack-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hometrack-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hometrack-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hometrack-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hometrack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hometrack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hometrack-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hometrack.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hometrack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hometrack.com/apis
- group: auth
  title: ''
  type: Authentication
  url: https://developer.hometrack.com/api-authentication
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: authentication/hometrack-auth0-openid-configuration.json
- group: start
  title: ''
  type: SignUp
  url: https://developer.hometrack.com/signup
- group: other
  title: ''
  type: SignIn
  url: https://developer.hometrack.com/signin
- group: operate
  title: ''
  type: ContactUs
  url: https://www.hometrack.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://www.hometrack.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.hometrack.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.hometrack.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.hometrack.com/press-releases/
- group: company
  title: ''
  type: Newsroom
  url: https://www.hometrack.com/newsroom/uk-house-price-index/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hometrack.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hometrack.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.hometrack.com/iso-27001/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hometrack
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/hometrack
created: '2026-07-26'
description: 'Hometrack is a United Kingdom property data, valuation and risk-decisioning company, founded in 1999 and now part of Houseful — the Silver Lake-owned group that also owns Zoopla, PrimeLocation, Alto and Jupix. It launched its automated valuation model in 2002 and says it now runs more than 50 million valuations a year, that 18 of the top 20 UK mortgage lenders use its AVM in their origination processes, and that it was the first AVM accredited by Moody''s, Standard & Poor''s and Fitch. It is a founding member of the European AVM Alliance. In the UK value chain it does not sit on the listings side at all: with no MLS in this market, residential listings are controlled by Rightmove and Zoopla and reach them through agency CRM software, while Hometrack sits on the lending and risk side — valuation, comparables, climate and property risk data, surveyor allocation and case management for mortgage lenders, surveyors, brokers, housing associations and investors. Its API posture is
  unusually revealing and must be stated in two halves. The developer surface is real and genuinely public: an Azure API Management developer portal at developer.hometrack.com is served anonymously, its data plane answers unauthenticated requests, and six APIs — a Valuation API, a Broker AVM API, a Property Risk Hub core client API, a Climate API, a Climate GraphQL API and an internal-facing public API — are listed there with full operation and schema metadata, from which six OpenAPI 3.0.1 documents were harvested. The access gate, however, is commercial: the portal states plainly that "to interact with any of our APIs you will need to have a valid API Key for that respective product. If you do not yet have an API Key, please contact us", and the gateway at api.hometrack.com answers anonymous calls with HTTP 401 "Unauthorized. Access token is missing or invalid." Authentication is OAuth 2.0 client credentials through Auth0 (hometrack-prod.eu.auth0.com) against the audience https://api.hometrack.com,
  with documented scopes read:valuations and write:valuations. So: contracts are readable by anyone, data is reachable by nobody without a Hometrack commercial agreement. There is no RESO Web API or Data Dictionary certification and no OData $metadata anywhere in Hometrack''s stack — RESO is a North American NAR/MLS construct and the UK has no MLS to certify against. Notably, Hometrack''s Climate API keys every property off the UPRN, the Unique Property Reference Number issued by GeoPlace and distributed by Ordnance Survey: the UK does have a universal property identifier, it just comes from government rather than from a real-estate standards body. Hometrack itself publishes no open data — the open UK property layer is HM Land Registry Price Paid and Ordnance Survey, not Hometrack.'
layout: provider
modified: '2026-07-26'
name: Hometrack
nav: Providers
network: true
overview: 'Hometrack publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Brands API, Broker API, and 15 more. Tagged areas include Real-Estate, United Kingdom, PropTech, Valuation, and AVM.


  Hometrack''s developer surface includes API reference, changelog, developer console, sandbox, authentication, documentation, signup flow, and 36 more developer resources.'
random_paper: 13
scopes:
- name: Hometrack Scopes
  scope_count: 2
  slug: hometrack-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 54.1
    developer_ergonomics: 49.4
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hometrack/refs/heads/main/screenshots/hometrack-2026-08-07T170250.png
security:
- kind: authentication
  name: Hometrack Authentication
  slug: hometrack-authentication
  summary_line: oauth2/apiKey/http · 5 schemes
- kind: domain-security
  name: Hometrack Domain Security
  slug: hometrack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hometrack
tags:
- Real-Estate
- United Kingdom
- PropTech
- Valuation
- AVM
- Mortgage
- Property Data
- Climate Risk
- Lending
- Surveying
website: https://www.hometrack.com/
---
