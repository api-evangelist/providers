---
aid: shovels
name: Shovels
description: Shovels is the intelligence layer for the built world, providing building permit data and contractor intelligence aggregated from 1,800+ jurisdictions across the United States. The platform offers 130M+ building permits, 2.3M+ contractor profiles, property details, resident information, and geographic market metrics. Shovels helps materials suppliers, construction tech companies, energy and climate firms, home services companies, real estate professionals, and telecommunications providers identify qualified contractors, understand work history, and power sales and marketing with rich permit data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Construction
  - Building Permits
  - Contractors
  - Real Estate
  - Property Data
  - Market Intelligence
url: https://raw.githubusercontent.com/api-evangelist/shovels/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shovels:shovels-api
    name: Shovels API
    description: The Shovels API v2 provides programmatic access to building permit intelligence and contractor data from 1,800+ US jurisdictions. Access 130M+ permits, 2.3M+ contractor profiles, geographic metrics, resident data, and market analytics. Authentication uses an X-API-Key header. Supports cursor-based pagination, credit tracking, and advanced filtering by geography, date range, tags, job value, property type, and contractor attributes. Data refreshes on the 1st and 15th of each month.
    humanURL: https://www.shovels.ai/api
    baseURL: https://api.shovels.ai/v2
    tags:
      - Construction
      - Building Permits
      - Contractors
      - Property Data
      - Market Intelligence
      - Real Estate
    properties:
      - type: Documentation
        url: https://docs.shovels.ai
      - type: GettingStarted
        url: https://docs.shovels.ai/docs/shovels-api-introduction
      - type: Authentication
        url: https://docs.shovels.ai/docs/shovels-api-introduction
      - type: Pricing
        url: https://www.shovels.ai/pricing
      - type: SignUp
        url: https://app.shovels.ai
      - type: GitHubOrganization
        url: https://github.com/ShovelsAI
      - type: OpenAPI
        url: openapi/shovels-openapi.yml
      - type: JSONSchema
        url: json-schema/shovels-permit-schema.json
      - type: JSONSchema
        url: json-schema/shovels-contractor-schema.json
      - type: JSONStructure
        url: json-structure/shovels-permit-structure.json
      - type: JSONLD
        url: json-ld/shovels-context.jsonld
      - type: SpectralRules
        url: rules/shovels-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/contractor-intelligence.yaml
      - type: Vocabulary
        url: vocabulary/shovels-vocabulary.yml
    contact:
      - FN: Shovels Support
        url: https://docs.shovels.ai
        email: sales@shovels.ai
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
