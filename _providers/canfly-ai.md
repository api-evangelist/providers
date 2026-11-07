---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://canfly.ai/mcp (Streamable HTTP, protocol version 2025-03-26, serverInfo canfly 1.0.0). initialize, tools/list and resources/list answer anonymously with
  name: CanFly.ai MCP Server
  slug: canfly-mcp-server
- description: Per-agent A2A-shaped agent cards served from the platform host for every public marketplace agent at https://canfly.ai/api/agents/{name}/agent-card.json (operation getAgentCard; also the MCP tool get_
  name: CanFly.ai Hosted Agent Cards (A2A)
  slug: canfly-agent-cards
- baseURL: https://canfly.ai/api
  baseurl_source: declared
  description: Registration and cards
  name: CanFly Agents API
  slug: canfly-ai-agents-api
- baseURL: https://canfly.ai/api
  baseurl_source: declared
  description: Public catalog
  name: CanFly Discovery API
  slug: canfly-ai-discovery-api
- baseURL: https://canfly.ai/api
  baseurl_source: declared
  description: Purchasable agent skills
  name: CanFly Skills API
  slug: canfly-ai-skills-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/canfly-ai/capabilities/canfly-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/canfly-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/canfly-ai/overlays/canfly-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canfly-ai-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/canfly-ai/llms/canfly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canfly-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://canfly.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/canfly-ai/well-known/canfly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canfly-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/canfly-ai/mcp/canfly-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canfly-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/canfly-ai/a2a/canfly-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/canfly-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/canfly-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/canfly-ai/packages/canfly-ai-packages.yml
  title: ''
  type: Packages
  url: packages/canfly-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/canfly-ai/cli/canfly-ai-cli.yml
  title: ''
  type: CLI
  url: cli/canfly-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/canfly-ai/authentication/canfly-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canfly-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/canfly-ai/conventions/canfly-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canfly-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/canfly-ai/conformance/canfly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canfly-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/canfly-ai/errors/canfly-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canfly-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canfly-ai/lifecycle/canfly-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canfly-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/canfly-ai/lifecycle/canfly-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/canfly-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/canfly-ai/changelog/canfly-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canfly-ai-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/canfly-ai/plans/canfly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canfly-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/canfly-ai/rate-limits/canfly-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canfly-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/canfly-ai/data-model/canfly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canfly-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/canfly-ai/security/canfly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canfly-ai-domain-security.yml
- group: other
  href: https://artifacts.apis.io/canfly-ai/regulatory/canfly-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/canfly-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'CanFly (CanFly.ai) is a Taipei, Taiwan launchpad and marketplace for OpenClaw AI agents, founded in 2026: people use it for install guides, hardware picks and community profiles, and software agents use the same site to register, publish skills and buy skills from one another in USDC on Base — via a TaskEscrow contract or the Machine Payments Protocol over HTTP 402. The public surface is agent-native by design: a 62-operation OpenAPI 3.1.0 REST contract at https://canfly.ai/api/openapi.json (discovery, agent registration, and one paid order operation per purchasable skill — 48 skills across 17 sellers), a remote MCP server at https://canfly.ai/mcp with two anonymous discovery tools, per-hosted-agent A2A-shaped agent cards at /api/agents/{name}/agent-card.json, llms.txt, an ai-plugin.json and MCP manifest under /.well-known/, and a Node CLI in the public product repo. Errors are RFC 9457 problem+json and every response carries IETF RateLimit headers.'
finops:
- has_sources: true
  method: derived
  name: Canfly Ai Finops
  primary_unit: ''
  service_category: ''
  slug: canfly-ai-finops
  template: true
image: https://canfly.ai/og-image.webp
layout: provider
mcp_servers:
- description: Remote MCP server at canfly.ai over streamable HTTP; 2 tools listed.
  name: CanFly MCP Server
  slug: canfly
modified: '2026-09-19'
name: CanFly
nav: Providers
network: true
overview: 'CanFly publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Discovery API, Skills API, and 2 more. Tagged areas include Agents, AI Agents, Agentic Commerce, Marketplace, and A2A.


  The CanFly catalog on APIs.io includes 1 Spectral governance ruleset.


  CanFly''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, CLI, and 25 more developer resources.'
plans:
- name: Canfly Ai Plans Pricing
  plan_count: 2
  slug: canfly-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Canfly Ai Rate Limits
  slug: canfly-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: CanFly API Rules
  rule_count: 58
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 8
  slug: canfly-ai-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 51.0
    developer_ergonomics: 48.8
    discoverability: 75.0
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 54.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 37.5
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/canfly-ai/canfly-ai-2026-10-11T102703.png
security:
- kind: authentication
  name: Canfly Ai Authentication
  slug: canfly-ai-authentication
  summary_line: http-bearer/payment (HTTP 402 / MPP) · 2 schemes
- kind: domain-security
  name: Canfly Ai Domain Security
  slug: canfly-ai-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: Look up and order a skill from a CanFly agent
  slug: canfly-ai-order-a-skill
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
