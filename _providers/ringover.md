---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 103
  human_in_the_loop: 2
  name: Ringover Agentic Access
  operation_count: 176
  slug: ringover-agentic-access
  summary_line: 176 operations · 103 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage blacklisted phone numbers. There are two levels of blacklist: - **Team blacklist** (`/blacklists/numbers`): Blocks numbers for the entire team. Requires `Numbers R/W` + Monitoring ON. - **User '
  name: Ringover Blacklist API
  slug: ringover-blacklist-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Initiate phone calls between a Ringover user and an external recipient. The system calls the user first on their chosen device, then connects them to the recipient. **Permissions required:** `Calls Wr
  name: Ringover Callbacks API
  slug: ringover-callbacks-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Manage your Ringover call history. Retrieve terminated and current calls, apply filters (by date, type, tags, users, IVRs…), archive calls, and access survey results. **Permissions required:** - **Rea
  name: Ringover Calls API
  slug: ringover-calls-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage your outbound call campaigns (Call Lists). This section provides a comprehensive overview of how to manage your campaign workflows: - Retrieve the list of campaigns, filterable by various param'
  name: Ringover Campaigns API
  slug: ringover-campaigns-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Private CDN URLs (`transcription_url`, `recap_url`, `audio_url`, `video_url`, and other Ringover CDN download links) cannot be opened with a public API token. Use `POST /cdn/download` to proxy the fil
  name: Ringover Cdn API
  slug: ringover-cdn-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Control live calls in real time. A channel represents an audio stream during a call. You can mute, hold, record, hangup, transfer, or send DTMF tones on active channels. **Permissions required:** `Cal
  name: Ringover Channels API
  slug: ringover-channels-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Manage conference rooms. List conferences and update access PIN codes. **Permissions required:** No specific permission category, but **Monitoring must be ON** for all conference routes. Returns `401`
  name: Ringover Conferences API
  slug: ringover-conferences-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage your Ringover contacts. Full CRUD operations on contacts and their phone numbers. **Permissions required:** - **Read** (`Contacts R`): List and get contacts. - **Write** (`Contacts W`): Create,'
  name: Ringover Contacts API
  slug: ringover-contacts-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage SMS and Chat conversations. List conversations and their messages, archive/unarchive, rename, and manage conversation metadata. **Permissions required:** - **Read** (`Conversations R`): List co'
  name: Ringover Conversations API
  slug: ringover-conversations-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Access Ringover [Empower](https://www.ringover.com/sales-enablement-tool) AI features: call transcriptions, AI-generated summaries, key moments detection, mood analysis, and analytics. CDN URLs on a c'
  name: Ringover Empower API
  slug: ringover-empower-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage your Ringover groups. Groups organize users for call distribution (ring groups). You can list groups, manage members, configure ring duration, and toggle free access. **Permissions required:** '
  name: Ringover Groups API
  slug: ringover-groups-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Retrieve your IVRs (Interactive Voice Response) and their scenarios. IVRs are the automated call routing systems configured on your Ringover account. **Permissions required:** - **Read** (`IVRs R`): L'
  name: Ringover Ivrs API
  slug: ringover-ivrs-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: '## Model Context Protocol The MCP endpoint exposes a **curated** set of Ringover operations to AI assistants (Claude, ChatGPT, Cursor, etc.) via the [Model Context Protocol](https://modelcontextprotoc'
  name: Ringover MCP API
  slug: ringover-mcp-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage messages within conversations. List messages, archive and unarchive individual messages. **Permissions required:** - **Read** (`Conversations R`): List messages in a conversation. - **Write** ('
  name: Ringover Messages API
  slug: ringover-messages-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Retrieve information about phone numbers assigned to your Ringover account. **Permissions required:** - **Read** (`Numbers R`): List and get number details. - **Write** (`Numbers W`): Manage team blac'
  name: Ringover Numbers API
  slug: ringover-numbers-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Retrieve real-time presence information about users: planning status, snooze status, connected device, and whether they are currently in a call. **Permissions required:** - `Users Read` for individual'
  name: Ringover Presences API
  slug: ringover-presences-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Retrieve user profiles defined on your Ringover account. Each profile has an ID and a name. **Permissions required:** `Users Read` required. **Monitoring impact:** None — profiles are team-wide and al
  name: Ringover Profiles API
  slug: ringover-profiles-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Ringover exposes a **SCIM 2.0** server (RFC 7643 / RFC 7644) so your identity provider (Okta, Microsoft Entra ID, OneLogin, …) can automatically provision, update and deprovision Ringover users and gr
  name: Ringover SCIM API
  slug: ringover-scim-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Send SMS messages to phone numbers. Phone numbers must be in E.164 format. **Permissions required:** `Conversations Write` required. **Monitoring impact:** - *OFF*: You can send SMS from your own numb'
  name: Ringover Sms API
  slug: ringover-sms-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Retrieve the list of available snooze statuses and manage user snooze settings. Snooze temporarily changes a user's availability status. **Permissions required:** - No specific permission to list snoo
  name: Ringover Snoozes API
  slug: ringover-snoozes-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Retrieve survey answers associated with calls. Surveys are customer satisfaction questionnaires triggered after calls. **Permissions required:** `Calls Read` required. **Monitoring impact:** None — su
  name: Ringover Surveys API
  slug: ringover-surveys-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Manage call tags. Tags are labels you can assign to calls for categorization and reporting. Each tag has an ID, name, color, description, and creation date. **Permissions required:** - **Read** (`IVRs
  name: Ringover Tags API
  slug: ringover-tags-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Manage team tasks. Create, list, and manage tasks associated with your team. **Permissions:** No specific permission required. A valid API key is sufficient.
  name: Ringover Task API
  slug: ringover-task-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'The team object is a model of your Ringover team. It contains a list of related objects: - `numbers` and related information such as their type, country and prefix according to the country, - `users` '
  name: Ringover Teams API
  slug: ringover-teams-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Retrieve call transcriptions. Access is controlled by a team-level setting — your team must have the transcription feature enabled. **Permissions required:** Transcription access is based on a team-le
  name: Ringover Transcriptions API
  slug: ringover-transcriptions-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Manage your Ringover team members. Retrieve user information, manage plannings, check availability (presences/snooze), and organize user blacklists. **Permissions required:** - **Read** (`Users R`): G'
  name: Ringover Users API
  slug: ringover-users-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: 'Ringover uses webhooks to notify you any time that an event associated with your team occurs (ex: a new voicemail, the reception of a new message, a missed call...). A webhook is a URL that we call wi'
  name: Ringover Webhook API
  slug: ringover-webhook-api
- baseURL: https://public-api.ringover.com/v2
  baseurl_source: declared
  description: Manage WhatsApp Business messaging. Send template messages, manage templates, and handle WhatsApp conversations. **Permissions:** No specific permission required. A valid API key is sufficient.
  name: Ringover WhatsApp API
  slug: ringover-whatsapp-api
artifact_total: 47
asyncapis:
- description: ''
  name: Ringover Webhooks
  slug: ringover-webhooks
common:
- group: other
  href: https://artifacts.apis.io/ringover/capabilities/ringover-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ringover-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ringover/agentic-access/ringover-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ringover-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/ringover/rate-limits/ringover-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ringover-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ringover/plans/ringover-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ringover-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ringover/rules/ringover-rules.yml
  title: ''
  type: Spectral
  url: rules/ringover-rules.yml
- group: design
  href: https://artifacts.apis.io/ringover/json-ld/ringover-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ringover-context.jsonld
- group: design
  href: https://artifacts.apis.io/ringover/vocabulary/ringover-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ringover-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ringover/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ringover/asyncapi/ringover-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ringover-webhooks.yml
- group: design
  href: https://artifacts.apis.io/ringover/data-model/ringover-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ringover-data-model.yml
- group: design
  href: https://artifacts.apis.io/ringover/conventions/ringover-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ringover-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ringover/authentication/ringover-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ringover-authentication.yml
- group: design
  href: https://artifacts.apis.io/ringover/lifecycle/ringover-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ringover-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ringover/errors/ringover-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ringover-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ringover/conformance/ringover-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ringover-conformance.yml
- group: other
  href: https://artifacts.apis.io/ringover/overlays/ringover-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ringover-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ringover/llms/ringover-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ringover-llms.txt
- group: agent
  href: https://artifacts.apis.io/ringover/well-known/ringover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ringover-well-known.yml
- group: other
  href: https://artifacts.apis.io/ringover/hosts/ringover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ringover-hosts.yml
- group: other
  href: https://artifacts.apis.io/ringover/vendors/ringover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ringover-vendors.yml
- group: build
  href: https://artifacts.apis.io/ringover/packages/ringover-packages.yml
  title: ''
  type: SDKs
  url: packages/ringover-packages.yml
- group: build
  href: https://artifacts.apis.io/ringover/packages/ringover-packages.yml
  title: ''
  type: Packages
  url: packages/ringover-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.ringover.com/webhooks
- group: auth
  title: ''
  type: Security
  url: https://www.ringover.com/security
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ringover.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ringover
- group: auth
  href: https://artifacts.apis.io/ringover/security/ringover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ringover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ringover.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ringover.com/features
- group: operate
  title: ''
  type: Support
  url: https://www.ringover.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.ringover.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ringover.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.ringover.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ringover.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ringover.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ringover.com/status
created: '2026-10-28'
description: Ringover provides a cloud‑based business phone system that unifies voice calling, messaging, and collaboration tools into a single platform. It offers features such as AI‑enhanced call handling, virtual numbers, call routing, analytics, and integrations with CRM and productivity applications, targeting enterprises and remote teams. The service is delivered via a web app and mobile apps, with a focus on scalability, security, and AI‑driven assistance for agents.
image: https://www.ringover.com/favicon.ico
json_schemas:
- name: callEmpower
  property_count: 31
  slug: ringover-call-empower
- name: calls_filter
  property_count: 22
  slug: ringover-calls-filter
- name: conversation_light
  property_count: 22
  slug: ringover-conversation-light
- name: empowerLogsCallsRequest
  property_count: 36
  slug: ringover-empower-logs-calls-request
- name: empowerLogsCallsResponse
  property_count: 6
  slug: ringover-empower-logs-calls-response
- name: getCallEmpowerResBody
  property_count: 30
  slug: ringover-get-call-empower-res-body
jsonld:
- class_count: 120
  name: Ringover Context
  property_count: 370
  slug: ringover-context
layout: provider
modified: '2026-10-28'
name: Ringover
nav: Providers
network: true
overview: 'Ringover publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Blacklist API, Callbacks API, Calls API, and 25 more. Tagged areas include Communications, Cloud, VoIP, Collaboration, and Artificial Intelligence.


  The Ringover catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ringover''s developer surface includes authentication, API reference, documentation, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Ringover Plans Pricing
  plan_count: 4
  slug: ringover-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Ringover Rate Limits
  slug: ringover-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Ringover API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: ringover-rules
scopes:
- name: Ringover Scopes
  scope_count: 0
  slug: ringover-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 37
    catalog_earned: 76.8
    catalog_earned_first_party: 12.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 73.0
    developer_ergonomics: 37.4
    discoverability: 73.2
    operational_transparency: 25.0
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/ringover/ringover-2026-11-03T142315.png
security:
- kind: authentication
  name: Ringover Authentication
  slug: ringover-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ringover Domain Security
  slug: ringover-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: create-contact
  slug: ringover-create-contact
- name: get-teams
  slug: ringover-get-teams
- name: list-users
  slug: ringover-list-users
- name: make-call
  slug: ringover-make-call
slug: ringover
tags:
- Communications
- Cloud
- VoIP
- Collaboration
- Artificial Intelligence
website: https://ringover.com/
---
