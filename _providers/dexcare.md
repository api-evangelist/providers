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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful service for accessing business information and performing actions against DexCare-managed healthcare environments — Virtual Care, Care Options, Booking, Patient, Provider Data Management, Omni
  name: DexCare REST API
  slug: dexcare-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://dexcare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dexcarehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dexcarehealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dexcarehealth.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dexcarehealth.com/jssdk/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DexCare
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexcare.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dexcare.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://dexcare.com/contact-info/
- group: build
  title: ''
  type: Packages
  url: packages/dexcare-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dexcare-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dexcare-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dexcare-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dexcare-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dexcare-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.dexcarehealth.com/api/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dexcare-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dexcare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dexcare.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dexcare-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dexcare-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dexcare-domain-security.yml
created: '2026-07-17'
description: DexCare is a healthcare navigation and care-orchestration platform, launched from within Providence Health, that connects patients to available care across fragmented health systems while helping providers fill capacity and reduce wait times. Its products span Search & Schedule, Virtual On Demand, Provider Data Management (PDM+), Optimize AI, and Acquire. DexCare exposes a RESTful API and native iOS, Android, and JavaScript SDKs that power search-and-schedule, virtual visits, patient records, provider data management, care-options discovery, omni search, and reporting for health systems. Public directory endpoints are open, while PHI/PII endpoints require OAuth 2.0-issued JWT bearer tokens. DexCare operates as a HIPAA business associate. This profile was enriched from DexCare's public developer surface as part of the API Evangelist network (originally surfaced as an ICONIQ Capital portfolio lead).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dexcare.png
layout: provider
modified: '2026-07-18'
name: DexCare
nav: Providers
network: true
overview: 'DexCare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Patient Access, and Scheduling.


  DexCare''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 15 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 32.2
  delta: -4.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 36.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/screenshots/dexcare-2026-07-25T211834.png
security:
- kind: authentication
  name: Dexcare Authentication
  slug: dexcare-authentication
  summary_line: oauth2/http/none · 3 schemes
- kind: domain-security
  name: Dexcare Domain Security
  slug: dexcare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dexcare
tags:
- Company
- Healthcare
- Health IT
- Patient Access
- Scheduling
- Virtual Care
- Telehealth
- Care Navigation
- Provider Data
- SDK
website: https://dexcare.com/
---
