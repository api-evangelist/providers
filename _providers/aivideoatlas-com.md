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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aivideoatlas Com Agentic Access
  operation_count: 1
  slug: aivideoatlas-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://mcp.aivideoatlas.com
  baseurl_source: declared
  description: The Plan Shots API from AI Video Atlas — 1 operation(s) for plan shots.
  name: AI Video Atlas Plan Shots API
  slug: aivideoatlas-com-plan-shots-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/aivideoatlas-com/vocabulary/aivideoatlas-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aivideoatlas-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aivideoatlas-com/agentic-access/aivideoatlas-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aivideoatlas-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aivideoatlas-com/rules/aivideoatlas-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aivideoatlas-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/aivideoatlas-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/aivideoatlas-com/changelog/aivideoatlas-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aivideoatlas-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/aivideoatlas-com/conformance/aivideoatlas-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aivideoatlas-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aivideoatlas-com/llms/aivideoatlas-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aivideoatlas-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aivideoatlas-com/mcp/aivideoatlas-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aivideoatlas-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aivideoatlas-com/mcp/aivideoatlas-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aivideoatlas-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/aivideoatlas-com/hosts/aivideoatlas-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aivideoatlas-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aivideoatlas-com/vendors/aivideoatlas-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aivideoatlas-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://aivideoatlas.com/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aivideoatlas.com/whats-new/
- group: auth
  href: https://artifacts.apis.io/aivideoatlas-com/security/aivideoatlas-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aivideoatlas-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aivideoatlas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.aivideoatlas.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://mcp.aivideoatlas.com/guide.md
- group: commercial
  title: ''
  type: Pricing
  url: https://aivideoatlas.com/prices/
- group: operate
  title: ''
  type: Support
  url: https://aivideoatlas.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aivideoatlas.com/privacy/
created: '2026-11-01'
description: AI Video Atlas helps people discover and compare AI video generation models by providing vendor‑stated prices, sourced shot examples, and side‑by‑side model comparisons. The site offers a free, read‑only MCP server and REST API that returns model data, pricing, prompts, and example videos. It is a New AI Society project run by an AI‑assisted editorial team that continuously scans GitHub, Hacker News, Reddit and vendor changelogs to keep the listings up to date.
image: https://aivideoatlas.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.aivideoatlas.com.
  name: AI Video Atlas MCP Server
  slug: aivideoatlas-com-mcp-yml
modified: '2026-11-01'
name: AI Video Atlas
nav: Providers
network: true
overview: 'AI Video Atlas publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Plan Shots API. Tagged areas include Artificial Intelligence, Video, Comparison, Pricing, and Tools.


  The AI Video Atlas catalog on APIs.io includes 1 Spectral governance ruleset.


  AI Video Atlas'' developer surface includes changelog, documentation, API reference, getting-started guide, pricing, support, and 14 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AI Video Atlas API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aivideoatlas-com-rules
scopes:
- name: Aivideoatlas Com Scopes
  scope_count: 0
  slug: aivideoatlas-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 44.7
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aivideoatlas Com Authentication
  slug: aivideoatlas-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aivideoatlas Com Domain Security
  slug: aivideoatlas-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 10
skills:
- name: best-prompt-skill
  slug: best-prompt-skill
- name: find-shot-skill
  slug: find-shot-skill
- name: fix-prompt-skill
  slug: fix-prompt-skill
- name: get-guide-skill
  slug: get-guide-skill
- name: get-prices-skill
  slug: get-prices-skill
- name: get-workflow-skill
  slug: get-workflow-skill
- name: plan-shots-skill
  slug: plan-shots-skill
- name: recommend-model-skill
  slug: recommend-model-skill
- name: refine-shot-skill
  slug: refine-shot-skill
- name: whats-new-skill
  slug: whats-new-skill
slug: aivideoatlas-com
tags:
- Artificial Intelligence
- Video
- Comparison
- Pricing
- Tools
website: https://aivideoatlas.com/
---
