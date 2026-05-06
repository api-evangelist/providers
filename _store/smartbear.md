---
aid: smartbear
name: SmartBear
description: SmartBear is a software company that provides AI-powered tools for API lifecycle management including design, testing, documentation, and governance. Their product portfolio includes SwaggerHub for API design and documentation, ReadyAPI for API testing, PactFlow for contract testing, and other tools for software quality and performance. SmartBear's developer API enables programmatic access to manage API definitions, automate lifecycle workflows, and integrate SwaggerHub with CI/CD pipelines and third-party services.
url: https://raw.githubusercontent.com/api-evangelist/smartbear/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - API Design
  - API Documentation
  - API Testing
  - Contract Testing
  - Governance
  - Monitoring
  - Platform
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consuming
apis:
  - aid: smartbear:swaggerhub
    name: SwaggerHub API
    tags:
      - API Design
      - API Documentation
      - Collaboration
      - OpenAPI
      - Governance
    humanURL: https://swagger.io/product/
    properties:
      - url: https://support.smartbear.com/swaggerhub/docs/en/index.html
        type: Documentation
      - url: https://swagger.io/product/pricing/
        type: Pricing
      - url: https://github.com/SmartBear/swaggerhub-cli
        type: GitHubRepository
      - url: https://openapi/smartbear-swaggerhub-openapi.yml
        type: OpenAPI
    description: 'The SwaggerHub API provides programmatic access to manage API definitions, domains, projects, and integrations on the SwaggerHub platform. It allows teams to automate API lifecycle management including creating, updating, publishing, and versioning APIs. Base URL: https://api.swaggerhub.com. Authentication via API key in the Authorization header.'
  - aid: smartbear:readyapi
    name: ReadyAPI
    tags:
      - API Testing
      - Performance Testing
      - Security Testing
      - Functional Testing
    humanURL: https://smartbear.com/product/ready-api/overview/
    properties:
      - url: https://support.smartbear.com/readyapi/docs/
        type: Documentation
      - url: https://github.com/SmartBear/readyapi4j
        type: GitHubRepository
    description: ReadyAPI is SmartBear's API quality platform for functional, security, and performance testing. It supports RESTful, GraphQL, and other API standards, and is used by more than 250,000 users running more than 2 million tests per month.
  - aid: smartbear:pactflow
    name: PactFlow
    tags:
      - API Testing
      - CI/CD
      - Contract Testing
      - Consumer-Driven Contracts
    humanURL: https://pactflow.io/
    properties:
      - url: https://docs.pactflow.io/
        type: Documentation
      - url: https://developer.smartbear.com/pactflow/default/pactflow_saas_api
        type: APIReference
    description: 'PactFlow is SmartBear''s contract testing platform that ensures API changes do not break consumer applications. It integrates with SwaggerHub for bi-directional contract testing and uses REST principles with predictable resource-oriented URLs. Base URL: https://{account}.pactflow.io.'
common:
  - type: Website
    url: https://smartbear.com/
  - type: DeveloperPortal
    url: https://developer.smartbear.com/
  - type: Documentation
    url: https://support.smartbear.com/documentation/
  - type: Community
    url: https://community.smartbear.com/
  - type: Blog
    url: https://smartbear.com/blog/
  - type: GitHubOrganization
    url: https://github.com/SmartBear
  - type: GitHubOrganization
    url: https://github.com/SmartBear-DevRel
  - type: Pricing
    url: https://swagger.io/product/pricing/
  - type: OpenAPI
    url: openapi/smartbear-swaggerhub-openapi.yml
  - type: Spectral
    url: rules/smartbear-rules.yml
  - type: Capabilities
    url: capabilities/api-design-and-governance.yaml
  - type: JSONSchema
    url: json-schema/smartbear-api-entry-schema.json
  - type: JSONSchema
    url: json-schema/smartbear-integration-schema.json
  - type: JSONStructure
    url: json-structure/smartbear-swaggerhub-structure.json
  - type: JSONLD
    url: json-ld/smartbear-context.jsonld
  - type: Vocabulary
    url: vocabulary/smartbear-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
