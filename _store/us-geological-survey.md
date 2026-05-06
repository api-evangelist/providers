---
aid: us-geological-survey
url: https://raw.githubusercontent.com/api-evangelist/us-geological-survey/refs/heads/main/apis.yml
apis:
  - aid: us-geological-survey:earthquake-catalog-api
    name: USGS Earthquake Catalog API
    tags:
      - Earthquakes
      - Seismology
      - Hazards
      - Federal Government
    humanURL: https://earthquake.usgs.gov/fdsnws/event/1/
    properties:
      - url: https://earthquake.usgs.gov/fdsnws/event/1/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-geological-survey/refs/heads/main/openapi/usgs-earthquake-catalog-openapi.yml
        type: OpenAPI
    description: The USGS Earthquake Catalog API implements the FDSN Event Web Service Specification, providing real-time and historical access to global earthquake data from the USGS National Earthquake Information Center. Query by time, location, magnitude, depth, and other parameters. Returns data in GeoJSON, QuakeML, KML, CSV, or text formats. No authentication required.
  - aid: us-geological-survey:water-data-api
    name: USGS Water Data OGC API
    tags:
      - Water Data
      - Hydrology
      - Streamflow
      - Federal Government
    humanURL: https://api.waterdata.usgs.gov
    properties:
      - url: https://api.waterdata.usgs.gov
        type: Documentation
      - url: https://api.waterdata.usgs.gov/ogcapi/v0/openapi?f=json
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/us-geological-survey/refs/heads/main/openapi/usgs-water-data-openapi.yml
        type: OpenAPI
    description: The USGS Water Data OGC APIs provide OGC-compliant interfaces to USGS water data including real-time continuous measurements from automated sensor networks, daily summary values, field measurements, and monitoring location metadata. Covers streamflow, gage height, groundwater levels, water quality, and hundreds of other parameters. API key required. Legacy WaterServices decommissioning in Q1 2027.
  - aid: us-geological-survey:sciencebase-api
    name: USGS ScienceBase Catalog API
    tags:
      - Scientific Data
      - Research
      - Catalog
      - Federal Government
    humanURL: https://www.sciencebase.gov/catalog/
    properties:
      - url: https://www.sciencebase.gov/catalog/
        type: Documentation
      - url: https://www.sciencebase.gov/catalog/swagger-ui.html
        type: SwaggerUI
    description: The USGS ScienceBase Catalog API provides access to USGS scientific data management infrastructure, enabling upload, documentation, sharing, and dynamic data services for USGS research datasets and scientific publications.
  - aid: us-geological-survey:geomagnetism-api
    name: USGS Geomagnetism Web Service
    tags:
      - Geomagnetism
      - Magnetic Data
      - Federal Government
    humanURL: https://www.usgs.gov/tools/web-service-geomagnetism-data
    properties:
      - url: https://www.usgs.gov/tools/web-service-geomagnetism-data
        type: Documentation
      - url: https://geomag.usgs.gov/ws/edge/
        type: BaseURL
    description: The USGS Geomagnetism Web Service provides programmatic access to geomagnetic data collected by USGS magnetic observatories across the United States and territories, supporting navigation, space weather, and geophysical research.
  - aid: us-geological-survey:seismic-design-api
    name: USGS Seismic Design Data Web Services
    tags:
      - Seismic Design
      - Engineering
      - Hazards
      - Federal Government
    humanURL: https://earthquake.usgs.gov/ws/designmaps/
    properties:
      - url: https://earthquake.usgs.gov/ws/designmaps/
        type: Documentation
    description: The USGS Seismic Design Data Web Services provide parameter values from seismic design reference documents for building and infrastructure design, supporting compliance with ASCE 7 and other engineering standards.
  - aid: us-geological-survey:national-map-api
    name: USGS National Map Services
    tags:
      - Mapping
      - Geospatial
      - Topography
      - Federal Government
    humanURL: https://apps.nationalmap.gov/api/
    properties:
      - url: https://apps.nationalmap.gov/api/
        type: Documentation
    description: The USGS National Map services provide geospatial data and elevation products via OGC web services, REST APIs, and download services covering topographic data, imagery, hydrography, boundaries, transportation, structures, and land cover for the United States.
name: US Geological Survey
tags:
  - Federal Government
  - Earth Science
  - Earthquakes
  - Water Data
  - Geospatial
  - Hazards
  - Environment
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The US Geological Survey is a scientific agency of the United States government that conducts research on the natural resources, natural hazards, and environmental health of the United States. The USGS is responsible for monitoring and assessing the country's water, energy, mineral, and biological resources, as well as investigating geological hazards such as earthquakes, volcanoes, landslides, and floods. USGS provides a broad portfolio of public REST APIs covering earthquake data, water resources, geomagnetism, mapping, seismic design, and scientific data catalogs - all available without cost as US Government works.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
