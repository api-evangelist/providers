---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Xceptor Agentic Access
  operation_count: 30
  slug: xceptor-agentic-access
  summary_line: 30 operations · 14 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: API for creating, managing, and executing data processing workflows within the Xceptor platform. Enables programmatic orchestration of automated data processing pipelines including event-driven trigge
  name: Xceptor Workflow API
  slug: xceptor-workflow-api
- description: API for uploading and processing documents through Xceptor's data extraction engine. Supports intelligent document processing using NLP, OCR, and generative AI to transform unstructured documents incl
  name: Xceptor Document Upload API
  slug: xceptor-document-upload-api
- description: API for exporting processed data in various formats. Supports output to multiple downstream systems and data formats including XML, JSON, CSV, and Excel for integration with trading platforms, data wa
  name: Xceptor Data Export API
  slug: xceptor-data-export-api
- description: API and connector framework for integrating Xceptor with external systems and data sources. Provides pre-built connectors for cloud storage (AWS S3, Azure Blob, Google Cloud Storage), messaging system
  name: Xceptor Connector API
  slug: xceptor-connector-api
- description: Operations for authenticating with the Xceptor platform and managing access tokens.
  name: Xceptor Authentication API
  slug: xceptor-authentication-api
- description: Operations for configuring and managing connections to external data sources used by the Xceptor platform.
  name: Xceptor Data Sources API
  slug: xceptor-data-sources-api
- description: Operations for uploading, listing, and managing documents in the Xceptor platform.
  name: Xceptor Documents API
  slug: xceptor-documents-api
- description: Operations for triggering and monitoring document data extraction using Xceptor's AI-powered processing engine.
  name: Xceptor Extraction API
  slug: xceptor-extraction-api
- description: Operations for checking the health and status of the Xceptor API services.
  name: Xceptor Health API
  slug: xceptor-health-api
- description: Operations for creating, monitoring, and managing data processing jobs that execute within the Xceptor platform.
  name: Xceptor Jobs API
  slug: xceptor-jobs-api
- description: Operations for managing extraction templates that define the fields and tables to extract from specific document types.
  name: Xceptor Templates API
  slug: xceptor-templates-api
- description: Operations for executing workflows, monitoring run status, and retrieving run history and output.
  name: Xceptor Workflow Runs API
  slug: xceptor-workflow-runs-api
- description: Operations for managing the individual processing steps that compose a workflow, including step ordering and configuration.
  name: Xceptor Workflow Steps API
  slug: xceptor-workflow-steps-api
- description: Operations for creating, updating, listing, and deleting workflow definitions.
  name: Xceptor Workflows API
  slug: xceptor-workflows-api
artifact_total: 56
collections:
- collection_type: open
  name: Xceptor Document Upload API
  slug: open-xceptor-document-upload-api
- collection_type: open
  name: Xceptor REST API
  slug: open-xceptor-rest-api
- collection_type: open
  name: Xceptor Workflow API
  slug: open-xceptor-workflow-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xceptor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xceptor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xceptor-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.xceptor.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xceptor.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.xceptor.com/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.xceptor.com/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xceptor.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xceptor.com/legal-tcs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xceptor.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.xceptor.com/contact-us
- group: company
  title: ''
  type: Website
  url: https://www.xceptor.com
- group: other
  title: ''
  type: Platform
  url: https://www.xceptor.com/platform
- group: company
  title: ''
  type: Blog
  url: https://www.xceptor.com/blogs
- group: company
  title: ''
  type: Newsroom
  url: https://www.xceptor.com/company/newsroom
- group: operate
  title: ''
  type: Support
  url: https://xceptor.zendesk.com/hc/en-gb
- group: learn
  title: ''
  type: Training
  url: https://www.xceptor.com/support/training
- group: operate
  title: ''
  type: Community
  url: https://connect.xceptor.com
- group: learn
  title: ''
  type: Academy
  url: https://academy.xceptor.com/learn
- group: other
  title: ''
  type: Resources
  url: https://www.xceptor.com/resources
- group: other
  title: ''
  type: Glossary
  url: https://www.xceptor.com/resources/glossary
- group: learn
  title: ''
  type: Webinars
  url: https://www.xceptor.com/resources/webinars
- group: learn
  title: ''
  type: Videos
  url: https://www.xceptor.com/resources/videos
- group: company
  title: ''
  type: About
  url: https://www.xceptor.com/about
- group: company
  title: ''
  type: Partners
  url: https://www.xceptor.com/find-a-partner
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xceptor
- group: other
  title: ''
  type: X
  url: https://x.com/xceptor
- group: other
  title: ''
  type: Connector Marketplace
  url: https://app.xceptor.cloud/xsllibrary/mx/home/
- group: other
  title: ''
  type: Azure Marketplace
  url: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/xceptor.xceptor
created: '2024-01-01'
description: Xceptor is a data automation platform that helps organizations extract, transform, and integrate data from various sources, particularly focused on document processing and financial data automation.
finops:
- name: Xceptor Finops
  service_category: Data Automation Platform
  slug: xceptor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xceptor.png
json_schemas:
- name: AccessToken
  property_count: 4
  slug: xceptor-accesstoken
- name: BatchFileError
  property_count: 2
  slug: xceptor-batchfileerror
- name: BatchUploadResult
  property_count: 6
  slug: xceptor-batchuploadresult
- name: BoundingBox
  property_count: 4
  slug: xceptor-boundingbox
- name: DataSource
  property_count: 7
  slug: xceptor-datasource
- name: DataSourceList
  property_count: 2
  slug: xceptor-datasourcelist
- name: Document
  property_count: 12
  slug: xceptor-document
- name: DocumentList
  property_count: 2
  slug: xceptor-documentlist
- name: Error
  property_count: 3
  slug: xceptor-error
- name: ExtractedField
  property_count: 7
  slug: xceptor-extractedfield
- name: ExtractedTable
  property_count: 5
  slug: xceptor-extractedtable
- name: ExtractionResult
  property_count: 9
  slug: xceptor-extractionresult
- name: FieldDefinition
  property_count: 4
  slug: xceptor-fielddefinition
- name: HealthStatus
  property_count: 4
  slug: xceptor-healthstatus
- name: Job
  property_count: 9
  slug: xceptor-job
- name: JobCreate
  property_count: 5
  slug: xceptor-jobcreate
- name: JobList
  property_count: 2
  slug: xceptor-joblist
- name: Pagination
  property_count: 4
  slug: xceptor-pagination
- name: StepResult
  property_count: 8
  slug: xceptor-stepresult
- name: TableDefinition
  property_count: 2
  slug: xceptor-tabledefinition
- name: Template
  property_count: 9
  slug: xceptor-template
- name: TemplateList
  property_count: 2
  slug: xceptor-templatelist
- name: Workflow
  property_count: 11
  slug: xceptor-workflow
- name: WorkflowCreate
  property_count: 5
  slug: xceptor-workflowcreate
- name: WorkflowList
  property_count: 2
  slug: xceptor-workflowlist
- name: WorkflowRun
  property_count: 10
  slug: xceptor-workflowrun
- name: WorkflowRunCreate
  property_count: 1
  slug: xceptor-workflowruncreate
- name: WorkflowRunList
  property_count: 2
  slug: xceptor-workflowrunlist
- name: WorkflowStep
  property_count: 6
  slug: xceptor-workflowstep
- name: WorkflowStepCreate
  property_count: 5
  slug: xceptor-workflowstepcreate
- name: WorkflowUpdate
  property_count: 6
  slug: xceptor-workflowupdate
json_structures:
- name: Xceptor Structure
  property_count: 0
  slug: xceptor-structure
layout: provider
modified: '2026-05-19'
name: Xceptor
nav: Providers
network: true
overview: 'Xceptor publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Workflow API, Authentication API, Data Sources API, and 8 more. Tagged areas include API Integration, Data Automation, Data Extraction, Document Processing, and ETL.


  The Xceptor catalog on APIs.io includes 1 Spectral governance ruleset.


  Xceptor''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, training material, academy / training, and 22 more developer resources.'
plans:
- name: Xceptor Plans Pricing
  plan_count: 1
  slug: xceptor-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 1
  name: Xceptor Rate Limits
  slug: xceptor-rate-limits
rules:
- name: Xceptor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: xceptor-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: -3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.5
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xceptor/refs/heads/main/screenshots/xceptor-2026-06-20T201656.png
security:
- kind: authentication
  name: Xceptor Authentication
  slug: xceptor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xceptor Domain Security
  slug: xceptor-domain-security
  summary_line: TLSv1.3 · HSTS
slug: xceptor
tags:
- API Integration
- Data Automation
- Data Extraction
- Document Processing
- ETL
- Financial Data
- Financial Services
- Intelligent Document Processing
- Reconciliations
- Trade Operations
website: https://www.xceptor.com
---
