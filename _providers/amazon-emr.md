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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Emr Agentic Access
  operation_count: 1
  slug: amazon-emr-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Operations for creating, managing, and terminating EMR clusters
  name: Amazon EMR Clusters API
  slug: amazon-emr-clusters-api
arazzos:
- description: Create a cluster and queue processing steps to run as soon as it starts.
  name: Amazon EMR Launch a Cluster With Processing Steps
  slug: amazon-emr-run-cluster-with-steps-workflow
- description: Create an EMR cluster with the Hadoop and Hive applications installed.
  name: Amazon EMR Launch a Hadoop and Hive Cluster
  slug: amazon-emr-run-hadoop-hive-cluster-workflow
- description: Create an EMR cluster with the Apache HBase application installed.
  name: Amazon EMR Launch an HBase Cluster
  slug: amazon-emr-run-hbase-cluster-workflow
- description: Create an EMR cluster with the Presto application for interactive SQL.
  name: Amazon EMR Launch a Presto Query Cluster
  slug: amazon-emr-run-presto-query-cluster-workflow
- description: Create and start a new EMR cluster pre-configured to run Apache Spark.
  name: Amazon EMR Launch a Spark Cluster
  slug: amazon-emr-run-spark-cluster-workflow
- description: Launch a Spark cluster and queue an ETL processing step in one call.
  name: Amazon EMR Run a Spark ETL Job
  slug: amazon-emr-run-spark-etl-job-workflow
artifact_total: 35
collections:
- collection_type: postman
  name: Amazon EMR API
  slug: postman-amazon-emr
- collection_type: open
  name: Amazon EMR API
  slug: open-amazon-emr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-emr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-emr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-emr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-emr-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-emr/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-emr-run-cluster-with-steps-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-emr-run-hadoop-hive-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-emr-run-hbase-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-emr-run-presto-query-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-emr-run-spark-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-emr-run-spark-etl-job-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/emr/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/emr/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/emr/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/emr/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/emr
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-emr-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-emr-vocabulary.yaml
created: '2024-01-15'
description: Amazon EMR is a cloud big data platform for running large-scale distributed data processing jobs, interactive SQL queries, and machine learning applications using open-source analytics frameworks such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto.
examples:
- key_count: 9
  name: Amazon Emr Example
  slug: amazon-emr-example
features:
- description: Run Apache Spark jobs for large-scale data processing and machine learning
  name: Apache Spark Support
- description: Automatically adjust cluster size based on workload demand
  name: Auto Scaling
- description: Use EC2 Spot instances to reduce costs up to 90%
  name: Spot Instance Integration
- description: Run analytics without provisioning or managing clusters
  name: EMR Serverless
- description: Develop and debug jobs using EMR Studio Jupyter notebooks
  name: Studio Notebooks
finops:
- name: Amazon Emr Finops
  service_category: API
  slug: amazon-emr-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Use S3 as data lake storage for EMR clusters
  name: Amazon S3
- description: Integrate with Glue Data Catalog for metadata management
  name: AWS Glue
- description: Query data processed by EMR using Athena SQL
  name: Amazon Athena
- description: Hand off processed data to SageMaker for model training
  name: Amazon SageMaker
json_schemas:
- name: Amazon EMR Cluster
  property_count: 9
  slug: amazon-emr
json_structures:
- name: Amazon Emr Structure
  property_count: 9
  slug: amazon-emr-structure
jsonld:
- class_count: 0
  name: Amazon Emr Context
  property_count: 2
  slug: amazon-emr-context
layout: provider
modified: '2026-05-19'
name: Amazon EMR
nav: Providers
network: true
overview: 'Amazon EMR publishes 1 API on the [APIs.io](https://apis.io/) network: Clusters API. Tagged areas include Amazon Web Services, Analytics, Apache Spark, Big Data, and Data Processing.


  The Amazon EMR catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EMR''s developer surface includes developer portal, documentation, engineering blog, developer console, signup flow, support, FAQ, and 25 more developer resources.'
plans:
- name: Amazon Emr Plans Pricing
  plan_count: 3
  slug: amazon-emr-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Amazon Emr Rate Limits
  slug: amazon-emr-rate-limits
rules:
- name: Amazon EMR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-emr-jsonschema-spectral-rules
- name: Amazon EMR API Rules
  rule_count: 21
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 10
  slug: amazon-emr-spectral-rules
score:
  band: strong
  composite: 65.2
  delta: -3.5
  facets:
    commercial_clarity: 89.5
    contract_quality: 65.3
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-emr/refs/heads/main/screenshots/amazon-emr-2026-06-20T171642.png
security:
- kind: domain-security
  name: Amazon Emr Domain Security
  slug: amazon-emr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Emr Vulnerability Disclosure
  slug: amazon-emr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Emr Trust Center
  slug: amazon-emr-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-emr
tags:
- Amazon Web Services
- Analytics
- Apache Spark
- Big Data
- Data Processing
- Hadoop
use_cases:
- description: Extract, transform, and load large datasets across data lakes and warehouses
  name: ETL Data Processing
- description: Train machine learning models on large datasets using Spark MLlib
  name: Machine Learning
- description: Process and analyze application logs at petabyte scale
  name: Log Analytics
- description: Run Monte Carlo simulations and risk models on large datasets
  name: Financial Risk Analysis
website: https://aws.amazon.com/emr/
---
