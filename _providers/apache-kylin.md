---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apache Kylin Agentic Access
  operation_count: 11
  slug: apache-kylin-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 7
apis:
- description: The Kylin JDBC driver provides SQL-over-Kylin access for BI tools and SQL clients, enabling standard JDBC connectivity to Kylin OLAP cubes.
  name: Apache Kylin JDBC Driver
  slug: jdbc-driver
- description: User authentication
  name: Apache Kylin Authentication API
  slug: apache-kylin-authentication-api
- description: Build job management
  name: Apache Kylin Jobs API
  slug: apache-kylin-jobs-api
- description: Data model management
  name: Apache Kylin Models API
  slug: apache-kylin-models-api
- description: Project management
  name: Apache Kylin Projects API
  slug: apache-kylin-projects-api
- description: SQL query execution
  name: Apache Kylin Query API
  slug: apache-kylin-query-api
- description: Table and datasource management
  name: Apache Kylin Tables API
  slug: apache-kylin-tables-api
artifact_total: 59
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-kylin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-kylin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-kylin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-kylin-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/kylin
- group: docs
  title: ''
  type: Documentation
  url: https://kylin.apache.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://kylin.apache.org/docs/tutorial/kylin_sample.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://kylin.apache.org/download/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-kylin-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-kylin-vocabulary.yaml
created: '2026-03-16'
description: Apache Kylin is an open-source distributed analytics engine designed to provide a SQL interface and multi-dimensional analysis (OLAP) on large-scale datasets. It provides sub-second query latency on trillion-record datasets via pre-computed cubes and works on top of Hadoop, Spark, and cloud storage.
examples:
- key_count: 2
  name: Rest Api Auth Response Example
  slug: rest-api-auth-response-example
- key_count: 9
  name: Rest Api Job Example
  slug: rest-api-job-example
- key_count: 4
  name: Rest Api Model Example
  slug: rest-api-model-example
- key_count: 3
  name: Rest Api Project Example
  slug: rest-api-project-example
- key_count: 2
  name: Rest Api Project Request Example
  slug: rest-api-project-request-example
- key_count: 5
  name: Rest Api Query Request Example
  slug: rest-api-query-request-example
- key_count: 10
  name: Rest Api Query Response Example
  slug: rest-api-query-response-example
- key_count: 4
  name: Rest Api Table Example
  slug: rest-api-table-example
features:
- description: Pre-computed cubes enable sub-second query response on trillion-record datasets.
  name: Sub-Second OLAP Queries
- description: ANSI SQL interface for business analysts using existing SQL skills.
  name: SQL Interface
- description: Build cubes with aggregates pre-calculated for instant query response.
  name: Cube Pre-computation
- description: Works on top of Hadoop, Spark, and cloud object storage.
  name: Hadoop and Cloud Integration
- description: Standard JDBC and ODBC drivers for BI tool integration.
  name: JDBC/ODBC Drivers
- description: Incremental cube building with date-range segment management.
  name: Segment Management
- description: Project-based multi-tenancy for isolating datasets and access.
  name: Multi-Tenancy
finops:
- name: Apache Kylin Finops
  service_category: API
  slug: apache-kylin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-kylin.png
integrations:
- description: Reads from HDFS and executes MapReduce cube builds on Hadoop.
  name: Apache Hadoop
- description: Spark-based cube building for faster and more efficient data processing.
  name: Apache Spark
- description: Hive metastore integration for table schema and metadata.
  name: Apache Hive
- description: HBase storage for pre-computed cube data.
  name: Apache HBase
- description: Native Tableau connector via Kylin JDBC driver.
  name: Tableau
- description: Apache Superset integration via JDBC for self-service analytics.
  name: Apache Superset
- type: Blog
  url: https://kylin.apache.org/blog/rss.xml
json_schemas:
- name: AuthResponse
  property_count: 2
  slug: rest-api-auth-response
- name: Job
  property_count: 9
  slug: rest-api-job
- name: Model
  property_count: 4
  slug: rest-api-model
- name: ProjectRequest
  property_count: 2
  slug: rest-api-project-request
- name: Project
  property_count: 3
  slug: rest-api-project
- name: QueryRequest
  property_count: 5
  slug: rest-api-query-request
- name: QueryResponse
  property_count: 10
  slug: rest-api-query-response
- name: Table
  property_count: 4
  slug: rest-api-table
json_structures:
- name: Rest Api Auth Response Structure
  property_count: 2
  slug: rest-api-auth-response-structure
- name: Rest Api Job Structure
  property_count: 9
  slug: rest-api-job-structure
- name: Rest Api Model Structure
  property_count: 4
  slug: rest-api-model-structure
- name: Rest Api Project Request Structure
  property_count: 2
  slug: rest-api-project-request-structure
- name: Rest Api Project Structure
  property_count: 3
  slug: rest-api-project-structure
- name: Rest Api Query Request Structure
  property_count: 5
  slug: rest-api-query-request-structure
- name: Rest Api Query Response Structure
  property_count: 10
  slug: rest-api-query-response-structure
- name: Rest Api Table Structure
  property_count: 4
  slug: rest-api-table-structure
jsonld:
- class_count: 10
  name: Apache Kylin Rest Api Context
  property_count: 29
  slug: apache-kylin-rest-api-context
layout: provider
modified: '2026-05-19'
name: Apache Kylin
nav: Providers
network: true
overview: 'Apache Kylin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Jobs API, Models API, and 3 more. Tagged areas include Analytics, Big Data, Cube, OLAP, and Open Source.


  The Apache Kylin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Kylin''s developer surface includes authentication, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Apache Kylin Plans Pricing
  plan_count: 3
  slug: apache-kylin-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Apache Kylin Rate Limits
  slug: apache-kylin-rate-limits
rules:
- name: Apache Kylin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-kylin-jsonschema-spectral-rules
- name: Apache Kylin API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 6
  slug: apache-kylin-spectral-rules
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.9
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-kylin/refs/heads/main/screenshots/apache-kylin-2026-06-20T172119.png
security:
- kind: authentication
  name: Apache Kylin Authentication
  slug: apache-kylin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Kylin Domain Security
  slug: apache-kylin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Kylin Vulnerability Disclosure
  slug: apache-kylin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-kylin
tags:
- Analytics
- Big Data
- Cube
- OLAP
- Open Source
- SQL
use_cases:
- description: Accelerate slow Hive or Spark queries with Kylin cube pre-computation.
  name: Data Warehouse Query Acceleration
- description: Connect Tableau, PowerBI, and Superset to Kylin via JDBC for analytics.
  name: BI Tool Integration
- description: Stream data into Kylin incrementally for near-real-time OLAP analytics.
  name: Real-Time OLAP
- description: Generate business reports over trillion-record datasets in seconds.
  name: Large-Scale Reporting
---
