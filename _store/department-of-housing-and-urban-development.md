---
aid: department-of-housing-and-urban-development
name: Department of Housing and Urban Development
description: The U.S. Department of Housing and Urban Development (HUD) is the federal agency responsible for overseeing programs that address the country's housing needs and promote sustainable urban development. HUD exposes programmatic data through the HUD USER FMR/IL API for Fair Market Rents and Income Limits, the HUD eGIS storefront and ArcGIS REST services for geospatial assets, the data.hud.gov data catalog, and various FHA tools including mortgage limits and condominium lookup services.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Affordable Housing
  - Fair Market Rents
  - Federal Government
  - FHA
  - GIS
  - Housing
  - HUD
  - Income Limits
  - Mortgage
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/department-of-housing-and-urban-development/refs/heads/main/apis.yml
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
position: Producer
access: Public
apis:
  - aid: department-of-housing-and-urban-development:hud-user-fmr-il-api
    name: HUD USER FMR/IL API
    description: The HUD USER FMR/IL API publishes Fair Market Rents (FMRs), Small Area Fair Market Rents, and Income Limits (IL) for U.S. metropolitan and non-metropolitan areas. It exposes endpoints for listing states, metros, and counties as well as retrieving annual FMR and IL values for specified geographies and fiscal years. Access requires a free token obtained from the HUD USER portal.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.huduser.gov/portal/dataset/fmr-api.html
    baseURL: https://www.huduser.gov/hudapi/public
    tags:
      - Fair Market Rents
      - Housing
      - HUD USER
      - Income Limits
      - PD&R
    properties:
      - type: Documentation
        url: https://www.huduser.gov/portal/dataset/fmr-api.html
      - type: Datasets
        url: https://www.huduser.gov/portal/pdrdatas_landing.html
      - type: FMR Data
        url: https://www.huduser.gov/portal/datasets/fmr.html
      - type: Income Limits
        url: https://www.huduser.gov/portal/datasets/il.html
      - type: Sign Up
        url: https://www.huduser.gov/hudapi/public/register
    contact:
      - FN: HUD USER
        email: helpdesk@huduser.gov
        url: https://www.huduser.gov/portal/home.html
  - aid: department-of-housing-and-urban-development:hud-egis-arcgis
    name: HUD eGIS ArcGIS REST Services
    description: The HUD eGIS storefront publishes ArcGIS-based REST services and feature layers for the Department's geospatial assets, including Continuum of Care boundaries, CPD activities, public housing locations, low-income housing tax credit properties, and HUD-administered geographies. The services are accessible via the HUD-GIS open data portal as well as directly from egis.hud.gov.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://hudgis-hud.opendata.arcgis.com/
    baseURL: https://egis.hud.gov/ArcGIS/rest/services
    tags:
      - ArcGIS
      - eGIS
      - Geospatial
      - GIS
      - HUD
    properties:
      - type: Open Data Portal
        url: https://hudgis-hud.opendata.arcgis.com/
      - type: ArcGIS Services
        url: https://egis.hud.gov/ArcGIS/rest/services
      - type: HUD CPD Activities Service
        url: https://egis.hud.gov/ArcGIS/rest/services/cpdmaps/HudCpdActivities/MapServer
      - type: GIS Tools
        url: https://www.hudexchange.info/programs/coc/gis-tools/
    contact:
      - FN: HUD GIS
        email: gis_helpdesk@hud.gov
        url: https://hudgis-hud.opendata.arcgis.com/
  - aid: department-of-housing-and-urban-development:fha-mortgage-limits
    name: FHA Mortgage Limits
    description: The FHA Mortgage Limits service lets users look up the FHA or Government-Sponsored Enterprise (GSE) mortgage limits for one or more areas, by state, county, or Metropolitan Statistical Area, with results that also include a Median Sale Price for each jurisdiction.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://entp.hud.gov/idapp/html/hicostlook.cfm
    baseURL: https://entp.hud.gov
    tags:
      - FHA
      - Lookup
      - Mortgage Limits
    properties:
      - type: Documentation
        url: https://entp.hud.gov/idapp/html/hicostlook.cfm
      - type: FHA Resources
        url: https://www.hud.gov/fha
    contact:
      - FN: HUD FHA
        url: https://www.hud.gov/contact_us
  - aid: department-of-housing-and-urban-development:hud-data-catalog
    name: HUD Open Data Catalog
    description: The HUD Open Data Catalog at data.hud.gov is curated by HUD's Office of the Chief Data Officer and lists the Department's open datasets across housing, community development, and fair housing. Datasets are cross-listed on Data.gov and accessible via Data.gov's CKAN-compatible API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://data.hud.gov/
    baseURL: https://catalog.data.gov/api/3
    tags:
      - CKAN
      - Datasets
      - Open Data
    properties:
      - type: Documentation
        url: https://data.hud.gov/open_data
      - type: Datasets
        url: https://data.hud.gov/datasets
      - type: Data.gov HUD Catalog
        url: https://catalog.data.gov/organization/hud-gov
      - type: CKAN Reference
        url: https://docs.ckan.org/en/2.8/api/
    contact:
      - FN: HUD Open Data
        email: OpenData@hud.gov
        url: https://data.hud.gov/
common:
  - type: Website
    url: https://www.hud.gov
  - type: Open Data
    url: https://data.hud.gov/
  - type: HUD USER
    url: https://www.huduser.gov/portal/home.html
  - type: HUD GIS
    url: https://hudgis-hud.opendata.arcgis.com/
  - type: FHA
    url: https://www.hud.gov/fha
  - type: HUD Exchange
    url: https://www.hudexchange.info/
  - type: News
    url: https://www.hud.gov/press
  - type: Contact
    url: https://www.hud.gov/contact_us
  - type: Privacy Policy
    url: https://www.hud.gov/notices/privacy_policy
  - type: Data.gov HUD Catalog
    url: https://catalog.data.gov/organization/hud-gov
  - type: GitHub Organization
    url: https://github.com/HUD-USER
  - type: JSON-LD
    url: json-ld/department-of-housing-and-urban-development-context.jsonld
  - type: Vocabulary
    url: vocabulary/department-of-housing-and-urban-development-vocabulary.yml
  - type: Capabilities
    url: capabilities/department-of-housing-and-urban-development-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
