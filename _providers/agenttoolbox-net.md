---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Agenttoolbox Net Agentic Access
  operation_count: 5
  slug: agenttoolbox-net-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://agenttoolbox.net
  baseurl_source: declared
  description: The Directory API from Agent Toolbox — 1 operation(s) for directory.
  name: Agent Toolbox Directory API
  slug: agenttoolbox-net-directory-api
- baseURL: https://agenttoolbox.net
  baseurl_source: declared
  description: The Tools API from Agent Toolbox — 4 operation(s) for tools.
  name: Agent Toolbox Tools API
  slug: agenttoolbox-net-tools-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/agenttoolbox-net/agentic-access/agenttoolbox-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenttoolbox-net-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agenttoolbox-net/plans/agenttoolbox-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenttoolbox-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenttoolbox-net/rules/agenttoolbox-net-rules.yml
  title: ''
  type: Spectral
  url: rules/agenttoolbox-net-rules.yml
- group: agent
  href: https://artifacts.apis.io/agenttoolbox-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agenttoolbox-net/authentication/agenttoolbox-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenttoolbox-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/agenttoolbox-net/conformance/agenttoolbox-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenttoolbox-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenttoolbox-net/llms/agenttoolbox-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenttoolbox-net-llms.txt
- group: other
  href: https://artifacts.apis.io/agenttoolbox-net/hosts/agenttoolbox-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenttoolbox-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenttoolbox-net/vendors/agenttoolbox-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenttoolbox-net-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://agenttoolbox.net/signin
- group: docs
  title: ''
  type: APIReference
  url: https://agenttoolbox.net/developers
- group: auth
  href: https://artifacts.apis.io/agenttoolbox-net/security/agenttoolbox-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenttoolbox-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenttoolbox.net/
- group: company
  title: ''
  type: Blog
  url: https://agenttoolbox.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://agenttoolbox.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenttoolbox.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenttoolbox.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://agenttoolbox.net/contact
created: '2026-11-01'
description: Agent Toolbox provides a free toolkit for AI agent builders, offering instant, private utilities that run directly in the browser without signup. The platform includes a directory of tools, MCP server configurations, token estimators, schema validators, and linting utilities, supporting popular LLM clients like Claude Desktop and Cursor. It aims to simplify tool integration for LLM applications, offering resources such as pricing, documentation, and community support.
image: https://agenttoolbox.net/opengraph-image?6e07f9ba2dc69262
layout: provider
modified: '2026-11-01'
name: Agent Toolbox
nav: Providers
network: true
overview: 'Agent Toolbox publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Directory API and Tools API. Tagged areas include Artificial Intelligence, Tools, Free, Browser, and Agents.


  The Agent Toolbox catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Toolbox''s developer surface includes authentication, API reference, engineering blog, pricing, support, and 13 more developer resources.'
plans:
- name: Agenttoolbox Net Plans Pricing
  plan_count: 2
  slug: agenttoolbox-net-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Agent Toolbox API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agenttoolbox-net-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 20.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
    skills: derived
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
  name: Agenttoolbox Net Authentication
  slug: agenttoolbox-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenttoolbox Net Domain Security
  slug: agenttoolbox-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: estimate-tokens
  slug: agenttoolbox-net-estimate-tokens
slug: agenttoolbox-net
tags:
- Artificial Intelligence
- Tools
- Free
- Browser
- Agents
website: https://agenttoolbox.net/
---
