---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ssen Agentic Access
  operation_count: 16
  slug: ssen-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- description: The public CKAN 2.10.10 Action API behind the SSEN Distribution Data Portal, serving 45 open datasets covering substations, LV feeder smart meter half-hourly usage, the Embedded Capacity Register, fle
  name: SSEN Distribution Data Portal API
  slug: ssen-distribution-data-portal-api
- description: 'Anonymous JSON API behind the SSEN Power Track map, returning planned and unplanned outages on the SSEN Distribution network with fault reference, type, latitude/longitude, estimated restoration time '
  name: SSEN Power Track Real Time Outage API
  slug: ssen-power-track-real-time-outage-api
- description: Near real-time power flow data from SSEN Distribution's EHV, HV and LV networks, drawn from SCADA PowerOn, LV monitoring equipment, the load model forecasting tool, the connectivity model and the Long
  name: SSEN NeRDA (Near Real-time Data Access) API
  slug: ssen-nerda-api
- baseURL: https://data-api.ssen.co.uk/api/3/action
  baseurl_source: declared
  description: API to enumerate datasets
  name: Scottish and Southern Electricity Networks Catalog API
  slug: ssen-catalog-api
- baseURL: https://data-api.ssen.co.uk/api/3/action
  baseurl_source: declared
  description: API to work on records
  name: Scottish and Southern Electricity Networks Dataset API
  slug: ssen-dataset-api
artifact_total: 11
collections:
- collection_type: open
  name: Explore API
  slug: open-ssen-transmission-opendatasoft-explore-v2
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ssen-transmission-opendatasoft-explore-v2.1-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ssen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ssen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ssen-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ssen-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ssen-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ssen-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ssen-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ssen-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ssen-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ssen-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ssen-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ssen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://ssentransmission.opendatasoft.com/.well-known/security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ssen-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ssen-llms.txt
- group: operate
  title: ''
  type: Roadmap
  url: https://data.ssen.co.uk/@ssen-distribution/ssen-distribution-data-roadmap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.ssen.co.uk/
- group: start
  title: ''
  type: GettingStarted
  url: https://raw.githubusercontent.com/datopian/ssen-content/refs/heads/dev/assets/Portal_Guide.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.ssen.co.uk/about-ssen/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://data.ssen.co.uk/faq
- group: company
  title: ''
  type: Blog
  url: https://www.ssen.co.uk/news-views/
- group: start
  title: ''
  type: SignUp
  url: https://data.ssen.co.uk/auth/signup
- group: start
  title: ''
  type: Login
  url: https://data.ssen.co.uk/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.ssen.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ssen.co.uk/privacy-notice/
- group: company
  title: ''
  type: Website
  url: https://www.ssen.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://data.ssen.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://data.ssen.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://ssentransmission.opendatasoft.com/
- group: start
  title: ''
  type: Portal
  url: https://nerda.ssen.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.ssen-transmission.co.uk/
- group: company
  title: ''
  type: Website
  url: https://ssen-innovation.co.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ssen
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCUCGdsJ4g3drX9GBvqRH01A
created: '2026-07-27'
description: Scottish and Southern Electricity Networks (SSEN) is the SSE plc electricity networks business in the United Kingdom, operating the poles-and-wires layer rather than selling energy. SSEN Distribution is the licensed Distribution Network Operator for two GB licence areas — Scottish Hydro Electric Power Distribution (SHEPD) in the north of Scotland and Southern Electric Power Distribution (SEPD) in central southern England — serving over 3.9 million homes and businesses, while SSEN Transmission owns and operates the high-voltage transmission system for the north of Scotland. Its API posture is the classic network-distributor split — grid and market data are genuinely open, consumer data is not offered at all. SSEN runs a CKAN open data portal whose anonymous Action API serves 45 datasets, an anonymous real-time outage API behind Power Track, a key-gated near-real-time power-flow API (NeRDA) covering EHV/HV/LV networks, and an Opendatasoft Explore API over 60 transmission datasets.
  There is no consumer data-portability mandate in Great Britain equivalent to the Australian Consumer Data Right or Ontario's Green Button regulation, and SSEN publishes no API through which a third party can obtain an individual customer's usage or billing data. What Britain mandated instead is infrastructure and disclosure — smart meter traffic runs through the licensed Smart DCC monopoly, and Ofgem's Data Best Practice licence condition under RIIO-ED2 obliges network licensees to treat data assets as Presumed Open subject to Open Data Triage. SSEN implements that obligation visibly — it became the first DNO to publish full smart meter half-hourly consumption data, aggregated to no fewer than five properties per LV feeder, and attaches published Open Data Triage records to its datasets.
image: https://www.ssen.co.uk/apple-touch-icon.png
layout: provider
modified: '2026-07-27'
name: Scottish and Southern Electricity Networks
nav: Providers
network: true
overview: 'Scottish and Southern Electricity Networks publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Grid.


  Scottish and Southern Electricity Networks'' developer surface includes authentication, getting-started guide, support, engineering blog, signup flow, documentation, developer portal, and 29 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Ssen Rate Limits
  slug: ssen-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 57.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 52.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ssen/refs/heads/main/screenshots/ssen-2026-08-17T082055.png
security:
- kind: authentication
  name: Ssen Authentication
  slug: ssen-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ssen Domain Security
  slug: ssen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ssen Vulnerability Disclosure
  slug: ssen-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ssen
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network Operator
- Transmission
- Smart Metering
- Open Data
- Flexibility
- Renewables
- DER
website: https://www.ssen.co.uk/
---
