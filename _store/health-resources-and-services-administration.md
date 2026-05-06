---
aid: health-resources-and-services-administration
name: Health Resources and Services Administration
description: The Health Resources and Services Administration (HRSA) is the primary Federal agency for improving access to health care services for people who are uninsured, isolated, or medically vulnerable. HRSA provides data and web services for healthcare resources, facility locations, and program information.
url: https://raw.githubusercontent.com/api-evangelist/health-resources-and-services-administration/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Healthcare
  - Open Data
  - Public Health
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: health-resources-and-services-administration:hrsa-health-center-data-service
    name: HRSA Health Center Data Service
    description: The HRSA Health Center Data Service enables users to query for health centers by state, county, or ZIP Code, providing access to federally qualified health center location and service information.
    humanURL: https://data.hrsa.gov/tools/web-services
    baseURL: https://data.hrsa.gov
    tags:
      - Government
      - Healthcare
      - Health Centers
      - Open Data
    properties:
      - type: Documentation
        url: https://data.hrsa.gov/tools/web-services
      - type: Registration
        url: https://data.hrsa.gov/tools/web-services/registration
  - aid: health-resources-and-services-administration:hrsa-ryan-white-medical-care-provider
    name: HRSA Ryan White HIV/AIDS Medical Care Provider Data Service
    description: The HRSA Ryan White HIV/AIDS Medical Care Provider Data Service enables users to query for HIV/AIDS care providers around a specified latitude and longitude, supporting access to Ryan White HIV/AIDS Program funded providers.
    humanURL: https://data.hrsa.gov/tools/web-services
    baseURL: https://data.hrsa.gov
    tags:
      - Government
      - Healthcare
      - HIV AIDS
      - Ryan White
      - Open Data
    properties:
      - type: Documentation
        url: https://data.hrsa.gov/tools/web-services
      - type: Registration
        url: https://data.hrsa.gov/tools/web-services/registration
common:
  - type: Website
    url: https://www.hrsa.gov/
  - type: Portal
    url: https://data.hrsa.gov
  - type: Web Services
    url: https://data.hrsa.gov/tools/web-services
  - type: Support
    url: https://www.hrsa.gov/about/contact/programsupport.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
