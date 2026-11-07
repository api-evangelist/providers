---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides endpoints for public LinkedIn data such as profiles, companies, posts, and jobs.
  name: Mart API
  slug: mart-api
- description: The Linked In API from Mart.dev — 1 operation(s) for linked in.
  name: Mart.dev Linked In API
  slug: mart-dev-linked-in-api
artifact_total: 8
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://mart.dev/#pricing
- group: commercial
  href: https://artifacts.apis.io/mart-dev/plans/mart-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mart-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mart-dev/rules/mart-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/mart-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/mart-dev/json-ld/mart-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mart-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/mart-dev/vocabulary/mart-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mart-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mart-dev/data-model/mart-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mart-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mart-dev/authentication/mart-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mart-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/mart-dev/conformance/mart-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mart-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/mart-dev/hosts/mart-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mart-dev-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://mart.dev/docs/#quickstart
- group: auth
  href: https://artifacts.apis.io/mart-dev/security/mart-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mart-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mart.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://mart.dev/docs/
- group: start
  title: ''
  type: SignUp
  url: https://mart.dev/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mart.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mart.dev/privacy/
coverage:
  checked: '2026-09-28'
  detail: Documentation is served as rendered HTML pages without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://mart.dev/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Mart.dev provides an unofficial, fast, and inexpensive API that delivers public LinkedIn data such as profiles, companies, posts, and jobs. It offers real‑time access without requiring LinkedIn credentials, delivering results in 1–2 seconds and supporting high request volumes. Free credits are available, and paid plans scale to millions of records.
image: https://mart.dev/logo.png
json_schemas:
- name: GetV1LinkedinResponse
  property_count: 8
  slug: mart-dev-get-v1-linkedin-response
jsonld:
- class_count: 1
  name: Mart Dev Context
  property_count: 8
  slug: mart-dev-context
layout: provider
modified: '2026-09-28'
name: Mart.dev
nav: Providers
network: true
overview: 'Mart.dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Linked In API, and 1 more. Tagged areas include Company, Data, LinkedIn, and Unofficial.


  The Mart.dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mart.dev''s developer surface includes pricing, authentication, getting-started guide, documentation, signup flow, and 11 more developer resources.'
plans:
- name: Mart Dev Plans Pricing
  plan_count: 2
  slug: mart-dev-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Mart.dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: mart-dev-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.2
    catalog_earned_first_party: 8.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 18.3
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 33.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mart-dev/mart-dev-2026-10-11T110818.png
security:
- kind: authentication
  name: Mart Dev Authentication
  slug: mart-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mart Dev Domain Security
  slug: mart-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mart-dev
tags:
- Company
- Data
- LinkedIn
- Unofficial
website: https://mart.dev/
---
