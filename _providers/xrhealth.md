---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Xrhealth Agentic Access
  operation_count: 12
  slug: xrhealth-agentic-access
  summary_line: 12 operations · 8 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.xr.health/v1
  baseurl_source: declared
  description: The Auth API from XRHealth — 8 operation(s) for auth.
  name: XRHealth Auth API
  slug: xrhealth-auth-api
- baseURL: https://api.xr.health/v1
  baseurl_source: declared
  description: The Me API from XRHealth — 1 operation(s) for me.
  name: XRHealth Me API
  slug: xrhealth-me-api
- baseURL: https://api.xr.health/v1
  baseurl_source: declared
  description: The Openapi.json API from XRHealth — 1 operation(s) for openapi.json.
  name: XRHealth Openapi.json API
  slug: xrhealth-openapi-json-api
- baseURL: https://api.xr.health/v1
  baseurl_source: declared
  description: The .well Known API from XRHealth — 1 operation(s) for .well known.
  name: XRHealth .well Known API
  slug: xrhealth-well-known-api
- baseURL: https://api.xr.health/v1
  baseurl_source: declared
  description: The XRHealth Platform API API from XRHealth — 1 operation(s) for xrhealth platform api.
  name: XRHealth XRHealth Platform API
  slug: xrhealth-xrhealth-platform-api-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/xrhealth/overlays/xrhealth-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xrhealth-platform-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/xrhealth/agentic-access/xrhealth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xrhealth-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/xrhealth/security/xrhealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xrhealth-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/xrhealth/authentication/xrhealth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xrhealth-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.xr.health/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.xr.health/
- group: start
  title: ''
  type: SignUp
  url: https://developer.xr.health/en/login
- group: start
  title: ''
  type: Login
  url: https://platform.xr.health/en/login
- group: operate
  title: ''
  type: Support
  url: https://support.xr.health/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.xr.health/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xr.health/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform.xr.health/en/p/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.xr.health/en/p/privacy
- group: build
  href: https://artifacts.apis.io/xrhealth/packages/xrhealth-packages.yml
  title: ''
  type: Packages
  url: packages/xrhealth-packages.yml
- group: agent
  href: https://artifacts.apis.io/xrhealth/llms/xrhealth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xrhealth-llms.txt
- group: design
  href: https://artifacts.apis.io/xrhealth/conventions/xrhealth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xrhealth-conventions.yml
- group: design
  href: https://artifacts.apis.io/xrhealth/errors/xrhealth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xrhealth-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xrhealth/data-model/xrhealth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xrhealth-data-model.yml
- group: design
  href: https://artifacts.apis.io/xrhealth/lifecycle/xrhealth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xrhealth-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/xrhealth/conformance/xrhealth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xrhealth-conformance.yml
- group: auth
  href: https://artifacts.apis.io/xrhealth/scopes/xrhealth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/xrhealth-scopes.yml
- group: operate
  href: https://artifacts.apis.io/xrhealth/rate-limits/xrhealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xrhealth-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/xrhealth/plans/xrhealth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xrhealth-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/xrhealth/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-04'
description: XRHealth is an extended-reality (XR) therapeutics and virtual-clinic company, founded in 2016 with offices in Boston, Massachusetts and Tel Aviv, Israel, that delivers FDA-registered and CE-marked virtual and augmented reality treatment for physical rehabilitation, cognitive training, pain management and mental health. Patients receive VR headsets at home and work with licensed clinicians through the XRHealth Virtual Clinic, while therapists use the XRHealth platform to prescribe applications, review session telemetry and track outcomes. The company merged with Amelia Virtual Care in 2023 to form one of the largest XR therapeutics platforms. Its programmable surface is the XRHealth Platform API on api.xr.health — a first-party OpenAPI 3.1 contract covering passwordless patient authentication, PKCE public-client token exchange, refresh-token rotation and JWKS key publication — plus an invitation-only XRH Developer portal for approved integrations.
image: https://blog.xr.health/hubfs/logo%20to%20chat.png
layout: provider
modified: '2026-09-04'
name: XRHealth
nav: Providers
network: true
overview: 'XRHealth publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Me API, Openapi.json API, and 2 more. Tagged areas include Health, Digital Health, Telehealth, Virtual Reality, and Extended Reality.


  The XRHealth catalog on APIs.io includes 1 Spectral governance ruleset.


  XRHealth''s developer surface includes authentication, signup flow, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Xrhealth Plans Pricing
  plan_count: 0
  slug: xrhealth-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Xrhealth Rate Limits
  slug: xrhealth-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: XRHealth API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: xrhealth-rules
scopes:
- name: Xrhealth Scopes
  scope_count: 2
  slug: xrhealth-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 44.5
    developer_ergonomics: 30.4
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/xrhealth/xrhealth-2026-10-11T195303.png
security:
- kind: authentication
  name: Xrhealth Authentication
  slug: xrhealth-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Xrhealth Domain Security
  slug: xrhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: XRHealth public-client PKCE login
  slug: xrhealth-public-client-pkce-login
- name: XRHealth server-side patient login
  slug: xrhealth-server-side-patient-login
slug: xrhealth
tags:
- Health
- Digital Health
- Telehealth
- Virtual Reality
- Extended Reality
- Medical Devices
- Rehabilitation
- Mental Health
- Patient Authentication
- Healthcare
website: https://www.xr.health/
---
