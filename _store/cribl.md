---
aid: cribl
url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/apis.yml
apis:
- aid: cribl:cloud-api
  name: Cribl Cloud API
  tags:
  - Cloud
  - Configuration
  - Data Pipelines
  - Management
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.cribl.cloud
  humanURL: https://docs.cribl.io/api-reference/
  properties:
  - url: https://docs.cribl.io/api-reference/
    type: Documentation
  - url: openapi/cribl-cloud-api-openapi.yml
    type: OpenAPI
  description: The Cribl Cloud API is a RESTful API that provides a centrally managed control plane for programmatically configuring and managing Cribl resources across Stream, Edge, Search, and Lake deployments. It allows developers to retrieve and manage data, automate repetitive manual processes, and integrate with third-party applications.
- aid: cribl:stream-api
  name: Cribl Stream API
  tags:
  - Data Pipelines
  - Observability
  - Routing
  - Stream Processing
  - Telemetry
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.cribl.io/stream/
  properties:
  - url: https://docs.cribl.io/stream/
    type: Documentation
  - url: openapi/cribl-stream-api-openapi.yml
    type: OpenAPI
  description: The Cribl Stream API provides programmatic access to Cribl Stream, an observability pipeline platform that processes and routes telemetry data in real time. Through the API, developers can manage pipelines, routes, sources, destinations, and worker groups. It enables automation of data collection, transformation, and routing workflows, allowing organizations to control how observability data flows between sources and analytics tools without vendor lock-in.
- aid: cribl:edge-api
  name: Cribl Edge API
  tags:
  - Agents
  - Data Collection
  - Edge Computing
  - Observability
  - Telemetry
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.cribl.io/edge/
  properties:
  - url: https://docs.cribl.io/edge/
    type: Documentation
  - url: openapi/cribl-edge-api-openapi.yml
    type: OpenAPI
  description: The Cribl Edge API provides programmatic access to Cribl Edge, which extends Stream capabilities to the network edge by deploying lightweight agents on endpoints. The API allows developers to manage edge fleets, configure data collection from endpoints, and control data processing closer to the source. This reduces bandwidth consumption and latency by filtering and transforming data at the point of origin before forwarding it to centralized destinations.
- aid: cribl:search-api
  name: Cribl Search API
  tags:
  - Analytics
  - Data Exploration
  - Observability
  - Querying
  - Search
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.cribl.io/search/
  properties:
  - url: https://docs.cribl.io/search/
    type: Documentation
  - url: openapi/cribl-search-api-openapi.yml
    type: OpenAPI
  description: The Cribl Search API provides programmatic access to Cribl Search, a tool for exploring and querying both live and stored observability data in real time. Developers can use the API to execute search queries, retrieve results, and integrate search capabilities into their own applications and workflows. Cribl Search supports federated search across multiple data sources, enabling organizations to gain insights without needing to move or duplicate data into a single location.
- aid: cribl:lake-api
  name: Cribl Lake API
  tags:
  - Analytics
  - Data Lake
  - Data Management
  - Observability
  - Storage
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.cribl.io/lake/
  properties:
  - url: https://docs.cribl.io/lake/
    type: Documentation
  - url: openapi/cribl-lake-api-openapi.yml
    type: OpenAPI
  description: The Cribl Lake API provides programmatic access to Cribl Lake, a data lake solution purpose-built for observability and security data. The API enables developers to manage data storage, retention policies, and access controls for large volumes of telemetry data. Cribl Lake stores data in open formats, making it accessible to any analytics tool, and provides cost-effective long-term storage that keeps data usable and valuable to the teams and tools that need it.
- aid: cribl:as-code-api
  name: Cribl as Code API
  tags:
  - Automation
  - Configuration
  - DevOps
  - Infrastructure as Code
  - Version Control
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://gateway.cribl.cloud
  humanURL: https://docs.cribl.io/cribl-as-code/api/
  properties:
  - url: https://docs.cribl.io/cribl-as-code/api/
    type: Documentation
  - url: openapi/cribl-as-code-api-openapi.yml
    type: OpenAPI
  description: The Cribl As Code API enables developers to manage Cribl configurations programmatically using infrastructure-as-code principles. It supports exporting and importing configurations across deployments, enabling version control, CI/CD integration, and reproducible infrastructure management. Developers can use the API alongside SDKs for Python, Go, and TypeScript, or through Terraform providers, to onboard sources, build and maintain pipelines, and standardize workflows at scale.
name: Cribl
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Redirecting… You are being redirected to the API Reference. If you are not redirected automatically, please click here. This API Reference lists the available endpoints in the Cribl API. Select a category (or tag) to see the endpoints it contains. Select an endpoint to see details like required and optional parameters and request and response examples. Try It Out ​ This API Reference is also available in Cribl at Settings > Global > API Reference.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

