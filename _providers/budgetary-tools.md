---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pre-inference token-spend estimates for LLM queries.
  name: Budgetary API
  slug: budgetary-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/budgetary-tools/rules/budgetary-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/budgetary-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/budgetary-tools/json-ld/budgetary-tools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/budgetary-tools-context.jsonld
- group: design
  href: https://artifacts.apis.io/budgetary-tools/vocabulary/budgetary-tools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/budgetary-tools-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/budgetary-tools/conformance/budgetary-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/budgetary-tools-conformance.yml
- group: design
  href: https://artifacts.apis.io/budgetary-tools/data-model/budgetary-tools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/budgetary-tools-data-model.yml
- group: design
  href: https://artifacts.apis.io/budgetary-tools/errors/budgetary-tools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/budgetary-tools-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/budgetary-tools/well-known/budgetary-tools-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/budgetary-tools-security.txt
- group: agent
  href: https://artifacts.apis.io/budgetary-tools/well-known/budgetary-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/budgetary-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/budgetary-tools/hosts/budgetary-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/budgetary-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/budgetary-tools/vendors/budgetary-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/budgetary-tools-vendors.yml
- group: build
  href: https://artifacts.apis.io/budgetary-tools/packages/budgetary-tools-packages.yml
  title: ''
  type: SDKs
  url: packages/budgetary-tools-packages.yml
- group: build
  href: https://artifacts.apis.io/budgetary-tools/packages/budgetary-tools-packages.yml
  title: ''
  type: Packages
  url: packages/budgetary-tools-packages.yml
- group: auth
  href: https://artifacts.apis.io/budgetary-tools/security/budgetary-tools-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/budgetary-tools-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/budgetary-tools/security/budgetary-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/budgetary-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://budgetary.tools/
- group: docs
  title: ''
  type: APIReference
  url: https://api.budgetary.tools/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://budgetary.tools/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://budgetary.tools/terms
- group: commercial
  title: ''
  type: License
  url: https://budgetary.tools/license
- group: auth
  title: ''
  type: Security
  url: https://budgetary.tools/.well-known/security.txt
created: '2026-11-03'
description: Budgetary provides a pre‑flight token‑spend estimate tool for AI coding agents. The service returns a token range, scenario, and confidence signal before a coding task runs, and reports "no read" when it lacks coverage. It is offered free and without usage limits, and integrates via an MCP server or plugins for agents such as Claude Code, VS Code, and others.
jsonld:
- class_count: 33
  name: Budgetary Tools Context
  property_count: 93
  slug: budgetary-tools-context
layout: provider
modified: '2026-11-03'
name: Budgetary
nav: Providers
network: true
overview: 'Budgetary publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include AI Coding, MCP Server, and Free Tier.


  The Budgetary catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Budgetary''s developer surface includes API reference, getting-started guide, and 18 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Budgetary API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: budgetary-tools-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    conformance: derived
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
  name: Budgetary Tools Domain Security
  slug: budgetary-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Budgetary Tools Vulnerability Disclosure
  slug: budgetary-tools-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: budgetary-tools
tags:
- AI Coding
- MCP Server
- Free Tier
website: https://budgetary.tools/
---
