---
aid: recreation-gov
name: Recreation.gov
description: The Recreation Information Database (RIDB) provides data resources to citizens, offering a single point of access to information about recreational opportunities nationwide. The RIDB represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, and other attractions/resources.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Recreation
  - Federal
  - Camping
  - Outdoors
  - Public Lands
created: '2025-03-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/recreation-gov/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: recreation-gov:ridb-api
    name: Recreation.gov RIDB API
    description: The Recreation Information Database (RIDB) API provides programmatic access to federal recreation data including activities, facilities, campsites, recreation areas, tours, permit entrances, events, media, links, and managing organizations. Authentication is via API key.
    humanURL: https://ridb.recreation.gov/landing
    baseURL: https://ridb.recreation.gov/api/v1
    tags:
      - Recreation
      - Federal
      - Camping
      - Permits
      - Facilities
    properties:
      - type: Documentation
        url: https://ridb.recreation.gov/docs
      - type: SignUp
        url: https://ridb.recreation.gov/profile
      - type: OpenAPI
        url: openapi/recreation-gov-openapi.yml
common:
  - type: Website
    url: https://www.recreation.gov
  - type: Documentation
    url: https://ridb.recreation.gov/docs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
