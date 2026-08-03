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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Data Pipeline Agentic Access
  operation_count: 13
  slug: amazon-data-pipeline-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 4
apis:
- description: Operations for managing pipeline object definitions
  name: Amazon Data Pipeline Pipeline Objects API
  slug: amazon-data-pipeline-pipeline-objects-api
- description: Operations for managing pipeline execution and task runs
  name: Amazon Data Pipeline Pipeline Runs API
  slug: amazon-data-pipeline-pipeline-runs-api
- description: Operations for managing data pipelines
  name: Amazon Data Pipeline Pipelines API
  slug: amazon-data-pipeline-pipelines-api
- description: Operations for managing pipeline tags
  name: Amazon Data Pipeline Tags API
  slug: amazon-data-pipeline-tags-api
arazzos:
- description: Copy an existing pipeline's definition into a brand-new pipeline and activate it.
  name: Amazon Data Pipeline Clone Pipeline
  slug: amazon-data-pipeline-clone-pipeline-workflow
- description: Stop a running pipeline and then permanently remove it and its run history.
  name: Amazon Data Pipeline Deactivate and Delete
  slug: amazon-data-pipeline-deactivate-and-delete-workflow
- description: Confirm a pipeline exists and then export its active definition objects.
  name: Amazon Data Pipeline Export Definition
  slug: amazon-data-pipeline-export-definition-workflow
- description: Find running task instances in a pipeline and pull their full object definitions.
  name: Amazon Data Pipeline Inspect Running Tasks
  slug: amazon-data-pipeline-inspect-running-tasks-workflow
- description: List all accessible pipelines and pull full metadata for the first page of them.
  name: Amazon Data Pipeline List and Describe
  slug: amazon-data-pipeline-list-and-describe-workflow
- description: Create an empty pipeline, populate its definition, activate it, and confirm its state.
  name: Amazon Data Pipeline Provision and Activate
  slug: amazon-data-pipeline-provision-and-activate-workflow
- description: Deactivate a pipeline, write a new definition, then reactivate it with the new objects.
  name: Amazon Data Pipeline Redeploy Definition
  slug: amazon-data-pipeline-redeploy-definition-workflow
- description: Add governance tags to a pipeline and confirm they are attached.
  name: Amazon Data Pipeline Tag and Confirm
  slug: amazon-data-pipeline-tag-and-confirm-workflow
- description: Validate a candidate pipeline definition and only commit it when it is error free.
  name: Amazon Data Pipeline Validate Then Put Definition
  slug: amazon-data-pipeline-validate-then-put-definition-workflow
artifact_total: 86
collections:
- collection_type: postman
  name: AWS Data Pipeline API
  slug: postman-amazon-data-pipeline
- collection_type: open
  name: AWS Data Pipeline API
  slug: open-amazon-data-pipeline
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-data-pipeline-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-data-pipeline-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-data-pipeline-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-data-pipeline-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-data-pipeline-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-data-pipeline/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-clone-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-deactivate-and-delete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-export-definition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-inspect-running-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-list-and-describe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-provision-and-activate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-redeploy-definition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-tag-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-pipeline-validate-then-put-definition-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/datapipeline/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/datapipeline/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/datapipeline/
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
  url: https://console.aws.amazon.com/datapipeline/
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
  url: rules/amazon-data-pipeline-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-data-pipeline-vocabulary.yaml
created: '2024-01-15'
description: AWS Data Pipeline is a web service that helps you reliably process and move data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals. With AWS Data Pipeline, you can regularly access your data where it is stored, transform and process it at scale, and efficiently transfer the results to AWS services such as Amazon S3, Amazon RDS, Amazon DynamoDB, and Amazon EMR. It supports data-driven workflows with retry, failure handling, and scheduling capabilities.
examples:
- key_count: 2
  name: Activate Pipeline Request Example
  slug: activate-pipeline-request-example
- key_count: 1
  name: Create Pipeline Output Example
  slug: create-pipeline-output-example
- key_count: 3
  name: Create Pipeline Request Example
  slug: create-pipeline-request-example
- key_count: 1
  name: Describe Pipelines Output Example
  slug: describe-pipelines-output-example
- key_count: 1
  name: Describe Pipelines Request Example
  slug: describe-pipelines-request-example
- key_count: 2
  name: Error Example
  slug: error-example
- key_count: 2
  name: Field Example
  slug: field-example
- key_count: 3
  name: Get Pipeline Definition Output Example
  slug: get-pipeline-definition-output-example
- key_count: 2
  name: List Pipelines Output Example
  slug: list-pipelines-output-example
- key_count: 4
  name: Pipeline Description Example
  slug: pipeline-description-example
- key_count: 2
  name: Pipeline Id Name Example
  slug: pipeline-id-name-example
- key_count: 3
  name: Pipeline Object Example
  slug: pipeline-object-example
- key_count: 3
  name: Put Pipeline Definition Output Example
  slug: put-pipeline-definition-output-example
- key_count: 2
  name: Query Objects Output Example
  slug: query-objects-output-example
- key_count: 2
  name: Tag Example
  slug: tag-example
- key_count: 2
  name: Validation Error Example
  slug: validation-error-example
features:
- description: Define complex data processing workflows with activities, data nodes, schedules, and preconditions using a declarative pipeline definition.
  name: Data-Driven Workflows
- description: Move and transform data between Amazon S3, Amazon RDS, Amazon DynamoDB, Amazon Redshift, and Amazon EMR in a single pipeline.
  name: Multi-Service Integration
- description: Schedule pipeline runs at fixed intervals (hourly, daily, weekly) or trigger them based on data availability preconditions.
  name: Flexible Scheduling
- description: Configure automatic retries for failed activities with configurable retry intervals, timeout settings, and failure notifications.
  name: Automated Retry and Failure Handling
- description: Process data from on-premises databases and file systems using the Data Pipeline Task Runner agent installed locally.
  name: On-Premises Data Support
- description: Launch and manage Amazon EMR clusters as pipeline resources to run Hive, Pig, and MapReduce jobs as part of data workflows.
  name: EMR Integration
- description: Manage active and latest pipeline definition versions, enabling updates to running pipelines without disrupting current execution.
  name: Pipeline Versioning
finops:
- name: Amazon Data Pipeline Finops
  service_category: API
  slug: amazon-data-pipeline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-data-pipeline.png
json_schemas:
- name: Activate Pipeline Request
  property_count: 2
  slug: activate-pipeline-request
- name: Create Pipeline Output
  property_count: 1
  slug: create-pipeline-output
- name: Create Pipeline Request
  property_count: 4
  slug: create-pipeline-request
- name: Describe Pipelines Output
  property_count: 1
  slug: describe-pipelines-output
- name: Describe Pipelines Request
  property_count: 1
  slug: describe-pipelines-request
- name: Error
  property_count: 2
  slug: error
- name: Field
  property_count: 3
  slug: field
- name: Get Pipeline Definition Output
  property_count: 3
  slug: get-pipeline-definition-output
- name: List Pipelines Output
  property_count: 3
  slug: list-pipelines-output
- name: Pipeline Description
  property_count: 4
  slug: pipeline-description
- name: Pipeline ID Name
  property_count: 2
  slug: pipeline-id-name
- name: Pipeline Object
  property_count: 3
  slug: pipeline-object
- name: Put Pipeline Definition Output
  property_count: 3
  slug: put-pipeline-definition-output
- name: Query Objects Output
  property_count: 3
  slug: query-objects-output
- name: Tag
  property_count: 2
  slug: tag
- name: Validation Error
  property_count: 2
  slug: validation-error
json_structures:
- name: Activate Pipeline Request Structure
  property_count: 0
  slug: activate-pipeline-request-structure
- name: Create Pipeline Output Structure
  property_count: 0
  slug: create-pipeline-output-structure
- name: Create Pipeline Request Structure
  property_count: 0
  slug: create-pipeline-request-structure
- name: Describe Pipelines Output Structure
  property_count: 0
  slug: describe-pipelines-output-structure
- name: Describe Pipelines Request Structure
  property_count: 0
  slug: describe-pipelines-request-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: Field Structure
  property_count: 0
  slug: field-structure
- name: Get Pipeline Definition Output Structure
  property_count: 0
  slug: get-pipeline-definition-output-structure
- name: List Pipelines Output Structure
  property_count: 0
  slug: list-pipelines-output-structure
- name: Pipeline Description Structure
  property_count: 0
  slug: pipeline-description-structure
- name: Pipeline Id Name Structure
  property_count: 0
  slug: pipeline-id-name-structure
- name: Pipeline Object Structure
  property_count: 0
  slug: pipeline-object-structure
- name: Put Pipeline Definition Output Structure
  property_count: 0
  slug: put-pipeline-definition-output-structure
- name: Query Objects Output Structure
  property_count: 0
  slug: query-objects-output-structure
- name: Tag Structure
  property_count: 0
  slug: tag-structure
- name: Validation Error Structure
  property_count: 0
  slug: validation-error-structure
jsonld:
- class_count: 0
  name: Amazon Data Pipeline Context
  property_count: 30
  slug: amazon-data-pipeline-context
layout: provider
modified: '2026-05-19'
name: Amazon Data Pipeline
nav: Providers
network: true
overview: 'Amazon Data Pipeline publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Pipeline Objects API, Pipeline Runs API, Pipelines API, and 1 more. Tagged areas include Data Processing, ETL, Workflows, Data Pipeline, and Automation.


  The Amazon Data Pipeline catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Data Pipeline''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, and 23 more developer resources.'
plans:
- name: Amazon Data Pipeline Plans Pricing
  plan_count: 3
  slug: amazon-data-pipeline-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Amazon Data Pipeline Rate Limits
  slug: amazon-data-pipeline-rate-limits
rules:
- name: Amazon Data Pipeline API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-data-pipeline-jsonschema-spectral-rules
- name: Amazon Data Pipeline API Rules
  rule_count: 26
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 8
  slug: amazon-data-pipeline-spectral-rules
score:
  band: exemplar
  composite: 67.3
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 79.1
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/screenshots/amazon-data-pipeline-2026-06-20T171620.png
security:
- kind: authentication
  name: Amazon Data Pipeline Authentication
  slug: amazon-data-pipeline-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Data Pipeline Domain Security
  slug: amazon-data-pipeline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Data Pipeline Vulnerability Disclosure
  slug: amazon-data-pipeline-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Data Pipeline Trust Center
  slug: amazon-data-pipeline-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-data-pipeline
tags:
- Data Processing
- ETL
- Workflows
- Data Pipeline
- Automation
use_cases:
- description: Schedule daily extraction, transformation, and loading of data from relational databases into S3 or Redshift for analytics processing.
  name: Daily ETL Workflows
- description: Process application and server log files from S3 using EMR activities to generate aggregated reports and analytics datasets.
  name: Log Processing Pipelines
- description: Migrate data between on-premises databases and AWS managed database services using scheduled pipeline activities.
  name: Database Migration
- description: Automate the ingestion and transformation of raw data into structured formats in S3 data lakes for downstream analytics.
  name: Data Lake Ingestion
- description: Replicate DynamoDB tables or S3 data across AWS regions using scheduled pipeline copy activities for disaster recovery.
  name: Cross-Region Data Replication
website: https://aws.amazon.com/datapipeline/
---
