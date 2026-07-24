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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 61
  human_in_the_loop: 6
  name: Opsgenie Agentic Access
  operation_count: 105
  slug: opsgenie-agentic-access
  summary_line: 105 operations · 61 acting · 6 human-in-the-loop
api_count: 15
apis:
- description: Operations for retrieving account information and configuration.
  name: OpsGenie Account API
  slug: opsgenie-account-api
- description: Operations for creating, retrieving, updating, and managing alerts within the OpsGenie platform.
  name: OpsGenie Alerts API
  slug: opsgenie-alerts-api
- description: Operations for creating, retrieving, updating, and deleting escalation policies.
  name: OpsGenie Escalations API
  slug: opsgenie-escalations-api
- description: Operations for creating, managing, and pinging heartbeat monitors.
  name: OpsGenie Heartbeats API
  slug: opsgenie-heartbeats-api
- description: Operations for creating, retrieving, updating, closing, and resolving incidents within the OpsGenie platform.
  name: OpsGenie Incidents API
  slug: opsgenie-incidents-api
- description: Operations for creating, retrieving, enabling, disabling, and managing integrations.
  name: OpsGenie Integrations API
  slug: opsgenie-integrations-api
- description: Operations for creating, listing, retrieving, and deleting maintenance windows.
  name: OpsGenie Maintenance API
  slug: opsgenie-maintenance-api
- description: Operations for managing user notification rules and their steps.
  name: OpsGenie Notification Rules API
  slug: opsgenie-notification-rules-api
- description: Operations for querying on-call participants.
  name: OpsGenie On-Call API
  slug: opsgenie-on-call-api
- description: Operations for managing schedule overrides.
  name: OpsGenie Overrides API
  slug: opsgenie-overrides-api
- description: Operations for managing schedule rotations.
  name: OpsGenie Rotations API
  slug: opsgenie-rotations-api
- description: Operations for managing on-call schedules.
  name: OpsGenie Schedules API
  slug: opsgenie-schedules-api
- description: Operations for creating, retrieving, updating, and deleting services in the service catalog.
  name: OpsGenie Services API
  slug: opsgenie-services-api
- description: Operations for creating, retrieving, updating, and deleting teams and managing team membership.
  name: OpsGenie Teams API
  slug: opsgenie-teams-api
- description: Operations for creating, retrieving, updating, and deleting user accounts within the OpsGenie platform.
  name: OpsGenie Users API
  slug: opsgenie-users-api
artifact_total: 159
asyncapis:
- description: OpsGenie sends webhook notifications for alert actions to configured webhook URLs. When alert events occur such as create, acknowledge, close, or delete, OpsGenie posts a JSON payload to the registere
  name: OpsGenie Webhook Events
  slug: opsgenie-webhook-asyncapi
collections:
- collection_type: open
  name: OpsGenie Account API
  slug: open-opsgenie-account
- collection_type: open
  name: OpsGenie Alert API
  slug: open-opsgenie-alert
- collection_type: open
  name: OpsGenie Escalation API
  slug: open-opsgenie-escalation
- collection_type: open
  name: OpsGenie Heartbeat API
  slug: open-opsgenie-heartbeat
- collection_type: open
  name: OpsGenie Incident API
  slug: open-opsgenie-incident
- collection_type: open
  name: OpsGenie Integration API
  slug: open-opsgenie-integration
- collection_type: open
  name: OpsGenie Maintenance API
  slug: open-opsgenie-maintenance
- collection_type: open
  name: OpsGenie Notification Rule API
  slug: open-opsgenie-notification-rule
- collection_type: open
  name: OpsGenie Schedule API
  slug: open-opsgenie-schedule
- collection_type: open
  name: OpsGenie Service API
  slug: open-opsgenie-service
- collection_type: open
  name: OpsGenie Team API
  slug: open-opsgenie-team
- collection_type: open
  name: OpsGenie User API
  slug: open-opsgenie-user
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opsgenie-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opsgenie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opsgenie-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opsgenie-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opsgenie
- group: start
  title: ''
  type: Portal
  url: https://docs.opsgenie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opsgenie.com/docs
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/opsgenie
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/software-license-agreement
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/opsgenie/
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.opsgenie.com/auth/login
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.opsgenie.com/llms.txt
created: '2025-03-01'
description: OpsGenie is an incident management and alerting platform, now part of Atlassian, that helps operations teams manage on-call schedules, route alerts, and coordinate incident response. The OpsGenie developer platform provides a comprehensive set of REST APIs for programmatically managing alerts, incidents, teams, schedules, escalations, integrations, heartbeats, services, notification rules, accounts, and maintenance windows.
features:
- 'Free: 5 users, 1 schedule, 1 escalation policy'
- 'Essentials: $9.45/user/mo'
- 'Standard: $19.95/user/mo with stakeholder comms + dashboards'
- 'Enterprise: $31.90/user/mo with PIRs, audit logs, ServiceNow'
- 'End-of-life: new sales ended 2025-06-04; migrate to JSM/Compass by 2027-04-05'
- REST API at api.opsgenie.com (eu/us regions)
- 'Alerts API: 60 req/min standard, up to 10K req/min for HV integrations'
- 'Other endpoints: 600 req/min/key'
- 200+ integrations with monitoring tools
- On-call schedules with rotations
- Escalation policies with multi-channel notification
- Heartbeat monitoring (Standard+)
- Status pages built-in (Essentials+)
- Post-incident reviews (Enterprise)
- Audit logs (Enterprise)
- GenieKey-based authentication (per integration)
finops:
- name: Opsgenie Finops
  service_category: Incident Response
  slug: opsgenie-finops
graphqls:
- description: OpsGenie is an incident management and alerting platform, now part of Atlassian, that helps operations teams manage on-call schedules, route alerts, and coordinate incident response. While OpsGenie cu
  name: OpsGenie (Atlassian) GraphQL Schema
  slug: opsgenie-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opsgenie.png
json_schemas:
- name: Account
  property_count: 3
  slug: opsgenie-account
- name: AddDetailsRequest
  property_count: 4
  slug: opsgenie-adddetailsrequest
- name: AddNoteRequest
  property_count: 3
  slug: opsgenie-addnoterequest
- name: AddResponderRequest
  property_count: 4
  slug: opsgenie-addresponderrequest
- name: AddTagsRequest
  property_count: 4
  slug: opsgenie-addtagsrequest
- name: OpsGenie Alert
  property_count: 25
  slug: opsgenie-alert
- name: AlertActionRequest
  property_count: 3
  slug: opsgenie-alertactionrequest
- name: AssignAlertRequest
  property_count: 4
  slug: opsgenie-assignalertrequest
- name: AsyncRequestResponse
  property_count: 3
  slug: opsgenie-asyncrequestresponse
- name: CloseAlertRequest
  property_count: 3
  slug: opsgenie-closealertrequest
- name: CloseIncidentRequest
  property_count: 1
  slug: opsgenie-closeincidentrequest
- name: CountAlertsResponse
  property_count: 3
  slug: opsgenie-countalertsresponse
- name: CreateAlertRequest
  property_count: 13
  slug: opsgenie-createalertrequest
- name: CreateEscalationRequest
  property_count: 5
  slug: opsgenie-createescalationrequest
- name: CreateHeartbeatRequest
  property_count: 9
  slug: opsgenie-createheartbeatrequest
- name: CreateIncidentRequest
  property_count: 9
  slug: opsgenie-createincidentrequest
- name: CreateIntegrationRequest
  property_count: 8
  slug: opsgenie-createintegrationrequest
- name: CreateIntegrationResponse
  property_count: 3
  slug: opsgenie-createintegrationresponse
- name: CreateMaintenanceRequest
  property_count: 3
  slug: opsgenie-createmaintenancerequest
- name: CreateNotificationRuleRequest
  property_count: 10
  slug: opsgenie-createnotificationrulerequest
- name: CreateNotificationRuleResponse
  property_count: 3
  slug: opsgenie-createnotificationruleresponse
- name: CreateNotificationRuleStepRequest
  property_count: 3
  slug: opsgenie-createnotificationrulesteprequest
- name: CreateOverrideRequest
  property_count: 4
  slug: opsgenie-createoverriderequest
- name: CreateRotationRequest
  property_count: 7
  slug: opsgenie-createrotationrequest
- name: CreateScheduleRequest
  property_count: 6
  slug: opsgenie-createschedulerequest
- name: CreateServiceRequest
  property_count: 5
  slug: opsgenie-createservicerequest
- name: CreateTeamRequest
  property_count: 3
  slug: opsgenie-createteamrequest
- name: CreateUserRequest
  property_count: 10
  slug: opsgenie-createuserrequest
- name: ErrorResponse
  property_count: 3
  slug: opsgenie-errorresponse
- name: EscalateAlertRequest
  property_count: 4
  slug: opsgenie-escalatealertrequest
- name: Escalation
  property_count: 6
  slug: opsgenie-escalation
- name: EscalationRule
  property_count: 4
  slug: opsgenie-escalationrule
- name: GetAccountResponse
  property_count: 3
  slug: opsgenie-getaccountresponse
- name: GetAlertResponse
  property_count: 3
  slug: opsgenie-getalertresponse
- name: GetEscalationResponse
  property_count: 3
  slug: opsgenie-getescalationresponse
- name: GetIncidentResponse
  property_count: 3
  slug: opsgenie-getincidentresponse
- name: GetIntegrationResponse
  property_count: 3
  slug: opsgenie-getintegrationresponse
- name: GetMaintenanceResponse
  property_count: 3
  slug: opsgenie-getmaintenanceresponse
- name: GetNotificationRuleResponse
  property_count: 3
  slug: opsgenie-getnotificationruleresponse
- name: GetNotificationRuleStepResponse
  property_count: 3
  slug: opsgenie-getnotificationrulestepresponse
- name: GetOnCallsResponse
  property_count: 3
  slug: opsgenie-getoncallsresponse
- name: GetOverrideResponse
  property_count: 3
  slug: opsgenie-getoverrideresponse
- name: GetRotationResponse
  property_count: 3
  slug: opsgenie-getrotationresponse
- name: GetScheduleResponse
  property_count: 3
  slug: opsgenie-getscheduleresponse
- name: GetServiceResponse
  property_count: 3
  slug: opsgenie-getserviceresponse
- name: GetTeamResponse
  property_count: 3
  slug: opsgenie-getteamresponse
- name: GetUserResponse
  property_count: 3
  slug: opsgenie-getuserresponse
- name: OpsGenie Heartbeat
  property_count: 11
  slug: opsgenie-heartbeat
- name: HeartbeatResponse
  property_count: 3
  slug: opsgenie-heartbeatresponse
- name: OpsGenie Incident
  property_count: 15
  slug: opsgenie-incident
- name: IncidentActionRequest
  property_count: 1
  slug: opsgenie-incidentactionrequest
- name: Integration
  property_count: 9
  slug: opsgenie-integration
- name: ListAlertLogsResponse
  property_count: 4
  slug: opsgenie-listalertlogsresponse
- name: ListAlertNotesResponse
  property_count: 4
  slug: opsgenie-listalertnotesresponse
- name: ListAlertRecipientsResponse
  property_count: 3
  slug: opsgenie-listalertrecipientsresponse
- name: ListAlertsResponse
  property_count: 4
  slug: opsgenie-listalertsresponse
- name: ListAttachmentsResponse
  property_count: 3
  slug: opsgenie-listattachmentsresponse
- name: ListEscalationsResponse
  property_count: 3
  slug: opsgenie-listescalationsresponse
- name: ListHeartbeatsResponse
  property_count: 3
  slug: opsgenie-listheartbeatsresponse
- name: ListIncidentsResponse
  property_count: 4
  slug: opsgenie-listincidentsresponse
- name: ListIntegrationsResponse
  property_count: 3
  slug: opsgenie-listintegrationsresponse
- name: ListMaintenancesResponse
  property_count: 3
  slug: opsgenie-listmaintenancesresponse
- name: ListNotificationRulesResponse
  property_count: 3
  slug: opsgenie-listnotificationrulesresponse
- name: ListNotificationRuleStepsResponse
  property_count: 3
  slug: opsgenie-listnotificationrulestepsresponse
- name: ListOverridesResponse
  property_count: 3
  slug: opsgenie-listoverridesresponse
- name: ListRotationsResponse
  property_count: 3
  slug: opsgenie-listrotationsresponse
- name: ListSchedulesResponse
  property_count: 4
  slug: opsgenie-listschedulesresponse
- name: ListServicesResponse
  property_count: 5
  slug: opsgenie-listservicesresponse
- name: ListTeamLogsResponse
  property_count: 4
  slug: opsgenie-listteamlogsresponse
- name: ListTeamMembersResponse
  property_count: 3
  slug: opsgenie-listteammembersresponse
- name: ListTeamsResponse
  property_count: 3
  slug: opsgenie-listteamsresponse
- name: ListUserEscalationsResponse
  property_count: 3
  slug: opsgenie-listuserescalationsresponse
- name: ListUserSchedulesResponse
  property_count: 3
  slug: opsgenie-listuserschedulesresponse
- name: ListUsersResponse
  property_count: 5
  slug: opsgenie-listusersresponse
- name: ListUserTeamsResponse
  property_count: 3
  slug: opsgenie-listuserteamsresponse
- name: Maintenance
  property_count: 5
  slug: opsgenie-maintenance
- name: NotificationCriteria
  property_count: 2
  slug: opsgenie-notificationcriteria
- name: NotificationRule
  property_count: 9
  slug: opsgenie-notificationrule
- name: NotificationRuleStep
  property_count: 4
  slug: opsgenie-notificationrulestep
- name: Paging
  property_count: 3
  slug: opsgenie-paging
- name: RequestStatusResponse
  property_count: 3
  slug: opsgenie-requeststatusresponse
- name: Responder
  property_count: 4
  slug: opsgenie-responder
- name: Rotation
  property_count: 8
  slug: opsgenie-rotation
- name: Schedule
  property_count: 7
  slug: opsgenie-schedule
- name: ScheduleTimelineResponse
  property_count: 3
  slug: opsgenie-scheduletimelineresponse
- name: Service
  property_count: 7
  slug: opsgenie-service
- name: SnoozeAlertRequest
  property_count: 4
  slug: opsgenie-snoozealertrequest
- name: SuccessResponse
  property_count: 3
  slug: opsgenie-successresponse
- name: Team
  property_count: 5
  slug: opsgenie-team
- name: TeamMember
  property_count: 2
  slug: opsgenie-teammember
- name: TimeRestriction
  property_count: 2
  slug: opsgenie-timerestriction
- name: UpdateEscalationRequest
  property_count: 5
  slug: opsgenie-updateescalationrequest
- name: UpdateHeartbeatRequest
  property_count: 8
  slug: opsgenie-updateheartbeatrequest
- name: UpdateIntegrationRequest
  property_count: 7
  slug: opsgenie-updateintegrationrequest
- name: UpdateNotificationRuleRequest
  property_count: 9
  slug: opsgenie-updatenotificationrulerequest
- name: UpdateNotificationRuleStepRequest
  property_count: 3
  slug: opsgenie-updatenotificationrulesteprequest
- name: UpdateOverrideRequest
  property_count: 4
  slug: opsgenie-updateoverriderequest
- name: UpdateRotationRequest
  property_count: 6
  slug: opsgenie-updaterotationrequest
- name: UpdateScheduleRequest
  property_count: 5
  slug: opsgenie-updateschedulerequest
- name: UpdateServiceRequest
  property_count: 4
  slug: opsgenie-updateservicerequest
- name: UpdateTeamRequest
  property_count: 3
  slug: opsgenie-updateteamrequest
- name: UpdateUserRequest
  property_count: 8
  slug: opsgenie-updateuserrequest
- name: User
  property_count: 12
  slug: opsgenie-user
json_structures:
- name: Opsgenie Structure
  property_count: 0
  slug: opsgenie-structure
jsonld:
- class_count: 0
  name: Opsgenie Context
  property_count: 10
  slug: opsgenie-context
layout: provider
modified: '2026-05-19'
name: OpsGenie
nav: Providers
network: true
overview: 'OpsGenie publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, Alerts API, Escalations API, and 12 more. Tagged areas include Alerts, Incident Management, Monitoring, On-Call, and Operations.


  The OpsGenie catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  OpsGenie''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Opsgenie Plans Pricing
  plan_count: 5
  slug: opsgenie-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Opsgenie Rate Limits
  slug: opsgenie-rate-limits
rules:
- name: OpsGenie API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: opsgenie-asyncapi-spectral-rules
- name: OpsGenie API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: opsgenie-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.0
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 77.9
    developer_ergonomics: 34.8
    discoverability: 67.5
    governance: 60.5
    operational_transparency: 36.8
  previous_composite: 60.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opsgenie/refs/heads/main/screenshots/opsgenie-2026-06-20T191103.png
security:
- kind: authentication
  name: Opsgenie Authentication
  slug: opsgenie-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opsgenie Domain Security
  slug: opsgenie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opsgenie Vulnerability Disclosure
  slug: opsgenie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opsgenie
tags:
- Alerts
- Incident Management
- Monitoring
- On-Call
- Operations
website: https://www.atlassian.com/software/opsgenie
---
