---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 8
  human_in_the_loop: 0
  name: Global Relay Agentic Access
  operation_count: 8
  slug: global-relay-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 5
apis:
- description: Endpoints for archiving conversations
  name: Global Relay Conversations API
  slug: global-relay-conversations-api
- description: Endpoints for archiving email messages
  name: Global Relay Email API
  slug: global-relay-email-api
- description: Endpoints for archiving event cards
  name: Global Relay Events API
  slug: global-relay-events-api
- description: Endpoints for uploading file attachments
  name: Global Relay Files API
  slug: global-relay-files-api
- description: Endpoints for archiving voice and video recordings
  name: Global Relay Voice API
  slug: global-relay-voice-api
artifact_total: 26
collections:
- collection_type: open
  name: Global Relay Conversation Archiving API
  slug: open-global-relay-conversation-archiving-api
- collection_type: open
  name: Global Relay Email Archiving API
  slug: open-global-relay-email-archiving-api
- collection_type: open
  name: Global Relay Event Archiving API
  slug: open-global-relay-event-archiving-api
- collection_type: open
  name: Global Relay Voice Archiving API
  slug: open-global-relay-voice-archiving-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/global-relay-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/global-relay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/global-relay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/global-relay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globalrelay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/global-relay
- group: start
  title: ''
  type: Portal
  url: https://developers.globalrelay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.globalrelay.com/connector/conversation-archiving-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.globalrelay.com/connector/eventfeed-archiving-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.globalrelay.com/connector/voice-archiving-api/
- group: agent
  title: ''
  type: LlmsText
  url: https://globalrelay.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.globalrelay.com/resources/blog/
created: '2025-01-01'
description: Global Relay is an enterprise-grade archiving and compliance platform for electronic communications including email, instant messaging, voice, video, and collaboration tools across regulated industries. It provides APIs for archiving conversations, emails, voice recordings, and event feeds from social media and collaboration platforms, ensuring organizations meet their compliance and regulatory requirements through secure, tamper-proof archiving with OAuth 2.0 authenticated REST APIs.
finops:
- name: Global Relay Finops
  service_category: Compliance / Archiving
  slug: global-relay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/global-relay.png
json_schemas:
- name: Global Relay Conversation
  property_count: 5
  slug: global-relay-conversation
- name: Global Relay Email Address
  property_count: 2
  slug: global-relay-email-address
- name: Global Relay Email
  property_count: 11
  slug: global-relay-email
- name: Global Relay Event Card
  property_count: 5
  slug: global-relay-event-card
- name: Global Relay Event
  property_count: 6
  slug: global-relay-event
- name: Global Relay File
  property_count: 4
  slug: global-relay-file
- name: Global Relay Participant
  property_count: 4
  slug: global-relay-participant
- name: Global Relay Voice Record
  property_count: 9
  slug: global-relay-voice-record
jsonld:
- class_count: 31
  name: Global Relay Context
  property_count: 15
  slug: global-relay-context
layout: provider
modified: '2026-05-19'
name: Global Relay
nav: Providers
network: true
overview: 'Global Relay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Email API, Events API, and 2 more. Tagged areas include Archiving, Compliance, Data Retention, Email Security, and Regulatory Compliance.


  The Global Relay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Global Relay''s developer surface includes authentication, developer portal, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Global Relay Plans Pricing
  plan_count: 2
  slug: global-relay-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Global Relay Rate Limits
  slug: global-relay-rate-limits
rules:
- name: Global Relay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: global-relay-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.7
  delta: -3.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 69.5
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/global-relay/refs/heads/main/screenshots/global-relay-2026-06-20T181917.png
security:
- kind: authentication
  name: Global Relay Authentication
  slug: global-relay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Global Relay Domain Security
  slug: global-relay-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Global Relay Trust Center
  slug: global-relay-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: global-relay
tags:
- Archiving
- Compliance
- Data Retention
- Email Security
- Regulatory Compliance
website: https://developers.globalrelay.com/
---
