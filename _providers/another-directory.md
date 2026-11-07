---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Another Directory Agentic Access
  operation_count: 2
  slug: another-directory-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://another.directory
  baseurl_source: declared
  description: The Categories API from Another Directory — 1 operation(s) for categories.
  name: Another Directory Categories API
  slug: another-directory-categories-api
- baseURL: https://another.directory
  baseurl_source: declared
  description: The Submissions API from Another Directory — 1 operation(s) for submissions.
  name: Another Directory Submissions API
  slug: another-directory-submissions-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/another-directory/agentic-access/another-directory-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/another-directory-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/another-directory/plans/another-directory-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/another-directory-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/another-directory/rules/another-directory-rules.yml
  title: ''
  type: Spectral
  url: rules/another-directory-rules.yml
- group: design
  href: https://artifacts.apis.io/another-directory/json-ld/another-directory-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/another-directory-context.jsonld
- group: design
  href: https://artifacts.apis.io/another-directory/vocabulary/another-directory-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/another-directory-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/another-directory/data-model/another-directory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/another-directory-data-model.yml
- group: design
  href: https://artifacts.apis.io/another-directory/errors/another-directory-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/another-directory-problem-types.yml
- group: design
  href: https://artifacts.apis.io/another-directory/conformance/another-directory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/another-directory-conformance.yml
- group: agent
  href: https://artifacts.apis.io/another-directory/llms/another-directory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/another-directory-llms.txt
- group: other
  href: https://artifacts.apis.io/another-directory/hosts/another-directory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/another-directory-hosts.yml
- group: other
  href: https://artifacts.apis.io/another-directory/vendors/another-directory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/another-directory-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://another.directory/users/log-in
- group: docs
  title: ''
  type: APIReference
  url: https://another.directory/llms.txt
- group: auth
  href: https://artifacts.apis.io/another-directory/security/another-directory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/another-directory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://another.directory
- group: docs
  title: ''
  type: Documentation
  url: https://another.directory/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://another.directory/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://another.directory/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://another.directory/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://another.directory/about
- group: operate
  title: ''
  type: Support
  url: mailto:hello@another.directory
created: '2026-11-05'
description: Another Directory is a directory of new software tools, offering listings across 57 tools in 21 categories. It provides free and paid (Pro) listings, with AI‑generated summaries and optional badge links. Operators can submit tools, manage listings, and access an API for automated submissions. Based in Poland, the service includes pricing details, terms of use, and a privacy policy.
image: https://another.directory/images/og-default.png
json_schemas:
- name: CategoryList
  property_count: 1
  slug: another-directory-category-list
- name: Submission
  property_count: 11
  slug: another-directory-submission
jsonld:
- class_count: 7
  name: Another Directory Context
  property_count: 33
  slug: another-directory-context
layout: provider
modified: '2026-11-05'
name: Another Directory
nav: Providers
network: true
overview: 'Another Directory publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Categories API and Submissions API. Tagged areas include Company.


  The Another Directory catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Another Directory''s developer surface includes API reference, documentation, pricing, getting-started guide, support, and 16 more developer resources.'
plans:
- name: Another Directory Plans Pricing
  plan_count: 5
  slug: another-directory-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Another Directory API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: another-directory-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Another Directory Domain Security
  slug: another-directory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: another-directory
tags:
- Company
website: https://another.directory
---
