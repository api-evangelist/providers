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
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Early-stage REST API for the Karaz platform exposing Karaz App resources (e.g. gamification Badges) and Karaz Care resources (e.g. Appointments), plus shared chat (WebSocket) events. HTTPS, version-pr
  name: Karaz API
  slug: karaz-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://karaz.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.karaz.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.karaz.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.karaz.app/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karaz.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karaz.app/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/karaz-platform-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/karaz-platform-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/karaz-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://karaz.app
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/karaz-platform-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/karaz-platform-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karaz-platform-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/karaz-platform-llms.txt
created: '2026-07-17'
description: Karaz is an AI-driven Electronic Health Record (EHR) platform based in Saudi Arabia that connects healthcare practitioners, patients, insurance providers, and wellness vendors in a unified health-management ecosystem. It provides real-time biometric and continuous-glucose (CGM) monitoring, AI-driven treatment insights, patient and provider mobile apps, analytics and reporting, rewards and community engagement, and a health-vendor marketplace, with integrations across Apple, Abbott, Medtronic, Dexcom, Roche, Google, and Omron. The Karaz developer API (early-stage) exposes Karaz App and Karaz Care resources over HTTPS with Bearer-token authentication. Surfaced as a portfolio company of 500 Global and enriched by the API Evangelist pipeline from public sources.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karaz-platform.png
layout: provider
modified: '2026-07-20'
name: Karaz Platform
nav: Providers
network: true
overview: 'Karaz Platform publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Electronic Health Records, EHR, and Health.


  Karaz Platform''s developer surface includes documentation, getting-started guide, authentication, and 11 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 25.9
  delta: -3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 29.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karaz-platform/refs/heads/main/screenshots/karaz-platform-2026-07-25T223502.png
security:
- kind: authentication
  name: Karaz Platform Authentication
  slug: karaz-platform-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Karaz Platform Domain Security
  slug: karaz-platform-domain-security
  summary_line: TLSv1.3 · DMARC
slug: karaz-platform
tags:
- Company
- Healthcare
- Electronic Health Records
- EHR
- Health
- Remote Patient Monitoring
- Appointments
- Artificial Intelligence
- Saudi Arabia
website: https://karaz.app
---
