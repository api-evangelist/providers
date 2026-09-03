---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API for food & nutrition data — search, barcode lookup, food-by-id, popular foods, categories, and health probe. Bearer auth optional; read endpoints work anonymously.
  name: DietlyAPI
  slug: dietlyapi
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://getdietly.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dietlyapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dietlyapi-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dietlyapi-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dietlyapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.getdietly.com/uptime
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dietlyapi-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dietlyapi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dietlyapi-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dietlyapi-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dietlyapi-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dietlyapi-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/dietlyapi-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dietlyapi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/dietlyapi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dietlyapi-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getdietly.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getdietly.com/api-guide
- group: docs
  title: ''
  type: APIReference
  url: https://www.getdietly.com/api#reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getdietly.com/api#pricing
- group: operate
  title: ''
  type: Support
  url: https://www.getdietly.com/support?topic=api
- group: company
  title: ''
  type: Blog
  url: https://www.getdietly.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.getdietly.com/account?mode=register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getdietly.com/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getdietly.com/privacy
created: '2026-07-17'
description: Food & nutrition data REST API with 4.7M+ foods, calories, macros, micronutrients, Nutri-Score and EAN/UPC barcode lookup, with confidence-ranked full-text search. Data primarily from Open Food Facts (ODbL) and USDA FoodData Central, EU-hosted, with key-optional read access.
image: https://www.getdietly.com/logo.png
layout: provider
modified: '2026-09-03'
name: DietlyAPI
nav: Providers
network: true
overview: 'DietlyAPI publishes 1 API on the [APIs.io](https://apis.io/) network: DietlyAPI. Tagged areas include Food, Nutrition, Barcodes, open-food-facts, and Health.


  DietlyAPI''s developer surface includes authentication, changelog, sandbox, getting-started guide, API reference, pricing, support, and 19 more developer resources.'
plans:
- name: Dietlyapi Plans Pricing
  plan_count: 4
  slug: dietlyapi-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Dietlyapi Rate Limits
  slug: dietlyapi-rate-limits
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 57.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 43.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 71.4
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 63.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dietlyapi/refs/heads/main/screenshots/dietlyapi-2026-07-25T211947.png
security:
- kind: authentication
  name: Dietlyapi Authentication
  slug: dietlyapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dietlyapi Domain Security
  slug: dietlyapi-domain-security
  summary_line: TLSv1.3
slug: dietlyapi
tags:
- Food
- Nutrition
- Barcodes
- open-food-facts
- Health
- Open Data
website: https://getdietly.com
---
