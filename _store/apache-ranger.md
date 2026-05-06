---
aid: apache-ranger
name: Apache Ranger
description: Apache Ranger is a framework to enable, monitor, and manage comprehensive data security across the Hadoop platform. It provides centralized security administration for fine-grained authorization policies across Hadoop ecosystem components.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Control
  - Authorization
  - Hadoop
  - Policy Management
  - Security
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-ranger/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-ranger:apache-ranger-rest-api
    name: Apache Ranger REST API
    description: The Ranger REST API provides endpoints for policy management, service management, user/group management, audit log retrieval, and security zone administration, with plugin APIs for enforcing policies in HDFS, Hive, HBase, and other services.
    humanURL: https://ranger.apache.org/apidocs/index.html
    tags:
      - Access Control
      - Policy Management
      - REST
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://ranger.apache.org/apidocs/index.html
      - type: Documentation
        url: https://ranger.apache.org/
      - type: OpenAPI
        url: openapi/apache-ranger-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/ranger
  - type: Documentation
    url: https://ranger.apache.org/
  - type: SpectralRules
    url: rules/apache-ranger-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-ranger-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ranger-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-ranger-context.jsonld
  - type: Features
    data:
      - name: Centralized Policy Management
        description: Manage security policies for all Hadoop services from a single interface
      - name: Fine-Grained Access Control
        description: Column-level, row-level, and data masking policies for Hive and HBase
      - name: Attribute-Based Access Control
        description: Context-aware policies based on user attributes and tag classifications
      - name: Audit Logging
        description: Comprehensive audit trail of all resource access events
      - name: Multi-Service Support
        description: Supports HDFS, Hive, HBase, Kafka, Storm, Solr, Kudu, and more
      - name: LDAP/AD Integration
        description: Sync users and groups from Active Directory or LDAP
      - name: Security Zones
        description: Delegate policy administration with security zones
  - type: UseCases
    data:
      - name: Data Lake Security
        description: Enforce column and row-level security on Hadoop data lake
      - name: Regulatory Compliance
        description: Meet GDPR, HIPAA, and SOX requirements with audit logs and masking
      - name: Multi-Tenant Authorization
        description: Isolate access between teams and business units
      - name: Kafka Topic Authorization
        description: Control which applications can produce and consume Kafka topics
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Native HDFS and YARN authorization integration
      - name: Apache Hive
        description: Column-level and row-level security for Hive queries
      - name: Apache HBase
        description: Table and column family security for HBase
      - name: Apache Kafka
        description: Topic-level authorization for Kafka producers and consumers
      - name: Apache Atlas
        description: Tag-based policies using Atlas data classifications
---
