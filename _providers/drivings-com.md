---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Drivings Com Agentic Access
  operation_count: 4
  slug: drivings-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://drivings.com
  baseurl_source: declared
  description: Public catalog and evidence retrieval with no side effects.
  name: Drivings Discovery API
  slug: drivings-com-discovery-api
- baseURL: https://drivings.com
  baseurl_source: declared
  description: Deterministic computation that is not persisted.
  name: Drivings Planning API
  slug: drivings-com-planning-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/drivings-com/agentic-access/drivings-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drivings-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/drivings-com/plans/drivings-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drivings-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/rules/drivings-com-rules.yml
  title: ''
  type: Spectral
  url: rules/drivings-com-rules.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/json-ld/drivings-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/drivings-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/drivings-com/vocabulary/drivings-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/drivings-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/data-model/drivings-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drivings-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/conventions/drivings-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/drivings-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/conventions/drivings-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drivings-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/errors/drivings-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drivings-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drivings-com/conformance/drivings-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drivings-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drivings-com/llms/drivings-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drivings-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/drivings-com/well-known/drivings-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drivings-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/drivings-com/hosts/drivings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drivings-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/drivings-com/vendors/drivings-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drivings-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drivings.com/terms
- group: operate
  title: ''
  type: Support
  url: https://drivings.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drivings.com/privacy
- group: start
  title: ''
  type: Login
  url: https://drivings.com/login
- group: company
  title: ''
  type: Blog
  url: https://drivings.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://drivings.com/help/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.drivings.com/
- group: docs
  title: ''
  type: APIReference
  url: https://drivings.com/developers
- group: auth
  href: https://artifacts.apis.io/drivings-com/scopes/drivings-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/drivings-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/drivings-com/authentication/drivings-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drivings-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/drivings-com/security/drivings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drivings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drivings.com/
created: '2026-11-05'
description: Drivings helps learners prepare for driving tests with practice questions, mock tests and audio lessons. Founded in 2024, the UK‑based platform serves learners in Great Britain and the United States, offering hazard‑perception training, theory‑test practice, and comprehensive study resources to boost confidence and pass rates.
image: https://drivings.com/opengraph-image
json_schemas:
- name: Capabilities
  property_count: 8
  slug: drivings-com-capabilities
- name: StudyOptions
  property_count: 5
  slug: drivings-com-study-options
- name: StudyPlanInput
  property_count: 5
  slug: drivings-com-study-plan-input
- name: StudyPlanPreview
  property_count: 9
  slug: drivings-com-study-plan-preview
- name: TestCentreSearch
  property_count: 8
  slug: drivings-com-test-centre-search
jsonld:
- class_count: 10
  name: Drivings Com Context
  property_count: 33
  slug: drivings-com-context
layout: provider
modified: '2026-11-05'
name: Drivings
nav: Providers
network: true
overview: 'Drivings publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API and Planning API. Tagged areas include Company, Driving, Education, United Kingdom, and US.


  The Drivings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Drivings'' developer surface includes support, engineering blog, getting-started guide, documentation, API reference, authentication, and 20 more developer resources.'
plans:
- name: Drivings Com Plans Pricing
  plan_count: 2
  slug: drivings-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Drivings API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: drivings-com-rules
scopes:
- name: Drivings Com Scopes
  scope_count: 3
  slug: drivings-com-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 66.7
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Drivings Com Authentication
  slug: drivings-com-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Drivings Com Domain Security
  slug: drivings-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drivings-com
tags:
- Company
- Driving
- Education
- United Kingdom
- US
website: https://drivings.com/
---
