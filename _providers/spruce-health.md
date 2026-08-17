---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 65.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Spruce Health Agentic Access
  operation_count: 47
  slug: spruce-health-agentic-access
  summary_line: 47 operations · 22 acting
api_count: 15
apis:
- description: Organization contact fields — the custom fields that appear on every contact in the organization.
  name: Spruce Health Contact Fields API
  slug: spruce-health-contact-fields
- description: Contact tags — the tags available to an organization that can be applied to contacts.
  name: Spruce Health Contact Tags API
  slug: spruce-health-contact-tags
- description: 'Contacts — the patients and other parties in a Spruce organization: list, search, create, retrieve, update and delete contacts, list a contact''s conversations, manage integration links to external EHR'
  name: Spruce Health Contacts API
  slug: spruce-health-contacts
- description: 'Conversation items — the individual messages, calls, faxes and events inside a conversation: retrieve one by id, or soft-delete it asynchronously.'
  name: Spruce Health Conversation Item API
  slug: spruce-health-conversation-item
- description: Conversation tags — the tags available to an organization that can be applied to conversations.
  name: Spruce Health Conversation Tags API
  slug: spruce-health-conversation-tags
- description: 'Conversations — the message threads in an organization: list and filter conversations with cursor pagination and ordering by created or last_message, create secure and note conversations, retrieve and'
  name: Spruce Health Conversations API
  slug: spruce-health-conversations
- description: 'Internal endpoints — the Spruce phone numbers, fax numbers, email addresses and Spruce Links an organization communicates from: list them, send a secure/SMS/email/fax message from one, and create an o'
  name: Spruce Health Internal Endpoints API
  slug: spruce-health-internal-endpoints
- description: Media — upload images, video and files to Spruce and receive a media ID that can be attached to messages.
  name: Spruce Health Media API
  slug: spruce-health-media
- description: Organization — read the organization record and its members (teammates, teams and the organization entity itself).
  name: Spruce Health Organization API
  slug: spruce-health-organization
- description: Phone lines — list the organization's phone lines and retrieve one by id.
  name: Spruce Health Phone Lines API
  slug: spruce-health-phone-lines
- description: Saved messages — the reusable private and organization-wide message templates available to the organization.
  name: Spruce Health Saved Messages API
  slug: spruce-health-saved-messages
- description: 'Scheduled messages — messages queued to send at a future time, organization-wide or within a single conversation: list, schedule and delete.'
  name: Spruce Health Scheduled Messages API
  slug: spruce-health-scheduled-messages
- description: Teams — list the members of a team by team id.
  name: Spruce Health Teams API
  slug: spruce-health-teams
- description: Transcriptions — retrieve the full transcription text and AI summarization for a transcription id found on voicemails, call recordings and audio messages.
  name: Spruce Health Transcription API
  slug: spruce-health-transcription
- description: Webhooks — register and manage the HTTPS destination endpoints that receive real-time contact, conversation, conversationItem and scheduledMessage events; create (returns the signing secret), list, re
  name: Spruce Health Webhooks API
  slug: spruce-health-webhooks
artifact_total: 39
asyncapis:
- description: ''
  name: Spruce Health Webhooks
  slug: spruce-health-webhooks
collections:
- collection_type: open
  name: Spruce Health API — Contact Fields
  slug: open-spruce-health-contact-fields
- collection_type: open
  name: Spruce Health API — Contact Tags
  slug: open-spruce-health-contact-tags
- collection_type: open
  name: Spruce Health API — Contacts
  slug: open-spruce-health-contacts
- collection_type: open
  name: Spruce Health API — Conversation Item
  slug: open-spruce-health-conversation-item
- collection_type: open
  name: Spruce Health API — Conversation Tags
  slug: open-spruce-health-conversation-tags
- collection_type: open
  name: Spruce Health API — Conversations
  slug: open-spruce-health-conversations
- collection_type: open
  name: Spruce Health API — Internal Endpoints
  slug: open-spruce-health-internal-endpoints
- collection_type: open
  name: Spruce Health API — Media
  slug: open-spruce-health-media
- collection_type: open
  name: Spruce Health API — Organization
  slug: open-spruce-health-organization
- collection_type: open
  name: Spruce Health API — Phone Lines
  slug: open-spruce-health-phone-lines
- collection_type: open
  name: Spruce Health API — Saved Messages
  slug: open-spruce-health-saved-messages
- collection_type: open
  name: Spruce Health API — Scheduled Messages
  slug: open-spruce-health-scheduled-messages
- collection_type: open
  name: Spruce Health API — Teams
  slug: open-spruce-health-teams
- collection_type: open
  name: Spruce Health API — Transcription
  slug: open-spruce-health-transcription
- collection_type: open
  name: Spruce Health API — Webhooks
  slug: open-spruce-health-webhooks
- collection_type: open
  name: Spruce Health API
  slug: open-spruce-health
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spruce-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spruce-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spruce-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sprucehealth.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spruce-health
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sprucehealth.com/docs/overview
- group: start
  title: ''
  type: SignUp
  url: https://app.sprucehealth.com/signup
- group: commercial
  title: ''
  type: Plans
  url: plans/spruce-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spruce-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spruce-health-finops.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spruce-health-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/spruce-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spruce-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spruce-health-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sprucehealth.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spruce-health-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spruce-health-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spruce-health-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spruce-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/spruce-health-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/spruce-health-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spruce-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/spruce-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spruce-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sprucehealth.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sprucehealth.com/reference/listcontacts
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sprucehealth.com/docs/overview
- group: operate
  title: ''
  type: Support
  url: https://help.sprucehealth.com/hc/en-us/articles/23003282513435-Spruce-Support
- group: company
  title: ''
  type: Blog
  url: https://sprucehealth.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sprucehealth
- group: commercial
  title: ''
  type: Pricing
  url: https://sprucehealth.com/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sprucehealth.com/terms-organizations/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sprucehealth.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://sprucehealth.com/whats-new
- group: company
  title: ''
  type: BlogRSS
  url: https://sprucehealth.com/whats-new/rss.xml
created: '2026-07-10'
description: 'Spruce Health is a HIPAA-compliant healthcare communication platform that unifies phone, SMS, secure messaging, video, e-fax, team chat, mobile payments and VoIP phone lines into one system for medical practices, with AI-enabled voicemail transcription, summarization and call routing. Every eligible organization receives a signed HIPAA Business Associate Agreement as part of the terms of service, and since July 2026 that BAA also carries formal Qualified Service Organization support for 42 CFR Part 2. Spruce is SOC 2 Type II audited annually. The Spruce Public API is a RESTful, Bearer-token interface at https://api.sprucehealth.com/v1 spanning 47 operations across contacts, conversations, conversation items, internal endpoints and phone lines, media, organization members and teams, saved and scheduled messages, AI transcriptions, and webhook endpoint management. It ships a real OpenAPI 3.0 definition, a first-class s-idempotency-key on every mutating request, four rate-limit
  response headers across a 60-second and a 24-hour window, and 15 HMAC-signed webhook event types. API access is gated twice: it is part of the Communicator plan, and an organization must additionally contact Spruce Support to have API access enabled before an administrator can generate a token.'
finops:
- name: Spruce Health Finops
  service_category: Healthcare Communication
  slug: spruce-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spruce-health.png
layout: provider
mcp_servers:
- description: ''
  name: spruce-health-mcp.yml
  slug: spruce-health-mcpyml
modified: '2026-08-15'
name: Spruce Health
nav: Providers
network: true
overview: 'Spruce Health publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Contact Fields API, Contact Tags API, Contacts API, and 12 more. Tagged areas include Healthcare, HIPAA, Health Care, Communication, and Secure Messaging.


  The Spruce Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spruce Health''s developer surface includes authentication, documentation, signup flow, changelog, API reference, getting-started guide, support, and 29 more developer resources.'
plans:
- name: Spruce Health Plans Pricing
  plan_count: 3
  slug: spruce-health-plans-pricing
random_paper: 141
rate_limits:
- limit_count: 3
  name: Spruce Health Rate Limits
  slug: spruce-health-rate-limits
score:
  band: strong
  composite: 65.1
  delta: 28.4
  facets:
    commercial_clarity: 92.1
    contract_quality: 69.9
    developer_ergonomics: 67.4
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 76.3
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Spruce Health Authentication
  slug: spruce-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spruce Health Domain Security
  slug: spruce-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spruce-health
tags:
- Healthcare
- HIPAA
- Health Care
- Communication
- Secure Messaging
- Telehealth
- Patient Engagement
- Contacts
- Conversations
- Messaging
- SMS
- Voice
- VoIP
- Fax
- Video
- Webhooks
- Scheduling
- Transcription
- EHR Integration
- Compliance
website: https://sprucehealth.com
---
