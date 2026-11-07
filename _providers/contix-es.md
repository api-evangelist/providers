---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Spanish invoicing API with Verifactu compliance (RD 1007/2023): customers, invoices with chained hash and QR, expenses, recurring invoices, Facturae/FACe and Modelo 303/349/390 figures.'
  name: Contix API
  slug: contix-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/contix-es/rules/contix-es-rules.yml
  title: ''
  type: Spectral
  url: rules/contix-es-rules.yml
- group: design
  href: https://artifacts.apis.io/contix-es/json-ld/contix-es-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contix-es-context.jsonld
- group: design
  href: https://artifacts.apis.io/contix-es/vocabulary/contix-es-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contix-es-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/contix-es/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/contix-es/conformance/contix-es-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contix-es-conformance.yml
- group: operate
  href: https://artifacts.apis.io/contix-es/rate-limits/contix-es-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/contix-es-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/contix-es/plans/contix-es-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contix-es-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contix-es/data-model/contix-es-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contix-es-data-model.yml
- group: auth
  href: https://artifacts.apis.io/contix-es/authentication/contix-es-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contix-es-authentication.yml
- group: design
  href: https://artifacts.apis.io/contix-es/errors/contix-es-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contix-es-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/contix-es/llms/contix-es-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contix-es-llms.txt
- group: agent
  href: https://artifacts.apis.io/contix-es/well-known/contix-es-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contix-es-well-known.yml
- group: other
  href: https://artifacts.apis.io/contix-es/hosts/contix-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contix-es-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.contix.es/register
- group: auth
  href: https://artifacts.apis.io/contix-es/security/contix-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contix-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contix.es/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.contix.es/
created: '2026-10-29'
description: Contix is a Spanish SaaS platform offering all‑in‑one invoicing for freelancers, self‑employed professionals and small companies. It integrates the Verifactu anti‑fraud standard, supports automatic generation of Spanish tax models (303, 130, 390, 349, 347, 202), expense tracking with AI‑powered OCR, CSV bank import, and connects to AI assistants like ChatGPT, Claude or Cursor via an integrated MCP server. Pricing is €12 per month plus VAT with a 30‑day free trial and no hidden fees.
image: https://contix.es/brand/contix-icon-dark-512.png
jsonld:
- class_count: 118
  name: Contix Es Context
  property_count: 288
  slug: contix-es-context
layout: provider
modified: '2026-10-30'
name: contix-es
nav: Providers
network: true
overview: 'contix-es publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Invoicing, Accounting, Software-as-a-Service, Spain, and Fintech.


  The contix-es catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  contix-es'' developer surface includes authentication, signup flow, and 15 more developer resources.'
plans:
- name: Contix Es Plans Pricing
  plan_count: 1
  slug: contix-es-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Contix Es Rate Limits
  slug: contix-es-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: contix-es API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 3
  slug: contix-es-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 16.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 17.3
    developer_ergonomics: 23.1
    discoverability: 73.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.4
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
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
    score: 38.9
screenshot: https://apis.io/screenshots/contix-es/contix-es-2026-11-03T125214.png
security:
- kind: authentication
  name: Contix Es Authentication
  slug: contix-es-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Contix Es Domain Security
  slug: contix-es-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contix-es
tags:
- Invoicing
- Accounting
- Software-as-a-Service
- Spain
- Fintech
- Automation
website: https://contix.es/
---
