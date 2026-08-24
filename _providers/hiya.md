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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: Branded calling API to register outbound originating numbers, manage Connect phone numbers and managed brands, upload and manage brand logos, and read branded-phones cache and billing analytics so bus
  name: Hiya Connect API
  slug: hiya-connect-api
- description: Spam and scam protection API covering the business partner reputation surface (register businesses and phones, query reputation), spammer and profile-phone caches distributed as country-specific gzipp
  name: Hiya Protect API
  slug: hiya-protect-api
- description: Audio-based authenticity, identity, and voiceprint verification API for detecting deepfakes and synthetic voices, managing audios, identities, identity/message/authenticity verifications, API keys, or
  name: Hiya Audio Intelligence API
  slug: hiya-audio-intelligence-api
- description: AI voice assistant and call management API for call logs, contacts, relations, user accounts and preferences, notification tokens, call feedback, assistant voices, number profiles, and a live-calls we
  name: Hiya AI Voice Platform API
  slug: hiya-ai-voice-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://hiya.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hiya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hiya.com/docs/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hiya.com/docs/getting-started/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hiya.com/docs/getting-started/introduction
- group: docs
  title: ''
  type: Guides
  url: https://developer.hiya.com/docs/guides/voice-protection/introduction
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.hiya.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://hiya.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hiyainc
- group: operate
  title: ''
  type: Support
  url: https://hiya.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hiya.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hiya.com/terms-of-service
- group: build
  title: ''
  type: MobileSDK
  url: https://developer.hiya.com/docs/mobile-sdk-docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/hiya-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hiya-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hiya-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hiya-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hiya-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/hiya-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hiya-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hiya-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hiya-llms.txt
created: '2026-07-17'
description: 'Hiya is an AI-native voice security company that blocks spam, fraud, and deepfake calls at network scale for mobile operators, enterprises, and consumers. Its developer platform exposes several REST APIs: Hiya Connect for branded outbound calling (registering originating numbers, managing branded phone numbers, logos, and managed brands), Hiya Protect for spam and scam reputation (business partner reputation submission, spammer and profile-phone caches, and voice scam protection reporting), Hiya Audio Intelligence for audio-based authenticity, identity, and voiceprint verification (deepfake and synthetic-voice detection), and the Hiya AI Voice Platform for call logs, contacts, relations, notifications, and an AI voice assistant. APIs are served over HTTPS from api.hiya.com with HTTP Basic authentication using an App ID and App Secret (bearer tokens for Audio Intelligence), plus iOS and Android mobile SDKs for embedding caller ID and protection in apps.'
image: https://developer.hiya.com/img/logo.svg
layout: provider
modified: '2026-07-19'
name: Hiya
nav: Providers
network: true
overview: 'Hiya publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Voice Security, Caller ID, Branded Calling, and Spam Protection.


  Hiya''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 28.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hiya/refs/heads/main/screenshots/hiya-2026-07-25T221307.png
security:
- kind: authentication
  name: Hiya Authentication
  slug: hiya-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Hiya Domain Security
  slug: hiya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hiya
tags:
- Company
- Voice Security
- Caller ID
- Branded Calling
- Spam Protection
- Scam Protection
- Deepfake Detection
- Voice Authentication
- Telecommunications
- Call Analytics
website: https://hiya.com/
---
