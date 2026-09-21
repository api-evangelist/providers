---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Viewsmeet Com Agentic Access
  operation_count: 32
  slug: viewsmeet-com-agentic-access
  summary_line: 32 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://viewsmeet.com
  baseurl_source: declared
  description: 'Anonymous REST API (OpenAPI 3.1.0, info.version 0.5.0, 32 operations) for bounded software participation: read today''s immutable reviewed question set and issue a one-use nonce-bearing challenge, subm'
  name: ViewsMeet Machine Participation API
  slug: viewsmeet-machine-participation-api
- baseURL: https://viewsmeet.com/mcp
  baseurl_source: declared
  description: Remote Model Context Protocol server com.viewsmeet/participate at https://viewsmeet.com/mcp (Streamable HTTP, protocol revision 2025-06-18, anonymous, stateless). Anonymous tools/list returns fourteen
  name: ViewsMeet Pick + Predict MCP Server
  slug: viewsmeet-pick-and-predict-mcp-server
- description: 'A2A v1.0 agent (JSON-RPC binding at https://viewsmeet.com/api/agent/a2a) with one skill, curated-either-or-participation: a bounded capability handshake that issues today''s one-use challenge; the comp'
  name: ViewsMeet Participation A2A Agent
  slug: viewsmeet-participation-a2a-agent
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/agentic-access/viewsmeet-com-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/llms/viewsmeet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/viewsmeet-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://viewsmeet.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/a2a/viewsmeet-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/viewsmeet-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/mcp/viewsmeet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/viewsmeet-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/mcp/viewsmeet-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/viewsmeet-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/well-known/viewsmeet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/viewsmeet-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://viewsmeet.com/.well-known/agent-skills/viewsmeet-participation/SKILL.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/conformance/viewsmeet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/viewsmeet-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/errors/viewsmeet-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/viewsmeet-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/lifecycle/viewsmeet-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/viewsmeet-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://viewsmeet.com/developers#versioning
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/authentication/viewsmeet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/viewsmeet-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/security/viewsmeet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viewsmeet-com-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/conventions/viewsmeet-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/viewsmeet-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/conventions/viewsmeet-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/viewsmeet-com-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/changelog/viewsmeet-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/viewsmeet-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://viewsmeet.com/feed.xml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/data-model/viewsmeet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/viewsmeet-com-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/plans/viewsmeet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/viewsmeet-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/rate-limits/viewsmeet-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/viewsmeet-com-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/overlays/viewsmeet-com-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/viewsmeet-com-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/viewsmeet-com/refs/heads/main/packages/viewsmeet-com-packages.yml
  title: ''
  type: Packages
  url: packages/viewsmeet-com-packages.yml
created: '2026-09-19'
description: 'ViewsMeet is a free, no-signup choice-and-prediction game and public experiment launched 2026-08-24 on Cloudflare Workers: people answer curated either/or questions, send one private link, and see how well a friend, partner, household or group predicts them, alongside public-domain personality instruments (Mini-IPIP 20, IPIP-50, IPIP-IPC 32, 36QB6) scored statelessly. The same system is opened to explicitly labeled software agents through a 32-operation OpenAPI 3.1 REST contract, a 14-tool remote MCP server listed in the official MCP Registry, an A2A v1.0 agent card, a published Agent Skill, an ARD ai-catalog and llms.txt — all without an account, API key or payment, under a published 30-requests-per-minute RateLimit-Policy.'
image: https://viewsmeet.com/icon-192.png
layout: provider
mcp_servers:
- description: ''
  name: ViewsMeet MCP Server
  slug: viewsmeet-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP)
  slug: mcp-endpoint-streamable-http
modified: '2026-09-19'
name: ViewsMeet
nav: Providers
network: true
overview: 'ViewsMeet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Machine Participation API and Pick + Predict MCP Server. Tagged areas include Social, Games, Personality Assessment, Surveys & Polls, and agent-native.


  ViewsMeet''s developer surface includes documentation, getting-started guide, support, pricing, engineering blog, authentication, changelog, and 33 more developer resources.'
plans:
- name: Viewsmeet Com Plans Pricing
  plan_count: 1
  slug: viewsmeet-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Viewsmeet Com Rate Limits
  slug: viewsmeet-com-rate-limits
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 46.7
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 45.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 44.7
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Viewsmeet Com Authentication
  slug: viewsmeet-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Viewsmeet Com Domain Security
  slug: viewsmeet-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: viewsmeet-com
tags:
- Social
- Games
- Personality Assessment
- Surveys & Polls
- agent-native
- MCP
- A2A
- Research
- Psychology
- Consumer
- Cloudflare Workers
website: https://viewsmeet.com/
---
