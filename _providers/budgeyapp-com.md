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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Budgey provides a developer platform for AI agents via an MCP server. Documentation is at the developers page.
  name: Budgey API
  slug: budgey-api
- description: 'Budgey API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Budgey API
  slug: budgeyapp-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/budgeyapp-com/plans/budgeyapp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/budgeyapp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/budgeyapp-com/rules/budgeyapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/budgeyapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/budgeyapp-com/json-ld/budgeyapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/budgeyapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/budgeyapp-com/vocabulary/budgeyapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/budgeyapp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/budgeyapp-com/data-model/budgeyapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/budgeyapp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/budgeyapp-com/authentication/budgeyapp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/budgeyapp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/budgeyapp-com/conformance/budgeyapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/budgeyapp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/budgeyapp-com/llms/budgeyapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/budgeyapp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/budgeyapp-com/well-known/budgeyapp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/budgeyapp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/budgeyapp-com/hosts/budgeyapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/budgeyapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/budgeyapp-com/vendors/budgeyapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/budgeyapp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.budgeyapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.budgeyapp.com/terms/privacy
- group: start
  title: ''
  type: Login
  url: https://www.budgeyapp.com/api/auth/signin
- group: auth
  href: https://artifacts.apis.io/budgeyapp-com/security/budgeyapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/budgeyapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://budgeyapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.budgeyapp.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.budgeyapp.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.budgeyapp.com/blog
coverage:
  checked: '2026-11-03'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.budgeyapp.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Budgey provides a paycheck‑budgeting app that helps users see what’s left of each pay period at a glance. The service offers budgeting tools, expense tracking, goal setting, and AI‑driven insights, with mobile apps for iOS and Android and a web interface. It supports bank sync, shared budgets for couples, and a developer platform for AI agents via an MCP server.
image: https://budgeyapp.com/og-image.png
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: budgeyapp-com-post-mcp-request
jsonld:
- class_count: 1
  name: Budgeyapp Com Context
  property_count: 3
  slug: budgeyapp-com-context
layout: provider
modified: '2026-11-03'
name: Budgey
nav: Providers
network: true
overview: 'Budgey is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Budgeting, Finance, Personal Finance, and AI Agents.


  The Budgey catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Budgey''s developer surface includes authentication, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Budgeyapp Com Plans Pricing
  plan_count: 2
  slug: budgeyapp-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Budgey API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: budgeyapp-com-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Budgeyapp Com Authentication
  slug: budgeyapp-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Budgeyapp Com Domain Security
  slug: budgeyapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: budgeyapp-com
tags:
- Company
- Budgeting
- Finance
- Personal Finance
- AI Agents
website: https://budgeyapp.com/
---
