---
aid: bureau-of-consular-affairs
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-consular-affairs/refs/heads/main/apis.yml
name: Bureau of Consular Affairs
tags:
  - Federal Government
  - Passports
  - Travel
  - Travel Advisories
  - Visas
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-25'
modified: '2026-04-21'
position: Consumer
description: The Bureau of Consular Affairs (CA) is a bureau of the United States Department of State responsible for administering laws, formulating regulations, and implementing policies related to consular services and immigration. CA provides travel advisories, passport and visa information, and publishes datasets through its data catalog accessible via the CKAN API.
apis:
  - aid: bureau-of-consular-affairs:ca-data-catalog-ckan-api
    name: Bureau of Consular Affairs Data Catalog (CKAN API)
    tags:
      - CKAN
      - Data Catalog
      - Federal Government
      - Open Data
    humanURL: https://cadatacatalog.state.gov/
    baseURL: https://cadatacatalog.state.gov/api/3/action
    properties:
      - url: https://cadatacatalog.state.gov/dataset/
        type: Documentation
      - url: https://cadatacatalog.state.gov/api/3
        type: DataAPI
    description: The CA Data Catalog provides access to datasets from the Bureau of Consular Affairs via the CKAN API. It includes passport issuance statistics, visa issuance data, adoption statistics, and other consular affairs data. The CKAN API supports dataset search, retrieval, and resource downloads.
  - aid: bureau-of-consular-affairs:travel-advisories
    name: Travel Advisories API
    tags:
      - Federal Government
      - Travel
      - Travel Advisories
    humanURL: https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/
    baseURL: https://travel.state.gov
    properties:
      - url: https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/
        type: Documentation
      - url: https://travelmaps.state.gov/TSGMap/
        type: DataAPI
    description: The State Department publishes travel advisory levels (Level 1-4) for every country. Advisory data is available for consumption by travel applications and services to help inform travelers about safety conditions.
  - aid: bureau-of-consular-affairs:passport-issuance-statistics
    name: Passport Issuance Statistics
    tags:
      - Federal Government
      - Passports
      - Statistics
    humanURL: https://cadatacatalog.state.gov/dataset/passportstatistics
    properties:
      - url: https://cadatacatalog.state.gov/dataset/passportstatistics
        type: DataAPI
      - url: https://cadatacatalog.state.gov/dataset/passportstatistics
        type: Documentation
    description: Annual and monthly passport issuance statistics published by the Bureau of Consular Affairs, available as downloadable datasets through the CA data catalog.
common:
  - type: Website
    url: https://travel.state.gov/
  - type: Portal
    url: https://cadatacatalog.state.gov/
  - type: Privacy Policy
    url: https://travel.state.gov/content/travel/en/legal/privacy-policy.html
  - type: CKAN API
    url: https://cadatacatalog.state.gov/api/3/action/package_list
  - type: Statistics
    url: https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
