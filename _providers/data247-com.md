---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_server: documented
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
  score: 16.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Data247 API provides REST endpoints for data services as described in the API User Manual.
  name: Data247 API
  slug: data247-api
- description: 'Data247 API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Data247 API
  slug: data247-com-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/data247-com/plans/data247-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/data247-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/data247-com/rules/data247-com-rules.yml
  title: ''
  type: Spectral
  url: rules/data247-com-rules.yml
- group: design
  href: https://artifacts.apis.io/data247-com/vocabulary/data247-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/data247-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/data247-com/conformance/data247-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/data247-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/data247-com/hosts/data247-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/data247-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/data247-com/vendors/data247-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/data247-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.data247.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.data247.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.data247.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.data247.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.data247.com/login
- group: auth
  href: https://artifacts.apis.io/data247-com/security/data247-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/data247-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.data247.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.data247.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.data247.com/docs/
coverage:
  checked: '2026-11-05'
  detail: The provider's API documentation is only available as HTML pages without a downloadable OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.data247.com/api_user_manual
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Data247 provides an all-in-one data management platform offering secure on-demand data lookup services, data enrichment, validation, and integration solutions for businesses. Their platform enables users to access a wide range of data sources through a simple API, supporting use cases such as data verification, enrichment, and compliance. Data247 emphasizes security, scalability, and ease of integration, positioning itself as a comprehensive solution for data-driven applications.
layout: provider
modified: '2026-11-04'
name: Data247
nav: Providers
network: true
overview: 'Data247 is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Management, Data Enrichment, Validation, and Integration.


  The Data247 catalog on APIs.io includes 1 Spectral governance ruleset.


  Data247''s developer surface includes support, pricing, documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Data247 Com Plans Pricing
  plan_count: 22
  slug: data247-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: Data247 API Rules
  rule_count: 29
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 1
  slug: data247-com-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.8
    catalog_earned_first_party: 12.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 10.4
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
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
  name: Data247 Com Domain Security
  slug: data247-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: data247-com
tags:
- Data Management
- Data Enrichment
- Validation
- Integration
website: https://www.data247.com/
---
