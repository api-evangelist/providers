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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Bommel Bot Agentic Access
  operation_count: 15
  slug: bommel-bot-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://bommel.bot
  baseurl_source: declared
  description: The Agent API from bommel-bot — 12 operation(s) for agent.
  name: bommel-bot Agent API
  slug: bommel-bot-agent-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/bommel-bot/agentic-access/bommel-bot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bommel-bot-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bommel-bot/plans/bommel-bot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bommel-bot-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bommel-bot/rules/bommel-bot-rules.yml
  title: ''
  type: Spectral
  url: rules/bommel-bot-rules.yml
- group: agent
  href: https://artifacts.apis.io/bommel-bot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/bommel-bot/authentication/bommel-bot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bommel-bot-authentication.yml
- group: design
  href: https://artifacts.apis.io/bommel-bot/conformance/bommel-bot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bommel-bot-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bommel-bot/llms/bommel-bot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bommel-bot-llms.txt
- group: build
  href: https://artifacts.apis.io/bommel-bot/mcp/bommel-bot-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bommel-bot-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bommel-bot/mcp/bommel-bot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bommel-bot-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bommel-bot/well-known/bommel-bot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bommel-bot-well-known.yml
- group: other
  href: https://artifacts.apis.io/bommel-bot/hosts/bommel-bot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bommel-bot-hosts.yml
- group: other
  href: https://artifacts.apis.io/bommel-bot/vendors/bommel-bot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bommel-bot-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bommel.bot/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://bommel.bot/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bommel.bot/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bommel.bot/pricing
- group: start
  title: ''
  type: Login
  url: https://bommel.bot/login
- group: start
  title: ''
  type: GettingStarted
  url: https://bommel.bot/help/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://bommel.bot/llms.txt
- group: auth
  href: https://artifacts.apis.io/bommel-bot/security/bommel-bot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bommel-bot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bommel.bot/
- group: docs
  href: https://artifacts.apis.io/bommel-bot/openapi/bommel-bot-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/bommel-bot-openapi.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://bommel.bot/api/mcp
  - status: 200
    url: https://bommel.bot/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: 'bommel-bot is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at bommel.bot.
  name: bommel-bot MCP Server
  slug: bommel-bot-mcp-yml
modified: '2026-11-02'
name: bommel-bot
nav: Providers
network: true
overview: 'bommel-bot publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include Company.


  The bommel-bot catalog on APIs.io includes 1 Spectral governance ruleset.


  bommel-bot''s developer surface includes authentication, support, pricing, getting-started guide, API reference, and 17 more developer resources.'
plans:
- name: Bommel Bot Plans Pricing
  plan_count: 2
  slug: bommel-bot-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: bommel-bot API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: bommel-bot-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.5
    catalog_earned_first_party: 8.0
    catalog_gap: 82.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 25.6
    discoverability: 36.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bommel Bot Authentication
  slug: bommel-bot-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bommel Bot Domain Security
  slug: bommel-bot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-feed
  slug: bommel-bot-search_skill
slug: bommel-bot
tags:
- Company
website: https://bommel.bot/
---
