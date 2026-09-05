---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
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
random_paper: 2
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
