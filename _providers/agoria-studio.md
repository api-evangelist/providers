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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agoria Studio Agentic Access
  operation_count: 1
  slug: agoria-studio-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://agoria.studio
  baseurl_source: declared
  description: The Search API from Agoria — 1 operation(s) for search.
  name: Agoria Search API
  slug: agoria-studio-search-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/agoria-studio/agentic-access/agoria-studio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agoria-studio-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agoria-studio/rules/agoria-studio-rules.yml
  title: ''
  type: Spectral
  url: rules/agoria-studio-rules.yml
- group: agent
  href: https://artifacts.apis.io/agoria-studio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agoria-studio/conformance/agoria-studio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agoria-studio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agoria-studio/llms/agoria-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agoria-studio-llms.txt
- group: agent
  href: https://artifacts.apis.io/agoria-studio/mcp/agoria-studio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agoria-studio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agoria-studio/well-known/agoria-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agoria-studio-well-known.yml
- group: other
  href: https://artifacts.apis.io/agoria-studio/hosts/agoria-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agoria-studio-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agoria.studio/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://agoria.studio/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://agoria.studio/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agoria.studio/i/demo-currentia-energy%2Fservice%3Asolar-feed-in-setup
- group: auth
  href: https://artifacts.apis.io/agoria-studio/security/agoria-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agoria-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agoria.studio/
created: '2026-11-01'
description: Agoria provides an AI-powered platform that transforms businesses into live, verified interfaces for AI assistants like ChatGPT, Claude, and Gemini. By aggregating data, pricing, and availability, Agoria enables assistants to accurately quote prices, schedule bookings, and present up‑to‑date information. The service includes a free AI readiness audit, multiple pricing tiers, and tools for businesses to manage their AI visibility across major conversational agents.
image: https://agoria.studio/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at agoria.studio.
  name: Agoria MCP Server
  slug: agoria-studio-mcp-yml
modified: '2026-11-01'
name: Agoria
nav: Providers
network: true
overview: 'Agoria publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Artificial Intelligence, Business, Platform, Commerce, and Automation.


  The Agoria catalog on APIs.io includes 1 Spectral governance ruleset.


  Agoria''s developer surface includes pricing, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Agoria API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: agoria-studio-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 35.5
    developer_ergonomics: 17.1
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agoria Studio Domain Security
  slug: agoria-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: search
  slug: agoria-studio-search
slug: agoria-studio
tags:
- Artificial Intelligence
- Business
- Platform
- Commerce
- Automation
website: https://agoria.studio/
---
