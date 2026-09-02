---
access_model:
  confidence: high
  label: Free · Self-serve registration
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - authentication
  - documentation
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Energy Storage Resource public data, launched May 29, 2025 per the ERCOT Public Data API release notes, beginning with four-second ESR charging MW telemetry (GET /rptesr-m/4_sec_esr_charging_mw). Docu
  name: ERCOT ESR Public Data API
  slug: ercot-esr-public-data-api
- description: ERCOT's SOAP web-services estate for Nodal market participants — the Market Information Service, Market Transaction Service (bid and offer submission via BidSet), Resource Parameter Transaction Servic
  name: ERCOT Web Services (EWS)
  slug: ercot-web-services
- description: SOAP API over MarkeTrak, ERCOT's retail-market issue tracking system, supporting QueryList, QueryDetail, Update, and Submit operations against retail transaction issues. Applications must pass ERCOT c
  name: ERCOT MarkeTrak API
  slug: ercot-marketrak-api
- description: 'SOAP web service supporting Texas Standard Electronic Transactions (TX SET) between ERCOT, Transmission and Distribution Service Providers, and Retail Electric Providers — the machinery behind retail '
  name: ERCOT Retail API
  slug: ercot-retail-api
- description: The EMIL Products API from ERCOT — 3 operation(s) for emil products.
  name: ERCOT EMIL Products API
  slug: ercot-emil-products-api
- description: <b>Hourly Resource Outage Capacity</b><br/><br/>This report includes all approved and accepted Planned, Forced and Maintenance Resource outages EXCEPT Resource outages for retirement of old equipment,
  name: ERCOT NP3 233 CD API
  slug: ercot-np3-233-cd-api
- description: <b>Seven-Day Load Forecast by Model and Weather Zone</b><br/><br/>Hourly system-wide Mid-Term Load Forecasts (MTLFs) for all forecast models with an indicator for which forecast was in use by ERCOT at
  name: ERCOT NP3 565 CD API
  slug: ercot-np3-565-cd-api
- description: <b>Seven-Day Load Forecast by Model and Study Area</b><br/><br/>Forecasted hourly demands by Study Area, for the current day plus the next seven days.
  name: ERCOT NP3 566 CD API
  slug: ercot-np3-566-cd-api
- description: <b>2-Day Real Time Gen and Load Data Reports</b><br/><br/>This report will contain all 48 Hour disclosure data related to Real Time. The following individual files are included in the report:NP3-919-E
  name: ERCOT NP3 910 ER API
  slug: ercot-np3-910-er-api
- description: <b>2-Day Ancillary Services Reports</b><br/><br/>This report will contain all 48 Hour disclosure data related to DAM. The following individual files are included in the report:NP3-959-EX 48-hour Aggre
  name: ERCOT NP3 911 ER API
  slug: ercot-np3-911-er-api
- description: '<b>60-Day SCED Disclosure Reports</b><br/><br/>This report will contain all 60 day disclosure data related to SCED. The following individual files are included in the report: NP3-967-EX 61-day QSE-spe'
  name: ERCOT NP3 965 ER API
  slug: ercot-np3-965-er-api
- description: '<b>60-Day DAM Disclosure Reports</b><br/><br/>This report will contain all 60 day disclosure data related to DAM. The following individual files are included in the report: NP3-974-EX 61-day QSE-speci'
  name: ERCOT NP3 966 ER API
  slug: ercot-np3-966-er-api
- description: <b>60-Day SASM Disclosure Reports</b><br/><br/>This report will contain all 60 day disclosure data related to SASM for Generation and Load Resources. The following individual files are included in the
  name: ERCOT NP3 990 EX API
  slug: ercot-np3-990-ex-api
- description: <b>60-Day COP All Updates</b><br/><br/>This report will contain all iterative Current Operating Plan (COP) submissions where a change has occurred for the operating day. Previously named 60-Day Curren
  name: ERCOT NP3 991 EX API
  slug: ercot-np3-991-ex-api
- description: <b>Load Distribution Factors</b><br/><br/>Load forecast distribution factors from which Market Participants can calculate Load at the Electrical Bus level by hour for the next seven days.
  name: ERCOT NP4 159 CD API
  slug: ercot-np4-159-cd-api
- description: '<b>Total Ancillary Service Offers</b><br/><br/>The total quantity in MW of Offers per Ancillary Service per hour from the Day-Ahead Market for the last thirty days on a daily basis which includes the '
  name: ERCOT NP4 179 CD API
  slug: ercot-np4-179-cd-api
- description: <b>DAM Hourly LMPs</b><br/><br/>The Hourly Locational Marginal Prices per electrical bus from the Day-Ahead Market for the last thirty days on a daily basis.
  name: ERCOT NP4 183 CD API
  slug: ercot-np4-183-cd-api
- description: <b>DAM Clearing Prices for Capacity</b><br/><br/>The Market Clearing Prices for Capacity for all Ancillary Services from the Day-Ahead Market for the last thirty days on a daily basis.
  name: ERCOT NP4 188 CD API
  slug: ercot-np4-188-cd-api
- description: <b>DAM Settlement Point Prices</b><br/><br/>The Settlement Point Prices for all Resource Nodes, Load Zones, and Trading Hubs from the Day-Ahead Market for the last thirty days on a daily basis.
  name: ERCOT NP4 190 CD API
  slug: ercot-np4-190-cd-api
- description: <b>DAM Shadow Prices</b><br/><br/>The active and binding constraints as well as the associated shadow prices from the Day-Ahead Market for the last thirty days on a daily basis.
  name: ERCOT NP4 191 CD API
  slug: ercot-np4-191-cd-api
- description: <b>DAM Price Corrections</b><br/><br/>Day-Ahead Market price corrections.
  name: ERCOT NP4 196 M API
  slug: ercot-np4-196-m-api
- description: <b>RTM Price Corrections</b><br/><br/>Real-Time Market price corrections.
  name: ERCOT NP4 197 M API
  slug: ercot-np4-197-m-api
- description: <b>DAM Ancillary Service Plan</b><br/><br/>Ancillary Service requirements by type and quantity for each hour of the current day plus the next 6 days.
  name: ERCOT NP4 33 CD API
  slug: ercot-np4-33-cd-api
- description: <b>DAM System Lambda</b><br/><br/>System lambda of each successful DAM.
  name: ERCOT NP4 523 CD API
  slug: ercot-np4-523-cd-api
- description: <b>Wind Power Production - Hourly Averaged Actual and Forecasted Values</b><br/><br/>This report is posted every hour and includes System-wide and Regional actual hourly averaged wind power production
  name: ERCOT NP4 732 CD API
  slug: ercot-np4-732-cd-api
- description: <b>Wind Power Production - Actual 5-Minute Averaged Values</b><br/><br/>This report is posted every 5 minutes and includes System-wide and Regional actual 5-min averaged wind power production for a ro
  name: ERCOT NP4 733 CD API
  slug: ercot-np4-733-cd-api
- description: <b>Solar Power Production - Hourly Averaged Actual and Forecasted Values</b><br/><br/>This report includes System-wide actual hourly averaged solar power production, STPPF, PVGRPP, and COP HSLs for On
  name: ERCOT NP4 737 CD API
  slug: ercot-np4-737-cd-api
- description: <b>Solar Power Production - Actual 5-Minute Averaged Values</b><br/><br/>This report is posted every 5 minutes and includes System-wide actual 5-minute averaged solar power production for On-Line PVGR
  name: ERCOT NP4 738 CD API
  slug: ercot-np4-738-cd-api
- description: <b>Wind Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region</b><br/><br/>This report is posted every hour and includes System-wide and Geographic Regional actual hou
  name: ERCOT NP4 742 CD API
  slug: ercot-np4-742-cd-api
- description: <b>Wind Power Production - Actual 5-Minute Averaged Values by Geographical Region</b><br/><br/>This report is posted every 5 minutes and includes System-wide and Geographic Regional actual 5-minute av
  name: ERCOT NP4 743 CD API
  slug: ercot-np4-743-cd-api
- description: <b>Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region</b><br/><br/>This report is posted every hour and includes System-wide and geographic regional hourly av
  name: ERCOT NP4 745 CD API
  slug: ercot-np4-745-cd-api
- description: <b>Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region</b><br/><br/>This report is posted every 5 minutes and includes system-wide and geographic regional 5-minute averaged
  name: ERCOT NP4 746 CD API
  slug: ercot-np4-746-cd-api
- description: <b>SCED System Lambda</b><br/><br/>System lambda of each successful SCED.
  name: ERCOT NP6 322 CD API
  slug: ercot-np6-322-cd-api
- description: <b>Actual System Load by Weather Zone</b><br/><br/>Report of Actual hourly load data by weather zone and ERCOT total.
  name: ERCOT NP6 345 CD API
  slug: ercot-np6-345-cd-api
- description: <b>Actual System Load by Forecast Zone</b><br/><br/>A daily report of Actual System Load by Forecast Zone for each hour of the previous operating day.
  name: ERCOT NP6 346 CD API
  slug: ercot-np6-346-cd-api
- description: <b>LMPs by Electrical Bus</b><br/><br/>The Locational Marginal Price for each Electrical Bus, normally produced by SCED every five minutes.
  name: ERCOT NP6 787 CD API
  slug: ercot-np6-787-cd-api
- description: <b>LMPs by Resource Nodes, Load Zones and Trading Hubs</b><br/><br/>The Locational Marginal Price for each Settlement Point, normally produced by SCED every five minutes.
  name: ERCOT NP6 788 CD API
  slug: ercot-np6-788-cd-api
- description: '<b>SCED Shadow Prices and Binding Transmission Constraints</b><br/><br/>The report for Shadow Prices of binding/violated constraints in SCED. The report shows the contingency name, overloaded element '
  name: ERCOT NP6 86 CD API
  slug: ercot-np6-86-cd-api
- description: <b>Settlement Point Prices at Resource Nodes, Hubs and Load Zones</b><br/><br/>Settlement Point Price for each Settlement Point, produced from SCED LMPs every 15 minutes.
  name: ERCOT NP6 905 CD API
  slug: ercot-np6-905-cd-api
- description: <b>RTD Indicative LMPs by Resource Nodes, Load Zones and Hubs</b><br/><br/>This report is posted after every Look Ahead RTD run and includes indicative LMPs at Resource Nodes, Hub LMPs and Load Zone f
  name: ERCOT NP6 970 CD API
  slug: ercot-np6-970-cd-api
- description: The Versioning API from ERCOT — 1 operation(s) for versioning.
  name: ERCOT Versioning API
  slug: ercot-versioning-api
artifact_total: 48
asyncapis:
- description: ''
  name: Ercot Ews Notifications
  slug: ercot-ews-notifications
collections:
- collection_type: open
  name: ERCOT Public API Client/Developer Documentation
  slug: open-ercot-public-data-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ercot-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ercot-public-data-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ercot/ews-client/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ercot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ercot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ercot-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ercot-well-known.yml
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/ercot-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/ercot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ercot-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ercot-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ercot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.ercot.com/applications/pubapi/deprecation-notices/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ercot-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ercot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ercot-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ercot-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ercot-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ercot-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ercot-ews-notifications.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ercot-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ercot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ercot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ercot.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apiexplorer.ercot.com/api-details#api=pubapi-apim-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ercot.com/applications/pubapi/user-guide/registration-and-authentication/
- group: other
  title: ''
  type: APIExplorer
  url: https://apiexplorer.ercot.com/
- group: start
  title: ''
  type: SignUp
  url: https://apiexplorer.ercot.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.ercot.com/support/support/
- group: operate
  title: ''
  type: Community
  url: https://developer.ercot.com/discussion_forums/discussion/
- group: commercial
  title: ''
  type: Plans
  url: https://apiexplorer.ercot.com/products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ercot.com/help/terms/data-portal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ercot.com/help/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ercot
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ercot/api-specs
- group: other
  title: ''
  type: OpenData
  url: https://data.ercot.com/
- group: other
  title: ''
  type: OpenData
  url: https://www.ercot.com/mp/data-products
- group: operate
  title: ''
  type: Issues
  url: https://github.com/ercot/api-specs/issues
created: '2026-07-27'
description: 'The Electric Reliability Council of Texas (ERCOT) is the independent system operator that manages the flow of electric power to roughly 27 million Texas customers on the ERCOT Interconnection, running the wholesale Day-Ahead and Real-Time energy markets, ancillary services, congestion revenue rights, and retail switching for the competitive Texas market. Its home market is the United States (Texas). ERCOT sits at the wholesale/system-operator layer of the energy value chain, upstream of the transmission and distribution utilities (Oncor, CenterPoint, AEP Texas, TNMP) and the retail electric providers that serve end customers. Its API posture is a clean split: market and grid data are genuinely open — ERCOT publishes a real, versioned OpenAPI 3.0 for the Public Data API covering 106 EMIL data-product endpoints (locational marginal prices, settlement point prices, system load, wind and solar production, ancillary services, outage capacity), and the Market Information System still
  serves public report archives anonymously with no account at all. Consumer energy data is a different story: ERCOT operates no consumer usage API and implements no Green Button / ESPI surface. Texas residential interval data lives in Smart Meter Texas, which is operated by the joint Transmission and Distribution Utilities under PUCT oversight, not by ERCOT. The market-participant SOAP estate (ERCOT Web Services, MarkeTrak, Retail API) is documented publicly on GitHub but reachable only by certified market participants.'
layout: provider
mcp_servers:
- description: 'ERCOT publishes no first-party MCP server. Searching the developer portal, the ERCOT GitHub organization and the npm registry turns up no ERCOT-operated hosted or stdio MCP endpoint, and no agent/LLM '
  name: ERCOT MCP Server
  slug: ercot-mcp-server
modified: '2026-07-27'
name: ERCOT
nav: Providers
network: true
overview: 'ERCOT publishes 37 APIs on the [APIs.io](https://apis.io/) network, including EMIL Products API, NP3 233 CD API, NP3 565 CD API, and 34 more. Tagged areas include Energy, United States, Electricity, Energy Markets, and Grid.


  The ERCOT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ERCOT''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, signup flow, support, and 32 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 2
  name: Ercot Rate Limits
  slug: ercot-rate-limits
scopes:
- name: Ercot Scopes
  scope_count: 3
  slug: ercot-scopes
  summary_line: 3 scopes · password
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 63.0
    developer_ergonomics: 56.5
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 54.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 67.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ercot/refs/heads/main/screenshots/ercot-2026-08-07T164957.png
security:
- kind: authentication
  name: Ercot Authentication
  slug: ercot-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Ercot Domain Security
  slug: ercot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ercot
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- System Operator
- Texas
- Renewables
- Demand Response
- Open Data
website: https://www.ercot.com/
---
