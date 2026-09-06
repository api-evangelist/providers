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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apache Spark Agentic Access
  operation_count: 26
  slug: apache-spark-agentic-access
  summary_line: 26 operations
api_count: 6
apis:
- description: Spark module for structured data processing with DataFrame and Dataset APIs. Provides a SQL interface and supports various data sources including Parquet, ORC, JSON, CSV, JDBC, Hive, and Delta Lake. T
  name: Apache Spark SQL API
  slug: apache-spark-sql-api
- description: Scalable, high-throughput, fault-tolerant stream processing of live data streams. Supports Structured Streaming (the newer DStream-based API) with exactly-once semantics, continuous processing mode, a
  name: Apache Spark Streaming API
  slug: apache-spark-streaming-api
- description: Spark's scalable machine learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, a
  name: Apache Spark MLlib API
  slug: apache-spark-mllib-api
- description: Spark API for graphs and graph-parallel computation with a collection of graph algorithms and builders, including PageRank, Connected Components, Triangle Counting, and shortest paths.
  name: Apache Spark GraphX API
  slug: apache-spark-graphx-api
- baseURL: http://localhost:4040/api/v1
  baseurl_source: spec
  description: The Applications API from Apache Spark — 25 operation(s) for applications.
  name: Apache Spark Applications API
  slug: apache-spark-applications-api
- baseURL: http://localhost:4040/api/v1
  baseurl_source: spec
  description: The Version API from Apache Spark — 1 operation(s) for version.
  name: Apache Spark Version API
  slug: apache-spark-version-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Spark Monitoring REST Applications API
  slug: open-apache-spark-applications-api
- collection_type: open
  name: Apache Spark Monitoring REST Applications Version API
  slug: open-apache-spark-version-api
- collection_type: open
  name: Apache Spark Monitoring REST API
  slug: open-apache-spark
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/spark/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/spark/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/spark/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/spark/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-spark-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-spark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-spark-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apachespark
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/spark
- group: start
  title: ''
  type: Portal
  url: https://spark.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://spark.apache.org/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://spark.apache.org/docs/latest/quick-start.html
- group: company
  title: ''
  type: Blog
  url: https://spark.apache.org/news/
- group: operate
  title: ''
  type: Support
  url: https://spark.apache.org/community.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apache-spark
- group: build
  title: PySpark (Python)
  type: SDKs
  url: https://pypi.org/project/pyspark/
- group: build
  title: Maven (Scala/Java)
  type: SDKs
  url: https://search.maven.org/search?q=g:org.apache.spark
created: '2024-01-01'
description: Apache Spark is a unified analytics engine for large-scale data processing. It provides high-level APIs in Java, Scala, Python, and R, and an optimized engine that supports general execution graphs. Spark offers a comprehensive suite of APIs for batch processing, SQL queries, streaming analytics, machine learning, and graph computation, governed by the Apache Software Foundation.
features:
- description: Single engine for batch, streaming, SQL, ML, and graph processing workloads.
  name: Unified Analytics Engine
- description: Optimized execution plans with Catalyst optimizer and DAG scheduling.
  name: Lazy Evaluation and DAG Execution
- description: Up to 100x faster than Hadoop MapReduce for iterative algorithms via in-memory caching.
  name: In-Memory Processing
- description: Unified streaming and batch processing with exactly-once semantics and Kafka integration.
  name: Structured Streaming
- description: High-level APIs in Scala, Java, Python (PySpark), and R (SparkR).
  name: Multi-Language Support
- description: ACID transactions, schema evolution, and time travel for data lakes.
  name: Delta Lake Integration
- description: Native Kubernetes scheduling for cloud-native deployment of Spark workloads.
  name: Kubernetes Native
finops:
- name: Apache Spark Finops
  service_category: API
  slug: apache-spark-finops
image: https://spark.apache.org/images/spark-logo-trademark.png
integrations:
- description: HDFS storage, YARN cluster manager, and Hadoop ecosystem integration.
  name: Apache Hadoop
- description: Structured Streaming source and sink for real-time event processing.
  name: Apache Kafka
- description: Open-source storage layer with ACID transactions for data lakes.
  name: Delta Lake
- description: Open table format for huge analytic datasets on cloud storage.
  name: Apache Iceberg
- description: Hive metastore integration for table catalog and metadata management.
  name: Apache Hive
- description: Native Kubernetes scheduling for cloud-native Spark deployments.
  name: Kubernetes
- description: Workflow orchestration for scheduling and managing Spark jobs.
  name: Apache Airflow
layout: provider
modified: '2026-05-19'
name: Apache Spark
nav: Providers
network: true
overview: 'Apache Spark publishes 2 APIs on the [APIs.io](https://apis.io/) network: Applications API and Version API. Tagged areas include Analytics, Big Data, Distributed Computing, Machine-Learning, and Open-Source.


  Apache Spark''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, Stack Overflow tag, and 13 more developer resources.'
plans:
- name: Apache Spark Plans Pricing
  plan_count: 3
  slug: apache-spark-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Apache Spark Rate Limits
  slug: apache-spark-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 0.0
    contract_quality: 34.7
    developer_ergonomics: 54.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 75.0
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-spark/refs/heads/main/screenshots/apache-spark-2026-06-20T172146.png
security:
- kind: domain-security
  name: Apache Spark Domain Security
  slug: apache-spark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Spark Vulnerability Disclosure
  slug: apache-spark-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-spark
tags:
- Analytics
- Big Data
- Distributed Computing
- Machine-Learning
- Open-Source
- Streaming
use_cases:
- description: Extract, transform, and load petabytes of data across distributed clusters.
  name: Large-Scale ETL
- description: Streaming analytics on live event data with sub-second latency.
  name: Real-Time Analytics
- description: Distributed ML training and feature engineering at scale with MLlib.
  name: Machine Learning Pipelines
- description: Query and transform data stored in cloud object stores and HDFS.
  name: Data Lake Processing
- description: Interactive SQL queries on structured and semi-structured data at scale.
  name: Interactive SQL Analytics
website: https://spark.apache.org/
---
