---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replika-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replika-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/replika-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://replika.com
- group: operate
  title: ''
  type: Support
  url: https://help.replika.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://replika.com/legal/terms/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://replika.com/legal/privacy/en
created: '2026-07-17'
description: Replika is an AI companion mobile and web application built by Luka, Inc. that lets people create a personalized conversational AI "friend" for chat, emotional support, roleplay, voice calls, and augmented-reality companionship. The product is a closed consumer experience delivered through iOS, Android, and a legacy web app; it retains conversational memory and adapts its personality over time. Replika does not publish a public developer API, SDKs, OpenAPI/AsyncAPI specifications, webhooks, or an MCP server — all model behavior is applied server-side and surfaced only through the first-party apps. This API Evangelist profile therefore captures identity, legal, support, and domain-security signals rather than an API contract. Replika was surfaced as a Y Combinator portfolio company and enriched here as a company profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replika.png
layout: provider
modified: '2026-07-20'
name: Replika
nav: Providers
network: true
overview: 'Replika is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Chatbot, AI Companion, and Consumer App.


  Replika''s developer surface includes support and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 11.9
  delta: 0.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Replika Domain Security
  slug: replika-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: replika
tags:
- Company
- Artificial Intelligence
- Chatbot
- AI Companion
- Consumer App
- Conversational AI
- Mobile
website: https://replika.com
---
