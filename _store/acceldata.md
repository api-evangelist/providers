---
aid: acceldata
url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/apis.yml
name: Acceldata
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - Data Management
  - Data Observability
  - Data Pipeline
  - Data Quality
  - Intelligence
  - Observability
description: Acceldata is an agentic data management platform that helps enterprises monitor, govern, and optimize data across cloud, lakehouse, and hybrid environments. The platform combines AI-powered agents with data observability to proactively detect issues, trace root causes, and automate remediation workflows. Key products include ADM (Agentic Data Management), ADOC (Acceldata Data Observability Cloud), Pulse for Hadoop environments, and Agent Studio for building custom AI agents. It supports integrations with Snowflake, Databricks, AWS, GCP, Azure, and Hadoop.
created: '2025-02-24'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: acceldata:adoc-api
    name: Acceldata Data Observability Cloud API
    description: The ADOC API provides programmatic access to data observability features including alerts, data quality rules, pipeline monitoring, data lineage, users, groups, roles, and permissions within the Acceldata Data Observability Cloud platform.
    humanURL: https://docs.acceldata.io/api/introduction
    baseURL: https://api.acceldata.app/v1
    tags:
      - Data Observability
      - Data Quality
      - Alerts
      - Data Pipeline
    properties:
      - url: https://docs.acceldata.io/api/introduction
        type: Documentation
      - url: https://docs.acceldata.io/api/authentication
        type: Authentication
      - url: openapi/acceldata-adoc-api.yaml
        type: OpenAPI
      - url: json-schema/adoc-api-alert-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-alert-list-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-data-quality-rule-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-data-quality-rule-list-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-dataset-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-dataset-list-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-lineage-node-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-lineage-graph-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-pipeline-job-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-pipeline-job-list-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-user-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-user-list-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-role-schema.json
        type: JSONSchema
      - url: json-schema/adoc-api-role-list-schema.json
        type: JSONSchema
      - url: json-structure/adoc-api-alert-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-alert-list-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-data-quality-rule-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-data-quality-rule-list-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-dataset-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-dataset-list-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-lineage-node-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-lineage-graph-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-pipeline-job-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-pipeline-job-list-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-user-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-user-list-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-role-structure.json
        type: JSONStructure
      - url: json-structure/adoc-api-role-list-structure.json
        type: JSONStructure
      - url: examples/adoc-api-alert-example.json
        type: Example
      - url: examples/adoc-api-alert-list-example.json
        type: Example
      - url: examples/adoc-api-data-quality-rule-example.json
        type: Example
      - url: examples/adoc-api-dataset-example.json
        type: Example
      - url: examples/adoc-api-lineage-graph-example.json
        type: Example
      - url: examples/adoc-api-pipeline-job-example.json
        type: Example
      - url: examples/adoc-api-user-example.json
        type: Example
      - url: examples/adoc-api-role-example.json
        type: Example
common:
  - type: Website
    url: https://www.acceldata.io/
  - type: Portal
    url: https://accounts.acceldata.app/login
  - type: Documentation
    url: https://docs.acceldata.io/
  - type: GettingStarted
    url: https://docs.acceldata.io/api/introduction
  - type: Pricing
    url: https://www.acceldata.io/pricing
  - type: Blog
    url: https://www.acceldata.io/blog
  - type: PrivacyPolicy
    url: https://www.acceldata.io/privacy-policy
  - type: TermsOfService
    url: https://www.acceldata.io/terms-of-use
  - type: Features
    data:
      - name: Agentic Data Management
        description: AI-powered agents that proactively detect issues, trace root causes, and automate data quality remediation workflows
      - name: Data Quality Monitoring
        description: Multi-variate anomaly detection, column-level profiling, and proactive monitoring across all data platforms
      - name: Data Lineage
        description: End-to-end data lineage visualization with schema change management and column-level impact analysis
      - name: Pipeline Health Monitoring
        description: Real-time SLA monitoring, bottleneck identification, and root cause analysis for data pipelines
      - name: Data Cost Management
        description: Visibility into data spending, budget optimization, chargebacks, and cost forecasting across cloud environments
      - name: Business Notebook
        description: Natural language interface with contextual memory for querying data quality and observability insights
      - name: Agent Studio
        description: Low-code environment for building and deploying custom AI agents for data management workflows
      - name: BYOLLM Support
        description: Bring Your Own Large Language Model for enterprise-controlled AI inference within data operations
      - name: xLake Reasoning Engine
        description: Exabyte-scale, AI-aware processing engine supporting cloud hyperscalers and on-premises deployments
  - type: UseCases
    data:
      - name: Data Quality Assurance
        description: Continuously monitor and automatically remediate data quality issues across cloud and hybrid environments
      - name: Cloud Migration Validation
        description: Validate data completeness, consistency, and accuracy during cloud migration projects
      - name: AI and LLM Data Readiness
        description: Ensure data pipelines produce clean, reliable, and AI-ready datasets for training and inference
      - name: Cost Optimization and FinOps
        description: Identify and reduce wasteful data pipeline and infrastructure costs with granular usage analytics
      - name: Data Reconciliation
        description: Automatically detect and resolve discrepancies between source and target systems across platforms
      - name: Compliance and Data Governance
        description: Track data lineage and access patterns to support regulatory compliance and data governance programs
  - type: Integrations
    data:
      - name: Snowflake
        description: Native integration for monitoring Snowflake data quality, query performance, and cost optimization
      - name: Databricks
        description: Integration for observing Databricks lakehouse pipelines, job health, and data quality
      - name: AWS
        description: Support for AWS data services including S3, Redshift, Glue, EMR, and Athena
      - name: Google Cloud Platform
        description: Integration with GCP data services including BigQuery, Dataflow, and Cloud Storage
      - name: Microsoft Azure
        description: Integration with Azure Synapse, Azure Data Factory, and Azure Data Lake Storage
      - name: Hadoop / Apache
        description: Dedicated Pulse product for Hadoop ecosystem monitoring including HDFS, YARN, Hive, and Spark
  - url: rules/acceldata-spectral-rules.yml
    type: SpectralRules
  - url: capabilities/data-observability.yaml
    type: NaftikoCapability
  - url: vocabulary/acceldata-vocabulary.yaml
    type: Vocabulary
  - url: json-ld/acceldata-adoc-api-context.jsonld
    type: JSON-LD
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
