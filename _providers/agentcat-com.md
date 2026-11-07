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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AgentCat API provides analytics and observability endpoints for Claude and ChatGPT agents. Documentation is at https://docs.agentcat.com.
  name: AgentCat API
  slug: agentcat-api
- baseURL: https://api.agentcat.com
  baseurl_source: declared
  description: 'AgentCat API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentCat API
  slug: agentcat-com-api
artifact_total: 5
common:
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentcat.com/languages/go/reference
- group: commercial
  href: https://artifacts.apis.io/agentcat-com/plans/agentcat-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentcat-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentcat-com/rules/agentcat-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentcat-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentcat-com/vocabulary/agentcat-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentcat-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentcat-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentcat-com/conformance/agentcat-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcat-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentcat-com/llms/agentcat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentcat-com/a2a/agentcat-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentcat-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentcat-com/well-known/agentcat-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentcat-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentcat-com/hosts/agentcat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcat-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcat-com/vendors/agentcat-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcat-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.agentcat.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentcathq
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentcat.com/quickstart
- group: auth
  href: https://artifacts.apis.io/agentcat-com/security/agentcat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentcat.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentcat.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://agentcat.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcat.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcat.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agentcat.com
coverage:
  checked: '2026-11-01'
  detail: Docs site returns a JavaScript shell, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.agentcat.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AgentCat provides analytics and observability for Claude connectors and ChatGPT applications. It offers session tracing, intent detection, and issue identification for AI agents, helping developers debug, monitor, and improve agent performance. Trusted by fast‑growing AI companies, AgentCat aims to enhance the agent experience through detailed session replay, tool‑call insights, and comprehensive dashboards.
image: https://agentcat.com/opengraph-image.png?1aedaa36f1c06f32
layout: provider
modified: '2026-10-31'
name: AgentCat
nav: Providers
network: true
overview: 'AgentCat is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Observability, Agent Experience, and Company.


  The AgentCat catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentCat''s developer surface includes API reference, getting-started guide, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Agentcat Com Plans Pricing
  plan_count: 4
  slug: agentcat-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: AgentCat API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: agentcat-com-rules
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 51.3
    contract_governance: 35.6
    contract_quality: 10.7
    developer_ergonomics: 25.5
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 37.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentcat Com Domain Security
  slug: agentcat-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentcat-com
tags:
- Artificial Intelligence
- Analytics
- Observability
- Agent Experience
- Company
website: https://agentcat.com/
---
