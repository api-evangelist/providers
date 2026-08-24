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
api_count: 2
apis:
- description: Vocalware is Oddcast's cloud text-to-speech service. It exposes a pay-as-you-go HTTP/REST API (suitable for mobile and server-side/standalone apps) and a JavaScript/HTML5 API (for in-browser playback)
  name: Vocalware Text-to-Speech API
  slug: vocalware-text-to-speech-api
- description: SitePal is Oddcast's AI avatar platform. Speaking characters are embedded on a web page or app and controlled at runtime through a JavaScript (VHost) API with methods such as sayText, sayAudio, sayAI,
  name: SitePal Avatar API
  slug: sitepal-avatar-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://oddcast.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.vocalware.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.vocalware.com/support/javascript
- group: docs
  title: ''
  type: APIReference
  url: https://www.vocalware.com/support/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sitepal.com/guide
- group: operate
  title: ''
  type: Support
  url: https://www.vocalware.com/support/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vocalware.com/index/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.vocalware.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://www.vocalware.com/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oddcast.com/term-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oddcast.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/oddcast-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oddcast-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/oddcast-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oddcast-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oddcast-domain-security.yml
created: '2026-07-17'
description: 'Oddcast is a New York-based creative media technology company that builds speaking-character, avatar, and text-to-speech products for agencies, brands, business, and education. For developers it operates two API-driven products: Vocalware, a pay-as-you-go cloud text-to-speech service exposed as an HTTP/REST API and a JavaScript/HTML5 API with hundreds of voices across more than thirty languages; and SitePal, an AI avatar platform whose speaking characters are embedded and controlled at runtime through a JavaScript (VHost) API for speech, facial expression, background, and AI-assistant integration. Both products are self-service with free trials, per-stream/per-download pricing, and published developer references.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oddcast.png
layout: provider
modified: '2026-07-20'
name: Oddcast
nav: Providers
network: true
overview: 'Oddcast publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Text-to-Speech, Speech Synthesis, Avatars, and Voice.


  Oddcast''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 9 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oddcast/refs/heads/main/screenshots/oddcast-2026-08-07T185949.png
security:
- kind: authentication
  name: Oddcast Authentication
  slug: oddcast-authentication
  summary_line: apiKey/checksum · 2 schemes
- kind: domain-security
  name: Oddcast Domain Security
  slug: oddcast-domain-security
  summary_line: TLSv1.2 · DMARC
slug: oddcast
tags:
- Company
- Text-to-Speech
- Speech Synthesis
- Avatars
- Voice
- Media
- Creative Technology
- Education
- Developers
website: https://oddcast.com
---
