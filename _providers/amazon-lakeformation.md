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
- acting_count: 4
  human_in_the_loop: 1
  name: Amazon Lakeformation Agentic Access
  operation_count: 7
  slug: amazon-lakeformation-agentic-access
  summary_line: 7 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Data Catalog database management
  name: AWS Lake Formation Databases API
  slug: amazon-lakeformation-databases-api
artifact_total: 34
collections:
- collection_type: postman
  name: AWS Lake Formation Databases API
  slug: postman-amazon-lakeformation-databases-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Lake Formation Databases API
  slug: open-amazon-lakeformation-databases-api
- collection_type: open
  name: AWS Lake Formation API
  slug: open-amazon-lakeformation
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-lake-formation/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lakeformation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-lakeformation-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lakeformation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-lakeformation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-lakeformation-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/lake-formation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lake-formation/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/lakeformation/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-lakeformation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lakeformation-vocabulary.yaml
created: '2024-01-15'
description: AWS Lake Formation is a fully managed service that makes it easy to build, secure, and manage data lakes. It simplifies and automates many of the complex manual steps usually required to create data lakes, including collecting, cleansing, cataloging, and securely sharing data, with centralized governance and fine-grained access control across your analytics and machine learning services.
examples:
- key_count: 6
  name: Amazon Lakeformation Data Cells Filter Example
  slug: amazon-lakeformation-data-cells-filter-example
- key_count: 5
  name: Amazon Lakeformation Database Example
  slug: amazon-lakeformation-database-example
features:
- description: Set up a secure data lake in days with centralized governance and automated data ingestion.
  name: Data Lake Setup
- description: ACID transactions, row-level security, and automatic compaction for governed tables.
  name: Governed Tables
- description: Column, row, and cell-level security policies enforced across analytics engines.
  name: Fine-Grained Access Control
- description: Pre-built workflows to ingest data from common data sources into the data lake.
  name: Blueprints
- description: Share data across accounts and organizations with fine-grained permissions.
  name: Data Sharing
finops:
- name: Amazon Lakeformation Finops
  service_category: API
  slug: amazon-lakeformation-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Store and manage data lake content in S3 with Lake Formation governance.
  name: Amazon S3
- description: Catalog data and run ETL jobs with Glue, governed by Lake Formation.
  name: AWS Glue
- description: Process large datasets with EMR Spark, respecting Lake Formation permissions.
  name: Amazon EMR
- description: Visualize data lake content with QuickSight enforcing Lake Formation policies.
  name: Amazon QuickSight
json_schemas:
- name: DataCellsFilter
  property_count: 6
  slug: amazon-lakeformation-data-cells-filter
- name: Database
  property_count: 5
  slug: amazon-lakeformation-database
json_structures:
- name: Amazon Lakeformation Data Cells Filter Structure
  property_count: 6
  slug: amazon-lakeformation-data-cells-filter-structure
- name: Amazon Lakeformation Database Structure
  property_count: 5
  slug: amazon-lakeformation-database-structure
jsonld:
- class_count: 2
  name: Amazon Lakeformation Context
  property_count: 7
  slug: amazon-lakeformation-context
layout: provider
modified: '2026-05-19'
name: AWS Lake Formation
nav: Providers
network: true
overview: 'AWS Lake Formation publishes 1 API on the [APIs.io](https://apis.io/) network: Databases API. Tagged areas include Analytics, Data Lake, and Governance.


  The AWS Lake Formation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AWS Lake Formation''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Lakeformation Plans Pricing
  plan_count: 3
  slug: amazon-lakeformation-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 5
  name: Amazon Lakeformation Rate Limits
  slug: amazon-lakeformation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AWS Lake Formation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-lakeformation-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: AWS Lake Formation API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 14
  slug: amazon-lakeformation-spectral-rules
score:
  band: developing
  composite: 50.2
  delta: -7.2
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 25.0
    contract_quality: 69.2
    developer_ergonomics: 47.6
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lakeformation/refs/heads/main/screenshots/amazon-lakeformation-2026-06-20T171721.png
security:
- kind: authentication
  name: Amazon Lakeformation Authentication
  slug: amazon-lakeformation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Lakeformation Domain Security
  slug: amazon-lakeformation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Lakeformation Vulnerability Disclosure
  slug: amazon-lakeformation-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Lakeformation Trust Center
  slug: amazon-lakeformation-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-lakeformation
tags:
- Analytics
- Data Lake
- Governance
use_cases:
- description: Build a centralized data lake with governed access for analytics teams.
  name: Enterprise Data Lake
- description: Implement a data mesh architecture with cross-account data sharing and governance.
  name: Data Mesh
- description: Enforce data access policies for GDPR, HIPAA, and other compliance requirements.
  name: Compliance Governance
website: https://aws.amazon.com/
---
