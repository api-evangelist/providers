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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cisco Webex Meetings Agentic Access
  operation_count: 14
  slug: cisco-webex-meetings-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 14
apis:
- description: The Webex Meetings API enables scheduling, updating, deleting, and listing of Webex meetings. Endpoints support recurring meetings, meeting templates, and host delegation. Authentication uses OAuth 2.
  name: Webex Meetings API
  slug: meetings-api
- description: Manage invitee lists for scheduled Webex meetings. Endpoints support adding, updating, and removing meeting invitees and bulk-inviting attendees by email.
  name: Webex Meeting Invitees API
  slug: meeting-invitees-api
- description: List and update participants in active or completed Webex meetings. Supports admin-mute, lobby admit, and participant removal operations during in-progress meetings.
  name: Webex Meeting Participants API
  slug: meeting-participants-api
- description: Manage host meeting preferences including personal room URLs, audio defaults, scheduling templates, and site preferences.
  name: Webex Meeting Preferences API
  slug: meeting-preferences-api
- description: List and manage meeting recordings. Provides access to recording details, download links, and metadata, with separate endpoints for admin and compliance officer access.
  name: Webex Recordings API
  slug: recordings-api
- description: Retrieve and manage meeting transcripts including download endpoints for VTT and TXT transcript formats. Supports compliance officer access for governance workflows.
  name: Webex Meeting Transcripts API
  slug: meeting-transcripts-api
- description: Retrieve questions and answers from Webex meetings and webinars for engagement reporting and post-event follow-up workflows.
  name: Webex Meeting Q and A API
  slug: meeting-qa-api
- description: Retrieve polls and poll responses from Webex meetings and webinars for engagement analytics and post-event reporting.
  name: Webex Meeting Polls API
  slug: meeting-polls-api
- description: Retrieve chat transcripts from completed Webex meetings for compliance and post-meeting reporting.
  name: Webex Meeting Chats API
  slug: meeting-chats-api
- description: The Webex XML API is the legacy SOAP-style interface for deep integration with Webex Meetings. It supports site administration, user provisioning, and meeting management for scenarios that pre-date th
  name: Webex XML API
  slug: webex-xml-api
- description: The Invitees API from Cisco Webex Meetings — 2 operation(s) for invitees.
  name: Cisco Webex Meetings Invitees API
  slug: cisco-webex-meetings-invitees-api
- description: The Meetings API from Cisco Webex Meetings — 2 operation(s) for meetings.
  name: Cisco Webex Meetings Meetings API
  slug: cisco-webex-meetings-meetings-api
- description: The Recordings API from Cisco Webex Meetings — 2 operation(s) for recordings.
  name: Cisco Webex Meetings Recordings API
  slug: cisco-webex-meetings-recordings-api
- description: The Transcripts API from Cisco Webex Meetings — 1 operation(s) for transcripts.
  name: Cisco Webex Meetings Transcripts API
  slug: cisco-webex-meetings-transcripts-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cisco Webex Meetings Invitees API
  slug: open-cisco-webex-meetings-invitees-api
- collection_type: open
  name: Cisco Webex Invitees Meetings API
  slug: open-cisco-webex-meetings-meetings-api
- collection_type: open
  name: Cisco Webex Meetings Invitees Recordings API
  slug: open-cisco-webex-meetings-recordings-api
- collection_type: open
  name: Cisco Webex Meetings Invitees Transcripts API
  slug: open-cisco-webex-meetings-transcripts-api
- collection_type: open
  name: Cisco Webex Meetings API
  slug: open-cisco-webex-meetings
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/webex/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-webex-meetings-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-webex-meetings-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-webex-meetings-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webex
- group: start
  title: ''
  type: Portal
  url: https://developer.webex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.webex.com/docs/meetings
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.webex.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.webex.com/docs/integrations
- group: build
  title: ''
  type: SDKs
  url: https://developer.webex.com/docs/sdks
- group: design
  title: ''
  type: Webhooks
  url: https://developer.webex.com/docs/webhooks
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.webex.com/docs/api-rate-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.webex.com/docs/api/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webex.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.webex.com/support
- group: company
  title: ''
  type: Blog
  url: https://developer.webex.com/blog
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/t5/webex-developers/bd-p/4416j-disc-dev-webex
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cisco-webex-meetings-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cisco-webex-meetings-rules.yml
created: '2024-01-01'
description: Cisco Webex Meetings is the meetings-focused subset of the Webex collaboration platform, providing scheduling, hosting, recording, transcription, and meeting administration capabilities through the Webex REST API. Authentication uses OAuth 2.0 access tokens, personal access tokens, or service apps and all endpoints respond with JSON. The legacy XML API remains available for deep integrations and enterprise scenarios that pre-date the REST surface.
finops:
- name: Cisco Webex Meetings Finops
  service_category: API
  slug: cisco-webex-meetings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-webex-meetings.png
jsonld:
- class_count: 18
  name: Cisco Webex Meetings Context
  property_count: 0
  slug: cisco-webex-meetings-context
layout: provider
modified: '2026-08-19'
name: Cisco Webex Meetings
nav: Providers
network: true
overview: 'Cisco Webex Meetings publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Invitees API, Meetings API, Recordings API, and 1 more. Tagged areas include Collaboration, Communications, Enterprise, Meetings, and Video Conferencing.


  The Cisco Webex Meetings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cisco Webex Meetings'' developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, support, engineering blog, and 14 more developer resources.'
plans:
- name: Cisco Webex Meetings Plans Pricing
  plan_count: 3
  slug: cisco-webex-meetings-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Cisco Webex Meetings Rate Limits
  slug: cisco-webex-meetings-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Cisco Webex Meetings API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: cisco-webex-meetings-rules
score:
  band: thin
  composite: 37.5
  delta: -11.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 45.5
    contract_quality: 22.0
    developer_ergonomics: 57.1
    discoverability: 64.8
    governance: 45.5
    operational_transparency: 26.3
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-webex-meetings/refs/heads/main/screenshots/cisco-webex-meetings-2026-06-20T174406.png
security:
- kind: authentication
  name: Cisco Webex Meetings Authentication
  slug: cisco-webex-meetings-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Webex Meetings Domain Security
  slug: cisco-webex-meetings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-webex-meetings
tags:
- Collaboration
- Communications
- Enterprise
- Meetings
- Video Conferencing
website: https://developer.webex.com/
---
