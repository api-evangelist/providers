---
name: Workday Extend
description: Workday Extend is a platform that enables developers to build custom applications that integrate seamlessly with Workday. It provides APIs, development tools, and a runtime environment for creating tailored solutions that extend Workday's core functionality.
image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
url: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
type: Index
created: 2025-03-14T00:00:00.000Z
modified: 2026-03-04T00:00:00.000Z
specificationVersion: '0.18'
apis:
  - name: Workday Extend REST API
    description: RESTful APIs for building and managing Workday Extend applications, including orchestrations, integrations, and custom objects.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://doc.workday.com/extend/
    baseURL: https://api.workday.com/extend/v1
    tags:
      - Custom Applications
      - Extensions
      - Integration
      - Orchestrations
    properties:
      - type: Documentation
        url: https://doc.workday.com/extend/
      - type: OpenAPI
        url: https://api.workday.com/extend/openapi.json
      - type: Authentication
        url: https://doc.workday.com/extend/reference/authentication.html
      - type: Reference
        url: https://developer.workday.com/rest-api-explorer
      - type: OpenAPI
        url: openapi/workday-extend-rest-api-openapi.yml
  - name: Workday Orchestration API
    description: APIs for creating and managing orchestrations that automate business processes and integrate with external systems. Developers visually build orchestrations using an intuitive drag-and-drop Orchestration Builder to define flows, map data, and perform transformations.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://doc.workday.com/extend/orchestrations/
    baseURL: https://api.workday.com/orchestrate/v1
    tags:
      - Automation
      - Business Processes
      - Orchestrations
      - Workflows
    properties:
      - type: Documentation
        url: https://doc.workday.com/extend/orchestrations/
      - type: Tutorials
        url: https://doc.workday.com/extend/tutorials/orchestrations/
      - type: Reference
        url: https://developer.workday.com/documentation/GUID-1293c9bb-ea02-48cd-a523-254b5060b3a6-enHYPHENus
      - type: OpenAPI
        url: openapi/workday-extend-orchestration-openapi.yml
  - name: Workday Custom Objects API
    description: APIs for defining and managing custom objects that extend Workday's data model to meet specific business needs. As new objects and business processes are built, a public REST API is automatically created for other developers and processes to use.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://doc.workday.com/extend/custom-objects/
    baseURL: https://api.workday.com/customObjects/v1
    tags:
      - Custom Fields
      - Custom Objects
      - Data Model
      - Schema
    properties:
      - type: Documentation
        url: https://doc.workday.com/extend/custom-objects/
      - type: Examples
        url: https://doc.workday.com/extend/examples/custom-objects/
      - type: OpenAPI
        url: openapi/workday-extend-custom-objects-openapi.yml
  - name: Workday Graph API
    description: Graph API for querying and traversing Workday data using a graph-based approach. Provides a flexible query interface for accessing interconnected Workday business objects and their relationships across the platform.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://developer.workday.com/graph-api-explorer
    baseURL: https://api.workday.com/
    tags:
      - Business Objects
      - Data Query
      - Graph API
      - Relationships
    properties:
      - type: Documentation
        url: https://developer.workday.com/graph-api-explorer
      - type: Reference
        url: https://developer.workday.com/graph-api-explorer
      - type: OpenAPI
        url: openapi/workday-extend-graph-api-openapi.yml
  - name: Workday Orchestrate Insights API
    description: API for accessing orchestration execution data and monitoring information. Provides insights into orchestration performance, run history, and operational metrics for troubleshooting and optimization.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://api.workday.com/orchestrate/insights
    baseURL: https://api.workday.com/orchestrate/insights
    tags:
      - Analytics
      - Insights
      - Monitoring
      - Orchestrations
    properties:
      - type: Documentation
        url: https://developer.workday.com/documentation/GUID-1293c9bb-ea02-48cd-a523-254b5060b3a6-enHYPHENus
  - name: Workday Illuminate AI API
    description: AI-powered APIs within Workday Illuminate that provide skills and sentiment analysis, document intelligence, natural language WQL queries, and machine learning forecasting capabilities. Enables developers to build intelligent Extend applications leveraging Workday AI services.
    image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
    baseURL: https://api.workday.com/
    tags:
      - Artificial Intelligence
      - Document Intelligence
      - Machine Learning
      - Natural Language Processing
    properties:
      - type: Documentation
        url: https://developer.workday.com/documentation
common:
  - type: Getting Started
    url: https://doc.workday.com/extend/getting-started/
  - type: Portal
    url: https://developer.workday.com/
  - type: Documentation
    url: https://developer.workday.com/documentation
  - type: Reference
    url: https://developer.workday.com/documentation/GUID-04def314-83a7-4edf-b84c-c0a5f005b23c-enHYPHENus
  - type: API Reference
    url: https://doc.workday.com/extend/reference/
  - type: SDK
    url: https://doc.workday.com/extend/sdk/
  - type: Code Samples
    url: https://github.com/Workday/extend-js-example
  - type: Community
    url: https://forum.developer.workday.com
  - type: Support
    url: https://support.developer.workday.com/s/
  - type: Change Log
    url: https://doc.workday.com/extend/release-notes/
  - type: Status
    url: https://status.workday.com/
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: Authentication
    url: https://doc.workday.com/extend/authentication/
  - type: Rate Limits
    url: https://doc.workday.com/extend/rate-limits/
  - type: Blog
    url: https://blog.workday.com/en-us/introducing-workday-build-developer-platform-build-future-work-ai.html
  - type: Website
    url: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
  - type: Login
    url: https://developer.workday.com/login
  - type: Console
    url: https://developer.workday.com/about
  - type: GitHub Organization
    url: https://github.com/Workday
  - type: Marketplace
    url: https://marketplace.workday.com/en-US/home
  - type: Developer Tools
    url: https://api.developer.workday.com/devtools
  - type: Partners
    url: https://www.workday.com/en-us/company/partners/software-partners.html
  - type: Spectral Rules
    url: rules/workday-extend-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/app-development.yaml
  - type: JSON-LD
    url: json-ld/workday-extend-context.jsonld
  - type: JSONSchema
    url: json-schema/workday-extend-app-schema.json
  - type: JSONSchema
    url: json-schema/workday-extend-orchestration-schema.json
  - type: JSONSchema
    url: json-schema/workday-extend-custom-object-schema.json
  - type: Vocabulary
    url: vocabulary/workday-extend-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Automation
  - Custom Applications
  - Enterprise
  - Extensions
  - HCM
  - Human Capital Management
  - Integration
  - Orchestration
  - PaaS
---
