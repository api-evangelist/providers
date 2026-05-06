---
aid: national-archives-and-records-administration-nara-
name: National Archives and Records Administration (NARA)
description: The National Archives and Records Administration (NARA) is the nation's record keeper, preserving and providing access to federal government records that document the rights of American citizens and the actions of their government.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.archives.gov/developer
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Archives
  - Federal Government
  - Records
  - Catalog
apis:
  - aid: national-archives-and-records-administration-nara-:catalog-api
    name: National Archives Catalog API
    description: The National Archives Catalog API is a read-write web API for the National Archives Catalog used to perform fielded search of archival metadata, bulk export of metadata and digital media, and post contributions to records.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.archives.gov/research/catalog/help/api
    baseURL: https://catalog.archives.gov/api/v2/
    tags:
      - Archives
      - Records
      - Catalog
      - Search
      - Metadata
    properties:
      - type: Documentation
        url: https://www.archives.gov/research/catalog/help/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/national-archives-and-records-administration-nara-/main/openapi/national-archives-and-records-administration-nara--openapi.json
      - type: SwaggerUI
        url: https://catalog.archives.gov/api/v2/api-docs/
      - type: SourceCode
        url: https://github.com/usnationalarchives/Catalog-API
common:
  - type: Website
    url: https://www.archives.gov/
  - type: Portal
    url: https://www.archives.gov/developer
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
