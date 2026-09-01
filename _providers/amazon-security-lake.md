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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Security Lake Agentic Access
  operation_count: 13
  slug: amazon-security-lake-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 3
apis:
- description: Data lake creation and management
  name: Amazon Security Lake Data Lakes API
  slug: amazon-security-lake-data-lakes-api
- description: AWS and custom log source management
  name: Amazon Security Lake Log Sources API
  slug: amazon-security-lake-log-sources-api
- description: Subscriber management for data access
  name: Amazon Security Lake Subscribers API
  slug: amazon-security-lake-subscribers-api
arazzos:
- description: Resolve a data lake, update its configuration, then delete its configuration object.
  name: Amazon Security Lake Decommission Data Lake
  slug: amazon-security-lake-decommission-data-lake-workflow
- description: Confirm a subscriber exists, then delete it and verify it is removed from the list.
  name: Amazon Security Lake Offboard Subscriber
  slug: amazon-security-lake-offboard-subscriber-workflow
- description: Add a natively supported AWS service as a log source and confirm it is collecting.
  name: Amazon Security Lake Onboard AWS Log Source
  slug: amazon-security-lake-onboard-aws-log-source-workflow
- description: Create a Security Lake data lake, confirm it is listed, and inspect its collecting sources.
  name: Amazon Security Lake Provision Data Lake
  slug: amazon-security-lake-provision-data-lake-workflow
- description: Create a subscriber, confirm its identity and status, and verify it is listed.
  name: Amazon Security Lake Provision Subscriber
  slug: amazon-security-lake-provision-subscriber-workflow
- description: Register a third-party custom log source and confirm it appears in the source list.
  name: Amazon Security Lake Register Custom Source
  slug: amazon-security-lake-register-custom-source-workflow
- description: Find a subscriber by name, confirm it, and update its name and description.
  name: Amazon Security Lake Rename Subscriber
  slug: amazon-security-lake-rename-subscriber-workflow
artifact_total: 50
collections:
- collection_type: postman
  name: Amazon Security Lake API
  slug: postman-amazon-security-lake
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Security Lake Data Lakes API
  slug: open-amazon-security-lake-data-lakes-api
- collection_type: open
  name: Amazon Security Lake Data Lakes Log Sources API
  slug: open-amazon-security-lake-log-sources-api
- collection_type: open
  name: Amazon Security Lake Data Lakes Subscribers API
  slug: open-amazon-security-lake-subscribers-api
- collection_type: open
  name: Amazon Security Lake API
  slug: open-amazon-security-lake
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-security-lake-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-security-lake-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-security-lake-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-security-lake-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-security-lake-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-security-lake/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-decommission-data-lake-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-offboard-subscriber-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-onboard-aws-log-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-provision-data-lake-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-provision-subscriber-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-register-custom-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-lake-rename-subscriber-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/security-lake/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/security-lake/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/security-lake/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/security-lake/latest/APIReference/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/securitylake/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/security-lake/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/security-lake/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/amazon-security-lake/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-security-lake
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-security-lake-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-security-lake-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-security-lake-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-security-lake-data-lake-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-security-lake-log-source-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-security-lake-subscriber-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-security-lake-data-lake-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-security-lake-log-source-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-security-lake-subscriber-example.json
created: '2026-03-16'
description: Amazon Security Lake is a service that automatically centralizes an organization's security data from cloud, on-premises, and custom sources into a purpose-built data lake stored in your own Amazon S3. It manages the data lifecycle to help you optimize storage and supports OCSF (Open Cybersecurity Schema Framework) for normalized security data analysis.
examples:
- key_count: 6
  name: Amazon Security Lake Data Lake Example
  slug: amazon-security-lake-data-lake-example
- key_count: 3
  name: Amazon Security Lake Log Source Example
  slug: amazon-security-lake-log-source-example
- key_count: 9
  name: Amazon Security Lake Subscriber Example
  slug: amazon-security-lake-subscriber-example
features:
- description: Automatically centralizes security data from AWS services, third-party tools, and custom sources into a single data lake.
  name: Automatic Data Centralization
- description: Converts security data to the Open Cybersecurity Schema Framework (OCSF) for standardized analysis across tools.
  name: OCSF Normalization
- description: Stores all security data in Apache Parquet format optimized for analytical query performance.
  name: Apache Parquet Format
- description: Centralizes security data across an entire AWS Organization from all accounts and regions.
  name: Multi-Account Support
- description: Automatically manages storage lifecycle with configurable retention and tiering policies.
  name: Lifecycle Management
- description: Grant third-party SIEMs and analytics tools direct query access to your security data lake.
  name: Subscriber Access
- description: Native connectors for CloudTrail, VPC Flow Logs, Route 53, Security Hub, and EKS audit logs.
  name: Native AWS Integration
- description: Ingest custom and third-party security data sources in OCSF format.
  name: Custom Log Sources
finops:
- name: Amazon Security Lake Finops
  service_category: API
  slug: amazon-security-lake-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-security-lake.png
json_schemas:
- name: DataLake
  property_count: 6
  slug: amazon-security-lake-data-lake
- name: LogSource
  property_count: 3
  slug: amazon-security-lake-log-source
- name: Subscriber
  property_count: 9
  slug: amazon-security-lake-subscriber
json_structures:
- name: Amazon Security Lake Data Lake Structure
  property_count: 6
  slug: amazon-security-lake-data-lake-structure
- name: Amazon Security Lake Log Source Structure
  property_count: 3
  slug: amazon-security-lake-log-source-structure
- name: Amazon Security Lake Subscriber Structure
  property_count: 9
  slug: amazon-security-lake-subscriber-structure
jsonld:
- class_count: 3
  name: Amazon Security Lake Context
  property_count: 18
  slug: amazon-security-lake-context
layout: provider
modified: '2026-05-19'
name: Amazon Security Lake
nav: Providers
network: true
overview: 'Amazon Security Lake publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data Lakes API, Log Sources API, and Subscribers API. Tagged areas include Data Lake, Security, SIEM, and Threat Detection.


  The Amazon Security Lake catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Security Lake''s developer surface includes authentication, developer portal, getting-started guide, documentation, API reference, developer console, signup flow, and 33 more developer resources.'
plans:
- name: Amazon Security Lake Plans Pricing
  plan_count: 3
  slug: amazon-security-lake-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Amazon Security Lake Rate Limits
  slug: amazon-security-lake-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Security Lake API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-security-lake-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Amazon Security Lake API Rules
  rule_count: 27
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 15
  slug: amazon-security-lake-spectral-rules
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.8
    contract_quality: 32.9
    developer_ergonomics: 69.0
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-security-lake/refs/heads/main/screenshots/amazon-security-lake-2026-06-20T171817.png
security:
- kind: authentication
  name: Amazon Security Lake Authentication
  slug: amazon-security-lake-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Security Lake Domain Security
  slug: amazon-security-lake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Security Lake Vulnerability Disclosure
  slug: amazon-security-lake-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Security Lake Trust Center
  slug: amazon-security-lake-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-security-lake
tags:
- Data Lake
- Security
- SIEM
- Threat Detection
use_cases:
- description: Aggregate all security data from across a multi-account AWS environment into one queryable data lake.
  name: Security Data Centralization
- description: Provide SIEM platforms like Splunk, Sumo Logic, and Microsoft Sentinel direct access to normalized security data.
  name: SIEM Integration
- description: Enable security analysts to query normalized OCSF data for threat hunting and forensic investigation.
  name: Threat Hunting
- description: Retain security logs in a cost-optimized data lake for compliance audit requirements.
  name: Compliance Data Retention
- description: Run advanced analytics and ML models against normalized security data for anomaly detection.
  name: Security Analytics
- description: Centralize security data from on-premises and other cloud providers alongside AWS security data.
  name: Multi-Cloud Security Data
website: https://aws.amazon.com/security-lake/
---
