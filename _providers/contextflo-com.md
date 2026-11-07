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
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Contextflo API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Contextflo API
  slug: contextflo-com-api
artifact_total: 4
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contextflo.com/legal/privacy
- group: commercial
  href: https://artifacts.apis.io/contextflo-com/plans/contextflo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextflo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contextflo-com/rules/contextflo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/contextflo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/contextflo-com/vocabulary/contextflo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextflo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/contextflo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/contextflo-com/conformance/contextflo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextflo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextflo-com/llms/contextflo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextflo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/contextflo-com/hosts/contextflo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextflo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextflo-com/vendors/contextflo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextflo-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://contextflo.com/legal/security
- group: start
  title: ''
  type: Sandbox
  url: https://contextflo.com/playground
- group: auth
  href: https://artifacts.apis.io/contextflo-com/security/contextflo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextflo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextflo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://contextflo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://contextflo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://contextflo.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://contextflo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://contextflo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://contextflo.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contextflo.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://contextflo.com/auth/signin?mode=signup
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://contextflo.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Contextflo provides a data analytics platform enabling teams to ask natural language questions to their data using Claude and ChatGPT. It offers reliable answers grounded in business definitions, integrates with various data sources, and presents query details for transparency. Founded in 2024, Contextflo aims to democratize data insights without requiring a dedicated data team.
image: https://contextflo.com/contextflo-og.png
layout: provider
modified: '2026-11-04'
name: Contextflo
nav: Providers
network: true
overview: 'Contextflo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Artificial Intelligence, Data Platform, Customer Service, and Finance.


  The Contextflo catalog on APIs.io includes 1 Spectral governance ruleset.


  Contextflo''s developer surface includes sandbox, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Contextflo Com Plans Pricing
  plan_count: 4
  slug: contextflo-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Contextflo API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: contextflo-com-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 49.3
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextflo Com Domain Security
  slug: contextflo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: contextflo-com
tags:
- Analytics
- Artificial Intelligence
- Data Platform
- Customer Service
- Finance
- Growth
website: https://contextflo.com/
---
