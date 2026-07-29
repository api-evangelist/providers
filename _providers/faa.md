---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Faa Agentic Access
  operation_count: 45
  slug: faa-agentic-access
  summary_line: 45 operations · 9 acting
api_count: 14
apis:
- description: Airport delay summaries and per-airport status for 40+ major US national airports, sourced from fly.faa.gov and served as JSON or XML. Keyed on IATA three-letter airport codes. Answers unauthenticated
  name: FAA Airport Status Web Service (ASWS)
  slug: faa-airport-status-web-service
- description: Chart publication metadata and download API from FAA Aeronautical Information Services. Thirty-four operations across VFR sectionals, terminal area charts, IFR enroute and oceanic charts, terminal pro
  name: FAA Aeronautic Product Release API (APRA)
  slug: faa-aeronautic-product-release-api
- description: Machine interface for submitting and searching pilot records in the FAA Pilot Records Database, the reporting obligation created for air carriers by 14 CFR Part 111. Requires client_id and client_secr
  name: FAA Air Carrier PRD API
  slug: faa-air-carrier-prd-api
- description: Single-operation API for submitting passenger discrepancy reports into the FAA Safety Assurance System. The harvested OpenAPI declares apiKey and appId header security schemes and carries a relative s
  name: FAA Safety Assurance System (SAS) API
  slug: faa-safety-assurance-system-api
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
artifact_total: 22
asyncapis:
- description: ''
  name: Faa Swim Event Surface
  slug: faa-swim-event-surface
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: Candidate MCP tool manifest derived from the FAA CC0 OpenAPIs — not published by the FAA
  slug: candidate-mcp-tool-manifest-derived-from-the-faa-cc0-openapis-not-published-by-the-faa
modified: '2026-07-28'
name: Federal Aviation Administration
nav: Providers
network: true
overview: 'Federal Aviation Administration publishes 4 APIs on the [APIs.io](https://apis.io/) network, including FAA Airport Status Web Service (ASWS), FAA Aeronautic Product Release API (APRA), FAA Air Carrier PRD API, and 1 more. Tagged areas include Travel, United States, Aviation, Airports, and Government.


  The Federal Aviation Administration catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Federal Aviation Administration''s developer surface includes authentication, API reference, getting-started guide, signup flow, support, engineering blog, documentation, and 39 more developer resources.'
plans:
- name: Faa Plans
  plan_count: 5
  slug: faa-plans
random_paper: 53
rate_limits:
- limit_count: 0
  name: Faa Rate Limits
  slug: faa-rate-limits
score:
  band: developing
  composite: 53.9
  facets:
    commercial_clarity: 65.8
    contract_quality: 51.3
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.6
  scored_at: '2026-07-28'
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
