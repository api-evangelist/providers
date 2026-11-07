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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bijack Ir Agentic Access
  operation_count: 1
  slug: bijack-ir-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://bijack.ir
  baseurl_source: declared
  description: The Loadboard API from Bijack — 1 operation(s) for loadboard.
  name: Bijack Loadboard API
  slug: bijack-ir-loadboard-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bijack-ir/agentic-access/bijack-ir-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bijack-ir-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/rules/bijack-ir-rules.yml
  title: ''
  type: Spectral
  url: rules/bijack-ir-rules.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/json-ld/bijack-ir-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bijack-ir-context.jsonld
- group: design
  href: https://artifacts.apis.io/bijack-ir/vocabulary/bijack-ir-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bijack-ir-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bijack-ir/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/data-model/bijack-ir-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bijack-ir-data-model.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/conventions/bijack-ir-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bijack-ir-conventions.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/conventions/bijack-ir-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bijack-ir-conventions.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/errors/bijack-ir-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bijack-ir-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bijack-ir/conformance/bijack-ir-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bijack-ir-conformance.yml
- group: other
  href: https://artifacts.apis.io/bijack-ir/hosts/bijack-ir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bijack-ir-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://bijack.ir/loadboard/login
- group: auth
  href: https://artifacts.apis.io/bijack-ir/authentication/bijack-ir-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bijack-ir-authentication.yml
- group: docs
  href: https://artifacts.apis.io/bijack-ir/openapi/bijack-ir-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/bijack-ir-openapi.yml
- group: auth
  href: https://artifacts.apis.io/bijack-ir/security/bijack-ir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bijack-ir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bijack.ir/
created: '2026-11-02'
description: بیجک یک بستر اعلام بار آزاد و دسترسی به سالن‌های اعلام بار است. اطلاعات بارها توسط کاربران ثبت یا منتشر می‌شود و لازم است پیش از هر توافق، هویت طرف مقابل، مشخصات بار، کرایه، بیمه، مجوز حمل و بارنامه از مسیرهای قانونی بررسی شود. این پلتفرم به صاحبان بار، اعلام‌کنندگان بار، شرکت‌های حمل‌ونقل و رانندگان کمک می‌کند بارها را ساختاریافته‌تر ثبت، جست‌وجو و پیگیری کنند.
jsonld:
- class_count: 4
  name: Bijack Ir Context
  property_count: 36
  slug: bijack-ir-context
layout: provider
modified: '2026-11-02'
name: Bijack
nav: Providers
network: true
overview: 'Bijack publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Loadboard API. Tagged areas include Logistics, Freight, Transportation, Marketplace, and Iran.


  The Bijack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bijack''s developer surface includes authentication and 15 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Bijack API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: bijack-ir-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 13.7
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bijack Ir Authentication
  slug: bijack-ir-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bijack Ir Domain Security
  slug: bijack-ir-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: shipper-leads
  slug: bijack-ir-shipper-leads
slug: bijack-ir
tags:
- Logistics
- Freight
- Transportation
- Marketplace
- Iran
website: https://bijack.ir/
---
