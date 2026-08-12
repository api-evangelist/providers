---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fleetmon Agentic Access
  operation_count: 49
  slug: fleetmon-agentic-access
  summary_line: 49 operations · 6 acting
api_count: 37
apis:
- description: Delivers basic static data for a vessel.
  name: FleetMon Basic Vessel Data API
  slug: fleetmon-basic-vessel-data-api
- description: Returns current info for lat/lon (and timestamp).
  name: FleetMon Current API
  slug: fleetmon-current-api
- description: Returns the high level summary of a route to port, only including distance, costs, and the count of edges from the routing graph.
  name: FleetMon Distance To Port API
  slug: fleetmon-distance-to-port-api
- description: This API returns an estimated laytime for a vessel in all terminals of a port.
  name: FleetMon Estimated Laytime - Specific Vessel API
  slug: fleetmon-estimated-laytime-specific-vessel-api
- description: Lists vessels heading for a specific port, matched by AIS destination.
  name: FleetMon Expected Port Arrivals API
  slug: fleetmon-expected-port-arrivals-api
- description: Tracking of current positions for a modifiable list of vessels.
  name: FleetMon Fleet Tracker API
  slug: fleetmon-fleet-tracker-api
- description: Delivers AIS messages of type 5, 19 & 24 for a specified MMSI number.
  name: FleetMon Historical AIS Static Messages API
  slug: fleetmon-historical-ais-static-messages-api
- description: Returns historical AIS position reports with fixed period and rate, by MMSI.
  name: FleetMon Historical Track API API
  slug: fleetmon-historical-track-api-api
- description: Generate new Login Tokens with Token Keys
  name: FleetMon Login Token API
  slug: fleetmon-login-token-api
- description: Delivers information about the vessels current state and the next port it is heading for.
  name: FleetMon Logistics API
  slug: fleetmon-logistics-api
- description: Delivers your MyFleet or a single vessel of it.
  name: FleetMon My Fleet Positions API
  slug: fleetmon-my-fleet-positions-api
- description: Delivers information about the next port, provided by the vessel itself via AIS destination.
  name: FleetMon Next Port / ETA Calculation API
  slug: fleetmon-next-port-eta-calculation-api
- description: Delivers owner, manager, DWT, GT and a photo-URL for a vessel, if it's available.
  name: FleetMon Non AIS Vessel Particulars API
  slug: fleetmon-non-ais-vessel-particulars-api
- description: Delivers portcalls for a port.
  name: FleetMon Port Calls per Port API
  slug: fleetmon-port-calls-per-port-api
- description: Delivers portcalls for a vessel.
  name: FleetMon Port Calls per Vessel API
  slug: fleetmon-port-calls-per-vessel-api
- description: Allows lookup of ports by UN/LOCODE, name and/or country.
  name: FleetMon Port Search API
  slug: fleetmon-port-search-api
- description: delivers AIS informations for a predefined bounding box
  name: FleetMon Regional AIS API
  slug: fleetmon-regional-ais-api
- description: This API deliver the enter and left event of the RoRo-Ferry-Terminal Rostock. It is no API key necessary. The look back is 48h. It will be provides information about the Terminal Call itself, informat
  name: FleetMon RoRo Ferry Terminal Demo API
  slug: fleetmon-roro-ferry-terminal-demo-api
- description: Delivers change events for vessels.
  name: FleetMon Vessel Change Events API
  slug: fleetmon-vessel-change-events-api
- description: Live Dynamic AIS data from requested vessel
  name: FleetMon Vessel Dynamic AIS API
  slug: fleetmon-vessel-dynamic-ais-api
- description: Delivers ETA & Destination Change for vessels.
  name: FleetMon Vessel ETA & Destination Change Events API
  slug: fleetmon-vessel-eta-destination-change-events-api
- description: Returns the identifying attributes of the provided vessel.
  name: FleetMon Vessel Identity API
  slug: fleetmon-vessel-identity-api
- description: Delivers the URL to the main photo for a vessel. Look-up can be done by Vessel ID or IMO-number.
  name: FleetMon Vessel Photo API
  slug: fleetmon-vessel-photo-api
- description: Returns the latest received position.
  name: FleetMon Vessel Positions Only API
  slug: fleetmon-vessel-positions-only-api
- description: Delivers position and extended detailed information for a single vessel.
  name: FleetMon Vessel Positions with Extended Vessel Data API
  slug: fleetmon-vessel-positions-with-extended-vessel-data-api
- description: Returns the actual route from last port to latest position.
  name: FleetMon Vessel Route From Last Port API
  slug: fleetmon-vessel-route-from-last-port-api
- description: Returns the route to the next port of a vessel (using ObjectID).
  name: FleetMon Vessel Route To Next Port API
  slug: fleetmon-vessel-route-to-next-port-api
- description: This endpoint provides schedules for vessels, e.g. container schedules.
  name: FleetMon Vessel Schedule API
  slug: fleetmon-vessel-schedule-api
- description: Allows searching over the FleetMon vessel database by name, IMO-number, MMSI-number and/or callsign.
  name: FleetMon Vessel Search API
  slug: fleetmon-vessel-search-api
- description: Lists vessels detected in port for the specified LOCODE.
  name: FleetMon Vessels in Port API
  slug: fleetmon-vessels-in-port-api
- description: Vessels near requested position
  name: FleetMon Vessels Near Position API
  slug: fleetmon-vessels-near-position-api
- description: Vessels nearby requested vessel
  name: FleetMon Vessels Nearby API
  slug: fleetmon-vessels-nearby-api
- description: Delivers ETA & distance estimations for a route with multiple ports specified by LOCODE.
  name: FleetMon Voyage Planning API
  slug: fleetmon-voyage-planning-api
- description: Returns wave info for lat/lon (and timestamp).
  name: FleetMon Water API
  slug: fleetmon-water-api
- description: Returns weather info for lat/lon (and timestamp).
  name: FleetMon Weather API
  slug: fleetmon-weather-api
- description: Zone Call API
  name: FleetMon Zone Call API
  slug: fleetmon-zone-call-api
- description: Delivers an overview of your geo-zones.
  name: FleetMon Zone Information API
  slug: fleetmon-zone-information-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fleetmon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetmon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fleetmon-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kpler.com
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.fleetmon.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fleetmon-com
- group: start
  title: ''
  type: ArchivedDeveloperPortal
  url: http://web.archive.org/web/20250106234623/https://developer.fleetmon.com/
- group: docs
  title: ''
  type: ArchivedAPIReference
  url: http://web.archive.org/web/20250106234623/https://developer.fleetmon.com/reference/
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.kpler.com/blog/kpler-acquires-marinetraffic-and-fleetmon-for-maritime-sector-expansion
- group: docs
  title: ''
  type: MigrationGuide
  url: https://support.marinetraffic.com/en/articles/9552991-fleetmon-and-marinetraffic-merge-process-for-former-fleetmon-ais-partners-from-january-2024
- group: other
  title: ''
  type: SuccessorAnnouncement
  url: https://support.marinetraffic.com/en/articles/12495052-19-september-2025-announcing-the-launch-of-kpler-ais
- group: docs
  title: ''
  type: SuccessorAPIDocumentation
  url: https://servicedocs.marinetraffic.com/
- group: other
  title: ''
  type: SuccessorProduct
  url: https://www.kpler.com/product/maritime/data-services
created: '2026-07-11'
description: FleetMon was a Rostock, Germany based vessel tracking and maritime data provider (founded 2007) that operated one of the world's largest terrestrial AIS receiver networks and a documented REST API (apiv2.fleetmon.com) for vessel search, live and historical AIS positions, port calls, expected arrivals, ETA and voyage planning. Kpler acquired FleetMon alongside MarineTraffic in 2023, the FleetMon platform and API were phased out from January 2024 and migrated into MarineTraffic, and in September 2025 the combined AIS assets were unified under the Kpler AIS brand. As of 2026 the fleetmon.com domain, developer portal, and API no longer resolve - this entry preserves the final archived API surface and points to the Kpler / MarineTraffic successor services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fleetmon.png
layout: provider
modified: '2026-07-11'
name: FleetMon
nav: Providers
network: true
overview: 'FleetMon publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Basic Vessel Data API, Current API, Distance To Port API, and 34 more. Tagged areas include Vessel Tracking, Maritime, AIS, Ships, and Ports.


  FleetMon''s developer surface includes authentication and 12 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 22.7
  delta: -0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 52.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleetmon/refs/heads/main/screenshots/fleetmon-2026-07-25T214742.png
security:
- kind: authentication
  name: Fleetmon Authentication
  slug: fleetmon-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Fleetmon Domain Security
  slug: fleetmon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fleetmon
tags:
- Vessel Tracking
- Maritime
- AIS
- Ships
- Ports
- Port Calls
- Shipping
- Retired
website: https://www.kpler.com
---
