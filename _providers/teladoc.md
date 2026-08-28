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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for the Teladoc Health Solo virtual-care platform. Manages patients, appointments, waiting rooms, appointment slots, visit notes, attachments, patient documents, episodes of care, encounter r
  name: Teladoc Health Solo External API
  slug: teladoc-health-solo-external-api
artifact_total: 7
asyncapis:
- description: ''
  name: Teladoc Webhooks
  slug: teladoc-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.teladochealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-documentation.teladochealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://intouchhealth.github.io/solo-slate/
- group: docs
  title: ''
  type: APIReference
  url: https://intouchhealth.github.io/solo-slate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IntouchHealth
- group: auth
  title: ''
  type: Authentication
  url: authentication/teladoc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teladoc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teladoc-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/teladoc-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/teladoc-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teladoc-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teladoc-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teladoc-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/teladoc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/teladoc-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teladoc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teladoc-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/teladoc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/teladoc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/teladoc-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/teladoc-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/teladoc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teladoc-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://www.teladochealth.com/helpcenter
- group: company
  title: ''
  type: Blog
  url: https://www.teladochealth.com/library
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teladochealth.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teladochealth.com/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://member.teladoc.com/registration
- group: start
  title: ''
  type: Login
  url: https://member.teladoc.com/signin
created: '2026-07-17'
description: 'Teladoc Health is a global virtual-care company providing telehealth, mental and behavioral health, chronic-condition management, and expert medical opinion services. Its developer surface is the Solo platform: a partner-gated REST API (the Solo External API, served under /qapi/v1 on visitnow.org) for patients, appointments, waiting rooms, visit notes, episodes of care, encounter reports, virtual nursing, and webhooks, plus native iOS and Android Mobile SDKs for embedding virtual care into partner applications. Access is granted under a partner agreement and Business Associate Agreement (BAA); requests authenticate with a static Api-Key header. Sector: healthtech.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teladoc.png
layout: provider
modified: '2026-08-15'
name: Teladoc
nav: Providers
network: true
overview: 'Teladoc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Telehealth, Telemedicine, and Virtual Care.


  The Teladoc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teladoc''s developer surface includes documentation, API reference, authentication, sandbox, changelog, support, engineering blog, and 22 more developer resources.'
plans:
- name: Teladoc Plans Pricing
  plan_count: 0
  slug: teladoc-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Teladoc Rate Limits
  slug: teladoc-rate-limits
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 59.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 48.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teladoc/refs/heads/main/screenshots/teladoc-2026-08-17T082301.png
security:
- kind: authentication
  name: Teladoc Authentication
  slug: teladoc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Teladoc Domain Security
  slug: teladoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Teladoc Vulnerability Disclosure
  slug: teladoc-vulnerability-disclosure
  summary_line: contact published
slug: teladoc
tags:
- Company
- Health Tech
- Telehealth
- Telemedicine
- Virtual Care
- Healthcare
- Behavioral Health
- Webhook
website: https://www.teladochealth.com
---
