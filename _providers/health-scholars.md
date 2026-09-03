---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://upskillai.com/
- group: company
  title: ''
  type: About
  url: https://upskillai.com/about/
- group: operate
  title: ''
  type: Support
  url: https://upskillai.com/contact/
- group: start
  title: ''
  type: Login
  url: https://app.upskillai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upskillai.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upskillai.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HealthScholars
- group: auth
  title: ''
  type: DomainSecurity
  url: security/health-scholars-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/health-scholars-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/health-scholars-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/health-scholars-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/health-scholars-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Health Scholars rebranded to UpSkillAI and sells XR training as an end-user product only — healthscholars.com 301s to upskillai.com, whose entire published site is 12 marketing pages with no developer section, and whose application backend api.upskillai.com answers unauthenticated callers with a bare 13-byte "404 Not Found".
  evidence:
  - status: 301
    url: https://healthscholars.com/
  - status: 200
    url: https://upskillai.com/
  - status: 404
    url: https://api.upskillai.com/openapi.json
  - status: 403
    url: https://api.healthscholars.com/openapi.json
  - status: 404
    url: https://upskillai.com/.well-known/agent-card.json
  - status: 404
    url: https://upskillai.com/pricing/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'Health Scholars — which rebranded to UpSkillAI in 2025 and now trades at upskillai.com — builds AI-powered extended reality (XR/VR) simulation training for mission-critical, hands-on work in healthcare, emergency medical services, stroke assessment and defense. The platform pairs voice-driven VR simulations with simulation management and readiness reporting, letting hospital systems, first responders and government programs run standardized protocol training on headsets without instructors or extra equipment. Customers reach it through a hosted web console at app.upskillai.com. The company publishes no public developer program: there is no developer portal, API reference, OpenAPI or other machine-readable contract, SDK, webhook catalog or public pricing. The production backend behind its own application (api.upskillai.com, with the legacy AWS API Gateway host api.healthscholars.com) is private and rejects unauthenticated requests.'
image: https://upskillai.com/wp-content/uploads/2025/10/Health_Scholars_Logo_alt.svg
layout: provider
modified: '2026-08-22'
name: Health Scholars
nav: Providers
network: true
overview: 'Health Scholars is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Training, Simulation, Virtual Reality, and Extended Reality.


  Health Scholars'' developer surface includes support and 11 more developer resources.'
plans:
- name: Health Scholars Plans Pricing
  plan_count: 0
  slug: health-scholars-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Health Scholars Rate Limits
  slug: health-scholars-rate-limits
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/health-scholars/refs/heads/main/screenshots/health-scholars-2026-09-02T145711.png
security:
- kind: domain-security
  name: Health Scholars Domain Security
  slug: health-scholars-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: health-scholars
tags:
- Company
- Training
- Simulation
- Virtual Reality
- Extended Reality
- Healthcare
- Education
- Defense
- Emergency Medical Services
- Artificial Intelligence
website: https://upskillai.com/
---
