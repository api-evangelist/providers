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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: U S Geological Survey Agentic Access
  operation_count: 11
  slug: u-s-geological-survey-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: The USGS Water Data OGC API — an OGC API Features service declaring 18 conformance classes, including OGC API Common Parts 1-3, Features Parts 1-4 and CQL2 filtering, and serving 37 collections. Verif
  name: USGS Water Data APIs
  slug: water-data-ogc-api
- description: The USGS Asset Identifier Service (AIS) allows USGS personnel to reserve, register, publish, and manage USGS persistent identifiers to make research more Findable, Accessible, Interoperable, and Reusa
  name: Asset Identifier Service (AIS)
  slug: asset-identifier-service-ais
- description: Web services produced by the U.S. Geological Survey for calculating parameter values from various seismic design reference documents for engineering and construction purposes.
  name: Seismic Design Web Service
  slug: seismic-design-web-service
- description: ScienceBase is a USGS Trusted Digital Repository that provides permission-controlled and public access to scientific data products through a REST API supporting upload, documentation, and sharing of r
  name: ScienceBase
  slug: sciencebase
- description: The StreamStats Web Services provide HTTP-accessible hydrological analysis services for delineating drainage areas, estimating peak flows, and computing basin characteristics for water resources plann
  name: StreamStats Web Services
  slug: streamstats-web-services
- description: The original USGS NWIS water services API providing streamflow, groundwater, water quality, and site information via REST protocol in XML and other media types. High availability and fault-tolerant de
  name: USGS Water Services (Legacy)
  slug: usgs-water-services
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Discover available catalogs, contributors, and supported parameter values.
  name: U.S. Geological Survey Catalog API
  slug: u-s-geological-survey-catalog-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Query and retrieve earthquake event data from the USGS earthquake catalog.
  name: U.S. Geological Survey Earthquakes API
  slug: u-s-geological-survey-earthquakes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: USGS stream gages, groundwater wells, and other water monitoring stations.
  name: U.S. Geological Survey Monitoring Locations API
  slug: u-s-geological-survey-monitoring-locations-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Reference code tables including agency codes, datum types, and aquifer data.
  name: U.S. Geological Survey Reference Data API
  slug: u-s-geological-survey-reference-data-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Continuous and daily value water data from USGS monitoring locations.
  name: U.S. Geological Survey Time Series Data API
  slug: u-s-geological-survey-time-series-data-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Code identifying the agency or organization used for site information, data sources, and permitting agencies. Agency codes are fixed values assigned by the National Water Information System (NWIS).
  name: U.S. Geological Survey Agency Codes API
  slug: u-s-geological-survey-agency-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: The recommended vertical datum is NAVD88 (North American Vertical Datum of 1988) where applicable as stated in Office of Information Technical Memo 2002.01. NGVD29 (National Geodetic Vertical Datum of
  name: U.S. Geological Survey Altitude Datums API
  slug: u-s-geological-survey-altitude-datums-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Local aquifers in USGS data are identified by an aquifer name and geohydrologic unit code (a three-digit number related to the age of the formation, followed by a 4 or 5 character abbreviation for the
  name: U.S. Geological Survey Aquifer Codes API
  slug: u-s-geological-survey-aquifer-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Groundwater occurs in aquifers under two different conditions. Where water only partly fills an aquifer, the upper surface is free to rise and decline. These aquifers are referred to as unconfined (or
  name: U.S. Geological Survey Aquifer Types API
  slug: u-s-geological-survey-aquifer-types-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Channel measurements taken as part of streamflow field measurements.
  name: U.S. Geological Survey Channel Measurements API
  slug: u-s-geological-survey-channel-measurements-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Citations associated with water measurement methods.
  name: U.S. Geological Survey Citations API
  slug: u-s-geological-survey-citations-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: This endpoint combines metadata from timeseries and field measurements collections by site.
  name: U.S. Geological Survey Combined Metadata API
  slug: u-s-geological-survey-combined-metadata-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Continuous data are collected via automated sensors installed at a monitoring location. They are collected at a high frequency and often at a fixed 15-minute interval. Depending on the specific monito
  name: U.S. Geological Survey Continuous API
  slug: u-s-geological-survey-continuous-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Appropriate code on the schedule to indicate the accuracy of the latitude-longitude values.
  name: U.S. Geological Survey Coordinate Accuracy Codes API
  slug: u-s-geological-survey-coordinate-accuracy-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Horizontal datum code for the latitude/longitude coordinates. There are currently more than 300 horizontal datums available for entry.
  name: U.S. Geological Survey Coordinate Datum Codes API
  slug: u-s-geological-survey-coordinate-datum-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Methods used to determine latitude-longitude values.
  name: U.S. Geological Survey Coordinate Method Codes API
  slug: u-s-geological-survey-coordinate-method-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: The name of the county or county equivalent (parish, borough, planning reagion, etc.) in which the site is located. List includes Census Bureau FIPS county codes, names and associated Country and Stat
  name: U.S. Geological Survey Counties API
  slug: u-s-geological-survey-counties-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: FIPS country codes and names.
  name: U.S. Geological Survey Countries API
  slug: u-s-geological-survey-countries-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Daily data provide one data value to represent water conditions for the day. Throughout much of the history of the USGS, the primary water data available was daily data collected manually at the monit
  name: U.S. Geological Survey Daily API
  slug: u-s-geological-survey-daily-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Field measurements are physically measured values collected during a visit to the monitoring location. Field measurements consist of measurements of gage height and discharge, and readings of groundwa
  name: U.S. Geological Survey Field Measurements API
  slug: u-s-geological-survey-field-measurements-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: This endpoint provides metadata about field measurement collections, including when the earliest and most recent observations for a parameter occurred at a monitoring location and its units.
  name: U.S. Geological Survey Field Measurements Metadata API
  slug: u-s-geological-survey-field-measurements-metadata-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: 'Hydrologic units are geographic areas representing part or all of a surface drainage basin or distinct hydrologic feature identified by a unique number (HUC), and a name. The United States is divided '
  name: U.S. Geological Survey Hydrologic Unit Codes API
  slug: u-s-geological-survey-hydrologic-unit-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: This endpoint provides the most recent observation for each time series of continuous data. Continuous data are collected via automated sensors installed at a monitoring location. They are collected a
  name: U.S. Geological Survey Latest Continuous API
  slug: u-s-geological-survey-latest-continuous-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Daily data provide one data value to represent water conditions for the day. Throughout much of the history of the USGS, the primary water data available was daily data collected manually at the monit
  name: U.S. Geological Survey Latest Daily API
  slug: u-s-geological-survey-latest-daily-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Field measurements are physically measured values collected during a visit to the monitoring location. Field measurements consist of measurements of gage height and discharge, and readings of groundwa
  name: U.S. Geological Survey Latest Field Measurements API
  slug: u-s-geological-survey-latest-field-measurements-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Medium refers to the specific environmental medium from which the sample was collected. Medium type differs from site type because one site type, such as surface water, could have data for several med
  name: U.S. Geological Survey Medium Codes API
  slug: u-s-geological-survey-medium-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Categorical standards for methods describing the associated data's appropriateness for an intended use.
  name: U.S. Geological Survey Method Categories API
  slug: u-s-geological-survey-method-categories-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Citation identifiers for water measurement methods.
  name: U.S. Geological Survey Method Citations API
  slug: u-s-geological-survey-method-citations-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Water measurement or water-quality analytical methods. Codes and descriptions defining a method for calculating or measuring the value of a water quality or quantity parameter. Method codes are associ
  name: U.S. Geological Survey Methods API
  slug: u-s-geological-survey-methods-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: National aquifers are the principal aquifers or aquifer systems in the United States, defined as regionally extensive aquifers or aquifer systems that have the potential to be used as a source of pota
  name: U.S. Geological Survey National Aquifer Codes API
  slug: u-s-geological-survey-national-aquifer-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Parameter codes are 5-digit codes and associated descriptions used to identify the constituent measured and the units of measure. Some parameter code definitions include information about the sampling
  name: U.S. Geological Survey Parameter Codes API
  slug: u-s-geological-survey-parameter-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Annual peak flow values are the maximum instantaneous streamflow values recorded at a particular site for the entire water year from October 1 to September 30. Note that the annual peak flow value may
  name: U.S. Geological Survey Peaks API
  slug: u-s-geological-survey-peaks-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Code indicating the reliability of the data available for the site.
  name: U.S. Geological Survey Reliability Codes API
  slug: u-s-geological-survey-reliability-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: The United States Geological Survey (USGS) collects water data at monitoring locations across the United States using both automated sensors and manual data collection. These APIs provide access to th
  name: U.S. Geological Survey Server API
  slug: u-s-geological-survey-server-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: The hydrologic cycle setting or a man-made feature thought to affect the hydrologic conditions measured at a site. Primary and secondary site types associated with data collection sites. All sites hav
  name: U.S. Geological Survey Site Types API
  slug: u-s-geological-survey-site-types-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: State name or territory. Includes U.S. states and foreign entities classified under FIPS as 'Principal Administrative Divisions'.
  name: U.S. Geological Survey States API
  slug: u-s-geological-survey-states-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Statistic codes.
  name: U.S. Geological Survey Statistic Codes API
  slug: u-s-geological-survey-statistic-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: 'Daily data and continuous measurements are grouped into time series, which represent a collection of observations of a single parameter, potentially aggregated using a standard statistic, at a single '
  name: U.S. Geological Survey Time Series Metadata API
  slug: u-s-geological-survey-time-series-metadata-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: Approved water data are considered published record, but on occasion changes or deletions (revisions) must be made to data after they are approved. Data revisions are rare because of USGS quality assu
  name: U.S. Geological Survey Time Series Revisions API
  slug: u-s-geological-survey-time-series-revisions-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: The ISO 8601 standard defines time zone offsets as a numerical value added to a local time to convert it to Coordinated Universal Time (UTC), either as +hh:mm or -hh:mm, or represented by the letter Z
  name: U.S. Geological Survey Time Zone Codes API
  slug: u-s-geological-survey-time-zone-codes-api
- baseURL: https://earthquake.usgs.gov/fdsnws/event/1
  baseurl_source: declared
  description: The code that best describes the topographic setting in which the site is located. Topographic setting refers to the geomorphic features in the vicinity of the site.
  name: U.S. Geological Survey Topographic Codes API
  slug: u-s-geological-survey-topographic-codes-api
artifact_total: 135
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USGS Earthquake Notifications, Feeds, and Web Services Catalog API
  slug: open-u-s-geological-survey-catalog-api
- collection_type: open
  name: USGS Earthquake Notifications, Feeds, and Web Services Catalog Collections API
  slug: open-u-s-geological-survey-collections-api
- collection_type: open
  name: USGS Earthquake Notifications, Feeds, and Web Services Catalog Earthquakes API
  slug: open-u-s-geological-survey-earthquakes-api
- collection_type: open
  name: USGS Earthquake Notifications, Feeds, and Web Services Catalog Monitoring Locations API
  slug: open-u-s-geological-survey-monitoring-locations-api
- collection_type: open
  name: USGS Earthquake Notifications, Feeds, and Web Services Catalog Reference Data API
  slug: open-u-s-geological-survey-reference-data-api
- collection_type: open
  name: USGS Earthquake Notifications, Feeds, and Web Services Catalog Time Series Data API
  slug: open-u-s-geological-survey-time-series-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/u-s-geological-survey-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/u-s-geological-survey-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/u-s-geological-survey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/u-s-geological-survey-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usgs
- group: company
  title: ''
  type: Website
  url: https://www.usgs.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usgs
- group: docs
  title: ''
  type: Documentation
  url: https://www.usgs.gov/products/web-tools/apis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/rules/usgs-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/vocabulary/u-s-geological-survey-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.usgs.gov/news/news-releases/all-news-releases
created: '2024-11-14'
description: The U.S. Geological Survey (USGS) is a scientific agency of the U.S. government that conducts research and provides data on the natural resources and hazards of the United States. The USGS is known for its work in mapping and monitoring earthquakes, volcanoes, and landslides to help mitigate risks and protect communities. USGS also studies water resources including streamflow, groundwater, and water quality through a nationwide network of monitoring stations. Their public APIs provide programmatic access to real-time earthquake data, water monitoring observations, seismic design parameters, and geospatial data products.
examples:
- key_count: 2
  name: Usgs Earthquake Api Count Response Example
  slug: usgs-earthquake-api-count-response-example
- key_count: 4
  name: Usgs Earthquake Api Earthquake Feature Collection Example
  slug: usgs-earthquake-api-earthquake-feature-collection-example
- key_count: 4
  name: Usgs Earthquake Api Earthquake Feature Example
  slug: usgs-earthquake-api-earthquake-feature-example
- key_count: 2
  name: Usgs Earthquake Api Earthquake Geometry Example
  slug: usgs-earthquake-api-earthquake-geometry-example
- key_count: 8
  name: Usgs Earthquake Api Earthquake Metadata Example
  slug: usgs-earthquake-api-earthquake-metadata-example
- key_count: 22
  name: Usgs Earthquake Api Earthquake Properties Example
  slug: usgs-earthquake-api-earthquake-properties-example
- key_count: 4
  name: Usgs Water Data Api Collection Example
  slug: usgs-water-data-api-collection-example
- key_count: 1
  name: Usgs Water Data Api Collections List Example
  slug: usgs-water-data-api-collections-list-example
- key_count: 2
  name: Usgs Water Data Api Error Response Example
  slug: usgs-water-data-api-error-response-example
- key_count: 4
  name: Usgs Water Data Api Feature Collection Example
  slug: usgs-water-data-api-feature-collection-example
- key_count: 3
  name: Usgs Water Data Api Landing Page Example
  slug: usgs-water-data-api-landing-page-example
- key_count: 4
  name: Usgs Water Data Api Link Example
  slug: usgs-water-data-api-link-example
- key_count: 4
  name: Usgs Water Data Api Monitoring Location Collection Example
  slug: usgs-water-data-api-monitoring-location-collection-example
- key_count: 3
  name: Usgs Water Data Api Monitoring Location Feature Example
  slug: usgs-water-data-api-monitoring-location-feature-example
- key_count: 9
  name: Usgs Water Data Api Monitoring Location Properties Example
  slug: usgs-water-data-api-monitoring-location-properties-example
- key_count: 4
  name: Usgs Water Data Api Time Series Collection Example
  slug: usgs-water-data-api-time-series-collection-example
- key_count: 2
  name: Usgs Water Data Api Time Series Feature Example
  slug: usgs-water-data-api-time-series-feature-example
- key_count: 7
  name: Usgs Water Data Api Time Series Properties Example
  slug: usgs-water-data-api-time-series-properties-example
features:
- description: Search the USGS ANSS ComCat earthquake catalog by geography, time, magnitude, depth, and event type with 20,000 event limit per query.
  name: Earthquake Catalog Query
- description: Access near real-time earthquake data updated within minutes of events occurring anywhere in the world.
  name: Real-Time Earthquake Data
- description: Query USGS stream gages, groundwater wells, and other water quality monitoring stations by state, watershed, or geographic area.
  name: Water Monitoring Locations
- description: Retrieve continuous and daily water data including streamflow, stage, temperature, and water quality parameters.
  name: Water Data Time Series
- description: USGS Water Data APIs implement OGC API Features standard supporting CQL2 filtering, spatial queries, and standardized output formats.
  name: OGC API Compliance
- description: All spatial data returned in GeoJSON format compatible with mapping libraries and geospatial analysis tools.
  name: GeoJSON Output
finops:
- name: U S Geological Survey Finops
  service_category: Public Open Data
  slug: u-s-geological-survey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/u-s-geological-survey.png
integrations:
- description: Open-source tools including libcomcat, rcomcat, and other clients for accessing USGS earthquake and water data.
  name: USGS GitHub Organization
- description: The flagship USGS water data portal at waterdata.usgs.gov providing maps and tools built on the NWIS water services API.
  name: USGS Water Data for the Nation
- description: Legacy USGS water data system providing the underlying data for Water Data APIs with millions of site records.
  name: National Water Information System (NWIS)
- description: USGS earthquake API implements FDSN (International Federation of Digital Seismograph Networks) web service specifications.
  name: FDSN Standards
json_schemas:
- name: CountResponse
  property_count: 2
  slug: usgs-earthquake-api-count-response
- name: EarthquakeFeatureCollection
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature-collection
- name: EarthquakeFeature
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature
- name: EarthquakeGeometry
  property_count: 2
  slug: usgs-earthquake-api-earthquake-geometry
- name: EarthquakeMetadata
  property_count: 8
  slug: usgs-earthquake-api-earthquake-metadata
- name: EarthquakeProperties
  property_count: 22
  slug: usgs-earthquake-api-earthquake-properties
- name: Collection
  property_count: 4
  slug: usgs-water-data-api-collection
- name: CollectionsList
  property_count: 1
  slug: usgs-water-data-api-collections-list
- name: ErrorResponse
  property_count: 2
  slug: usgs-water-data-api-error-response
- name: FeatureCollection
  property_count: 4
  slug: usgs-water-data-api-feature-collection
- name: LandingPage
  property_count: 3
  slug: usgs-water-data-api-landing-page
- name: Link
  property_count: 4
  slug: usgs-water-data-api-link
- name: MonitoringLocationCollection
  property_count: 4
  slug: usgs-water-data-api-monitoring-location-collection
- name: MonitoringLocationFeature
  property_count: 3
  slug: usgs-water-data-api-monitoring-location-feature
- name: MonitoringLocationProperties
  property_count: 9
  slug: usgs-water-data-api-monitoring-location-properties
- name: TimeSeriesCollection
  property_count: 4
  slug: usgs-water-data-api-time-series-collection
- name: TimeSeriesFeature
  property_count: 2
  slug: usgs-water-data-api-time-series-feature
- name: TimeSeriesProperties
  property_count: 7
  slug: usgs-water-data-api-time-series-properties
json_structures:
- name: Usgs Earthquake Api Count Response Structure
  property_count: 2
  slug: usgs-earthquake-api-count-response-structure
- name: Usgs Earthquake Api Earthquake Feature Collection Structure
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature-collection-structure
- name: Usgs Earthquake Api Earthquake Feature Structure
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature-structure
- name: Usgs Earthquake Api Earthquake Geometry Structure
  property_count: 2
  slug: usgs-earthquake-api-earthquake-geometry-structure
- name: Usgs Earthquake Api Earthquake Metadata Structure
  property_count: 8
  slug: usgs-earthquake-api-earthquake-metadata-structure
- name: Usgs Earthquake Api Earthquake Properties Structure
  property_count: 22
  slug: usgs-earthquake-api-earthquake-properties-structure
- name: Usgs Water Data Api Collection Structure
  property_count: 4
  slug: usgs-water-data-api-collection-structure
- name: Usgs Water Data Api Collections List Structure
  property_count: 1
  slug: usgs-water-data-api-collections-list-structure
- name: Usgs Water Data Api Error Response Structure
  property_count: 2
  slug: usgs-water-data-api-error-response-structure
- name: Usgs Water Data Api Feature Collection Structure
  property_count: 4
  slug: usgs-water-data-api-feature-collection-structure
- name: Usgs Water Data Api Landing Page Structure
  property_count: 3
  slug: usgs-water-data-api-landing-page-structure
- name: Usgs Water Data Api Link Structure
  property_count: 4
  slug: usgs-water-data-api-link-structure
- name: Usgs Water Data Api Monitoring Location Collection Structure
  property_count: 4
  slug: usgs-water-data-api-monitoring-location-collection-structure
- name: Usgs Water Data Api Monitoring Location Feature Structure
  property_count: 3
  slug: usgs-water-data-api-monitoring-location-feature-structure
- name: Usgs Water Data Api Monitoring Location Properties Structure
  property_count: 9
  slug: usgs-water-data-api-monitoring-location-properties-structure
- name: Usgs Water Data Api Time Series Collection Structure
  property_count: 4
  slug: usgs-water-data-api-time-series-collection-structure
- name: Usgs Water Data Api Time Series Feature Structure
  property_count: 2
  slug: usgs-water-data-api-time-series-feature-structure
- name: Usgs Water Data Api Time Series Properties Structure
  property_count: 7
  slug: usgs-water-data-api-time-series-properties-structure
jsonld:
- class_count: 6
  name: Usgs Earthquake Api Context
  property_count: 35
  slug: usgs-earthquake-api-context
- class_count: 12
  name: Usgs Water Data Api Context
  property_count: 30
  slug: usgs-water-data-api-context
layout: provider
modified: '2026-05-19'
name: U.S. Geological Survey
nav: Providers
network: true
overview: 'U.S. Geological Survey publishes 42 APIs on the [APIs.io](https://apis.io/) network, including USGS Water Data APIs, Catalog API, Earthquakes API, and 39 more. Tagged areas include Federal-Government, Geological, Earth Science, Natural Resources, and Earthquake.


  The U.S. Geological Survey catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  U.S. Geological Survey''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: U S Geological Survey Plans Pricing
  plan_count: 1
  slug: u-s-geological-survey-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: U S Geological Survey Rate Limits
  slug: u-s-geological-survey-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: U.S. Geological Survey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: u-s-geological-survey-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: U.S. Geological Survey API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: u-s-geological-survey-spectral-rules
- effective_rule_count: 33
  extends: []
  name: U.S. Geological Survey API Rules
  rule_count: 33
  severity_counts:
    error: 9
    hint: 0
    info: 10
    warn: 14
  slug: usgs-spectral-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 47.0
    contract_quality: 68.2
    developer_ergonomics: 35.7
    discoverability: 53.7
    governance: 47.0
    operational_transparency: 7.9
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 14.0
      total: 43
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/screenshots/u-s-geological-survey-2026-06-20T195914.png
security:
- kind: authentication
  name: U S Geological Survey Authentication
  slug: u-s-geological-survey-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: U S Geological Survey Domain Security
  slug: u-s-geological-survey-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: U S Geological Survey Vulnerability Disclosure
  slug: u-s-geological-survey-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: u-s-geological-survey
tags:
- Federal-Government
- Geological
- Earth Science
- Natural Resources
- Earthquake
- Water
- Hydrology
use_cases:
- description: Emergency managers and scientists monitor real-time earthquake activity for hazard assessment and emergency response planning.
  name: Earthquake Hazard Monitoring
- description: Hydrologists use USGS streamflow data for flood prediction, water supply forecasting, and reservoir management.
  name: Flood Forecasting
- description: Water managers track groundwater level trends for sustainable aquifer management and drought assessment.
  name: Groundwater Management
- description: Researchers use USGS geological and water data for environmental impact assessments and climate change studies.
  name: Environmental Research
- description: Civil engineers use USGS water data and seismic design services for infrastructure planning and construction.
  name: Engineering Design
website: https://www.usgs.gov/
---
