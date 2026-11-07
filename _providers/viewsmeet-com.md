---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Viewsmeet Com Agentic Access
  operation_count: 32
  slug: viewsmeet-com-agentic-access
  summary_line: 32 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'A2A v1.0 agent (JSON-RPC binding at https://viewsmeet.com/api/agent/a2a) with one skill, curated-either-or-participation: a bounded capability handshake that issues today''s one-use challenge; the comp'
  name: ViewsMeet Participation A2A Agent
  slug: viewsmeet-participation-a2a-agent
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Agent API from ViewsMeet — 2 operation(s) for agent.
  name: ViewsMeet Agent API
  slug: viewsmeet-com-agent-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Agents API from ViewsMeet — 4 operation(s) for agents.
  name: ViewsMeet Agents API
  slug: viewsmeet-com-agents-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Assessments API from ViewsMeet — 4 operation(s) for assessments.
  name: ViewsMeet Assessments API
  slug: viewsmeet-com-assessments-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Connections API from ViewsMeet — 1 operation(s) for connections.
  name: ViewsMeet Connections API
  slug: viewsmeet-com-connections-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Experiments API from ViewsMeet — 7 operation(s) for experiments.
  name: ViewsMeet Experiments API
  slug: viewsmeet-com-experiments-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Mcp API from ViewsMeet — 1 operation(s) for mcp.
  name: ViewsMeet MCP API
  slug: viewsmeet-com-mcp-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: The Personality API from ViewsMeet — 9 operation(s) for personality.
  name: ViewsMeet Personality API
  slug: viewsmeet-com-personality-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://viewsmeet.com/mcp
- group: agent
  href: https://artifacts.apis.io/viewsmeet-com/agentic-access/viewsmeet-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/viewsmeet-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://viewsmeet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://viewsmeet.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://viewsmeet.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://viewsmeet.com/developers#quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://viewsmeet.com/agents
- group: operate
  title: ''
  type: Support
  url: https://viewsmeet.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://viewsmeet.com/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viewsmeet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viewsmeet.com/privacy
- group: company
  title: ''
  type: About
  url: https://viewsmeet.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://viewsmeet.com/methodology
- group: company
  title: ''
  type: Blog
  url: https://viewsmeet.com/research
- group: company
  title: ''
  type: BlogRSS
  url: https://viewsmeet.com/feed.xml
- group: company
  title: ''
  type: Newsroom
  url: https://viewsmeet.com/press
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ViewsMeet
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/viewsmeet/
- group: agent
  href: https://artifacts.apis.io/viewsmeet-com/llms/viewsmeet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/viewsmeet-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://viewsmeet.com/llms.txt
- group: other
  href: https://artifacts.apis.io/viewsmeet-com/a2a/viewsmeet-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/viewsmeet-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/viewsmeet-com/mcp/viewsmeet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/viewsmeet-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/viewsmeet-com/mcp/viewsmeet-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/viewsmeet-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/viewsmeet-com/well-known/viewsmeet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/viewsmeet-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/viewsmeet-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://viewsmeet.com/.well-known/agent-skills/viewsmeet-participation/SKILL.md
- group: design
  href: https://artifacts.apis.io/viewsmeet-com/conformance/viewsmeet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/viewsmeet-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/viewsmeet-com/errors/viewsmeet-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/viewsmeet-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/viewsmeet-com/lifecycle/viewsmeet-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/viewsmeet-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://viewsmeet.com/developers#versioning
- group: auth
  href: https://artifacts.apis.io/viewsmeet-com/authentication/viewsmeet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/viewsmeet-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/viewsmeet-com/security/viewsmeet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viewsmeet-com-domain-security.yml
- group: design
  href: https://artifacts.apis.io/viewsmeet-com/conventions/viewsmeet-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/viewsmeet-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/viewsmeet-com/conventions/viewsmeet-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/viewsmeet-com-conventions.yml
- group: operate
  href: https://artifacts.apis.io/viewsmeet-com/changelog/viewsmeet-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/viewsmeet-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://viewsmeet.com/feed.xml
- group: design
  href: https://artifacts.apis.io/viewsmeet-com/data-model/viewsmeet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/viewsmeet-com-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/viewsmeet-com/plans/viewsmeet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/viewsmeet-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/viewsmeet-com/rate-limits/viewsmeet-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/viewsmeet-com-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/viewsmeet-com/overlays/viewsmeet-com-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/viewsmeet-com-overlay.yaml
- group: build
  href: https://artifacts.apis.io/viewsmeet-com/packages/viewsmeet-com-packages.yml
  title: ''
  type: Packages
  url: packages/viewsmeet-com-packages.yml
created: '2026-09-19'
description: 'ViewsMeet is a free, no-signup choice-and-prediction game and public experiment launched 2026-08-24 on Cloudflare Workers: people answer curated either/or questions, send one private link, and see how well a friend, partner, household or group predicts them, alongside public-domain personality instruments (Mini-IPIP 20, IPIP-50, IPIP-IPC 32, 36QB6) scored statelessly. The same system is opened to explicitly labeled software agents through a 32-operation OpenAPI 3.1 REST contract, a 14-tool remote MCP server listed in the official MCP Registry, an A2A v1.0 agent card, a published Agent Skill, an ARD ai-catalog and llms.txt — all without an account, API key or payment, under a published 30-requests-per-minute RateLimit-Policy.'
finops:
- has_sources: true
  method: derived
  name: Viewsmeet Com Finops
  primary_unit: ''
  service_category: ''
  slug: viewsmeet-com-finops
  template: true
image: https://viewsmeet.com/icon-192.png
layout: provider
mcp_servers:
- description: ''
  name: ViewsMeet MCP Server
  slug: mcp
modified: '2026-09-19'
name: ViewsMeet
nav: Providers
network: true
overview: 'ViewsMeet publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Agents API, Assessments API, and 5 more. Tagged areas include Social, Games, Personality Assessment, Surveys & Polls, and Agent-Native.


  The ViewsMeet catalog on APIs.io includes 1 Spectral governance ruleset.


  ViewsMeet''s developer surface includes documentation, getting-started guide, support, pricing, engineering blog, authentication, changelog, and 34 more developer resources.'
plans:
- name: Viewsmeet Com Plans Pricing
  plan_count: 1
  slug: viewsmeet-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Viewsmeet Com Rate Limits
  slug: viewsmeet-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: ViewsMeet API Rules
  rule_count: 48
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 6
  slug: viewsmeet-com-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.5
    catalog_earned_first_party: 16.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 48.8
    developer_ergonomics: 41.7
    discoverability: 75.8
    operational_transparency: 40.8
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: first-party
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/viewsmeet-com/viewsmeet-com-2026-10-11T132955.png
security:
- kind: authentication
  name: Viewsmeet Com Authentication
  slug: viewsmeet-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Viewsmeet Com Domain Security
  slug: viewsmeet-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: viewsmeet-group-picks-room
  slug: viewsmeet-com-group-picks-room
- name: viewsmeet-score-assessment-vector
  slug: viewsmeet-com-score-assessment-vector
slug: viewsmeet-com
tags:
- Social
- Games
- Personality Assessment
- Surveys & Polls
- Agent-Native
- MCP
- A2A
- Research
- Psychology
- Consumer
- Cloudflare Workers
website: https://viewsmeet.com/
---
