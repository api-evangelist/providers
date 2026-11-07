---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.getdietly.com
  baseurl_source: declared
  description: Read-only nutrition data from a worldwide catalog. Public reads work without a key at 30 requests/minute per IP; send a Bearer key for account-level paid limits.
  name: DietlyAPI Foods API
  slug: dietlyapi-foods-api
- baseURL: https://api.getdietly.com
  baseurl_source: declared
  description: Service health.
  name: DietlyAPI Meta API
  slug: dietlyapi-meta-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://getdietly.com
- group: auth
  href: https://artifacts.apis.io/dietlyapi/security/dietlyapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dietlyapi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dietlyapi/authentication/dietlyapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dietlyapi-authentication.yml
- group: operate
  href: https://artifacts.apis.io/dietlyapi/changelog/dietlyapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dietlyapi-changelog.yml
- group: design
  href: https://artifacts.apis.io/dietlyapi/lifecycle/dietlyapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dietlyapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.getdietly.com/uptime
- group: design
  href: https://artifacts.apis.io/dietlyapi/errors/dietlyapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dietlyapi-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/dietlyapi/rate-limits/dietlyapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dietlyapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dietlyapi/plans/dietlyapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dietlyapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dietlyapi/conventions/dietlyapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dietlyapi-conventions.yml
- group: start
  href: https://artifacts.apis.io/dietlyapi/sandbox/dietlyapi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dietlyapi-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/dietlyapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/dietlyapi/overlays/dietlyapi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dietlyapi-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/dietlyapi/data-model/dietlyapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dietlyapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/dietlyapi/conformance/dietlyapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dietlyapi-conformance.yml
- group: build
  href: https://artifacts.apis.io/dietlyapi/packages/dietlyapi-packages.yml
  title: ''
  type: Packages
  url: packages/dietlyapi-packages.yml
- group: agent
  href: https://artifacts.apis.io/dietlyapi/llms/dietlyapi-llms.txt
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
finops:
- has_sources: true
  method: derived
  name: Dietlyapi Finops
  primary_unit: subscription
  service_category: ''
  slug: dietlyapi-finops
  template: false
image: https://www.getdietly.com/logo.png
layout: provider
modified: '2026-09-03'
name: DietlyAPI
nav: Providers
network: true
overview: 'DietlyAPI publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Foods API and Meta API. Tagged areas include Food, Nutrition, Barcodes, open-food-facts, and Health.


  The DietlyAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  DietlyAPI''s developer surface includes authentication, changelog, sandbox, getting-started guide, API reference, pricing, support, and 19 more developer resources.'
plans:
- name: Dietlyapi Plans Pricing
  plan_count: 4
  slug: dietlyapi-plans-pricing
- name: Dietlyapi Price Estimates
  plan_count: 0
  slug: dietlyapi-price-estimates
random_paper: 5
rate_limits:
- limit_count: 4
  name: Dietlyapi Rate Limits
  slug: dietlyapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: DietlyAPI API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: dietlyapi-rules
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 49.3
    developer_ergonomics: 66.1
    discoverability: 67.9
    operational_transparency: 63.2
  previous_composite: 60.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/dietlyapi/dietlyapi-2026-07-25T211947.png
security:
- kind: authentication
  name: Dietlyapi Authentication
  slug: dietlyapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dietlyapi Domain Security
  slug: dietlyapi-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: dietly-barcode-lookup
  slug: dietlyapi-barcode-lookup
- name: dietly-food-discovery
  slug: dietlyapi-food-discovery
- name: dietly-food-search
  slug: dietlyapi-food-search
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
