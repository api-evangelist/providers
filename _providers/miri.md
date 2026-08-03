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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Server-side Miri API (API-key authenticated) plus the React Native Component SDK for embedding Miri's chat, goal-tracking, measurement, and admin surfaces, with configurable webhooks. Currently in alp
  name: Miri API
  slug: miri-api
artifact_total: 4
asyncapis:
- description: ''
  name: Miri Webhooks
  slug: miri-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/miri-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.miri.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.miri.ai/developer/docs/alpha/main
- group: docs
  title: ''
  type: Documentation
  url: https://www.miri.ai/developer/docs/alpha/main
- group: start
  title: ''
  type: Portal
  url: https://miri.health
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.miri.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.miri.ai/terms
- group: operate
  title: ''
  type: Support
  url: mailto:support@miri.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/miri-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/miri-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/miri-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/miri-packages.yml
- group: design
  title: ''
  type: Components
  url: components/miri-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/miri-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/miri-llms.txt
created: '2026-07-17'
description: Miri (Miri AI) is an AI-powered health and wellness engagement platform based in Oakland, California, that helps digital health, telehealth, GLP-1 and medical weight-loss, lab-diagnostics, and supplement companies increase patient retention and lifetime value. Miri sits between clinical touchpoints as a daily AI companion — logging meals via text or photo, tracking goals and body measurements, and running coach check-ins — while a behavioral-intelligence layer surfaces at-risk users and revenue opportunities. Developers embed Miri through a React Native Component SDK and a server-side, API-key-authenticated API with configurable webhooks for events such as meal logging, goal completion, profile updates, coach interactions, and push notifications. The developer program is currently in alpha.
image: https://cdn.prod.website-files.com/694f2f5f5d150634df22024d/69969307b5f2e9ea4dedb518_Group%209725.png
layout: provider
modified: '2026-07-20'
name: Miri
nav: Providers
network: true
overview: 'Miri publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Wellness, Digital Health, and Telehealth.


  The Miri catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Miri''s developer surface includes documentation, developer portal, support, authentication, and 11 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 39.1
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Miri Authentication
  slug: miri-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Miri Domain Security
  slug: miri-domain-security
  summary_line: TLSv1.3 · HSTS
slug: miri
tags:
- Company
- Health
- Wellness
- Digital Health
- Telehealth
- Artificial Intelligence
- Patient Engagement
- Weight Loss
- SDK
- Webhooks
website: https://www.miri.ai
---
