---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 67.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Lightfield Agentic Access
  operation_count: 55
  slug: lightfield-agentic-access
  summary_line: 55 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Accounts API from Lightfield — 3 operation(s) for accounts.
  name: Lightfield Accounts API
  phrasing_intents:
  - id: account.definitions
    intent: Get the field schema for accounts
    question: What fields and custom fields can an account record have in Lightfield?
  - id: account.create
    intent: Create a company account
    question: How do I add a new company account, and does it get enriched if I give a website?
  - id: account.list
    intent: List accounts
    question: How do I page through all the companies stored as accounts?
  - id: account.update
    intent: Update an existing account
    question: How do I change fields on a company account I already created?
  - id: account.retrieve
    intent: Retrieve one account by ID
    question: How do I look up a single account when I already have its ID?
  phrasing_ops: 5
  slug: lightfield-accounts-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Auth API from Lightfield — 1 operation(s) for auth.
  name: Lightfield Auth API
  phrasing_intents:
  - id: auth.validate
    intent: Check the current API key and its scopes
    question: Is my Lightfield API key still active?
  phrasing_ops: 1
  slug: lightfield-auth-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Contacts API from Lightfield — 3 operation(s) for contacts.
  name: Lightfield Contacts API
  phrasing_intents:
  - id: contact.definitions
    intent: Get the field schema for contacts
    question: What fields and custom fields are available on a contact record in Lightfield?
  - id: contact.create
    intent: Create a contact
    question: How do I add a new person as a contact, and will it be enriched automatically?
  - id: contact.list
    intent: List contacts
    question: How can I page through every person stored as a contact?
  - id: contact.update
    intent: Update an existing contact
    question: How do I edit a person's details on a contact I already have?
  - id: contact.retrieve
    intent: Retrieve one contact by ID
    question: How do I fetch a single contact when I have their ID?
  phrasing_ops: 5
  slug: lightfield-contacts-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Emails API from Lightfield — 4 operation(s) for emails.
  name: Lightfield Emails API
  phrasing_intents:
  - id: email.retrieve
    intent: Read one email including its body
    question: How do I read the full body of a specific email?
  - id: email.list
    intent: List emails
    question: How can I page through the emails synced into my workspace?
  - id: email.send
    intent: Send a new email
    question: Can I send an email from my connected mailbox through Lightfield?
  - id: email.draft
    intent: Save an email as a draft
    question: Can I prepare an email as a draft without sending it?
  phrasing_ops: 4
  slug: lightfield-emails-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Files API from Lightfield — 5 operation(s) for files.
  name: Lightfield Files API
  phrasing_intents:
  - id: file.create
    intent: Start a file upload and get an upload URL
    question: How do I upload a file, such as a meeting transcript, to Lightfield?
  - id: file.list
    intent: List workspace files
    question: How do I see all the files uploaded to my workspace?
  - id: file.complete
    intent: Finalize a file upload
    question: What do I call after the file bytes have finished uploading?
  - id: file.retrieve
    intent: Get a file's details and status
    question: How do I check the status of one uploaded file?
  - id: file.url
    intent: Get a temporary download link for a file
    question: How do I download a file I uploaded?
  - id: file.cancel
    intent: Cancel a pending file upload
    question: How do I abort an upload that hasn't been completed yet?
  phrasing_ops: 6
  slug: lightfield-files-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Lists API from Lightfield — 5 operation(s) for lists.
  name: Lightfield Lists API
  phrasing_intents:
  - id: list.create
    intent: Create a list of records
    question: How do I create a new list for grouping accounts, contacts or opportunities?
  - id: list.list
    intent: List saved lists
    question: Which saved lists exist in my workspace?
  - id: list.update
    intent: Rename or edit a list
    question: How do I rename a list I already made?
  - id: list.retrieve
    intent: Retrieve one list by ID
    question: How do I look up a single list's name and type?
  - id: list.listAccounts
    intent: List the accounts in a list
    question: Which companies are in a particular list?
  - id: list.listContacts
    intent: List the contacts in a list
    question: Which people are members of a particular list?
  - id: list.listOpportunities
    intent: List the opportunities in a list
    question: Which deals are included in a particular list?
  phrasing_ops: 7
  slug: lightfield-lists-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Meetings API from Lightfield — 2 operation(s) for meetings.
  name: Lightfield Meetings API
  phrasing_intents:
  - id: meeting.create
    intent: Log a past meeting
    question: Can I record a meeting that already happened, with its transcript?
  - id: meeting.list
    intent: List meetings
    question: How do I page through all the meetings recorded in my workspace?
  - id: meeting.update
    intent: Set a meeting's privacy or transcript
    question: How do I attach or replace the transcript on a meeting already logged?
  - id: meeting.retrieve
    intent: Retrieve one meeting by ID
    question: How do I fetch a single meeting and its transcript?
  phrasing_ops: 4
  slug: lightfield-meetings-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Members API from Lightfield — 2 operation(s) for members.
  name: Lightfield Members API
  phrasing_intents:
  - id: member.retrieve
    intent: Retrieve one workspace member
    question: How do I look up a teammate by their member ID?
  - id: member.list
    intent: List workspace members
    question: Who are all the members of my Lightfield workspace?
  phrasing_ops: 2
  slug: lightfield-members-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Notes API from Lightfield — 2 operation(s) for notes.
  name: Lightfield Notes API
  phrasing_intents:
  - id: note.create
    intent: Write a new note
    question: How do I add a note to an account or opportunity?
  - id: note.list
    intent: List notes
    question: How do I page through all the notes in my workspace?
  - id: note.update
    intent: Edit a note or relink it
    question: How do I edit the text of a note I already wrote?
  - id: note.retrieve
    intent: Retrieve one note by ID
    question: How do I read a single note when I have its ID?
  phrasing_ops: 4
  slug: lightfield-notes-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Objects API from Lightfield — 5 operation(s) for objects.
  name: Lightfield Objects API
  phrasing_intents:
  - id: object.create
    intent: Create a custom object record
    question: How do I add a record to one of my custom object types?
  - id: object.retrieve
    intent: Retrieve one custom object record
    question: How do I fetch a single custom object record by its ID?
  - id: object.update
    intent: Update a custom object record
    question: How do I change fields on an existing custom object record?
  - id: object.list
    intent: List records of a custom object type
    question: How do I list all records for one custom object type?
  - id: object.definitions
    intent: Get the field schema of a custom object
    question: What fields and relationships does a particular custom object type have?
  - id: object.listDefinitions
    intent: List the custom object types
    question: Which custom object types exist in my Lightfield workspace?
  phrasing_ops: 6
  slug: lightfield-objects-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Opportunities API from Lightfield — 3 operation(s) for opportunities.
  name: Lightfield Opportunities API
  phrasing_intents:
  - id: opportunity.definitions
    intent: Get the field schema for opportunities
    question: What fields and custom fields exist on opportunities in Lightfield?
  - id: opportunity.create
    intent: Create a sales opportunity
    question: How do I open a new deal for a company account?
  - id: opportunity.list
    intent: List opportunities
    question: How do I page through every deal in my pipeline?
  - id: opportunity.update
    intent: Update an existing opportunity
    question: How do I move an existing deal to a new stage?
  - id: opportunity.retrieve
    intent: Retrieve one opportunity by ID
    question: How do I look up one deal when I have its ID?
  phrasing_ops: 5
  slug: lightfield-opportunities-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Tasks API from Lightfield — 3 operation(s) for tasks.
  name: Lightfield Tasks API
  phrasing_intents:
  - id: task.definitions
    intent: Get the field schema for tasks
    question: What fields and relationships can a task have in Lightfield?
  - id: task.create
    intent: Create and assign a task
    question: How do I create a to-do and assign it to a teammate?
  - id: task.list
    intent: List tasks
    question: How do I page through all the tasks in my workspace?
  - id: task.update
    intent: Update an existing task
    question: How do I mark an existing task done or change its status?
  - id: task.retrieve
    intent: Retrieve one task by ID
    question: How do I look up a single task when I have its ID?
  phrasing_ops: 5
  slug: lightfield-tasks-api
- baseURL: https://api.lightfield.app/v1
  baseurl_source: declared
  description: The Workflow Run API from Lightfield — 1 operation(s) for workflow run.
  name: Lightfield Workflow Run API
  phrasing_intents:
  - id: workflowRun.status
    intent: Check a workflow run's status
    question: How do I find out whether a workflow run has finished?
  phrasing_ops: 1
  slug: lightfield-workflow-run-api
artifact_total: 56
asyncapis:
- description: ''
  name: Lightfield Events
  slug: lightfield-events
collections:
- collection_type: postman
  name: API Reference Accounts API
  slug: postman-lightfield-accounts-api
- collection_type: postman
  name: API Reference Accounts Auth API
  slug: postman-lightfield-auth-api
- collection_type: postman
  name: API Reference Accounts Contacts API
  slug: postman-lightfield-contacts-api
- collection_type: postman
  name: API Reference Accounts Emails API
  slug: postman-lightfield-emails-api
- collection_type: postman
  name: API Reference Accounts Files API
  slug: postman-lightfield-files-api
- collection_type: postman
  name: API Reference Accounts Lists API
  slug: postman-lightfield-lists-api
- collection_type: postman
  name: API Reference Accounts Meetings API
  slug: postman-lightfield-meetings-api
- collection_type: postman
  name: API Reference Accounts Members API
  slug: postman-lightfield-members-api
- collection_type: postman
  name: API Reference Accounts Notes API
  slug: postman-lightfield-notes-api
- collection_type: postman
  name: API Reference Accounts Objects API
  slug: postman-lightfield-objects-api
- collection_type: postman
  name: API Reference Accounts Opportunities API
  slug: postman-lightfield-opportunities-api
- collection_type: postman
  name: API Reference Accounts Tasks API
  slug: postman-lightfield-tasks-api
- collection_type: postman
  name: API Reference Accounts WorkflowRun API
  slug: postman-lightfield-workflowrun-api
- collection_type: open
  name: API Reference Accounts API
  slug: open-lightfield-accounts-api
- collection_type: open
  name: API Reference Accounts Auth API
  slug: open-lightfield-auth-api
- collection_type: open
  name: API Reference Accounts Contacts API
  slug: open-lightfield-contacts-api
- collection_type: open
  name: API Reference Accounts Emails API
  slug: open-lightfield-emails-api
- collection_type: open
  name: API Reference Accounts Files API
  slug: open-lightfield-files-api
- collection_type: open
  name: API Reference Accounts Lists API
  slug: open-lightfield-lists-api
- collection_type: open
  name: API Reference Accounts Meetings API
  slug: open-lightfield-meetings-api
- collection_type: open
  name: API Reference Accounts Members API
  slug: open-lightfield-members-api
- collection_type: open
  name: API Reference Accounts Notes API
  slug: open-lightfield-notes-api
- collection_type: open
  name: API Reference Accounts Objects API
  slug: open-lightfield-objects-api
- collection_type: open
  name: API Reference Accounts Opportunities API
  slug: open-lightfield-opportunities-api
- collection_type: open
  name: API Reference Accounts Tasks API
  slug: open-lightfield-tasks-api
- collection_type: open
  name: API Reference Accounts WorkflowRun API
  slug: open-lightfield-workflowrun-api
common:
- group: other
  href: https://artifacts.apis.io/lightfield/capabilities/lightfield-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lightfield-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lightfield/overlays/lightfield-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lightfield-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lightfield/overview
- group: company
  title: ''
  type: Website
  url: https://lightfield.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lightfield.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lightfield.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lightfield.app/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lightfield.app/getting-started/http-quickstart/
- group: operate
  title: ''
  type: Support
  url: https://support.lightfield.app
- group: company
  title: ''
  type: Blog
  url: https://lightfield.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightfld
- group: commercial
  title: ''
  type: Pricing
  url: https://lightfield.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://crm.lightfield.app/signup
- group: start
  title: ''
  type: Login
  url: https://crm.lightfield.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lightfield.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightfield.app/privacy
- group: build
  href: https://artifacts.apis.io/lightfield/packages/lightfield-packages.yml
  title: ''
  type: Packages
  url: packages/lightfield-packages.yml
- group: build
  href: https://artifacts.apis.io/lightfield/packages/lightfield-packages.yml
  title: ''
  type: SDKs
  url: packages/lightfield-packages.yml
- group: build
  href: https://artifacts.apis.io/lightfield/cli/lightfield-cli.yml
  title: ''
  type: CLI
  url: cli/lightfield-cli.yml
- group: agent
  href: https://artifacts.apis.io/lightfield/mcp/lightfield-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lightfield-mcp.yml
- group: build
  href: https://artifacts.apis.io/lightfield/mcp/lightfield-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lightfield-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lightfield/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lightfield/llms/lightfield-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lightfield-llms.txt
- group: agent
  href: https://artifacts.apis.io/lightfield/well-known/lightfield-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lightfield-well-known.yml
- group: auth
  href: https://artifacts.apis.io/lightfield/authentication/lightfield-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lightfield-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lightfield/scopes/lightfield-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lightfield-scopes.yml
- group: design
  href: https://artifacts.apis.io/lightfield/conventions/lightfield-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lightfield-conventions.yml
- group: design
  href: https://artifacts.apis.io/lightfield/conventions/lightfield-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lightfield-conventions.yml
- group: operate
  href: https://artifacts.apis.io/lightfield/rate-limits/lightfield-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lightfield-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lightfield/plans/lightfield-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lightfield-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lightfield/errors/lightfield-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lightfield-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lightfield/errors/lightfield-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/lightfield-error-codes.yml
- group: design
  href: https://artifacts.apis.io/lightfield/data-model/lightfield-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lightfield-data-model.yml
- group: design
  href: https://artifacts.apis.io/lightfield/lifecycle/lightfield-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lightfield-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightfield.app/
- group: operate
  href: https://artifacts.apis.io/lightfield/changelog/lightfield-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lightfield-changelog.yml
- group: design
  href: https://artifacts.apis.io/lightfield/asyncapi/lightfield-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/lightfield-events.yml
- group: design
  href: https://artifacts.apis.io/lightfield/conformance/lightfield-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lightfield-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.lightfield.app/security/
- group: auth
  href: https://artifacts.apis.io/lightfield/security/lightfield-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lightfield-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lightfield/security/lightfield-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lightfield-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.lightfield.app/security/
- group: auth
  href: https://artifacts.apis.io/lightfield/security/lightfield-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lightfield-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/lightfield/agentic-access/lightfield-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lightfield-agentic-access.yml
created: '2026-07-17'
description: Lightfield is an agent-native customer relationship management (CRM) platform for high-growth and AI-native go-to-market teams. Rather than depending on manual data entry, Lightfield captures customer interactions — calls, emails, meetings and external signals — as unstructured data, organizes them into a versioned context graph of CRM objects, and lets AI agents reason over that graph to generate pipeline, prepare for meetings, enrich records and drive follow-up. The public Lightfield API (beta) provides read/write access to every CRM entity — accounts, contacts, opportunities, meetings, notes, tasks, lists, emails, files, members, custom objects and workflow runs — across 55 operations, with first-party TypeScript, Python and Go SDKs, a Go CLI, and a hosted Model Context Protocol server at mcp.lightfield.app secured with OAuth 2.1. Workflows and Automations add trigger-driven agent pipelines fed by inbound webhooks, object lifecycle events and schedules. Backed by Greylock
  and Lightspeed Venture Partners.
finops:
- has_sources: true
  method: derived
  name: Lightfield Finops
  primary_unit: workspace, billed annually
  service_category: ''
  slug: lightfield-finops
  template: false
image: https://cdn.sanity.io/images/3ccg9tet/production/ab2fd80ee036fa9627f507d73c4236b5e40a0715-2400x1260.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lightfield.app over HTTP; 5 tools listed.
  name: Lightfield MCP Server
  slug: lightfield
modified: '2026-08-13'
name: Lightfield
nav: Providers
network: true
overview: 'Lightfield publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Contacts API, and 10 more. Tagged areas include Company, Application, CRM, Sales, and Artificial Intelligence.


  The Lightfield catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lightfield''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Lightfield Plans Pricing
  plan_count: 5
  slug: lightfield-plans-pricing
- name: Lightfield Price Estimates
  plan_count: 0
  slug: lightfield-price-estimates
random_paper: 20
rate_limits:
- limit_count: 3
  name: Lightfield Rate Limits
  slug: lightfield-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Lightfield API Rules
  rule_count: 49
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 4
  slug: lightfield-rules
scopes:
- name: Lightfield Scopes
  scope_count: 26
  slug: lightfield-scopes
  summary_line: 26 scopes
score:
  band: exemplar
  composite: 72.7
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 55.4
    developer_ergonomics: 74.4
    discoverability: 75.0
    operational_transparency: 84.2
  previous_composite: 72.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lightfield/lightfield-2026-07-25T225114.png
security:
- kind: authentication
  name: Lightfield Authentication
  slug: lightfield-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lightfield Domain Security
  slug: lightfield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lightfield Vulnerability Disclosure
  slug: lightfield-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Lightfield Trust Center
  slug: lightfield-trust-center
  summary_line: SOC 2 Type 2, HIPAA, GDPR, ISO 27001
skill_count: 4
skills:
- name: Advance a Lightfield opportunity through its pipeline
  slug: lightfield-advance-opportunity
- name: Create a Lightfield account and linked contact
  slug: lightfield-create-account-and-contact
- name: Summarize a Lightfield meeting and log the follow-up
  slug: lightfield-meeting-followup
- name: Draft and send a Lightfield email through a connected mailbox
  slug: lightfield-send-outbound-email
slug: lightfield
tags:
- Company
- Application
- CRM
- Sales
- Artificial Intelligence
- Agents
- Go-To-Market
- Productivity
- Software-as-a-Service
website: https://lightfield.app/
---
