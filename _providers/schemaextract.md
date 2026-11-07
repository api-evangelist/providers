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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: The Extract API from SchemaExtract — 1 operation(s) for extract.
  name: SchemaExtract Extract API
  slug: schemaextract-extract-api
- baseURL: /
  baseurl_source: spec
  description: The Health API from SchemaExtract — 1 operation(s) for health.
  name: SchemaExtract Health API
  slug: schemaextract-health-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/schemaextract/security/schemaextract-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/schemaextract-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/schemaextract/authentication/schemaextract-authentication.yml
  title: ''
  type: Authentication
  url: authentication/schemaextract-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://schemaextract.shop/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://schemaextract.shop/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://schemaextract.shop/pricing
- group: start
  title: ''
  type: Login
  url: https://schemaextract.shop/login
- group: operate
  title: ''
  type: Support
  url: https://schemaextract.shop/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://schemaextract.shop/status
- group: design
  href: https://artifacts.apis.io/schemaextract/lifecycle/schemaextract-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/schemaextract-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/schemaextract/errors/schemaextract-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/schemaextract-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/schemaextract/rate-limits/schemaextract-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/schemaextract-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/schemaextract/plans/schemaextract-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/schemaextract-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/schemaextract/sandbox/schemaextract-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/schemaextract-sandbox.yml
- group: design
  href: https://artifacts.apis.io/schemaextract/conventions/schemaextract-conventions.yml
  title: ''
  type: Conventions
  url: conventions/schemaextract-conventions.yml
- group: design
  href: https://artifacts.apis.io/schemaextract/data-model/schemaextract-data-model.yml
  title: ''
  type: DataModel
  url: data-model/schemaextract-data-model.yml
- group: design
  href: https://artifacts.apis.io/schemaextract/conformance/schemaextract-conformance.yml
  title: ''
  type: Conformance
  url: conformance/schemaextract-conformance.yml
- group: agent
  href: https://artifacts.apis.io/schemaextract/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/schemaextract/overlays/schemaextract-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/schemaextract-openapi-overlay.yaml
created: '2026-09-19'
description: A document-to-JSON extraction service. Upload a PDF or image, pick a preset or paste a JSON schema, and get typed fields back — vendor, totals, line items, packages, containers. Supports invoice, packing list, bank statement, and bill of lading presets plus custom schemas.
finops:
- has_sources: true
  method: derived
  name: Schemaextract Finops
  primary_unit: ''
  service_category: ''
  slug: schemaextract-finops
  template: true
layout: provider
modified: '2026-09-20'
name: SchemaExtract
nav: Providers
network: true
overview: 'SchemaExtract publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Extract API and Health API. Tagged areas include Document AI, Intelligent Document Processing, Data Extraction, PDF/OCR-to-JSON, and Invoice & AP automation.


  The SchemaExtract catalog on APIs.io includes 1 Spectral governance ruleset.


  SchemaExtract''s developer surface includes authentication, pricing, support, sandbox, and 14 more developer resources.'
plans:
- name: Schemaextract Plans Pricing
  plan_count: 3
  slug: schemaextract-plans-pricing
- name: Schemaextract Price Estimates
  plan_count: 0
  slug: schemaextract-price-estimates
random_paper: 20
rate_limits:
- limit_count: 4
  name: Schemaextract Rate Limits
  slug: schemaextract-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: SchemaExtract API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: schemaextract-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.5
    catalog_earned_first_party: 24.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 36.3
    discoverability: 55.4
    operational_transparency: 39.5
  previous_composite: 45.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/schemaextract/schemaextract-2026-10-11T125535.png
security:
- kind: authentication
  name: Schemaextract Authentication
  slug: schemaextract-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Schemaextract Domain Security
  slug: schemaextract-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: extract-document-to-json
  slug: schemaextract-extract-document
slug: schemaextract
tags:
- Document AI
- Intelligent Document Processing
- Data Extraction
- PDF/OCR-to-JSON
- Invoice & AP automation
- Logistics/freight
- Fintech
- Developer API
website: https://schemaextract.shop/
---
