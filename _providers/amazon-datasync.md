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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Datasync Agentic Access
  operation_count: 6
  slug: amazon-datasync-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 6
apis:
- description: The Amazon DataSync REST API API from Amazon DataSync — 1 operation(s) for amazon datasync rest api.
  name: Amazon DataSync Amazon DataSync REST API API
  slug: amazon-datasync-amazon-datasync-rest-api-api
- description: 'The #CreateAgent API from Amazon DataSync — 1 operation(s) for #createagent.'
  name: 'Amazon DataSync #CreateAgent API'
  slug: amazon-datasync-createagent-api
- description: 'The #CreateLocationS3 API from Amazon DataSync — 1 operation(s) for #createlocations3.'
  name: 'Amazon DataSync #CreateLocationS3 API'
  slug: amazon-datasync-createlocations3-api
- description: 'The #DescribeTask API from Amazon DataSync — 1 operation(s) for #describetask.'
  name: 'Amazon DataSync #DescribeTask API'
  slug: amazon-datasync-describetask-api
- description: 'The #ListTasks API from Amazon DataSync — 1 operation(s) for #listtasks.'
  name: 'Amazon DataSync #ListTasks API'
  slug: amazon-datasync-listtasks-api
- description: 'The #StartTaskExecution API from Amazon DataSync — 1 operation(s) for #starttaskexecution.'
  name: 'Amazon DataSync #StartTaskExecution API'
  slug: amazon-datasync-starttaskexecution-api
artifact_total: 67
collections:
- collection_type: postman
  name: Amazon DataSync REST Amazon DataSync REST API API
  slug: postman-amazon-datasync-amazon-datasync-rest-api-api
- collection_type: postman
  name: 'Amazon DataSync REST Amazon DataSync REST API #CreateAgent API'
  slug: postman-amazon-datasync-createagent-api
- collection_type: postman
  name: 'Amazon DataSync REST Amazon DataSync REST API #CreateLocationS3 API'
  slug: postman-amazon-datasync-createlocations3-api
- collection_type: postman
  name: 'Amazon DataSync REST Amazon DataSync REST API #DescribeTask API'
  slug: postman-amazon-datasync-describetask-api
- collection_type: postman
  name: 'Amazon DataSync REST Amazon DataSync REST API #ListTasks API'
  slug: postman-amazon-datasync-listtasks-api
- collection_type: postman
  name: 'Amazon DataSync REST Amazon DataSync REST API #StartTaskExecution API'
  slug: postman-amazon-datasync-starttaskexecution-api
- collection_type: open
  name: Amazon DataSync REST API
  slug: open-amazon-datasync-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-datasync/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-datasync-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-datasync-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-datasync-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-datasync-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-datasync-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/datasync/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/datasync/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/datasync/
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
  url: https://aws.amazon.com/blogs/storage/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/datasync/
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
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-datasync
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-datasync-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-datasync-vocabulary.yaml
created: '2024-01-15'
description: AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems, AWS storage services, and other cloud storage. DataSync can transfer data at speeds up to 10 times faster than open-source tools by using purpose-built network protocol and parallel multi-threaded architecture. It supports NFS, SMB, HDFS, S3, EFS, FSx, and more as transfer endpoints.
examples:
- key_count: 4
  name: Agent Example
  slug: agent-example
- key_count: 3
  name: Create Location S3 Request Example
  slug: create-location-s3-request-example
- key_count: 3
  name: Create Task Request Example
  slug: create-task-request-example
- key_count: 1
  name: Create Task Response Example
  slug: create-task-response-example
- key_count: 2
  name: Error Example
  slug: error-example
- key_count: 3
  name: Location Example
  slug: location-example
- key_count: 5
  name: Options Example
  slug: options-example
- key_count: 5
  name: Task Example
  slug: task-example
- key_count: 5
  name: Task Execution Example
  slug: task-execution-example
- key_count: 3
  name: Task List Entry Example
  slug: task-list-entry-example
features:
- description: Transfer data at speeds up to 10 times faster than open-source tools using purpose-built multi-threaded network protocol over TLS.
  name: High-Speed Data Transfer
- description: Connect to NFS, SMB, HDFS, Amazon S3, Amazon EFS, FSx for Windows, FSx for Lustre, and FSx for NetApp ONTAP as transfer endpoints.
  name: Multi-Protocol Support
- description: Automatically verify data integrity using checksums at both source and destination to ensure byte-for-byte data consistency after transfer.
  name: Automated Data Validation
- description: Configure recurring scheduled transfers on hourly, daily, or weekly cadences for ongoing data synchronization between systems.
  name: Scheduled Transfers
- description: Deploy the DataSync agent VM on-premises to connect local NFS and SMB storage to AWS without opening inbound firewall ports.
  name: On-Premises Agent
- description: Control the network bandwidth consumed by DataSync transfers to minimize impact on production workloads during business hours.
  name: Bandwidth Throttling
- description: Monitor transfer metrics, task execution history, and set up alarms for failed transfers using Amazon CloudWatch.
  name: CloudWatch Integration
finops:
- name: Amazon Datasync Finops
  service_category: API
  slug: amazon-datasync-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-datasync.png
json_schemas:
- name: Agent
  property_count: 4
  slug: agent
- name: Amazon DataSync Task
  property_count: 12
  slug: amazon-datasync-task
- name: Create Location S3 Request
  property_count: 4
  slug: create-location-s3-request
- name: Create Task Request
  property_count: 6
  slug: create-task-request
- name: Create Task Response
  property_count: 1
  slug: create-task-response
- name: Error
  property_count: 2
  slug: error
- name: Location
  property_count: 3
  slug: location
- name: Options
  property_count: 5
  slug: options
- name: Task Execution
  property_count: 6
  slug: task-execution
- name: Task List Entry
  property_count: 3
  slug: task-list-entry
- name: Task
  property_count: 7
  slug: task
json_structures:
- name: Agent Structure
  property_count: 0
  slug: agent-structure
- name: Create Location S3 Request Structure
  property_count: 0
  slug: create-location-s3-request-structure
- name: Create Task Request Structure
  property_count: 0
  slug: create-task-request-structure
- name: Create Task Response Structure
  property_count: 0
  slug: create-task-response-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: Location Structure
  property_count: 0
  slug: location-structure
- name: Options Structure
  property_count: 0
  slug: options-structure
- name: Task Execution Structure
  property_count: 0
  slug: task-execution-structure
- name: Task List Entry Structure
  property_count: 0
  slug: task-list-entry-structure
- name: Task Structure
  property_count: 0
  slug: task-structure
jsonld:
- class_count: 0
  name: Amazon Datasync Context
  property_count: 3
  slug: amazon-datasync-context
layout: provider
modified: '2026-05-19'
name: Amazon DataSync
nav: Providers
network: true
overview: 'Amazon DataSync publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Amazon DataSync REST API API, #CreateAgent API, #CreateLocationS3 API, and 3 more. Tagged areas include Data Transfer, Migration, Storage, Automation, and Hybrid Cloud.


  The Amazon DataSync catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon DataSync''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 16 more developer resources.'
plans:
- name: Amazon Datasync Plans Pricing
  plan_count: 3
  slug: amazon-datasync-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Amazon Datasync Rate Limits
  slug: amazon-datasync-rate-limits
rules:
- name: Amazon DataSync API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-datasync-jsonschema-spectral-rules
- name: Amazon DataSync API Rules
  rule_count: 21
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 7
  slug: amazon-datasync-spectral-rules
score:
  band: strong
  composite: 65.8
  delta: -3.5
  facets:
    commercial_clarity: 81.6
    contract_quality: 71.2
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-datasync/refs/heads/main/screenshots/amazon-datasync-2026-06-20T171614.png
security:
- kind: authentication
  name: Amazon Datasync Authentication
  slug: amazon-datasync-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Datasync Domain Security
  slug: amazon-datasync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Datasync Vulnerability Disclosure
  slug: amazon-datasync-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Datasync Trust Center
  slug: amazon-datasync-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-datasync
tags:
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
use_cases:
- description: Migrate petabytes of data from on-premises NAS and SAN systems to Amazon S3 or EFS during cloud adoption and data center exit projects.
  name: Data Center Migration
- description: Keep on-premises and cloud storage in sync on a scheduled basis for hybrid cloud architectures and distributed workloads.
  name: Ongoing Hybrid Synchronization
- description: Transfer on-premises file data to Amazon S3 Glacier for cost-effective long-term archival and backup storage.
  name: Backup and Archive to Cloud
- description: Transfer datasets between AWS Regions or across AWS accounts for data sharing, disaster recovery, or multi-region analytics.
  name: Data Distribution
- description: Stage large datasets from S3 or on-premises storage to FSx for Lustre for high-performance computing workloads on AWS.
  name: HPC Data Staging
website: https://aws.amazon.com/datasync/
---
