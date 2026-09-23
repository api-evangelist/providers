---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-09-23'
api_count: 3
apis:
- description: 'Live, anonymous, remote Model Context Protocol server at https://p0stman.com/api/mcp (JSON-RPC 2.0 over HTTPS POST, protocol 2024-11-05, tools primitive only). Five tools: get_services (services with '
  name: p0stman MCP Server
  slug: p0stman-mcp-server
- description: 'p0stman''s agent-to-agent surface: an A2A agent card for "Zero" served at /.well-known/agent-card.json (and the legacy /.well-known/agent.json) on p0stman.com and www.p0stman.com, pointing at an anonym'
  name: Zero A2A Agent
  slug: zero-a2a-agent
- description: 'Three anonymous JSON endpoints documented in agents.md for agents that do not speak MCP: GET /api/ai/context (company, services, case_studies, contact, how_to_engage, mcp_endpoint), GET /api/ai/servic'
  name: p0stman AI Context API
  slug: p0stman-ai-context-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://p0stman.com/
- group: docs
  title: ''
  type: Documentation
  url: https://p0stman.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://p0stman.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://p0stman.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://p0stman.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://p0stman.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://p0stman.com/guides
- group: other
  title: ''
  type: Leadership
  url: https://p0stman.com/paulgosnell
- group: commercial
  title: ''
  type: TermsOfService
  url: https://p0stman.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://p0stman.com/privacy
- group: other
  title: ''
  type: Sitemap
  url: https://p0stman.com/sitemap.xml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/paulgosnell/zero-agent
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/in/pgosnell
- group: company
  title: ''
  type: Twitter
  url: https://x.com/paulgosnell
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/llms/p0stman-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/p0stman-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/llms/p0stman-com-agents.md
  title: ''
  type: AgentsMd
  url: llms/p0stman-com-agents.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/well-known/p0stman-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/p0stman-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/a2a/p0stman-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/p0stman-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/mcp/p0stman-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/p0stman-com-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/authentication/p0stman-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/p0stman-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/conventions/p0stman-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/p0stman-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/errors/p0stman-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/p0stman-com-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/rate-limits/p0stman-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/p0stman-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/plans/p0stman-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/p0stman-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/conformance/p0stman-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/p0stman-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/lifecycle/p0stman-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/p0stman-com-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/packages/p0stman-com-packages.yml
  title: ''
  type: Packages
  url: packages/p0stman-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/security/p0stman-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/p0stman-com-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/p0stman-com/refs/heads/main/regulatory/p0stman-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/p0stman-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://p0stman.com/privacy
created: '2026-09-19'
description: 'p0stman is an AI-native product studio operated by Thrive Venture Labs Ltd (Norfolk and London, UK), founded by Paul Gosnell. It builds AI voice agents, AI automation, operations command centres, rapid MVPs and "agentic web readiness" rebuilds for clients at fixed prices from £1,500-£8,000, and it uses its own site as the demonstration: p0stman.com serves a live anonymous MCP server at /api/mcp (five tools, JSON-RPC 2.0, protocol 2024-11-05), an A2A agent card for its assistant "Zero" at /.well-known/agent-card.json with a task endpoint at /api/agent, machine-readable JSON at /api/ai/context, /api/ai/services and /api/ai/portfolio, plus llms.txt, agents.md, context.md and a root mcp.json manifest. No OpenAPI, SDK, OAuth surface or developer sign-up is published - the whole API is free, anonymous and read-mostly, with two write tools that book a discovery call or send an enquiry. Not the Postman API platform.'
image: https://p0stman.com/icon-512.png
layout: provider
mcp_servers:
- description: p0stman ships a live, anonymous, remote MCP server at https://p0stman.com/api/mcp (JSON-RPC 2.0 over HTTPS POST, no session handshake required). It is advertised in llms.txt, agents.md, context.md and
  name: p0stman MCP Server
  slug: p0stman-mcp-server
modified: '2026-09-19'
name: p0stman
nav: Providers
network: true
overview: 'p0stman publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, MCP, A2A, Agentic Web, and Voice AI.


  p0stman''s developer surface includes documentation, getting-started guide, support, pricing, engineering blog, authentication, and 25 more developer resources.'
plans:
- name: P0Stman Com Plans Pricing
  plan_count: 0
  slug: p0stman-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: P0Stman Com Rate Limits
  slug: p0stman-com-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 81.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 25.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: P0Stman Com Authentication
  slug: p0stman-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: P0Stman Com Domain Security
  slug: p0stman-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: p0stman-com
tags:
- AI Agents
- MCP
- A2A
- Agentic Web
- Voice AI
- AI Automation
- Product Studio
- Software Development
- Consulting
- United Kingdom
website: https://p0stman.com/
---
