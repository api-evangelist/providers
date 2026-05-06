---
aid: datahub
name: DataHub
description: DataHub is LinkedIn's generalized metadata search and discovery platform, providing a unified data catalog, lineage graph, governance tooling, and event-driven Actions Framework. It exposes GraphQL, OpenAPI, and Rest.li APIs along with Python and Java SDKs and a CLI for metadata ingestion.
image: https://datahubproject.io/img/datahub-logo.svg
type: Index
tags:
  - Data Catalog
  - Data Discovery
  - Data Governance
  - Data Lineage
  - Metadata
created: '2024-01-15'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/apis.yml
specificationVersion: '0.19'
xType: opensource
position: Consumer
access: 3rd-Party
apis:
  - aid: datahub:datahub-graphql-api
    name: DataHub GraphQL API
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
  - aid: datahub:datahub-openapi
    name: DataHub OpenAPI
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
      - type: OpenAPI
        url: openapi/datahub-openapi-openapi.yml
      - type: JSONSchema
        url: json-schema/datahub-metadata-change-log-event-schema.json
  - aid: datahub:datahub-rest-api
    name: DataHub REST API
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
  - aid: datahub:datahub-python-sdk
    name: DataHub Python SDK
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
  - aid: datahub:datahub-java-sdk
    name: DataHub Java SDK
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
  - aid: datahub:datahub-cli
    name: DataHub CLI
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
  - aid: datahub:datahub-actions-framework
    name: DataHub Actions Framework
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
      - type: AsyncAPI
        url: asyncapi/datahub-actions-asyncapi.yml
common:
  - type: Website
    url: https://datahub.com
  - type: Portal
    url: https://docs.datahub.com
  - type: Documentation
    url: https://docs.datahub.com/docs/
  - type: Getting Started
    url: https://docs.datahub.com/docs/quickstart
  - type: Authentication
    url: https://docs.datahub.com/docs/authentication
  - type: GitHubRepository
    url: https://github.com/datahub-project/datahub
  - type: Slack
    url: https://slack.datahubproject.io
  - type: Blog
    url: https://datahub.com/blog/
  - type: Demo
    url: https://demo.datahubproject.io/
  - type: Change Log
    url: https://github.com/datahub-project/datahub/releases
  - type: Status
    url: https://status.datahub.com
  - type: Community
    url: https://forum.datahubproject.io/
  - type: YouTube
    url: https://youtube.com/@datahubproject
  - type: LinkedIn
    url: https://www.linkedin.com/company/datahub-cloud
  - type: Privacy Policy
    url: https://datahub.com/privacy-policy/
  - type: Security
    url: https://docs.datahub.com/docs/security_stance
  - type: JSON-LD
    url: json-ld/datahub-context.jsonld
  - type: Vocabulary
    url: vocabulary/datahub-vocabulary.yml
  - type: Capabilities
    url: capabilities/datahub-capabilities.yml
  - type: Rules
    url: rules/datahub-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
