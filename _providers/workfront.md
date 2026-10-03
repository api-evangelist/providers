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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.8
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 34
  human_in_the_loop: 1
  name: Workfront Agentic Access
  operation_count: 59
  slug: workfront-agentic-access
  summary_line: 59 operations · 34 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The core Workfront REST API. Every object in the system has a URI of the form /attask/api/v22.0/{objCode}/{id}; GET retrieves or searches, POST inserts, PUT edits and DELETE removes. Adobe does not pu
  name: Adobe Workfront API
  slug: workfront-api
- description: The Workfront webhook/event surface. A system administrator registers a subscription for an object type (objCode) and event type (CREATE, UPDATE, DELETE) with a destination URL and auth token; Workfro
  name: Adobe Workfront Event Subscription API
  slug: workfront-event-subscription-api
- description: Adobe's hosted Model Context Protocol server for Workfront, generally available since June 2026. It exposes 87 documented tools across three families — Approvals (documents, approval workflows, remind
  name: Adobe Workfront MCP Server
  slug: workfront-mcp-server
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: 'Field management. Per-record-type quotas: max 500 fields total; max 20 PARAGRAPH (long-text) fields; max 20 FORMULA fields; max 30 REFERENCE fields. Field display names must be unique within a record '
  name: Adobe Workfront Fields API
  phrasing_intents:
  - id: getField
    intent: Get a field by ID
    question: How do I see a field's type and options, like the choices on a single-select?
  - id: updateField
    intent: Replace a field's definition in full
    question: What happens to field settings I omit when I fully replace a field?
  - id: deleteField
    intent: Delete a field
    question: How do I remove a field from a record type?
  - id: patchField
    intent: Change some settings on a field
    question: Can I rename a field without resending its options?
  - id: getFieldsByRecordType
    intent: List the fields on a record type
    question: What fields does a record type have?
  - id: createField
    intent: Add a field to a record type
    question: How do I add a new column, like a due date, to a record type?
  phrasing_ops: 6
  slug: workfront-fields-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Resource permissions, member management, and access requests.
  name: Adobe Workfront Permissions API
  phrasing_intents:
  - id: getAccessRequests
    intent: List pending access requests on a resource
    question: Who is waiting for me to approve access to my workspace?
  - id: createAccessRequest
    intent: Request access to a resource
    question: How do I ask for access to a workspace I can't open?
  - id: deleteAccessRequests
    intent: Dismiss access requests on a resource
    question: How do I dismiss access requests I don't want to approve?
  - id: getMembers
    intent: List who a resource is shared with and their roles
    question: Which users, groups and teams have been given access to this record type?
  - id: updateMembers
    intent: Grant, change or revoke members' access
    question: Can I add new people, change roles and remove others from a workspace in one request?
  - id: getMyPermissions
    intent: Check my effective permissions on a resource
    question: Am I allowed to edit or delete this record?
  - id: getInheritance
    intent: See if a record type inherits workspace access
    question: Do workspace members automatically get their workspace access on this record type?
  phrasing_ops: 7
  slug: workfront-permissions-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Record Type Controller
  name: Adobe Workfront Record Types API
  phrasing_intents:
  - id: getRecordTypes
    intent: List a workspace's record types (legacy v1)
    question: Can the older v1 API list all record types in a workspace in one response?
  - id: getRecordType
    intent: Fetch a record type with the legacy v1 endpoint
    question: Is there still a v1 endpoint to look up one record type by ID?
  - id: getV2RecordTypesById
    intent: Get a record type by ID
    question: How do I see a record type's settings, primary field and permissions?
  - id: updateRecordType
    intent: Replace a record type's settings in full
    question: What happens to settings I leave out when I fully replace a record type?
  - id: deleteRecordType
    intent: Permanently delete a record type and its records
    question: Does deleting a record type also wipe out its fields and records?
  - id: patchRecordType
    intent: Change some settings on a record type
    question: Can I just change a record type's icon without resending its other settings?
  - id: getRecordTypesByWorkspace
    intent: Page through a workspace's record types
    question: What record types exist in my workspace, page by page?
  - id: createRecordType
    intent: Create a record type in a workspace
    question: How do I add a new record type, like Campaigns, to a workspace?
  phrasing_ops: 10
  slug: workfront-record-types-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Record Controller
  name: Adobe Workfront Records API
  phrasing_intents:
  - id: getRecord
    intent: Fetch a record with the legacy v1 endpoint
    question: Can I still pull a single record through the older v1 records endpoint?
  - id: updateRecord
    intent: Update a record with the legacy v1 endpoint
    question: How would I change a record's field data using the original v1 records API?
  - id: deleteRecord
    intent: Delete a record with the legacy v1 endpoint
    question: Does the older v1 records API let me delete a single record by its ID?
  - id: createRecord
    intent: Create a record with the legacy v1 endpoint
    question: How did the v1 API create a record when the record type goes in the body rather than the path?
  - id: searchRecordsGet
    intent: Search records by field values via v1 query string
    question: Can I search records by field value with a plain GET on the older v1 search endpoint?
  - id: searchRecordsPost
    intent: Search records by field values via v1 POST body
    question: Can the v1 record search take its filters and sorting in a POST body instead of the URL?
  - id: getV2RecordsById
    intent: Get a record by ID
    question: How can I look up one Workfront Planning record and see its field data?
  - id: putV2RecordsById
    intent: Replace a record's contents in full
    question: What happens to fields I leave out when I fully replace a record?
  phrasing_ops: 22
  slug: workfront-records-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: 'View management. Limits: max 100 personal views per record type; max 255 characters for view name.'
  name: Adobe Workfront Views API
  phrasing_intents:
  - id: getView
    intent: Get a view by ID
    question: How do I see the filters, grouping and sorting saved on a view?
  - id: updateView
    intent: Replace a view's configuration in full
    question: What happens to view settings I leave out on a full replacement?
  - id: deleteView
    intent: Delete a view
    question: How do I get rid of a saved view?
  - id: patchView
    intent: Change some settings on a view
    question: Can I hide a view from the list without changing its filters?
  - id: getViewsByRecordType
    intent: List the views on a record type
    question: What saved views exist for a record type?
  - id: createView
    intent: Create a view for a record type
    question: How do I add a timeline or calendar view to a record type?
  phrasing_ops: 6
  slug: workfront-views-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Workspace Controller
  name: Adobe Workfront Workspaces API
  phrasing_intents:
  - id: getWorkspaces
    intent: List all workspaces (legacy v1)
    question: Can the older v1 API list every workspace without cursor paging?
  - id: getWorkspace
    intent: Fetch a workspace with the legacy v1 endpoint
    question: Is there a v1 endpoint that still returns one workspace by ID?
  - id: getV2WorkspacesById
    intent: Get a workspace by ID
    question: How do I look up a workspace's name, owner and record type sections?
  - id: updateWorkspace
    intent: Replace a workspace's settings in full
    question: What happens to workspace settings I leave out on a full replacement?
  - id: deleteWorkspace
    intent: Delete a workspace
    question: How do I delete a workspace I no longer need?
  - id: patchWorkspace
    intent: Change some settings on a workspace
    question: Can I rename a workspace without touching its other settings?
  - id: getV2Workspaces
    intent: Page through all workspaces
    question: What workspaces do I have in Workfront Planning?
  - id: createWorkspace
    intent: Create a workspace
    question: How do I set up a new workspace for a team?
  phrasing_ops: 8
  slug: workfront-workspaces-api
artifact_total: 21
asyncapis:
- description: ''
  name: Workfront Event Subscriptions Webhooks
  slug: workfront-event-subscriptions-webhooks
collections:
- collection_type: open
  name: Workfront Planning API Version 1
  slug: open-workfront-planning-v1
- collection_type: open
  name: Workfront Planning API Version 2
  slug: open-workfront-planning-v2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/overlays/workfront-planning-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workfront-planning-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/overlays/workfront-planning-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workfront-planning-v1-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/agentic-access/workfront-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workfront-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://business.adobe.com/products/workfront/main.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/wf-planning
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/workfront-api
- group: docs
  title: ''
  type: APIReference
  url: https://developersupport.workfront.com/page-api-explorer.html
- group: start
  title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-general-information/api-basics
- group: operate
  title: ''
  type: Support
  url: https://experienceleaguecommunities.adobe.com/t5/workfront/ct-p/workfront-community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workfront
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/workfront/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-notes/api-version-support-schedule
- group: operate
  title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/en/docs/workfront/using/product-announcements/product-releases/product-releases
- group: auth
  title: ''
  type: Security
  url: https://helpx.adobe.com/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.adobe.com/trust/compliance/compliance-list.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.adobe.com/trust.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/packages/workfront-packages.yml
  title: ''
  type: SDKs
  url: packages/workfront-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/packages/workfront-packages.yml
  title: ''
  type: Packages
  url: packages/workfront-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/cli/workfront-cli.yml
  title: ''
  type: CLI
  url: cli/workfront-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/components/workfront-components.yml
  title: ''
  type: Components
  url: components/workfront-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/sandbox/workfront-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/workfront-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/authentication/workfront-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workfront-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/scopes/workfront-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/workfront-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/conventions/workfront-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workfront-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/errors/workfront-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workfront-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/lifecycle/workfront-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workfront-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/rate-limits/workfront-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/workfront-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/plans/workfront-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workfront-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/changelog/workfront-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/workfront-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/conformance/workfront-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workfront-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/security/workfront-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workfront-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/security/workfront-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/workfront-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/well-known/workfront-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workfront-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/well-known/workfront-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/workfront-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/llms/workfront-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workfront-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/asyncapi/workfront-event-subscriptions-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/workfront-event-subscriptions-webhooks.yml
created: '2026-08-12'
description: 'Adobe Workfront is Adobe''s enterprise work-management platform for marketing and creative operations — project and portfolio planning, request intake, task and resource management, proofing and approvals, timesheets, financial tracking and reporting — sold in Select, Prime and Ultimate packages. Its developer surface is unusually wide for a work-management vendor: a versioned REST core API at /attask/api (v22.0, 174 objects exposed through an anonymous object-metadata endpoint), the separately versioned Workfront Planning API published as first-party OpenAPI 3.0.1 and 3.1.0 documents on developer.adobe.com, an Event Subscription API that pushes object change events to customer webhook endpoints, a Document Webhooks API third-party document providers implement, and — since June 2026 — a hosted Model Context Protocol server at mcp.workfront.adobe.com exposing 87 documented tools behind OAuth 2.1, plus first-party agent Skills published in the adobe/skills repository.'
image: https://avatars.githubusercontent.com/u/3494194?v=4
layout: provider
mcp_servers:
- description: ''
  name: Adobe Workfront MCP server
  slug: adobe-workfront-mcp-server
modified: '2026-08-12'
name: Adobe Workfront
nav: Providers
network: true
overview: 'Adobe Workfront publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Permissions API, Record Types API, and 6 more. Tagged areas include Company, Work Management, Project Management, Marketing Operations, and Creative Operations.


  The Adobe Workfront catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adobe Workfront''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, CLI, and 33 more developer resources.'
plans:
- name: Workfront Plans Pricing
  plan_count: 3
  slug: workfront-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 9
  name: Workfront Rate Limits
  slug: workfront-rate-limits
scopes:
- name: Workfront Scopes
  scope_count: 18
  slug: workfront-scopes
  summary_line: 18 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 56.4
    developer_ergonomics: 83.3
    discoverability: 75.0
    operational_transparency: 78.9
  previous_composite: 70.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/screenshots/workfront-2026-08-17T075411.png
security:
- kind: authentication
  name: Workfront Authentication
  slug: workfront-authentication
  summary_line: http/apiKey/oauth2 · 8 schemes
- kind: domain-security
  name: Workfront Domain Security
  slug: workfront-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workfront Vulnerability Disclosure
  slug: workfront-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Workfront Trust Center
  slug: workfront-trust-center
  summary_line: SOC 2 Type 2 (Security, Availability & Confidentiality), SOC 3 (Security, Availability & Confidentiality), ISO 9001:2015, ISO 27001:2022, ISO 27017:2015, ISO 27018:2019, ISO 22301:2019, HIPAA ready, IRAP Assessed (Australia), GLBA ready, FERPA ready
slug: workfront
tags:
- Company
- Work Management
- Project Management
- Marketing Operations
- Creative Operations
- Collaboration
- Approvals
- Resource Management
- Workflow Automation
- Enterprise Software
- Adobe
- MCP
website: https://business.adobe.com/products/workfront/main.html
---
