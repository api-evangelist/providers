---
aid: library-of-congress
name: Library of Congress
description: The Library of Congress is the largest library in the world, with millions of books, films and video, audio recordings, photographs, newspapers, maps and manuscripts in its collections. The Library is the main research arm of the U.S. Congress and the home of the U.S. Copyright Office. The Library publishes a suite of public APIs that expose its catalog, digital collections, historic newspapers, and legislative information.
type: Index
position: Producer
access: Public
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cultural Heritage
  - Federal Government
  - Library
  - Legislative
  - Newspapers
  - Search
created: '2024-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/library-of-congress/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: library-of-congress:loc-gov-json-api
    name: Library of Congress loc.gov JSON API
    description: The loc.gov JSON API returns structured JSON or YAML representations of the Library of Congress's online collections, items, search results, and resource pages, enabling programmatic access to digital collections metadata and content.
    humanURL: https://www.loc.gov/apis/json-and-yaml/
    baseURL: https://www.loc.gov
    tags:
      - Collections
      - Library
      - Metadata
      - Search
    properties:
      - type: Documentation
        url: https://www.loc.gov/apis/json-and-yaml/
      - type: Reference
        url: https://www.loc.gov/apis/json-and-yaml/requests/
      - type: OpenAPI
        url: openapi/library-of-congress-loc-gov-json-api-openapi.yml
  - aid: library-of-congress:chronicling-america-api
    name: Library of Congress Chronicling America API
    description: The Chronicling America API exposes historic American newspapers digitized through the National Digital Newspaper Program, providing search and metadata access to newspaper pages, issues, and titles.
    humanURL: https://chroniclingamerica.loc.gov/about/api/
    baseURL: https://chroniclingamerica.loc.gov
    tags:
      - Historic
      - Library
      - Newspapers
      - Search
    properties:
      - type: Documentation
        url: https://chroniclingamerica.loc.gov/about/api/
      - type: OpenAPI
        url: openapi/library-of-congress-chronicling-america-api-openapi.yml
  - aid: library-of-congress:congress-gov-api
    name: Library of Congress Congress.gov API
    description: The Congress.gov API provides programmatic access to legislative information, including bills, laws, members, committees, and Congressional Record content from the U.S. Congress.
    humanURL: https://api.congress.gov/
    baseURL: https://api.congress.gov/v3
    tags:
      - Bills
      - Congress
      - Legislative
      - Members
    properties:
      - type: Documentation
        url: https://github.com/LibraryOfCongress/api.congress.gov/
      - type: SignUp
        url: https://api.congress.gov/sign-up/
      - type: OpenAPI
        url: openapi/library-of-congress-congress-gov-api-openapi.yml
common:
  - type: Website
    url: https://www.loc.gov/
  - type: Documentation
    url: https://www.loc.gov/apis/
  - type: Reference
    url: https://www.loc.gov/apis/json-and-yaml-responses/
  - type: GitHubOrganization
    url: https://github.com/LibraryOfCongress
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
