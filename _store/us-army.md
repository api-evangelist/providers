---
aid: us-army
url: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/apis.yml
apis:
  - aid: us-army:us-army-public-api
    name: US Army Public API
    tags:
      - Army
      - Federal Government
      - Military
      - News
      - Articles
      - Public Information
    humanURL: https://api.army.mil/
    baseURL: https://api.army.mil/api/v1
    properties:
      - url: https://api.army.mil/
        type: Documentation
      - url: https://api.army.mil/
        type: SwaggerUI
      - url: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/openapi/us-army-public-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/rules/us-army-public-rules.yml
        type: SpectralRuleset
      - url: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/capabilities/army-public-information.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/json-schema/us-army-article-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/json-ld/us-army-context.jsonld
        type: JSONLDContext
    description: The US Army Public API provides public access to Army news articles, events, and official announcements. Documented with OpenAPI 3 (OAS3) and a Swagger UI interface at api.army.mil. The API enables access to Army content including articles, news items, and public events.
  - aid: us-army:us-army-open-data
    name: US Army Open Data
    tags:
      - Army
      - Federal Government
      - Open Data
      - Military
    humanURL: https://www.army.mil/
    properties:
      - url: https://www.army.mil/
        type: Documentation
      - url: https://catalog.data.gov/dataset?publisher=US+Army
        type: DataGov
      - url: https://github.com/USArmyResearchLab
        type: GitHubOrg
    description: The US Army provides open data resources through data.gov and maintains open source projects through the US Army Research Laboratory GitHub organization. Army data includes geospatial datasets, research publications, and public information resources.
name: US Army
tags:
  - Army
  - Federal Government
  - Military
  - Defense
  - Open Data
  - News
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-05-03'
position: Consuming
description: The US Army is the largest branch of the United States military and is responsible for conducting ground combat operations. Its mission is to defend the nation and support humanitarian, peacekeeping, and training missions worldwide. The Army maintains a public API at api.army.mil providing access to news articles, events, and official content using OpenAPI 3 specification.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
