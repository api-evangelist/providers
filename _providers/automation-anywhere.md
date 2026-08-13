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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Automation Anywhere Agentic Access
  operation_count: 69
  slug: automation-anywhere-agentic-access
  summary_line: 69 operations · 49 acting
api_count: 22
apis:
- description: The Automation Anywhere Package SDK is a Java-based development toolkit that enables developers to build custom action packages and triggers for the Automation 360 bot editor. Developers use the SDK i
  name: Automation Anywhere Package SDK
  slug: package-sdk
- description: Generate execution URLs and authorization tokens for API Tasks
  name: automation-anywhere AccessDetails API
  slug: automation-anywhere-accessdetails-api
- description: List and manage API Task allocations within the Control Room
  name: automation-anywhere Allocations API
  slug: automation-anywhere-allocations-api
- description: Manage credential attribute values for individual credentials
  name: automation-anywhere AttributeValues API
  slug: automation-anywhere-attributevalues-api
- description: Retrieve Control Room audit trail data
  name: automation-anywhere AuditData API
  slug: automation-anywhere-auditdata-api
- description: Generate, refresh, validate, and revoke JWT tokens for API access
  name: automation-anywhere Authentication API
  slug: automation-anywhere-authentication-api
- description: Retrieve bot execution run data and performance metrics
  name: automation-anywhere BotRunData API
  slug: automation-anywhere-botrundata-api
- description: Create, retrieve, update, delete, and search credentials
  name: automation-anywhere Credentials API
  slug: automation-anywhere-credentials-api
- description: Deploy bots to Bot Runner devices and monitor deployment status
  name: automation-anywhere Deployments API
  slug: automation-anywhere-deployments-api
- description: Manage individual bot files and their dependencies in the repository
  name: automation-anywhere Files API
  slug: automation-anywhere-files-api
- description: Create, update, list, and delete folders in the repository
  name: automation-anywhere Folders API
  slug: automation-anywhere-folders-api
- description: Manage roles with consumer access to locker credentials
  name: automation-anywhere LockerConsumers API
  slug: automation-anywhere-lockerconsumers-api
- description: Manage user membership within lockers
  name: automation-anywhere LockerMembers API
  slug: automation-anywhere-lockermembers-api
- description: Create, retrieve, update, and delete credential lockers
  name: automation-anywhere Lockers API
  slug: automation-anywhere-lockers-api
- description: Manage role-based permissions on repository folders
  name: automation-anywhere Permissions API
  slug: automation-anywhere-permissions-api
- description: Create and manage work item queues and their members
  name: automation-anywhere Queues API
  slug: automation-anywhere-queues-api
- description: Create, list, retrieve, update, and delete user roles
  name: automation-anywhere Roles API
  slug: automation-anywhere-roles-api
- description: Retrieve task metadata, variable profiles, and task-level logs
  name: automation-anywhere TaskData API
  slug: automation-anywhere-taskdata-api
- description: Create, list, retrieve, update, and delete Control Room users
  name: automation-anywhere Users API
  slug: automation-anywhere-users-api
- description: Create and retrieve work item data models defining queue schema
  name: automation-anywhere WorkItemModels API
  slug: automation-anywhere-workitemmodels-api
- description: Add, update, and manage individual work items within queues
  name: automation-anywhere WorkItems API
  slug: automation-anywhere-workitems-api
- description: List and manage content across public and private workspaces
  name: automation-anywhere Workspaces API
  slug: automation-anywhere-workspaces-api
artifact_total: 142
collections:
- collection_type: open
  name: Automation Anywhere API Task Execution API
  slug: open-automation-anywhere-api-task-execution
- collection_type: open
  name: Automation Anywhere Bot Deploy API
  slug: open-automation-anywhere-bot-deploy
- collection_type: open
  name: Automation Anywhere Bot Insight API
  slug: open-automation-anywhere-bot-insight
- collection_type: open
  name: Automation Anywhere Control Room API
  slug: open-automation-anywhere-control-room
- collection_type: open
  name: Automation Anywhere Credential Vault API
  slug: open-automation-anywhere-credential-vault
- collection_type: open
  name: Automation Anywhere Repository Management API
  slug: open-automation-anywhere-repository-management
- collection_type: open
  name: Automation Anywhere Workload Management API
  slug: open-automation-anywhere-workload-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/automation-anywhere-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automation-anywhere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/automation-anywhere-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AutomationAnywhere
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/automation-anywhere
- group: start
  title: ''
  type: Portal
  url: https://developer.automationanywhere.com
- group: company
  title: ''
  type: Website
  url: https://www.automationanywhere.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automationanywhere.com
- group: auth
  title: ''
  type: Authentication
  url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-authentication.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.automationanywhere.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.automationanywhere.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.automationanywhere.com
- group: company
  title: ''
  type: Blog
  url: https://www.automationanywhere.com/blog
- group: design
  title: ''
  type: JSONLD
  url: json-ld/automation-anywhere-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/automation-anywhere-bot-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/automation-anywhere-deployment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/automation-anywhere-work-item-schema.json
description: Automation Anywhere is an enterprise robotic process automation (RPA) platform that enables organizations to automate business processes using software bots. Their developer platform, centered around the Automation 360 Control Room, provides a comprehensive suite of REST APIs for managing bot deployment, workload queues, credentials, repositories, and analytics, as well as an SDK for building custom action packages.
features:
- description: All Control Room APIs use JWT-based authentication. Tokens are obtained via the Authentication API and passed in the X-Authorization or Authorization Bearer header. OAuth 2.0 is supported from v.27 onwards.
  name: JWT Authentication
- description: APIs are versioned (v1, v2, v3, v4) with backwards compatibility maintained for at least two years. Deprecated endpoints are announced with at least one additional year of availability.
  name: Versioned API Endpoints
- description: Each Control Room instance exposes a Swagger UI at /swagger/ for interactive API exploration and testing with live credentials.
  name: Swagger UI Explorer
- description: API Tasks allow RPA bots to be exposed as synchronous REST endpoints, enabling external applications to call bots as microservices with input/output parameter exchange.
  name: API Task Execution
- description: Work item queues allow high-volume data to be fed into RPA pipelines from ERP, CRM, and BPM systems with status tracking and result retrieval.
  name: Workload Queuing
finops:
- name: Automation Anywhere Finops
  service_category: RPA / Intelligent Automation
  slug: automation-anywhere-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automation-anywhere.png
json_schemas:
- name: AccessDetailsRequest
  property_count: 1
  slug: automation-anywhere-accessdetailsrequest
- name: AccessDetailsResponse
  property_count: 2
  slug: automation-anywhere-accessdetailsresponse
- name: ApiTaskAccessDetail
  property_count: 2
  slug: automation-anywhere-apitaskaccessdetail
- name: ApiTaskAllocation
  property_count: 5
  slug: automation-anywhere-apitaskallocation
- name: ApiTaskHeaders
  property_count: 1
  slug: automation-anywhere-apitaskheaders
- name: AssignLabelRequest
  property_count: 2
  slug: automation-anywhere-assignlabelrequest
- name: AttendedRequest
  property_count: 1
  slug: automation-anywhere-attendedrequest
- name: AuditRecord
  property_count: 13
  slug: automation-anywhere-auditrecord
- name: AuditTrailResponse
  property_count: 2
  slug: automation-anywhere-audittrailresponse
- name: AuthenticationRequest
  property_count: 4
  slug: automation-anywhere-authenticationrequest
- name: AuthenticationResponse
  property_count: 2
  slug: automation-anywhere-authenticationresponse
- name: Automation Anywhere Bot
  property_count: 17
  slug: automation-anywhere-bot
- name: BotInputVariable
  property_count: 6
  slug: automation-anywhere-botinputvariable
- name: BotRunDataResponse
  property_count: 2
  slug: automation-anywhere-botrundataresponse
- name: BotRunRecord
  property_count: 14
  slug: automation-anywhere-botrunrecord
- name: CallbackInfo
  property_count: 2
  slug: automation-anywhere-callbackinfo
- name: CreateRoleRequest
  property_count: 3
  slug: automation-anywhere-createrolerequest
- name: CreateUserRequest
  property_count: 8
  slug: automation-anywhere-createuserrequest
- name: Credential
  property_count: 9
  slug: automation-anywhere-credential
- name: CredentialAttribute
  property_count: 5
  slug: automation-anywhere-credentialattribute
- name: CredentialAttributePost
  property_count: 4
  slug: automation-anywhere-credentialattributepost
- name: CredentialAttributeValue
  property_count: 5
  slug: automation-anywhere-credentialattributevalue
- name: CredentialAttributeValueList
  property_count: 1
  slug: automation-anywhere-credentialattributevaluelist
- name: CredentialAttributeValuePost
  property_count: 3
  slug: automation-anywhere-credentialattributevaluepost
- name: CredentialAttributeValuePostList
  property_count: 1
  slug: automation-anywhere-credentialattributevaluepostlist
- name: CredentialAttributeValuePut
  property_count: 1
  slug: automation-anywhere-credentialattributevalueput
- name: CredentialFilterResponse
  property_count: 2
  slug: automation-anywhere-credentialfilterresponse
- name: CredentialPost
  property_count: 3
  slug: automation-anywhere-credentialpost
- name: DependencyUpdateRequest
  property_count: 1
  slug: automation-anywhere-dependencyupdaterequest
- name: Automation Anywhere Bot Deployment
  property_count: 13
  slug: automation-anywhere-deployment
- name: DeploymentRequest
  property_count: 12
  slug: automation-anywhere-deploymentrequest
- name: DeploymentResponse
  property_count: 1
  slug: automation-anywhere-deploymentresponse
- name: Error
  property_count: 2
  slug: automation-anywhere-error
- name: ErrorMessage
  property_count: 2
  slug: automation-anywhere-errormessage
- name: FileDependencyResponse
  property_count: 1
  slug: automation-anywhere-filedependencyresponse
- name: FileListResponse
  property_count: 2
  slug: automation-anywhere-filelistresponse
- name: FileParentsResponse
  property_count: 1
  slug: automation-anywhere-fileparentsresponse
- name: FilterExpression
  property_count: 2
  slug: automation-anywhere-filterexpression
- name: FilterOperand
  property_count: 2
  slug: automation-anywhere-filteroperand
- name: FilterRequest
  property_count: 4
  slug: automation-anywhere-filterrequest
- name: FolderRequest
  property_count: 2
  slug: automation-anywhere-folderrequest
- name: HeadlessRequest
  property_count: 1
  slug: automation-anywhere-headlessrequest
- name: ListAllocationsRequest
  property_count: 1
  slug: automation-anywhere-listallocationsrequest
- name: ListAllocationsResponse
  property_count: 2
  slug: automation-anywhere-listallocationsresponse
- name: Locker
  property_count: 8
  slug: automation-anywhere-locker
- name: LockerConsumer
  property_count: 2
  slug: automation-anywhere-lockerconsumer
- name: LockerConsumerList
  property_count: 1
  slug: automation-anywhere-lockerconsumerlist
- name: LockerConsumerPost
  property_count: 1
  slug: automation-anywhere-lockerconsumerpost
- name: LockerCredentialList
  property_count: 1
  slug: automation-anywhere-lockercredentiallist
- name: LockerCredentialUpdate
  property_count: 1
  slug: automation-anywhere-lockercredentialupdate
- name: LockerListResponse
  property_count: 2
  slug: automation-anywhere-lockerlistresponse
- name: LockerMember
  property_count: 3
  slug: automation-anywhere-lockermember
- name: LockerMemberList
  property_count: 1
  slug: automation-anywhere-lockermemberlist
- name: LockerMemberUpdate
  property_count: 1
  slug: automation-anywhere-lockermemberupdate
- name: LockerPost
  property_count: 2
  slug: automation-anywhere-lockerpost
- name: ObjectPermission
  property_count: 6
  slug: automation-anywhere-objectpermission
- name: PackageVersionUpdateRequest
  property_count: 3
  slug: automation-anywhere-packageversionupdaterequest
- name: PageInfo
  property_count: 3
  slug: automation-anywhere-pageinfo
- name: PageRequest
  property_count: 2
  slug: automation-anywhere-pagerequest
- name: Permission
  property_count: 4
  slug: automation-anywhere-permission
- name: PermissionsUpdateRequest
  property_count: 1
  slug: automation-anywhere-permissionsupdaterequest
- name: Queue
  property_count: 17
  slug: automation-anywhere-queue
- name: QueueConsumer
  property_count: 2
  slug: automation-anywhere-queueconsumer
- name: QueueConsumerRequest
  property_count: 1
  slug: automation-anywhere-queueconsumerrequest
- name: QueueExpiry
  property_count: 3
  slug: automation-anywhere-queueexpiry
- name: QueueMember
  property_count: 2
  slug: automation-anywhere-queuemember
- name: QueueMemberRequest
  property_count: 1
  slug: automation-anywhere-queuememberrequest
- name: QueueParticipantRequest
  property_count: 1
  slug: automation-anywhere-queueparticipantrequest
- name: RecoverRequest
  property_count: 2
  slug: automation-anywhere-recoverrequest
- name: RepositoryObject
  property_count: 13
  slug: automation-anywhere-repositoryobject
- name: RepositoryPermissions
  property_count: 2
  slug: automation-anywhere-repositorypermissions
- name: RoleListResponse
  property_count: 2
  slug: automation-anywhere-rolelistresponse
- name: RoleRef
  property_count: 2
  slug: automation-anywhere-roleref
- name: RoleResponse
  property_count: 8
  slug: automation-anywhere-roleresponse
- name: RunAsUser
  property_count: 1
  slug: automation-anywhere-runasuser
- name: SortCriteria
  property_count: 2
  slug: automation-anywhere-sortcriteria
- name: TaskLogDataResponse
  property_count: 2
  slug: automation-anywhere-tasklogdataresponse
- name: TaskLogRecord
  property_count: 4
  slug: automation-anywhere-tasklogrecord
- name: TaskMetadataResponse
  property_count: 2
  slug: automation-anywhere-taskmetadataresponse
- name: TaskVariable
  property_count: 3
  slug: automation-anywhere-taskvariable
- name: TaskVariableProfileResponse
  property_count: 4
  slug: automation-anywhere-taskvariableprofileresponse
- name: TokenValidationResponse
  property_count: 1
  slug: automation-anywhere-tokenvalidationresponse
- name: UnattendedRequest
  property_count: 2
  slug: automation-anywhere-unattendedrequest
- name: UpdateRoleRequest
  property_count: 3
  slug: automation-anywhere-updaterolerequest
- name: UpdateUserRequest
  property_count: 7
  slug: automation-anywhere-updateuserrequest
- name: UpdateWorkItemRequest
  property_count: 6
  slug: automation-anywhere-updateworkitemrequest
- name: UserListResponse
  property_count: 2
  slug: automation-anywhere-userlistresponse
- name: UserResponse
  property_count: 12
  slug: automation-anywhere-userresponse
- name: UserSummary
  property_count: 4
  slug: automation-anywhere-usersummary
- name: VariableProfile
  property_count: 3
  slug: automation-anywhere-variableprofile
- name: Automation Anywhere Work Item
  property_count: 27
  slug: automation-anywhere-work-item
- name: WorkItem
  property_count: 20
  slug: automation-anywhere-workitem
- name: WorkItemAttribute
  property_count: 4
  slug: automation-anywhere-workitemattribute
- name: WorkItemModel
  property_count: 10
  slug: automation-anywhere-workitemmodel
json_structures:
- name: Automation Anywhere Structure
  property_count: 0
  slug: automation-anywhere-structure
jsonld:
- class_count: 0
  name: Automation Anywhere Context
  property_count: 10
  slug: automation-anywhere-context
layout: provider
modified: '2026-05-19'
name: automation-anywhere
nav: Providers
network: true
overview: 'automation-anywhere publishes 21 APIs on the [APIs.io](https://apis.io/) network, including AccessDetails API, Allocations API, AttributeValues API, and 18 more.


  The automation-anywhere catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  automation-anywhere''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Automation Anywhere Plans Pricing
  plan_count: 4
  slug: automation-anywhere-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 2
  name: Automation Anywhere Rate Limits
  slug: automation-anywhere-rate-limits
rules:
- name: automation-anywhere API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: automation-anywhere-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 72.2
    developer_ergonomics: 34.8
    discoverability: 40.7
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/screenshots/automation-anywhere-2026-06-20T172657.png
security:
- kind: authentication
  name: Automation Anywhere Authentication
  slug: automation-anywhere-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Automation Anywhere Domain Security
  slug: automation-anywhere-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: automation-anywhere
use_cases:
- description: Automate bot deployment across dev, test, and production environments using the Bot Deploy and Repository Management APIs in CI/CD pipelines.
  name: DevOps Bot Pipeline
- description: Connect ERP, CRM, and BPM systems to RPA workload queues to distribute and process high-volume transactional data with Automation Anywhere bots.
  name: Enterprise System Integration
- description: Feed Bot Insight API data into Tableau, Power BI, or Splunk for real-time RPA operational dashboards and business KPI tracking.
  name: Bot Performance Monitoring
- description: Programmatically provision and rotate bot credentials in the Credential Vault from enterprise secrets management systems like CyberArk or HashiCorp Vault.
  name: Credential Governance
- description: Build proprietary Java action packages using the Package SDK to extend Automation 360 with custom connectors for legacy or specialized systems.
  name: Custom Action Packages
website: https://www.automationanywhere.com
---
