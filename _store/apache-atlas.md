---
aid: apache-atlas
name: Apache Atlas
description: Apache Atlas is a scalable and extensible set of core foundational data governance services developed by the Apache Software Foundation. It enables enterprises to effectively meet their compliance requirements within Hadoop and allows integration with the whole enterprise data ecosystem. Atlas provides metadata management, data classification, lineage tracking, business glossary, and a REST API for programmatic governance operations. It supports discovery, auditing, and policy management for enterprise data assets.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Big Data
  - Compliance
  - Data Governance
  - Data Lineage
  - Hadoop
  - Metadata
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-atlas/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-atlas:apache-atlas-rest-api
    name: Apache Atlas REST API
    description: The Atlas REST API provides endpoints for managing types, entities, lineage, discovery, and glossary resources, enabling programmatic metadata management and data governance operations. It covers entity CRUD, type definitions, basic and full-text search, lineage tracking, relationship management, and business glossary management.
    humanURL: https://atlas.apache.org/api/v2/index.html
    baseURL: http://localhost:21000/api/atlas
    tags:
      - Governance
      - Metadata
      - REST
    properties:
      - type: Documentation
        url: https://atlas.apache.org/api/v2/index.html
      - type: OpenAPI
        url: openapi/apache-atlas-rest-openapi.yaml
      - type: GettingStarted
        url: https://atlas.apache.org/quick_start_v2.html
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/atlas
  - type: Documentation
    url: https://atlas.apache.org/
  - type: GettingStarted
    url: https://atlas.apache.org/quick_start_v2.html
  - type: Support
    url: https://atlas.apache.org/mailing_list.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://github.com/apache/atlas/releases
  - type: SpectralRules
    url: rules/apache-atlas-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-atlas-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/atlas-data-governance.yaml
  - type: Features
    data:
      - name: Metadata Management
        description: Centrally manage metadata for enterprise data assets including Hive tables, HDFS files, Kafka topics, HBase tables, and Spark jobs.
      - name: Data Classification
        description: Apply classification tags to data assets for sensitivity classification (PII, PHI, confidential) and policy enforcement.
      - name: Data Lineage Tracking
        description: Automatically capture and visualize data lineage across data pipeline stages for impact analysis and compliance.
      - name: Business Glossary
        description: Manage a centralized business glossary of terms and categories to standardize data definitions across the organization.
      - name: REST API
        description: Comprehensive REST API for programmatic metadata management, discovery, lineage retrieval, and type definition management.
      - name: Search and Discovery
        description: Find data assets using basic, full-text, DSL, and attribute-based search across all registered metadata.
      - name: Policy-Based Data Access
        description: Integrate with Apache Ranger for attribute-based access control policies driven by Atlas classification tags.
      - name: Auditing
        description: Comprehensive audit trail of all metadata changes and entity operations for compliance and governance.
      - name: Hook-Based Metadata Collection
        description: Hooks for Hive, HBase, Sqoop, Storm, and other Hadoop ecosystem tools for automatic metadata harvesting.
      - name: Type System
        description: Extensible type system for defining custom entity types, classification types, and relationship types.
  - type: UseCases
    data:
      - name: Data Governance and Compliance
        description: Track data assets, apply classifications, and enforce policies for GDPR, HIPAA, and CCPA compliance.
      - name: Data Lineage Analysis
        description: Trace data from source to consumption to understand pipeline impact and debug data quality issues.
      - name: Metadata-Driven Data Discovery
        description: Enable data consumers to find relevant datasets using classification-based and attribute-based search.
      - name: Data Catalog Integration
        description: Serve as the metadata backbone for enterprise data catalogs and data mesh architectures.
      - name: Sensitive Data Identification
        description: Classify PII and sensitive data assets and integrate with Ranger for attribute-based access control.
      - name: Business Glossary Management
        description: Maintain standard business definitions and link them to technical metadata for consistent data interpretation.
  - type: Integrations
    data:
      - name: Apache Hive
        description: Native Hive hook for automatic metadata harvesting of Hive databases, tables, and query lineage.
      - name: Apache Ranger
        description: Integration with Ranger for policy-based data access control driven by Atlas classification tags.
      - name: Apache Kafka
        description: Kafka hook for tracking Kafka topics and message schema metadata.
      - name: Apache HBase
        description: HBase hook for capturing table and namespace metadata.
      - name: Apache Spark
        description: Spark integration for capturing dataset and job-level lineage from Spark applications.
      - name: Apache Sqoop
        description: Sqoop hook for importing relational database metadata and lineage into Atlas.
      - name: Cloudera Data Platform
        description: Native integration with Cloudera Data Platform (CDP) as the metadata management backbone.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
