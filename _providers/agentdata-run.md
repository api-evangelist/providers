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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API providing company data for AI agents, including company profiles, tools, and contacts.
  name: AgentData API
  slug: agentdata-api
- baseURL: https://agentdata.run
  baseurl_source: declared
  description: 'AgentData API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentData API
  slug: agentdata-run-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/agentdata-run/plans/agentdata-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdata-run-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentdata-run/rules/agentdata-run-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdata-run-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdata-run/vocabulary/agentdata-run-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdata-run-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentdata-run/conformance/agentdata-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdata-run-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentdata-run/llms/agentdata-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdata-run-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentdata-run/well-known/agentdata-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdata-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentdata-run/hosts/agentdata-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdata-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentdata-run/vendors/agentdata-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentdata-run-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentdata-run/packages/agentdata-run-packages.yml
  title: ''
  type: SDKs
  url: packages/agentdata-run-packages.yml
- group: build
  href: https://artifacts.apis.io/agentdata-run/packages/agentdata-run-packages.yml
  title: ''
  type: Packages
  url: packages/agentdata-run-packages.yml
- group: auth
  href: https://artifacts.apis.io/agentdata-run/security/agentdata-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdata-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdata.run/
- group: docs
  title: ''
  type: Documentation
  url: https://useagentdata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://useagentdata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://useagentdata.com/signup
- group: company
  title: ''
  type: About
  url: https://useagentdata.com/about
- group: company
  title: ''
  type: Blog
  url: https://useagentdata.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useagentdata.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useagentdata.com/legal/terms
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://agentdata.run/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AgentData provides a platform that aggregates company data for AI agents and growth teams, showing what a company does, the tools it runs, how to reach it, and recent changes. Built by Nick and Duda Timms in the UK, the service offers live data, pricing information, documentation, and APIs, with a focus on transparency and data quality.
layout: provider
modified: '2026-10-31'
name: AgentData
nav: Providers
network: true
overview: 'AgentData is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The AgentData catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentData''s developer surface includes documentation, pricing, signup flow, engineering blog, and 15 more developer resources.'
plans:
- name: Agentdata Run Plans Pricing
  plan_count: 3
  slug: agentdata-run-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AgentData API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agentdata-run-rules
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.8
    catalog_earned_first_party: 12.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 12.9
    developer_ergonomics: 13.1
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentdata Run Domain Security
  slug: agentdata-run-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentdata-run
tags:
- Company
website: https://agentdata.run/
---
