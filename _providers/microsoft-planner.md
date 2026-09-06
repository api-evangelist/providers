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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 29.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Microsoft Planner Agentic Access
  operation_count: 22
  slug: microsoft-planner-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- description: Beta version of the Planner API in Microsoft Graph providing access to preview features including plannerRoster resources, business scenarios integration, and expanded container type support.
  name: Microsoft Graph Planner API (Beta)
  slug: microsoft-graph-planner-api-beta
- description: Beta API for integrating external business processes with Microsoft Planner through business scenarios, allowing creation of scenario-controlled Planner tasks and plans.
  name: Microsoft Graph Business Scenarios Planner API (Beta)
  slug: microsoft-graph-business-scenarios-planner-api-beta
- baseURL: https://graph.microsoft.com/v1.0/planner
  baseurl_source: declared
  description: Operations for managing Planner buckets
  name: Microsoft Planner Buckets API
  slug: microsoft-planner-buckets-api
- baseURL: https://graph.microsoft.com/v1.0/planner
  baseurl_source: declared
  description: Operations for managing additional plan details
  name: Microsoft Planner Plan Details API
  slug: microsoft-planner-plan-details-api
- baseURL: https://graph.microsoft.com/v1.0/planner
  baseurl_source: declared
  description: Operations for managing Planner plans
  name: Microsoft Planner Plans API
  slug: microsoft-planner-plans-api
- baseURL: https://graph.microsoft.com/v1.0/planner
  baseurl_source: declared
  description: Operations for managing additional task details
  name: Microsoft Planner Task Details API
  slug: microsoft-planner-task-details-api
- baseURL: https://graph.microsoft.com/v1.0/planner
  baseurl_source: declared
  description: Operations for managing Planner tasks
  name: Microsoft Planner Tasks API
  slug: microsoft-planner-tasks-api
arazzos:
- description: Confirm a plan exists, create a new bucket in it, then add a task to that bucket.
  name: Microsoft Planner Add a Bucket and Task to an Existing Plan
  slug: microsoft-planner-add-bucket-task-to-plan-workflow
- description: List tasks assigned to the signed-in user and, if any exist, mark the first one complete.
  name: Microsoft Planner Complete My First Assigned Task
  slug: microsoft-planner-complete-my-first-task-workflow
- description: Read a task to capture its ETag, then patch it to 100 percent complete.
  name: Microsoft Planner Mark a Task Complete
  slug: microsoft-planner-complete-task-workflow
- description: Create a plan in a group, add a bucket to it, then create the first task in that bucket.
  name: Microsoft Planner Stand Up a Plan with a Bucket and First Task
  slug: microsoft-planner-create-plan-bucket-task-workflow
- description: Create a task in a plan, then read and update its task details with a description and checklist.
  name: Microsoft Planner Create a Task and Populate Its Details
  slug: microsoft-planner-create-task-with-details-workflow
- description: List a group's plans, pick the first plan, and list that plan's tasks and buckets.
  name: Microsoft Planner Drill From Group to Plan to Tasks
  slug: microsoft-planner-list-group-plan-tasks-workflow
- description: Confirm the target bucket exists, read the task ETag, then reassign the task to that bucket.
  name: Microsoft Planner Move a Task Into a Different Bucket
  slug: microsoft-planner-move-task-to-bucket-workflow
- description: Read a plan and its details for ETags, rename the plan, then set category label descriptions.
  name: Microsoft Planner Rename a Plan and Describe Its Categories
  slug: microsoft-planner-rename-plan-workflow
artifact_total: 196
collections:
- collection_type: postman
  name: Microsoft Planner Microsoft Graph Planner API
  slug: postman-microsoft-planner
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Planner Microsoft Graph Planner Buckets API
  slug: open-microsoft-planner-buckets-api
- collection_type: open
  name: Microsoft Planner Microsoft Graph Planner Buckets Plan Details API
  slug: open-microsoft-planner-plan-details-api
- collection_type: open
  name: Microsoft Planner Microsoft Graph Planner Buckets Plans API
  slug: open-microsoft-planner-plans-api
- collection_type: open
  name: Microsoft Planner Microsoft Graph Planner Buckets Task Details API
  slug: open-microsoft-planner-task-details-api
- collection_type: open
  name: Microsoft Planner Microsoft Graph Planner Buckets Tasks API
  slug: open-microsoft-planner-tasks-api
- collection_type: open
  name: Microsoft Planner Microsoft Graph Planner API
  slug: open-microsoft-planner
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-planner-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-planner-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-planner-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-planner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-planner-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-planner-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-planner/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-add-bucket-task-to-plan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-complete-my-first-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-complete-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-create-plan-bucket-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-create-task-with-details-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-list-group-plan-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-move-task-to-bucket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-planner-rename-plan-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/graph/blogs/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.microsoft.com/en-us/graph/status
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
- group: start
  title: ''
  type: Login
  url: https://planner.cloud.microsoft
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us/planner
- group: operate
  title: ''
  type: FAQ
  url: https://support.microsoft.com/en-us/office/frequently-asked-questions-about-microsoft-planner-d1a2d4e6-a4d7-408c-a48a-31caaa267de5
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: start
  title: ''
  type: Signup
  url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
- group: start
  title: ''
  type: Sandbox
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/microsoft-planner-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-planner-task-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/microsoft-planner-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-planner-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-planner-vocabulary.yaml
created: '2024-01-01'
description: Microsoft Planner is a task management tool that helps teams organize work, assign tasks, share files, and collaborate on projects within Microsoft 365.
examples:
- key_count: 6
  name: Microsoft Planner Createbucket Example
  slug: microsoft-planner-createbucket-example
- key_count: 6
  name: Microsoft Planner Createplan Example
  slug: microsoft-planner-createplan-example
- key_count: 6
  name: Microsoft Planner Createtask Example
  slug: microsoft-planner-createtask-example
- key_count: 6
  name: Microsoft Planner Getbucket Example
  slug: microsoft-planner-getbucket-example
- key_count: 6
  name: Microsoft Planner Getplan Example
  slug: microsoft-planner-getplan-example
- key_count: 6
  name: Microsoft Planner Getplandetails Example
  slug: microsoft-planner-getplandetails-example
- key_count: 6
  name: Microsoft Planner Gettask Example
  slug: microsoft-planner-gettask-example
- key_count: 6
  name: Microsoft Planner Gettaskdetails Example
  slug: microsoft-planner-gettaskdetails-example
- key_count: 2
  name: Microsoft Planner Identity Example
  slug: microsoft-planner-identity-example
- key_count: 0
  name: Microsoft Planner Identity Set Example
  slug: microsoft-planner-identity-set-example
- key_count: 6
  name: Microsoft Planner Listbuckettasks Example
  slug: microsoft-planner-listbuckettasks-example
- key_count: 6
  name: Microsoft Planner Listgroupplans Example
  slug: microsoft-planner-listgroupplans-example
- key_count: 6
  name: Microsoft Planner Listmytasks Example
  slug: microsoft-planner-listmytasks-example
- key_count: 6
  name: Microsoft Planner Listplanbuckets Example
  slug: microsoft-planner-listplanbuckets-example
- key_count: 6
  name: Microsoft Planner Listplantasks Example
  slug: microsoft-planner-listplantasks-example
- key_count: 6
  name: Microsoft Planner Listusertasks Example
  slug: microsoft-planner-listusertasks-example
- key_count: 1
  name: Microsoft Planner O Data Error Example
  slug: microsoft-planner-o-data-error-example
- key_count: 0
  name: Microsoft Planner Planner Applied Categories Example
  slug: microsoft-planner-planner-applied-categories-example
- key_count: 3
  name: Microsoft Planner Planner Assignment Example
  slug: microsoft-planner-planner-assignment-example
- key_count: 0
  name: Microsoft Planner Planner Assignments Example
  slug: microsoft-planner-planner-assignments-example
- key_count: 3
  name: Microsoft Planner Planner Bucket Collection Example
  slug: microsoft-planner-planner-bucket-collection-example
- key_count: 3
  name: Microsoft Planner Planner Bucket Create Example
  slug: microsoft-planner-planner-bucket-create-example
- key_count: 5
  name: Microsoft Planner Planner Bucket Example
  slug: microsoft-planner-planner-bucket-example
- key_count: 2
  name: Microsoft Planner Planner Bucket Update Example
  slug: microsoft-planner-planner-bucket-update-example
- key_count: 25
  name: Microsoft Planner Planner Category Descriptions Example
  slug: microsoft-planner-planner-category-descriptions-example
- key_count: 5
  name: Microsoft Planner Planner Checklist Item Example
  slug: microsoft-planner-planner-checklist-item-example
- key_count: 0
  name: Microsoft Planner Planner Checklist Items Example
  slug: microsoft-planner-planner-checklist-items-example
- key_count: 5
  name: Microsoft Planner Planner External Reference Example
  slug: microsoft-planner-planner-external-reference-example
- key_count: 0
  name: Microsoft Planner Planner External References Example
  slug: microsoft-planner-planner-external-references-example
- key_count: 3
  name: Microsoft Planner Planner Plan Collection Example
  slug: microsoft-planner-planner-plan-collection-example
- key_count: 3
  name: Microsoft Planner Planner Plan Container Example
  slug: microsoft-planner-planner-plan-container-example
- key_count: 2
  name: Microsoft Planner Planner Plan Create Example
  slug: microsoft-planner-planner-plan-create-example
- key_count: 2
  name: Microsoft Planner Planner Plan Details Example
  slug: microsoft-planner-planner-plan-details-example
- key_count: 0
  name: Microsoft Planner Planner Plan Details Update Example
  slug: microsoft-planner-planner-plan-details-update-example
- key_count: 5
  name: Microsoft Planner Planner Plan Example
  slug: microsoft-planner-planner-plan-example
- key_count: 1
  name: Microsoft Planner Planner Plan Update Example
  slug: microsoft-planner-planner-plan-update-example
- key_count: 3
  name: Microsoft Planner Planner Task Collection Example
  slug: microsoft-planner-planner-task-collection-example
- key_count: 10
  name: Microsoft Planner Planner Task Create Example
  slug: microsoft-planner-planner-task-create-example
- key_count: 4
  name: Microsoft Planner Planner Task Details Example
  slug: microsoft-planner-planner-task-details-example
- key_count: 2
  name: Microsoft Planner Planner Task Details Update Example
  slug: microsoft-planner-planner-task-details-update-example
- key_count: 19
  name: Microsoft Planner Planner Task Example
  slug: microsoft-planner-planner-task-example
- key_count: 10
  name: Microsoft Planner Planner Task Update Example
  slug: microsoft-planner-planner-task-update-example
- key_count: 0
  name: Microsoft Planner Planner User Ids Example
  slug: microsoft-planner-planner-user-ids-example
- key_count: 6
  name: Microsoft Planner Updatebucket Example
  slug: microsoft-planner-updatebucket-example
- key_count: 6
  name: Microsoft Planner Updateplan Example
  slug: microsoft-planner-updateplan-example
- key_count: 6
  name: Microsoft Planner Updateplandetails Example
  slug: microsoft-planner-updateplandetails-example
- key_count: 6
  name: Microsoft Planner Updatetask Example
  slug: microsoft-planner-updatetask-example
- key_count: 6
  name: Microsoft Planner Updatetaskdetails Example
  slug: microsoft-planner-updatetaskdetails-example
features:
- Visual task boards with drag-and-drop organization
- Plan creation tied to Microsoft 365 Groups
- Task assignment with due dates and priorities
- Bucket-based task categorization and organization
- Checklist subtasks within individual tasks
- File attachment and external reference linking
- Progress tracking with charts and status views
- Microsoft Teams integration for collaborative planning
- Category labels for cross-cutting task classification
- Microsoft Graph API for programmatic access
finops:
- name: Microsoft Planner Finops
  service_category: Project and Task Management
  slug: microsoft-planner-finops
image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
integrations:
- Microsoft Teams for in-chat task management
- Microsoft To Do for personal task sync
- Power Automate for workflow automation
- SharePoint for document-linked tasks
- Outlook for email-to-task conversion
- Excel for data export and reporting
- Power BI for advanced analytics dashboards
- Azure DevOps for development task bridging
json_schemas:
- name: Identity
  property_count: 2
  slug: microsoft-planner-identity
- name: IdentitySet
  property_count: 0
  slug: microsoft-planner-identity-set
- name: IdentitySet
  property_count: 3
  slug: microsoft-planner-identityset
- name: ODataError
  property_count: 1
  slug: microsoft-planner-o-data-error
- name: ODataError
  property_count: 1
  slug: microsoft-planner-odataerror
- name: PlannerAppliedCategories
  property_count: 0
  slug: microsoft-planner-planner-applied-categories
- name: PlannerAssignment
  property_count: 3
  slug: microsoft-planner-planner-assignment
- name: PlannerAssignments
  property_count: 0
  slug: microsoft-planner-planner-assignments
- name: PlannerBucketCollection
  property_count: 3
  slug: microsoft-planner-planner-bucket-collection
- name: PlannerBucketCreate
  property_count: 3
  slug: microsoft-planner-planner-bucket-create
- name: PlannerBucket
  property_count: 5
  slug: microsoft-planner-planner-bucket
- name: PlannerBucketUpdate
  property_count: 2
  slug: microsoft-planner-planner-bucket-update
- name: PlannerCategoryDescriptions
  property_count: 25
  slug: microsoft-planner-planner-category-descriptions
- name: PlannerChecklistItem
  property_count: 5
  slug: microsoft-planner-planner-checklist-item
- name: PlannerChecklistItems
  property_count: 0
  slug: microsoft-planner-planner-checklist-items
- name: PlannerExternalReference
  property_count: 5
  slug: microsoft-planner-planner-external-reference
- name: PlannerExternalReferences
  property_count: 0
  slug: microsoft-planner-planner-external-references
- name: PlannerPlanCollection
  property_count: 3
  slug: microsoft-planner-planner-plan-collection
- name: PlannerPlanContainer
  property_count: 3
  slug: microsoft-planner-planner-plan-container
- name: PlannerPlanCreate
  property_count: 2
  slug: microsoft-planner-planner-plan-create
- name: PlannerPlanDetails
  property_count: 2
  slug: microsoft-planner-planner-plan-details
- name: PlannerPlanDetailsUpdate
  property_count: 0
  slug: microsoft-planner-planner-plan-details-update
- name: PlannerPlan
  property_count: 5
  slug: microsoft-planner-planner-plan
- name: PlannerPlanUpdate
  property_count: 1
  slug: microsoft-planner-planner-plan-update
- name: PlannerTaskCollection
  property_count: 3
  slug: microsoft-planner-planner-task-collection
- name: PlannerTaskCreate
  property_count: 10
  slug: microsoft-planner-planner-task-create
- name: PlannerTaskDetails
  property_count: 4
  slug: microsoft-planner-planner-task-details
- name: PlannerTaskDetailsUpdate
  property_count: 2
  slug: microsoft-planner-planner-task-details-update
- name: PlannerTask
  property_count: 19
  slug: microsoft-planner-planner-task
- name: PlannerTaskUpdate
  property_count: 10
  slug: microsoft-planner-planner-task-update
- name: PlannerUserIds
  property_count: 0
  slug: microsoft-planner-planner-user-ids
- name: PlannerAppliedCategories
  property_count: 0
  slug: microsoft-planner-plannerappliedcategories
- name: PlannerAssignment
  property_count: 4
  slug: microsoft-planner-plannerassignment
- name: PlannerAssignments
  property_count: 0
  slug: microsoft-planner-plannerassignments
- name: PlannerBucket
  property_count: 5
  slug: microsoft-planner-plannerbucket
- name: PlannerBucketCollection
  property_count: 3
  slug: microsoft-planner-plannerbucketcollection
- name: PlannerBucketCreate
  property_count: 3
  slug: microsoft-planner-plannerbucketcreate
- name: PlannerBucketUpdate
  property_count: 2
  slug: microsoft-planner-plannerbucketupdate
- name: PlannerCategoryDescriptions
  property_count: 25
  slug: microsoft-planner-plannercategorydescriptions
- name: PlannerChecklistItem
  property_count: 6
  slug: microsoft-planner-plannerchecklistitem
- name: PlannerChecklistItems
  property_count: 0
  slug: microsoft-planner-plannerchecklistitems
- name: PlannerExternalReference
  property_count: 6
  slug: microsoft-planner-plannerexternalreference
- name: PlannerExternalReferences
  property_count: 0
  slug: microsoft-planner-plannerexternalreferences
- name: PlannerPlan
  property_count: 7
  slug: microsoft-planner-plannerplan
- name: PlannerPlanCollection
  property_count: 3
  slug: microsoft-planner-plannerplancollection
- name: PlannerPlanContainer
  property_count: 3
  slug: microsoft-planner-plannerplancontainer
- name: PlannerPlanCreate
  property_count: 2
  slug: microsoft-planner-plannerplancreate
- name: PlannerPlanDetails
  property_count: 4
  slug: microsoft-planner-plannerplandetails
- name: PlannerPlanDetailsUpdate
  property_count: 2
  slug: microsoft-planner-plannerplandetailsupdate
- name: PlannerPlanUpdate
  property_count: 1
  slug: microsoft-planner-plannerplanupdate
- name: PlannerTask
  property_count: 23
  slug: microsoft-planner-plannertask
- name: PlannerTaskCollection
  property_count: 3
  slug: microsoft-planner-plannertaskcollection
- name: PlannerTaskCreate
  property_count: 12
  slug: microsoft-planner-plannertaskcreate
- name: PlannerTaskDetails
  property_count: 6
  slug: microsoft-planner-plannertaskdetails
- name: PlannerTaskDetailsUpdate
  property_count: 4
  slug: microsoft-planner-plannertaskdetailsupdate
- name: PlannerTaskUpdate
  property_count: 12
  slug: microsoft-planner-plannertaskupdate
- name: PlannerUserIds
  property_count: 0
  slug: microsoft-planner-planneruserids
- name: Microsoft Planner Task
  property_count: 23
  slug: microsoft-planner-task
json_structures:
- name: Microsoft Planner Identity Set Structure
  property_count: 0
  slug: microsoft-planner-identity-set-structure
- name: Microsoft Planner Identity Structure
  property_count: 2
  slug: microsoft-planner-identity-structure
- name: Microsoft Planner O Data Error Structure
  property_count: 1
  slug: microsoft-planner-o-data-error-structure
- name: Microsoft Planner Planner Applied Categories Structure
  property_count: 0
  slug: microsoft-planner-planner-applied-categories-structure
- name: Microsoft Planner Planner Assignment Structure
  property_count: 3
  slug: microsoft-planner-planner-assignment-structure
- name: Microsoft Planner Planner Assignments Structure
  property_count: 0
  slug: microsoft-planner-planner-assignments-structure
- name: Microsoft Planner Planner Bucket Collection Structure
  property_count: 3
  slug: microsoft-planner-planner-bucket-collection-structure
- name: Microsoft Planner Planner Bucket Create Structure
  property_count: 3
  slug: microsoft-planner-planner-bucket-create-structure
- name: Microsoft Planner Planner Bucket Structure
  property_count: 5
  slug: microsoft-planner-planner-bucket-structure
- name: Microsoft Planner Planner Bucket Update Structure
  property_count: 2
  slug: microsoft-planner-planner-bucket-update-structure
- name: Microsoft Planner Planner Category Descriptions Structure
  property_count: 25
  slug: microsoft-planner-planner-category-descriptions-structure
- name: Microsoft Planner Planner Checklist Item Structure
  property_count: 5
  slug: microsoft-planner-planner-checklist-item-structure
- name: Microsoft Planner Planner Checklist Items Structure
  property_count: 0
  slug: microsoft-planner-planner-checklist-items-structure
- name: Microsoft Planner Planner External Reference Structure
  property_count: 5
  slug: microsoft-planner-planner-external-reference-structure
- name: Microsoft Planner Planner External References Structure
  property_count: 0
  slug: microsoft-planner-planner-external-references-structure
- name: Microsoft Planner Planner Plan Collection Structure
  property_count: 3
  slug: microsoft-planner-planner-plan-collection-structure
- name: Microsoft Planner Planner Plan Container Structure
  property_count: 3
  slug: microsoft-planner-planner-plan-container-structure
- name: Microsoft Planner Planner Plan Create Structure
  property_count: 2
  slug: microsoft-planner-planner-plan-create-structure
- name: Microsoft Planner Planner Plan Details Structure
  property_count: 2
  slug: microsoft-planner-planner-plan-details-structure
- name: Microsoft Planner Planner Plan Details Update Structure
  property_count: 0
  slug: microsoft-planner-planner-plan-details-update-structure
- name: Microsoft Planner Planner Plan Structure
  property_count: 5
  slug: microsoft-planner-planner-plan-structure
- name: Microsoft Planner Planner Plan Update Structure
  property_count: 1
  slug: microsoft-planner-planner-plan-update-structure
- name: Microsoft Planner Planner Task Collection Structure
  property_count: 3
  slug: microsoft-planner-planner-task-collection-structure
- name: Microsoft Planner Planner Task Create Structure
  property_count: 10
  slug: microsoft-planner-planner-task-create-structure
- name: Microsoft Planner Planner Task Details Structure
  property_count: 4
  slug: microsoft-planner-planner-task-details-structure
- name: Microsoft Planner Planner Task Details Update Structure
  property_count: 2
  slug: microsoft-planner-planner-task-details-update-structure
- name: Microsoft Planner Planner Task Structure
  property_count: 19
  slug: microsoft-planner-planner-task-structure
- name: Microsoft Planner Planner Task Update Structure
  property_count: 10
  slug: microsoft-planner-planner-task-update-structure
- name: Microsoft Planner Planner User Ids Structure
  property_count: 0
  slug: microsoft-planner-planner-user-ids-structure
- name: Microsoft Planner Structure
  property_count: 0
  slug: microsoft-planner-structure
jsonld:
- class_count: 0
  name: Microsoft Planner Context
  property_count: 0
  slug: microsoft-planner-context
layout: provider
modified: '2026-05-19'
name: Microsoft Planner
nav: Providers
network: true
overview: 'Microsoft Planner publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Buckets API, Plan Details API, Plans API, and 2 more. Tagged areas include Collaboration, Microsoft-365, Productivity, Project Management, and Task Management.


  The Microsoft Planner catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Planner''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, documentation, support, FAQ, and 30 more developer resources.'
plans:
- name: Microsoft Planner Plans Pricing
  plan_count: 4
  slug: microsoft-planner-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Microsoft Planner Rate Limits
  slug: microsoft-planner-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Microsoft Planner API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-planner-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Microsoft Planner API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: microsoft-planner-spectral-rules
scopes:
- name: Microsoft Planner Scopes
  scope_count: 6
  slug: microsoft-planner-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 28.8
    contract_quality: 75.3
    developer_ergonomics: 82.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-planner/refs/heads/main/screenshots/microsoft-planner-2026-06-20T185518.png
security:
- kind: authentication
  name: Microsoft Planner Authentication
  slug: microsoft-planner-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Planner Domain Security
  slug: microsoft-planner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Planner Vulnerability Disclosure
  slug: microsoft-planner-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-planner
tags:
- Collaboration
- Microsoft-365
- Productivity
- Project Management
- Task Management
use_cases:
- Project management for team-based work coordination
- Sprint planning and agile task tracking
- Onboarding workflows for new employees
- Event planning with task delegation and deadlines
- Content publishing calendars and editorial workflows
- IT helpdesk ticket organization and tracking
- Marketing campaign task management
- Cross-functional team collaboration on initiatives
website: https://developer.microsoft.com/en-us/graph
---
