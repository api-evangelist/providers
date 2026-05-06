---
aid: federal-bureau-of-investigation
name: Federal Bureau of Investigation
type: Index
description: The Federal Bureau of Investigation (FBI) is the domestic intelligence and security service of the United States and its principal federal law enforcement agency. The FBI publishes public APIs covering its Most Wanted program and Uniform Crime Reporting (UCR) data through the Crime Data Explorer.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FBI
  - Federal Government
created: '2024-10-18'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/federal-bureau-of-investigation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-bureau-of-investigation:most-wanted-api
    name: FBI Most Wanted
    description: The FBI Most Wanted API is designed to help developers easily get information on the FBI Wanted program, including Ten Most Wanted Fugitives, Most Wanted Terrorists, kidnappings and missing persons, and seeking information cases. The API supports filtering by field office and pagination of results.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.fbi.gov/wanted/api
    baseURL: https://api.fbi.gov
    tags:
      - Criminals
      - Law Enforcement
      - Most Wanted
    properties:
      - type: Documentation
        url: https://www.fbi.gov/wanted/api
      - type: OpenAPI
        url: openapi/most-wanted-api-openapi.yml
  - aid: federal-bureau-of-investigation:crime-data-explorer
    name: FBI Crime Data Explorer
    description: The FBI Crime Data Explorer (CDE) provides public access to Uniform Crime Reporting (UCR) data through a JSON API. The API exposes summary statistics, agency-level participation, offense and arrest counts, and hate crime, victimization, and law enforcement officer data drawn from the National Incident-Based Reporting System (NIBRS) and Summary Reporting System.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://crime-data-explorer.fbi.gov/
    baseURL: https://api.usa.gov/crime/fbi/cde
    tags:
      - Crime Data
      - Law Enforcement
      - Statistics
      - Uniform Crime Reporting
    properties:
      - type: Documentation
        url: https://crime-data-explorer.fbi.gov/pages/docApi
      - type: Portal
        url: https://crime-data-explorer.fbi.gov/
common:
  - type: Website
    url: https://www.fbi.gov/
  - type: Documentation
    url: https://www.fbi.gov/services
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
