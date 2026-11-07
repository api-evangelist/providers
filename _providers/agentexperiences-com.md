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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AXO implementation guides by role – developer documentation for Agent Experiences.
  name: Agent Experiences API
  slug: agent-experiences-api
- description: 'Agent Experiences API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Agent Experiences API
  slug: agentexperiences-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/agentexperiences-com/rules/agentexperiences-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentexperiences-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentexperiences-com/json-ld/agentexperiences-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentexperiences-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentexperiences-com/vocabulary/agentexperiences-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentexperiences-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentexperiences-com/data-model/agentexperiences-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentexperiences-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentexperiences-com/conformance/agentexperiences-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentexperiences-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentexperiences-com/llms/agentexperiences-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentexperiences-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentexperiences-com/hosts/agentexperiences-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentexperiences-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentexperiences-com/vendors/agentexperiences-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentexperiences-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentexperiences-com/security/agentexperiences-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentexperiences-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentexperiences.com/
- group: company
  title: ''
  type: Blog
  url: https://www.agentexperiences.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentexperiences.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentexperiences.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentexperiences.com/websites/guides/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentexperiences.com/overview
coverage:
  checked: '2026-11-01'
  detail: Public developer guides exist but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://www.agentexperiences.com/websites/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agent Experiences provides educational resources and consulting on Agent Experience Optimization (AXO) and Agentic Experience Design (AXD). Published by PrimeCo, the site offers guides, scoring tools, and analysis to help websites and applications become readable and actionable by AI agents, improving AI citation and discovery. It covers principles, architecture, and practical steps for optimizing content, structuring data, and designing interfaces that enable intelligent agents to interact with digital services on behalf of users.
image: https://www.agentexperiences.com/images/logo-head.svg
json_schemas:
- name: GetApiV1UsersUseridResponse
  property_count: 3
  slug: agentexperiences-com-get-api-v1-users-userid-response
jsonld:
- class_count: 1
  name: Agentexperiences Com Context
  property_count: 3
  slug: agentexperiences-com-context
layout: provider
modified: '2026-10-31'
name: Agent Experiences
nav: Providers
network: true
overview: 'Agent Experiences is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agent Experience, Optimization, Consulting, and Technology.


  The Agent Experiences catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Experiences'' developer surface includes engineering blog, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Agentexperiences Com Plans Pricing
  plan_count: 0
  slug: agentexperiences-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Agentexperiences Com Rate Limits
  slug: agentexperiences-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Agent Experiences API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentexperiences-com-rules
scopes:
- name: Agentexperiences Com Scopes
  scope_count: 0
  slug: agentexperiences-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 23.4
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentexperiences Com Authentication
  slug: agentexperiences-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentexperiences Com Domain Security
  slug: agentexperiences-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentexperiences-com
tags:
- Artificial Intelligence
- Agent Experience
- Optimization
- Consulting
- Technology
website: https://agentexperiences.com/
---
