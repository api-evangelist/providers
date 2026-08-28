---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 41
  human_in_the_loop: 0
  name: Basecamp Agentic Access
  operation_count: 77
  slug: basecamp-agentic-access
  summary_line: 77 operations · 41 acting
api_count: 20
apis:
- description: Basecamp Webhooks deliver real-time HTTP notifications when events occur within a project. Configure webhooks per project with an HTTPS payload URL and resource types.
  name: Basecamp Webhooks
  slug: basecamp-webhooks
- description: OAuth 2.0 authorization code flow endpoints
  name: Basecamp Authorization API
  slug: basecamp-authorization-api
- description: Manage project campfire chat rooms and lines
  name: Basecamp Campfires API
  slug: basecamp-campfires-api
- description: Manage kanban-style card tables and card movements
  name: Basecamp Card Tables API
  slug: basecamp-card-tables-api
- description: Manage comments on any commentable recording
  name: Basecamp Comments API
  slug: basecamp-comments-api
- description: Manage documents stored in vaults
  name: Basecamp Documents API
  slug: basecamp-documents-api
- description: Retrieve authenticated user identity
  name: Basecamp Identity API
  slug: basecamp-identity-api
- description: Manage messages on message boards
  name: Basecamp Messages API
  slug: basecamp-messages-api
- description: Manage people, profiles, and project access
  name: Basecamp People API
  slug: basecamp-people-api
- description: Manage Basecamp projects (buckets)
  name: Basecamp Projects API
  slug: basecamp-projects-api
- description: Common actions for all recordable resources (archive, trash, restore)
  name: Basecamp Recordings API
  slug: basecamp-recordings-api
- description: Manage individual schedule events and recurring entries
  name: Basecamp Schedule Entries API
  slug: basecamp-schedule-entries-api
- description: Manage project schedules
  name: Basecamp Schedules API
  slug: basecamp-schedules-api
- description: Manage per-recording notification subscriptions
  name: Basecamp Subscriptions API
  slug: basecamp-subscriptions-api
- description: Manage project templates and construct projects from them
  name: Basecamp Templates API
  slug: basecamp-templates-api
- description: Manage to-do lists within a to-do set
  name: Basecamp To-Do Lists API
  slug: basecamp-to-do-lists-api
- description: Manage individual to-do items
  name: Basecamp To-Dos API
  slug: basecamp-to-dos-api
- description: Token exchange and refresh endpoints
  name: Basecamp Token API
  slug: basecamp-token-api
- description: Manage file uploads stored in vaults
  name: Basecamp Uploads API
  slug: basecamp-uploads-api
- description: Manage webhook subscriptions for a project
  name: Basecamp Webhooks API
  slug: basecamp-webhooks-api
artifact_total: 208
asyncapis:
- description: 'The Basecamp webhook system delivers real-time HTTP notifications to registered HTTPS endpoints when events occur within a Basecamp project. Webhooks are configured per project with a payload URL and '
  name: Basecamp Webhook Events
  slug: basecamp-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Basecamp API
  slug: open-basecamp-api
- collection_type: open
  name: Basecamp Authorization API
  slug: open-basecamp-authorization-api
- collection_type: open
  name: Basecamp Authorization Campfires API
  slug: open-basecamp-campfires-api
- collection_type: open
  name: Basecamp Authorization Card Tables API
  slug: open-basecamp-card-tables-api
- collection_type: open
  name: Basecamp Authorization Comments API
  slug: open-basecamp-comments-api
- collection_type: open
  name: Basecamp Authorization Documents API
  slug: open-basecamp-documents-api
- collection_type: open
  name: Basecamp Authorization Identity API
  slug: open-basecamp-identity-api
- collection_type: open
  name: Basecamp Authorization Messages API
  slug: open-basecamp-messages-api
- collection_type: open
  name: Basecamp OAuth API
  slug: open-basecamp-oauth
- collection_type: open
  name: Basecamp Authorization People API
  slug: open-basecamp-people-api
- collection_type: open
  name: Basecamp Authorization Projects API
  slug: open-basecamp-projects-api
- collection_type: open
  name: Basecamp Authorization Recordings API
  slug: open-basecamp-recordings-api
- collection_type: open
  name: Basecamp Authorization Schedule Entries API
  slug: open-basecamp-schedule-entries-api
- collection_type: open
  name: Basecamp Authorization Schedules API
  slug: open-basecamp-schedules-api
- collection_type: open
  name: Basecamp Authorization Subscriptions API
  slug: open-basecamp-subscriptions-api
- collection_type: open
  name: Basecamp Authorization Templates API
  slug: open-basecamp-templates-api
- collection_type: open
  name: Basecamp Authorization To-Do Lists API
  slug: open-basecamp-to-do-lists-api
- collection_type: open
  name: Basecamp Authorization To-Dos API
  slug: open-basecamp-to-dos-api
- collection_type: open
  name: Basecamp Authorization Token API
  slug: open-basecamp-token-api
- collection_type: open
  name: Basecamp Authorization Uploads API
  slug: open-basecamp-uploads-api
- collection_type: open
  name: Basecamp Authorization Webhooks API
  slug: open-basecamp-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/basecamp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/basecamp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basecamp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/basecamp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/37signals
- group: company
  title: ''
  type: Website
  url: https://basecamp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/basecamp/bc3-api
- group: start
  title: ''
  type: Signup
  url: https://launchpad.37signals.com/
- group: company
  title: ''
  type: Blog
  url: https://basecamp.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basecamp.com/about/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basecamp.com/about/policies/privacy
- group: design
  title: ''
  type: SpectralRules
  url: rules/basecamp-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/basecamp-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/basecamp-context.jsonld
created: '2024-01-01'
description: Basecamp is a project management and team collaboration platform developed by 37signals. The Basecamp REST API (bc3-api) provides programmatic access to projects, to-do lists, messages, documents, schedules, and team members. OAuth2 authentication via the 37signals Launchpad is required. The API returns JSON and is documented on GitHub at github.com/basecamp/bc3-api.
examples:
- key_count: 5
  name: Bucketref Example
  slug: bucketref-example
- key_count: 0
  name: Campfire Example
  slug: campfire-example
- key_count: 11
  name: Campfireline Example
  slug: campfireline-example
- key_count: 1
  name: Campfirelinecreaterequest Example
  slug: campfirelinecreaterequest-example
- key_count: 7
  name: Cardcolumn Example
  slug: cardcolumn-example
- key_count: 3
  name: Cardmoverequest Example
  slug: cardmoverequest-example
- key_count: 0
  name: Cardtable Example
  slug: cardtable-example
- key_count: 0
  name: Comment Example
  slug: comment-example
- key_count: 1
  name: Commentcreaterequest Example
  slug: commentcreaterequest-example
- key_count: 7
  name: Dockitem Example
  slug: dockitem-example
- key_count: 0
  name: Document Example
  slug: document-example
- key_count: 3
  name: Documentcreaterequest Example
  slug: documentcreaterequest-example
- key_count: 1
  name: Error Example
  slug: error-example
- key_count: 0
  name: Message Example
  slug: message-example
- key_count: 5
  name: Messagecreaterequest Example
  slug: messagecreaterequest-example
- key_count: 3
  name: Messageupdaterequest Example
  slug: messageupdaterequest-example
- key_count: 0
  name: Person Example
  slug: person-example
- key_count: 17
  name: Personref Example
  slug: personref-example
- key_count: 1
  name: Positionrequest Example
  slug: positionrequest-example
- key_count: 6
  name: Profileupdaterequest Example
  slug: profileupdaterequest-example
- key_count: 14
  name: Project Example
  slug: project-example
- key_count: 3
  name: Projectaccessrequest Example
  slug: projectaccessrequest-example
- key_count: 4
  name: Projectconstruction Example
  slug: projectconstruction-example
- key_count: 1
  name: Projectconstructionrequest Example
  slug: projectconstructionrequest-example
- key_count: 2
  name: Projectcreaterequest Example
  slug: projectcreaterequest-example
- key_count: 4
  name: Projectupdaterequest Example
  slug: projectupdaterequest-example
- key_count: 12
  name: Recording Example
  slug: recording-example
- key_count: 7
  name: Recurrenceschedule Example
  slug: recurrenceschedule-example
- key_count: 0
  name: Schedule Example
  slug: schedule-example
- key_count: 0
  name: Scheduleentry Example
  slug: scheduleentry-example
- key_count: 7
  name: Scheduleentrycreaterequest Example
  slug: scheduleentrycreaterequest-example
- key_count: 1
  name: Scheduleupdaterequest Example
  slug: scheduleupdaterequest-example
- key_count: 4
  name: Subscription Example
  slug: subscription-example
- key_count: 2
  name: Subscriptionupdaterequest Example
  slug: subscriptionupdaterequest-example
- key_count: 9
  name: Template Example
  slug: template-example
- key_count: 2
  name: Templatecreaterequest Example
  slug: templatecreaterequest-example
- key_count: 0
  name: Todo Example
  slug: todo-example
- key_count: 7
  name: Todocreaterequest Example
  slug: todocreaterequest-example
- key_count: 0
  name: Todolist Example
  slug: todolist-example
- key_count: 2
  name: Todolistcreaterequest Example
  slug: todolistcreaterequest-example
- key_count: 0
  name: Upload Example
  slug: upload-example
- key_count: 3
  name: Uploadcreaterequest Example
  slug: uploadcreaterequest-example
- key_count: 2
  name: Uploadupdaterequest Example
  slug: uploadupdaterequest-example
- key_count: 8
  name: Webhook Example
  slug: webhook-example
- key_count: 3
  name: Webhookcreaterequest Example
  slug: webhookcreaterequest-example
- key_count: 3
  name: Webhookupdaterequest Example
  slug: webhookupdaterequest-example
features:
- description: Create and manage projects with team access controls.
  name: Project Management
- description: Hierarchical to-do lists with assignments, due dates, and completion tracking.
  name: To-Do Lists
- description: Threaded message boards for team discussion and announcements.
  name: Message Boards
- description: Real-time group chat within projects.
  name: Campfire Chat
- description: Project calendars with events and milestones.
  name: Schedules
- description: Document and file storage with version history.
  name: File Storage
- description: Real-time event notifications for project activity.
  name: Webhooks
- description: Full REST API with OAuth2 authentication for third-party integrations.
  name: OAuth2 API
finops:
- name: Basecamp Finops
  service_category: Collaboration / Project Management SaaS
  slug: basecamp-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Basecamp project management platform, derived from the Basecamp REST API (bc3-api). Basecamp does not currently offer a native GraphQL endpoint; this schema
  name: Basecamp GraphQL Schema
  slug: basecamp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basecamp.png
json_schemas:
- name: Basecamp Project
  property_count: 14
  slug: basecamp-project
- name: Basecamp Webhook Payload
  property_count: 6
  slug: basecamp-webhook-payload
- name: BucketRef
  property_count: 5
  slug: bucketref
- name: Campfire
  property_count: 0
  slug: campfire
- name: CampfireLine
  property_count: 11
  slug: campfireline
- name: CampfireLineCreateRequest
  property_count: 1
  slug: campfirelinecreaterequest
- name: CardColumn
  property_count: 7
  slug: cardcolumn
- name: CardMoveRequest
  property_count: 3
  slug: cardmoverequest
- name: CardTable
  property_count: 0
  slug: cardtable
- name: Comment
  property_count: 0
  slug: comment
- name: CommentCreateRequest
  property_count: 1
  slug: commentcreaterequest
- name: DockItem
  property_count: 7
  slug: dockitem
- name: Document
  property_count: 0
  slug: document
- name: DocumentCreateRequest
  property_count: 3
  slug: documentcreaterequest
- name: Error
  property_count: 1
  slug: error
- name: Message
  property_count: 0
  slug: message
- name: MessageCreateRequest
  property_count: 5
  slug: messagecreaterequest
- name: MessageUpdateRequest
  property_count: 3
  slug: messageupdaterequest
- name: Person
  property_count: 0
  slug: person
- name: PersonRef
  property_count: 17
  slug: personref
- name: PositionRequest
  property_count: 1
  slug: positionrequest
- name: ProfileUpdateRequest
  property_count: 6
  slug: profileupdaterequest
- name: Project
  property_count: 14
  slug: project
- name: ProjectAccessRequest
  property_count: 3
  slug: projectaccessrequest
- name: ProjectConstruction
  property_count: 4
  slug: projectconstruction
- name: ProjectConstructionRequest
  property_count: 1
  slug: projectconstructionrequest
- name: ProjectCreateRequest
  property_count: 2
  slug: projectcreaterequest
- name: ProjectUpdateRequest
  property_count: 4
  slug: projectupdaterequest
- name: Recording
  property_count: 12
  slug: recording
- name: RecurrenceSchedule
  property_count: 7
  slug: recurrenceschedule
- name: Schedule
  property_count: 0
  slug: schedule
- name: ScheduleEntry
  property_count: 0
  slug: scheduleentry
- name: ScheduleEntryCreateRequest
  property_count: 7
  slug: scheduleentrycreaterequest
- name: ScheduleUpdateRequest
  property_count: 1
  slug: scheduleupdaterequest
- name: Subscription
  property_count: 4
  slug: subscription
- name: SubscriptionUpdateRequest
  property_count: 2
  slug: subscriptionupdaterequest
- name: Template
  property_count: 9
  slug: template
- name: TemplateCreateRequest
  property_count: 2
  slug: templatecreaterequest
- name: Todo
  property_count: 0
  slug: todo
- name: TodoCreateRequest
  property_count: 7
  slug: todocreaterequest
- name: TodoList
  property_count: 0
  slug: todolist
- name: TodoListCreateRequest
  property_count: 2
  slug: todolistcreaterequest
- name: Upload
  property_count: 0
  slug: upload
- name: UploadCreateRequest
  property_count: 3
  slug: uploadcreaterequest
- name: UploadUpdateRequest
  property_count: 2
  slug: uploadupdaterequest
- name: Webhook
  property_count: 8
  slug: webhook
- name: WebhookCreateRequest
  property_count: 3
  slug: webhookcreaterequest
- name: WebhookUpdateRequest
  property_count: 3
  slug: webhookupdaterequest
json_structures:
- name: Bucketref Structure
  property_count: 0
  slug: bucketref-structure
- name: Campfire Structure
  property_count: 0
  slug: campfire-structure
- name: Campfireline Structure
  property_count: 0
  slug: campfireline-structure
- name: Campfirelinecreaterequest Structure
  property_count: 0
  slug: campfirelinecreaterequest-structure
- name: Cardcolumn Structure
  property_count: 0
  slug: cardcolumn-structure
- name: Cardmoverequest Structure
  property_count: 0
  slug: cardmoverequest-structure
- name: Cardtable Structure
  property_count: 0
  slug: cardtable-structure
- name: Comment Structure
  property_count: 0
  slug: comment-structure
- name: Commentcreaterequest Structure
  property_count: 0
  slug: commentcreaterequest-structure
- name: Dockitem Structure
  property_count: 0
  slug: dockitem-structure
- name: Document Structure
  property_count: 0
  slug: document-structure
- name: Documentcreaterequest Structure
  property_count: 0
  slug: documentcreaterequest-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: Message Structure
  property_count: 0
  slug: message-structure
- name: Messagecreaterequest Structure
  property_count: 0
  slug: messagecreaterequest-structure
- name: Messageupdaterequest Structure
  property_count: 0
  slug: messageupdaterequest-structure
- name: Person Structure
  property_count: 0
  slug: person-structure
- name: Personref Structure
  property_count: 0
  slug: personref-structure
- name: Positionrequest Structure
  property_count: 0
  slug: positionrequest-structure
- name: Profileupdaterequest Structure
  property_count: 0
  slug: profileupdaterequest-structure
- name: Project Structure
  property_count: 0
  slug: project-structure
- name: Projectaccessrequest Structure
  property_count: 0
  slug: projectaccessrequest-structure
- name: Projectconstruction Structure
  property_count: 0
  slug: projectconstruction-structure
- name: Projectconstructionrequest Structure
  property_count: 0
  slug: projectconstructionrequest-structure
- name: Projectcreaterequest Structure
  property_count: 0
  slug: projectcreaterequest-structure
- name: Projectupdaterequest Structure
  property_count: 0
  slug: projectupdaterequest-structure
- name: Recording Structure
  property_count: 0
  slug: recording-structure
- name: Recurrenceschedule Structure
  property_count: 0
  slug: recurrenceschedule-structure
- name: Schedule Structure
  property_count: 0
  slug: schedule-structure
- name: Scheduleentry Structure
  property_count: 0
  slug: scheduleentry-structure
- name: Scheduleentrycreaterequest Structure
  property_count: 0
  slug: scheduleentrycreaterequest-structure
- name: Scheduleupdaterequest Structure
  property_count: 0
  slug: scheduleupdaterequest-structure
- name: Subscription Structure
  property_count: 0
  slug: subscription-structure
- name: Subscriptionupdaterequest Structure
  property_count: 0
  slug: subscriptionupdaterequest-structure
- name: Template Structure
  property_count: 0
  slug: template-structure
- name: Templatecreaterequest Structure
  property_count: 0
  slug: templatecreaterequest-structure
- name: Todo Structure
  property_count: 0
  slug: todo-structure
- name: Todocreaterequest Structure
  property_count: 0
  slug: todocreaterequest-structure
- name: Todolist Structure
  property_count: 0
  slug: todolist-structure
- name: Todolistcreaterequest Structure
  property_count: 0
  slug: todolistcreaterequest-structure
- name: Upload Structure
  property_count: 0
  slug: upload-structure
- name: Uploadcreaterequest Structure
  property_count: 0
  slug: uploadcreaterequest-structure
- name: Uploadupdaterequest Structure
  property_count: 0
  slug: uploadupdaterequest-structure
- name: Webhook Structure
  property_count: 0
  slug: webhook-structure
- name: Webhookcreaterequest Structure
  property_count: 0
  slug: webhookcreaterequest-structure
- name: Webhookupdaterequest Structure
  property_count: 0
  slug: webhookupdaterequest-structure
jsonld:
- class_count: 0
  name: Basecamp Context
  property_count: 124
  slug: basecamp-context
layout: provider
modified: '2026-05-19'
name: Basecamp
nav: Providers
network: true
overview: 'Basecamp publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Authorization API, Campfires API, and 17 more. Tagged areas include Collaboration, Project Management, REST, Software-as-a-Service, and Team Communication.


  The Basecamp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Basecamp''s developer surface includes authentication, documentation, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Basecamp Plans Pricing
  plan_count: 4
  slug: basecamp-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Basecamp Rate Limits
  slug: basecamp-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Basecamp API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: basecamp-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Basecamp API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: basecamp-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Basecamp API Rules
  rule_count: 22
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 12
  slug: basecamp-spectral-rules
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 76.6
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basecamp/refs/heads/main/screenshots/basecamp-2026-06-20T173011.png
security:
- kind: authentication
  name: Basecamp Authentication
  slug: basecamp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Basecamp Domain Security
  slug: basecamp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Basecamp Vulnerability Disclosure
  slug: basecamp-vulnerability-disclosure
  summary_line: disclosure policy published
slug: basecamp
tags:
- Collaboration
- Project Management
- REST
- Software-as-a-Service
- Team Communication
use_cases:
- description: Track sprints, bugs, and feature development with to-do lists.
  name: Software Development
- description: Manage client deliverables, approvals, and communications.
  name: Client Projects
- description: Asynchronous team communication and project coordination.
  name: Remote Team Collaboration
- description: Automate project workflows and reporting via REST API.
  name: Project Automation
- description: Multi-client project organization for agencies and consultancies.
  name: Agency Project Management
website: https://basecamp.com/
---
