---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Alteryx Agentic Access
  operation_count: 50
  slug: alteryx-agentic-access
  summary_line: 50 operations · 36 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'REST API for managing workflows, schedules, and jobs on Alteryx Server. Provides Subscription, User V2, Admin V1, Admin V2, and V3 API endpoints for creating, updating, searching, and deleting users, '
  name: Alteryx Server API
  slug: alteryx-server-api
- description: The V1 API for Alteryx Server provides endpoints for admins including the Migratable Endpoint for migrating workflows across Server environments and the Auditlog Endpoint for tracking changes to syste
  name: Alteryx Server API V1
  slug: alteryx-server-api-v1
- description: API for interacting with Alteryx Analytics Gallery for workflow sharing and execution.
  name: Alteryx Gallery API
  slug: alteryx-gallery-api
- description: API for Alteryx Connect data catalog and collaboration platform.
  name: Alteryx Connect API
  slug: alteryx-connect-api
- description: The AlteryxEngine API allows you to call into the Alteryx Engine to build applications that can programmatically execute Alteryx Designer workflows. Workflows and applications can be executed as a sep
  name: Alteryx AlteryxEngine API
  slug: alteryx-alteryxengine-api
- description: REST API for Alteryx Designer Cloud (powered by Trifacta) providing data preparation, transformation, and pipeline management capabilities. Enables programmatic access to data preparation workflows an
  name: Alteryx Designer Cloud API
  slug: alteryx-designer-cloud-api
- description: Manage collections of workflows, schedules, users, and user groups
  name: Alteryx Collections API
  slug: alteryx-collections-api
- description: Manage stored credentials and credential sharing
  name: Alteryx Credentials API
  slug: alteryx-credentials-api
- description: Manage and monitor workflow execution jobs
  name: Alteryx Jobs API
  slug: alteryx-jobs-api
- description: Create, retrieve, update, and delete workflow execution schedules
  name: Alteryx Schedules API
  slug: alteryx-schedules-api
- description: Manage user accounts, permissions, and asset transfers
  name: Alteryx Users API
  slug: alteryx-users-api
- description: Manage workflows including upload, retrieval, update, deletion, versioning, and job execution
  name: Alteryx Workflows API
  slug: alteryx-workflows-api
artifact_total: 153
collections:
- collection_type: postman
  name: Alteryx Server API V3 Collections API
  slug: postman-alteryx-collections-api
- collection_type: postman
  name: Alteryx Server API V3 Collections Credentials API
  slug: postman-alteryx-credentials-api
- collection_type: postman
  name: Alteryx Server API V3 Collections Jobs API
  slug: postman-alteryx-jobs-api
- collection_type: postman
  name: Alteryx Server API V3 Collections Schedules API
  slug: postman-alteryx-schedules-api
- collection_type: postman
  name: Alteryx Server API V3 Collections Users API
  slug: postman-alteryx-users-api
- collection_type: postman
  name: Alteryx Server API V3 Collections Workflows API
  slug: postman-alteryx-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alteryx Server API V3 Collections API
  slug: open-alteryx-collections-api
- collection_type: open
  name: Alteryx Server API V3 Collections Credentials API
  slug: open-alteryx-credentials-api
- collection_type: open
  name: Alteryx Server API V3 Collections Jobs API
  slug: open-alteryx-jobs-api
- collection_type: open
  name: Alteryx Server API V3 Collections Schedules API
  slug: open-alteryx-schedules-api
- collection_type: open
  name: Alteryx Server API V3
  slug: open-alteryx-server-api-v3
- collection_type: open
  name: Alteryx Server API V3 Collections Users API
  slug: open-alteryx-users-api
- collection_type: open
  name: Alteryx Server API V3 Collections Workflows API
  slug: open-alteryx-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/alteryx/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alteryx-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/alteryx-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alteryx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alteryx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alteryx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alteryx-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.alteryx.com/current/en/developer-help.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.alteryx.com/current/en/developer-help/apis/get-started-with-apis.html
- group: build
  title: ''
  type: SDKs
  url: https://help.alteryx.com/current/en/developer-help/platform-sdk.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alteryx.com
- group: operate
  title: ''
  type: Support
  url: https://community.alteryx.com
- group: company
  title: ''
  type: Blog
  url: https://community.alteryx.com/t5/Engine-Works/bg-p/engine-works
- group: other
  title: ''
  type: X
  url: https://twitter.com/alteryx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alteryx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alteryx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alteryx.com/products/pricing
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.alteryx.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alteryx.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alteryx.com/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.alteryx.com/legal
created: '2024-01-15'
description: Alteryx is an analytics automation platform that enables data analysts and scientists to break data barriers, deliver insights, and experience the thrill of getting to the answer faster.
examples:
- key_count: 4
  name: Alteryx Server V3 Collection Example
  slug: alteryx-server-v3-collection-example
- key_count: 6
  name: Alteryx Server V3 Collection Permission Flags Example
  slug: alteryx-server-v3-collection-permission-flags-example
- key_count: 7
  name: Alteryx Server V3 Collection User Permission Example
  slug: alteryx-server-v3-collection-user-permission-example
- key_count: 4
  name: Alteryx Server V3 Create Job Contract Example
  slug: alteryx-server-v3-create-job-contract-example
- key_count: 8
  name: Alteryx Server V3 Create Schedule Contract Example
  slug: alteryx-server-v3-create-schedule-contract-example
- key_count: 17
  name: Alteryx Server V3 Create User Contract Example
  slug: alteryx-server-v3-create-user-contract-example
- key_count: 2
  name: Alteryx Server V3 Credential Example
  slug: alteryx-server-v3-credential-example
- key_count: 2
  name: Alteryx Server V3 Error Response Example
  slug: alteryx-server-v3-error-response-example
- key_count: 10
  name: Alteryx Server V3 Job Detail Example
  slug: alteryx-server-v3-job-detail-example
- key_count: 6
  name: Alteryx Server V3 Job Summary Example
  slug: alteryx-server-v3-job-summary-example
- key_count: 9
  name: Alteryx Server V3 Patch Schedule Contract Example
  slug: alteryx-server-v3-patch-schedule-contract-example
- key_count: 24
  name: Alteryx Server V3 Schedule Detail Example
  slug: alteryx-server-v3-schedule-detail-example
- key_count: 9
  name: Alteryx Server V3 Schedule Iteration Example
  slug: alteryx-server-v3-schedule-iteration-example
- key_count: 6
  name: Alteryx Server V3 Schedule Summary Example
  slug: alteryx-server-v3-schedule-summary-example
- key_count: 10
  name: Alteryx Server V3 Update Schedule Contract Example
  slug: alteryx-server-v3-update-schedule-contract-example
- key_count: 21
  name: Alteryx Server V3 Update User Contract Example
  slug: alteryx-server-v3-update-user-contract-example
- key_count: 15
  name: Alteryx Server V3 Update Workflow Contract Example
  slug: alteryx-server-v3-update-workflow-contract-example
- key_count: 3
  name: Alteryx Server V3 User Asset Example
  slug: alteryx-server-v3-user-asset-example
- key_count: 22
  name: Alteryx Server V3 User Detail Example
  slug: alteryx-server-v3-user-detail-example
- key_count: 17
  name: Alteryx Server V3 Workflow Detail Example
  slug: alteryx-server-v3-workflow-detail-example
- key_count: 6
  name: Alteryx Server V3 Workflow Question Example
  slug: alteryx-server-v3-workflow-question-example
- key_count: 8
  name: Alteryx Server V3 Workflow Summary Example
  slug: alteryx-server-v3-workflow-summary-example
- key_count: 10
  name: Alteryx Server V3 Workflow Version Details Example
  slug: alteryx-server-v3-workflow-version-details-example
- key_count: 15
  name: Alteryx Server V3 Workflow Version Example
  slug: alteryx-server-v3-workflow-version-example
features:
- description: Visual drag-and-drop workflow builder for automating data preparation, blending, and analytics pipelines.
  name: Workflow Automation
- description: Schedule workflows to run at specific times or intervals for automated recurring analytics processes.
  name: Scheduled Execution
- description: Fine-grained user management with role-based access control for shared workflow environments.
  name: User and Access Management
- description: Secure storage and sharing of data source credentials across workflows and users.
  name: Credential Management
- description: Organize workflows, schedules, and users into collections for logical grouping and permission management.
  name: Collection Organization
- description: Browser-based data preparation and transformation through Designer Cloud with AI-assisted suggestions.
  name: Cloud Data Preparation
finops:
- name: Alteryx Finops
  service_category: Analytics Platform
  slug: alteryx-finops
image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
integrations:
- description: Native connector for reading from and writing to Snowflake data warehouse for cloud analytics.
  name: Snowflake
- description: Publish prepared data directly to Tableau Server for visualization and business intelligence.
  name: Tableau
- description: Connect to Salesforce CRM data for analytics, reporting, and automated data synchronization.
  name: Salesforce
- description: Read and write data to Amazon S3 for cloud-based data lake analytics workflows.
  name: AWS S3
- description: Integration with Azure data services including SQL Database, Blob Storage, and Synapse Analytics.
  name: Microsoft Azure
json_schemas:
- name: Collection
  property_count: 4
  slug: alteryx-collection
- name: CollectionPermissionFlags
  property_count: 6
  slug: alteryx-collectionpermissionflags
- name: CollectionUserPermission
  property_count: 7
  slug: alteryx-collectionuserpermission
- name: CreateJobContract
  property_count: 4
  slug: alteryx-createjobcontract
- name: CreateScheduleContract
  property_count: 9
  slug: alteryx-createschedulecontract
- name: CreateUserContract
  property_count: 17
  slug: alteryx-createusercontract
- name: Credential
  property_count: 2
  slug: alteryx-credential
- name: ErrorResponse
  property_count: 2
  slug: alteryx-errorresponse
- name: JobDetail
  property_count: 10
  slug: alteryx-jobdetail
- name: JobSummary
  property_count: 6
  slug: alteryx-jobsummary
- name: PatchScheduleContract
  property_count: 10
  slug: alteryx-patchschedulecontract
- name: ScheduleDetail
  property_count: 25
  slug: alteryx-scheduledetail
- name: ScheduleIteration
  property_count: 9
  slug: alteryx-scheduleiteration
- name: ScheduleSummary
  property_count: 6
  slug: alteryx-schedulesummary
- name: CollectionPermissionFlags
  property_count: 6
  slug: alteryx-server-v3-collection-permission-flags
- name: Collection
  property_count: 4
  slug: alteryx-server-v3-collection
- name: CollectionUserPermission
  property_count: 7
  slug: alteryx-server-v3-collection-user-permission
- name: CreateJobContract
  property_count: 4
  slug: alteryx-server-v3-create-job-contract
- name: CreateScheduleContract
  property_count: 8
  slug: alteryx-server-v3-create-schedule-contract
- name: CreateUserContract
  property_count: 17
  slug: alteryx-server-v3-create-user-contract
- name: Credential
  property_count: 2
  slug: alteryx-server-v3-credential
- name: ErrorResponse
  property_count: 2
  slug: alteryx-server-v3-error-response
- name: JobDetail
  property_count: 10
  slug: alteryx-server-v3-job-detail
- name: JobSummary
  property_count: 6
  slug: alteryx-server-v3-job-summary
- name: PatchScheduleContract
  property_count: 9
  slug: alteryx-server-v3-patch-schedule-contract
- name: ScheduleDetail
  property_count: 24
  slug: alteryx-server-v3-schedule-detail
- name: ScheduleIteration
  property_count: 9
  slug: alteryx-server-v3-schedule-iteration
- name: ScheduleSummary
  property_count: 6
  slug: alteryx-server-v3-schedule-summary
- name: UpdateScheduleContract
  property_count: 10
  slug: alteryx-server-v3-update-schedule-contract
- name: UpdateUserContract
  property_count: 21
  slug: alteryx-server-v3-update-user-contract
- name: UpdateWorkflowContract
  property_count: 15
  slug: alteryx-server-v3-update-workflow-contract
- name: UserAsset
  property_count: 3
  slug: alteryx-server-v3-user-asset
- name: UserDetail
  property_count: 22
  slug: alteryx-server-v3-user-detail
- name: WorkflowDetail
  property_count: 17
  slug: alteryx-server-v3-workflow-detail
- name: WorkflowQuestion
  property_count: 6
  slug: alteryx-server-v3-workflow-question
- name: WorkflowSummary
  property_count: 8
  slug: alteryx-server-v3-workflow-summary
- name: WorkflowVersionDetails
  property_count: 10
  slug: alteryx-server-v3-workflow-version-details
- name: WorkflowVersion
  property_count: 15
  slug: alteryx-server-v3-workflow-version
- name: UpdateScheduleContract
  property_count: 11
  slug: alteryx-updateschedulecontract
- name: UpdateUserContract
  property_count: 21
  slug: alteryx-updateusercontract
- name: UpdateWorkflowContract
  property_count: 15
  slug: alteryx-updateworkflowcontract
- name: UserAsset
  property_count: 3
  slug: alteryx-userasset
- name: UserDetail
  property_count: 22
  slug: alteryx-userdetail
- name: Alteryx Workflow
  property_count: 22
  slug: alteryx-workflow
- name: WorkflowDetail
  property_count: 17
  slug: alteryx-workflowdetail
- name: WorkflowQuestion
  property_count: 6
  slug: alteryx-workflowquestion
- name: WorkflowSummary
  property_count: 8
  slug: alteryx-workflowsummary
- name: WorkflowVersion
  property_count: 16
  slug: alteryx-workflowversion
- name: WorkflowVersionDetails
  property_count: 10
  slug: alteryx-workflowversiondetails
json_structures:
- name: Alteryx Server V3 Collection Permission Flags Structure
  property_count: 6
  slug: alteryx-server-v3-collection-permission-flags-structure
- name: Alteryx Server V3 Collection Structure
  property_count: 4
  slug: alteryx-server-v3-collection-structure
- name: Alteryx Server V3 Collection User Permission Structure
  property_count: 7
  slug: alteryx-server-v3-collection-user-permission-structure
- name: Alteryx Server V3 Create Job Contract Structure
  property_count: 4
  slug: alteryx-server-v3-create-job-contract-structure
- name: Alteryx Server V3 Create Schedule Contract Structure
  property_count: 8
  slug: alteryx-server-v3-create-schedule-contract-structure
- name: Alteryx Server V3 Create User Contract Structure
  property_count: 17
  slug: alteryx-server-v3-create-user-contract-structure
- name: Alteryx Server V3 Credential Structure
  property_count: 2
  slug: alteryx-server-v3-credential-structure
- name: Alteryx Server V3 Error Response Structure
  property_count: 2
  slug: alteryx-server-v3-error-response-structure
- name: Alteryx Server V3 Job Detail Structure
  property_count: 10
  slug: alteryx-server-v3-job-detail-structure
- name: Alteryx Server V3 Job Summary Structure
  property_count: 6
  slug: alteryx-server-v3-job-summary-structure
- name: Alteryx Server V3 Patch Schedule Contract Structure
  property_count: 9
  slug: alteryx-server-v3-patch-schedule-contract-structure
- name: Alteryx Server V3 Schedule Detail Structure
  property_count: 24
  slug: alteryx-server-v3-schedule-detail-structure
- name: Alteryx Server V3 Schedule Iteration Structure
  property_count: 9
  slug: alteryx-server-v3-schedule-iteration-structure
- name: Alteryx Server V3 Schedule Summary Structure
  property_count: 6
  slug: alteryx-server-v3-schedule-summary-structure
- name: Alteryx Server V3 Update Schedule Contract Structure
  property_count: 10
  slug: alteryx-server-v3-update-schedule-contract-structure
- name: Alteryx Server V3 Update User Contract Structure
  property_count: 21
  slug: alteryx-server-v3-update-user-contract-structure
- name: Alteryx Server V3 Update Workflow Contract Structure
  property_count: 15
  slug: alteryx-server-v3-update-workflow-contract-structure
- name: Alteryx Server V3 User Asset Structure
  property_count: 3
  slug: alteryx-server-v3-user-asset-structure
- name: Alteryx Server V3 User Detail Structure
  property_count: 22
  slug: alteryx-server-v3-user-detail-structure
- name: Alteryx Server V3 Workflow Detail Structure
  property_count: 17
  slug: alteryx-server-v3-workflow-detail-structure
- name: Alteryx Server V3 Workflow Question Structure
  property_count: 6
  slug: alteryx-server-v3-workflow-question-structure
- name: Alteryx Server V3 Workflow Summary Structure
  property_count: 8
  slug: alteryx-server-v3-workflow-summary-structure
- name: Alteryx Server V3 Workflow Version Details Structure
  property_count: 10
  slug: alteryx-server-v3-workflow-version-details-structure
- name: Alteryx Server V3 Workflow Version Structure
  property_count: 15
  slug: alteryx-server-v3-workflow-version-structure
- name: Alteryx Structure
  property_count: 0
  slug: alteryx-structure
jsonld:
- class_count: 0
  name: Alteryx Context
  property_count: 8
  slug: alteryx-context
- class_count: 0
  name: Alteryx Server V3 Context
  property_count: 0
  slug: alteryx-server-v3-context
layout: provider
modified: '2026-05-19'
name: Alteryx
nav: Providers
network: true
overview: 'Alteryx publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Credentials API, Jobs API, and 3 more. Tagged areas include Analytics, Automation, Data Engineering, Data Preparation, and Data Science.


  The Alteryx catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Alteryx''s developer surface includes authentication, getting-started guide, support, engineering blog, pricing, legal docs, and 15 more developer resources.'
plans:
- name: Alteryx Plans Pricing
  plan_count: 3
  slug: alteryx-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Alteryx Rate Limits
  slug: alteryx-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Alteryx API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: alteryx-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Alteryx API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: alteryx-spectral-rules
scopes:
- name: Alteryx Scopes
  scope_count: 0
  slug: alteryx-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 65.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 13.6
    contract_quality: 58.2
    developer_ergonomics: 57.1
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 15.8
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alteryx/refs/heads/main/screenshots/alteryx-2026-06-20T171552.png
security:
- kind: authentication
  name: Alteryx Authentication
  slug: alteryx-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Alteryx Domain Security
  slug: alteryx-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Alteryx Vulnerability Disclosure
  slug: alteryx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Alteryx Trust Center
  slug: alteryx-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: alteryx
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine-Learning
- Predictive Analytics
use_cases:
- description: Schedule and automate data preparation workflows to generate recurring business reports.
  name: Automated Reporting Pipelines
- description: Migrate workflows and configurations across Server environments using the V1 migration API.
  name: Data Migration
- description: Automate user provisioning, credential management, and workflow deployment through the V3 admin API.
  name: Server Administration Automation
- description: Enable business users to discover and run published workflows through the Gallery API.
  name: Self-Service Analytics
- description: Catalog and discover data assets across the organization using Alteryx Connect APIs.
  name: Enterprise Data Catalog
website: https://help.alteryx.com/current/en/developer-help.html
---
