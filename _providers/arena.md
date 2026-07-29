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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Arena''s REST Platform API (V3) for programmatically managing engagement resources — Liveblog, Live Chat, Analytics, Account, Stream, Users, Moderation, Polls, and Q&A — mirroring the Arena Dashboard. '
  name: Arena Platform API
  slug: arena-platform-api
artifact_total: 4
asyncapis:
- description: ''
  name: Arena Webhooks
  slug: arena-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://arena.im/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.arena.im/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.arena.im/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.arena.im/
- group: operate
  title: ''
  type: Support
  url: https://help.arena.im/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.arena.im/
- group: company
  title: ''
  type: Blog
  url: https://arena.im/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://arena.im/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.arena.im/auth/create
- group: start
  title: ''
  type: Login
  url: https://app.arena.im/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arena.im/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arena.im/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stationfy
- group: build
  title: ''
  type: Packages
  url: packages/arena-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/arena-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arena-authentication.yml
- group: design
  title: ''
  type: Components
  url: components/arena-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arena-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/arena-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arena-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arena-llms.txt
created: '2026-07-17'
description: Arena is an AI-powered audience engagement platform that lets publishers, media companies, and brands build first-party communities directly on their own websites and apps. Its products include Live Chat, Live Blog, Comments, Polls, and Q&A, plus moderation, analytics, and monetization tooling designed to increase traffic, boost engagement, generate leads, and monetize audiences. Developers integrate through the Arena Platform API (V3) and official JavaScript, Android, and iOS SDKs, authenticating with a site API key or a JWT that also powers Single Sign-On for Live Chat and Live Blog. Arena is a developer-tools / audience-engagement company backed by CRV, Felicis, Lightspeed Venture Partners, and Techstars.
image: https://dashboard-sandbox.arena.im/js/imgs/arena-logo-purple.png
layout: provider
modified: '2026-07-18'
name: Arena
nav: Providers
network: true
overview: 'Arena publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Audience Engagement, Live Chat, and Live Blog.


  The Arena catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Arena''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 14 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 40.7
  delta: 5.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 35.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/arena/refs/heads/main/screenshots/arena-2026-07-25T201123.png
security:
- kind: authentication
  name: Arena Authentication
  slug: arena-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Arena Domain Security
  slug: arena-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arena
tags:
- Company
- Developer Tools
- Audience Engagement
- Live Chat
- Live Blog
- Comments
- Community
- Real-Time
- Moderation
- Media
website: https://arena.im/
---
