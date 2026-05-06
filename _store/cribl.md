---
aid: cribl
name: Cribl
x-type: company
description: Cribl is an observability pipeline company providing a suite of products for collecting, processing, routing, searching, and storing telemetry data at scale. Cribl's developer platform offers REST APIs across Stream, Edge, Search, Lake, and the As Code product line, exposing programmatic control over data pipelines, edge agents, federated search jobs, lake datasets, and infrastructure-as-code configuration management. The Cribl Cloud API acts as a centrally managed control plane across all deployments and authenticates with OAuth 2.0 client credentials.
url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Configuration
  - Data Lake
  - Data Pipelines
  - Data Routing
  - Edge Computing
  - Infrastructure as Code
  - Observability
  - Search
  - Security Data
  - Stream Processing
  - Telemetry
created: '2025-03-05'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Index
access: 3rd-Party
position: Consuming
apis:
  - aid: cribl:cribl-cloud-api
    name: Cribl Cloud API
    description: The Cribl Cloud API is a RESTful control plane API for programmatically configuring and managing Cribl resources across Stream, Edge, Search, and Lake deployments. It allows developers to retrieve and manage data, automate repetitive manual processes, and integrate with third-party applications. The API uses OAuth 2.0 client credentials and follows a resource-based structure where each endpoint corresponds to a specific Cribl resource or collection.
    humanURL: https://docs.cribl.io/api-reference/
    baseURL: https://api.cribl.cloud
    properties:
      - type: Documentation
        url: https://docs.cribl.io/api-reference/
      - type: OpenAPI
        url: openapi/cribl-cloud-api-openapi.yml
      - type: Rules
        url: rules/cribl-cloud-api-rules.yml
      - type: Capabilities
        url: capabilities/cribl-cloud-api-capabilities.yml
    tags:
      - Cloud
      - Configuration
      - Control Plane
      - Data Pipelines
      - Management
      - Observability
  - aid: cribl:cribl-stream-api
    name: Cribl Stream API
    description: The Cribl Stream API provides programmatic access to Cribl Stream, an observability pipeline platform that processes and routes telemetry data in real time. Through the API, developers can manage pipelines, routes, sources, destinations, and worker groups. It enables automation of data collection, transformation, and routing workflows.
    humanURL: https://docs.cribl.io/stream/
    baseURL: https://api.example.com
    properties:
      - type: Documentation
        url: https://docs.cribl.io/stream/
      - type: OpenAPI
        url: openapi/cribl-stream-api-openapi.yml
      - type: Rules
        url: rules/cribl-stream-api-rules.yml
      - type: Capabilities
        url: capabilities/cribl-stream-api-capabilities.yml
    tags:
      - Data Pipelines
      - Observability
      - Routing
      - Stream Processing
      - Telemetry
  - aid: cribl:cribl-edge-api
    name: Cribl Edge API
    description: The Cribl Edge API provides programmatic access to Cribl Edge, which extends Stream capabilities to the network edge by deploying lightweight agents on endpoints. The API allows developers to manage edge fleets, configure data collection from endpoints, and control data processing closer to the source.
    humanURL: https://docs.cribl.io/edge/
    baseURL: https://api.example.com
    properties:
      - type: Documentation
        url: https://docs.cribl.io/edge/
      - type: OpenAPI
        url: openapi/cribl-edge-api-openapi.yml
      - type: Rules
        url: rules/cribl-edge-api-rules.yml
      - type: Capabilities
        url: capabilities/cribl-edge-api-capabilities.yml
    tags:
      - Agents
      - Data Collection
      - Edge Computing
      - Observability
      - Telemetry
  - aid: cribl:cribl-search-api
    name: Cribl Search API
    description: The Cribl Search API provides programmatic access to Cribl Search, a tool for exploring and querying both live and stored observability data in real time. Developers can use the API to execute search queries, retrieve results, and integrate search capabilities into their own applications and workflows.
    humanURL: https://docs.cribl.io/search/
    baseURL: https://api.example.com
    properties:
      - type: Documentation
        url: https://docs.cribl.io/search/
      - type: OpenAPI
        url: openapi/cribl-search-api-openapi.yml
      - type: Rules
        url: rules/cribl-search-api-rules.yml
      - type: Capabilities
        url: capabilities/cribl-search-api-capabilities.yml
    tags:
      - Analytics
      - Data Exploration
      - Federated Search
      - Observability
      - Querying
  - aid: cribl:cribl-lake-api
    name: Cribl Lake API
    description: The Cribl Lake API provides programmatic access to Cribl Lake, a data lake solution purpose-built for observability and security data. The API enables developers to manage data storage, retention policies, and access controls for large volumes of telemetry data in open formats.
    humanURL: https://docs.cribl.io/lake/
    baseURL: https://api.example.com
    properties:
      - type: Documentation
        url: https://docs.cribl.io/lake/
      - type: OpenAPI
        url: openapi/cribl-lake-api-openapi.yml
      - type: Rules
        url: rules/cribl-lake-api-rules.yml
      - type: Capabilities
        url: capabilities/cribl-lake-api-capabilities.yml
    tags:
      - Analytics
      - Data Lake
      - Data Management
      - Observability
      - Storage
  - aid: cribl:cribl-as-code-api
    name: Cribl As Code API
    description: The Cribl As Code API enables developers to manage Cribl configurations programmatically using infrastructure-as-code principles. It supports exporting and importing configurations across deployments, enabling version control, CI/CD integration, and reproducible infrastructure management. Developers can use the API alongside SDKs for Python, Go, and TypeScript or through Terraform providers.
    humanURL: https://docs.cribl.io/cribl-as-code/api/
    baseURL: https://gateway.cribl.cloud
    properties:
      - type: Documentation
        url: https://docs.cribl.io/cribl-as-code/api/
      - type: OpenAPI
        url: openapi/cribl-as-code-api-openapi.yml
      - type: Rules
        url: rules/cribl-as-code-api-rules.yml
      - type: Capabilities
        url: capabilities/cribl-as-code-api-capabilities.yml
    tags:
      - Automation
      - Configuration
      - DevOps
      - Infrastructure as Code
      - Version Control
common:
  - type: JSONLD
    url: json-ld/cribl-context.jsonld
  - type: JSONSchema
    url: json-schema/cribl-pipeline-schema.json
  - type: JSONSchema
    url: json-schema/cribl-route-schema.json
  - type: JSONSchema
    url: json-schema/cribl-source-schema.json
  - type: JSONSchema
    url: json-schema/cribl-destination-schema.json
  - type: JSONSchema
    url: json-schema/cribl-worker-group-schema.json
  - type: Website
    url: https://cribl.io/
  - type: Documentation
    url: https://docs.cribl.io/
  - type: Portal
    url: https://docs.cribl.io/
  - type: Login
    url: https://login.cribl.cloud/
  - type: Blog
    url: https://cribl.io/blog/
  - type: PrivacyPolicy
    url: https://cribl.io/privacy-policy/
  - type: TermsOfService
    url: https://cribl.io/terms-of-service/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
