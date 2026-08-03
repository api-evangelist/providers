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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Amazon Supply Chain Agentic Access
  operation_count: 24
  slug: amazon-supply-chain-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 6
apis:
- description: The Bill of Materials API from Amazon Supply Chain — 2 operation(s) for bill of materials.
  name: Amazon Supply Chain Bill of Materials API
  slug: amazon-supply-chain-bill-of-materials-api
- description: The Data Integration Events API from Amazon Supply Chain — 1 operation(s) for data integration events.
  name: Amazon Supply Chain Data Integration Events API
  slug: amazon-supply-chain-data-integration-events-api
- description: The Data Integration Flows API from Amazon Supply Chain — 2 operation(s) for data integration flows.
  name: Amazon Supply Chain Data Integration Flows API
  slug: amazon-supply-chain-data-integration-flows-api
- description: The Data Lake API from Amazon Supply Chain — 3 operation(s) for data lake.
  name: Amazon Supply Chain Data Lake API
  slug: amazon-supply-chain-data-lake-api
- description: The Instances API from Amazon Supply Chain — 2 operation(s) for instances.
  name: Amazon Supply Chain Instances API
  slug: amazon-supply-chain-instances-api
- description: The Tags API from Amazon Supply Chain — 1 operation(s) for tags.
  name: Amazon Supply Chain Tags API
  slug: amazon-supply-chain-tags-api
artifact_total: 51
collections:
- collection_type: postman
  name: AWS Supply Chain Bill of Materials API
  slug: postman-amazon-supply-chain-bill-of-materials-api
- collection_type: postman
  name: AWS Supply Chain Bill of Materials Data Integration Events API
  slug: postman-amazon-supply-chain-data-integration-events-api
- collection_type: postman
  name: AWS Supply Chain Bill of Materials Data Integration Flows API
  slug: postman-amazon-supply-chain-data-integration-flows-api
- collection_type: postman
  name: AWS Supply Chain Bill of Materials Data Lake API
  slug: postman-amazon-supply-chain-data-lake-api
- collection_type: postman
  name: AWS Supply Chain Bill of Materials Instances API
  slug: postman-amazon-supply-chain-instances-api
- collection_type: postman
  name: AWS Supply Chain Bill of Materials Tags API
  slug: postman-amazon-supply-chain-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-supply-chain/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-supply-chain-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-supply-chain-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-supply-chain-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-supply-chain-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-supply-chain-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/supply-chain/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/aws-supply-chain/
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
  url: https://aws.amazon.com/blogs/industries/supply-chain/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/scn/
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
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-supply-chain-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-supply-chain-vocabulary.yaml
created: '2026-03-16'
description: AWS Supply Chain is a cloud-based application that works with your existing enterprise resource planning (ERP) and supply chain management systems to help you manage supply chain risks. It provides ML-powered insights and recommended actions to help mitigate supply chain disruptions.
examples:
- key_count: 5
  name: Amazon Supply Chain Bill Of Materials Import Job Example
  slug: amazon-supply-chain-bill-of-materials-import-job-example
- key_count: 6
  name: Amazon Supply Chain Data Integration Event Example
  slug: amazon-supply-chain-data-integration-event-example
- key_count: 7
  name: Amazon Supply Chain Data Integration Flow Example
  slug: amazon-supply-chain-data-integration-flow-example
- key_count: 8
  name: Amazon Supply Chain Data Lake Dataset Example
  slug: amazon-supply-chain-data-lake-dataset-example
- key_count: 5
  name: Amazon Supply Chain Data Lake Namespace Example
  slug: amazon-supply-chain-data-lake-namespace-example
- key_count: 8
  name: Amazon Supply Chain Instance Example
  slug: amazon-supply-chain-instance-example
features:
- description: Machine learning models provide risk visibility and recommended actions for supply chain disruptions.
  name: ML-Powered Insights
- description: Connects with existing ERP and supply chain management systems via data integration flows.
  name: ERP Integration
- description: Centralized data lake for supply chain data with namespace and dataset management.
  name: Data Lake
- description: Import bill of materials data from S3 for inventory and component tracking.
  name: Bill of Materials Import
- description: Event-driven data ingestion for real-time supply chain data updates.
  name: Data Integration Events
- description: Create and manage multiple supply chain instances for different business units.
  name: Multi-instance
finops:
- name: Amazon Supply Chain Finops
  service_category: API
  slug: amazon-supply-chain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-supply-chain.png
json_schemas:
- name: BillOfMaterialsImportJob
  property_count: 5
  slug: amazon-supply-chain-bill-of-materials-import-job
- name: DataIntegrationEvent
  property_count: 6
  slug: amazon-supply-chain-data-integration-event
- name: DataIntegrationFlow
  property_count: 7
  slug: amazon-supply-chain-data-integration-flow
- name: DataLakeDataset
  property_count: 8
  slug: amazon-supply-chain-data-lake-dataset
- name: DataLakeNamespace
  property_count: 5
  slug: amazon-supply-chain-data-lake-namespace
- name: Instance
  property_count: 8
  slug: amazon-supply-chain-instance
json_structures:
- name: Amazon Supply Chain Bill Of Materials Import Job Structure
  property_count: 5
  slug: amazon-supply-chain-bill-of-materials-import-job-structure
- name: Amazon Supply Chain Data Integration Event Structure
  property_count: 6
  slug: amazon-supply-chain-data-integration-event-structure
- name: Amazon Supply Chain Data Integration Flow Structure
  property_count: 7
  slug: amazon-supply-chain-data-integration-flow-structure
- name: Amazon Supply Chain Data Lake Dataset Structure
  property_count: 8
  slug: amazon-supply-chain-data-lake-dataset-structure
- name: Amazon Supply Chain Data Lake Namespace Structure
  property_count: 5
  slug: amazon-supply-chain-data-lake-namespace-structure
- name: Amazon Supply Chain Instance Structure
  property_count: 8
  slug: amazon-supply-chain-instance-structure
jsonld:
- class_count: 8
  name: Amazon Supply Chain Context
  property_count: 23
  slug: amazon-supply-chain-context
layout: provider
modified: '2026-05-19'
name: Amazon Supply Chain
nav: Providers
network: true
overview: 'Amazon Supply Chain publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bill of Materials API, Data Integration Events API, Data Integration Flows API, and 3 more. Tagged areas include ERP Integration, Logistics, Machine Learning, and Supply Chain.


  The Amazon Supply Chain catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Supply Chain''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Supply Chain Plans Pricing
  plan_count: 3
  slug: amazon-supply-chain-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Amazon Supply Chain Rate Limits
  slug: amazon-supply-chain-rate-limits
rules:
- name: Amazon Supply Chain API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-supply-chain-jsonschema-spectral-rules
- name: Amazon Supply Chain API Rules
  rule_count: 24
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 10
  slug: amazon-supply-chain-spectral-rules
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 23.1
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/screenshots/amazon-supply-chain-2026-06-20T171834.png
security:
- kind: authentication
  name: Amazon Supply Chain Authentication
  slug: amazon-supply-chain-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Supply Chain Domain Security
  slug: amazon-supply-chain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Supply Chain Vulnerability Disclosure
  slug: amazon-supply-chain-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Supply Chain Trust Center
  slug: amazon-supply-chain-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-supply-chain
tags:
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
use_cases:
- description: Identify and mitigate supply chain disruptions with ML-powered risk insights.
  name: Supply Chain Risk Management
- description: Unified view of inventory across suppliers, warehouses, and distribution centers.
  name: Inventory Visibility
- description: Integrate ERP data with AWS Supply Chain for unified supply chain visibility.
  name: ERP Data Integration
- description: Use ML models to forecast demand and optimize inventory levels.
  name: Demand Forecasting
website: https://aws.amazon.com/supply-chain/
---
