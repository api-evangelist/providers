---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Atlas Agentic Access
  operation_count: 12
  slug: apache-atlas-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 6
apis:
- description: Search and discover metadata entities using various search strategies.
  name: Apache Atlas Discovery API
  slug: apache-atlas-discovery-api
- description: Manage metadata entities (CRUD operations on Atlas entities).
  name: Apache Atlas Entities API
  slug: apache-atlas-entities-api
- description: Manage business glossary terms and categories.
  name: Apache Atlas Glossary API
  slug: apache-atlas-glossary-api
- description: Track data lineage and provenance between entities.
  name: Apache Atlas Lineage API
  slug: apache-atlas-lineage-api
- description: Manage relationships between entities.
  name: Apache Atlas Relationships API
  slug: apache-atlas-relationships-api
- description: Manage type definitions including entity types, classifications, and relationships.
  name: Apache Atlas Types API
  slug: apache-atlas-types-api
artifact_total: 85
collections:
- collection_type: postman
  name: Apache Atlas REST Discovery API
  slug: postman-apache-atlas-discovery-api
- collection_type: postman
  name: Apache Atlas REST Discovery Entities API
  slug: postman-apache-atlas-entities-api
- collection_type: postman
  name: Apache Atlas REST Discovery Glossary API
  slug: postman-apache-atlas-glossary-api
- collection_type: postman
  name: Apache Atlas REST Discovery Lineage API
  slug: postman-apache-atlas-lineage-api
- collection_type: postman
  name: Apache Atlas REST Discovery Relationships API
  slug: postman-apache-atlas-relationships-api
- collection_type: postman
  name: Apache Atlas REST Discovery Types API
  slug: postman-apache-atlas-types-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Atlas REST Discovery API
  slug: open-apache-atlas-discovery-api
- collection_type: open
  name: Apache Atlas REST Discovery Entities API
  slug: open-apache-atlas-entities-api
- collection_type: open
  name: Apache Atlas REST Discovery Glossary API
  slug: open-apache-atlas-glossary-api
- collection_type: open
  name: Apache Atlas REST Discovery Lineage API
  slug: open-apache-atlas-lineage-api
- collection_type: open
  name: Apache Atlas REST Discovery Relationships API
  slug: open-apache-atlas-relationships-api
- collection_type: open
  name: Apache Atlas REST Discovery Types API
  slug: open-apache-atlas-types-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/atlas/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-atlas/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-atlas-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-atlas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-atlas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-atlas-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/atlas
- group: docs
  title: ''
  type: Documentation
  url: https://atlas.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://atlas.apache.org/quick_start_v2.html
- group: operate
  title: ''
  type: Support
  url: https://atlas.apache.org/mailing_list.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apache/atlas/releases
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-atlas-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-atlas-vocabulary.yaml
created: '2026-03-16'
description: Apache Atlas is a scalable and extensible set of core foundational data governance services developed by the Apache Software Foundation. It enables enterprises to effectively meet their compliance requirements within Hadoop and allows integration with the whole enterprise data ecosystem. Atlas provides metadata management, data classification, lineage tracking, business glossary, and a REST API for programmatic governance operations. It supports discovery, auditing, and policy management for enterprise data assets.
examples:
- key_count: 2
  name: Atlas Atlas Entities With Ext Info Example
  slug: atlas-atlas-entities-with-ext-info-example
- key_count: 6
  name: Atlas Atlas Entity Example
  slug: atlas-atlas-entity-example
- key_count: 2
  name: Atlas Atlas Entity With Ext Info Example
  slug: atlas-atlas-entity-with-ext-info-example
- key_count: 3
  name: Atlas Atlas Error Response Example
  slug: atlas-atlas-error-response-example
- key_count: 6
  name: Atlas Atlas Glossary Example
  slug: atlas-atlas-glossary-example
- key_count: 5
  name: Atlas Atlas Lineage Info Example
  slug: atlas-atlas-lineage-info-example
- key_count: 5
  name: Atlas Atlas Relationship Example
  slug: atlas-atlas-relationship-example
- key_count: 4
  name: Atlas Atlas Search Result Example
  slug: atlas-atlas-search-result-example
- key_count: 5
  name: Atlas Atlas Types Def Example
  slug: atlas-atlas-types-def-example
- key_count: 2
  name: Atlas Entity Mutation Response Example
  slug: atlas-entity-mutation-response-example
- key_count: 2
  name: Atlas Entity With Ext Info Example
  slug: atlas-entity-with-ext-info-example
features:
- description: Centrally manage metadata for enterprise data assets including Hive tables, HDFS files, Kafka topics, HBase tables, and Spark jobs.
  name: Metadata Management
- description: Apply classification tags to data assets for sensitivity classification (PII, PHI, confidential) and policy enforcement.
  name: Data Classification
- description: Automatically capture and visualize data lineage across data pipeline stages for impact analysis and compliance.
  name: Data Lineage Tracking
- description: Manage a centralized business glossary of terms and categories to standardize data definitions across the organization.
  name: Business Glossary
- description: Comprehensive REST API for programmatic metadata management, discovery, lineage retrieval, and type definition management.
  name: REST API
- description: Find data assets using basic, full-text, DSL, and attribute-based search across all registered metadata.
  name: Search and Discovery
- description: Integrate with Apache Ranger for attribute-based access control policies driven by Atlas classification tags.
  name: Policy-Based Data Access
- description: Comprehensive audit trail of all metadata changes and entity operations for compliance and governance.
  name: Auditing
- description: Hooks for Hive, HBase, Sqoop, Storm, and other Hadoop ecosystem tools for automatic metadata harvesting.
  name: Hook-Based Metadata Collection
- description: Extensible type system for defining custom entity types, classification types, and relationship types.
  name: Type System
finops:
- name: Apache Atlas Finops
  service_category: API
  slug: apache-atlas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-atlas.png
integrations:
- description: Native Hive hook for automatic metadata harvesting of Hive databases, tables, and query lineage.
  name: Apache Hive
- description: Integration with Ranger for policy-based data access control driven by Atlas classification tags.
  name: Apache Ranger
- description: Kafka hook for tracking Kafka topics and message schema metadata.
  name: Apache Kafka
- description: HBase hook for capturing table and namespace metadata.
  name: Apache HBase
- description: Spark integration for capturing dataset and job-level lineage from Spark applications.
  name: Apache Spark
- description: Sqoop hook for importing relational database metadata and lineage into Atlas.
  name: Apache Sqoop
- description: Native integration with Cloudera Data Platform (CDP) as the metadata management backbone.
  name: Cloudera Data Platform
json_schemas:
- name: AtlasEntitiesWithExtInfo
  property_count: 2
  slug: atlas-atlas-entities-with-ext-info
- name: AtlasEntity
  property_count: 6
  slug: atlas-atlas-entity
- name: AtlasEntityWithExtInfo
  property_count: 2
  slug: atlas-atlas-entity-with-ext-info
- name: AtlasErrorResponse
  property_count: 3
  slug: atlas-atlas-error-response
- name: AtlasGlossary
  property_count: 6
  slug: atlas-atlas-glossary
- name: AtlasLineageInfo
  property_count: 5
  slug: atlas-atlas-lineage-info
- name: AtlasRelationship
  property_count: 5
  slug: atlas-atlas-relationship
- name: AtlasSearchResult
  property_count: 4
  slug: atlas-atlas-search-result
- name: AtlasTypesDef
  property_count: 5
  slug: atlas-atlas-types-def
- name: EntityMutationResponse
  property_count: 2
  slug: atlas-entity-mutation-response
- name: EntityWithExtInfo
  property_count: 2
  slug: atlas-entity-with-ext-info
json_structures:
- name: Atlas Atlas Entities With Ext Info Structure
  property_count: 2
  slug: atlas-atlas-entities-with-ext-info-structure
- name: Atlas Atlas Entity Structure
  property_count: 6
  slug: atlas-atlas-entity-structure
- name: Atlas Atlas Entity With Ext Info Structure
  property_count: 2
  slug: atlas-atlas-entity-with-ext-info-structure
- name: Atlas Atlas Error Response Structure
  property_count: 3
  slug: atlas-atlas-error-response-structure
- name: Atlas Atlas Glossary Structure
  property_count: 6
  slug: atlas-atlas-glossary-structure
- name: Atlas Atlas Lineage Info Structure
  property_count: 5
  slug: atlas-atlas-lineage-info-structure
- name: Atlas Atlas Relationship Structure
  property_count: 5
  slug: atlas-atlas-relationship-structure
- name: Atlas Atlas Search Result Structure
  property_count: 4
  slug: atlas-atlas-search-result-structure
- name: Atlas Atlas Types Def Structure
  property_count: 5
  slug: atlas-atlas-types-def-structure
- name: Atlas Entity Mutation Response Structure
  property_count: 2
  slug: atlas-entity-mutation-response-structure
- name: Atlas Entity With Ext Info Structure
  property_count: 2
  slug: atlas-entity-with-ext-info-structure
jsonld:
- class_count: 11
  name: Apache Atlas Context
  property_count: 34
  slug: apache-atlas-context
layout: provider
modified: '2026-05-19'
name: Apache Atlas
nav: Providers
network: true
overview: 'Apache Atlas publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Entities API, Glossary API, and 3 more. Tagged areas include Apache, Big Data, Compliance, Data Governance, and Data Lineage.


  The Apache Atlas catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Atlas'' developer surface includes authentication, documentation, getting-started guide, support, changelog, and 11 more developer resources.'
plans:
- name: Apache Atlas Plans Pricing
  plan_count: 3
  slug: apache-atlas-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Apache Atlas Rate Limits
  slug: apache-atlas-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Atlas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-atlas-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Apache Atlas API Rules
  rule_count: 20
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 12
  slug: apache-atlas-spectral-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 21.2
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-atlas/refs/heads/main/screenshots/apache-atlas-2026-06-20T172046.png
security:
- kind: authentication
  name: Apache Atlas Authentication
  slug: apache-atlas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Atlas Domain Security
  slug: apache-atlas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Atlas Vulnerability Disclosure
  slug: apache-atlas-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-atlas
tags:
- Apache
- Big Data
- Compliance
- Data Governance
- Data Lineage
- Hadoop
- Metadata
- Open-Source
use_cases:
- description: Track data assets, apply classifications, and enforce policies for GDPR, HIPAA, and CCPA compliance.
  name: Data Governance and Compliance
- description: Trace data from source to consumption to understand pipeline impact and debug data quality issues.
  name: Data Lineage Analysis
- description: Enable data consumers to find relevant datasets using classification-based and attribute-based search.
  name: Metadata-Driven Data Discovery
- description: Serve as the metadata backbone for enterprise data catalogs and data mesh architectures.
  name: Data Catalog Integration
- description: Classify PII and sensitive data assets and integrate with Ranger for attribute-based access control.
  name: Sensitive Data Identification
- description: Maintain standard business definitions and link them to technical metadata for consistent data interpretation.
  name: Business Glossary Management
---
