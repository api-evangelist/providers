---
aid: harbor
name: Harbor
description: Harbor is a no-code tool that lets brands build an owned community platform where superfans can engage with the brand and earn rewards. Harbor enables businesses to create superfan strategies through customizable community platforms with engagement and loyalty features.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Community
  - Engagement
  - Loyalty
  - Superfans
url: https://raw.githubusercontent.com/api-evangelist/harbor/refs/heads/main/apis.yml
created: '2025-02-17'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: harbor:harbor
    name: Harbor API
    description: The Harbor API enables programmatic access to the Harbor community platform, allowing brands to manage their superfan community, rewards programs, and engagement features.
    humanURL: https://api.harbor.gg/
    tags:
      - Community
      - Engagement
      - Loyalty
    properties:
      - type: Documentation
        url: https://api.harbor.gg/
      - type: OpenAPI
        url: https://api.harbor.gg/docs/v1/swagger.json
      - type: OpenAPI
        url: openapi/harbor-openapi.yml
      - type: JSONSchema
        url: json-schema/harbor-account-schema.json
      - type: JSONSchema
        url: json-schema/harbor-member-schema.json
common:
  - type: Website
    url: https://www.harbor.gg/
  - type: Documentation
    url: https://api.harbor.gg/
  - type: Privacy Policy
    url: https://www.harbor.gg/privacy-policy
  - type: JSON-LD
    url: json-ld/harbor-context.jsonld
  - type: JSONSchema
    url: json-schema/harbor-member-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
