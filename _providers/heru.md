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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Heru API provides tax automation, electronic invoicing, and compliance operations for Mexican fintech users.
  name: Heru API
  slug: heru-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/heru/rules/heru-rules.yml
  title: ''
  type: Spectral
  url: rules/heru-rules.yml
- group: design
  href: https://artifacts.apis.io/heru/json-ld/heru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/heru-context.jsonld
- group: design
  href: https://artifacts.apis.io/heru/vocabulary/heru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/heru-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/heru/data-model/heru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heru-data-model.yml
- group: auth
  href: https://artifacts.apis.io/heru/security/heru-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/heru-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/heru/conformance/heru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/heru/llms/heru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heru-llms.txt
- group: auth
  href: https://artifacts.apis.io/heru/well-known/heru-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/heru-security.txt
- group: auth
  href: https://artifacts.apis.io/heru/well-known/heru-heru-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/heru-heru-security.txt
- group: agent
  href: https://artifacts.apis.io/heru/well-known/heru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heru-well-known.yml
- group: other
  href: https://artifacts.apis.io/heru/hosts/heru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heru-hosts.yml
- group: other
  href: https://artifacts.apis.io/heru/vendors/heru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heru-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.heru.app/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.heru.app/reference/point-of-sale/create-merchant-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://developers.heru.app/
- group: auth
  href: https://artifacts.apis.io/heru/security/heru-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/heru-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/heru/security/heru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heru.app/
- group: company
  title: ''
  type: Blog
  url: https://www.heru.app/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.heru.app/preguntas-frecuentes/
coverage:
  checked: '2026-10-29'
  detail: Developer portal lists endpoints but no OpenAPI/GraphQL/AsyncAPI spec is available.
  evidence:
  - status: 200
    url: https://developers.heru.app/reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Heru is a Mexican fintech platform that automates tax declarations, electronic invoicing, and compliance with the SAT for individuals, freelancers, and businesses. By connecting a user's RFC, Heru calculates, optimizes, and submits monthly tax obligations, offers expert accounting support, and provides plans ranging from basic to RESICO specialization. The service includes automated filing, tax deductions detection, and secure data handling with bank‑grade encryption.
image: https://www.heru.app/heru-logo.svg
jsonld:
- class_count: 44
  name: Heru Context
  property_count: 116
  slug: heru-context
layout: provider
modified: '2026-10-29'
name: Heru
nav: Providers
network: true
overview: 'Heru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Tax Automation, Mexico, Software-as-a-Service, and Accounting.


  The Heru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Heru''s developer surface includes changelog, getting-started guide, documentation, engineering blog, support, and 15 more developer resources.'
plans:
- name: Heru Plans Pricing
  plan_count: 0
  slug: heru-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Heru Rate Limits
  slug: heru-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Heru API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: heru-rules
scopes:
- name: Heru Scopes
  scope_count: 0
  slug: heru-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 17.1
    developer_ergonomics: 17.9
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/heru/heru-2026-11-03T133351.png
security:
- kind: authentication
  name: Heru Authentication
  slug: heru-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Heru Domain Security
  slug: heru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Heru Vulnerability Disclosure
  slug: heru-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: heru
tags:
- Fintech
- Tax Automation
- Mexico
- Software-as-a-Service
- Accounting
website: https://www.heru.app/
---
