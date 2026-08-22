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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 2
  name: Apache Zeppelin Agentic Access
  operation_count: 31
  slug: apache-zeppelin-agentic-access
  summary_line: 31 operations · 20 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Notebook API from Apache Zeppelin — 18 operation(s) for notebook.
  name: Apache Zeppelin Notebook API
  slug: apache-zeppelin-notebook-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Zeppelin REST Notebook API
  slug: open-apache-zeppelin-notebook-api
- collection_type: open
  name: Apache Zeppelin Notebook REST API
  slug: open-apache-zeppelin
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/zeppelin/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/zeppelin/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-zeppelin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-zeppelin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-zeppelin-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/zeppelin
- group: docs
  title: ''
  type: Documentation
  url: https://zeppelin.apache.org/docs/latest/
- group: start
  title: ''
  type: Portal
  url: https://zeppelin.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://zeppelin.apache.org/docs/latest/quickstart/install.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/zeppelin/releases
- group: operate
  title: ''
  type: Support
  url: https://zeppelin.apache.org/community.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: Apache Zeppelin is a web-based notebook that enables data-driven, interactive data analytics and collaborative documents with SQL, Scala, Python, R, and more. It provides built-in data visualization, collaboration features, and interpreter integration with Apache Spark, JDBC, Python, R, Shell, and 20+ other backends. Zeppelin exposes a REST API for notebook management, interpreter configuration, and job execution. It is maintained by the Apache Software Foundation.
features:
- description: Execute code in Scala, Python, R, SQL, Shell, and 20+ languages in the same notebook.
  name: Multi-Language Support
- description: Bar, line, pie, scatter, and map charts from query results without additional tools.
  name: Built-In Visualization
- description: Real-time collaborative editing of notebooks with user management and permissions.
  name: Collaborative Notebooks
- description: Native Apache Spark interpreter for Scala, Python (PySpark), and SQL queries.
  name: Spark Integration
- description: Universal JDBC interpreter for any SQL database including MySQL, PostgreSQL, Hive.
  name: JDBC Interpreter
- description: Schedule notebook paragraphs with cron expressions for automated execution.
  name: Paragraph Scheduling
- description: Interactive input forms within notebook paragraphs for parameterized execution.
  name: Dynamic Forms
finops:
- name: Apache Zeppelin Finops
  service_category: API
  slug: apache-zeppelin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-zeppelin.png
integrations:
- description: Native Spark interpreter for Scala, PySpark, and SparkSQL workloads.
  name: Apache Spark
- description: Hive JDBC and HiveQL interpreter for Hive data warehouse queries.
  name: Apache Hive
- description: Apache Flink interpreter for stream processing in Zeppelin notebooks.
  name: Apache Flink
- description: Zeppelin on Kubernetes with per-notebook pod isolation for interpreter processes.
  name: Kubernetes
- description: Elasticsearch interpreter for indexing and querying Elasticsearch data.
  name: Elasticsearch
layout: provider
modified: '2026-05-19'
name: Apache Zeppelin
nav: Providers
network: true
overview: 'Apache Zeppelin publishes 1 API on the [APIs.io](https://apis.io/) network: Notebook API. Tagged areas include Data Analytics, Interactive Computing, Notebook, Visualization, and Open Source.


  Apache Zeppelin''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 8 more developer resources.'
plans:
- name: Apache Zeppelin Plans Pricing
  plan_count: 3
  slug: apache-zeppelin-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Apache Zeppelin Rate Limits
  slug: apache-zeppelin-rate-limits
score:
  band: thin
  composite: 32.6
  delta: 0.9
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 39.2
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-zeppelin/refs/heads/main/screenshots/apache-zeppelin-2026-06-20T172200.png
security:
- kind: domain-security
  name: Apache Zeppelin Domain Security
  slug: apache-zeppelin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Zeppelin Vulnerability Disclosure
  slug: apache-zeppelin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-zeppelin
tags:
- Data Analytics
- Interactive Computing
- Notebook
- Visualization
- Open Source
use_cases:
- description: Exploratory data analysis with Spark SQL, Python, and R in a collaborative notebook.
  name: Interactive Data Exploration
- description: Rapid ML prototyping and model development with live results visualization.
  name: Data Science Prototyping
- description: Interactive SQL queries against Hive, Spark SQL, or any JDBC database.
  name: SQL Analytics
- description: Scheduled notebook execution for automated data report generation.
  name: Automated Reporting
website: https://zeppelin.apache.org/
---
