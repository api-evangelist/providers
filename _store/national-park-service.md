---
aid: national-park-service
name: National Park Service
description: The National Park Service is a federal agency responsible for managing and protecting the United States' national parks, monuments, and historic sites. Established in 1916, the NPS works to preserve natural and cultural resources for future generations while providing opportunities for the public to enjoy and learn from these special places.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-park-service/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Conservation
  - Federal Government
  - Parks
apis:
  - aid: national-park-service:national-park-service
    name: National Park Service API
    tags:
      - Conservation
      - Parks
    humanURL: https://www.nps.gov/subjects/developer/api-documentation.htm
    baseURL: https://developer.nps.gov/api/v1/
    properties:
      - url: https://www.nps.gov/subjects/developer/api-documentation.htm
        type: Documentation
      - url: https://www.nps.gov/subjects/developer/get-started.htm
        type: GettingStarted
      - url: https://www.nps.gov/subjects/developer/guides.htm
        type: Guides
      - url: https://www.nps.gov/subjects/developer/api-key.htm
        type: SignUp
      - url: https://raw.githubusercontent.com/api-evangelist/national-park-service/refs/heads/main/openapi/national-park-service-openapi.yml
        type: OpenAPI
    description: The NPS Data API is open and accessible to all developers, providing official, authoritative data and content about national parks, monuments, and historic sites for use in apps, maps, and other projects.
common:
  - type: Website
    url: https://www.nps.gov/
  - type: Portal
    url: https://www.nps.gov/subjects/developer/index.htm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
