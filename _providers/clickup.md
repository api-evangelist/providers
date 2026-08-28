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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 40
  human_in_the_loop: 1
  name: Clickup Agentic Access
  operation_count: 75
  slug: clickup-agentic-access
  summary_line: 75 operations · 40 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Operations for retrieving authenticated user information.
  name: clickup Authorization API
  slug: clickup-authorization-api
- description: Operations for managing comments on tasks, views, and lists.
  name: clickup Comments API
  slug: clickup-comments-api
- description: Operations for retrieving custom field definitions and setting custom field values on tasks.
  name: clickup Custom Fields API
  slug: clickup-custom-fields-api
- description: Operations for managing Folders within ClickUp Spaces.
  name: clickup Folders API
  slug: clickup-folders-api
- description: Operations for managing Goals and Key Results within a ClickUp Workspace.
  name: clickup Goals API
  slug: clickup-goals-api
- description: Operations for managing Lists within ClickUp Spaces and Folders.
  name: clickup Lists API
  slug: clickup-lists-api
- description: Operations for OAuth 2.0 authentication and token management.
  name: clickup OAuth API
  slug: clickup-oauth-api
- description: Operations for managing Spaces within a ClickUp Workspace.
  name: clickup Spaces API
  slug: clickup-spaces-api
- description: Operations for creating, retrieving, updating, and deleting tasks within ClickUp lists and workspaces.
  name: clickup Tasks API
  slug: clickup-tasks-api
- description: Operations for retrieving Workspace (team) information and membership.
  name: clickup Teams API
  slug: clickup-teams-api
- description: Operations for managing time entries and timers within a ClickUp Workspace.
  name: clickup Time Tracking API
  slug: clickup-time-tracking-api
- description: Operations for managing views at various levels of the ClickUp hierarchy.
  name: clickup Views API
  slug: clickup-views-api
- description: Operations for creating, retrieving, updating, and deleting webhook subscriptions.
  name: clickup Webhooks API
  slug: clickup-webhooks-api
artifact_total: 109
asyncapis:
- description: The ClickUp Webhooks event system delivers real-time notifications when changes occur within a ClickUp Workspace. When subscribed events happen, ClickUp sends HTTP POST requests to a registered endpoi
  name: ClickUp Webhooks Events
  slug: clickup-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClickUp Comments Authorization API
  slug: open-clickup-authorization-api
- collection_type: open
  name: ClickUp Authorization Comments API
  slug: open-clickup-comments-api
- collection_type: open
  name: ClickUp Comments API
  slug: open-clickup-comments
- collection_type: open
  name: ClickUp Comments Authorization Custom Fields API
  slug: open-clickup-custom-fields-api
- collection_type: open
  name: ClickUp Custom Fields API
  slug: open-clickup-custom-fields
- collection_type: open
  name: ClickUp Comments Authorization Folders API
  slug: open-clickup-folders-api
- collection_type: open
  name: ClickUp Folders API
  slug: open-clickup-folders
- collection_type: open
  name: ClickUp Comments Authorization Goals API
  slug: open-clickup-goals-api
- collection_type: open
  name: ClickUp Goals API
  slug: open-clickup-goals
- collection_type: open
  name: ClickUp Comments Authorization Lists API
  slug: open-clickup-lists-api
- collection_type: open
  name: ClickUp Lists API
  slug: open-clickup-lists
- collection_type: open
  name: ClickUp Comments Authorization OAuth API
  slug: open-clickup-oauth-api
- collection_type: open
  name: ClickUp OAuth API
  slug: open-clickup-oauth
- collection_type: open
  name: ClickUp Comments Authorization Spaces API
  slug: open-clickup-spaces-api
- collection_type: open
  name: ClickUp Spaces API
  slug: open-clickup-spaces
- collection_type: open
  name: ClickUp Comments Authorization Tasks API
  slug: open-clickup-tasks-api
- collection_type: open
  name: ClickUp Tasks API
  slug: open-clickup-tasks
- collection_type: open
  name: ClickUp Comments Authorization Teams API
  slug: open-clickup-teams-api
- collection_type: open
  name: ClickUp Teams (Workspaces) API
  slug: open-clickup-teams
- collection_type: open
  name: ClickUp Comments Authorization Time Tracking API
  slug: open-clickup-time-tracking-api
- collection_type: open
  name: ClickUp Time Tracking API
  slug: open-clickup-time-tracking
- collection_type: open
  name: ClickUp Comments Authorization Views API
  slug: open-clickup-views-api
- collection_type: open
  name: ClickUp Views API
  slug: open-clickup-views
- collection_type: open
  name: ClickUp Comments Authorization Webhooks API
  slug: open-clickup-webhooks-api
- collection_type: open
  name: ClickUp Webhooks API
  slug: open-clickup-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickup-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clickup-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickup-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickup-app
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clickup-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clickup-task-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clickup-webhook-payload-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.clickup.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://clickup.com/blog
description: Work with tasks using the ClickUp API.
features:
- 'Free plan: 60MB storage, unlimited tasks/members'
- Unlimited at $7/user/mo annual with unlimited everything
- Business at $12/user/mo with dashboards, automations (5K/mo), Google SSO
- 'Enterprise: SAML/SCIM, MSA/HIPAA, 250K automations/mo, data residency'
- 'REST API v2: 100/min Free, 1000/min Unlimited/Business, 10K/min Enterprise'
- Webhooks for task, list, space, doc events
- OAuth 2.0 and personal API tokens
- Custom Fields API
- Goals, Portfolios, Time Tracking APIs
- Docs, Whiteboards, Forms
- ClickUp Chat (Business+)
- ClickUp AI for content and automation (per-user add-on)
- Sprint management with story points
- Mind maps and Gantt charts
- 1,000+ integrations
- Custom branding and audit log on Enterprise
finops:
- name: Clickup Finops
  service_category: Project Management
  slug: clickup-finops
graphqls:
- description: ClickUp does not offer a native public GraphQL API. The platform exposes its functionality exclusively through a REST API (v2) available at `https://api.clickup.com/api/v2`. There is no publicly docum
  name: ClickUp GraphQL
  slug: clickup-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickup.png
json_schemas:
- name: AuthorizedUser
  property_count: 9
  slug: clickup-authorizeduser
- name: Comment
  property_count: 9
  slug: clickup-comment
- name: CreateCommentRequest
  property_count: 3
  slug: clickup-createcommentrequest
- name: CreateFolderRequest
  property_count: 1
  slug: clickup-createfolderrequest
- name: CreateGoalRequest
  property_count: 6
  slug: clickup-creategoalrequest
- name: CreateKeyResultRequest
  property_count: 8
  slug: clickup-createkeyresultrequest
- name: CreateListRequest
  property_count: 7
  slug: clickup-createlistrequest
- name: CreateSpaceRequest
  property_count: 3
  slug: clickup-createspacerequest
- name: CreateTaskRequest
  property_count: 17
  slug: clickup-createtaskrequest
- name: CreateTimeEntryRequest
  property_count: 8
  slug: clickup-createtimeentryrequest
- name: CreateWebhookRequest
  property_count: 6
  slug: clickup-createwebhookrequest
- name: CustomField
  property_count: 8
  slug: clickup-customfield
- name: CustomFieldDefinition
  property_count: 7
  slug: clickup-customfielddefinition
- name: Folder
  property_count: 11
  slug: clickup-folder
- name: Goal
  property_count: 20
  slug: clickup-goal
- name: GoalFolder
  property_count: 8
  slug: clickup-goalfolder
- name: KeyResult
  property_count: 17
  slug: clickup-keyresult
- name: List
  property_count: 16
  slug: clickup-list
- name: Member
  property_count: 6
  slug: clickup-member
- name: Priority
  property_count: 4
  slug: clickup-priority
- name: Space
  property_count: 11
  slug: clickup-space
- name: Status
  property_count: 5
  slug: clickup-status
- name: Tag
  property_count: 4
  slug: clickup-tag
- name: ClickUp Task
  property_count: 34
  slug: clickup-task
- name: Team
  property_count: 5
  slug: clickup-team
- name: TeamMember
  property_count: 2
  slug: clickup-teammember
- name: TimeEntry
  property_count: 14
  slug: clickup-timeentry
- name: UpdateCommentRequest
  property_count: 3
  slug: clickup-updatecommentrequest
- name: UpdateFolderRequest
  property_count: 1
  slug: clickup-updatefolderrequest
- name: UpdateGoalRequest
  property_count: 6
  slug: clickup-updategoalrequest
- name: UpdateKeyResultRequest
  property_count: 2
  slug: clickup-updatekeyresultrequest
- name: UpdateListRequest
  property_count: 7
  slug: clickup-updatelistrequest
- name: UpdateSpaceRequest
  property_count: 6
  slug: clickup-updatespacerequest
- name: UpdateTaskRequest
  property_count: 13
  slug: clickup-updatetaskrequest
- name: UpdateTimeEntryRequest
  property_count: 8
  slug: clickup-updatetimeentryrequest
- name: UpdateViewRequest
  property_count: 9
  slug: clickup-updateviewrequest
- name: UpdateWebhookRequest
  property_count: 3
  slug: clickup-updatewebhookrequest
- name: User
  property_count: 6
  slug: clickup-user
- name: View
  property_count: 16
  slug: clickup-view
- name: ClickUp Webhook Payload
  property_count: 8
  slug: clickup-webhook-payload
- name: Webhook
  property_count: 12
  slug: clickup-webhook
json_structures:
- name: Clickup Structure
  property_count: 0
  slug: clickup-structure
jsonld:
- class_count: 0
  name: Clickup Context
  property_count: 11
  slug: clickup-context
layout: provider
modified: '2026-05-19'
name: clickup
nav: Providers
network: true
overview: 'clickup publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Comments API, Custom Fields API, and 10 more.


  The clickup catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  clickup''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Clickup Plans Pricing
  plan_count: 4
  slug: clickup-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Clickup Rate Limits
  slug: clickup-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: clickup API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: clickup-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: clickup API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: clickup-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.3
  delta: 1.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 72.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/screenshots/clickup-2026-06-20T174517.png
security:
- kind: authentication
  name: Clickup Authentication
  slug: clickup-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clickup Domain Security
  slug: clickup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clickup Trust Center
  slug: clickup-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR
slug: clickup
---
