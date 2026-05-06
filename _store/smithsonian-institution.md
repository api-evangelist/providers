---
aid: smithsonian-institution
name: Smithsonian Institution
description: The Smithsonian Institution provides open access APIs to its collections of over 22 million objects, artworks, and natural history specimens from 19 museums, 21 libraries, and 9 research centers. The Open Access API enables developers to search and retrieve collection data, images, and metadata across the world's largest museum and research complex.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collections
  - Cultural Heritage
  - Museums
  - Open Data
  - Art
  - Natural History
  - Research
created: '2024-12-25'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/smithsonian-institution/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: smithsonian-institution:open-access-api
    name: Smithsonian Open Access API
    description: The Smithsonian Open Access API provides programmatic access to the Smithsonian's publicly available collection data including objects, artworks, specimens, and related media across its museums and research centers. Requires API key registration at api.data.gov.
    humanURL: https://www.si.edu/openaccess/devtools
    baseURL: https://edan.si.edu/openaccess
    tags:
      - Collections
      - Museums
      - Open Data
      - Search
      - Objects
      - Art
      - Natural History
    properties:
      - type: Documentation
        url: https://www.si.edu/openaccess/devtools
      - type: Documentation
        url: https://edan.si.edu/openaccess/docs/
      - type: GitHub Repository
        url: https://github.com/Smithsonian/smithsonian-openaccess
      - type: Sign Up
        url: https://api.data.gov/signup
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/smithsonian-institution/refs/heads/main/openapi/smithsonian-open-access-openapi.yml
common:
  - type: Website
    url: https://www.si.edu/
  - type: Open Access Portal
    url: https://www.si.edu/openaccess
  - type: Developer Tools
    url: https://www.si.edu/openaccess/devtools
  - type: GitHub Organization
    url: https://github.com/Smithsonian
  - type: Data Repository
    url: https://github.com/Smithsonian/OpenAccess
  - type: API Key Registration
    url: https://api.data.gov/signup
  - type: Python Client
    url: https://github.com/Smithsonian/smithsonian-openaccess
  - type: Metadata Documentation
    url: https://edan.si.edu/openaccess/docs/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
