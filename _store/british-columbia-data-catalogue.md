---
aid: british-columbia-data-catalogue
url: https://raw.githubusercontent.com/api-evangelist/british-columbia-data-catalogue/refs/heads/main/apis.yml
name: British Columbia Data Catalogue
tags:
  - Open Data
  - Government
  - Canadian Government
  - British Columbia
  - Provincial Data
  - CKAN
  - Geospatial
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open
created: '2024-11-07'
modified: '2026-04-21'
position: Consumer
description: The British Columbia Data Catalogue is the official open data portal for the Government of British Columbia, Canada. Built on the CKAN open data platform, it provides programmatic access to thousands of BC government datasets spanning census and demographic data, environmental and climate information, geospatial and mapping data, financial reports, transportation and infrastructure data, and health and social services statistics. The CKAN API at api/3/action/ enables searching, listing, and retrieving dataset metadata and resources without authentication.
apis:
  - aid: british-columbia-data-catalogue:ckan-api
    name: BC Data Catalogue CKAN API
    tags:
      - CKAN
      - Open Data
      - Dataset Search
      - Metadata
      - Government Data
    humanURL: https://catalogue.data.gov.bc.ca/
    properties:
      - url: https://catalogue.data.gov.bc.ca/
        type: Documentation
      - url: https://catalogue.data.gov.bc.ca/api/3
        type: BaseURL
    description: The BC Data Catalogue exposes a CKAN v3 REST API at https://catalogue.data.gov.bc.ca/api/3/action/ providing programmatic access to BC government open datasets. Key endpoints include package_list (list all datasets), package_search (search datasets by query), package_show (retrieve dataset metadata and resources), organization_list (list BC government organizations), and resource_show (retrieve specific data resource information). Returns JSON with success status and result payloads. No authentication required for read access to public datasets.
common:
  - type: Website
    url: https://catalogue.data.gov.bc.ca/
  - type: APIBaseURL
    url: https://catalogue.data.gov.bc.ca/api/3/action/
  - type: DatasetList
    url: https://catalogue.data.gov.bc.ca/api/3/action/package_list
  - type: DatasetSearch
    url: https://catalogue.data.gov.bc.ca/api/3/action/package_search
  - type: GovernmentPortal
    url: https://www2.gov.bc.ca/gov/content/data/bc-data-catalogue
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
