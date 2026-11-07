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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Aunoo Skills is a thin MCP / REST wrapper over Aunoo's tool palette, providing sentiment analysis, forecasting, and other AI-driven insights.
  name: Aunoo Skills API
  slug: aunoo-skills-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/aunoo-ai/plans/aunoo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aunoo-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aunoo-ai/rules/aunoo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aunoo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aunoo-ai/json-ld/aunoo-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aunoo-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aunoo-ai/vocabulary/aunoo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aunoo-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aunoo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aunoo-ai/data-model/aunoo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aunoo-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/aunoo-ai/errors/aunoo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aunoo-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aunoo-ai/conformance/aunoo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aunoo-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aunoo-ai/llms/aunoo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aunoo-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/aunoo-ai/well-known/aunoo-ai-saas-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aunoo-ai-saas-security.txt
- group: auth
  href: https://artifacts.apis.io/aunoo-ai/well-known/aunoo-ai-agentic-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aunoo-ai-agentic-security.txt
- group: agent
  href: https://artifacts.apis.io/aunoo-ai/well-known/aunoo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aunoo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aunoo-ai/hosts/aunoo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aunoo-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aunoo-ai/security/aunoo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aunoo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aunoo.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://aunoo.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AuNooAI
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agentic.aunoo.ai/openapi.json
  - status: null
    url: https://saas.aunoo.ai/openapi.json
  - status: 401
    url: https://agentic.aunoo.ai/mcp
  - status: 401
    url: https://saas.aunoo.ai/mcp
  - status: 401
    url: https://agentic.aunoo.ai/api/graphql
  - status: 401
    url: https://saas.aunoo.ai/api/graphql
  reason: partner-login
  state: gated
created: '2026-11-02'
description: AuNoo AI provides open strategic intelligence solutions, offering AI‑driven analytics, risk assessment, and narrative generation for organizations. Their platform delivers real‑time insights, customizable dashboards, and open‑source tools to help users understand emerging trends and make data‑informed decisions.
image: https://framerusercontent.com/images/30z0pYhLwODVMgkumpdpg5SEj4.png
jsonld:
- class_count: 2
  name: Aunoo Ai Context
  property_count: 6
  slug: aunoo-ai-context
layout: provider
modified: '2026-11-02'
name: AuNoo AI
nav: Providers
network: true
overview: 'AuNoo AI publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Intelligence, Software-as-a-Service, and Open Source.


  The AuNoo AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AuNoo AI''s developer surface includes pricing and 16 more developer resources.'
plans:
- name: Aunoo Ai Plans Pricing
  plan_count: 3
  slug: aunoo-ai-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: AuNoo AI API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 1
  slug: aunoo-ai-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 1.8
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 21.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aunoo Ai Domain Security
  slug: aunoo-ai-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: aunoo-ai-run-workspace-tool
  slug: aunoo-ai-run-workspace-tool
slug: aunoo-ai
tags:
- Artificial Intelligence
- Analytics
- Intelligence
- Software-as-a-Service
- Open Source
website: https://aunoo.ai/
---
