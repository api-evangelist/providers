---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Xrhealth Agentic Access
  operation_count: 12
  slug: xrhealth-agentic-access
  summary_line: 12 operations · 8 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.xr.health/v1
  baseurl_source: declared
  description: First-party REST API for XRHealth applications and approved integrations, published as OpenAPI 3.1.0 at https://api.xr.health/v1/openapi.json. The document currently describes the platform authenticat
  name: XRHealth Platform API
  slug: xrhealth-platform-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xrhealth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xrhealth-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/xrhealth-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xrhealth-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/xrhealth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xrhealth-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xrhealth-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xrhealth-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xrhealth-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xrhealth-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xrhealth-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xrhealth-plans-pricing.yml
- group: agent
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
overview: 'XRHealth publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Health, Digital Health, Telehealth, Virtual Reality, and Extended Reality.


  XRHealth''s developer surface includes authentication, signup flow, support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Xrhealth Plans Pricing
  plan_count: 0
  slug: xrhealth-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Xrhealth Rate Limits
  slug: xrhealth-rate-limits
scopes:
- name: Xrhealth Scopes
  scope_count: 2
  slug: xrhealth-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Xrhealth Authentication
  slug: xrhealth-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Xrhealth Domain Security
  slug: xrhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
