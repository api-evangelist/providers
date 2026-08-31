---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Us Dot Agentic Access
  operation_count: 53
  slug: us-dot-agentic-access
  summary_line: 53 operations · 15 acting
api_count: 5
apis:
- description: The Federal Aviation Administration's open data catalog, running CKAN 2.11.4 and exposing the full CKAN Action API v3 anonymously at /api/3/action/. package_list, package_search, package_show, organiz
  name: FAA Data Catalog (CKAN Action API v3)
  slug: faa-data-catalog-ckan-api
- description: 'The departmental open data platform, served from both data.transportation.gov and datahub.transportation.gov on Socrata SODA 2.1. For travel and aviation this is where the DOT Office of the Assistant '
  name: DOT Data Hub Open Data API
  slug: dot-data-hub-soda-api
- description: The Bureau of Transportation Statistics open data platform on Socrata SODA 2.1, and the authoritative record of US commercial aviation activity. Aviation holdings verified live include T-100 segment s
  name: Bureau of Transportation Statistics Open Data API
  slug: bts-open-data-soda-api
- description: The National Highway Traffic Safety Administration's Vehicle Product Information Catalog and VIN decoder, and the most widely consumed API in the department. Decodes any US-market VIN into make, model
  name: NHTSA vPIC (Vehicle Product Information Catalog) API
  slug: nhtsa-vpic-api
- description: 'The NHTSA public safety API that powers the dynamic search applications on nhtsa.gov. Three families: /recalls for safety recalls by vehicle or campaign number, /complaints for consumer complaints fil'
  name: NHTSA Safety API (recalls, complaints, safety ratings)
  slug: nhtsa-safety-api
- description: The Federal Railroad Administration's rail safety web services, and the only SOAP surface in the department. Two WSDL 1.1 contracts were retrieved live and harvested verbatim on 2026-07-28. The Master
  name: FRA Safety Data Web Services
  slug: fra-safety-data-api
- description: The Federal Motor Carrier Safety Administration's carrier data API — real-time queries on motor carrier registration, authority and safety data, including all of the passenger carrier data that used t
  name: FMCSA QCMobile API
  slug: fmcsa-qcmobile-api
- description: The AirCarrierApi API from U.S. Department of Transportation — 4 operation(s) for aircarrierapi.
  name: U.S. Department of Transportation Air Carrier API
  slug: us-dot-aircarrierapi-api
- description: The Axhsubmitdiscrepancies API from U.S. Department of Transportation — 1 operation(s) for axhsubmitdiscrepancies.
  name: U.S. Department of Transportation Axhsubmitdiscrepancies API
  slug: us-dot-axhsubmitdiscrepancies-api
- description: The Coded Instrument Flight Procedures (CIFP) API from U.S. Department of Transportation — 2 operation(s) for coded instrument flight procedures (cifp).
  name: U.S. Department of Transportation Coded Instrument Flight Procedures (CIFP) API
  slug: us-dot-coded-instrument-flight-procedures-cifp-api
- description: The Daily Digital Obstacle File (DDOF) API from U.S. Department of Transportation — 2 operation(s) for daily digital obstacle file (ddof).
  name: U.S. Department of Transportation Daily Digital Obstacle File (DDOF) API
  slug: us-dot-daily-digital-obstacle-file-ddof-api
- description: The Digital Enroute Charts US (DDECUS) API from U.S. Department of Transportation — 2 operation(s) for digital enroute charts us (ddecus).
  name: U.S. Department of Transportation Digital Enroute Charts US (DDECUS) API
  slug: us-dot-digital-enroute-charts-us-ddecus-api
- description: The Digital Enroute Supplement (DERS) API from U.S. Department of Transportation — 2 operation(s) for digital enroute supplement (ders).
  name: U.S. Department of Transportation Digital Enroute Supplement (DERS) API
  slug: us-dot-digital-enroute-supplement-ders-api
- description: The FAA Airport Status Service API from U.S. Department of Transportation — 2 operation(s) for faa airport status service.
  name: U.S. Department of Transportation FAA Airport Status Service API
  slug: us-dot-faa-airport-status-service-api
- description: The Grand Canyon VFR Chart API from U.S. Department of Transportation — 2 operation(s) for grand canyon vfr chart.
  name: U.S. Department of Transportation Grand Canyon VFR Chart API
  slug: us-dot-grand-canyon-vfr-chart-api
- description: The Gulf of Mexico IFR Enroute Chart API from U.S. Department of Transportation — 2 operation(s) for gulf of mexico ifr enroute chart.
  name: U.S. Department of Transportation Gulf of Mexico IFR Enroute Chart API
  slug: us-dot-gulf-of-mexico-ifr-enroute-chart-api
- description: The IFR Enroute Charts API from U.S. Department of Transportation — 2 operation(s) for ifr enroute charts.
  name: U.S. Department of Transportation IFR Enroute Charts API
  slug: us-dot-ifr-enroute-charts-api
- description: The IFR Planning Charts API from U.S. Department of Transportation — 2 operation(s) for ifr planning charts.
  name: U.S. Department of Transportation IFR Planning Charts API
  slug: us-dot-ifr-planning-charts-api
- description: The log file API from U.S. Department of Transportation — 1 operation(s) for log file.
  name: U.S. Department of Transportation log file API
  slug: us-dot-log-file-api
- description: The NASR 28 Day Subscription API from U.S. Department of Transportation — 2 operation(s) for nasr 28 day subscription.
  name: U.S. Department of Transportation NASR 28 Day Subscription API
  slug: us-dot-nasr-28-day-subscription-api
- description: The Oceanic Route Charts API from U.S. Department of Transportation — 2 operation(s) for oceanic route charts.
  name: U.S. Department of Transportation Oceanic Route Charts API
  slug: us-dot-oceanic-route-charts-api
- description: The PDM API from U.S. Department of Transportation — 1 operation(s) for pdm.
  name: U.S. Department of Transportation PDM API
  slug: us-dot-pdm-api
- description: The Sectional Charts API from U.S. Department of Transportation — 2 operation(s) for sectional charts.
  name: U.S. Department of Transportation Sectional Charts API
  slug: us-dot-sectional-charts-api
- description: The SNMP API from U.S. Department of Transportation — 1 operation(s) for snmp.
  name: U.S. Department of Transportation SNMP API
  slug: us-dot-snmp-api
- description: The Supplement Chart API from U.S. Department of Transportation — 2 operation(s) for supplement chart .
  name: U.S. Department of Transportation Supplement Chart API
  slug: us-dot-supplement-chart-api
- description: The Terminal Area Charts API from U.S. Department of Transportation — 2 operation(s) for terminal area charts.
  name: U.S. Department of Transportation Terminal Area Charts API
  slug: us-dot-terminal-area-charts-api
- description: The TIM API from U.S. Department of Transportation — 2 operation(s) for tim.
  name: U.S. Department of Transportation TIM API
  slug: us-dot-tim-api
- description: The US Terminal Procedures Publication (TPP) API from U.S. Department of Transportation — 2 operation(s) for us terminal procedures publication (tpp).
  name: U.S. Department of Transportation US Terminal Procedures Publication (TPP) API
  slug: us-dot-us-terminal-procedures-publication-tpp-api
- description: The US VFR Wall Planning Chart API from U.S. Department of Transportation — 2 operation(s) for us vfr wall planning chart.
  name: U.S. Department of Transportation US VFR Wall Planning Chart API
  slug: us-dot-us-vfr-wall-planning-chart-api
- description: The Version API from U.S. Department of Transportation — 1 operation(s) for version.
  name: U.S. Department of Transportation Version API
  slug: us-dot-version-api
- description: The VFR Helicopter Route Chart API from U.S. Department of Transportation — 4 operation(s) for vfr helicopter route chart.
  name: U.S. Department of Transportation VFR Helicopter Route Chart API
  slug: us-dot-vfr-helicopter-route-chart-api
artifact_total: 51
asyncapis:
- description: ''
  name: Us Dot Event Surfaces
  slug: us-dot-event-surfaces
- description: DERIVED, NOT PUBLISHED BY USDOT. The U.S. Department of Transportation publishes no AsyncAPI document. This document is a faithful derivation of the Kafka topic catalog the USDOT ITS Joint Program Off
  name: USDOT ITS JPO Operational Data Environment (ODE) — Kafka event surface
  slug: us-dot-its-jpo-ode-asyncapi
collections:
- collection_type: open
  name: Aeronautic Product Release API
  slug: open-us-dot-faa-aeronautic-product-release-api
- collection_type: open
  name: PRD Air Carrier API
  slug: open-us-dot-faa-air-carrier-prd-api
- collection_type: open
  name: Airport Status Web Service
  slug: open-us-dot-faa-airport-status-web-service
- collection_type: open
  name: sas-api
  slug: open-us-dot-faa-safety-assurance-system-api
- collection_type: open
  name: ODE REST API
  slug: open-us-dot-its-jpo-ode-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/us-dot-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/usdot-jpo-ode/jpo-ode/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/usdot-jpo-ode/jpo-ode/releases
- group: other
  title: ''
  type: Overlay
  url: overlays/us-dot-faa-aeronautic-product-release-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/us-dot-download-aeronautical-products.md
- group: other
  title: ''
  type: Overlay
  url: overlays/us-dot-faa-air-carrier-prd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/us-dot-faa-safety-assurance-system-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/us-dot-submit-sas-discrepancy.md
- group: other
  title: ''
  type: Overlay
  url: overlays/us-dot-its-jpo-ode-rest-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/us-dot-deposit-tim-to-roadside-unit.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/us-dot-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.transportation.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.transportation.gov/developer
- group: start
  title: ''
  type: Portal
  url: https://api.faa.gov/s/
- group: start
  title: ''
  type: Portal
  url: https://data.transportation.gov/
- group: start
  title: ''
  type: Portal
  url: https://data.bts.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://api.faa.gov/s/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.socrata.com/docs/queries/
- group: start
  title: ''
  type: GettingStarted
  url: https://mobile.fmcsa.dot.gov/QCDevsite/docs/getStarted
- group: operate
  title: ''
  type: Support
  url: https://api.faa.gov/s/help
- group: company
  title: ''
  type: Blog
  url: https://www.transportation.gov/blog
- group: start
  title: ''
  type: SignUp
  url: https://mobile.fmcsa.dot.gov/QCDevsite/logingovInfo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transportation.gov/web-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transportation.gov/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.transportation.gov/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/us-dot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-dot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-dot-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/us-dot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/us-dot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/us-dot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socrata.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/us-dot-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/us-dot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/us-dot-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/us-dot-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/us-dot-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://data.transportation.gov/data.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/us-dot-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-dot-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/us-dot-tool-crosswalk.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/us-dot-its-jpo-ode-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/us-dot-wzdx-4.2-workzonefeed.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/us-dot-wzdx-4.2-devicefeed.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/us-dot-wzdx-4.2-roadeventfeature.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/us-dot-wzdx-4.2-feedinfo.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/us-dot-wzdx-4.2-boundingbox.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/us-dot-wzdx-4.2-direction.json
- group: other
  title: ''
  type: BulkData
  url: https://www.transtats.bts.gov/
- group: other
  title: ''
  type: BulkData
  url: https://registry.faa.gov/database/ReleasableAircraft.zip
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usdot-jpo-ode
- group: other
  title: ''
  type: X
  url: https://x.com/USDOT
- group: commercial
  title: ''
  type: License
  url: https://www.usa.gov/government-works
- group: other
  title: ''
  type: Regulation
  url: https://www.ecfr.gov/current/title-14/chapter-II/subchapter-A/part-256
created: '2026-07-28'
description: 'The U.S. Department of Transportation (DOT) is the federal transportation regulator for the United States, the deepest travel market in the world. In aviation DOT is not a participant in the distribution chain — it is the counterweight to it: through the Office of the Secretary it writes and enforces 14 CFR Part 256 on electronic airline information systems (explicitly naming global distribution systems, corporate booking tools and internet flight search tools), Part 257 on code-share disclosure, Part 250 on oversales, Part 259 on enhanced passenger protections, Part 260 on fare and ancillary fee refunds, and 399.84 on full-fare advertising. Its Bureau of Transportation Statistics is the sole authoritative source for US airline economics — T-100 segment traffic, Form 41 financials, the Consumer Airfare Report city-pair fare tables, denied boardings and mishandled baggage — published as free Socrata SODA APIs. Its Federal Aviation Administration operates a Gravitee API portal
  at api.faa.gov whose public catalog is enumerable without login and serves genuinely open, unauthenticated OpenAPI 3.0.1 services for national airspace delay status and aeronautical chart product releases, alongside gated APIs for pilot records and safety reporting. Beyond aviation the operating administrations each run their own surface: NHTSA publishes anonymous vehicle, recall, complaint and safety-rating APIs; FRA publishes SOAP/WSDL rail safety services; FMCSA issues the department''s only self-serve API key behind a Login.gov account. API posture, honestly: transportation.gov itself is bot-blocked (HTTP 403 to any non-browser client) and publishes no departmental OpenAPI, there is no OAuth, no idempotency key, no RFC 9457 errors, no Sunset headers and no security.txt anywhere — but the data surfaces underneath are open, unmetered, public domain and fully bulk-exportable. This is a provider with an excellent exit path and no commercial lock-in of any kind.'
examples:
- key_count: 6
  name: Us Dot Faa Sas Submit Discrepancies Request
  slug: us-dot-faa-sas-submit-discrepancies-request
- key_count: 4
  name: Us Dot Faa Sas Submit Discrepancies Response
  slug: us-dot-faa-sas-submit-discrepancies-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dot.png
json_schemas:
- name: GeoJSON Bounding Box
  property_count: 0
  slug: us-dot-wzdx-4.2-boundingbox
- name: WZDx v4.2 DeviceFeed
  property_count: 4
  slug: us-dot-wzdx-4.2-devicefeed
- name: Direction Enumerated Type
  property_count: 0
  slug: us-dot-wzdx-4.2-direction
- name: WZDx Feed Information
  property_count: 8
  slug: us-dot-wzdx-4.2-feedinfo
- name: Road Event Feature (GeoJSON Feature)
  property_count: 5
  slug: us-dot-wzdx-4.2-roadeventfeature
- name: WZDx v4.2 Work Zone Feed
  property_count: 5
  slug: us-dot-wzdx-4.2-workzonefeed
layout: provider
mcp_servers:
- description: ''
  name: U.S. Department of Transportation MCP Server
  slug: us-department-of-transportation-mcp-server
modified: '2026-07-28'
name: U.S. Department of Transportation
nav: Providers
network: true
overview: 'U.S. Department of Transportation publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Air Carrier API, Axhsubmitdiscrepancies API, Coded Instrument Flight Procedures (CIFP) API, and 21 more. Tagged areas include Travel, United States, Aviation, Airlines, and Airports.


  The U.S. Department of Transportation catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  U.S. Department of Transportation''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 49 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 26
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 25.0
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-dot/refs/heads/main/screenshots/us-dot-2026-08-17T082655.png
security:
- kind: authentication
  name: Us Dot Authentication
  slug: us-dot-authentication
  summary_line: none/apiKey · 8 schemes
- kind: domain-security
  name: Us Dot Domain Security
  slug: us-dot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Us Dot Vulnerability Disclosure
  slug: us-dot-vulnerability-disclosure
  summary_line: Bugcrowd
slug: us-dot
tags:
- Travel
- United States
- Aviation
- Airlines
- Airports
- Government
- Regulator
- Distribution
- Aviation Consumer Protection
- Open Data
- Transportation
- Safety
- Statistics
- Automotive
- Rail
website: https://www.transportation.gov/
---
