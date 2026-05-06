---
aid: new-york-public-library-whats-on-the-menu
name: New York Public Library What's On The Menu
description: The New York Public Library's What's On The Menu project is a digital collection that showcases over 17,000 historical restaurant menus from the New York City area dating back to the 1850s. The companion API provides programmatic access to menus, pages, and dishes including prices, names, dates, and full-text search. Token-based authentication is required and rate limits apply (5,000 requests/day, 2 requests/second).
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Libraries
  - Menus
  - Restaurants
  - History
  - Open Data
  - Food
url: https://raw.githubusercontent.com/api-evangelist/new-york-public-library-whats-on-the-menu/refs/heads/main/apis.yml
created: '2024-11-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: new-york-public-library-whats-on-the-menu:new-york-public-library-whats-on-the-menu
    name: NYPL What's On The Menu API
    description: The NYPL What's On The Menu API exposes the full Menus dataset for programmatic exploration. Endpoints cover menus and their pages, dishes, search across both, and filtering by year, status, and other properties. Responses are JSON or XML. Token-based authentication is required (request access via menus@nypl.org). Daily rate limits and pagination headers are provided.
    humanURL: http://nypl.github.io/menus-api/
    baseURL: http://api.menus.nypl.org
    tags:
      - Libraries
      - Menus
      - Restaurants
      - History
      - Open Data
    properties:
      - type: Documentation
        url: http://nypl.github.io/menus-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/new-york-public-library-whats-on-the-menu/refs/heads/main/openapi/new-york-public-library-whats-on-the-menu-openapi-original.yaml
      - type: Project Site
        url: http://menus.nypl.org/
      - type: Data Exports
        url: http://menus.nypl.org/data
    contact:
      - FN: NYPL Menus Project
        email: menus@nypl.org
common:
  - type: Website
    url: http://menus.nypl.org/
  - type: Documentation
    url: http://nypl.github.io/menus-api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
