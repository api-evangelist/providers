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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 64.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1056
  human_in_the_loop: 204
  name: Cisco Webex Agentic Access
  operation_count: 2053
  slug: cisco-webex-agentic-access
  summary_line: 2053 operations · 1056 acting · 204 human-in-the-loop
api_count: 9
apis:
- description: The Webex Administration API — 148 operations across 115 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Administration API
  slug: admin
- description: The Webex BroadWorks API — 19 operations across 11 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex BroadWorks API
  slug: broadworks
- description: The Webex Cloud Calling API — 1087 operations across 687 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Cloud Calling API
  slug: cloud-calling
- description: The Webex Contact Center API — 448 operations across 327 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Contact Center API
  slug: contact-center
- description: The Webex Devices API — 101 operations across 67 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Devices API
  slug: device
- description: The Webex Meetings API — 168 operations across 128 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Meetings API
  slug: meeting
- description: The Webex Messaging API — 63 operations across 36 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Messaging API
  slug: messaging
- description: The Webex Unified CM API — 1 operations across 1 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Unified CM API
  slug: ucm
- description: The Webex Wholesale API — 18 operations across 10 paths, from Cisco's published OpenAPI definition.
  name: Cisco Webex Wholesale API
  slug: wholesale
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Find a person by email, add them to a team, and add them to a team room.
  name: Cisco Webex Add Person to Team and a Team Room
  slug: cisco-webex-add-person-to-team-and-team-room-workflow
- description: Create a new space, add a person to it, and post an opening message.
  name: Cisco Webex Create Room, Add Member, and Post Message
  slug: cisco-webex-create-room-add-member-post-message-workflow
- description: Create a team and a room scoped to that team, then announce it.
  name: Cisco Webex Create Team and Team Room
  slug: cisco-webex-create-team-and-team-room-workflow
- description: Add a person to a room only if they are not already a member.
  name: Cisco Webex Ensure Room Membership
  slug: cisco-webex-ensure-room-membership-workflow
- description: Look up a person by email and send them a 1:1 direct message.
  name: Cisco Webex Find Person and Send Direct Message
  slug: cisco-webex-find-person-direct-message-workflow
- description: Post a card message to a room, then submit and read an attachment action.
  name: Cisco Webex Post an Adaptive Card and Read its Attachment Action
  slug: cisco-webex-post-card-and-read-attachment-action-workflow
- description: Create an organization user, then add them to a room and welcome them.
  name: Cisco Webex Provision a Person and Add to a Room
  slug: cisco-webex-provision-person-and-add-to-room-workflow
- description: Create a room and register a messages-created webhook scoped to it.
  name: Cisco Webex Register a Messages Webhook for a Room
  slug: cisco-webex-register-messages-webhook-workflow
- description: Post a parent message to a room and then post a threaded reply to it.
  name: Cisco Webex Post a Message and Reply in Thread
  slug: cisco-webex-reply-in-thread-workflow
- description: Create a meeting and post its join link as a message into a room.
  name: Cisco Webex Schedule a Meeting and Notify a Room
  slug: cisco-webex-schedule-meeting-and-notify-room-workflow
artifact_total: 119
collections:
- collection_type: postman
  name: Cisco Webex Admin Audit Events API
  slug: postman-cisco-webex-admin-audit-events
- collection_type: postman
  name: Cisco Webex Attachment Actions API
  slug: postman-cisco-webex-attachment-actions
- collection_type: postman
  name: Cisco Webex Call Controls API
  slug: postman-cisco-webex-call-controls
- collection_type: postman
  name: Cisco Webex Converged Recordings API
  slug: postman-cisco-webex-converged-recordings
- collection_type: postman
  name: Cisco Webex Devices API
  slug: postman-cisco-webex-devices
- collection_type: postman
  name: Cisco Webex Events API
  slug: postman-cisco-webex-events
- collection_type: postman
  name: Cisco Webex Licenses API
  slug: postman-cisco-webex-licenses
- collection_type: postman
  name: Cisco Webex Meetings API
  slug: postman-cisco-webex-meetings
- collection_type: postman
  name: Cisco Webex Memberships API
  slug: postman-cisco-webex-memberships
- collection_type: postman
  name: Cisco Webex Messaging API
  slug: postman-cisco-webex-messaging
- collection_type: postman
  name: Cisco Webex Organizations API
  slug: postman-cisco-webex-organizations
- collection_type: postman
  name: Cisco Webex People API
  slug: postman-cisco-webex-people
- collection_type: postman
  name: Cisco Webex Recordings API
  slug: postman-cisco-webex-recordings
- collection_type: postman
  name: Cisco Webex Roles API
  slug: postman-cisco-webex-roles
- collection_type: postman
  name: Cisco Webex Rooms API
  slug: postman-cisco-webex-rooms
- collection_type: postman
  name: Cisco Webex Team Memberships API
  slug: postman-cisco-webex-team-memberships
- collection_type: postman
  name: Cisco Webex Teams API
  slug: postman-cisco-webex-teams
- collection_type: postman
  name: Cisco Webex Webhooks API
  slug: postman-cisco-webex-webhooks
- collection_type: postman
  name: Cisco Webex Workspaces API
  slug: postman-cisco-webex-workspaces
- collection_type: open
  name: Cisco Webex Admin Audit Events API
  slug: open-cisco-webex-admin-audit-events
- collection_type: open
  name: Cisco Webex Attachment Actions API
  slug: open-cisco-webex-attachment-actions
- collection_type: open
  name: Cisco Webex Call Controls API
  slug: open-cisco-webex-call-controls
- collection_type: open
  name: Cisco Webex Converged Recordings API
  slug: open-cisco-webex-converged-recordings
- collection_type: open
  name: Cisco Webex Devices API
  slug: open-cisco-webex-devices
- collection_type: open
  name: Cisco Webex Events API
  slug: open-cisco-webex-events
- collection_type: open
  name: Cisco Webex Licenses API
  slug: open-cisco-webex-licenses
- collection_type: open
  name: Cisco Webex Meetings API
  slug: open-cisco-webex-meetings
- collection_type: open
  name: Cisco Webex Memberships API
  slug: open-cisco-webex-memberships
- collection_type: open
  name: Cisco Webex Messaging API
  slug: open-cisco-webex-messaging
- collection_type: open
  name: Cisco Webex Organizations API
  slug: open-cisco-webex-organizations
- collection_type: open
  name: Cisco Webex People API
  slug: open-cisco-webex-people
- collection_type: open
  name: Cisco Webex Recordings API
  slug: open-cisco-webex-recordings
- collection_type: open
  name: Cisco Webex Roles API
  slug: open-cisco-webex-roles
- collection_type: open
  name: Cisco Webex Rooms API
  slug: open-cisco-webex-rooms
- collection_type: open
  name: Cisco Webex Team Memberships API
  slug: open-cisco-webex-team-memberships
- collection_type: open
  name: Cisco Webex Teams API
  slug: open-cisco-webex-teams
- collection_type: open
  name: Cisco Webex Webhooks API
  slug: open-cisco-webex-webhooks
- collection_type: open
  name: Cisco Webex Workspaces API
  slug: open-cisco-webex-workspaces
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-webex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-webex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-webex-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cisco-webex/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-add-person-to-team-and-team-room-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-create-room-add-member-post-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-create-team-and-team-room-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-ensure-room-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-find-person-direct-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-post-card-and-read-attachment-action-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-provision-person-and-add-to-room-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-register-messages-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-reply-in-thread-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-webex-schedule-meeting-and-notify-room-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/webex
- group: start
  title: ''
  type: Portal
  url: https://developer.webex.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.webex.com/docs/basics
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.webex.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.webex.com/docs/getting-started#authentication
- group: build
  title: ''
  type: SDKs
  url: https://developer.webex.com/docs/sdks
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.webex.com/docs/api/changelog
- group: company
  title: ''
  type: Blog
  url: https://developer.webex.com/blog
- group: operate
  title: ''
  type: Support
  url: https://developer.webex.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webex.com
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.webex.com/docs/api-rate-limits
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/t5/webex-developers/bd-p/4416j-disc-dev-webex
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.webex.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webex
- group: company
  title: ''
  type: Website
  url: https://www.webex.com
- group: start
  title: ''
  type: Login
  url: https://developer.webex.com/login
- group: start
  title: ''
  type: Signup
  url: https://developer.webex.com/signup
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cisco-webex-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: Spectral
  url: rules/cisco-webex-rules.yml
- group: build
  title: ''
  type: Packages
  url: packages/cisco-webex-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cisco-webex-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-webex-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cisco-webex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-webex-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-webex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-webex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-webex-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cisco-webex-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-webex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cisco-webex-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cisco-webex-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-webex-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-webex-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/cisco-webex-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-webex-data-model.yml
created: '2024-01-01'
description: Cisco Webex is a comprehensive collaboration platform that provides video conferencing, team messaging, file sharing, and calling capabilities for businesses and teams. The Webex developer platform offers REST APIs, SDKs, and integrations for extending and automating collaboration workflows across meetings, messaging, calling, devices, administration, and contact center scenarios. Authentication uses OAuth 2.0 access tokens, personal access tokens, or service apps and all endpoints are served from the webexapis.com base.
finops:
- name: Cisco Webex Finops
  service_category: Unified Communications
  slug: cisco-webex-finops
image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
json_schemas:
- name: AdminAuditEvent
  property_count: 18
  slug: cisco-webex-adminauditevent
- name: AdminRecording
  property_count: 0
  slug: cisco-webex-adminrecording
- name: AttachmentAction
  property_count: 7
  slug: cisco-webex-attachmentaction
- name: CallSession
  property_count: 10
  slug: cisco-webex-callsession
- name: ConvergedRecording
  property_count: 15
  slug: cisco-webex-convergedrecording
- name: CreateAttachmentActionRequest
  property_count: 3
  slug: cisco-webex-createattachmentactionrequest
- name: CreateDeviceRequest
  property_count: 3
  slug: cisco-webex-createdevicerequest
- name: CreateMeetingRequest
  property_count: 12
  slug: cisco-webex-createmeetingrequest
- name: CreateMembershipRequest
  property_count: 4
  slug: cisco-webex-createmembershiprequest
- name: CreateMessageRequest
  property_count: 8
  slug: cisco-webex-createmessagerequest
- name: CreatePersonRequest
  property_count: 17
  slug: cisco-webex-createpersonrequest
- name: CreateRoomRequest
  property_count: 7
  slug: cisco-webex-createroomrequest
- name: CreateTeamMembershipRequest
  property_count: 4
  slug: cisco-webex-createteammembershiprequest
- name: CreateTeamRequest
  property_count: 2
  slug: cisco-webex-createteamrequest
- name: CreateWebhookRequest
  property_count: 7
  slug: cisco-webex-createwebhookrequest
- name: CreateWorkspaceRequest
  property_count: 9
  slug: cisco-webex-createworkspacerequest
- name: Cisco Webex Device
  property_count: 22
  slug: cisco-webex-device
- name: DeviceActivation
  property_count: 3
  slug: cisco-webex-deviceactivation
- name: EditMessageRequest
  property_count: 3
  slug: cisco-webex-editmessagerequest
- name: Cisco Webex Event
  property_count: 8
  slug: cisco-webex-event
- name: Cisco Webex License
  property_count: 9
  slug: cisco-webex-license
- name: LicenseAssignment
  property_count: 5
  slug: cisco-webex-licenseassignment
- name: LicenseDetail
  property_count: 0
  slug: cisco-webex-licensedetail
- name: Cisco Webex Meeting
  property_count: 19
  slug: cisco-webex-meeting
- name: Cisco Webex Membership
  property_count: 11
  slug: cisco-webex-membership
- name: Cisco Webex Message
  property_count: 16
  slug: cisco-webex-message
- name: Cisco Webex Organization
  property_count: 3
  slug: cisco-webex-organization
- name: Cisco Webex Person
  property_count: 28
  slug: cisco-webex-person
- name: Cisco Webex Recording
  property_count: 14
  slug: cisco-webex-recording
- name: Registrant
  property_count: 8
  slug: cisco-webex-registrant
- name: RegistrantInput
  property_count: 11
  slug: cisco-webex-registrantinput
- name: Role
  property_count: 2
  slug: cisco-webex-role
- name: Cisco Webex Room
  property_count: 15
  slug: cisco-webex-room
- name: RoomMeetingInfo
  property_count: 7
  slug: cisco-webex-roommeetinginfo
- name: Cisco Webex Team
  property_count: 5
  slug: cisco-webex-team
- name: TeamMembership
  property_count: 8
  slug: cisco-webex-teammembership
- name: UpdateDeviceRequest
  property_count: 3
  slug: cisco-webex-updatedevicerequest
- name: UpdateMeetingRequest
  property_count: 9
  slug: cisco-webex-updatemeetingrequest
- name: UpdateMembershipRequest
  property_count: 2
  slug: cisco-webex-updatemembershiprequest
- name: UpdatePersonRequest
  property_count: 17
  slug: cisco-webex-updatepersonrequest
- name: UpdateRoomRequest
  property_count: 8
  slug: cisco-webex-updateroomrequest
- name: UpdateTeamMembershipRequest
  property_count: 1
  slug: cisco-webex-updateteammembershiprequest
- name: UpdateTeamRequest
  property_count: 2
  slug: cisco-webex-updateteamrequest
- name: UpdateWebhookRequest
  property_count: 5
  slug: cisco-webex-updatewebhookrequest
- name: UpdateWorkspaceRequest
  property_count: 8
  slug: cisco-webex-updateworkspacerequest
- name: Cisco Webex Webhook
  property_count: 13
  slug: cisco-webex-webhook
- name: Cisco Webex Workspace
  property_count: 13
  slug: cisco-webex-workspace
json_structures:
- name: Cisco Webex Structure
  property_count: 0
  slug: cisco-webex-structure
jsonld:
- class_count: 0
  name: Cisco Webex Context
  property_count: 14
  slug: cisco-webex-context
layout: provider
mcp_servers:
- description: ''
  name: cisco-webex-mcp.yml
  slug: cisco-webex-mcpyml
modified: '2026-07-31'
name: Cisco Webex
nav: Providers
network: true
overview: 'Cisco Webex publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Administration API, BroadWorks API, Cloud Calling API, and 6 more. Tagged areas include Collaboration, Communications, Meetings, Messaging, and Teams.


  The Cisco Webex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cisco Webex''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, support, and 44 more developer resources.'
plans:
- name: Cisco Webex Plans Pricing
  plan_count: 4
  slug: cisco-webex-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 3
  name: Cisco Webex Rate Limits
  slug: cisco-webex-rate-limits
rules:
- name: Cisco Webex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cisco-webex-jsonschema-spectral-rules
- name: Cisco Webex API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: cisco-webex-rules
scopes:
- name: Cisco Webex Scopes
  scope_count: 30
  slug: cisco-webex-scopes
  summary_line: 30 scopes
score:
  band: exemplar
  composite: 71.8
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 57.4
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 71.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/screenshots/cisco-webex-2026-06-20T174405.png
security:
- kind: authentication
  name: Cisco Webex Authentication
  slug: cisco-webex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Webex Domain Security
  slug: cisco-webex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Webex Vulnerability Disclosure
  slug: cisco-webex-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cisco Webex Trust Center
  slug: cisco-webex-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, FedRAMP (Moderate — Webex for Government), HIPAA, GDPR, C5 (Germany), CSA STAR (Level 1 and 2), Cyber Essentials (UK), DISA IL5
slug: cisco-webex
tags:
- Collaboration
- Communications
- Meetings
- Messaging
- Teams
- Video Conferencing
website: https://www.webex.com
---
