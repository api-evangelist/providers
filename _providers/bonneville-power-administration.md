---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bonneville Power Administration Agentic Access
  operation_count: 8
  slug: bonneville-power-administration-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: The BPA GIS Data Hub provides publicly available geospatial data from Bonneville Power Administration. The hub is built on ArcGIS and supports data downloads in multiple formats including CSV, KML, Ge
  name: BPA GIS Data Hub API
  slug: gis-data-api
- description: BPA publishes real-time and historical wind and solar generation data for the Balancing Authority area. Data includes total wind generation, total solar generation, net generation, and load data avail
  name: BPA Wind and Solar Generation Data
  slug: wind-solar-data
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: spec
  description: The Customers API from Bonneville Power Administration — 3 operation(s) for customers.
  name: Bonneville Power Administration Customers API
  slug: bonneville-power-administration-customers-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: spec
  description: The Hydrology API from Bonneville Power Administration — 1 operation(s) for hydrology.
  name: Bonneville Power Administration Hydrology API
  slug: bonneville-power-administration-hydrology-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: spec
  description: The Right of Way API from Bonneville Power Administration — 1 operation(s) for right of way.
  name: Bonneville Power Administration Right of Way API
  slug: bonneville-power-administration-right-of-way-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: spec
  description: The Service Area API from Bonneville Power Administration — 1 operation(s) for service area.
  name: Bonneville Power Administration Service Area API
  slug: bonneville-power-administration-service-area-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: spec
  description: The Transmission API from Bonneville Power Administration — 2 operation(s) for transmission.
  name: Bonneville Power Administration Transmission API
  slug: bonneville-power-administration-transmission-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers API
  slug: open-bonneville-power-administration-customers-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Hydrology API
  slug: open-bonneville-power-administration-hydrology-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Right of Way API
  slug: open-bonneville-power-administration-right-of-way-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Service Area API
  slug: open-bonneville-power-administration-service-area-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Transmission API
  slug: open-bonneville-power-administration-transmission-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub API
  slug: open-bonneville-power-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bonneville-power-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonneville-power-administration-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bpa.gov/rss-feeds/news-feed-no-cp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bonnevillepower
- group: company
  title: ''
  type: Website
  url: https://www.bpa.gov
- group: company
  title: ''
  type: About
  url: https://www.bpa.gov/about/
- group: other
  title: ''
  type: OpenData
  url: https://data-bpagis.hub.arcgis.com
- group: other
  title: ''
  type: DataDownload
  url: https://transmission.bpa.gov/business/operations/Wind/
- group: start
  title: ''
  type: CustomerPortal
  url: https://www.bpa.gov/energy-and-services/
- group: operate
  title: ''
  type: Contact
  url: https://www.bpa.gov/about/contact/
created: '2024-11-25'
description: The Bonneville Power Administration (BPA) is a federal agency within the U.S. Department of Energy that markets wholesale electrical power from federal hydroelectric projects in the Pacific Northwest. BPA also operates and maintains about three-quarters of the high-voltage transmission in the Pacific Northwest. The agency provides publicly available GIS data, energy statistics, and operational data through its data hub and web services.
features:
- features:
  - ArcGIS REST API
  - GeoJSON Export
  - CSV Export
  - KML Export
  - GeoTIFF Export
  - Web Map Service (WMS)
  - Web Feature Service (WFS)
  name: GeoServices API
  url: https://data-bpagis.hub.arcgis.com
- features:
  - CSV Download
  - JSON Download
  - GeoJSON Download
  - Shapefile Download
  - KML Download
  name: Open Data Downloads
  url: https://data-bpagis.hub.arcgis.com
finops:
- name: Bonneville Power Administration Finops
  service_category: API
  slug: bonneville-power-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bonneville-power-administration.png
layout: provider
modified: '2026-04-19'
name: Bonneville Power Administration
nav: Providers
network: true
overview: 'Bonneville Power Administration publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Hydrology API, Right of Way API, and 2 more. Tagged areas include Energy, Federal-Government, GIS, Hydroelectric, and Pacific Northwest.


  Bonneville Power Administration''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Bonneville Power Administration Plans Pricing
  plan_count: 3
  slug: bonneville-power-administration-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Bonneville Power Administration Rate Limits
  slug: bonneville-power-administration-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bonneville-power-administration/refs/heads/main/screenshots/bonneville-power-administration-2026-06-20T173608.png
security:
- kind: domain-security
  name: Bonneville Power Administration Domain Security
  slug: bonneville-power-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bonneville-power-administration
tags:
- Energy
- Federal-Government
- GIS
- Hydroelectric
- Pacific Northwest
- Power
- Transmission
- Wind
use_cases:
- features:
  - Geospatial Data Download
  - Map Visualization
  - Service Area Data
  - Transmission Infrastructure Mapping
  - Energy Facility Locations
  name: GIS Data Analysis
  url: https://data-bpagis.hub.arcgis.com
- features:
  - Wind Generation Data
  - Solar Generation Data
  - Real-Time Generation Monitoring
  - Historical Data Access
  - Grid Load Tracking
  name: Renewable Energy Monitoring
  url: https://transmission.bpa.gov/business/operations/Wind/
- features:
  - Transmission Availability
  - Hourly Firm Data
  - System Load Monitoring
  - Grid Operations Data
  name: Transmission System Monitoring
  url: https://www.bpa.gov/energy-and-services/transmission/
website: https://www.bpa.gov
---
