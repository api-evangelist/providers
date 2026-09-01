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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Amazon Finspace Agentic Access
  operation_count: 20
  slug: amazon-finspace-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 6
apis:
- description: Manage FinSpace environments
  name: Amazon FinSpace Environments API
  slug: amazon-finspace-environments-api
- description: Manage kdb compute clusters
  name: Amazon FinSpace Kdb Clusters API
  slug: amazon-finspace-kdb-clusters-api
- description: Manage kdb databases
  name: Amazon FinSpace Kdb Databases API
  slug: amazon-finspace-kdb-databases-api
- description: Manage Managed kdb Insights environments
  name: Amazon FinSpace Kdb Environments API
  slug: amazon-finspace-kdb-environments-api
- description: Manage kdb users
  name: Amazon FinSpace Kdb Users API
  slug: amazon-finspace-kdb-users-api
- description: Tag FinSpace resources
  name: Amazon FinSpace Tagging API
  slug: amazon-finspace-tagging-api
artifact_total: 58
collections:
- collection_type: postman
  name: Amazon FinSpace Environments API
  slug: postman-amazon-finspace-environments-api
- collection_type: postman
  name: Amazon FinSpace Environments Kdb Clusters API
  slug: postman-amazon-finspace-kdb-clusters-api
- collection_type: postman
  name: Amazon FinSpace Environments Kdb Databases API
  slug: postman-amazon-finspace-kdb-databases-api
- collection_type: postman
  name: Amazon FinSpace Environments Kdb Environments API
  slug: postman-amazon-finspace-kdb-environments-api
- collection_type: postman
  name: Amazon FinSpace Environments Kdb Users API
  slug: postman-amazon-finspace-kdb-users-api
- collection_type: postman
  name: Amazon FinSpace Environments Tagging API
  slug: postman-amazon-finspace-tagging-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon FinSpace Environments API
  slug: open-amazon-finspace-environments-api
- collection_type: open
  name: Amazon FinSpace Environments Kdb Clusters API
  slug: open-amazon-finspace-kdb-clusters-api
- collection_type: open
  name: Amazon FinSpace Environments Kdb Databases API
  slug: open-amazon-finspace-kdb-databases-api
- collection_type: open
  name: Amazon FinSpace Environments Kdb Environments API
  slug: open-amazon-finspace-kdb-environments-api
- collection_type: open
  name: Amazon FinSpace Environments Kdb Users API
  slug: open-amazon-finspace-kdb-users-api
- collection_type: open
  name: Amazon FinSpace Environments Tagging API
  slug: open-amazon-finspace-tagging-api
- collection_type: open
  name: Amazon FinSpace API
  slug: open-amazon-finspace
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-finspace/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-finspace-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-finspace-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-finspace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-finspace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-finspace-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/finspace/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/finspace/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/finspace/
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
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/industries/financial-services/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/finspace/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-finspace
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-finspace-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-finspace-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-finspace-context.jsonld
created: '2026-03-16'
description: Amazon FinSpace is a data management and analytics service built specifically for the financial services industry. It reduces the time you spend on time-consuming data preparation tasks and makes it easy for analysts to access and analyze petabytes of financial data with a few clicks.
examples:
- key_count: 10
  name: Amazon Finspace Environment Example
  slug: amazon-finspace-environment-example
- key_count: 11
  name: Amazon Finspace Kx Cluster Example
  slug: amazon-finspace-kx-cluster-example
- key_count: 6
  name: Amazon Finspace Kx Database Example
  slug: amazon-finspace-kx-database-example
- key_count: 11
  name: Amazon Finspace Kx Environment Example
  slug: amazon-finspace-kx-environment-example
- key_count: 6
  name: Amazon Finspace Kx User Example
  slug: amazon-finspace-kx-user-example
features:
- description: Fully managed kdb+ (kdb+/q) compute infrastructure with HDB, RDB, Gateway, and Tickerplant cluster types.
  name: Managed kdb Environment
- description: Isolated FinSpace environments with preconfigured tools for financial data ingestion, preparation, and analysis.
  name: Financial Analytics Workspace
- description: Store and query petabytes of financial time-series data including tick, OHLCV, and alternative datasets.
  name: Petabyte-Scale Data
- description: Configure auto-scaling policies for kdb clusters to match intraday compute demand.
  name: kdb+ Cluster Autoscaling
- description: Deploy kdb clusters across multiple availability zones for high availability.
  name: Multi-AZ Clusters
- description: Map FinSpace kdb users to IAM roles for fine-grained permission control.
  name: IAM-Integrated Users
- description: Access financial data from FinSpace environments directly within Amazon SageMaker Studio.
  name: SageMaker Integration
finops:
- name: Amazon Finspace Finops
  service_category: API
  slug: amazon-finspace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-finspace.png
json_schemas:
- name: Environment
  property_count: 12
  slug: amazon-finspace-environment
- name: KxCluster
  property_count: 23
  slug: amazon-finspace-kx-cluster
- name: KxDatabase
  property_count: 6
  slug: amazon-finspace-kx-database
- name: KxEnvironment
  property_count: 18
  slug: amazon-finspace-kx-environment
- name: KxUser
  property_count: 6
  slug: amazon-finspace-kx-user
json_structures:
- name: Amazon Finspace Environment Structure
  property_count: 0
  slug: amazon-finspace-environment-structure
- name: Amazon Finspace Kx Cluster Structure
  property_count: 0
  slug: amazon-finspace-kx-cluster-structure
- name: Amazon Finspace Kx Database Structure
  property_count: 0
  slug: amazon-finspace-kx-database-structure
- name: Amazon Finspace Kx Environment Structure
  property_count: 0
  slug: amazon-finspace-kx-environment-structure
- name: Amazon Finspace Kx User Structure
  property_count: 0
  slug: amazon-finspace-kx-user-structure
jsonld:
- class_count: 5
  name: Amazon Finspace Context
  property_count: 22
  slug: amazon-finspace-context
layout: provider
modified: '2026-05-19'
name: Amazon FinSpace
nav: Providers
network: true
overview: 'Amazon FinSpace publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Environments API, Kdb Clusters API, Kdb Databases API, and 3 more. Tagged areas include Capital Markets, Data Analytics, Data Management, and Financial-Services.


  The Amazon FinSpace catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon FinSpace''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 15 more developer resources.'
plans:
- name: Amazon Finspace Plans Pricing
  plan_count: 3
  slug: amazon-finspace-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Amazon Finspace Rate Limits
  slug: amazon-finspace-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon FinSpace API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-finspace-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Amazon FinSpace API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 9
  slug: amazon-finspace-spectral-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 35.5
    developer_ergonomics: 66.7
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-finspace/refs/heads/main/screenshots/amazon-finspace-2026-06-20T171652.png
security:
- kind: authentication
  name: Amazon Finspace Authentication
  slug: amazon-finspace-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Finspace Domain Security
  slug: amazon-finspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Finspace Vulnerability Disclosure
  slug: amazon-finspace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Finspace Trust Center
  slug: amazon-finspace-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-finspace
tags:
- Capital Markets
- Data Analytics
- Data Management
- Financial-Services
use_cases:
- description: Ingest, store, and query high-frequency market tick data (trades, quotes, order books) using kdb+ clusters.
  name: Tick Data Management
- description: Run intraday risk calculations and post-trade analytics on financial time-series data at low latency.
  name: Risk Analytics
- description: Provide quants and data scientists with managed kdb environments for backtesting and strategy development.
  name: Quantitative Research
- description: Aggregate and transform trade and order data for regulatory submissions and compliance.
  name: Regulatory Reporting
- description: Ingest and correlate alternative datasets (news, satellite, ESG) with market data for signal generation.
  name: Alternative Data Processing
website: https://aws.amazon.com/finspace/
---
