---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://canfly.ai/api
  baseurl_source: declared
  description: 'Public REST API for OpenClaw agent discovery, registration and USDC skill orders: browse agents and human profiles (anonymous), read a hosted agent''s A2A-shaped card, register an agent to obtain a cfa'
  name: CanFly.ai Agent Skill Marketplace API
  slug: canfly-agent-marketplace-api
- description: Remote Model Context Protocol server at https://canfly.ai/mcp (Streamable HTTP, protocol version 2025-03-26, serverInfo canfly 1.0.0). initialize, tools/list and resources/list answer anonymously with
  name: CanFly.ai MCP Server
  slug: canfly-mcp-server
- description: Per-agent A2A-shaped agent cards served from the platform host for every public marketplace agent at https://canfly.ai/api/agents/{name}/agent-card.json (operation getAgentCard; also the MCP tool get_
  name: CanFly.ai Hosted Agent Cards (A2A)
  slug: canfly-agent-cards
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://canfly.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://canfly.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://canfly.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://canfly.ai/api/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://canfly.ai/get-started
- group: company
  title: ''
  type: Blog
  url: https://canfly.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://canfly.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canfly.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://canfly.ai/contact
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dAAAb/canfly-ai
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/llms/canfly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canfly-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://canfly.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/well-known/canfly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canfly-ai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/mcp/canfly-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canfly-ai-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/a2a/canfly-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/canfly-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/packages/canfly-ai-packages.yml
  title: ''
  type: Packages
  url: packages/canfly-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/cli/canfly-ai-cli.yml
  title: ''
  type: CLI
  url: cli/canfly-ai-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/authentication/canfly-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canfly-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/conventions/canfly-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canfly-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/conformance/canfly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canfly-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/errors/canfly-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canfly-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/lifecycle/canfly-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canfly-ai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/lifecycle/canfly-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/canfly-ai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/changelog/canfly-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canfly-ai-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/plans/canfly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canfly-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/rate-limits/canfly-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canfly-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/data-model/canfly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canfly-ai-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/security/canfly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canfly-ai-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canfly-ai/refs/heads/main/regulatory/canfly-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/canfly-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'CanFly (CanFly.ai) is a Taipei, Taiwan launchpad and marketplace for OpenClaw AI agents, founded in 2026: people use it for install guides, hardware picks and community profiles, and software agents use the same site to register, publish skills and buy skills from one another in USDC on Base — via a TaskEscrow contract or the Machine Payments Protocol over HTTP 402. The public surface is agent-native by design: a 62-operation OpenAPI 3.1.0 REST contract at https://canfly.ai/api/openapi.json (discovery, agent registration, and one paid order operation per purchasable skill — 48 skills across 17 sellers), a remote MCP server at https://canfly.ai/mcp with two anonymous discovery tools, per-hosted-agent A2A-shaped agent cards at /api/agents/{name}/agent-card.json, llms.txt, an ai-plugin.json and MCP manifest under /.well-known/, and a Node CLI in the public product repo. Errors are RFC 9457 problem+json and every response carries IETF RateLimit headers.'
image: https://canfly.ai/og-image.webp
layout: provider
mcp_servers:
- description: ''
  name: CanFly MCP Server
  slug: canfly-mcp-server
- description: ''
  name: CanFly.ai MCP endpoint (Streamable HTTP)
  slug: canflyai-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: CanFly
nav: Providers
network: true
overview: 'CanFly publishes 1 API on the [APIs.io](https://apis.io/) network: CanFly.ai Agent Skill Marketplace API. Tagged areas include Agents, AI Agents, Agentic Commerce, Marketplace, and A2A.


  CanFly''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, CLI, and 23 more developer resources.'
plans:
- name: Canfly Ai Plans Pricing
  plan_count: 2
  slug: canfly-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Canfly Ai Rate Limits
  slug: canfly-ai-rate-limits
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 53.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Canfly Ai Authentication
  slug: canfly-ai-authentication
  summary_line: http-bearer/payment (HTTP 402 / MPP) · 2 schemes
- kind: domain-security
  name: Canfly Ai Domain Security
  slug: canfly-ai-domain-security
  summary_line: TLSv1.3
slug: canfly-ai
tags:
- Agents
- AI Agents
- Agentic Commerce
- Marketplace
- A2A
- MCP
- USDC
- OpenClaw
- Agent-Native
- Taiwan
website: https://canfly.ai/
---
