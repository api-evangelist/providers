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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fleetmon Agentic Access
  operation_count: 49
  slug: fleetmon-agentic-access
  summary_line: 49 operations · 6 acting
api_count: 1
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
artifact_total: 78
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data API
  slug: open-fleetmon-basic-vessel-data-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Current API
  slug: open-fleetmon-current-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Distance To Port API
  slug: open-fleetmon-distance-to-port-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Estimated Laytime - Specific Vessel API
  slug: open-fleetmon-estimated-laytime-specific-vessel-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Expected Port Arrivals API
  slug: open-fleetmon-expected-port-arrivals-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Fleet Tracker API
  slug: open-fleetmon-fleet-tracker-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Historical AIS Static Messages API
  slug: open-fleetmon-historical-ais-static-messages-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Historical Track API API
  slug: open-fleetmon-historical-track-api-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Login Token API
  slug: open-fleetmon-login-token-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Logistics API
  slug: open-fleetmon-logistics-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data My Fleet Positions API
  slug: open-fleetmon-my-fleet-positions-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Next Port / ETA Calculation API
  slug: open-fleetmon-next-port-eta-calculation-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Non AIS Vessel Particulars API
  slug: open-fleetmon-non-ais-vessel-particulars-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Port Calls per Port API
  slug: open-fleetmon-port-calls-per-port-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Port Calls per Vessel API
  slug: open-fleetmon-port-calls-per-vessel-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Port Search API
  slug: open-fleetmon-port-search-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Regional AIS API
  slug: open-fleetmon-regional-ais-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data RoRo Ferry Terminal Demo API
  slug: open-fleetmon-roro-ferry-terminal-demo-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Change Events API
  slug: open-fleetmon-vessel-change-events-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Dynamic AIS API
  slug: open-fleetmon-vessel-dynamic-ais-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel ETA & Destination Change Events API
  slug: open-fleetmon-vessel-eta-destination-change-events-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Identity API
  slug: open-fleetmon-vessel-identity-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Photo API
  slug: open-fleetmon-vessel-photo-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Positions Only API
  slug: open-fleetmon-vessel-positions-only-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Positions with Extended Vessel Data API
  slug: open-fleetmon-vessel-positions-with-extended-vessel-data-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Route From Last Port API
  slug: open-fleetmon-vessel-route-from-last-port-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Route To Next Port API
  slug: open-fleetmon-vessel-route-to-next-port-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Schedule API
  slug: open-fleetmon-vessel-schedule-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessel Search API
  slug: open-fleetmon-vessel-search-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessels in Port API
  slug: open-fleetmon-vessels-in-port-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessels Near Position API
  slug: open-fleetmon-vessels-near-position-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Vessels Nearby API
  slug: open-fleetmon-vessels-nearby-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Voyage Planning API
  slug: open-fleetmon-voyage-planning-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Water API
  slug: open-fleetmon-water-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Weather API
  slug: open-fleetmon-weather-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Zone Call API
  slug: open-fleetmon-zone-call-api
- collection_type: open
  name: FleetMon API Reference Basic Vessel Data Zone Information API
  slug: open-fleetmon-zone-information-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fleetmon-capability-edges.yml
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


  FleetMon''s developer surface includes authentication and 13 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
