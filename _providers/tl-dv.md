---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 26.9
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: List, retrieve, import and download meetings
  name: tl;dv Meetings API
  slug: tl-dv-meetings-api
- description: Retrieve AI-generated meeting notes
  name: tl;dv Notes API
  slug: tl-dv-notes-api
- description: Service health
  name: tl;dv System API
  slug: tl-dv-system-api
- description: Retrieve meeting transcripts
  name: tl;dv Transcripts API
  slug: tl-dv-transcripts-api
artifact_total: 8
asyncapis:
- description: Webhook events delivered by tl;dv when a meeting finishes processing or a transcript becomes available. Webhooks are configurable at user, team or organization level.
  name: tl;dv Webhooks
  slug: tl-dv-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://tldv.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.tldv.io
- group: docs
  title: ''
  type: Documentation
  url: https://doc.tldv.io
- group: docs
  title: ''
  type: APIReference
  url: https://doc.tldv.io
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.tldv.io
- group: company
  title: ''
  type: Blog
  url: https://tldv.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/tldv/en
- group: commercial
  title: ''
  type: Pricing
  url: https://tldv.io/app/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://tldv.io/app/signup
- group: start
  title: ''
  type: Login
  url: https://tldv.io/app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tldv.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tldv.io/privacy/
- group: auth
  title: ''
  type: Security
  url: https://tldv.io/features/security-commitment/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tldv.io/
- group: auth
  title: ''
  type: Compliance
  url: https://tldv.io/features/security-commitment/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tl-dv-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tl-dv-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tl-dv-well-known.yml
created: '2026-07-17'
description: tl;dv is an AI meeting notetaker for Zoom, Google Meet and Microsoft Teams that automatically records, transcribes and summarizes meetings in 30+ languages and syncs the resulting insights into CRMs and productivity tools. Its public API (base URL https://pasta.tldv.io, version v1alpha1) gives developers programmatic access to meetings, speaker-attributed transcripts and AI-generated notes, plus meeting import from a URL and webhook delivery of MeetingReady and TranscriptReady events. Authentication is via an x-api-key header issued from account settings.
image: https://api.tldv.io/assets/images/logo_login.png
layout: provider
modified: '2026-07-21'
name: tl;dv
nav: Providers
network: true
overview: 'tl;dv publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Meetings API, Notes API, System API, and 1 more. Tagged areas include Company, AI, Meetings, Transcription, and Notetaking.


  The tl;dv catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  tl;dv''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 11 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.0
    developer_ergonomics: 41.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 48.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tl Dv Authentication
  slug: tl-dv-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tl Dv Domain Security
  slug: tl-dv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tl Dv Trust Center
  slug: tl-dv-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: tl-dv
tags:
- Company
- AI
- Meetings
- Transcription
- Notetaking
- Conversation Intelligence
- Productivity
- Video
- Webhooks
- API
website: https://tldv.io
---
