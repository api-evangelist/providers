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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Apero's fully-featured REST API connecting healthcare and finance workflows for medical practices, with webhooks and CSV import. Developer documentation is gated behind an Apero account login.
  name: Apero Health API
  slug: apero-health-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apero-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apero-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aperostatus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aperohealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aperohealth.com/
- group: design
  title: ''
  type: Webhooks
  url: https://docs.aperohealth.com/webhooks
- group: start
  title: ''
  type: SignUp
  url: https://app.aperohealth.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.aperohealth.com/login
- group: operate
  title: ''
  type: Support
  url: https://aperohealth.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aperohealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aperohealth.com/privacy
- group: company
  title: ''
  type: Website
  url: https://aperohealth.com/
created: '2026-07-17'
description: Apero Health is a San Francisco-based, Y Combinator-backed healthcare technology company that provides an integrated practice-management and revenue-cycle-management (RCM) platform for medical practices. Its cloud software unifies scheduling, clinical visit notes, insurance eligibility verification and claims billing, patient billing and payments, e-prescriptions, and financial reporting, and claims to reduce billing time by up to 80% while helping practices scale operations. Apero exposes a fully-featured REST API, webhooks, and CSV import that connect healthcare and finance workflows, and integrates with payers (Aetna, Cigna, UnitedHealthcare, Blue Cross Blue Shield) and platforms including Stripe, QuickBooks Online, Google, and Snowflake.
image: https://cdn.prod.website-files.com/642de057e0489a5a784c3b68/642de057e0489a03594c3d2b_Frame%2039.svg
layout: provider
modified: '2026-07-17'
name: Apero
nav: Providers
network: true
overview: 'Apero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Healthcare, Health Tech, and Revenue Cycle Management.


  Apero''s developer surface includes documentation, signup flow, support, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 3.9
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apero/refs/heads/main/screenshots/apero-2026-07-25T200557.png
security:
- kind: domain-security
  name: Apero Domain Security
  slug: apero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apero
tags:
- Company
- Enterprise Saas
- Healthcare
- Health Tech
- Revenue Cycle Management
- Medical Billing
- Practice Management
- Insurance
- Payments
- Webhook
website: https://aperohealth.com/
---
