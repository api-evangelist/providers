---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-09-05'
api_count: 11
apis:
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Xpansiv Connect exposes environmental commodity account, portfolio, exchange, forward deal, issuance, project, reference data, report, retirement, split lot and transfer operations over REST. Bearer t
  name: Xpansiv Connect API
  slug: xpansiv-connect
- baseURL: https://www.ms.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Access facilities, transactions, meter readings, clean transportation, market, qualified reporting entity, building type, remote data collector and utility data from an Xpansiv Managed Solutions accou
  name: Xpansiv Managed Solutions API
  slug: xpansiv-managed-solutions
- description: Real-time, end-of-day and historical transaction-based market data for environmental and energy commodities, sourced from CBL and global intermediaries including Evolution Markets. Delivered as time s
  name: Xpansiv Data API
  slug: xpansiv-data
- baseURL: https://narenewables2.apx.com/ClientAPI
  baseurl_source: declared
  description: 'The North American Renewables Registry client API for retrieving and transacting NAR monthly vintage renewable energy certificates — account, ledger, subaccount and system operations behind an OAuth2 '
  name: NAR Registry Client API
  slug: xpansiv-nar-registry
- baseURL: https://tigrsregistry.apx.com/clientapi
  baseurl_source: declared
  description: The Tradable Instrument for Global Renewables (TIGR) registry client API for retrieving and retiring TIGR certificates — corporate entity, ledger, subaccount and system operations behind an OAuth2 pas
  name: TIGRS Registry Client API
  slug: xpansiv-tigr-registry
- baseURL: https://optimalapi-ext.apx.com
  baseurl_source: declared
  description: The Optimal Outcomes suite — a system health API, a file registry, a meter-data telemetry API, a reporting service, a resource API and a transfer position external API for viewing and managing environ
  name: Xpansiv Optimal Outcomes APIs
  slug: xpansiv-optimal-outcomes
- baseURL: https://pm-file-api.apx.com
  baseurl_source: declared
  description: 'The APX MarketSuite file registry and reporting API used to submit and retrieve ISO scheduling files for CAISO, ERCOT, PJM, SPP, MISO, ISONE and NYISO, alongside the XML/XSD schedule schemas and REST '
  name: APX Power Markets File Registry API
  slug: xpansiv-apx-power-markets
- description: The Xpansiv Marketplace Server API for retrieving real-time market data and executing and managing orders on CBL, published as rules of engagement against the FIX 4.4 specification from the FIX Tradin
  name: Xpansiv Marketplace FIX API
  slug: xpansiv-marketplace-fix
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.xpansiv.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.xpansiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.xpansiv.com/developer-portal
- group: docs
  title: ''
  type: APIReference
  url: https://developer.xpansiv.com/developer-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.xpansiv.com/developer-portal/xpansiv-connect/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.xpansiv.com/
- group: start
  title: ''
  type: SignUp
  url: https://connect.xpansiv.com/app/login/
- group: company
  title: ''
  type: Blog
  url: https://www.xpansiv.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xpansiv.com/general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xpansiv.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://developer.xpansiv.com/developer-portal/xpansiv-power/rest_api/postman
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xpansiv-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xpansiv-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/xpansiv-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xpansiv-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/xpansiv-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/xpansiv-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xpansiv-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xpansiv-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xpansiv-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xpansiv-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xpansiv-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xpansiv-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xpansiv-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xpansiv-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xpansiv-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xpansiv-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/xpansiv-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/xpansiv-connect-overlay.yaml
created: '2026-09-04'
description: Xpansiv is market infrastructure for global environmental and energy commodities — carbon credits, renewable energy certificates, water, low-carbon fuels and recycled materials. It operates CBL, the largest spot exchange for environmental commodities, the Evolution Markets and OTX brokerage and execution desks, the H2OX water market and the ACE and JSEV carbon platforms, alongside the environmental registries it acquired with APX in 2022 — NAR (North American Renewables Registry), TIGR, I-REC, I-TRACK-G and the Xpansiv-powered digital fuels registries. Its public developer portal at developer.xpansiv.com publishes eleven OpenAPI descriptions across Xpansiv Connect (environmental commodity portfolio, retirement and transfer), Xpansiv Managed Solutions, the NAR and TIGR registry client APIs, the Optimal Outcomes suite and the APX Power Markets file registry, plus a FIX 4.4 marketplace protocol specification, Xpansiv Data market-data APIs and a first-party Python SDK.
image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Xpansiv Developer Portal MCP Server
  slug: xpansiv-developer-portal-mcp-server
modified: '2026-09-04'
name: Xpansiv
nav: Providers
network: true
overview: 'Xpansiv publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Connect API, Managed Solutions API, NAR Registry Client API, and 3 more. Tagged areas include Company, Environmental Commodities, Carbon Markets, Renewable Energy Certificates, and Registries.


  Xpansiv''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Xpansiv Plans Pricing
  plan_count: 0
  slug: xpansiv-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Xpansiv Rate Limits
  slug: xpansiv-rate-limits
scopes:
- name: Xpansiv Scopes
  scope_count: 0
  slug: xpansiv-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 56.8
    developer_ergonomics: 78.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 51.8
  provenance:
    conformance: first-party
    contracts:
      callable: 90.9
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Xpansiv Authentication
  slug: xpansiv-authentication
  summary_line: http (bearer)/http (basic)/apiKey · 3 schemes
- kind: domain-security
  name: Xpansiv Domain Security
  slug: xpansiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xpansiv
tags:
- Company
- Environmental Commodities
- Carbon Markets
- Renewable Energy Certificates
- Registries
- Market Data
- Trading
- Energy
- Sustainability
- Climate
website: https://www.xpansiv.com/
---
