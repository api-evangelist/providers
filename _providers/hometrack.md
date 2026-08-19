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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Hometrack Agentic Access
  operation_count: 59
  slug: hometrack-agentic-access
  summary_line: 59 operations · 18 acting
api_count: 6
apis:
- description: 'Hometrack''s own catalogue description is "This API provides access to the Broker AVM service." Twelve operations across two revisions (v1 and v2 paths served side by side): POST /broker/order creates '
  name: Hometrack Broker AVM API
  slug: hometrack-broker-avm-api
- description: A GraphQL API registered in Hometrack's API Management catalogue with type "graphql" and path /climate/graphql, fronting the same climate data backend (web-uks-prod-data-api.azurewebsites.net/graphql)
  name: Hometrack Climate GraphQL API
  slug: hometrack-climate-graphql-api
- description: Hometrack API Public from Hometrack — 19 path(s) described in OpenAPI.
  name: Hometrack API Public
  slug: hometrack-api-public-openapi
- description: Hometrack Climate API (v2) from Hometrack — 5 path(s) described in OpenAPI.
  name: Hometrack Climate API (v2)
  slug: hometrack-climate-api-v2-openapi
- description: Hometrack (PRH) - Core External Client API v2.0 from Hometrack — 16 path(s) described in OpenAPI.
  name: Hometrack (PRH) - Core External Client API v2.0
  slug: hometrack-prh-core-external-client-api-v2-openapi
- description: Hometrack Valuation API from Hometrack — 3 path(s) described in OpenAPI.
  name: Hometrack Valuation API
  slug: hometrack-valuation-api-v1-openapi
artifact_total: 17
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
  type: MCPServer
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: hometrack-mcp.yml
  slug: hometrack-mcpyml
modified: '2026-07-26'
name: Hometrack
nav: Providers
network: true
overview: 'Hometrack publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Broker AVM API, Climate GraphQL API, API Public, and 3 more. Tagged areas include Real Estate, United Kingdom, PropTech, Valuation, and AVM.


  Hometrack''s developer surface includes API reference, changelog, developer console, sandbox, authentication, documentation, signup flow, and 33 more developer resources.'
random_paper: 64
scopes:
- name: Hometrack Scopes
  scope_count: 2
  slug: hometrack-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 47.1
  delta: 0.8
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 49.8
    developer_ergonomics: 49.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- Real Estate
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
