---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Raute Io Agentic Access
  operation_count: 9
  slug: raute-io-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://www.raute.io/api/v1
  baseurl_source: declared
  description: Read drivers and link them to ids in your own system.
  name: raute-io Drivers API
  slug: raute-io-drivers-api
- baseURL: https://www.raute.io/api/v1
  baseurl_source: declared
  description: Create, read, update and cancel delivery orders.
  name: raute-io Orders API
  slug: raute-io-orders-api
- baseURL: https://www.raute.io/api/v1
  baseurl_source: declared
  description: Where an order is, its ETA and its driver.
  name: raute-io Tracking API
  slug: raute-io-tracking-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/raute-io/agentic-access/raute-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/raute-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/raute-io/plans/raute-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/raute-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/raute-io/rules/raute-io-rules.yml
  title: ''
  type: Spectral
  url: rules/raute-io-rules.yml
- group: design
  href: https://artifacts.apis.io/raute-io/json-ld/raute-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/raute-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/raute-io/vocabulary/raute-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/raute-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/raute-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/raute-io/data-model/raute-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/raute-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/raute-io/conventions/raute-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/raute-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/raute-io/authentication/raute-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/raute-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/raute-io/scopes/raute-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/raute-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/raute-io/errors/raute-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/raute-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/raute-io/conformance/raute-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/raute-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/raute-io/llms/raute-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/raute-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/raute-io/well-known/raute-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/raute-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/raute-io/hosts/raute-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raute-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/raute-io/vendors/raute-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/raute-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.raute.io/security/
- group: docs
  title: ''
  type: APIReference
  url: https://www.raute.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/raute-io/security/raute-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/raute-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/raute-io/security/raute-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raute-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://raute.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.raute.io/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.raute.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.raute.io/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.raute.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.raute.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/raute-io
- group: operate
  title: ''
  type: Roadmap
  url: https://www.raute.io/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.raute.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.raute.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.raute.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raute.io/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.raute.io/postman
created: '2026-10-30'
description: Raute provides AI‑powered route planning and delivery management software for fleets of any size. Its platform uses artificial intelligence to read orders, optimise driver routes, and offer live tracking, supporting a free 7‑day trial without requiring a credit card. Founded in 2025, Raute serves US delivery operations across sectors such as medical equipment, food, and courier services, integrating with popular e‑commerce and logistics tools.
image: https://www.raute.io/logo.png
json_schemas:
- name: Driver
  property_count: 6
  slug: raute-io-driver
- name: NewOrder
  property_count: 14
  slug: raute-io-new-order
- name: OrderPatch
  property_count: 10
  slug: raute-io-order-patch
- name: Order
  property_count: 31
  slug: raute-io-order
- name: Tracking
  property_count: 7
  slug: raute-io-tracking
jsonld:
- class_count: 7
  name: Raute Io Context
  property_count: 36
  slug: raute-io-context
layout: provider
modified: '2026-10-30'
name: raute-io
nav: Providers
network: true
overview: 'raute-io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Drivers API, Orders API, and Tracking API. Tagged areas include Company, Logistics, Delivery, Route Planning, and Artificial Intelligence.


  The raute-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  raute-io''s developer surface includes authentication, API reference, documentation, getting-started guide, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Raute Io Plans Pricing
  plan_count: 3
  slug: raute-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Raute Io Rate Limits
  slug: raute-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: raute-io API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: raute-io-rules
scopes:
- name: Raute Io Scopes
  scope_count: 0
  slug: raute-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 69.0
    developer_ergonomics: 43.3
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 68.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 66.7
screenshot: https://apis.io/screenshots/raute-io/raute-io-2026-11-03T141940.png
security:
- kind: authentication
  name: Raute Io Authentication
  slug: raute-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Raute Io Domain Security
  slug: raute-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Raute Io Vulnerability Disclosure
  slug: raute-io-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: orders
  slug: raute-io-orders-skill
slug: raute-io
tags:
- Company
- Logistics
- Delivery
- Route Planning
- Artificial Intelligence
- Fleet Management
website: https://raute.io/
---
