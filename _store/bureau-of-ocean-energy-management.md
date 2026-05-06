---
aid: bureau-of-ocean-energy-management
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-ocean-energy-management/refs/heads/main/apis.yml
name: Bureau of Ocean Energy Management
tags:
  - Energy
  - Federal Government
  - Marine
  - Oceans
  - GIS
  - Offshore
  - Environmental
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-23'
position: Consumer
description: The Bureau of Ocean Energy Management (BOEM) manages the nation's offshore resources in an environmentally and economically responsible way. BOEM oversees the responsible development of U.S. Outer Continental Shelf energy and mineral resources while protecting the environment and conserving natural resources.
apis:
  - aid: bureau-of-ocean-energy-management:marine-cadastre
    name: MarineCadastre.gov
    tags:
      - Federal Government
      - Marine
      - GIS
      - Oceans
    humanURL: https://marinecadastre.gov/
    baseURL: https://hub.marinecadastre.gov/
    properties:
      - url: https://hub.marinecadastre.gov/
        type: Portal
      - url: https://marinecadastre.gov/oceanreports
        type: Tool
    description: MarineCadastre.gov is the authoritative source for marine cadastre data and services. It provides an interactive map viewer with integrated submerged lands information including legal, property ownership (cadastre), physical, biological, ocean uses, and cultural information. Includes Web Map Services (WMS) for GIS integration and downloadable data layers.
    features:
      - Web Map Services (WMS)
      - Interactive Map Viewer
      - OceanReports Analysis Tool
      - AIS Vessel Traffic Data
      - Downloadable Geospatial Layers
      - Legal and Cadastral Data
    useCases:
      - Offshore energy project planning
      - Marine spatial planning
      - Environmental impact assessment
      - Coastal and ocean use analysis
  - aid: bureau-of-ocean-energy-management:boem-arcgis-rest-services
    name: BOEM ArcGIS REST Services
    tags:
      - Federal Government
      - GIS
      - Oceans
      - Offshore
    humanURL: https://www.boem.gov/oil-gas-energy/mapping-and-data
    baseURL: https://gis.boem.gov/arcgis/rest/services/
    properties:
      - url: https://www.boem.gov/oil-gas-energy/mapping-and-data
        type: Documentation
      - url: https://catalog.data.gov/dataset?organization=boem-gov
        type: DataAPI
    description: BOEM provides ArcGIS REST Services exposing geospatial data for the Outer Continental Shelf (OCS) regions. Data includes active leases, offshore block grids, boundaries, wells, and pipelines for Atlantic, Gulf of Mexico, Pacific, and Alaska regions.
    features:
      - Active Lease Boundaries
      - Offshore Block Grids
      - Pipeline Data
      - Well Locations
      - OCS Planning Areas
      - Regional Shapefiles
    useCases:
      - Offshore drilling planning
      - Lease management
      - Environmental review
      - Marine infrastructure mapping
  - aid: bureau-of-ocean-energy-management:espis
    name: Environmental Studies Program Information System (ESPIS)
    tags:
      - Federal Government
      - Environmental
      - Marine
    humanURL: https://esp-boem.hub.arcgis.com/
    properties:
      - url: https://esp-boem.hub.arcgis.com/
        type: Portal
    description: ESPIS provides access to BOEM's environmental studies data, including research reports, environmental impact studies, and scientific literature related to offshore energy development. Searchable by topic, location, and year.
    features:
      - Environmental Studies Database
      - Research Reports
      - Scientific Literature
      - Geographic Search
    useCases:
      - Environmental impact research
      - Offshore energy regulation compliance
      - Academic marine research
      - Policy development
common:
  - type: Website
    url: https://www.boem.gov
  - type: Portal
    url: https://marinecadastre.gov/
  - type: Privacy Policy
    url: https://www.boem.gov/privacy-policy
  - type: Mapping and Data
    url: https://www.boem.gov/oil-gas-energy/mapping-and-data
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=boem-gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
