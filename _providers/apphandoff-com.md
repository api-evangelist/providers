---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
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
  score: 37.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AppHandoff platform
  name: AppHandoff API
  slug: apphandoff-api
artifact_total: 10
asyncapis:
- description: ''
  name: Apphandoff Com Webhooks
  slug: apphandoff-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/apphandoff-com/rules/apphandoff-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apphandoff-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apphandoff-com/json-ld/apphandoff-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apphandoff-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apphandoff-com/vocabulary/apphandoff-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apphandoff-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apphandoff-com/conformance/apphandoff-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apphandoff-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/apphandoff-com/plans/apphandoff-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apphandoff-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/apphandoff-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apphandoff-com/asyncapi/apphandoff-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apphandoff-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/apphandoff-com/data-model/apphandoff-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apphandoff-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apphandoff-com/authentication/apphandoff-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apphandoff-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/apphandoff-com/errors/apphandoff-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apphandoff-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/apphandoff-com/llms/apphandoff-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apphandoff-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/apphandoff-com/well-known/apphandoff-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apphandoff-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apphandoff-com/hosts/apphandoff-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apphandoff-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apphandoff-com/vendors/apphandoff-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apphandoff-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TeamK2K
- group: start
  title: ''
  type: GettingStarted
  url: https://apphandoff.com/blog/github-mcp-server-cursor-setup
- group: docs
  title: ''
  type: APIReference
  url: https://apphandoff.com/docs/
- group: auth
  href: https://artifacts.apis.io/apphandoff-com/security/apphandoff-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apphandoff-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apphandoff.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apphandoff.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.apphandoff.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://apphandoff.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://apphandoff.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apphandoff.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apphandoff.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.apphandoff.com/mcp
  - status: 200
    url: https://apphandoff.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AppHandoff provides a Multi-Agent MCP Coordination platform for AI coding agents, enabling shared direction, decisions, and context across tools like Claude, Cursor, and Codex. The service offers features such as project handoff, shared kanban, authentication via portal, and billing plans, targeting developers building AI-driven applications.
image: https://apphandoff.com/og/root.png
jsonld:
- class_count: 31
  name: Apphandoff Com Context
  property_count: 170
  slug: apphandoff-com-context
layout: provider
modified: '2026-11-01'
name: AppHandoff
nav: Providers
network: true
overview: 'AppHandoff publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Coding Tools, Agent Orchestration, and Multi‑Agent Coordination.


  The AppHandoff catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AppHandoff''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Apphandoff Com Plans Pricing
  plan_count: 1
  slug: apphandoff-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: AppHandoff API Rules
  rule_count: 65
  severity_counts:
    error: 50
    hint: 0
    info: 6
    warn: 9
  slug: apphandoff-com-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 56.8
    catalog_earned_first_party: 8.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 53.2
    developer_ergonomics: 33.9
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 46.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
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
- kind: authentication
  name: Apphandoff Com Authentication
  slug: apphandoff-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Apphandoff Com Domain Security
  slug: apphandoff-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: apphandoff-com-billing-setup
  slug: apphandoff-com-billing-setup
- name: apphandoff-com-check-github-sync-health
  slug: apphandoff-com-check-github-sync-health
- name: apphandoff-com-record-machine-and-run-events
  slug: apphandoff-com-record-machine-and-run-events
slug: apphandoff-com
tags:
- AI Agents
- Coding Tools
- Agent Orchestration
- Multi‑Agent Coordination
website: https://apphandoff.com/
---
