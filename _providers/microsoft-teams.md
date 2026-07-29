---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Microsoft Teams Agentic Access
  operation_count: 24
  slug: microsoft-teams-agentic-access
  summary_line: 24 operations · 15 acting
api_count: 11
apis:
- description: API for building conversational bots that interact with users in Microsoft Teams through the Bot Framework.
  name: Microsoft Teams Bot Framework API
  slug: microsoft-teams-bot-framework-api
- description: APIs for creating incoming webhooks and Office 365 connectors to post messages and notifications to Teams channels.
  name: Microsoft Teams Webhook and Connector API
  slug: microsoft-teams-webhook-and-connector-api
- description: APIs for building calling and meeting experiences in Teams including VoIP calls, group calls, IVR flows, and online meetings.
  name: Microsoft Teams Real-Time Communication APIs
  slug: microsoft-teams-real-time-communication-apis
- description: Operations for managing app installations in teams.
  name: Microsoft Teams Apps API
  slug: microsoft-teams-apps-api
- description: Operations for initiating and managing calls.
  name: Microsoft Teams Calls API
  slug: microsoft-teams-calls-api
- description: Operations for managing channels within teams.
  name: Microsoft Teams Channels API
  slug: microsoft-teams-channels-api
- description: Operations for managing team and channel members.
  name: Microsoft Teams Members API
  slug: microsoft-teams-members-api
- description: Operations for sending and receiving chat messages.
  name: Microsoft Teams Messages API
  slug: microsoft-teams-messages-api
- description: Operations for creating and managing online meetings.
  name: Microsoft Teams Online Meetings API
  slug: microsoft-teams-online-meetings-api
- description: Operations for managing tabs in channels.
  name: Microsoft Teams Tabs API
  slug: microsoft-teams-tabs-api
- description: Operations for managing teams.
  name: Microsoft Teams Teams API
  slug: microsoft-teams-teams-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Add a member to a team and post a welcome message to a chosen channel.
  name: Microsoft Teams Add Member and Welcome
  slug: microsoft-teams-add-member-and-welcome-workflow
- description: Confirm a team is active and then archive it, making it read-only.
  name: Microsoft Teams Archive Team
  slug: microsoft-teams-archive-team-workflow
- description: Resolve a team and enumerate its channels for an inventory snapshot.
  name: Microsoft Teams Audit Team Channels
  slug: microsoft-teams-audit-team-channels-workflow
- description: Pick one of the current user's joined teams, find a channel, and post to it.
  name: Microsoft Teams Broadcast to Joined Team Channel
  slug: microsoft-teams-broadcast-to-joined-team-channel-workflow
- description: Create a new Microsoft Teams team and capture the provisioning operation location.
  name: Microsoft Teams Create Team
  slug: microsoft-teams-create-team-workflow
- description: List a team's channels and enumerate the tabs in a chosen channel.
  name: Microsoft Teams Discover Channel Tabs
  slug: microsoft-teams-discover-channel-tabs-workflow
- description: Snapshot a team's members, channels, and installed apps in one pass.
  name: Microsoft Teams Inventory Team Collaboration
  slug: microsoft-teams-inventory-team-collaboration-workflow
- description: Find a member by user id in a team and remove their membership.
  name: Microsoft Teams Offboard Team Member
  slug: microsoft-teams-offboard-team-member-workflow
- description: Add a user to a team and then promote them to owner.
  name: Microsoft Teams Onboard Team Member
  slug: microsoft-teams-onboard-team-member-workflow
- description: Find a channel by name in a team and post an announcement message to it.
  name: Microsoft Teams Post Channel Announcement
  slug: microsoft-teams-post-channel-announcement-workflow
- description: List a team's members and promote an existing membership to owner.
  name: Microsoft Teams Promote Team Member
  slug: microsoft-teams-promote-team-member-workflow
- description: Confirm a team, create a channel in it, and post an opening message.
  name: Microsoft Teams Provision Channel
  slug: microsoft-teams-provision-channel-workflow
- description: Read a team and update its display name and description.
  name: Microsoft Teams Rename Team
  slug: microsoft-teams-rename-team-workflow
- description: List a team's channels and read the recent messages in a chosen channel.
  name: Microsoft Teams Review Channel Conversation
  slug: microsoft-teams-review-channel-conversation-workflow
artifact_total: 106
asyncapis:
- description: 'AsyncAPI 2.6 description of the asynchronous event surface for Microsoft Teams. Two distinct delivery channels are modeled: 1. Microsoft Graph change notifications - HTTPS webhook deliveries that Micr'
  name: Microsoft Teams Event Surface
  slug: microsoft-teams-asyncapi
collections:
- collection_type: postman
  name: Microsoft Graph Teams API
  slug: postman-microsoft-teams-graph-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-teams-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-teams-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-teams-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-teams-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-teams-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-teams-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-teams-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-teams-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-teams-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-teams-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-teams-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-teams-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-teams-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-teams-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-teams-cli.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-teams-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-teams-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-teams/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-add-member-and-welcome-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-archive-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-audit-team-channels-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-broadcast-to-joined-team-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-create-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-discover-channel-tabs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-inventory-team-collaboration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-offboard-team-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-onboard-team-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-post-channel-announcement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-promote-team-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-provision-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-rename-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-teams-review-channel-conversation-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft_teams
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-teams
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/microsoftteams/platform/get-started/get-started-overview
- group: build
  title: Teams Toolkit
  type: SDKs
  url: https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-teams-blog/bg-p/MicrosoftTeamsBlog
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/products/office-teams
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev/Microsoft-Teams-Samples
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teams.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-teams-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-teams-vocabulary.yaml
created: '2024'
description: Microsoft Teams is a collaboration platform that combines workplace chat, meetings, file storage, and application integration. It provides APIs for building custom integrations, managing teams and channels, sending messages, scheduling meetings, and initiating calls through Microsoft Graph.
examples:
- key_count: 6
  name: Microsoft Teams Addteammember Example
  slug: microsoft-teams-addteammember-example
- key_count: 6
  name: Microsoft Teams Createcall Example
  slug: microsoft-teams-createcall-example
- key_count: 6
  name: Microsoft Teams Createchannel Example
  slug: microsoft-teams-createchannel-example
- key_count: 6
  name: Microsoft Teams Createonlinemeeting Example
  slug: microsoft-teams-createonlinemeeting-example
- key_count: 6
  name: Microsoft Teams Createteam Example
  slug: microsoft-teams-createteam-example
- key_count: 6
  name: Microsoft Teams Getteam Example
  slug: microsoft-teams-getteam-example
- key_count: 6
  name: Microsoft Teams Listchannelmessages Example
  slug: microsoft-teams-listchannelmessages-example
- key_count: 6
  name: Microsoft Teams Listchannels Example
  slug: microsoft-teams-listchannels-example
- key_count: 6
  name: Microsoft Teams Listchanneltabs Example
  slug: microsoft-teams-listchanneltabs-example
- key_count: 6
  name: Microsoft Teams Listjoinedteams Example
  slug: microsoft-teams-listjoinedteams-example
- key_count: 6
  name: Microsoft Teams Listteammembers Example
  slug: microsoft-teams-listteammembers-example
- key_count: 6
  name: Microsoft Teams Sendchannelmessage Example
  slug: microsoft-teams-sendchannelmessage-example
- key_count: 6
  name: Microsoft Teams Updateteam Example
  slug: microsoft-teams-updateteam-example
- key_count: 6
  name: Microsoft Teams Updateteammember Example
  slug: microsoft-teams-updateteammember-example
- key_count: 6
  name: Teams Graph Api Call Example
  slug: teams-graph-api-call-example
- key_count: 6
  name: Teams Graph Api Channel Example
  slug: teams-graph-api-channel-example
- key_count: 8
  name: Teams Graph Api Chat Message Example
  slug: teams-graph-api-chat-message-example
- key_count: 5
  name: Teams Graph Api Conversation Member Example
  slug: teams-graph-api-conversation-member-example
- key_count: 5
  name: Teams Graph Api Online Meeting Example
  slug: teams-graph-api-online-meeting-example
- key_count: 7
  name: Teams Graph Api Team Example
  slug: teams-graph-api-team-example
features:
- 'Microsoft Teams: hundreds of services across Collaboration'
- 'Detailed pricing: see https://www.microsoft.com/en-us/microsoft-teams/compare-microsoft-teams-options'
- 'Service: Microsoft Graph - Teams API'
- 'Service: Bot Framework'
- 'Service: Adaptive Cards'
- 'Service: Teams Toolkit'
- 'Service: Teams Meeting API'
- 'Service: Teams Webhook API'
- 'Service: Teams Communication Services'
- 'Service: PSTN Calling'
- 'Service: Teams Phone'
finops:
- name: Microsoft Teams Finops
  service_category: Collaboration
  slug: microsoft-teams-finops
graphqls:
- description: This GraphQL schema provides a conceptual representation of the Microsoft Teams API surface exposed through Microsoft Graph. It maps the core Teams resources — teams, channels, messages, meetings, cal
  name: Microsoft Teams GraphQL Schema
  slug: microsoft-teams-graphql
image: https://learn.microsoft.com/en-us/graph/images/teams-logo.png
json_schemas:
- name: AppInstallationCollection
  property_count: 1
  slug: microsoft-teams-appinstallationcollection
- name: Call
  property_count: 6
  slug: microsoft-teams-call
- name: Channel
  property_count: 6
  slug: microsoft-teams-channel
- name: ChannelCollection
  property_count: 1
  slug: microsoft-teams-channelcollection
- name: ChatMessage
  property_count: 8
  slug: microsoft-teams-chatmessage
- name: ChatMessageCollection
  property_count: 1
  slug: microsoft-teams-chatmessagecollection
- name: ConversationMember
  property_count: 5
  slug: microsoft-teams-conversationmember
- name: ErrorResponse
  property_count: 1
  slug: microsoft-teams-errorresponse
- name: MemberCollection
  property_count: 1
  slug: microsoft-teams-membercollection
- name: OnlineMeeting
  property_count: 6
  slug: microsoft-teams-onlinemeeting
- name: TabCollection
  property_count: 1
  slug: microsoft-teams-tabcollection
- name: Team
  property_count: 7
  slug: microsoft-teams-team
- name: TeamCollection
  property_count: 1
  slug: microsoft-teams-teamcollection
- name: TeamsAppInstallation
  property_count: 2
  slug: microsoft-teams-teamsappinstallation
- name: TeamsTab
  property_count: 4
  slug: microsoft-teams-teamstab
- name: Call
  property_count: 6
  slug: teams-graph-api-call
- name: Channel
  property_count: 6
  slug: teams-graph-api-channel
- name: ChatMessage
  property_count: 8
  slug: teams-graph-api-chat-message
- name: ConversationMember
  property_count: 5
  slug: teams-graph-api-conversation-member
- name: OnlineMeeting
  property_count: 5
  slug: teams-graph-api-online-meeting
- name: Team
  property_count: 7
  slug: teams-graph-api-team
json_structures:
- name: Microsoft Teams Structure
  property_count: 0
  slug: microsoft-teams-structure
- name: Teams Graph Api Call Structure
  property_count: 6
  slug: teams-graph-api-call-structure
- name: Teams Graph Api Channel Structure
  property_count: 6
  slug: teams-graph-api-channel-structure
- name: Teams Graph Api Chat Message Structure
  property_count: 8
  slug: teams-graph-api-chat-message-structure
- name: Teams Graph Api Conversation Member Structure
  property_count: 5
  slug: teams-graph-api-conversation-member-structure
- name: Teams Graph Api Online Meeting Structure
  property_count: 5
  slug: teams-graph-api-online-meeting-structure
- name: Teams Graph Api Team Structure
  property_count: 7
  slug: teams-graph-api-team-structure
jsonld:
- class_count: 9
  name: Microsoft Teams Graph Api Context
  property_count: 22
  slug: microsoft-teams-graph-api-context
layout: provider
modified: '2026-06-20'
name: Microsoft Teams
nav: Providers
network: true
overview: 'Microsoft Teams publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bot Framework API, Apps API, Calls API, and 6 more. Tagged areas include Chat, Collaboration, Communication, Microsoft 365, and Productivity.


  The Microsoft Teams catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Microsoft Teams'' developer surface includes authentication, changelog, CLI, sandbox, getting-started guide, engineering blog, support, and 37 more developer resources.'
plans:
- name: Microsoft Teams Plans Pricing
  plan_count: 3
  slug: microsoft-teams-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 2
  name: Microsoft Teams Rate Limits
  slug: microsoft-teams-rate-limits
rules:
- name: Microsoft Teams API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: microsoft-teams-asyncapi-spectral-rules
- name: Microsoft Teams API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-teams-jsonschema-spectral-rules
- name: Microsoft Teams API Rules
  rule_count: 28
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 11
  slug: microsoft-teams-spectral-rules
scopes:
- name: Microsoft Teams Scopes
  scope_count: 10
  slug: microsoft-teams-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.2
  delta: -3.2
  facets:
    commercial_clarity: 68.4
    contract_quality: 76.6
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 69.8
    operational_transparency: 57.9
  previous_composite: 73.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Microsoft Teams Authentication
  slug: microsoft-teams-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Teams Domain Security
  slug: microsoft-teams-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Teams Vulnerability Disclosure
  slug: microsoft-teams-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Teams Trust Center
  slug: microsoft-teams-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, FedRAMP, HIPAA / HITECH, PCI DSS, CSA STAR, GDPR
slug: microsoft-teams
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
use_cases:
- description: Automate creation and configuration of teams for projects.
  name: Team Provisioning
- description: Send automated notifications and updates to channels.
  name: Messaging Automation
- description: Programmatically create and manage online meetings.
  name: Meeting Scheduling
- description: Build conversational bots for customer support in Teams.
  name: Customer Service Bots
- description: Manage shifts and schedules for frontline workers.
  name: Workforce Management
website: https://developer.microsoft.com/en-us/microsoft-teams
---
