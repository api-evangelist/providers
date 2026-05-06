---
aid: department-of-labor
name: Department of Labor
description: The U.S. Department of Labor (DOL) is the federal department that fosters, promotes, and develops the welfare of wage earners, job seekers, and retirees, improves working conditions, advances opportunities for profitable employment, and assures work-related benefits and rights. DOL exposes a portfolio of public APIs and data feeds including the modernized DOL APIv4 served from the DOL Open Data Portal, the Bureau of Labor Statistics Public Data API, the DOL Enforcement Data site, and Data.gov.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - BLS
  - Employment
  - Enforcement
  - Federal Government
  - Labor
  - Open Data
  - Statistics
  - Wages
  - Workforce
url: https://raw.githubusercontent.com/api-evangelist/department-of-labor/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
position: Producer
access: Public
apis:
  - aid: department-of-labor:dol-api-v4
    name: DOL Open Data API V4
    description: The DOL Open Data API v4 is the Department of Labor's modernized REST API replacing the retired developer.dol.gov APIv1 and APIv2. It is served from the DOL Data Portal at dataportal.dol.gov and exposes more than 200 datasets covering wage and hour, occupational safety and health, employment and training, retirement security, and other DOL programs. The Datasets endpoint is publicly accessible without an API key; data endpoints require an API key obtained through registration on the Data Portal.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dataportal.dol.gov/
    baseURL: https://apiprod.dol.gov/v4
    tags:
      - Datasets
      - DOL Data Portal
      - Open Data
      - REST
    properties:
      - type: Documentation
        url: https://dataportal.dol.gov/
      - type: User Guide
        url: https://www.dataportal.dol.gov/pdf/dol-api-user-guide.pdf
      - type: Datasets Catalog
        url: https://dataportal.dol.gov/datasets
      - type: Datasets Endpoint
        url: https://apiprod.dol.gov/v4/datasets
      - type: Sign Up
        url: https://dataportal.dol.gov/registration
    contact:
      - FN: DOL Data Portal
        url: https://dataportal.dol.gov/
  - aid: department-of-labor:bls-public-data-api
    name: BLS Public Data API V2
    description: The Bureau of Labor Statistics Public Data API v2 provides programmatic access to historical BLS time series data in JSON or Excel. Version 2 requires registration to obtain a registrationkey query parameter and raises limits to up to 20 years of data per request, 50 series per request, and 500 queries per day. Series include CPI, PPI, employment, wages, productivity, and more.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.bls.gov/developers/
    baseURL: https://api.bls.gov/publicAPI/v2
    tags:
      - BLS
      - CPI
      - Employment
      - Statistics
      - Time Series
      - Wages
    properties:
      - type: Documentation
        url: https://www.bls.gov/developers/home.htm
      - type: API Signatures
        url: https://www.bls.gov/developers/api_signature_v2.htm
      - type: Features
        url: https://www.bls.gov/bls/api_features.htm
      - type: FAQ
        url: https://www.bls.gov/developers/api_faqs.htm
      - type: Python Sample
        url: https://www.bls.gov/developers/api_python.htm
      - type: Sign Up
        url: https://data.bls.gov/registrationEngine/
    contact:
      - FN: BLS Customer Support
        url: https://www.bls.gov/bls/contact.htm
  - aid: department-of-labor:dol-enforcement-data
    name: DOL Enforcement Data
    description: The DOL Enforcement Data site at data.dol.gov publishes the Department's enforcement records from agencies including the Wage and Hour Division, OSHA, MSHA, OFCCP, and the Employee Benefits Security Administration. Records are available as bulk downloads and through datasets surfaced on Data.gov.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://data.dol.gov/
    baseURL: https://data.dol.gov
    tags:
      - Enforcement
      - MSHA
      - OFCCP
      - OSHA
      - Wage and Hour
    properties:
      - type: Documentation
        url: https://data.dol.gov/
      - type: Datasets
        url: https://catalog.data.gov/organization/dol-gov
    contact:
      - FN: DOL Open Data
        url: https://www.dol.gov/agencies/oasam
  - aid: department-of-labor:dol-api-sampler
    name: DOL API Sampler
    description: The DOL API Sampler is an interactive playground for exploring the DOL Open Data API v4 endpoints. It serves as a quick way to issue sample requests, browse parameters, and inspect responses against the live API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://devtools.dol.gov/apisampler
    baseURL: https://devtools.dol.gov/apisampler
    tags:
      - DevTools
      - Playground
      - Sampler
    properties:
      - type: Documentation
        url: https://devtools.dol.gov/apisampler
    contact:
      - FN: DOL Developer Community
        url: https://usdepartmentoflabor.github.io/DOLAPI/
  - aid: department-of-labor:dol-open-data-catalog
    name: DOL Open Data Catalog
    description: The Department of Labor Open Data Catalog publishes datasets across labor statistics, enforcement, employment training, and worker protection programs. Datasets are surfaced on Data.gov under the dol-gov organization and accessible via the Data.gov CKAN-compatible API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://catalog.data.gov/organization/dol-gov
    baseURL: https://catalog.data.gov/api/3
    tags:
      - CKAN
      - Datasets
      - Open Data
    properties:
      - type: Documentation
        url: https://catalog.data.gov/organization/dol-gov
      - type: CKAN Reference
        url: https://docs.ckan.org/en/2.8/api/
    contact:
      - FN: DOL Open Data
        url: https://catalog.data.gov/organization/dol-gov
common:
  - type: Website
    url: https://www.dol.gov
  - type: Open Data Portal
    url: https://dataportal.dol.gov/
  - type: Developer Community
    url: https://usdepartmentoflabor.github.io/DOLAPI/
  - type: Bureau of Labor Statistics
    url: https://www.bls.gov
  - type: Enforcement Data
    url: https://data.dol.gov/
  - type: API Sampler
    url: https://devtools.dol.gov/apisampler
  - type: OSHA
    url: https://www.osha.gov
  - type: MSHA
    url: https://www.msha.gov
  - type: ETA
    url: https://www.dol.gov/agencies/eta
  - type: Wage and Hour Division
    url: https://www.dol.gov/agencies/whd
  - type: EBSA
    url: https://www.dol.gov/agencies/ebsa
  - type: OFCCP
    url: https://www.dol.gov/agencies/ofccp
  - type: Data.gov DOL Catalog
    url: https://catalog.data.gov/organization/dol-gov
  - type: News
    url: https://www.dol.gov/newsroom
  - type: Privacy Policy
    url: https://www.dol.gov/general/privacynotice
  - type: GitHub Organization
    url: https://github.com/USDepartmentofLabor
  - type: JSON-LD
    url: json-ld/department-of-labor-context.jsonld
  - type: Vocabulary
    url: vocabulary/department-of-labor-vocabulary.yml
  - type: Capabilities
    url: capabilities/department-of-labor-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
