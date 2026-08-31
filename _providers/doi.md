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
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Doi Agentic Access
  operation_count: 284
  slug: doi-agentic-access
  summary_line: 284 operations · 35 acting
api_count: 1
apis:
- description: The National Park Service Data API provides authoritative data about NPS sites including parks, alerts, campgrounds, events, visitor centers, news releases, articles, and educational lesson plans. Acc
  name: NPS Data API
  slug: nps-data-api
- description: Real-time earthquake data feeds, notifications, and web services providing access to seismic event data including location, magnitude, depth, and related hazard information. Supports GeoJSON, QuakeML,
  name: USGS Earthquake Hazards Web Services
  slug: usgs-earthquake-hazards-web-services
- description: API access to the USGS Mineral Resources Data System (MRDS) and related mineral deposit databases. Supports geographic queries, bounding box searches, point queries, and access to data on mineral depo
  name: USGS Mineral Resources Data API
  slug: usgs-mineral-resources-data-api
- description: Bureau of Land Management geospatial REST services providing access to federal land status, cadastral data (Public Land Survey System), mineral rights boundaries, and other BLM-managed land data throu
  name: BLM GIS REST Services
  slug: blm-gis-rest-services
- description: ScienceBase provides collaborative scientific data management infrastructure enabling upload, documentation, sharing, and discovery of USGS scientific data using standards-compliant REST web services.
  name: USGS ScienceBase API
  slug: usgs-sciencebase-api
- description: Code identifying the agency or organization used for site information, data sources, and permitting agencies. Agency codes are fixed values assigned by the National Water Information System (NWIS).
  name: Department of Interior agency-codes API
  slug: doi-agency-codes-api
- description: The recommended vertical datum is NAVD88 (North American Vertical Datum of 1988) where applicable as stated in Office of Information Technical Memo 2002.01. NGVD29 (National Geodetic Vertical Datum of
  name: Department of Interior altitude-datums API
  slug: doi-altitude-datums-api
- description: Local aquifers in USGS data are identified by an aquifer name and geohydrologic unit code (a three-digit number related to the age of the formation, followed by a 4 or 5 character abbreviation for the
  name: Department of Interior aquifer-codes API
  slug: doi-aquifer-codes-api
- description: Groundwater occurs in aquifers under two different conditions. Where water only partly fills an aquifer, the upper surface is free to rise and decline. These aquifers are referred to as unconfined (or
  name: Department of Interior aquifer-types API
  slug: doi-aquifer-types-api
- description: Channel measurements taken as part of streamflow field measurements.
  name: Department of Interior channel-measurements API
  slug: doi-channel-measurements-api
- description: Citations associated with water measurement methods.
  name: Department of Interior citations API
  slug: doi-citations-api
- description: This endpoint combines metadata from timeseries and field measurements collections by site.
  name: Department of Interior combined-metadata API
  slug: doi-combined-metadata-api
- description: Continuous data are collected via automated sensors installed at a monitoring location. They are collected at a high frequency and often at a fixed 15-minute interval. Depending on the specific monito
  name: Department of Interior continuous API
  slug: doi-continuous-api
- description: Appropriate code on the schedule to indicate the accuracy of the latitude-longitude values.
  name: Department of Interior coordinate-accuracy-codes API
  slug: doi-coordinate-accuracy-codes-api
- description: Horizontal datum code for the latitude/longitude coordinates. There are currently more than 300 horizontal datums available for entry.
  name: Department of Interior coordinate-datum-codes API
  slug: doi-coordinate-datum-codes-api
- description: Methods used to determine latitude-longitude values.
  name: Department of Interior coordinate-method-codes API
  slug: doi-coordinate-method-codes-api
- description: The name of the county or county equivalent (parish, borough, planning reagion, etc.) in which the site is located. List includes Census Bureau FIPS county codes, names and associated Country and Stat
  name: Department of Interior counties API
  slug: doi-counties-api
- description: FIPS country codes and names.
  name: Department of Interior countries API
  slug: doi-countries-api
- description: Daily data provide one data value to represent water conditions for the day. Throughout much of the history of the USGS, the primary water data available was daily data collected manually at the monit
  name: Department of Interior daily API
  slug: doi-daily-api
- description: Field measurements are physically measured values collected during a visit to the monitoring location. Field measurements consist of measurements of gage height and discharge, and readings of groundwa
  name: Department of Interior field-measurements API
  slug: doi-field-measurements-api
- description: This endpoint provides metadata about field measurement collections, including when the earliest and most recent observations for a parameter occurred at a monitoring location and its units.
  name: Department of Interior field-measurements-metadata API
  slug: doi-field-measurements-metadata-api
- description: 'Hydrologic units are geographic areas representing part or all of a surface drainage basin or distinct hydrologic feature identified by a unique number (HUC), and a name. The United States is divided '
  name: Department of Interior hydrologic-unit-codes API
  slug: doi-hydrologic-unit-codes-api
- description: This endpoint provides the most recent observation for each time series of continuous data. Continuous data are collected via automated sensors installed at a monitoring location. They are collected a
  name: Department of Interior latest-continuous API
  slug: doi-latest-continuous-api
- description: Daily data provide one data value to represent water conditions for the day. Throughout much of the history of the USGS, the primary water data available was daily data collected manually at the monit
  name: Department of Interior latest-daily API
  slug: doi-latest-daily-api
- description: Field measurements are physically measured values collected during a visit to the monitoring location. Field measurements consist of measurements of gage height and discharge, and readings of groundwa
  name: Department of Interior latest-field-measurements API
  slug: doi-latest-field-measurements-api
- description: Medium refers to the specific environmental medium from which the sample was collected. Medium type differs from site type because one site type, such as surface water, could have data for several med
  name: Department of Interior medium-codes API
  slug: doi-medium-codes-api
- description: Categorical standards for methods describing the associated data's appropriateness for an intended use.
  name: Department of Interior method-categories API
  slug: doi-method-categories-api
- description: Citation identifiers for water measurement methods.
  name: Department of Interior method-citations API
  slug: doi-method-citations-api
- description: Water measurement or water-quality analytical methods. Codes and descriptions defining a method for calculating or measuring the value of a water quality or quantity parameter. Method codes are associ
  name: Department of Interior methods API
  slug: doi-methods-api
- description: Location information is basic information about the monitoring location including the name, identifier, agency responsible for data collection, and the date the location was established. It also inclu
  name: Department of Interior monitoring-locations API
  slug: doi-monitoring-locations-api
- description: National aquifers are the principal aquifers or aquifer systems in the United States, defined as regionally extensive aquifers or aquifer systems that have the potential to be used as a source of pota
  name: Department of Interior national-aquifer-codes API
  slug: doi-national-aquifer-codes-api
- description: Parameter codes are 5-digit codes and associated descriptions used to identify the constituent measured and the units of measure. Some parameter code definitions include information about the sampling
  name: Department of Interior parameter-codes API
  slug: doi-parameter-codes-api
- description: Annual peak flow values are the maximum instantaneous streamflow values recorded at a particular site for the entire water year from October 1 to September 30. Note that the annual peak flow value may
  name: Department of Interior peaks API
  slug: doi-peaks-api
- description: Code indicating the reliability of the data available for the site.
  name: Department of Interior reliability-codes API
  slug: doi-reliability-codes-api
- description: These APIs provide OGC-compliant interfaces to USGS water data, letting you download continuous sensor measurements, discrete field measurements, metadata about monitoring locations, and more.
  name: Department of Interior server API
  slug: doi-server-api
- description: The hydrologic cycle setting or a man-made feature thought to affect the hydrologic conditions measured at a site. Primary and secondary site types associated with data collection sites. All sites hav
  name: Department of Interior site-types API
  slug: doi-site-types-api
- description: State name or territory. Includes U.S. states and foreign entities classified under FIPS as 'Principal Administrative Divisions'.
  name: Department of Interior states API
  slug: doi-states-api
- description: Statistic codes.
  name: Department of Interior statistic-codes API
  slug: doi-statistic-codes-api
- description: 'Daily data and continuous measurements are grouped into time series, which represent a collection of observations of a single parameter, potentially aggregated using a standard statistic, at a single '
  name: Department of Interior time-series-metadata API
  slug: doi-time-series-metadata-api
- description: The ISO 8601 standard defines time zone offsets as a numerical value added to a local time to convert it to Coordinated Universal Time (UTC), either as +hh:mm or -hh:mm, or represented by the letter Z
  name: Department of Interior time-zone-codes API
  slug: doi-time-zone-codes-api
- description: The code that best describes the topographic setting in which the site is located. Topographic setting refers to the geomorphic features in the vicinity of the site.
  name: Department of Interior topographic-codes API
  slug: doi-topographic-codes-api
artifact_total: 94
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes API
  slug: open-doi-agency-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes altitude-datums API
  slug: open-doi-altitude-datums-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes aquifer-codes API
  slug: open-doi-aquifer-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes aquifer-types API
  slug: open-doi-aquifer-types-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes channel-measurements API
  slug: open-doi-channel-measurements-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes citations API
  slug: open-doi-citations-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes combined-metadata API
  slug: open-doi-combined-metadata-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes continuous API
  slug: open-doi-continuous-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes coordinate-accuracy-codes API
  slug: open-doi-coordinate-accuracy-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes coordinate-datum-codes API
  slug: open-doi-coordinate-datum-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes coordinate-method-codes API
  slug: open-doi-coordinate-method-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes counties API
  slug: open-doi-counties-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes countries API
  slug: open-doi-countries-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes daily API
  slug: open-doi-daily-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes field-measurements API
  slug: open-doi-field-measurements-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes field-measurements-metadata API
  slug: open-doi-field-measurements-metadata-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes hydrologic-unit-codes API
  slug: open-doi-hydrologic-unit-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes latest-continuous API
  slug: open-doi-latest-continuous-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes latest-daily API
  slug: open-doi-latest-daily-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes latest-field-measurements API
  slug: open-doi-latest-field-measurements-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes medium-codes API
  slug: open-doi-medium-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes method-categories API
  slug: open-doi-method-categories-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes method-citations API
  slug: open-doi-method-citations-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes methods API
  slug: open-doi-methods-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes monitoring-locations API
  slug: open-doi-monitoring-locations-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes national-aquifer-codes API
  slug: open-doi-national-aquifer-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes parameter-codes API
  slug: open-doi-parameter-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes peaks API
  slug: open-doi-peaks-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes reliability-codes API
  slug: open-doi-reliability-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes server API
  slug: open-doi-server-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes site-types API
  slug: open-doi-site-types-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes states API
  slug: open-doi-states-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes statistic-codes API
  slug: open-doi-statistic-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes time-series-metadata API
  slug: open-doi-time-series-metadata-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes time-zone-codes API
  slug: open-doi-time-zone-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes topographic-codes API
  slug: open-doi-topographic-codes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.doi.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.doi.gov/ocio/customers/web-services
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/usgs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/department-of-the-interior
- group: company
  title: ''
  type: Blog
  url: https://www.doi.gov/blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/interior
- group: commercial
  title: ''
  type: Plans
  url: plans/doi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doi-finops.yml
created: '2026-06-13'
description: The U.S. Department of the Interior (DOI) manages and conserves federal lands and natural resources across America. DOI's bureaus and offices provide REST APIs and data services covering national park information, water resources, earthquake data, mineral resources, geospatial federal land boundaries, and wildlife data. Key API providers include the National Park Service (NPS), the U.S. Geological Survey (USGS), and the Bureau of Land Management (BLM).
examples:
- key_count: 3
  name: Usgs Water Collections Example
  slug: usgs-water-collections-example
- key_count: 3
  name: Usgs Water Error Example
  slug: usgs-water-error-example
- key_count: 3
  name: Usgs Water Monitoring Location Example
  slug: usgs-water-monitoring-location-example
finops:
- name: Doi Finops
  service_category: ''
  slug: doi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doi.png
json_schemas:
- name: Error
  property_count: 1
  slug: doi-usgs-water-Error
- name: Queryable
  property_count: 6
  slug: doi-usgs-water-queryable
- name: Queryables
  property_count: 1
  slug: doi-usgs-water-queryables
- name: Tilematrixsetlink
  property_count: 2
  slug: doi-usgs-water-tilematrixsetlink
- name: Tiles
  property_count: 2
  slug: doi-usgs-water-tiles
jsonld:
- class_count: 10
  name: Doi Context
  property_count: 40
  slug: doi-context
layout: provider
modified: '2026-06-13'
name: Department of Interior
nav: Providers
network: true
overview: 'Department of Interior publishes 36 APIs on the [APIs.io](https://apis.io/) network, including agency-codes API, altitude-datums API, aquifer-codes API, and 33 more. Tagged areas include Federal-Government, National Parks, Federal Lands, Water Resources, and Wildlife.


  The Department of Interior catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of Interior''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Doi Plans Pricing
  plan_count: 3
  slug: doi-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Doi Rate Limits
  slug: doi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Department of Interior API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: doi-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.5
    developer_ergonomics: 23.8
    discoverability: 44.4
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doi/refs/heads/main/screenshots/doi-2026-06-20T180128.png
security:
- kind: authentication
  name: Doi Authentication
  slug: doi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Doi Domain Security
  slug: doi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: doi
tags:
- Federal-Government
- National Parks
- Federal Lands
- Water Resources
- Wildlife
- Minerals
- Geospatial
- Geology
- Native American Affairs
- Public Lands
website: https://www.doi.gov/
---
