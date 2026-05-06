---
aid: animal-and-plant-health-inspection-service
url: https://raw.githubusercontent.com/api-evangelist/animal-and-plant-health-inspection-service/refs/heads/main/apis.yml
apis:
  - aid: animal-and-plant-health-inspection-service:aphis-public-search-api
    name: APHIS Public Search Tool
    tags:
      - Agriculture
      - Animal Health
      - Federal Government
      - Permits
      - Plant Health
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://aphis.my.site.com/PublicSearchTool/s/
    humanURL: https://aphis.my.site.com/PublicSearchTool/s/
    properties:
      - url: https://aphis.my.site.com/PublicSearchTool/s/
        type: Portal
    description: The APHIS Public Search Tool provides public access to search APHIS program data, permits, and regulatory information related to animal and plant health programs.
  - aid: animal-and-plant-health-inspection-service:aphis-efile-api
    name: APHIS eFile Permitting System
    tags:
      - Agriculture
      - Animal Health
      - Federal Government
      - Import Export
      - Permits
      - Plant Health
      - Regulatory
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://efile.aphis.usda.gov
    humanURL: https://efile.aphis.usda.gov/s/
    properties:
      - url: https://efile.aphis.usda.gov/s/
        type: Portal
      - url: https://www.aphis.usda.gov/efile
        type: Documentation
    description: APHIS eFile is the web-based permitting system for submitting animal and plant health import/export permit applications, tracking application status, applying for renewals and amendments, and receiving permit copies online. Integrated with CBP's ACE system for automated permit verification at ports of entry. Requires USDA eAuthentication account.
  - aid: animal-and-plant-health-inspection-service:aphis-acir-api
    name: Agricultural Commodity Import Requirements (ACIR)
    tags:
      - Agriculture
      - Commodities
      - Federal Government
      - Import
      - Plant Health
      - Regulatory
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://acir.aphis.usda.gov
    humanURL: https://acir.aphis.usda.gov/s/
    properties:
      - url: https://acir.aphis.usda.gov/s/
        type: Portal
    description: The Agricultural Commodity Import Requirements (ACIR) system provides searchable access to APHIS import requirements for agricultural commodities, including plants, plant products, animals, and animal products by country of origin.
  - aid: animal-and-plant-health-inspection-service:aphis-geospatial-hub
    name: APHIS and AMS Geospatial Hub
    tags:
      - Agriculture
      - Animal Health
      - Federal Government
      - Geospatial
      - GIS
      - Mapping
      - Plant Health
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.aphis.usda.gov/aphis-ams-geospatial-hub
    humanURL: https://www.aphis.usda.gov/aphis-ams-geospatial-hub
    properties:
      - url: https://www.aphis.usda.gov/aphis-ams-geospatial-hub
        type: Portal
      - url: https://www.aphis.usda.gov/plant-pests-diseases/mobile-data-collection/gis-portal
        type: GISPortal
    description: The APHIS and AMS Geospatial Hub provides GIS mapping applications, spatial data layers, and geospatial analysis tools for animal and plant health surveillance, pest and disease tracking, and quarantine management.
name: Animal and Plant Health Inspection Service
tags:
  - Agriculture
  - Animal Health
  - Animal Welfare
  - Biotechnology
  - Federal Government
  - Import Export
  - Permits
  - Pest Control
  - Plant Health
  - Regulatory
  - USDA
  - Wildlife
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Government
common:
  - url: https://www.aphis.usda.gov/
    name: APHIS Website
    type: Website
  - url: https://www.aphis.usda.gov/efile
    name: APHIS eFile Permitting Portal
    type: Portal
  - url: https://efile.aphis.usda.gov/s/
    name: APHIS eFile Application
    type: Portal
  - url: https://acir.aphis.usda.gov/s/
    name: Agricultural Commodity Import Requirements
    type: Portal
  - url: https://aphis.my.site.com/PublicSearchTool/s/
    name: APHIS Public Search Tool
    type: Portal
  - url: https://www.aphis.usda.gov/aphis-ams-geospatial-hub
    name: APHIS Geospatial Hub
    type: GISPortal
  - url: https://www.aphis.usda.gov/data-visualization-tools
    name: APHIS Data Visualization Tools
    type: DataVisualization
  - url: https://www.aphis.usda.gov/wildlife-services/publications/pdr
    name: APHIS Wildlife Services Program Data Reports
    type: DataAPI
  - url: https://catalog.data.gov/organization/aphis-usda-gov
    name: APHIS Datasets on Data.gov
    type: OpenData
  - url: https://www.aphis.usda.gov/contact/mrpbs-informatics
    name: Contact APHIS
    type: Contact
  - url: https://www.aphis.usda.gov/about/foia
    name: FOIA Requests
    type: FOIA
  - url: https://www.aphis.usda.gov/about/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
created: '2024-11-21'
modified: '2026-04-19'
position: Consumer
description: USDA's Animal and Plant Health Inspection Service (APHIS) protects the health and value of U.S. agriculture and natural resources by safeguarding against agricultural pests and diseases, ensuring the welfare of animals, and supporting sustainable agricultural practices. APHIS provides digital services including the eFile permitting system for import/export permits, the Agricultural Commodity Import Requirements (ACIR) portal, a geospatial hub for spatial analysis, data visualization tools, and open datasets via data.gov.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
