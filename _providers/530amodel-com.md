---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.530amodel.com
  baseurl_source: declared
  description: 'Free, stateless projection API for 530A custodial accounts ("Trump Accounts"). Deterministic: identical requests return identical results (and cache at the edge). No auth, no PII, nothing stored. Plea'
  name: 530A Model public API API
  slug: 530a-model-public-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/530amodel-com/rules/530amodel-com-rules.yml
  title: ''
  type: Spectral
  url: rules/530amodel-com-rules.yml
- group: design
  href: https://artifacts.apis.io/530amodel-com/json-ld/530amodel-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/530amodel-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/530amodel-com/vocabulary/530amodel-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/530amodel-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/530amodel-com/data-model/530amodel-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/530amodel-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/530amodel-com/errors/530amodel-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/530amodel-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/530amodel-com/conformance/530amodel-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/530amodel-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/530amodel-com/llms/530amodel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/530amodel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/530amodel-com/well-known/530amodel-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/530amodel-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/530amodel-com/hosts/530amodel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/530amodel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/530amodel-com/vendors/530amodel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/530amodel-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://530amodel.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://530amodel.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://530amodel.com/press
- group: auth
  href: https://artifacts.apis.io/530amodel-com/security/530amodel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/530amodel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://530amodel.com/
created: '2026-11-01'
description: 530A Model is an independent, open‑source public‑good project offering a free calculator for the newly created 530A “Trump Accounts” tax‑advantaged investment accounts for children. It provides an educational, client‑side tool with no data collection, no login, and transparent methodology, linking to its public GitHub repository for the code and API.
image: https://530amodel.com/assets/og/home.png
json_schemas:
- name: Projection
  property_count: 8
  slug: 530amodel-com-projection
- name: Returns
  property_count: 4
  slug: 530amodel-com-returns
- name: Rules
  property_count: 6
  slug: 530amodel-com-rules
- name: Scenario
  property_count: 12
  slug: 530amodel-com-scenario
jsonld:
- class_count: 4
  name: 530Amodel Com Context
  property_count: 25
  slug: 530amodel-com-context
layout: provider
modified: '2026-11-01'
name: 530A Model
nav: Providers
network: true
overview: '530A Model publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: public API API. Tagged areas include Finance, Education, Open Source, Calculator, and PublicGood.


  The 530A Model catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: 530Amodel Com Plans Pricing
  plan_count: 0
  slug: 530amodel-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: 530A Model API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: 530amodel-com-rules
scopes:
- name: 530Amodel Com Scopes
  scope_count: 0
  slug: 530amodel-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 0.0
    discoverability: 67.0
    operational_transparency: 0.0
  previous_composite: 28.7
  provenance:
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 530Amodel Com Authentication
  slug: 530amodel-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 530Amodel Com Domain Security
  slug: 530amodel-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: get-returns
  slug: get-returns
- name: get-rules
  slug: get-rules
- name: project-scenario
  slug: project-scenario
slug: 530amodel-com
tags:
- Finance
- Education
- Open Source
- Calculator
- PublicGood
website: https://530amodel.com/
---
