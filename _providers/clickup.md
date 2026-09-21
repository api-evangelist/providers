---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.7
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 40
  human_in_the_loop: 1
  name: Clickup Agentic Access
  operation_count: 75
  slug: clickup-agentic-access
  summary_line: 75 operations · 40 acting · 1 human-in-the-loop
api_count: 14
apis:
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for retrieving authenticated user information.
  name: clickup Authorization API
  slug: clickup-authorization-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing comments on tasks, views, and lists.
  name: clickup Comments API
  slug: clickup-comments-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for retrieving custom field definitions and setting custom field values on tasks.
  name: clickup Custom Fields API
  slug: clickup-custom-fields-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Folders within ClickUp Spaces.
  name: clickup Folders API
  slug: clickup-folders-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Goals and Key Results within a ClickUp Workspace.
  name: clickup Goals API
  slug: clickup-goals-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Lists within ClickUp Spaces and Folders.
  name: clickup Lists API
  slug: clickup-lists-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Spaces within a ClickUp Workspace.
  name: clickup Spaces API
  slug: clickup-spaces-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting tasks within ClickUp lists and workspaces.
  name: clickup Tasks API
  slug: clickup-tasks-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for retrieving Workspace (team) information and membership.
  name: clickup Teams API
  slug: clickup-teams-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing time entries and timers within a ClickUp Workspace.
  name: clickup Time Tracking API
  slug: clickup-time-tracking-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing views at various levels of the ClickUp hierarchy.
  name: clickup Views API
  slug: clickup-views-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting webhook subscriptions.
  name: clickup Webhooks API
  slug: clickup-webhooks-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for OAuth 2.0 authentication and token management.
  name: Clickup O Auth API
  slug: clickup-oauth-api
- baseURL: https://api.clickup.com/api
  baseurl_source: declared
  description: 'The complete first-party ClickUp public API v2 contract as ClickUp publishes it: 138 operations across 83 paths covering Tasks, Lists, Folders, Spaces, Workspaces, Goals, Views, Comments, Custom Field'
  name: ClickUp API v2
  slug: clickup-api-v2
- baseURL: https://api.clickup.com/
  baseurl_source: declared
  description: 'The first-party ClickUp Public API v3 contract: 35 operations covering Chat channels and messages, Docs and pages, entity Attachments, Workspace audit logs, object ACLs, task moves and per-user time e'
  name: ClickUp Public API v3
  slug: clickup-api-v3
artifact_total: 114
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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/security/clickup-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clickup-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.clickup.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/agentic-access/clickup-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clickup-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/security/clickup-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clickup-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/security/clickup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickup-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/authentication/clickup-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/json-ld/clickup-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clickup-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/json-schema/clickup-task-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clickup-task-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/json-schema/clickup-webhook-payload-schema.json
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clickup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clickup.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clickup.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clickup.com/docs/authentication
- group: operate
  title: ''
  type: Support
  url: https://help.clickup.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://clickup.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.clickup.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickup.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickup.com/terms/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.clickup.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clickup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://clickup.canny.io/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/changelog/clickup-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clickup-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://clickup.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://security.clickup.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/conformance/clickup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clickup-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/well-known/clickup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickup-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/well-known/clickup-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/clickup-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/well-known/clickup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clickup-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/packages/clickup-packages.yml
  title: ''
  type: Packages
  url: packages/clickup-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/mcp/clickup-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clickup-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/mcp/clickup-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clickup-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/llms/clickup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickup-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/errors/clickup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickup-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/errors/clickup-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickup-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/lifecycle/clickup-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clickup-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/scopes/clickup-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clickup-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/conventions/clickup-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clickup-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/data-model/clickup-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clickup-data-model.yml
- group: start
  title: ''
  type: Console
  url: https://developer.clickup.com/docs/trytheapi
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/sandbox/clickup-sandbox.yml
  title: ''
  type: Console
  url: sandbox/clickup-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/rate-limits/clickup-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clickup-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/plans/clickup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clickup-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developer.clickup.com/docs/webhooks
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/clickup-api/clickup-public-api/collection/rekuqnj/clickup-api-v2-reference
created: '2026-05-03'
description: 'ClickUp is a work management platform — tasks, Lists, Folders, Spaces, Docs, Chat, Goals, time tracking, dashboards and automations in one Workspace. It ships a public REST API in two concurrent versions: v2 (138 operations, the broad surface) and v3 (35 operations, Chat, Docs, attachments, audit logs and ACLs), both published as first-party OpenAPI documents and advertised through an RFC 9727 api-catalog at developer.clickup.com. Authentication is a single Authorization header carrying either a personal token or an OAuth 2.0 access token authorized per Workspace; there are no OAuth scopes. Webhooks are HMAC-SHA256 signed. ClickUp also runs a remote MCP server at mcp.clickup.com with its own OAuth authorization server, PKCE and dynamic client registration, exposing 48 documented tools. Rate limits are per token and set by the Workspace plan. There is no sandbox, no idempotency mechanism and no published deprecation policy.'
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
mcp_servers:
- description: ''
  name: Clickup MCP Server
  slug: clickup-mcp-server
modified: '2026-09-17'
name: Clickup
nav: Providers
network: true
overview: 'Clickup publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Comments API, Custom Fields API, and 12 more. Tagged areas include Project Management, Work Management, Productivity, Collaboration, and Task.


  The Clickup catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Clickup''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 42 more developer resources.'
plans:
- name: Clickup Plans Pricing
  plan_count: 6
  slug: clickup-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Clickup Rate Limits
  slug: clickup-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Clickup API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: clickup-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Clickup API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: clickup-jsonschema-spectral-rules
scopes:
- name: Clickup Scopes
  scope_count: 2
  slug: clickup-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 70.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 79.5
    catalog_earned_first_party: 24.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 72.2
    developer_ergonomics: 62.5
    discoverability: 81.5
    operational_transparency: 85.5
  previous_composite: 70.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/screenshots/clickup-2026-06-20T174517.png
security:
- kind: authentication
  name: Clickup Authentication
  slug: clickup-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Clickup Domain Security
  slug: clickup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickup Vulnerability Disclosure
  slug: clickup-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clickup Trust Center
  slug: clickup-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR
slug: clickup
tags:
- Project Management
- Work Management
- Productivity
- Collaboration
- Task
- Documents
- Chat
- Time Tracking
- MCP
website: https://www.clickup.com/
---
