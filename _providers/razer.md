---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'Razer Chroma REST API for controlling 16.8-million-color RGB lighting effects across Chroma-enabled keyboards, mice, headsets, mousepads, keypads and ChromaLink devices. Clients POST application info '
  name: Razer Chroma RGB REST API
  slug: razer-chroma-rgb-rest-api
- description: Razer Gold developer and partner program payment API for monetizing games and apps with Razer Gold virtual currency across 19 currencies and 5 million channel touchpoints, with fraud and chargeback pr
  name: Razer Gold API
  slug: razer-gold-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/razer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://razer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.razer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wyvrn.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/razerofficial
- group: company
  title: ''
  type: Blog
  url: https://www.razer.com/blog
- group: operate
  title: ''
  type: Support
  url: https://mysupport.razer.com/
- group: build
  title: ''
  type: Packages
  url: packages/razer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/razer-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/razer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/razer-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/razer-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/razer-llms.txt
created: '2026-07-17'
description: Razer is a global lifestyle brand for gamers that designs gaming hardware (Blade laptops, mice, keyboards, headsets and other peripherals), software (Synapse, Cortex) and services. For developers Razer operates the WYVRN immersive gaming platform, exposing the Razer Chroma RGB SDK and REST API for controlling 16.8-million-color lighting across devices, the Razer Sensa HD Haptics and THX Spatial Audio SDKs, Razer ID for user sign-in, and the Razer Gold / Razer Silver virtual-currency payment and rewards APIs for in-app monetization across 34,000+ integrated games and apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/razer.png
layout: provider
modified: '2026-07-20'
name: Razer
nav: Providers
network: true
overview: 'Razer publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Hardware, and Peripherals.


  Razer''s developer surface includes documentation, engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 16.9
  delta: -2.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Razer Authentication
  slug: razer-authentication
  summary_line: none/custom-credentials/user-sign-in · 3 schemes
- kind: domain-security
  name: Razer Domain Security
  slug: razer-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: razer
tags:
- Company
- Consumer
- Gaming
- Hardware
- Peripherals
- RGB Lighting
- Haptics
- Payments
- Developer Platform
- SDK
website: https://razer.com/
---
