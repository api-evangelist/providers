---
aid: bureau-of-land-management
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-land-management/refs/heads/main/apis.yml
name: Bureau of Land Management
tags:
  - Environment
  - Federal Government
  - Land
  - Resources
  - GIS
  - Geospatial
  - Mining
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-23'
position: Consumer
description: The Bureau of Land Management (BLM) is a U.S. government agency responsible for managing vast stretches of public lands across the country, primarily focused on activities like outdoor recreation, livestock grazing, mineral development, and energy production, aiming to sustain the health and diversity of these lands for future generations.
apis:
  - aid: bureau-of-land-management:blm-geospatial-business-platform
    name: BLM Geospatial Business Platform (GBP) Hub
    tags:
      - Federal Government
      - Geospatial
      - GIS
      - Land
    humanURL: https://gbp-blm-egis.hub.arcgis.com/
    baseURL: https://blm-egis.maps.arcgis.com/sharing/rest/
    properties:
      - url: https://gbp-blm-egis.hub.arcgis.com/
        type: Portal
      - url: https://blm-egis.maps.arcgis.com/home/index.html
        type: Documentation
      - url: https://catalog.data.gov/dataset?organization=blm-gov
        type: DataAPI
    description: The BLM Geospatial Business Platform is a public tool and publication platform for exploring and downloading GIS data. Built on ArcGIS Online, it provides REST endpoints for BLM geospatial data including public lands boundaries, mineral resources, recreation areas, and environmental data.
    features:
      - ArcGIS REST Endpoints
      - ISO-19139 XML Metadata
      - DCAT-US Compliance
      - Keyword and Location Search
      - Public Land Records
    useCases:
      - Public lands research
      - Recreation planning
      - Environmental impact assessment
      - Mineral rights research
  - aid: bureau-of-land-management:blm-mineral-land-records
    name: BLM Mineral and Land Records System (MLRS)
    tags:
      - Federal Government
      - Land
      - Mining
      - Minerals
    humanURL: https://mlrs.blm.gov/s/
    properties:
      - url: https://mlrs.blm.gov/s/
        type: Portal
    description: The Mineral and Land Records System (MLRS) is an online platform delivering state-of-the-art mineral and land records transactions, tracking, mapping, and more for BLM customers and staff. It manages land patents, rights-of-way, mining claims, and related records.
    features:
      - Mineral Records
      - Land Patent Records
      - Rights-of-Way Management
      - Mining Claims
    useCases:
      - Mineral rights research
      - Land patent lookup
      - Rights-of-way applications
      - Mining claim verification
  - aid: bureau-of-land-management:blm-general-land-office-records
    name: BLM General Land Office Records
    tags:
      - Federal Government
      - Land
      - Historical Records
    humanURL: https://glorecords.blm.gov/default.aspx
    properties:
      - url: https://glorecords.blm.gov/default.aspx
        type: Portal
    description: The General Land Office (GLO) Records provide access to federal land conveyance records including land patents, survey plats, and field notes from 1788 to the present. The system contains over 10 million Federal land title records.
    features:
      - Land Patent Records
      - Survey Plats
      - Field Notes
      - Historical Records Search
    useCases:
      - Historical land research
      - Genealogy research
      - Property title research
      - Academic historical study
  - aid: bureau-of-land-management:blm-eplanning
    name: BLM ePlanning
    tags:
      - Federal Government
      - Land Use Planning
      - Environmental
    humanURL: https://eplanning.blm.gov/
    properties:
      - url: https://eplanning.blm.gov/
        type: Portal
    description: BLM ePlanning provides public access to land use planning documents, environmental impact statements, and resource management plans. Citizens can track planning projects and participate in comment periods.
    features:
      - Land Use Planning Documents
      - Environmental Impact Statements
      - Resource Management Plans
      - Public Comment Access
    useCases:
      - Environmental review tracking
      - Public comment participation
      - Land use planning research
      - Policy development support
common:
  - type: Website
    url: https://www.blm.gov
  - type: Portal
    url: https://gbp-blm-egis.hub.arcgis.com/
  - type: Privacy Policy
    url: https://www.blm.gov/privacy-policy
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=blm-gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
