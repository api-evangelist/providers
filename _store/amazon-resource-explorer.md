---
aid: amazon-resource-explorer
name: Amazon Resource Explorer
description: AWS Resource Explorer is a resource search and discovery service. With Resource Explorer, you can explore your resources across AWS Regions using an internet search-like experience. It provides a unified view of your AWS resources and helps you understand your resource inventory.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Discovery
  - Inventory
  - Operations
  - Resource Management
url: https://raw.githubusercontent.com/api-evangelist/amazon-resource-explorer/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-resource-explorer:aws-resource-explorer-api
    name: AWS Resource Explorer API
    description: The AWS Resource Explorer API provides programmatic access to search and discover AWS resources across Regions, manage indexes, views, and resource type configurations for your AWS account.
    humanURL: https://aws.amazon.com/resourceexplorer/
    baseURL: https://resource-explorer-2.amazonaws.com
    tags:
      - Discovery
      - Inventory
      - Resource Management
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/Welcome.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/resource-explorer-2/2022-07-28/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/resourceexplorer/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/resourceexplorer/pricing/
      - type: FAQ
        url: https://aws.amazon.com/resourceexplorer/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/resourceexplorer/
  - type: Portal
    url: https://aws.amazon.com/resourceexplorer/
  - type: Documentation
    url: https://docs.aws.amazon.com/resource-explorer/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/tag/aws-resource-explorer/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Portal
    url: https://console.aws.amazon.com/resource-explorer/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSON-LD
    url: json-ld/amazon-resource-explorer-openapi-index-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-resource-explorer-openapi-resource-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-resource-explorer-openapi-search-request-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-resource-explorer-openapi-search-response-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-resource-explorer-openapi-view-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-resource-explorer-openapi-index-schema.json
  - type: JSONSchema
    url: json-schema/amazon-resource-explorer-openapi-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-resource-explorer-openapi-search-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-resource-explorer-openapi-search-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-resource-explorer-openapi-view-schema.json
  - type: JSONStructure
    url: json-structure/amazon-resource-explorer-openapi-index-structure.json
  - type: JSONStructure
    url: json-structure/amazon-resource-explorer-openapi-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-resource-explorer-openapi-search-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-resource-explorer-openapi-search-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-resource-explorer-openapi-view-structure.json
  - type: Example
    url: examples/amazon-resource-explorer-openapi-index-example.json
  - type: Example
    url: examples/amazon-resource-explorer-openapi-resource-example.json
  - type: Example
    url: examples/amazon-resource-explorer-openapi-search-request-example.json
  - type: Example
    url: examples/amazon-resource-explorer-openapi-search-response-example.json
  - type: Example
    url: examples/amazon-resource-explorer-openapi-view-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-resource-explorer.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-resource-explorer.yaml
  - type: SpectralRules
    url: rules/amazon-resource-explorer-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-resource-explorer-vocabulary.yaml
  - type: OpenAPI
    url: openapi/amazon-resource-explorer-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
