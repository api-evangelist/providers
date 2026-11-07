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
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BugiaData provides a fake data generation API as described in their documentation.
  name: BugiaData API
  slug: bugiadata-api
- baseURL: http://localhost:5000
  baseurl_source: declared
  description: A production-ready, subscription-based API service that generates locale-specific fake data
  name: BugiaData Api API
  slug: bugiadata-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/bugiadata-com/rules/bugiadata-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bugiadata-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bugiadata-com/vocabulary/bugiadata-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bugiadata-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bugiadata-com/conformance/bugiadata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bugiadata-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/bugiadata-com/plans/bugiadata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bugiadata-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bugiadata-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/bugiadata-com/authentication/bugiadata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bugiadata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bugiadata-com/errors/bugiadata-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bugiadata-com-problem-types.yml
- group: other
  href: https://artifacts.apis.io/bugiadata-com/hosts/bugiadata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bugiadata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bugiadata-com/vendors/bugiadata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bugiadata-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://bugiadata.com/login
- group: company
  title: ''
  type: Blog
  url: https://bugiadata.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://bugiadata.com/mcp
- group: auth
  href: https://artifacts.apis.io/bugiadata-com/security/bugiadata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugiadata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bugiadata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bugiadata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://bugiadata.com/pricing
created: '2026-11-03'
description: BugiaData provides high-quality fake relational data for AI agents and developers. It offers an API with over 100 locales, generating multi-table data with foreign keys in a single REST call. Free tier and paid plans are available, targeting testing, QA, and rapid prototyping use cases.
image: https://bugiadata.com/static/img/logo.png
layout: provider
modified: '2026-11-03'
name: BugiaData
nav: Providers
network: true
overview: 'BugiaData publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api API, and 1 more. Tagged areas include Data, Artificial Intelligence, Testing, and Fake Data.


  The BugiaData catalog on APIs.io includes 1 Spectral governance ruleset.


  BugiaData''s developer surface includes authentication, engineering blog, getting-started guide, documentation, pricing, and 11 more developer resources.'
plans:
- name: Bugiadata Com Plans Pricing
  plan_count: 3
  slug: bugiadata-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: BugiaData API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 1
  slug: bugiadata-com-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 29.7
    developer_ergonomics: 30.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bugiadata Com Authentication
  slug: bugiadata-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bugiadata Com Domain Security
  slug: bugiadata-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bugiadata-com
tags:
- Data
- Artificial Intelligence
- Testing
- Fake Data
website: https://bugiadata.com/
---
