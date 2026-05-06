---
aid: dbt
name: dbt
url: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/apis.yml
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics Engineering
  - Data
  - ELT
  - Metrics
  - Projects
  - SQL
  - Transformation
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: dbt Labs operates dbt Cloud, the managed platform for the open-source dbt (data build tool) used to transform data inside cloud warehouses. dbt Cloud exposes a set of APIs for managing accounts, projects, jobs, and runs programmatically (Administrative API), inspecting project metadata (Discovery API), and querying governed metrics (Semantic Layer API).
apis:
  - aid: dbt:dbt-cloud-administrative-api
    name: dbt Cloud Administrative API
    description: The dbt Cloud Administrative API manages accounts, projects, jobs, runs, environments, and other resources. It is the primary integration point for external orchestrators (Airflow, Dagster, Prefect) and for Terraform-based management of dbt Cloud configuration.
    humanURL: https://docs.getdbt.com/docs/dbt-cloud-apis/admin-cloud-api
    baseURL: https://cloud.getdbt.com/api/v3
    tags:
      - Accounts
      - Administration
      - Jobs
      - Projects
      - Runs
    properties:
      - type: Documentation
        url: https://docs.getdbt.com/docs/dbt-cloud-apis/admin-cloud-api
      - type: OpenAPI
        url: openapi/dbt-cloud-administrative-api-openapi.yml
      - type: JSONSchema
        url: json-schema/dbt-job.json
      - type: JSONSchema
        url: json-schema/dbt-run.json
      - type: Rules
        url: rules/dbt-cloud-administrative-api-rules.yml
      - type: Capabilities
        url: capabilities/dbt-cloud-administrative-api-capabilities.yml
  - aid: dbt:dbt-cloud-discovery-api
    name: dbt Cloud Discovery API
    description: Every time dbt Cloud runs a project, it generates and stores information about the project. The Discovery API exposes that metadata including details about models, sources, exposures, and execution results so teams can understand and govern their DAG.
    humanURL: https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-api
    baseURL: https://metadata.cloud.getdbt.com/graphql
    tags:
      - Discovery
      - GraphQL
      - Lineage
      - Metadata
    properties:
      - type: Documentation
        url: https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-api
      - type: OpenAPI
        url: openapi/dbt-cloud-discovery-api-openapi.yml
  - aid: dbt:dbt-cloud-semantic-layer-api
    name: dbt Cloud Semantic Layer API
    description: The dbt Semantic Layer lets teams define metrics in code with MetricFlow and query them consistently from BI tools, notebooks, and applications. The Semantic Layer API exposes metric and dimension queries via GraphQL, JDBC, and a Python SDK.
    humanURL: https://docs.getdbt.com/docs/dbt-cloud-apis/sl-api-overview
    baseURL: https://semantic-layer.cloud.getdbt.com/api/graphql
    tags:
      - Dimensions
      - GraphQL
      - JDBC
      - MetricFlow
      - Metrics
      - Semantic Layer
    properties:
      - type: Documentation
        url: https://docs.getdbt.com/docs/dbt-cloud-apis/sl-api-overview
      - type: OpenAPI
        url: openapi/dbt-cloud-semantic-layer-api-openapi.yml
common:
  - type: Website
    url: https://www.getdbt.com/
  - type: Documentation
    url: https://docs.getdbt.com/
  - type: Portal
    url: https://docs.getdbt.com/docs/dbt-cloud-apis/overview
  - type: Authentication
    url: https://docs.getdbt.com/docs/dbt-cloud-apis/authentication
  - type: Pricing
    url: https://www.getdbt.com/pricing
  - type: GitHub
    url: https://github.com/dbt-labs/dbt-core
  - type: SDK
    url: https://docs.getdbt.com/docs/dbt-cloud-apis/sl-python
  - type: Terms of Service
    url: https://www.getdbt.com/cloud/terms
  - type: Privacy Policy
    url: https://www.getdbt.com/cloud/privacy-policy
  - type: JSON-LD
    url: json-ld/dbt-context.jsonld
  - type: Vocabulary
    url: vocabulary/dbt-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
