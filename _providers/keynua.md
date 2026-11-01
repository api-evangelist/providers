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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST API for creating contracts, sending them to signers over WhatsApp/SMS/email, running biometric identity verification, generating documents from templates, sending and verifying OTPs, and register
  name: Keynua API
  slug: keynua-api
artifact_total: 9
asyncapis:
- description: ''
  name: Keynua Webhooks
  slug: keynua-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/keynua/plans/keynua-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keynua-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/keynua/security/keynua-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keynua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.keynua.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://keynua.github.io/slate
- group: docs
  title: ''
  type: Documentation
  url: https://keynua.github.io/slate
- group: docs
  title: ''
  type: APIReference
  url: https://keynua.github.io/slate
- group: start
  title: ''
  type: GettingStarted
  url: https://keynua.github.io/slate/#introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keynua.com/en/plans/
- group: start
  title: ''
  type: SignUp
  url: https://www.keynua.com/en/account-request/
- group: start
  title: ''
  type: Login
  url: https://app.keynua.com?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keynua.com/en/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keynua.com/en/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Keynua
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keynua.com
- group: design
  href: https://artifacts.apis.io/keynua/lifecycle/keynua-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keynua-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/keynua/authentication/keynua-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keynua-authentication.yml
- group: design
  href: https://artifacts.apis.io/keynua/errors/keynua-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/keynua-error-codes.yml
- group: design
  href: https://artifacts.apis.io/keynua/conventions/keynua-conventions.yml
  title: ''
  type: Conventions
  url: conventions/keynua-conventions.yml
- group: design
  href: https://artifacts.apis.io/keynua/asyncapi/keynua-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/keynua-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/keynua/mcp/keynua-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/keynua-mcp.yml
- group: agent
  href: https://artifacts.apis.io/keynua/llms/keynua-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keynua-llms.txt
- group: start
  href: https://artifacts.apis.io/keynua/sandbox/keynua-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/keynua-sandbox.yml
- group: design
  href: https://artifacts.apis.io/keynua/data-model/keynua-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keynua-data-model.yml
- group: agent
  href: https://artifacts.apis.io/keynua/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Keynua is a Latin American digital identity and electronic signature platform that lets businesses design signing flows combining video, drawn, OTP, and digital signatures with biometric identity verification — liveness detection, facial matching, 3D and selfie identification, and geopositioning. Its REST API covers contracts, document templates, identity verification, OTP, and Deceval promissory notes, delivering requests to signers over WhatsApp, SMS, or email and emitting webhooks for asynchronous processing events. It supports 20+ Latin American identity documents across 20 countries and serves financial services, real estate, human resources, commercial contracts, and sports betting.
finops:
- has_sources: true
  method: derived
  name: Keynua Finops
  primary_unit: transaction pack
  service_category: ''
  slug: keynua-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keynua.png
layout: provider
modified: '2026-07-19'
name: Keynua
nav: Providers
network: true
overview: 'Keynua is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Signature, Digital Signature, Identity Verification, and Biometrics.


  The Keynua catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Keynua''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, sandbox, and 17 more developer resources.'
plans:
- name: Keynua Plans Pricing
  plan_count: 7
  slug: keynua-plans-pricing
random_paper: 5
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 41.0
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/keynua/keynua-2026-07-25T223656.png
security:
- kind: authentication
  name: Keynua Authentication
  slug: keynua-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Keynua Domain Security
  slug: keynua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create and sign a Keynua contract
  slug: keynua-create-and-sign-contract
- name: Send and verify a Keynua OTP
  slug: keynua-send-and-verify-otp
- name: Run a Keynua identity verification
  slug: keynua-verify-identity
slug: keynua
tags:
- Company
- E-Signature
- Digital Signature
- Identity Verification
- Biometrics
- KYC
- Onboarding
- OTP
- Webhook
- Latin America
website: https://www.keynua.com/en
---
