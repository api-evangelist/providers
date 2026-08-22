---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Apache Sqoop provides a command-line interface for bulk data transfer between Hadoop and relational databases. Commands include sqoop-import for loading data into HDFS or Hive, sqoop-export for writin
  name: Apache Sqoop CLI
  slug: apache-sqoop-cli
artifact_total: 17
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/sqoop/blob/trunk/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-sqoop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-sqoop-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/sqoop
- group: docs
  title: ''
  type: Documentation
  url: https://sqoop.apache.org/docs/1.4.7/
- group: start
  title: ''
  type: Portal
  url: https://sqoop.apache.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: 'Apache Sqoop is a command-line tool designed for efficiently transferring bulk data between Apache Hadoop and structured data stores such as relational databases. It supports parallel import and export of data, incremental loads, and direct database connectors for MySQL, PostgreSQL, Oracle, SQL Server, and DB2. Note: Apache Sqoop has been retired to the Apache Attic as of 2021. Users are encouraged to migrate to Apache Spark or Apache NiFi.'
features:
- description: High-throughput parallel import from RDBMS to HDFS, Hive, or HBase.
  name: Bulk Import
- description: Export data from HDFS back to relational database tables.
  name: Bulk Export
- description: Delta-based incremental loading using append or lastmodified strategies.
  name: Incremental Loads
- description: Native database utility-based transfers for MySQL and PostgreSQL.
  name: Direct Import Mode
- description: Auto-create Hive tables and load imported data directly into Hive.
  name: Hive Integration
finops:
- name: Apache Sqoop Finops
  service_category: API
  slug: apache-sqoop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-sqoop.png
integrations:
- description: Primary target storage for Sqoop imports via HDFS.
  name: Apache Hadoop
- description: Create and populate Hive tables from RDBMS imports.
  name: Apache Hive
- description: MySQL JDBC and direct mysqldump-based connector.
  name: MySQL
- description: Oracle JDBC connector for enterprise database data transfer.
  name: Oracle
layout: provider
modified: '2026-04-19'
name: Apache Sqoop
nav: Providers
network: true
overview: 'Apache Sqoop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Big Data, Data Transfer, ETL, Hadoop, and RDBMS.


  Apache Sqoop''s developer surface includes documentation, developer portal, and 6 more developer resources.'
plans:
- name: Apache Sqoop Plans Pricing
  plan_count: 3
  slug: apache-sqoop-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Apache Sqoop Rate Limits
  slug: apache-sqoop-rate-limits
score:
  band: emerging
  composite: 16.0
  delta: 0.3
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-sqoop/refs/heads/main/screenshots/apache-sqoop-2026-06-20T172147.png
security:
- kind: domain-security
  name: Apache Sqoop Domain Security
  slug: apache-sqoop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Sqoop Vulnerability Disclosure
  slug: apache-sqoop-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-sqoop
tags:
- Big Data
- Data Transfer
- ETL
- Hadoop
- RDBMS
- Retired
use_cases:
- description: Load relational database data into Hadoop-based data warehouses.
  name: Data Warehouse Loading
- description: Move historical data from RDBMS to HDFS for cost-effective storage.
  name: Database Offloading
website: https://sqoop.apache.org/
---
