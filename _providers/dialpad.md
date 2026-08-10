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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Dialpad Agentic Access
  operation_count: 38
  slug: dialpad-agentic-access
  summary_line: 38 operations · 23 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Originate, control and read call records and recordings.
  name: Dialpad Calls API
  slug: dialpad-calls-api
- description: Provision and manage users, offices and groups.
  name: Dialpad Users API
  slug: dialpad-users-api
- description: Manage phone numbers including main lines and assignment.
  name: Dialpad Numbers API
  slug: dialpad-numbers-api
- description: Send and receive SMS and MMS.
  name: Dialpad SMS API
  slug: dialpad-sms-api
- description: Contact center call routing, queues, agents and stats.
  name: Dialpad Contact Center API
  slug: dialpad-contact-center-api
- description: Transcripts, summaries, sentiment, and Ai-powered moments.
  name: Dialpad Conversation AI API
  slug: dialpad-conversation-ai-api
- description: Register and manage webhook subscriptions.
  name: Dialpad Webhooks API
  slug: dialpad-webhooks-api
- description: The Calls API from Dialpad — 7 operation(s) for calls.
  name: Dialpad Calls API
  slug: dialpad-calls-api
- description: The Contacts API from Dialpad — 2 operation(s) for contacts.
  name: Dialpad Contacts API
  slug: dialpad-contacts-api
- description: The Offices API from Dialpad — 2 operation(s) for offices.
  name: Dialpad Offices API
  slug: dialpad-offices-api
- description: The Recordings API from Dialpad — 2 operation(s) for recordings.
  name: Dialpad Recordings API
  slug: dialpad-recordings-api
- description: The Rooms API from Dialpad — 2 operation(s) for rooms.
  name: Dialpad Rooms API
  slug: dialpad-rooms-api
- description: The Subscriptions API from Dialpad — 3 operation(s) for subscriptions.
  name: Dialpad Subscriptions API
  slug: dialpad-subscriptions-api
- description: The Transcripts API from Dialpad — 2 operation(s) for transcripts.
  name: Dialpad Transcripts API
  slug: dialpad-transcripts-api
- description: The Users API from Dialpad — 3 operation(s) for users.
  name: Dialpad Users API
  slug: dialpad-users-api
- description: The Webhooks API from Dialpad — 2 operation(s) for webhooks.
  name: Dialpad Webhooks API
  slug: dialpad-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: Dialpad Webhook Events API
  slug: open-dialpad-asyncapi
- collection_type: open
  name: Dialpad API
  slug: open-dialpad
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dialpad-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dialpad-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dialpad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dialpad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dialpad-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dialpad
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dialpad
- group: company
  title: ''
  type: Website
  url: https://www.dialpad.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/dialpad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dialpad-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dialpad-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.dialpad.com/llms.txt
created: '2026-05-08'
description: Dialpad is an AI-powered cloud communications platform offering business phone, contact center, video, and messaging. Notable for Dialpad Ai (real-time transcription, sentiment, coaching).
finops:
- name: Dialpad Finops
  service_category: Communications
  slug: dialpad-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Dialpad API. Dialpad is an AI-powered cloud communications platform offering business phone, contact center, video, and messaging services —
  name: Dialpad GraphQL Schema
  slug: dialpad-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dialpad.png
layout: provider
modified: '2026-05-30'
name: Dialpad
nav: Providers
network: true
overview: 'Dialpad publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Users API, Webhooks API, and 9 more. Tagged areas include Communications, Voice, AI, Contact Center, and UCaaS.


  Dialpad''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Dialpad Plans Pricing
  plan_count: 1
  slug: dialpad-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Dialpad Rate Limits
  slug: dialpad-rate-limits
score:
  band: thin
  composite: 35.7
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 67.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 90.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dialpad/refs/heads/main/screenshots/dialpad-2026-06-20T180006.png
security:
- kind: authentication
  name: Dialpad Authentication
  slug: dialpad-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dialpad Domain Security
  slug: dialpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dialpad Vulnerability Disclosure
  slug: dialpad-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dialpad Trust Center
  slug: dialpad-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CSA STAR
slug: dialpad
tags:
- Communications
- Voice
- AI
- Contact Center
- UCaaS
website: https://www.dialpad.com/
---
