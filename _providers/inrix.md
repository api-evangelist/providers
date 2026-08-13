---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-12'
api_count: 18
apis:
- description: Authentication and account service for the entire INRIX platform. Exchanges an appId plus a SHA-1 hashToken (or OAuth2 client credentials) for a bearer access token, and manages applications, applicat
  name: INRIX User Accounts System (UAS) API
  slug: inrix-user-accounts-system-uas-api
- description: 'On-street and off-street parking data: parking lots and city blocks, rates and hours, real-time and historical occupancy and probability, open spots from the Utilization Sensing Service, destinations,'
  name: INRIX Parking API (INRIX Parking Services 3.0 / ParkMe)
  slug: inrix-parking-api-inrix-parking-services-30-parkme
- description: 'Traffic-signal and intersection analytics served from the INRIX IQ backend: intersection metrics, intersection metadata, metrics availability, and namespace management for customer-scoped signal datas'
  name: INRIX Signals Analytics API
  slug: inrix-signals-analytics-api
- description: Real-time, historical and predicted speed, travel time and reference speed for INRIX XD and TMC road segments, queried by bounding box, radius, point, segment set or corridor.
  name: INRIX Segment Speed API
  slug: inrix-segment-speed-api
- description: Roadway incident, construction, flow, event and hazard alerts within a bounding box, radius or along a route, with TMC and OpenLR location referencing and TPEG-style event codes.
  name: INRIX Safety Alerts (Incidents) API
  slug: inrix-safety-alerts-incidents-api
- description: Pre-rendered raster traffic tiles for map overlays, addressed by quadkey and rendered from live INRIX speed data.
  name: INRIX Traffic Tiles API
  slug: inrix-traffic-tiles-api
- description: Fuel station locations, brands, amenities and current fuel prices by grade, searchable by bounding box, radius or station identifier.
  name: INRIX Fuel Stations API
  slug: inrix-fuel-stations-api
- description: Detects and reports sudden, unexpected slowdowns on the road network so vehicles and drivers can be warned ahead of a hazard.
  name: INRIX Dangerous Slowdowns API
  slug: inrix-dangerous-slowdowns-api
- description: Ranked collision and safety risk scoring for road segments, used to identify the most dangerous roads and intersections in a geography.
  name: INRIX Dangerous Roads API
  slug: inrix-dangerous-roads-api
- description: Aggregated, anonymized trip origin-destination counts into and out of a defined trade area or location polygon, for retail site selection and location analytics.
  name: INRIX Trade Area Trips API
  slug: inrix-trade-area-trips-api
- description: Trip volume and travel-behaviour trend reports over time for a geography, including seasonal adjustment and data-quality metadata.
  name: INRIX Trip Trends Reports API
  slug: inrix-trip-trends-reports-api
- description: 'Asynchronous report and bulk speed-data downloader for INRIX Roadway Analytics: submit a report request, poll its status and retrieve the generated dataset.'
  name: INRIX Roadway Analytics Data Downloader API
  slug: inrix-roadway-analytics-data-downloader-api
- description: Queries and downloads static INRIX data deliverables organized by product, dataset and file - beginning with map releases (XD added/removed/replaced, TMC changes, OpenLR dictionaries, shapefiles and G
  name: INRIX Data Download Service
  slug: inrix-data-download-service
- description: 'Inbound data streams for partners contributing probe data to INRIX: batched JSON POSTs of GPS points, extended floating car data (XFCD) readings, and parking events, consumed asynchronously with sub-s'
  name: INRIX Data Upload Service (GPS, XFCD and Parking Event Streams)
  slug: inrix-data-upload-service-gps-xfcd-and-parking-event-streams
- description: Reports the current INRIX map and XD network version in use, so consumers can align segment identifiers with the correct map release.
  name: INRIX Gateway Map Version API
  slug: inrix-gateway-map-version-api
- description: The long-standing INRIX Connected Services gateway (Inrix.ashx), which serves routing, drive time polygons, traffic cameras, road speed at points, segment sets and speed buckets through Action-style r
  name: INRIX Connected Services Gateway API
  slug: inrix-connected-services-gateway-api
- description: Delivers INRIX traffic, incident, parking, weather and fuel content in TISA TPEG format over HTTP POST sessions, with incremental deltas, configurable content radii, compression and encryption for emb
  name: INRIX TPEG Connect
  slug: inrix-tpeg-connect
- description: Anonymized visit counts and dwell analytics for points of interest and custom polygons, derived from INRIX device and vehicle movement data.
  name: INRIX Visits Analytics API
  slug: inrix-visits-analytics-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inrix-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inrix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inrix-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://inrix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://inrix.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inrix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inrix.com/traffic/general_info/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inrix.com/authentication/getting_authorized/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.inrix.com/authentication/getting_authorized/
- group: start
  title: ''
  type: Console
  url: https://iq.inrix.com/
- group: start
  title: ''
  type: SignUp
  url: https://iq.inrix.com/
- group: start
  title: ''
  type: Login
  url: https://iq.inrix.com/?l=1
- group: operate
  title: ''
  type: Support
  url: mailto:support@inrix.com
- group: company
  title: ''
  type: Blog
  url: https://inrix.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/INRIX
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inrix.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.inrix.com/parking/change_log/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inrix.com/site-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inrix.com/site-privacy-policy/
- group: other
  title: ''
  type: Glossary
  url: https://docs.inrix.com/reference/glossary/
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.inrix.com/reference/errorstatusids/
- group: build
  title: ''
  type: SDK
  url: https://docs.inrix.com/sdk/general/
- group: commercial
  title: ''
  type: Pricing
  url: https://inrix.com/contact/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inrix-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inrix-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inrix-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inrix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/inrix-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/inrix-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/inrix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/inrix-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inrix-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/inrix-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inrix-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inrix-llms.txt
created: '2026-08-01'
description: 'INRIX is a Kirkland, Washington-based transportation analytics company that turns anonymized GPS probe data from connected vehicles, mobile devices and fleets into real-time and historical road intelligence for automakers, cities, departments of transportation, retailers and app developers. Its developer surface is organized around the INRIX IQ platform and documented at docs.inrix.com, spanning Traffic APIs (segment speed, safety alerts/incidents, traffic tiles, routing, drive time polygons, traffic cameras, dangerous slowdowns, fuel stations and TPEG Connect), Parking APIs (INRIX Parking Services 3.0, formerly ParkMe: lots, blocks, occupancy and probability, destinations and reservations), Analytics APIs (trade area trips, trip trends, visits, dangerous roads and Roadway Analytics), Signals intersection analytics, a Data Download Service for map and XD network releases, and data-upload streams for GPS, XFCD and parking events. All access is brokered through the INRIX User
  Accounts System (UAS), which exchanges an appId and a SHA-1 hashToken for a bearer access token used across every product API.'
image: https://docs.inrix.com/images/inrix.png
layout: provider
mcp_servers:
- description: ''
  name: inrix-mcp.yml
  slug: inrix-mcpyml
modified: '2026-08-01'
name: INRIX
nav: Providers
network: true
overview: 'INRIX publishes 3 APIs on the [APIs.io](https://apis.io/) network: User Accounts System (UAS) API, Parking API (INRIX Parking Services 3.0 / ParkMe), and Signals Analytics API. Tagged areas include Transportation, Traffic, Mobility, Parking, and Geospatial.


  INRIX''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, signup flow, support, and 29 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 40.0
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 49.8
  provenance:
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inrix/refs/heads/main/screenshots/inrix-2026-08-07T170714.png
security:
- kind: authentication
  name: Inrix Authentication
  slug: inrix-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Inrix Domain Security
  slug: inrix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inrix
tags:
- Transportation
- Traffic
- Mobility
- Parking
- Geospatial
- Location Data
- Analytics
- Automotive
- Smart Cities
- Routing
- Connected Vehicles
- Road Network
- Data
- Fleet
- Intelligent Transportation Systems
website: https://inrix.com/
---
