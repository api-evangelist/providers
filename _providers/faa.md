---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Faa Agentic Access
  operation_count: 45
  slug: faa-agentic-access
  summary_line: 45 operations · 9 acting
api_count: 4
apis:
- description: Notices to Air Missions retrieval API. Probe-confirmed live but gated — an unauthenticated GET returned HTTP 401 with the body {"message":"Unauthorized", "http_status_code":401} on 2026-07-28, while t
  name: FAA NOTAM API
  slug: faa-notam-api
- description: The distribution interface of the FAA's new NOTAM Management Service, the vendor-provided replacement for the legacy United States NOTAM System (USNS) and Federal NOTAM System (FNS). Discovered and ve
  name: FAA NOTAM Management Service (NMS) API
  slug: faa-nms-api
- description: Unauthenticated JSON feed of North Atlantic Track NOTAMs published by the FAA NOTAM Management Service. Each record carries accountability and origin ids, the formatted NOTAM number, ICAO id, location
  name: FAA NMS North Atlantic Track NOTAM Feed
  slug: faa-nms-nat-track-feed
- description: Unauthenticated JSON feed backing the NOTAM Management Service system metrics dashboard — cumulative NOTAMs processed, NMS API onboarded users, NMS API volume of data pulled per day, number of API cal
  name: FAA NMS System Metrics Feed
  slug: faa-nms-metrics-feed
- description: Retrieves designee information from the FAA Data Management System using either a Designee Number or an ODA Key ID. Listed in the api.faa.gov portal under the "Public" category, but the only entrypoin
  name: FAA DMS Lookup API
  slug: faa-dms-lookup-api
- description: The FAA's public data clearinghouse at catalog.data.faa.gov runs CKAN 2.11.4 and exposes the standard CKAN Action API. Verified 2026-07-28 — status_show returned site_title "Federal Aviation Administr
  name: FAA Data Catalog API (CKAN)
  slug: faa-data-catalog-ckan-api
- description: ArcGIS Open Data hub published by "Federal Aviation Administration - AIS" carrying 73 datasets — class airspace, frequencies, runways, navaids, obstacles, VFR and IFR chart tile services. Every featur
  name: FAA Aeronautical Information Services Open Data
  slug: faa-ais-open-data
- description: ArcGIS Open Data hub for unmanned aircraft data — UAS Facility Maps (the LAANC altitude grid), national security UAS flight restrictions, part-time restrictions, FAA-Recognized Identification Areas an
  name: FAA UAS Data Delivery System Open Data
  slug: faa-uas-data-delivery-system
- description: Unauthenticated XML feed of national airspace system status — ground stop programs, ground delay programs, airport closures and arrival/departure delays — as consumed by nasstatus.faa.gov. Verified li
  name: FAA NAS Status Airport Status Information Feed
  slug: faa-nas-status-feed
- description: Unauthenticated JSON list of active Temporary Flight Restrictions, each carrying a NOTAM id, TFR type, ARTCC facility identifier, state and effective description. Verified live 2026-07-28 (HTTP 200, a
  name: FAA Temporary Flight Restriction (TFR) List API
  slug: faa-tfr-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The AirCarrierApi API from Federal Aviation Administration — 4 operation(s) for aircarrierapi.
  name: Federal Aviation Administration Air Carrier API
  slug: faa-aircarrierapi-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Axhsubmitdiscrepancies API from Federal Aviation Administration — 1 operation(s) for axhsubmitdiscrepancies.
  name: Federal Aviation Administration Axhsubmitdiscrepancies API
  slug: faa-axhsubmitdiscrepancies-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Coded Instrument Flight Procedures (CIFP) API from Federal Aviation Administration — 2 operation(s) for coded instrument flight procedures (cifp).
  name: Federal Aviation Administration Coded Instrument Flight Procedures (CIFP) API
  slug: faa-coded-instrument-flight-procedures-cifp-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Daily Digital Obstacle File (DDOF) API from Federal Aviation Administration — 2 operation(s) for daily digital obstacle file (ddof).
  name: Federal Aviation Administration Daily Digital Obstacle File (DDOF) API
  slug: faa-daily-digital-obstacle-file-ddof-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Digital Enroute Charts US (DDECUS) API from Federal Aviation Administration — 2 operation(s) for digital enroute charts us (ddecus).
  name: Federal Aviation Administration Digital Enroute Charts US (DDECUS) API
  slug: faa-digital-enroute-charts-us-ddecus-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Digital Enroute Supplement (DERS) API from Federal Aviation Administration — 2 operation(s) for digital enroute supplement (ders).
  name: Federal Aviation Administration Digital Enroute Supplement (DERS) API
  slug: faa-digital-enroute-supplement-ders-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The FAA Airport Status Service API from Federal Aviation Administration — 2 operation(s) for faa airport status service.
  name: Federal Aviation Administration FAA Airport Status Service API
  slug: faa-faa-airport-status-service-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Grand Canyon VFR Chart API from Federal Aviation Administration — 2 operation(s) for grand canyon vfr chart.
  name: Federal Aviation Administration Grand Canyon VFR Chart API
  slug: faa-grand-canyon-vfr-chart-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Gulf of Mexico IFR Enroute Chart API from Federal Aviation Administration — 2 operation(s) for gulf of mexico ifr enroute chart.
  name: Federal Aviation Administration Gulf of Mexico IFR Enroute Chart API
  slug: faa-gulf-of-mexico-ifr-enroute-chart-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The IFR Enroute Charts API from Federal Aviation Administration — 2 operation(s) for ifr enroute charts.
  name: Federal Aviation Administration IFR Enroute Charts API
  slug: faa-ifr-enroute-charts-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The IFR Planning Charts API from Federal Aviation Administration — 2 operation(s) for ifr planning charts.
  name: Federal Aviation Administration IFR Planning Charts API
  slug: faa-ifr-planning-charts-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The NASR 28 Day Subscription API from Federal Aviation Administration — 2 operation(s) for nasr 28 day subscription.
  name: Federal Aviation Administration NASR 28 Day Subscription API
  slug: faa-nasr-28-day-subscription-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Oceanic Route Charts API from Federal Aviation Administration — 2 operation(s) for oceanic route charts.
  name: Federal Aviation Administration Oceanic Route Charts API
  slug: faa-oceanic-route-charts-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Sectional Charts API from Federal Aviation Administration — 2 operation(s) for sectional charts.
  name: Federal Aviation Administration Sectional Charts API
  slug: faa-sectional-charts-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Supplement Chart API from Federal Aviation Administration — 2 operation(s) for supplement chart .
  name: Federal Aviation Administration Supplement Chart API
  slug: faa-supplement-chart-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The Terminal Area Charts API from Federal Aviation Administration — 2 operation(s) for terminal area charts.
  name: Federal Aviation Administration Terminal Area Charts API
  slug: faa-terminal-area-charts-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The US Terminal Procedures Publication (TPP) API from Federal Aviation Administration — 2 operation(s) for us terminal procedures publication (tpp).
  name: Federal Aviation Administration US Terminal Procedures Publication (TPP) API
  slug: faa-us-terminal-procedures-publication-tpp-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The US VFR Wall Planning Chart API from Federal Aviation Administration — 2 operation(s) for us vfr wall planning chart.
  name: Federal Aviation Administration US VFR Wall Planning Chart API
  slug: faa-us-vfr-wall-planning-chart-api
- baseURL: https://external-api.faa.gov/apra
  baseurl_source: declared
  description: The VFR Helicopter Route Chart API from Federal Aviation Administration — 4 operation(s) for vfr helicopter route chart.
  name: Federal Aviation Administration VFR Helicopter Route Chart API
  slug: faa-vfr-helicopter-route-chart-api
artifact_total: 40
asyncapis:
- description: ''
  name: Faa Swim Event Surface
  slug: faa-swim-event-surface
collections:
- collection_type: open
  name: Aeronautic Product Release API
  slug: open-faa-aeronautic-product-release-api
- collection_type: open
  name: PRD Air Carrier API
  slug: open-faa-air-carrier-prd-api
- collection_type: open
  name: Airport Status Web Service
  slug: open-faa-airport-status-web-service
- collection_type: open
  name: sas-api
  slug: open-faa-safety-assurance-system-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/faa-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/faa-aeronautic-product-release-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/faa-track-nasr-28-day-cycle.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/faa-fetch-terminal-procedures-and-charts.md
- group: other
  title: ''
  type: Overlay
  url: overlays/faa-air-carrier-prd-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/faa-safety-assurance-system-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/faa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/faa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/faa-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/faa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.faa.gov/web_policies/vulnerability_disclosure_policy
- group: design
  title: ''
  type: Conventions
  url: conventions/faa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/faa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/faa-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://nms.aim.faa.gov/#system-metrics
- group: operate
  title: ''
  type: Deprecation
  url: https://nms.aim.faa.gov/
- group: design
  title: ''
  type: Conformance
  url: conformance/faa-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/faa-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/faa-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/faa-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/faa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/faa-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/faa-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://apim-api.apic4e.faa.gov/portal/environments/DEFAULT/apis
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/faa-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/faa-llms.txt
- group: other
  title: ''
  type: Events
  url: asyncapi/faa-swim-event-surface.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.faa.gov/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.faa.gov/data
- group: start
  title: ''
  type: SignUp
  url: https://portal.apic4e.faa.gov/
- group: operate
  title: ''
  type: Support
  url: https://www.faa.gov/contact
- group: company
  title: ''
  type: Blog
  url: https://www.faa.gov/blog/cleared_for_takeoff
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/faa-swim
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.faa.gov/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.faa.gov/web_policies
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/publicdomain/zero/1.0/legalcode
- group: company
  title: ''
  type: Website
  url: https://www.faa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://api.faa.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.faa.gov/
- group: start
  title: ''
  type: DataPortal
  url: https://www.faa.gov/data
- group: other
  title: ''
  type: DataCatalog
  url: https://catalog.data.faa.gov/dataset
- group: other
  title: ''
  type: OpenData
  url: https://ais-faa.opendata.arcgis.com/
- group: other
  title: ''
  type: OpenData
  url: https://udds-faa.opendata.arcgis.com/
- group: other
  title: ''
  type: BulkDownload
  url: https://registry.faa.gov/database/ReleasableAircraft.zip
- group: company
  title: ''
  type: Website
  url: https://registry.faa.gov/aircraftinquiry/
- group: company
  title: ''
  type: Website
  url: https://www.faa.gov/air_traffic/technology/swim
- group: company
  title: ''
  type: Website
  url: https://portal.swim.faa.gov/
- group: company
  title: ''
  type: Website
  url: https://drs.faa.gov/browse
- group: company
  title: ''
  type: Website
  url: https://adip.faa.gov/agis/public/
- group: company
  title: ''
  type: Website
  url: https://www.faa.gov/uas/programs_partnerships/data_exchange
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/faa
created: '2026-07-28'
description: The Federal Aviation Administration (FAA) is the United States civil aviation authority, an operating administration of the U.S. Department of Transportation. It regulates and certificates aircraft, airmen, airports and air carriers, operates the National Airspace System and its air traffic control, and issues the aeronautical information the entire U.S. travel and aviation chain runs on — NOTAMs, TFRs, charts, the 28-day NASR subscription, aircraft registration and airport data. It sits upstream of commercial travel distribution rather than inside it — the FAA sells no inventory and is not a GDS, NDC or channel participant, but every airline, GDS, OTA, flight-planning app and drone service supplier in the United States consumes FAA data as a source of truth. Its API posture is genuinely mixed and honest reporting requires saying so. The Airport Status Web Service and the Aeronautic Product Release API are published under a Creative Commons Zero licence, answer unauthenticated
  over HTTPS, and ship real OpenAPI 3.0.1 documents through a public Gravitee developer portal at api.faa.gov. Alongside them the FAA runs a CKAN 2.11.4 catalog and two ArcGIS Open Data hubs with DCAT-US 1.1 feeds and bulk CSV/GeoJSON/KML export. But the NOTAM API, the Air Carrier Pilot Records Database API and SWIM are gated — client_id/client_secret headers, operator eligibility restricted by regulation, or an executed SWIM agreement — and LAANC drone authorization is reachable only through FAA-approved UAS Service Suppliers, never directly.
image: https://www.faa.gov/themes/custom/faa/favicon.png
layout: provider
modified: '2026-07-28'
name: Federal Aviation Administration
nav: Providers
network: true
overview: 'Federal Aviation Administration publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Air Carrier API, Axhsubmitdiscrepancies API, Coded Instrument Flight Procedures (CIFP) API, and 16 more. Tagged areas include Travel, United States, Aviation, Airports, and Government.


  The Federal Aviation Administration catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Federal Aviation Administration''s developer surface includes authentication, API reference, getting-started guide, signup flow, support, engineering blog, documentation, and 45 more developer resources.'
plans:
- name: Faa Plans
  plan_count: 5
  slug: faa-plans
random_paper: 2
rate_limits:
- limit_count: 1
  name: Faa Rate Limits
  slug: faa-rate-limits
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 52.8
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 94.7
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/faa/refs/heads/main/screenshots/faa-2026-08-07T165207.png
security:
- kind: authentication
  name: Faa Authentication
  slug: faa-authentication
  summary_line: none/apiKey · 5 schemes
- kind: domain-security
  name: Faa Domain Security
  slug: faa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Faa Vulnerability Disclosure
  slug: faa-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: faa
tags:
- Travel
- United States
- Aviation
- Airports
- Government
- Regulator
- Open Data
- Airspace
- Drones
- Aeronautical Information
website: https://www.faa.gov/
---
