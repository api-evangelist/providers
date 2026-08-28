---
access_model:
  confidence: high
  label: Open public market data · Member-gated participant APIs
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - documentation
  trial: false
  try_now: true
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.3
  scored_at: '2026-08-26'
api_count: 6
apis:
- description: 'SPP''s officially documented programmatic interface to its public data. The SPP Public Data Access guide (v3.0, July 2023) names FTP as the programmatic access path for Integrated Marketplace, Western '
  name: SPP Public Data FTP
  slug: spp-public-data-ftp
- description: 'The HTTP download service behind the SPP Portal public data pages. Anonymous GET requests of the form /file-browser-api/download/{dataset}?path={file} return CSV for real-time balancing market LMP by '
  name: SPP Portal Public Data File Browser API
  slug: spp-portal-file-browser-api
- description: 'JSON and CSV chart feeds serving the SPP Portal dashboards. Confirmed anonymously on 2026-07-27: /chart-api/gen-mix/asChart and /chart-api/load-forecast/asChart return application/json with labelled h'
  name: SPP Portal Chart API
  slug: spp-portal-chart-api
- description: 'An Esri ArcGIS Server REST directory serving the geospatial layers behind SPP''s price contour map. Confirmed anonymously on 2026-07-27 at ArcGIS 11.5: the service root returned JSON listing the PCM an'
  name: SPP Price Contour Map ArcGIS REST Services
  slug: spp-price-contour-map-arcgis
- description: 'SPP''s REST implementation of GE Vernova''s Limit Exchange Portal (LEP) using the LF Energy TROLIE (Transmission Ratings and Operating Limits Information Exchange) API specification, built to meet FERC '
  name: SPP LEP/TROLIE Ratings API
  slug: spp-lep-trolie-api
- description: The SOAP web and notification services market participants use to submit offers and bids and retrieve results from the SPP Integrated Marketplace, with WEIS Markets Web Service as the western equivale
  name: SPP Integrated Marketplace Markets Web Service
  slug: spp-integrated-marketplace-web-services
artifact_total: 14
collections:
- collection_type: open
  name: Transmission Ratings and Operating Limits Information Exchange (TROLIE)
  slug: open-trolie-standard
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spp-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spp-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spp-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spp-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spp-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spp-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spp-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spp-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spp-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spp-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/spp-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spp-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.spp.org/
- group: start
  title: ''
  type: Portal
  url: https://portal.spp.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.spp.org/stakeholder-center/user-guides-apis-integrations/
- group: start
  title: ''
  type: GettingStarted
  url: https://spp.org/documents/28853/spp%20public%20data%20access%2020230707.pdf
- group: operate
  title: ''
  type: Roadmap
  url: https://www.spp.org/stakeholder-center/spp-roadmap/
- group: auth
  title: ''
  type: Compliance
  url: https://www.spp.org/stakeholder-center/spp-rto-compliance/
- group: start
  title: ''
  type: SignUp
  url: https://www.spp.org/account/create-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spp.org/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spp.org/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://rms.spp.org/
- group: company
  title: ''
  type: Blog
  url: https://www.spp.org/newsroom/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southwest-power-pool
- group: company
  title: ''
  type: Twitter
  url: https://www.twitter.com/spporg
created: '2026-07-27'
description: 'Southwest Power Pool (SPP) is a nonprofit Regional Transmission Organization regulated by the Federal Energy Regulatory Commission and headquartered in Little Rock, Arkansas. Founded in 1941 and approved as an RTO in 2004, SPP operates the Integrated Marketplace day-ahead and real-time balancing markets, the Western Energy Imbalance Service (WEIS) market, Western Reliability Coordination services, and is building the Markets+ day-ahead market for the West with a targeted 2027 go-live. SPP sits at the wholesale layer of the United States energy value chain: it dispatches generation, prices congestion, plans transmission, and settles the market for its member utilities — it has no retail customers, so no consumer energy-data mandate such as Green Button applies to it. Its API posture is a clean split. Market and grid data is genuinely open: locational marginal prices, market clearing prices, operating reserves, load, generation mix, VER curtailments and outage capacity are served
  anonymously as CSV from the SPP Portal file browser and from an anonymous public FTP site, with an Esri ArcGIS REST price-contour service alongside — no account, no key, no licence click-through. Everything a market participant actually transacts against is the opposite: the Integrated Marketplace SOAP web services, the Settlement Management System API, and the FERC Order 881 LEP/TROLIE ratings API are member-only, require an OATI webCARES x.509 digital certificate plus an SPP UAA role, and SPP publishes no base URL and no OpenAPI for them.'
examples:
- key_count: 5
  name: Spp Arcgis Rest Info
  slug: spp-arcgis-rest-info
- key_count: 36
  name: Spp Arcgis Rtbm Lmp Mapserver
  slug: spp-arcgis-rtbm-lmp-mapserver
- key_count: 3
  name: Spp Chart Api Gen Mix
  slug: spp-chart-api-gen-mix
image: https://www.spp.org/logo.png
layout: provider
modified: '2026-07-27'
name: Southwest Power Pool
nav: Providers
network: true
overview: 'Southwest Power Pool publishes 1 API on the [APIs.io](https://apis.io/) network: SPP LEP/TROLIE Ratings API. Tagged areas include Energy, United States, Energy Markets, Electricity, and Grid.


  Southwest Power Pool''s developer surface includes authentication, sandbox, code examples, developer portal, documentation, getting-started guide, signup flow, and 21 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Spp Rate Limits
  slug: spp-rate-limits
scopes:
- name: Spp Scopes
  scope_count: 15
  slug: spp-scopes
  summary_line: 15 scopes · clientCredentials
score:
  band: developing
  composite: 53.6
  delta: 0.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 16.7
    contract_quality: 63.2
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 5.3
  previous_composite: 52.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spp/refs/heads/main/screenshots/spp-2026-08-17T082042.png
security:
- kind: authentication
  name: Spp Authentication
  slug: spp-authentication
  summary_line: none/apiKey/mutualTLS/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Spp Domain Security
  slug: spp-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: spp
tags:
- Energy
- United States
- Energy Markets
- Electricity
- Grid
- Utilities
- Renewables
- Market Data
- Transmission
- System Operator
website: https://www.spp.org/
---
