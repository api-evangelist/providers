---
aid: datahub
url: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/apis.yml
apis:
- name: DataHub GraphQL API
  description: Primary API for querying and mutating metadata in DataHub. The GraphQL API serves as the main public API for the platform and can be used to fetch and update metadata programmatically in the language of your choice. It mirrors the capabilities available in the DataHub UI.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/api/graphql/overview
  baseURL: http://localhost:8080/api/graphql
  tags:
  - GraphQL
  - Metadata
  - Queries
  - Search
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/api/graphql/overview
  - type: Getting Started
    url: https://docs.datahub.com/docs/api/graphql/getting-started
  - type: Reference
    url: https://docs.datahub.com/docs/graphql/queries
  - type: Playground
    url: http://localhost:8080/api/graphiql
- name: DataHub OpenAPI
  description: RESTful API endpoints documented using the OpenAPI standard for interacting with DataHub metadata. Provides endpoints for entities, relationships, timeline, and platform events. The OpenAPI spec is auto-generated and available via Swagger UI for interactive exploration. Recommended for advanced users who need lower-level access to the metadata graph.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/api/openapi/openapi-usage-guide
  baseURL: http://localhost:8080/openapi/
  tags:
  - Entities
  - Metadata
  - OpenAPI
  - REST
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/api/openapi/openapi-usage-guide
- name: DataHub REST API
  description: The Rest.li API represents the underlying persistence layer and exposes the raw PDL models used in storage. It powers the GraphQL API under the hood and is used for system-specific ingestion of metadata by the Metadata Ingestion Framework. This API is considered system-internal and is not recommended for direct external use.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/api/datahub-apis
  baseURL: http://localhost:8080/
  tags:
  - Entities
  - Internal
  - Metadata
  - REST
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/api/datahub-apis
- name: DataHub Python SDK
  description: Python client for interacting with DataHub. The acryl-datahub package provides a CLI and SDK for DataHub, including REST and Kafka emitter APIs for pushing metadata programmatically. It is one of the most recommended tools for extending and customizing DataHub behavior, especially for ingestion and bulk metadata operations.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/metadata-ingestion/as-a-library
  baseURL: https://pypi.org/project/acryl-datahub/
  tags:
  - Emitter
  - Ingestion
  - Python
  - SDK
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/metadata-ingestion/as-a-library
  - type: GitHubRepository
    url: https://github.com/datahub-project/datahub
  - type: SDKs
    url: https://pypi.org/project/acryl-datahub/
- name: DataHub Java SDK
  description: Java client for interacting with DataHub. The io.acryl datahub-client package offers REST emitter APIs that can be used to emit metadata from JVM-based systems. It supports all major DataHub entity types including Dataset, Chart, Dashboard, Container, DataFlow, DataJob, MLModel, and MLModelGroup.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/metadata-integration/java/as-a-library
  baseURL: https://github.com/datahub-project/datahub
  tags:
  - Emitter
  - Java
  - Metadata
  - SDK
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/metadata-integration/java/as-a-library
  - type: GitHubRepository
    url: https://github.com/datahub-project/datahub
- name: DataHub CLI
  description: Command line tool for interacting with DataHub. The datahub CLI allows you to perform common operations including metadata ingestion, entity management, and system administration from the command line. It is installed as part of the acryl-datahub Python package and supports a plugin architecture for different data source connectors.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/cli
  baseURL: https://pypi.org/project/acryl-datahub/
  tags:
  - CLI
  - Command Line
  - Ingestion
  - Metadata
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/cli
  - type: Getting Started
    url: https://docs.datahub.com/docs/metadata-ingestion/cli-ingestion
  - type: SDKs
    url: https://pypi.org/project/acryl-datahub/
- name: DataHub Actions Framework
  description: Event-driven framework for responding to real-time changes in the DataHub metadata graph. The Actions Framework allows you to configure event sources, transformations, and actions using YAML configuration files. It enables seamless integration of DataHub into a broader event-based architecture by consuming Metadata Change Logs and Platform Events.
  image: https://datahubproject.io/img/datahub-logo.svg
  humanURL: https://docs.datahub.com/docs/actions
  baseURL: https://pypi.org/project/acryl-datahub-actions/
  tags:
  - Actions
  - Automation
  - Events
  - Real-Time
  properties:
  - type: Documentation
    url: https://docs.datahub.com/docs/actions
  - type: Getting Started
    url: https://docs.datahub.com/docs/actions/quickstart
  - type: SDKs
    url: https://pypi.org/project/acryl-datahub-actions/
name: DataHub
tags:
- Data Catalog
- Data Discovery
- Data Governance
- Data Lineage
- Metadata
type: Contract
image: https://datahubproject.io/img/datahub-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: DataHub is LinkedIn's generalized metadata search & discovery tool.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

