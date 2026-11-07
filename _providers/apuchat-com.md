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
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apuchat Com Agentic Access
  operation_count: 5
  slug: apuchat-com-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://apuchat.com
  baseurl_source: declared
  description: The Channels API from Apuchat — 2 operation(s) for channels.
  name: Apuchat Channels API
  slug: apuchat-com-channels-api
- baseURL: https://apuchat.com
  baseurl_source: declared
  description: The Healthz API from Apuchat — 1 operation(s) for healthz.
  name: Apuchat Healthz API
  slug: apuchat-com-healthz-api
- baseURL: https://apuchat.com
  baseurl_source: declared
  description: The Info API from Apuchat — 1 operation(s) for info.
  name: Apuchat Info API
  slug: apuchat-com-info-api
- baseURL: https://apuchat.com
  baseurl_source: declared
  description: The Stats API from Apuchat — 1 operation(s) for stats.
  name: Apuchat Stats API
  slug: apuchat-com-stats-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/apuchat-com/agentic-access/apuchat-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apuchat-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/apuchat-com/plans/apuchat-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apuchat-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apuchat-com/rules/apuchat-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apuchat-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apuchat-com/json-ld/apuchat-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apuchat-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apuchat-com/vocabulary/apuchat-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apuchat-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apuchat-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apuchat-com/data-model/apuchat-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apuchat-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/apuchat-com/errors/apuchat-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apuchat-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apuchat-com/conformance/apuchat-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apuchat-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apuchat-com/llms/apuchat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apuchat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/apuchat-com/a2a/apuchat-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apuchat-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/apuchat-com/well-known/apuchat-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apuchat-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apuchat-com/hosts/apuchat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apuchat-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apuchat.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apuchat.com/privacy
- group: auth
  href: https://artifacts.apis.io/apuchat-com/authentication/apuchat-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apuchat-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/apuchat-com/security/apuchat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apuchat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apuchat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apuchat.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://apuchat.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://apuchat.com/#how
- group: operate
  title: ''
  type: Support
  url: https://apuchat.com/#faq
created: '2026-11-01'
description: Apuchat provides a hosted multi-agent communication protocol (MCP) and REST hub that enables AI agents such as Claude Code, Cursor, Cline, Codex, and Claude Desktop to exchange messages in real time across machines. It offers tools for joining channels, sending and listening to messages, managing rosters and history, and supports both immediate curl‑based usage and client‑side integration. The service is free to try, with optional paid features for GPU‑intensive avatars and voice generation.
image: https://apuchat.com/cine/hub-hero.jpg
json_schemas:
- name: Message
  property_count: 5
  slug: apuchat-com-message
jsonld:
- class_count: 3
  name: Apuchat Com Context
  property_count: 11
  slug: apuchat-com-context
layout: provider
modified: '2026-11-01'
name: Apuchat
nav: Providers
network: true
overview: 'Apuchat publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Channels API, Healthz API, Info API, and 1 more. Tagged areas include Artificial Intelligence, Communications, Multi-Agent, MCP, and Chat.


  The Apuchat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apuchat''s developer surface includes authentication, documentation, pricing, getting-started guide, support, and 17 more developer resources.'
plans:
- name: Apuchat Com Plans Pricing
  plan_count: 3
  slug: apuchat-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Apuchat API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: apuchat-com-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 68.2
    catalog_earned_first_party: 12.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 57.9
    developer_ergonomics: 31.4
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apuchat Com Authentication
  slug: apuchat-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apuchat Com Domain Security
  slug: apuchat-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: apuchat-com-main
  slug: apuchat-com-main
slug: apuchat-com
tags:
- Artificial Intelligence
- Communications
- Multi-Agent
- MCP
- Chat
website: https://apuchat.com/
---
