---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Usgs Water Agentic Access
  operation_count: 284
  slug: usgs-water-agentic-access
  summary_line: 284 operations · 35 acting
api_count: 43
apis:
- description: Provides near real-time water data — streamflow, gage height, temperature, specific conductance, and hundreds of other parameters — from thousands of USGS monitoring sites. Values are typically record
  name: USGS Instantaneous Values Service
  slug: instantaneous-values
- description: Returns historical summarized daily hydrologic data (mean, median, maximum, minimum) for streams, lakes, estuaries, and wells. Many sites have more than 10 years of record. Supports WaterML 1.1, Water
  name: USGS Daily Values Service
  slug: daily-values
- description: Searches and retrieves metadata for millions of USGS hydrologic data collection sites including streams, springs, wells, lakes, reservoirs, estuaries, and glaciers. Filtering options include site numb
  name: USGS Site Service
  slug: site-service
- description: Retrieves daily, monthly, or annual statistics (mean, minimum, maximum, median, and percentiles P05–P95) computed from approved historical time-series data. Supports up to 10 sites per request and ret
  name: USGS Statistics Service
  slug: statistics-service
- description: Provides historical manually-recorded groundwater level measurements from USGS wells and monitoring sites. Returns depth-to-water and water-level-above-datum values in JSON or RDB format. For automate
  name: USGS Groundwater Levels Service
  slug: groundwater-levels
- description: A cooperative service sponsored by USGS and EPA providing access to water quality data from over 400 agencies including USGS NWIS and EPA WQX. Endpoints cover monitoring sites, chemistry results, biol
  name: Water Quality Portal (WQP) API
  slug: water-quality-portal
- description: Next-generation statistics API at api.waterdata.usgs.gov providing computed statistical summaries for USGS water time series. Part of the platform replacing the legacy WaterServices statistics endpoin
  name: USGS Water Data Statistics API
  slug: statistics-next-gen
- description: Code identifying the agency or organization used for site information, data sources, and permitting agencies. Agency codes are fixed values assigned by the National Water Information System (NWIS).
  name: USGS Water Services agency-codes API
  slug: usgs-water-agency-codes-api
- description: The recommended vertical datum is NAVD88 (North American Vertical Datum of 1988) where applicable as stated in Office of Information Technical Memo 2002.01. NGVD29 (National Geodetic Vertical Datum of
  name: USGS Water Services altitude-datums API
  slug: usgs-water-altitude-datums-api
- description: Local aquifers in USGS data are identified by an aquifer name and geohydrologic unit code (a three-digit number related to the age of the formation, followed by a 4 or 5 character abbreviation for the
  name: USGS Water Services aquifer-codes API
  slug: usgs-water-aquifer-codes-api
- description: Groundwater occurs in aquifers under two different conditions. Where water only partly fills an aquifer, the upper surface is free to rise and decline. These aquifers are referred to as unconfined (or
  name: USGS Water Services aquifer-types API
  slug: usgs-water-aquifer-types-api
- description: Channel measurements taken as part of streamflow field measurements.
  name: USGS Water Services channel-measurements API
  slug: usgs-water-channel-measurements-api
- description: Citations associated with water measurement methods.
  name: USGS Water Services citations API
  slug: usgs-water-citations-api
- description: This endpoint combines metadata from timeseries and field measurements collections by site.
  name: USGS Water Services combined-metadata API
  slug: usgs-water-combined-metadata-api
- description: Continuous data are collected via automated sensors installed at a monitoring location. They are collected at a high frequency and often at a fixed 15-minute interval. Depending on the specific monito
  name: USGS Water Services continuous API
  slug: usgs-water-continuous-api
- description: Appropriate code on the schedule to indicate the accuracy of the latitude-longitude values.
  name: USGS Water Services coordinate-accuracy-codes API
  slug: usgs-water-coordinate-accuracy-codes-api
- description: Horizontal datum code for the latitude/longitude coordinates. There are currently more than 300 horizontal datums available for entry.
  name: USGS Water Services coordinate-datum-codes API
  slug: usgs-water-coordinate-datum-codes-api
- description: Methods used to determine latitude-longitude values.
  name: USGS Water Services coordinate-method-codes API
  slug: usgs-water-coordinate-method-codes-api
- description: The name of the county or county equivalent (parish, borough, planning reagion, etc.) in which the site is located. List includes Census Bureau FIPS county codes, names and associated Country and Stat
  name: USGS Water Services counties API
  slug: usgs-water-counties-api
- description: FIPS country codes and names.
  name: USGS Water Services countries API
  slug: usgs-water-countries-api
- description: Daily data provide one data value to represent water conditions for the day. Throughout much of the history of the USGS, the primary water data available was daily data collected manually at the monit
  name: USGS Water Services daily API
  slug: usgs-water-daily-api
- description: Field measurements are physically measured values collected during a visit to the monitoring location. Field measurements consist of measurements of gage height and discharge, and readings of groundwa
  name: USGS Water Services field-measurements API
  slug: usgs-water-field-measurements-api
- description: This endpoint provides metadata about field measurement collections, including when the earliest and most recent observations for a parameter occurred at a monitoring location and its units.
  name: USGS Water Services field-measurements-metadata API
  slug: usgs-water-field-measurements-metadata-api
- description: 'Hydrologic units are geographic areas representing part or all of a surface drainage basin or distinct hydrologic feature identified by a unique number (HUC), and a name. The United States is divided '
  name: USGS Water Services hydrologic-unit-codes API
  slug: usgs-water-hydrologic-unit-codes-api
- description: This endpoint provides the most recent observation for each time series of continuous data. Continuous data are collected via automated sensors installed at a monitoring location. They are collected a
  name: USGS Water Services latest-continuous API
  slug: usgs-water-latest-continuous-api
- description: Daily data provide one data value to represent water conditions for the day. Throughout much of the history of the USGS, the primary water data available was daily data collected manually at the monit
  name: USGS Water Services latest-daily API
  slug: usgs-water-latest-daily-api
- description: Field measurements are physically measured values collected during a visit to the monitoring location. Field measurements consist of measurements of gage height and discharge, and readings of groundwa
  name: USGS Water Services latest-field-measurements API
  slug: usgs-water-latest-field-measurements-api
- description: Medium refers to the specific environmental medium from which the sample was collected. Medium type differs from site type because one site type, such as surface water, could have data for several med
  name: USGS Water Services medium-codes API
  slug: usgs-water-medium-codes-api
- description: Categorical standards for methods describing the associated data's appropriateness for an intended use.
  name: USGS Water Services method-categories API
  slug: usgs-water-method-categories-api
- description: Citation identifiers for water measurement methods.
  name: USGS Water Services method-citations API
  slug: usgs-water-method-citations-api
- description: Water measurement or water-quality analytical methods. Codes and descriptions defining a method for calculating or measuring the value of a water quality or quantity parameter. Method codes are associ
  name: USGS Water Services methods API
  slug: usgs-water-methods-api
- description: Location information is basic information about the monitoring location including the name, identifier, agency responsible for data collection, and the date the location was established. It also inclu
  name: USGS Water Services monitoring-locations API
  slug: usgs-water-monitoring-locations-api
- description: National aquifers are the principal aquifers or aquifer systems in the United States, defined as regionally extensive aquifers or aquifer systems that have the potential to be used as a source of pota
  name: USGS Water Services national-aquifer-codes API
  slug: usgs-water-national-aquifer-codes-api
- description: Parameter codes are 5-digit codes and associated descriptions used to identify the constituent measured and the units of measure. Some parameter code definitions include information about the sampling
  name: USGS Water Services parameter-codes API
  slug: usgs-water-parameter-codes-api
- description: Annual peak flow values are the maximum instantaneous streamflow values recorded at a particular site for the entire water year from October 1 to September 30. Note that the annual peak flow value may
  name: USGS Water Services peaks API
  slug: usgs-water-peaks-api
- description: Code indicating the reliability of the data available for the site.
  name: USGS Water Services reliability-codes API
  slug: usgs-water-reliability-codes-api
- description: These APIs provide OGC-compliant interfaces to USGS water data, letting you download continuous sensor measurements, discrete field measurements, metadata about monitoring locations, and more.
  name: USGS Water Services server API
  slug: usgs-water-server-api
- description: The hydrologic cycle setting or a man-made feature thought to affect the hydrologic conditions measured at a site. Primary and secondary site types associated with data collection sites. All sites hav
  name: USGS Water Services site-types API
  slug: usgs-water-site-types-api
- description: State name or territory. Includes U.S. states and foreign entities classified under FIPS as 'Principal Administrative Divisions'.
  name: USGS Water Services states API
  slug: usgs-water-states-api
- description: Statistic codes.
  name: USGS Water Services statistic-codes API
  slug: usgs-water-statistic-codes-api
- description: 'Daily data and continuous measurements are grouped into time series, which represent a collection of observations of a single parameter, potentially aggregated using a standard statistic, at a single '
  name: USGS Water Services time-series-metadata API
  slug: usgs-water-time-series-metadata-api
- description: The ISO 8601 standard defines time zone offsets as a numerical value added to a local time to convert it to Coordinated Universal Time (UTC), either as +hh:mm or -hh:mm, or represented by the letter Z
  name: USGS Water Services time-zone-codes API
  slug: usgs-water-time-zone-codes-api
- description: The code that best describes the topographic setting in which the site is located. Topographic setting refers to the geomorphic features in the vicinity of the site.
  name: USGS Water Services topographic-codes API
  slug: usgs-water-topographic-codes-api
artifact_total: 125
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes API
  slug: open-usgs-water-agency-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes altitude-datums API
  slug: open-usgs-water-altitude-datums-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes aquifer-codes API
  slug: open-usgs-water-aquifer-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes aquifer-types API
  slug: open-usgs-water-aquifer-types-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes channel-measurements API
  slug: open-usgs-water-channel-measurements-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes citations API
  slug: open-usgs-water-citations-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes combined-metadata API
  slug: open-usgs-water-combined-metadata-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes continuous API
  slug: open-usgs-water-continuous-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes coordinate-accuracy-codes API
  slug: open-usgs-water-coordinate-accuracy-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes coordinate-datum-codes API
  slug: open-usgs-water-coordinate-datum-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes coordinate-method-codes API
  slug: open-usgs-water-coordinate-method-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes counties API
  slug: open-usgs-water-counties-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes countries API
  slug: open-usgs-water-countries-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes daily API
  slug: open-usgs-water-daily-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes field-measurements API
  slug: open-usgs-water-field-measurements-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes field-measurements-metadata API
  slug: open-usgs-water-field-measurements-metadata-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes hydrologic-unit-codes API
  slug: open-usgs-water-hydrologic-unit-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes latest-continuous API
  slug: open-usgs-water-latest-continuous-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes latest-daily API
  slug: open-usgs-water-latest-daily-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes latest-field-measurements API
  slug: open-usgs-water-latest-field-measurements-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes medium-codes API
  slug: open-usgs-water-medium-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes method-categories API
  slug: open-usgs-water-method-categories-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes method-citations API
  slug: open-usgs-water-method-citations-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes methods API
  slug: open-usgs-water-methods-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes monitoring-locations API
  slug: open-usgs-water-monitoring-locations-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes national-aquifer-codes API
  slug: open-usgs-water-national-aquifer-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes parameter-codes API
  slug: open-usgs-water-parameter-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes peaks API
  slug: open-usgs-water-peaks-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes reliability-codes API
  slug: open-usgs-water-reliability-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes server API
  slug: open-usgs-water-server-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes site-types API
  slug: open-usgs-water-site-types-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes states API
  slug: open-usgs-water-states-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes statistic-codes API
  slug: open-usgs-water-statistic-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes time-series-metadata API
  slug: open-usgs-water-time-series-metadata-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes time-zone-codes API
  slug: open-usgs-water-time-zone-codes-api
- collection_type: open
  name: USGS Water Data OGC APIs agency-codes topographic-codes API
  slug: open-usgs-water-topographic-codes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usgs-water-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usgs-water-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usgs-water-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://waterservices.usgs.gov/
- group: company
  title: ''
  type: Website
  url: https://api.waterdata.usgs.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://waterservices.usgs.gov/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.waterdata.usgs.gov/docs/
- group: start
  title: ''
  type: Signup
  url: https://api.waterdata.usgs.gov/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doi.gov/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits
- group: operate
  title: ''
  type: Contact
  url: mailto:wdfn@usgs.gov
- group: operate
  title: ''
  type: StatusPage
  url: https://waterservices.usgs.gov/test-tools/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/usgs-water/refs/heads/main/plans/usgs-water-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/usgs-water/refs/heads/main/rate-limits/usgs-water-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/usgs-water/refs/heads/main/finops/usgs-water-finops.yml
created: '2026-06-13'
description: The U.S. Geological Survey (USGS) National Water Information System (NWIS) exposes a suite of REST APIs providing access to real-time and historical water data from over 1.5 million monitoring locations across the United States and territories. The legacy WaterServices APIs (being decommissioned in early 2027) and the next-generation api.waterdata.usgs.gov OGC-compliant APIs together cover streamflow, groundwater levels, water quality, site metadata, and statistical summaries. All services are free, publicly funded, and require no authentication for standard use; API keys are available at no cost for higher rate-limit access.
examples:
- key_count: 7
  name: Usgs Water Examples
  slug: usgs-water-examples
finops:
- name: Usgs Water Finops
  service_category: Government Open Data / Environmental APIs
  slug: usgs-water-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usgs-water.png
json_schemas:
- name: Agency Codes
  property_count: 2
  slug: agency-codes
- name: Altitude Datums
  property_count: 2
  slug: altitude-datums
- name: Aquifer Codes
  property_count: 2
  slug: aquifer-codes
- name: Aquifer Types
  property_count: 2
  slug: aquifer-types
- name: Channel Measurements
  property_count: 26
  slug: channel-measurements
- name: Citations
  property_count: 2
  slug: citations
- name: Combined Metadata
  property_count: 56
  slug: combined-metadata
- name: Continuous
  property_count: 10
  slug: continuous
- name: Coordinate Accuracy Codes
  property_count: 2
  slug: coordinate-accuracy-codes
- name: Coordinate Datum Codes
  property_count: 2
  slug: coordinate-datum-codes
- name: Coordinate Method Codes
  property_count: 2
  slug: coordinate-method-codes
- name: Counties
  property_count: 5
  slug: counties
- name: Countries
  property_count: 2
  slug: countries
- name: Daily
  property_count: 10
  slug: daily
- name: Field Measurements Metadata
  property_count: 8
  slug: field-measurements-metadata
- name: Field Measurements
  property_count: 21
  slug: field-measurements
- name: Hydrologic Unit Codes
  property_count: 3
  slug: hydrologic-unit-codes
- name: Latest Continuous
  property_count: 11
  slug: latest-continuous
- name: Latest Daily
  property_count: 11
  slug: latest-daily
- name: Latest Field Measurements
  property_count: 21
  slug: latest-field-measurements
- name: Medium Codes
  property_count: 4
  slug: medium-codes
- name: Method Categories
  property_count: 3
  slug: method-categories
- name: Method Citations
  property_count: 5
  slug: method-citations
- name: Methods
  property_count: 5
  slug: methods
- name: Monitoring Locations
  property_count: 43
  slug: monitoring-locations
- name: National Aquifer Codes
  property_count: 2
  slug: national-aquifer-codes
- name: Parameter Codes
  property_count: 13
  slug: parameter-codes
- name: Peaks
  property_count: 15
  slug: peaks
- name: Reliability Codes
  property_count: 2
  slug: reliability-codes
- name: Site Types
  property_count: 4
  slug: site-types
- name: States
  property_count: 5
  slug: states
- name: Statistic Codes
  property_count: 3
  slug: statistic-codes
- name: Time Series Metadata
  property_count: 21
  slug: time-series-metadata
- name: Time Zone Codes
  property_count: 7
  slug: time-zone-codes
- name: Topographic Codes
  property_count: 4
  slug: topographic-codes
jsonld:
- class_count: 0
  name: Usgs Water Api Context
  property_count: 0
  slug: usgs-water-api
- class_count: 2
  name: Usgs Water Context
  property_count: 151
  slug: usgs-water-context
layout: provider
modified: '2026-06-13'
name: USGS Water Services
nav: Providers
network: true
overview: 'USGS Water Services publishes 36 APIs on the [APIs.io](https://apis.io/) network, including agency-codes API, altitude-datums API, aquifer-codes API, and 33 more. Tagged areas include Water, Streamflow, Groundwater, Water Quality, and Hydrology.


  The USGS Water Services catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  USGS Water Services'' developer surface includes authentication, documentation, signup flow, and 12 more developer resources.'
plans:
- name: Usgs Water Plans
  plan_count: 2
  slug: usgs-water-plans
random_paper: 13
rate_limits:
- limit_count: 2
  name: Usgs Water Rate Limits
  slug: usgs-water-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: USGS Water Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: usgs-water-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 59.1
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 48.2
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
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usgs-water/refs/heads/main/screenshots/usgs-water-2026-06-20T200736.png
security:
- kind: authentication
  name: Usgs Water Authentication
  slug: usgs-water-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Usgs Water Domain Security
  slug: usgs-water-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: usgs-water
tags:
- Water
- Streamflow
- Groundwater
- Water Quality
- Hydrology
- Environmental
- USGS
- NWIS
- Government
- Open Data
- OGC
website: https://waterservices.usgs.gov/
---
