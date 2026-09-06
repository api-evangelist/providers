---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.2
  scored_at: '2026-09-05'
api_count: 3
apis:
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
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The accounts API from INRIX — 1 operation(s) for accounts.
  name: INRIX Accounts API
  slug: inrix-accounts-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The api API from INRIX — 3 operation(s) for api.
  name: INRIX API
  slug: inrix-api-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The Application API from INRIX — 9 operation(s) for application.
  name: INRIX Application API
  slug: inrix-application-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The ApplicationManagement API from INRIX — 9 operation(s) for applicationmanagement.
  name: INRIX Application Management API
  slug: inrix-applicationmanagement-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The Auth API from INRIX — 6 operation(s) for auth.
  name: INRIX Auth API
  slug: inrix-auth-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The Developer API from INRIX — 2 operation(s) for developer.
  name: INRIX Developer API
  slug: inrix-developer-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The Device API from INRIX — 3 operation(s) for device.
  name: INRIX Device API
  slug: inrix-device-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The EmailTemplate API from INRIX — 2 operation(s) for emailtemplate.
  name: INRIX Email Template API
  slug: inrix-emailtemplate-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The Metadata API from INRIX — 1 operation(s) for metadata.
  name: INRIX Metadata API
  slug: inrix-metadata-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The Metrics API from INRIX — 2 operation(s) for metrics.
  name: INRIX Metrics API
  slug: inrix-metrics-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: APIs for managing intersection namespace subscriptions
  name: INRIX Namespace Management API
  slug: inrix-namespace-management-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The User API from INRIX — 18 operation(s) for user.
  name: INRIX User API
  slug: inrix-user-api
- baseURL: https://uas-api.inrix.com
  baseurl_source: declared
  description: The UserGroup API from INRIX — 8 operation(s) for usergroup.
  name: INRIX User Group API
  slug: inrix-usergroup-api
artifact_total: 33
collections:
- collection_type: open
  name: INRIX Parkme API
  slug: open-inrix-parkme-openapi-original
- collection_type: open
  name: INRIX Analytics Webservice Template API
  slug: open-inrix-signals-analytics-openapi-original
- collection_type: open
  name: Inrix.UserAccounts.Web
  slug: open-inrix-user-accounts-openapi-original
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/inrix-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/inrix-user-accounts-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/inrix-authenticate-and-call.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/inrix-manage-applications-and-users.md
- group: other
  title: ''
  type: Overlay
  url: overlays/inrix-parkme-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/inrix-signals-analytics-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/inrix-query-signals-intersection-metrics.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-08-01'
name: INRIX
nav: Providers
network: true
overview: 'INRIX publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Application API, and 11 more. Tagged areas include Transportation, Traffic, Mobility, Parking, and Geospatial.


  INRIX''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, signup flow, support, and 36 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 40.9
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.9
  provenance:
    conformance: first-party
    contracts:
      callable: 76.9
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
