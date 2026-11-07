---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Gong Agentic Access
  operation_count: 57
  slug: gong-agentic-access
  summary_line: 57 operations · 24 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: List calls, retrieve metadata, transcripts, recordings and trackers.
  name: Gong Calls API
  slug: gong-calls-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Read user, manager and team data.
  name: Gong Users API
  slug: gong-users-api
- description: Push CRM-style account, contact, deal and engagement data into Gong.
  name: Gong CRM Integration API
  slug: gong-crm-integration-api
- description: Read activity, scorecards, trackers, and library content.
  name: Gong Engagement Data API
  slug: gong-engagement-data-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Access and organize library folders and shared call collections.
  name: Gong Library API
  slug: gong-library-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Operations for managing and retrieving call data
  name: Gong Calls API
  slug: gong-calls-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Operations for data privacy management and compliance
  name: Gong Data Privacy API
  slug: gong-data-privacy-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Operations for posting digital interaction data
  name: Gong Digital Interactions API
  slug: gong-digital-interactions-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Operations for browsing and retrieving library content
  name: Gong Library API
  slug: gong-library-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Operations for managing permission profiles
  name: Gong Permission Profiles API
  slug: gong-permission-profiles-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: Operations for managing and retrieving user data
  name: Gong Users API
  slug: gong-users-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Accounts Enrich” API endpoints allow you to enrich your account records with Gong's data.</h3> <p>Enrichment is asynchronous and works in two steps:</p> <ol> <li> Submit up to 10 accounts,
  name: Gong Accounts Enrich API
  slug: gong-accounts-enrich-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Auditing” API endpoints allow you to request the following log types from Gong:</h3> <ul> <li> Access Log - This log is preserved for 14 days only </li> <li> User Activity Log - The data i
  name: Gong Auditing API
  slug: gong-auditing-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: The Coaching API from Gong — 1 operation(s) for coaching.
  name: Gong Coaching API
  slug: gong-coaching-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Contacts Enrich” API endpoints allow you to enrich your contact records with Gong's data.</h3> <p>Enrichment is asynchronous and works in two steps:</p> <ol> <li> Submit up to 10 contacts,
  name: Gong Contacts Enrich API
  slug: gong-contacts-enrich-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: '<style>.public-api-info { background: rgb(222, 235, 255);}.public-api-tip { background: rgb(227, 252, 239);}.public-api-parameter { background: rgba(9,30,66,0.08);}.public-api-note { background: rgb(2'
  name: Gong CRM API
  slug: gong-crm-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Flows” API endpoints allow you to:</h3> <ul> <li> View a list of relevant Gong Engage flows to choose from and the current flow assignment status </li> <li> Add prospects to Gong Engage fl
  name: Gong Engage Flows API
  slug: gong-engage-flows-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Limited release - contact <a href="mailto:integration.requests@gong.io">integration.requests@gong.io</a> for more information. </h3> <h3>Gong’s "Engagement" API endpoints allow you to push engagem
  name: Gong Engagement (Legacy – See “Digital Interactions”) API
  slug: gong-engagement-legacy-see-digital-interactions-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong's “Entity” endpoints allow you to:</h3> <ul> <li> Ask questions in natural language about CRM entities (accounts, contacts, deals, leads) and get AI-generated insights based on data from call
  name: Gong Entities API
  slug: gong-entities-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <p>Configure your integration settings for displaying your company data in iFrames. For example, use this API to configure dynamic links as the iFrame source. This endpoint includes validation mechani
  name: Gong Integration Settings API
  slug: gong-integration-settings-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Consent Meeting” API endpoints allow you to:</h3> <ul> <li> Request creating a Gong Consent meeting link </li> <li> Update a Consent Meeting’s details </li> <li> Delete a Consent Meeting <
  name: Gong Meetings (in Beta Phase) API
  slug: gong-meetings-in-beta-phase-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: The Outcomes API from Gong — 1 operation(s) for outcomes.
  name: Gong Outcomes API
  slug: gong-outcomes-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s "Permission" API endpoints allow you to:</h3> <ul> <li> List all permission profiles in a given workspace </li> <li> Create permission profile </li> <li> Get a permission profile </li> <li>
  name: Gong Permissions API
  slug: gong-permissions-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Settings” API endpoints allow you to:</h3> <ul> <li> Request all the scorecards within the Gong system. </li> <li> Request all the workspaces including their details. </li> </ul>
  name: Gong Settings API
  slug: gong-settings-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: <h3>Gong’s “Stats” API endpoints allow you to:</h3> <ul> <li> Request user activity </li> <li> Request scorecards activity </li> <li> Request interaction stats on calls that have Whisper turned on </l
  name: Gong Stats API
  slug: gong-stats-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: The Targets API from Gong — 2 operation(s) for targets.
  name: Gong Targets API
  slug: gong-targets-api
- baseURL: https://api.gong.io/v2
  baseurl_source: declared
  description: The Tasks API from Gong — 2 operation(s) for tasks.
  name: Gong Tasks API
  slug: gong-tasks-api
artifact_total: 177
asyncapis:
- description: ''
  name: Gong Webhooks
  slug: gong-webhooks
collections:
- collection_type: open
  name: Gong Auditing Audit Logs API
  slug: open-gong-audit-logs-api
- collection_type: open
  name: Gong Auditing API
  slug: open-gong-auditing
- collection_type: open
  name: Gong Auditing Audit Logs Calls API
  slug: open-gong-calls-api
- collection_type: open
  name: Gong Calls API
  slug: open-gong-calls
- collection_type: open
  name: Gong Auditing Audit Logs CRM Data API
  slug: open-gong-crm-data-api
- collection_type: open
  name: Gong Auditing Audit Logs CRM Integration API
  slug: open-gong-crm-integration-api
- collection_type: open
  name: Gong Auditing Audit Logs CRM Schema API
  slug: open-gong-crm-schema-api
- collection_type: open
  name: Gong CRM API
  slug: open-gong-crm
- collection_type: open
  name: Gong Auditing Audit Logs Data Privacy API
  slug: open-gong-data-privacy-api
- collection_type: open
  name: Gong Data Privacy API
  slug: open-gong-data-privacy
- collection_type: open
  name: Gong Auditing Audit Logs Digital Interactions API
  slug: open-gong-digital-interactions-api
- collection_type: open
  name: Gong Engage API
  slug: open-gong-engage
- collection_type: open
  name: Gong Auditing Audit Logs Engagement Events API
  slug: open-gong-engagement-events-api
- collection_type: open
  name: Gong Engagement API
  slug: open-gong-engagement
- collection_type: open
  name: Gong Auditing Audit Logs Flows API
  slug: open-gong-flows-api
- collection_type: open
  name: Gong Auditing Audit Logs Folders API
  slug: open-gong-folders-api
- collection_type: open
  name: Gong Auditing Audit Logs Library API
  slug: open-gong-library-api
- collection_type: open
  name: Gong Library API
  slug: open-gong-library
- collection_type: open
  name: Gong Auditing Audit Logs Meetings API
  slug: open-gong-meetings-api
- collection_type: open
  name: Gong Meetings API
  slug: open-gong-meetings
- collection_type: open
  name: Gong Auditing Audit Logs Permission Profiles API
  slug: open-gong-permission-profiles-api
- collection_type: open
  name: Gong Permissions API
  slug: open-gong-permissions
- collection_type: open
  name: Gong Auditing Audit Logs Prospects API
  slug: open-gong-prospects-api
- collection_type: open
  name: Gong Auditing Audit Logs Recordings API
  slug: open-gong-recordings-api
- collection_type: open
  name: Gong Auditing Audit Logs Scorecards API
  slug: open-gong-scorecards-api
- collection_type: open
  name: Gong Settings API
  slug: open-gong-settings
- collection_type: open
  name: Gong Auditing Audit Logs Statistics API
  slug: open-gong-statistics-api
- collection_type: open
  name: Gong Stats API
  slug: open-gong-stats
- collection_type: open
  name: Gong Auditing Audit Logs Trackers API
  slug: open-gong-trackers-api
- collection_type: open
  name: Gong Auditing Audit Logs Transcripts API
  slug: open-gong-transcripts-api
- collection_type: open
  name: Gong Auditing Audit Logs Users API
  slug: open-gong-users-api
- collection_type: open
  name: Gong Users API
  slug: open-gong-users
- collection_type: open
  name: Gong Auditing Audit Logs Workspaces API
  slug: open-gong-workspaces-api
common:
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-audit-logs-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-audit-logs-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-crm-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-crm-data-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-crm-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-crm-integration-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-crm-schema-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-crm-schema-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-engagement-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-engagement-events-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-flows-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-flows-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-folders-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-folders-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-meetings-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-meetings-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-prospects-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-prospects-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-recordings-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-recordings-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-scorecards-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-scorecards-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-statistics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-statistics-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-trackers-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-trackers-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-transcripts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-transcripts-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/overlays/gong-workspaces-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gong-workspaces-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gong/capabilities/gong-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gong-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gong/agentic-access/gong-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gong-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gong/security/gong-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gong-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gong/security/gong-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gong-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gong/authentication/gong-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gong-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gong-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gong-io
- group: company
  title: ''
  type: Website
  url: https://www.gong.io/
- group: commercial
  href: https://artifacts.apis.io/gong/plans/gong-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gong-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gong/rate-limits/gong-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gong-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gong/finops/gong-finops.yml
  title: ''
  type: FinOps
  url: finops/gong-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://app.gong.io/settings/api/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app.gong.io/settings/api/documentation
- group: operate
  title: ''
  type: Help
  url: https://app.gong.io/help
- group: start
  title: ''
  type: GettingStarted
  url: https://app.gong.io/help/docs/api
- group: start
  title: ''
  type: Login
  url: https://app.gong.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gong.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.gong.io/blog
- group: operate
  title: ''
  type: Status
  url: https://status.gong.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gong.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gong.io/terms-of-service
- group: auth
  title: ''
  type: Trust
  url: https://www.gong.io/trust-center
- group: auth
  title: ''
  type: Security
  url: https://www.gong.io/trust-center/security
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gong-io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/gong_io
- group: build
  href: https://artifacts.apis.io/gong/packages/gong-packages.yml
  title: ''
  type: Packages
  url: packages/gong-packages.yml
- group: build
  href: https://artifacts.apis.io/gong/packages/gong-packages.yml
  title: ''
  type: SDKs
  url: packages/gong-packages.yml
- group: agent
  href: https://artifacts.apis.io/gong/well-known/gong-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gong-well-known.yml
- group: agent
  href: https://artifacts.apis.io/gong/mcp/gong-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gong-mcp.yml
- group: build
  href: https://artifacts.apis.io/gong/mcp/gong-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gong-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gong/llms/gong-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gong-llms.txt
- group: design
  href: https://artifacts.apis.io/gong/conformance/gong-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gong-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gong.io/security
- group: design
  href: https://artifacts.apis.io/gong/errors/gong-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gong-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gong/lifecycle/gong-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gong-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gong.io
- group: operate
  title: ''
  type: Deprecation
  url: https://help.gong.io/docs/public-api-change-deprecating-call-action-items-in-the-extensive-endpoint
- group: auth
  href: https://artifacts.apis.io/gong/scopes/gong-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gong-scopes.yml
- group: auth
  href: https://artifacts.apis.io/gong/security/gong-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gong-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/gong/sandbox/gong-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gong-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gong/conventions/gong-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gong-conventions.yml
- group: operate
  href: https://artifacts.apis.io/gong/changelog/gong-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gong-changelog.yml
- group: design
  href: https://artifacts.apis.io/gong/components/gong-components.yml
  title: ''
  type: Components
  url: components/gong-components.yml
- group: design
  href: https://artifacts.apis.io/gong/data-model/gong-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gong-data-model.yml
- group: design
  href: https://artifacts.apis.io/gong/asyncapi/gong-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gong-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/gong/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.gong.io/docs/how-to-use-the-gong-developers-hub
- group: operate
  title: ''
  type: Support
  url: https://contact.gong.io/hc/en-us/requests/new
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.gong.io/
created: '2026-05-08'
description: Gong is the revenue intelligence platform that captures and analyzes customer interactions across calls, emails, meetings and web conferencing, then applies AI to surface deal risk, coaching signal and forecast correction for B2B go-to-market teams. Its public REST v2 API at api.gong.io exposes 57 operations covering calls, transcripts, recordings, users, permission profiles, workspaces, statistics, scorecards, trackers, library content, Engage flows and prospects, engagement events, meetings, audit logs, generic CRM ingestion and GDPR/CCPA data-privacy erasure. Gong also runs an official remote MCP server at mcp.gong.io for external AI agents, a rule-driven outbound webhook surface for calls, and a frontend SDK for partner apps embedded in the Gong UI.
finops:
- has_sources: true
  method: derived
  name: Gong Finops
  primary_unit: ''
  service_category: ''
  slug: gong-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gong.png
json_schemas:
- name: AggregatedActivityRequest
  property_count: 2
  slug: gong-aggregatedactivityrequest
- name: AggregatedActivityResponse
  property_count: 3
  slug: gong-aggregatedactivityresponse
- name: AnsweredScorecard
  property_count: 8
  slug: gong-answeredscorecard
- name: AnsweredScorecardsRequest
  property_count: 2
  slug: gong-answeredscorecardsrequest
- name: AnsweredScorecardsResponse
  property_count: 3
  slug: gong-answeredscorecardsresponse
- name: AssignProspectsRequest
  property_count: 3
  slug: gong-assignprospectsrequest
- name: AssignProspectsResponse
  property_count: 3
  slug: gong-assignprospectsresponse
- name: AuditLogEntry
  property_count: 10
  slug: gong-auditlogentry
- name: AuditLogsResponse
  property_count: 3
  slug: gong-auditlogsresponse
- name: BaseResponse
  property_count: 1
  slug: gong-baseresponse
- name: Gong Call
  property_count: 13
  slug: gong-call
- name: CallParty
  property_count: 9
  slug: gong-callparty
- name: CallsResponse
  property_count: 3
  slug: gong-callsresponse
- name: CallTranscript
  property_count: 2
  slug: gong-calltranscript
- name: CallTranscriptRequest
  property_count: 2
  slug: gong-calltranscriptrequest
- name: CallTranscriptsResponse
  property_count: 3
  slug: gong-calltranscriptsresponse
- name: CoachingMetricsResponse
  property_count: 2
  slug: gong-coachingmetricsresponse
- name: ContentShareEventRequest
  property_count: 8
  slug: gong-contentshareeventrequest
- name: ContentViewEventRequest
  property_count: 9
  slug: gong-contentvieweventrequest
- name: CreateMeetingRequest
  property_count: 9
  slug: gong-createmeetingrequest
- name: CreatePermissionProfileRequest
  property_count: 3
  slug: gong-createpermissionprofilerequest
- name: CrmEntitiesUploadRequest
  property_count: 1
  slug: gong-crmentitiesuploadrequest
- name: CrmEntitiesUploadResponse
  property_count: 3
  slug: gong-crmentitiesuploadresponse
- name: CrmEntitySchemaResponse
  property_count: 2
  slug: gong-crmentityschemaresponse
- name: CrmEntitySchemaUploadRequest
  property_count: 3
  slug: gong-crmentityschemauploadrequest
- name: CrmIntegrationRegistrationRequest
  property_count: 4
  slug: gong-crmintegrationregistrationrequest
- name: CrmIntegrationRegistrationResponse
  property_count: 2
  slug: gong-crmintegrationregistrationresponse
- name: CrmIntegrationsResponse
  property_count: 2
  slug: gong-crmintegrationsresponse
- name: CrmObjectsResponse
  property_count: 2
  slug: gong-crmobjectsresponse
- name: CustomActionEventRequest
  property_count: 6
  slug: gong-customactioneventrequest
- name: DailyActivityRequest
  property_count: 2
  slug: gong-dailyactivityrequest
- name: DailyActivityResponse
  property_count: 3
  slug: gong-dailyactivityresponse
- name: DataDeletionResponse
  property_count: 2
  slug: gong-datadeletionresponse
- name: DataReference
  property_count: 4
  slug: gong-datareference
- name: DetailedCall
  property_count: 4
  slug: gong-detailedcall
- name: DigitalInteractionRequest
  property_count: 8
  slug: gong-digitalinteractionrequest
- name: DigitalInteractionResponse
  property_count: 2
  slug: gong-digitalinteractionresponse
- name: EmailDeleteRequest
  property_count: 1
  slug: gong-emaildeleterequest
- name: EmailReferencesResponse
  property_count: 3
  slug: gong-emailreferencesresponse
- name: ErrorResponse
  property_count: 2
  slug: gong-errorresponse
- name: ExtensiveCallsRequest
  property_count: 3
  slug: gong-extensivecallsrequest
- name: ExtensiveCallsResponse
  property_count: 3
  slug: gong-extensivecallsresponse
- name: Gong Engage Flow
  property_count: 10
  slug: gong-flow
- name: FlowContentOverrideRequest
  property_count: 1
  slug: gong-flowcontentoverriderequest
- name: FlowFolder
  property_count: 5
  slug: gong-flowfolder
- name: FlowFoldersResponse
  property_count: 2
  slug: gong-flowfoldersresponse
- name: FlowsResponse
  property_count: 3
  slug: gong-flowsresponse
- name: IntegrationSettingsRequest
  property_count: 4
  slug: gong-integrationsettingsrequest
- name: InteractionStatsRequest
  property_count: 2
  slug: gong-interactionstatsrequest
- name: InteractionStatsResponse
  property_count: 3
  slug: gong-interactionstatsresponse
- name: LibraryCall
  property_count: 8
  slug: gong-librarycall
- name: LibraryFolder
  property_count: 7
  slug: gong-libraryfolder
- name: LibraryFolderCallsResponse
  property_count: 2
  slug: gong-libraryfoldercallsresponse
- name: LibraryFoldersResponse
  property_count: 2
  slug: gong-libraryfoldersresponse
- name: ManualAssociationResponse
  property_count: 3
  slug: gong-manualassociationresponse
- name: Gong Meeting
  property_count: 10
  slug: gong-meeting
- name: MeetingAttendee
  property_count: 3
  slug: gong-meetingattendee
- name: MeetingIntegrationStatusRequest
  property_count: 2
  slug: gong-meetingintegrationstatusrequest
- name: MeetingIntegrationStatusResponse
  property_count: 5
  slug: gong-meetingintegrationstatusresponse
- name: MeetingResponse
  property_count: 3
  slug: gong-meetingresponse
- name: NewCallAddingRequest
  property_count: 14
  slug: gong-newcalladdingrequest
- name: NewCallAddingResponse
  property_count: 2
  slug: gong-newcalladdingresponse
- name: NewCallParty
  property_count: 4
  slug: gong-newcallparty
- name: NewCallRecordingResponse
  property_count: 2
  slug: gong-newcallrecordingresponse
- name: PermissionProfile
  property_count: 6
  slug: gong-permissionprofile
- name: PermissionProfileResponse
  property_count: 2
  slug: gong-permissionprofileresponse
- name: PermissionProfilesResponse
  property_count: 2
  slug: gong-permissionprofilesresponse
- name: PermissionProfileUsersResponse
  property_count: 2
  slug: gong-permissionprofileusersresponse
- name: PhoneDeleteRequest
  property_count: 1
  slug: gong-phonedeleterequest
- name: PhoneReferencesResponse
  property_count: 3
  slug: gong-phonereferencesresponse
- name: Gong Prospect
  property_count: 8
  slug: gong-prospect
- name: ProspectsFlowsRequest
  property_count: 1
  slug: gong-prospectsflowsrequest
- name: ProspectsFlowsResponse
  property_count: 2
  slug: gong-prospectsflowsresponse
- name: Gong Scorecard
  property_count: 7
  slug: gong-scorecard
- name: ScorecardQuestion
  property_count: 5
  slug: gong-scorecardquestion
- name: ScorecardsResponse
  property_count: 2
  slug: gong-scorecardsresponse
- name: SpecificCallResponse
  property_count: 2
  slug: gong-specificcallresponse
- name: Tracker
  property_count: 6
  slug: gong-tracker
- name: TrackersResponse
  property_count: 2
  slug: gong-trackersresponse
- name: Gong Call Transcript
  property_count: 2
  slug: gong-transcript
- name: UnassignProspectsRequest
  property_count: 1
  slug: gong-unassignprospectsrequest
- name: UnassignProspectsResponse
  property_count: 2
  slug: gong-unassignprospectsresponse
- name: UpdateMeetingRequest
  property_count: 6
  slug: gong-updatemeetingrequest
- name: UpdatePermissionProfileRequest
  property_count: 3
  slug: gong-updatepermissionprofilerequest
- name: UploadStatusResponse
  property_count: 5
  slug: gong-uploadstatusresponse
- name: Gong User
  property_count: 16
  slug: gong-user
- name: UserAggregatedActivity
  property_count: 9
  slug: gong-useraggregatedactivity
- name: UserCallAccessRequest
  property_count: 1
  slug: gong-usercallaccessrequest
- name: UserCallAccessResponse
  property_count: 2
  slug: gong-usercallaccessresponse
- name: UserCallAccessUpdateRequest
  property_count: 2
  slug: gong-usercallaccessupdaterequest
- name: UserInteractionStats
  property_count: 7
  slug: gong-userinteractionstats
- name: UserResponse
  property_count: 2
  slug: gong-userresponse
- name: UserSettingsHistoryResponse
  property_count: 2
  slug: gong-usersettingshistoryresponse
- name: UsersFilterRequest
  property_count: 2
  slug: gong-usersfilterrequest
- name: UsersResponse
  property_count: 3
  slug: gong-usersresponse
- name: Gong Workspace
  property_count: 3
  slug: gong-workspace
- name: WorkspacesResponse
  property_count: 2
  slug: gong-workspacesresponse
json_structures:
- name: Gong Structure
  property_count: 0
  slug: gong-structure
jsonld:
- class_count: 0
  name: Gong Context
  property_count: 13
  slug: gong-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.gong.io over HTTP requiring OAuth; 3 tools listed.
  name: Gong MCP server
  slug: gong-mcp-server
modified: '2026-08-13'
name: Gong
nav: Providers
network: true
overview: 'Gong publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calls API, Users API, Library API, and 24 more. Tagged areas include Sales, Revenue Intelligence, Conversations, Analytics, and Artificial Intelligence.


  The Gong catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gong''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, status page, and 57 more developer resources.'
plans:
- name: Gong Plans Pricing
  plan_count: 0
  slug: gong-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Gong Rate Limits
  slug: gong-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Gong — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: gong-jsonschema-spectral-rules
scopes:
- name: Gong Scopes
  scope_count: 6
  slug: gong-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 36
    catalog_earned: 59.3
    catalog_earned_first_party: 8.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 43.4
    contract_governance: 28.0
    contract_quality: 65.7
    developer_ergonomics: 67.3
    discoverability: 80.0
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 39.2
      total: 51
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/gong/gong-2026-06-20T182025.png
security:
- kind: authentication
  name: Gong Authentication
  slug: gong-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Gong Domain Security
  slug: gong-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gong Vulnerability Disclosure
  slug: gong-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Gong Trust Center
  slug: gong-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO/IEC 42001:2023, PCI DSS (SAQ D), CSA STAR, EU-U.S. Data Privacy Framework
skill_count: 6
skills:
- name: Audit Gong users, permissions and admin activity
  slug: gong-audit-users-and-access
- name: Handle a Gong data subject erasure request
  slug: gong-handle-data-subject-request
- name: Manage Gong Engage flows and prospects
  slug: gong-manage-engage-flows
- name: Pull Gong calls and transcripts
  slug: gong-pull-calls-and-transcripts
- name: Push CRM data into Gong
  slug: gong-sync-crm-data
- name: Upload an externally recorded call to Gong
  slug: gong-upload-an-external-call
slug: gong
tags:
- Sales
- Revenue Intelligence
- Conversations
- Analytics
- Artificial Intelligence
- Conversation Intelligence
- Sales Engagement
- CRM
- Forecasting
- Transcription
- Agents
website: https://www.gong.io/
---
