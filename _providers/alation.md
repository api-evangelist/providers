---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Alation Agentic Access
  operation_count: 30
  slug: alation-agentic-access
  summary_line: 30 operations · 10 acting
api_count: 12
apis:
- description: Retrieve aggregated context for AI applications
  name: Alation Aggregated Context API
  slug: alation-aggregated-context-api
- description: Retrieve column metadata
  name: Alation Columns API
  slug: alation-columns-api
- description: Manage custom field values
  name: Alation Custom Fields API
  slug: alation-custom-fields-api
- description: Manage data quality rules and scores
  name: Alation Data Quality API
  slug: alation-data-quality-api
- description: Manage data source connections
  name: Alation Data Sources API
  slug: alation-data-sources-api
- description: Manage dataflow lineage objects
  name: Alation Dataflows API
  slug: alation-dataflows-api
- description: Manage business glossary terms
  name: Alation Glossary Terms API
  slug: alation-glossary-terms-api
- description: Retrieve lineage paths between catalog objects
  name: Alation Lineage API
  slug: alation-lineage-api
- description: Manage data governance policies
  name: Alation Policies API
  slug: alation-policies-api
- description: Retrieve schema metadata
  name: Alation Schemas API
  slug: alation-schemas-api
- description: Search catalog assets
  name: Alation Search API
  slug: alation-search-api
- description: Retrieve table metadata
  name: Alation Tables API
  slug: alation-tables-api
artifact_total: 96
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alation Data Catalog Aggregated Context API
  slug: open-alation-aggregated-context-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Columns API
  slug: open-alation-columns-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Custom Fields API
  slug: open-alation-custom-fields-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Data Quality API
  slug: open-alation-data-quality-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Data Sources API
  slug: open-alation-data-sources-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Dataflows API
  slug: open-alation-dataflows-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Glossary Terms API
  slug: open-alation-glossary-terms-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Lineage API
  slug: open-alation-lineage-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Policies API
  slug: open-alation-policies-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Schemas API
  slug: open-alation-schemas-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Search API
  slug: open-alation-search-api
- collection_type: open
  name: Alation Data Catalog Aggregated Context Tables API
  slug: open-alation-tables-api
- collection_type: open
  name: API Collection
  slug: open-alation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/alation-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alation-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alation
- group: company
  title: ''
  type: Blog
  url: https://www.alation.com/blog/
- group: company
  title: ''
  type: Website
  url: https://alation.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.alation.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.alation.com/dev/docs/about-the-alation-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alation
- group: design
  title: ''
  type: SpectralRules
  url: rules/alation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/alation-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/alation-alation-context.jsonld
created: '2025-01-08'
description: Alation is a data intelligence platform that helps organizations harness the power of their data by providing a centralized platform for data cataloging, governance, and collaboration. By enabling users to easily search, understand, and trust their data, Alation empowers organizations to make data-driven decisions with confidence. Through advanced analytics and AI capabilities, Alation helps organizations uncover insights, improve data quality, and drive innovation.
examples:
- key_count: 9
  name: Alation Alation Data Catalog Column Example
  slug: alation-alation-data-catalog-column-example
- key_count: 5
  name: Alation Alation Data Catalog Custom Field Value Example
  slug: alation-alation-data-catalog-custom-field-value-example
- key_count: 8
  name: Alation Alation Data Catalog Data Source Example
  slug: alation-alation-data-catalog-data-source-example
- key_count: 6
  name: Alation Alation Data Catalog Schema Example
  slug: alation-alation-data-catalog-schema-example
- key_count: 8
  name: Alation Alation Data Catalog Table Example
  slug: alation-alation-data-catalog-table-example
- key_count: 7
  name: Alation Alation Governance Data Quality Rule Example
  slug: alation-alation-governance-data-quality-rule-example
- key_count: 5
  name: Alation Alation Governance Data Quality Score Example
  slug: alation-alation-governance-data-quality-score-example
- key_count: 9
  name: Alation Alation Governance Glossary Term Example
  slug: alation-alation-governance-glossary-term-example
- key_count: 7
  name: Alation Alation Governance Policy Example
  slug: alation-alation-governance-policy-example
- key_count: 8
  name: Alation Alation Lineage Dataflow Example
  slug: alation-alation-lineage-dataflow-example
- key_count: 2
  name: Alation Alation Lineage Lineage Graph Example
  slug: alation-alation-lineage-lineage-graph-example
- key_count: 7
  name: Alation Alation Search Article Example
  slug: alation-alation-search-article-example
- key_count: 3
  name: Alation Alation Search Context Request Example
  slug: alation-alation-search-context-request-example
- key_count: 7
  name: Alation Alation Search Search Result Example
  slug: alation-alation-search-search-result-example
- key_count: 2
  name: Alation Alation Search Search Results Example
  slug: alation-alation-search-search-results-example
features:
- description: Centralized catalog for data sources, schemas, tables, and columns with rich metadata, descriptions, and custom fields for discoverability.
  name: Data Catalog
- description: End-to-end data lineage tracking via dataflow objects showing how data moves between sources, transformations, and targets.
  name: Data Lineage
- description: Collaborative business glossary for defining standardized terms, abbreviations, and synonyms with stewardship assignments.
  name: Business Glossary
- description: Comprehensive data quality rules covering accuracy, completeness, consistency, timeliness, uniqueness, validity, and custom dimensions.
  name: Data Quality
- description: Governance policy management for data protection, retention, access control, and quality enforcement across the enterprise.
  name: Governance Policies
- description: Full-text and semantic search powered by AI for discovering trusted data assets, with aggregated context for LLM consumption.
  name: AI-Powered Search
- description: Specialized API for AI applications to retrieve structured catalog context for natural language queries, enabling RAG and AI agent workflows.
  name: Aggregated Context API
- description: Extensible metadata framework with custom fields for any catalog object type, supporting batch updates via the REST API.
  name: Custom Fields
finops:
- name: Alation Finops
  service_category: Data Intelligence Platform
  slug: alation-finops
graphqls:
- description: Alation is a data intelligence platform for data search and discovery. The API covers data source management, data objects (tables, columns, queries), catalog articles, lineage, governance policies, u
  name: Alation GraphQL API
  slug: alation-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alation.png
json_schemas:
- name: Column
  property_count: 9
  slug: alation-alation-data-catalog-column
- name: CustomFieldValue
  property_count: 5
  slug: alation-alation-data-catalog-custom-field-value
- name: DataSource
  property_count: 8
  slug: alation-alation-data-catalog-data-source
- name: Schema
  property_count: 6
  slug: alation-alation-data-catalog-schema
- name: Table
  property_count: 8
  slug: alation-alation-data-catalog-table
- name: DataQualityRule
  property_count: 7
  slug: alation-alation-governance-data-quality-rule
- name: DataQualityScore
  property_count: 5
  slug: alation-alation-governance-data-quality-score
- name: GlossaryTerm
  property_count: 9
  slug: alation-alation-governance-glossary-term
- name: Policy
  property_count: 7
  slug: alation-alation-governance-policy
- name: Dataflow
  property_count: 8
  slug: alation-alation-lineage-dataflow
- name: LineageGraph
  property_count: 2
  slug: alation-alation-lineage-lineage-graph
- name: Article
  property_count: 7
  slug: alation-alation-search-article
- name: ContextRequest
  property_count: 3
  slug: alation-alation-search-context-request
- name: SearchResult
  property_count: 7
  slug: alation-alation-search-search-result
- name: SearchResults
  property_count: 2
  slug: alation-alation-search-search-results
json_structures:
- name: Alation Alation Data Catalog Column Structure
  property_count: 9
  slug: alation-alation-data-catalog-column-structure
- name: Alation Alation Data Catalog Custom Field Value Structure
  property_count: 5
  slug: alation-alation-data-catalog-custom-field-value-structure
- name: Alation Alation Data Catalog Data Source Structure
  property_count: 8
  slug: alation-alation-data-catalog-data-source-structure
- name: Alation Alation Data Catalog Schema Structure
  property_count: 6
  slug: alation-alation-data-catalog-schema-structure
- name: Alation Alation Data Catalog Table Structure
  property_count: 8
  slug: alation-alation-data-catalog-table-structure
- name: Alation Alation Governance Data Quality Rule Structure
  property_count: 7
  slug: alation-alation-governance-data-quality-rule-structure
- name: Alation Alation Governance Data Quality Score Structure
  property_count: 5
  slug: alation-alation-governance-data-quality-score-structure
- name: Alation Alation Governance Glossary Term Structure
  property_count: 9
  slug: alation-alation-governance-glossary-term-structure
- name: Alation Alation Governance Policy Structure
  property_count: 7
  slug: alation-alation-governance-policy-structure
- name: Alation Alation Lineage Dataflow Structure
  property_count: 8
  slug: alation-alation-lineage-dataflow-structure
- name: Alation Alation Lineage Lineage Graph Structure
  property_count: 2
  slug: alation-alation-lineage-lineage-graph-structure
- name: Alation Alation Search Article Structure
  property_count: 7
  slug: alation-alation-search-article-structure
- name: Alation Alation Search Context Request Structure
  property_count: 3
  slug: alation-alation-search-context-request-structure
- name: Alation Alation Search Search Result Structure
  property_count: 7
  slug: alation-alation-search-search-result-structure
- name: Alation Alation Search Search Results Structure
  property_count: 2
  slug: alation-alation-search-search-results-structure
jsonld:
- class_count: 0
  name: Alation Alation Context
  property_count: 60
  slug: alation-alation-context
layout: provider
modified: '2026-05-19'
name: Alation
nav: Providers
network: true
overview: 'Alation publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Aggregated Context API, Columns API, Custom Fields API, and 9 more. Tagged areas include Data Catalog, Data Governance, Data Intelligence, Data Lineage, and Data Quality.


  The Alation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Alation''s developer surface includes authentication, engineering blog, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Alation Plans Pricing
  plan_count: 1
  slug: alation-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Alation Rate Limits
  slug: alation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Alation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: alation-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Alation API Rules
  rule_count: 32
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 15
  slug: alation-spectral-rules
score:
  band: thin
  composite: 38.0
  delta: -6.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 25.0
    contract_quality: 69.2
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/screenshots/alation-2026-06-20T171502.png
security:
- kind: authentication
  name: Alation Authentication
  slug: alation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alation Domain Security
  slug: alation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alation Vulnerability Disclosure
  slug: alation-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Alation Trust Center
  slug: alation-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP
slug: alation
tags:
- Data Catalog
- Data Governance
- Data Intelligence
- Data Lineage
- Data Quality
- Business Glossary
- Metadata Management
- AI
use_cases:
- description: Enable data teams to search and find trusted data assets across all data sources using metadata-enriched catalog browsing and search.
  name: Enterprise Data Discovery
- description: Enforce data governance policies, maintain business glossaries, and track stewardship for regulatory compliance and data accountability.
  name: Data Governance Compliance
- description: Power AI applications with structured catalog context from the aggregated context API, enabling accurate data-aware LLM responses.
  name: AI Data Context
- description: Track data flows between systems for compliance auditing, impact analysis, and root cause investigation of data quality issues.
  name: Data Lineage Auditing
- description: Define and score data quality rules across catalog objects for continuous quality monitoring and improvement workflows.
  name: Data Quality Management
website: https://alation.com
---
