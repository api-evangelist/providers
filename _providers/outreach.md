---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.outreach.ai/pricing
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 160
  human_in_the_loop: 0
  name: Outreach Agentic Access
  operation_count: 253
  slug: outreach-agentic-access
  summary_line: 253 operations · 160 acting
api_count: 2
apis:
- description: Remote Model Context Protocol server exposing Outreach as 41 agent tools (27 read, 11 write, 3 schema introspection) over streamable HTTP, authorized by OAuth 2.1 with PKCE and RFC 7591 Dynamic Client
  name: Outreach MCP Server
  slug: outreach-mcp-server
- description: Client extensibility surface for embedding a web application inside the Outreach client — shell, tab and tile web-widget extensions, a text-editor extension, activity-feed custom events and a mailing-
  name: Outreach Client Extensions API
  slug: outreach-client-extensions-api
- description: Read-only access to an organization's Outreach data through Snowflake secure data sharing and Delta Sharing, in a ready-to-query format with no data copy or custom pipeline. Roughly 60 documented tabl
  name: Outreach Data Sharing
  slug: outreach-data-sharing
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: Event-driven webhook deliveries for accounts, calls, contacts, email addresses, imports, Kaia recordings, mailings, opportunities, opportunity prospect roles, prospects, sequences, sequence states, ta
  name: Outreach Webhooks
  slug: outreach-webhooks
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/account" /> ## Account Relationships <SchemaDefinition schemaRef="#/components/schemas/accountRelationships" /> ## Account Resource Metadata | **METAD'
  name: Outreach Account API
  slug: outreach-account-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/accountNote" /> ## Account Note Relationships <SchemaDefinition schemaRef="#/components/schemas/accountNoteRelationships" /> ## ⌵ Account Note Actions'
  name: Outreach Account Note API
  slug: outreach-account-note-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/auditLog" /> ## Audit Log Custom Filters | **NAME**| **VALUE TYPE** | **VALUE KIND** | **VALUE LENGTH** | | --- | --- | --- | --- | | agentEmail | str'
  name: Outreach Audit Log API
  slug: outreach-audit-log-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/batch" /> ## Batch Relationships <SchemaDefinition schemaRef="#/components/schemas/batchRelationships" /> ## Batch Resource Metadata | **METADATA NAME'
  name: Outreach Batch API
  slug: outreach-batch-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/batchItem" /> ## Batch Item Relationships <SchemaDefinition schemaRef="#/components/schemas/batchItemRelationships" /> ## ⌵ Batch Item Actions'
  name: Outreach Batch Item API
  slug: outreach-batch-item-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/call" /> ## Call Relationships <SchemaDefinition schemaRef="#/components/schemas/callRelationships" /> ## Call Resource Metadata | **METADATA NAME**| '
  name: Outreach Call API
  slug: outreach-call-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/callDisposition" /> ## Call Disposition Relationships <SchemaDefinition schemaRef="#/components/schemas/callDispositionRelationships" /> ## Call Dispo'
  name: Outreach Call Disposition API
  slug: outreach-call-disposition-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/callPurpose" /> ## Call Purpose Relationships <SchemaDefinition schemaRef="#/components/schemas/callPurposeRelationships" /> ## Call Purpose Resource '
  name: Outreach Call Purpose API
  slug: outreach-call-purpose-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/complianceRequest" /> ## Compliance Request Relationships <SchemaDefinition schemaRef="#/components/schemas/complianceRequestRelationships" /> ## ⌵ Co'
  name: Outreach Compliance Request API
  slug: outreach-compliance-request-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/contentCategory" /> ## Content Category Relationships <SchemaDefinition schemaRef="#/components/schemas/contentCategoryRelationships" /> ## Content Ca'
  name: Outreach Content Category API
  slug: outreach-content-category-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/contentCategoryMembership" /> ## Content Category Membership Relationships <SchemaDefinition schemaRef="#/components/schemas/contentCategoryMembership'
  name: Outreach Content Category Membership API
  slug: outreach-content-category-membership-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/contentCategoryOwnership" /> ## Content Category Ownership Relationships <SchemaDefinition schemaRef="#/components/schemas/contentCategoryOwnershipRel'
  name: Outreach Content Category Ownership API
  slug: outreach-content-category-ownership-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/customDuty" /> ## ⌵ Custom Duty Actions'
  name: Outreach Custom Duty API
  slug: outreach-custom-duty-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/duty" /> ## ⌵ Duty Actions'
  name: Outreach Duty API
  slug: outreach-duty-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/emailAddress" /> ## Email Address Relationships <SchemaDefinition schemaRef="#/components/schemas/emailAddressRelationships" /> ## Email Address Resou'
  name: Outreach Email Address API
  slug: outreach-email-address-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/event" /> ## Event Relationships <SchemaDefinition schemaRef="#/components/schemas/eventRelationships" /> ## Event Resource Metadata | **METADATA NAME'
  name: Outreach Event API
  slug: outreach-event-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/favorite" /> ## Favorite Relationships <SchemaDefinition schemaRef="#/components/schemas/favoriteRelationships" /> ## Favorite Resource Metadata | **M'
  name: Outreach Favorite API
  slug: outreach-favorite-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/import" /> ## Import Relationships <SchemaDefinition schemaRef="#/components/schemas/importRelationships" /> ## Import Resource Metadata | **METADATA '
  name: Outreach Import API
  slug: outreach-import-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/kaiaRecording" /> ## Kaia Recording Relationships <SchemaDefinition schemaRef="#/components/schemas/kaiaRecordingRelationships" /> ## ⌵ Kaia Recording'
  name: Outreach Kaia Recording API
  slug: outreach-kaia-recording-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/kaiaVoiceImport" /> ## ⌵ Kaia Voice Import Actions'
  name: Outreach Kaia Voice Import API
  slug: outreach-kaia-voice-import-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/mailAlias" /> ## Mail Alias Relationships <SchemaDefinition schemaRef="#/components/schemas/mailAliasRelationships" /> ## ⌵ Mail Alias Actions'
  name: Outreach Mail Alias API
  slug: outreach-mail-alias-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/mailbox" /> ## Mailbox Relationships <SchemaDefinition schemaRef="#/components/schemas/mailboxRelationships" /> ## Mailbox Resource Metadata | **METAD'
  name: Outreach Mailbox API
  slug: outreach-mailbox-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/mailing" /> ## Mailing Relationships <SchemaDefinition schemaRef="#/components/schemas/mailingRelationships" /> ## Mailing Resource Metadata | **METAD'
  name: Outreach Mailing API
  slug: outreach-mailing-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/opportunity" /> ## Opportunity Relationships <SchemaDefinition schemaRef="#/components/schemas/opportunityRelationships" /> ## Opportunity Resource Me'
  name: Outreach Opportunity API
  slug: outreach-opportunity-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/opportunityProspectRole" /> ## Opportunity Prospect Role Relationships <SchemaDefinition schemaRef="#/components/schemas/opportunityProspectRoleRelati'
  name: Outreach Opportunity Prospect Role API
  slug: outreach-opportunity-prospect-role-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/opportunityStage" /> ## Opportunity Stage Relationships <SchemaDefinition schemaRef="#/components/schemas/opportunityStageRelationships" /> ## Opportu'
  name: Outreach Opportunity Stage API
  slug: outreach-opportunity-stage-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/orgSetting" /> ## ⌵ Org Setting Actions'
  name: Outreach Org Setting API
  slug: outreach-org-setting-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/persona" /> ## Persona Relationships <SchemaDefinition schemaRef="#/components/schemas/personaRelationships" /> ## Persona Resource Metadata | **METAD'
  name: Outreach Persona API
  slug: outreach-persona-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/phoneNumber" /> ## Phone Number Relationships <SchemaDefinition schemaRef="#/components/schemas/phoneNumberRelationships" /> ## Phone Number Resource '
  name: Outreach Phone Number API
  slug: outreach-phone-number-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/product" /> ## Product Relationships <SchemaDefinition schemaRef="#/components/schemas/productRelationships" /> ## Product Resource Metadata | **METAD'
  name: Outreach Product API
  slug: outreach-product-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/profile" /> ## Profile Resource Metadata | **METADATA NAME**| **DESCRIPTION** | **QUERY PARAM** | | --- | --- | --- | | canWrite | A boolean value ind'
  name: Outreach Profile API
  slug: outreach-profile-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/prospect" /> ## Prospect Relationships <SchemaDefinition schemaRef="#/components/schemas/prospectRelationships" /> ## Prospect Resource Metadata | **M'
  name: Outreach Prospect API
  slug: outreach-prospect-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/prospectNote" /> ## Prospect Note Relationships <SchemaDefinition schemaRef="#/components/schemas/prospectNoteRelationships" /> ## ⌵ Prospect Note Act'
  name: Outreach Prospect Note API
  slug: outreach-prospect-note-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/purchase" /> ## Purchase Relationships <SchemaDefinition schemaRef="#/components/schemas/purchaseRelationships" /> ## Purchase Resource Metadata | **M'
  name: Outreach Purchase API
  slug: outreach-purchase-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/recipient" /> ## Recipient Relationships <SchemaDefinition schemaRef="#/components/schemas/recipientRelationships" /> ## Recipient Resource Metadata |'
  name: Outreach Recipient API
  slug: outreach-recipient-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/role" /> ## Role Relationships <SchemaDefinition schemaRef="#/components/schemas/roleRelationships" /> ## Role Resource Metadata | **METADATA NAME**| '
  name: Outreach Role API
  slug: outreach-role-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/ruleset" /> ## Ruleset Relationships <SchemaDefinition schemaRef="#/components/schemas/rulesetRelationships" /> ## Ruleset Resource Metadata | **METAD'
  name: Outreach Ruleset API
  slug: outreach-ruleset-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/sequence" /> ## Sequence Relationships <SchemaDefinition schemaRef="#/components/schemas/sequenceRelationships" /> ## Sequence Resource Metadata | **M'
  name: Outreach Sequence API
  slug: outreach-sequence-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/sequenceState" /> ## Sequence State Relationships <SchemaDefinition schemaRef="#/components/schemas/sequenceStateRelationships" /> ## Sequence State R'
  name: Outreach Sequence State API
  slug: outreach-sequence-state-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/sequenceStep" /> ## Sequence Step Relationships <SchemaDefinition schemaRef="#/components/schemas/sequenceStepRelationships" /> ## Sequence Step Resou'
  name: Outreach Sequence Step API
  slug: outreach-sequence-step-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/sequenceTemplate" /> ## Sequence Template Relationships <SchemaDefinition schemaRef="#/components/schemas/sequenceTemplateRelationships" /> ## Sequenc'
  name: Outreach Sequence Template API
  slug: outreach-sequence-template-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/snippet" /> ## Snippet Relationships <SchemaDefinition schemaRef="#/components/schemas/snippetRelationships" /> ## Snippet Resource Metadata | **METAD'
  name: Outreach Snippet API
  slug: outreach-snippet-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/stage" /> ## Stage Relationships <SchemaDefinition schemaRef="#/components/schemas/stageRelationships" /> ## Stage Resource Metadata | **METADATA NAME'
  name: Outreach Stage API
  slug: outreach-stage-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/task" /> ## Task Relationships <SchemaDefinition schemaRef="#/components/schemas/taskRelationships" /> ## Task Resource Metadata | **METADATA NAME**| '
  name: Outreach Task API
  slug: outreach-task-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/taskDisposition" /> ## Task Disposition Relationships <SchemaDefinition schemaRef="#/components/schemas/taskDispositionRelationships" /> ## Task Dispo'
  name: Outreach Task Disposition API
  slug: outreach-task-disposition-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/taskPriority" /> ## Task Priority Relationships <SchemaDefinition schemaRef="#/components/schemas/taskPriorityRelationships" /> ## ⌵ Task Priority Act'
  name: Outreach Task Priority API
  slug: outreach-task-priority-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/taskPurpose" /> ## Task Purpose Relationships <SchemaDefinition schemaRef="#/components/schemas/taskPurposeRelationships" /> ## Task Purpose Resource '
  name: Outreach Task Purpose API
  slug: outreach-task-purpose-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/team" /> ## Team Relationships <SchemaDefinition schemaRef="#/components/schemas/teamRelationships" /> ## Team Resource Metadata | **METADATA NAME**| '
  name: Outreach Team API
  slug: outreach-team-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/template" /> ## Template Relationships <SchemaDefinition schemaRef="#/components/schemas/templateRelationships" /> ## Template Resource Metadata | **M'
  name: Outreach Template API
  slug: outreach-template-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/user" /> ## User Relationships <SchemaDefinition schemaRef="#/components/schemas/userRelationships" /> ## User Resource Metadata | **METADATA NAME**| '
  name: Outreach User API
  slug: outreach-user-api
- baseURL: https://api.outreach.io/api/v2
  baseurl_source: declared
  description: '<SchemaDefinition schemaRef="#/components/schemas/webhook" /> ## Webhook Relationships <SchemaDefinition schemaRef="#/components/schemas/webhookRelationships" /> ## Webhook Resource Metadata | **METAD'
  name: Outreach Webhook API
  slug: outreach-webhook-api
artifact_total: 66
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/outreach-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/outreach-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/outreach-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/outreach-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/outreach-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/outreach-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.outreach.ai/platform/trust
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/outreach-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.outreach.ai/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outreach-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outreach-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/outreach-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outreach-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.outreach.io
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.outreach.io/api/deprecated-features
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/outreach-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/outreach-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/outreach-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getoutreach
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/outreach-saas
- group: company
  title: ''
  type: Website
  url: https://www.outreach.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.outreach.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.outreach.io/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.outreach.io/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.outreach.io/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.outreach.io/support/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.outreach.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.outreach.ai/request-demo
- group: start
  title: ''
  type: Login
  url: https://accounts.outreach.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outreach.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outreach.ai/privacy-statement
- group: commercial
  title: ''
  type: Plans
  url: plans/outreach-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outreach-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/outreach-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outreach-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.outreach.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.outreach.ai/resources/blog
created: '2026-05-08'
description: Outreach is a sales execution and revenue platform for go-to-market teams, unifying email, calling, social and meetings into sequenced outbound motions with AI agents layered on top. Its public developer surface is a JSON API 1.0 REST API at api.outreach.io/api/v2 covering accounts, prospects, opportunities, sequences, sequence states, mailings, calls, tasks, teams, users, imports and webhooks across 51 tagged resources and 253 operations, authorized by OAuth 2.0 with a scope-per-resource permission model and a separate server-to-server JWT token for unattended integrations. Outreach also runs a remote Model Context Protocol server at api.outreach.io/mcp with 41 tools, authorized by OAuth 2.1 with PKCE and Dynamic Client Registration, plus a client extensibility SDK for embedding web widgets inside the Outreach app, an event-driven webhook surface with HMAC-signed deliveries, and Outreach Data Sharing over Snowflake and Delta Sharing.
finops:
- name: Outreach Finops
  service_category: Sales
  slug: outreach-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outreach.png
json_schemas:
- name: Outreach Hyper
  property_count: 50
  slug: outreach-hyper
layout: provider
mcp_servers:
- description: ''
  name: Outreach MCP Server
  slug: outreach-mcp-server
modified: '2026-08-13'
name: Outreach
nav: Providers
network: true
overview: 'Outreach publishes 52 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, Account Note API, and 49 more. Tagged areas include Sales, Sales Engagement, Sequences, CRM, and Email.


  Outreach''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 31 more developer resources.'
plans:
- name: Outreach Plans Pricing
  plan_count: 4
  slug: outreach-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Outreach Rate Limits
  slug: outreach-rate-limits
scopes:
- name: Outreach Scopes
  scope_count: 46
  slug: outreach-scopes
  summary_line: 46 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 59.7
    developer_ergonomics: 66.1
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outreach/refs/heads/main/screenshots/outreach-2026-06-20T191233.png
security:
- kind: authentication
  name: Outreach Authentication
  slug: outreach-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Outreach Domain Security
  slug: outreach-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Outreach Vulnerability Disclosure
  slug: outreach-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Outreach Trust Center
  slug: outreach-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: outreach
tags:
- Sales
- Sales Engagement
- Sequences
- CRM
- Email
- Revenue Operations
- Sales Execution
- Prospecting
- Agents
- MCP
website: https://www.outreach.ai/
---
