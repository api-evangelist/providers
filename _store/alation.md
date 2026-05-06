---
aid: alation
url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/apis.yml
name: Alation
tags:
  - Data Catalog
  - Data Governance
  - Data Intelligence
  - Data Lineage
  - Data Quality
  - Business Glossary
  - Metadata Management
  - AI
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: Alation is a data intelligence platform that helps organizations harness the power of their data by providing a centralized platform for data cataloging, governance, and collaboration. By enabling users to easily search, understand, and trust their data, Alation empowers organizations to make data-driven decisions with confidence. Through advanced analytics and AI capabilities, Alation helps organizations uncover insights, improve data quality, and drive innovation.
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: alation:data-catalog-api
    name: Alation Data Catalog API
    tags:
      - Data Catalog
      - Metadata
      - Data Sources
      - Schemas
      - Tables
      - Columns
    properties:
      - url: https://developer.alation.com
        type: Documentation
      - url: openapi/alation-data-catalog-openapi.yaml
        type: OpenAPI
      - url: json-schema/alation-alation-data-catalog-data-source-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-data-catalog-schema-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-data-catalog-table-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-data-catalog-column-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-data-catalog-custom-field-value-schema.json
        type: JSONSchema
      - url: json-structure/alation-alation-data-catalog-data-source-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-data-catalog-schema-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-data-catalog-table-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-data-catalog-column-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-data-catalog-custom-field-value-structure.json
        type: JSONStructure
      - url: examples/alation-alation-data-catalog-data-source-example.json
        type: Example
      - url: examples/alation-alation-data-catalog-schema-example.json
        type: Example
      - url: examples/alation-alation-data-catalog-table-example.json
        type: Example
      - url: examples/alation-alation-data-catalog-column-example.json
        type: Example
      - url: examples/alation-alation-data-catalog-custom-field-value-example.json
        type: Example
    humanURL: https://developer.alation.com
    baseURL: https://your-instance.alation.com/integration/v2
    description: REST API for managing data sources, schemas, tables, columns, and custom field values in the Alation data catalog. Supports metadata retrieval and batch updates for catalog objects.
  - aid: alation:lineage-api
    name: Alation Lineage API
    tags:
      - Data Lineage
      - Dataflow
      - Metadata
    properties:
      - url: https://developer.alation.com
        type: Documentation
      - url: openapi/alation-lineage-openapi.yaml
        type: OpenAPI
      - url: json-schema/alation-alation-lineage-dataflow-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-lineage-lineage-graph-schema.json
        type: JSONSchema
      - url: json-structure/alation-alation-lineage-dataflow-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-lineage-lineage-graph-structure.json
        type: JSONStructure
      - url: examples/alation-alation-lineage-dataflow-example.json
        type: Example
      - url: examples/alation-alation-lineage-lineage-graph-example.json
        type: Example
    humanURL: https://developer.alation.com/dev/reference/lineage-overview
    baseURL: https://your-instance.alation.com/api/v1
    description: REST API for managing data lineage and dataflow objects in Alation. Supports creating, retrieving, updating, and deleting lineage paths between catalog objects.
  - aid: alation:governance-api
    name: Alation Governance API
    tags:
      - Data Governance
      - Business Glossary
      - Data Quality
      - Policies
    properties:
      - url: https://developer.alation.com
        type: Documentation
      - url: openapi/alation-governance-openapi.yaml
        type: OpenAPI
      - url: json-schema/alation-alation-governance-glossary-term-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-governance-policy-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-governance-data-quality-rule-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-governance-data-quality-score-schema.json
        type: JSONSchema
      - url: json-structure/alation-alation-governance-glossary-term-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-governance-policy-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-governance-data-quality-rule-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-governance-data-quality-score-structure.json
        type: JSONStructure
      - url: examples/alation-alation-governance-glossary-term-example.json
        type: Example
      - url: examples/alation-alation-governance-policy-example.json
        type: Example
      - url: examples/alation-alation-governance-data-quality-rule-example.json
        type: Example
      - url: examples/alation-alation-governance-data-quality-score-example.json
        type: Example
    humanURL: https://developer.alation.com
    baseURL: https://your-instance.alation.com/integration/v2
    description: REST API for data governance workflows in Alation, including business glossary management, governance policy enforcement, and data quality rules and scoring.
  - aid: alation:search-api
    name: Alation Search API
    tags:
      - Search
      - Data Discovery
      - AI
      - Catalog
    properties:
      - url: https://developer.alation.com
        type: Documentation
      - url: openapi/alation-search-openapi.yaml
        type: OpenAPI
      - url: json-schema/alation-alation-search-search-result-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-search-search-results-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-search-context-request-schema.json
        type: JSONSchema
      - url: json-schema/alation-alation-search-article-schema.json
        type: JSONSchema
      - url: json-structure/alation-alation-search-search-result-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-search-search-results-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-search-context-request-structure.json
        type: JSONStructure
      - url: json-structure/alation-alation-search-article-structure.json
        type: JSONStructure
      - url: examples/alation-alation-search-search-result-example.json
        type: Example
      - url: examples/alation-alation-search-search-results-example.json
        type: Example
      - url: examples/alation-alation-search-context-request-example.json
        type: Example
      - url: examples/alation-alation-search-article-example.json
        type: Example
    humanURL: https://developer.alation.com
    baseURL: https://your-instance.alation.com/integration/v2
    description: REST API for searching and discovering catalog assets in Alation. Supports full-text search, AI-powered aggregated context retrieval, and article browsing.
common:
  - url: https://alation.com
    type: Website
  - url: https://developer.alation.com
    type: Documentation
  - url: https://developer.alation.com/dev/docs/about-the-alation-apis
    type: GettingStarted
  - url: https://github.com/Alation
    type: GitHubOrganization
  - url: rules/alation-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/alation-vocabulary.yaml
    type: Vocabulary
  - url: json-ld/alation-alation-context.jsonld
    type: JSONLD
  - url: capabilities/shared/data-catalog-api.yaml
    type: NaftikoCapability
    title: Alation Data Catalog Shared Capability
  - url: capabilities/shared/lineage-api.yaml
    type: NaftikoCapability
    title: Alation Lineage Shared Capability
  - url: capabilities/shared/governance-api.yaml
    type: NaftikoCapability
    title: Alation Governance Shared Capability
  - url: capabilities/shared/search-api.yaml
    type: NaftikoCapability
    title: Alation Search Shared Capability
  - url: capabilities/data-intelligence.yaml
    type: NaftikoCapability
    title: Data Intelligence Workflow
  - type: Features
    data:
      - name: Data Catalog
        description: Centralized catalog for data sources, schemas, tables, and columns with rich metadata, descriptions, and custom fields for discoverability.
      - name: Data Lineage
        description: End-to-end data lineage tracking via dataflow objects showing how data moves between sources, transformations, and targets.
      - name: Business Glossary
        description: Collaborative business glossary for defining standardized terms, abbreviations, and synonyms with stewardship assignments.
      - name: Data Quality
        description: Comprehensive data quality rules covering accuracy, completeness, consistency, timeliness, uniqueness, validity, and custom dimensions.
      - name: Governance Policies
        description: Governance policy management for data protection, retention, access control, and quality enforcement across the enterprise.
      - name: AI-Powered Search
        description: Full-text and semantic search powered by AI for discovering trusted data assets, with aggregated context for LLM consumption.
      - name: Aggregated Context API
        description: Specialized API for AI applications to retrieve structured catalog context for natural language queries, enabling RAG and AI agent workflows.
      - name: Custom Fields
        description: Extensible metadata framework with custom fields for any catalog object type, supporting batch updates via the REST API.
  - type: UseCases
    data:
      - name: Enterprise Data Discovery
        description: Enable data teams to search and find trusted data assets across all data sources using metadata-enriched catalog browsing and search.
      - name: Data Governance Compliance
        description: Enforce data governance policies, maintain business glossaries, and track stewardship for regulatory compliance and data accountability.
      - name: AI Data Context
        description: Power AI applications with structured catalog context from the aggregated context API, enabling accurate data-aware LLM responses.
      - name: Data Lineage Auditing
        description: Track data flows between systems for compliance auditing, impact analysis, and root cause investigation of data quality issues.
      - name: Data Quality Management
        description: Define and score data quality rules across catalog objects for continuous quality monitoring and improvement workflows.
  - type: Integrations
    data:
      - name: Snowflake
        description: Native Snowflake integration for automatic metadata harvesting and query log analysis to build comprehensive data lineage.
      - name: dbt
        description: dbt integration for capturing transformation lineage and linking dbt models to physical tables in the Alation catalog.
      - name: Tableau
        description: BI metadata integration for cataloging Tableau reports and dashboards with lineage to underlying data sources.
      - name: Python SDK
        description: Official Python SDK and AI Agent SDK for programmatic access to Alation catalog APIs and AI agent development.
      - name: Apache Atlas
        description: Integration with Apache Atlas for federated metadata management across heterogeneous data platforms.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
