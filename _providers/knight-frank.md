---
access_model:
  confidence: high
  label: No published developer programme · one unadvertised anonymous API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probes
  - website
  - openapi
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Knight Frank Agentic Access
  operation_count: 11
  slug: knight-frank-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 1
apis:
- description: The CMSPage API from Knight Frank — 1 operation(s) for cmspage.
  name: Knight Frank CMS Page API
  slug: knight-frank-cmspage-api
- description: The IntelligenceLab API from Knight Frank — 2 operation(s) for intelligencelab.
  name: Knight Frank Intelligence Lab API
  slug: knight-frank-intelligencelab-api
- description: The Office API from Knight Frank — 2 operation(s) for office.
  name: Knight Frank Office API
  slug: knight-frank-office-api
- description: The Person API from Knight Frank — 3 operation(s) for person.
  name: Knight Frank Person API
  slug: knight-frank-person-api
- description: The Search API from Knight Frank — 1 operation(s) for search.
  name: Knight Frank Search API
  slug: knight-frank-search-api
- description: The ServiceLine API from Knight Frank — 1 operation(s) for serviceline.
  name: Knight Frank Service Line API
  slug: knight-frank-serviceline-api
- description: The Telemetry API from Knight Frank — 1 operation(s) for telemetry.
  name: Knight Frank Telemetry API
  slug: knight-frank-telemetry-api
arazzos:
- description: Search the Knight Frank office directory, then fetch the full record for the best-matching office.
  name: Knight Frank office lookup
  slug: knight-frank-office-lookup
artifact_total: 14
collections:
- collection_type: open
  name: KnightFrank Api v3
  slug: open-knight-frank-api-v3
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knight-frank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knight-frank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knight-frank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/knight-frank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knight-frank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knight-frank-error-responses.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knight-frank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knight-frank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knight-frank-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/knight-frank-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/knight-frank-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/knight-frank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knight-frank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/knight-frank-api-v3-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knight-frank-office-lookup.yml
- group: operate
  title: ''
  type: Support
  url: https://www.knightfrank.co.uk/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.knightfrank.co.uk/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.knightfrank.com/legals/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.knightfrank.com/legals/privacy-statement
- group: company
  title: ''
  type: Website
  url: https://www.knightfrank.com/
- group: company
  title: ''
  type: WebsiteUK
  url: https://www.knightfrank.co.uk/
- group: company
  title: ''
  type: WebsiteUS
  url: https://www.knightfrank.com/usa
- group: other
  title: ''
  type: PropertySearch
  url: https://www.knightfrank.co.uk/properties/residential/for-sale/london
- group: other
  title: ''
  type: Research
  url: https://www.knightfrank.com/research
- group: other
  title: ''
  type: Account
  url: https://account.knightfrank.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.knightfrank.co.uk/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.knightfrank.com/recruitment
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/knight-frank
- group: other
  title: ''
  type: OpenIDConfiguration
  url: authentication/knight-frank-b2c-mykfsignin-openid-configuration.json
- group: other
  title: ''
  type: OpenIDConfiguration
  url: authentication/knight-frank-b2clogin-mykfsignin-openid-configuration.json
created: '2026-07-26'
description: 'Knight Frank LLP is a London-headquartered global real estate consultancy founded in 1896, structured as a partnership rather than a listed company, operating through a network of over 700 offices in more than 50 territories and best known for prime and super-prime residential agency, commercial agency and occupier services, valuation and advisory, capital markets, rural and agricultural consultancy, and the Knight Frank Research programme that publishes The Wealth Report and the Prime International Residential Index. It sits on the advisory and agency side of the property value chain rather than the data-platform side. Its home market is the United Kingdom, where there is no MLS and no cooperative listing standard — residential stock reaches consumers through the Rightmove and Zoopla duopoly by way of agency CRM software (Reapit, Alto, Street, Apex27) rather than a shared cooperative pool, so Knight Frank is a supplier into that pipe and not an operator of it. Its API posture
  is honest but unflattering: Knight Frank publishes no developer portal, no API programme, no developer terms, no SDK and no Postman collection, and every conventional developer entry point fails — developer., developers., docs. and apis.knightfrank.com do not resolve in DNS, and /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs all return 404 on knightfrank.com and knightfrank.co.uk. On the UK site /developers is a homonym trap: it redirects to a commercial services page for property developers and housebuilders, not software developers. What does exist, entirely unadvertised, is a real machine-readable contract. The corporate search service at api-v3.web.prd-knightfrank.com serves a live Swagger UI and an OpenAPI 3.0.1 document (11 GET/POST operations across CMSPage, IntelligenceLab, Office, Person, Search, ServiceLine and Telemetry) to anonymous clients, and those endpoints answer with real office and people-directory data without any credential. The property search
  and saved-property service at api-v2.web.prd-knightfrank.com is the opposite: it returns 401 and is protected by Azure AD B2C (tenant KnightFrankB2Cprod, custom policy B2C_1A_MYKFSIGNIN, scope MyKf.ReadWrite) through a first-party MSAL client for the consumer My Knight Frank account, which is an end-user login and not a developer credential. There is no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier anywhere in the Knight Frank estate — RESO is a North American NAR/MLS construct and the United Kingdom has no MLS to certify against. Knight Frank publishes no open data either; its research ships as PDF and web narrative, and the genuinely open UK property layer belongs to the public sector — HM Land Registry Price Paid Data and Ordnance Survey open products — not to the brokerage.'
image: https://www.knightfrank.com/icons/apple-touch-icon-180x180.png
layout: provider
mcp_servers:
- description: Knight Frank operates NO Model Context Protocol server. Searches on 2026-07-26 found no MCP server in the provider's estate, no @knightfrank package on npm, no entry in any public MCP registry, no /mc
  name: Knight Frank MCP Server
  slug: knight-frank-mcp-server
modified: '2026-07-26'
name: Knight Frank
nav: Providers
network: true
overview: 'Knight Frank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including CMS Page API, Intelligence Lab API, Office API, and 4 more. Tagged areas include Real-Estate, United Kingdom, Property Listings, Commercial Real Estate, and Valuation.


  Knight Frank''s developer surface includes authentication, support, engineering blog, and 28 more developer resources.'
random_paper: 2
scopes:
- name: Knight Frank Scopes
  scope_count: 2
  slug: knight-frank-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 29.3
    developer_ergonomics: 28.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.6
  provenance:
    agentic_access: derived
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
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knight-frank/refs/heads/main/screenshots/knight-frank-2026-08-07T171255.png
security:
- kind: authentication
  name: Knight Frank Authentication
  slug: knight-frank-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Knight Frank Domain Security
  slug: knight-frank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knight-frank
tags:
- Real-Estate
- United Kingdom
- Property Listings
- Commercial Real Estate
- Valuation
- Brokerage
- Property Management
- Rentals
- PropTech
- Research
website: https://www.knightfrank.com/
---
