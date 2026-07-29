---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Gong Agentic Access
  operation_count: 57
  slug: gong-agentic-access
  summary_line: 57 operations · 33 acting · 1 human-in-the-loop
api_count: 26
apis:
- description: List calls, retrieve metadata, transcripts, recordings and trackers.
  name: Gong Calls API
  slug: gong-calls-api
- description: Read user, manager and team data.
  name: Gong Users API
  slug: gong-users-api
- description: Push CRM-style account, contact, deal and engagement data into Gong.
  name: Gong CRM Integration API
  slug: gong-crm-integration-api
- description: Read activity, scorecards, trackers, and library content.
  name: Gong Engagement Data API
  slug: gong-engagement-data-api
- description: Access and organize library folders and shared call collections.
  name: Gong Library API
  slug: gong-library-api
- description: Operations for retrieving audit log data
  name: Gong Audit Logs API
  slug: gong-audit-logs-api
- description: Operations for managing and retrieving call data
  name: Gong Calls API
  slug: gong-calls-api
- description: Operations for uploading and retrieving CRM data
  name: Gong CRM Data API
  slug: gong-crm-data-api
- description: Operations for registering and managing CRM integrations
  name: Gong CRM Integration API
  slug: gong-crm-integration-api
- description: Operations for managing CRM object schemas
  name: Gong CRM Schema API
  slug: gong-crm-schema-api
- description: Operations for data privacy management and compliance
  name: Gong Data Privacy API
  slug: gong-data-privacy-api
- description: Operations for posting digital interaction data
  name: Gong Digital Interactions API
  slug: gong-digital-interactions-api
- description: Operations for reporting customer engagement events
  name: Gong Engagement Events API
  slug: gong-engagement-events-api
- description: Operations for managing Engage flows
  name: Gong Flows API
  slug: gong-flows-api
- description: Operations for managing flow folders
  name: Gong Folders API
  slug: gong-folders-api
- description: Operations for browsing and retrieving library content
  name: Gong Library API
  slug: gong-library-api
- description: Operations for managing meetings
  name: Gong Meetings API
  slug: gong-meetings-api
- description: Operations for managing permission profiles
  name: Gong Permission Profiles API
  slug: gong-permission-profiles-api
- description: Operations for managing prospects in Engage flows
  name: Gong Prospects API
  slug: gong-prospects-api
- description: Operations for managing call recordings and media
  name: Gong Recordings API
  slug: gong-recordings-api
- description: Operations for retrieving scorecard configurations
  name: Gong Scorecards API
  slug: gong-scorecards-api
- description: Operations for retrieving activity and performance statistics
  name: Gong Statistics API
  slug: gong-statistics-api
- description: Operations for retrieving tracker configurations
  name: Gong Trackers API
  slug: gong-trackers-api
- description: Operations for retrieving call transcripts
  name: Gong Transcripts API
  slug: gong-transcripts-api
- description: Operations for managing and retrieving user data
  name: Gong Users API
  slug: gong-users-api
- description: Operations for managing workspaces
  name: Gong Workspaces API
  slug: gong-workspaces-api
artifact_total: 145
collections:
- collection_type: open
  name: Gong Auditing API
  slug: open-gong-auditing
- collection_type: open
  name: Gong Calls API
  slug: open-gong-calls
- collection_type: open
  name: Gong CRM API
  slug: open-gong-crm
- collection_type: open
  name: Gong Data Privacy API
  slug: open-gong-data-privacy
- collection_type: open
  name: Gong Engage API
  slug: open-gong-engage
- collection_type: open
  name: Gong Engagement API
  slug: open-gong-engagement
- collection_type: open
  name: Gong Library API
  slug: open-gong-library
- collection_type: open
  name: Gong Meetings API
  slug: open-gong-meetings
- collection_type: open
  name: Gong Permissions API
  slug: open-gong-permissions
- collection_type: open
  name: Gong Settings API
  slug: open-gong-settings
- collection_type: open
  name: Gong Stats API
  slug: open-gong-stats
- collection_type: open
  name: Gong Users API
  slug: open-gong-users
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gong-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gong-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gong-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/gong-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gong-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gong-finops.yml
created: '2026-05-08'
description: Gong is the revenue intelligence platform that captures and analyzes customer interactions across calls, emails, and meetings. APIs expose calls, transcripts, deals, users, and analytics.
finops:
- name: Gong Finops
  service_category: Sales
  slug: gong-finops
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
  property_count: 0
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
modified: '2026-05-08'
name: Gong
nav: Providers
network: true
overview: 'Gong publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Users API, CRM Integration API, and 22 more. Tagged areas include Sales, Revenue Intelligence, Conversation, Analytics, and AI.


  The Gong catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gong''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Gong Plans Pricing
  plan_count: 1
  slug: gong-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Gong Rate Limits
  slug: gong-rate-limits
rules:
- name: Gong API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: gong-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.6
  delta: -3.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 68.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gong/refs/heads/main/screenshots/gong-2026-06-20T182025.png
security:
- kind: authentication
  name: Gong Authentication
  slug: gong-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Gong Domain Security
  slug: gong-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gong Trust Center
  slug: gong-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, CSA STAR
slug: gong
tags:
- Sales
- Revenue Intelligence
- Conversation
- Analytics
- AI
website: https://www.gong.io/
---
