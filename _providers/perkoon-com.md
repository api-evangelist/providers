---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: true
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
  score: 20.7
  scored_at: '2026-09-25'
api_count: 3
apis:
- description: 'Perkoon''s agent-to-agent surface: an A2A agent card served at /.well-known/agent-card.json and the legacy /.well-known/agent.json (byte-identical, 200 application/json) pointing at a JSON-RPC 2.0 endp'
  name: Perkoon Agent Data Layer (A2A)
  slug: perkoon-a2a-agent
- description: 'The anonymous REST surface under https://perkoon.com/api/v1 that every Perkoon client uses: POST /sessions (create, 10/min per IP), POST /sessions/{code}/join (30/min) and GET /sessions/{code}/status '
  name: Perkoon Sessions API
  slug: perkoon-sessions-api
- description: 'Official local stdio MCP server, @perkoon/mcp on npm (0.3.0, 2026-09-01), installed with npx -y @perkoon/mcp and named in the A2A card''s resources[] and in llms.txt as the recommended path for coding '
  name: Perkoon MCP Server
  slug: perkoon-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://perkoon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://perkoon.com/automate
- group: start
  title: ''
  type: GettingStarted
  url: https://perkoon.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://perkoon.com/pricing
- group: other
  title: ''
  type: Sitemap
  url: https://perkoon.com/sitemap.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Perkoon
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/llms/perkoon-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/perkoon-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/well-known/perkoon-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/perkoon-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/a2a/perkoon-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/perkoon-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/mcp/perkoon-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/perkoon-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/packages/perkoon-com-packages.yml
  title: ''
  type: Packages
  url: packages/perkoon-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/packages/perkoon-com-packages.yml
  title: ''
  type: SDKs
  url: packages/perkoon-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/cli/perkoon-com-cli.yml
  title: ''
  type: CLI
  url: cli/perkoon-com-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/rate-limits/perkoon-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/perkoon-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/plans/perkoon-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/perkoon-com-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/authentication/perkoon-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/perkoon-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/conventions/perkoon-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/perkoon-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/errors/perkoon-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/perkoon-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/conformance/perkoon-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/perkoon-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/lifecycle/perkoon-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/perkoon-com-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/regulatory/perkoon-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/perkoon-com-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perkoon-com/refs/heads/main/security/perkoon-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perkoon-com-domain-security.yml
created: '2026-09-19'
description: 'Perkoon is an account-less file-transfer service built for AI agents as much as for people, operated by MB "Perkunu simtas" in Lithuania. Small files upload once to free cloud delivery and return a durable ~48-hour share link (fire-and-forget); larger files stream directly between machines over WebRTC with no size limit, with perkoon.com doing signalling only. The same capability - create a transfer session, join it, check it - is projected over four entry points the provider documents for agents: an A2A agent card at /.well-known/agent-card.json (conformant to A2A 1.0.0, protocol 0.3.0, four skills, JSON-RPC at /a2a), an anonymous REST surface at /api/v1/sessions consumed by the first-party perkoon CLI (npm, also an importable JS library), a stdio MCP server (@perkoon/mcp: send_file, receive_file, check_session) and a Playwright-ready browser flow. It publishes llms.txt, a skillpm Agent Skill (perkoon-transfer) and per-IP rate limits inside the card itself. No OpenAPI, OAuth
  or event surface is published, and every HTML page - including the /automate guide and /pricing - sits behind a Cloudflare managed challenge for non-browser clients, while the card, llms.txt and robots.txt are served openly.'
layout: provider
mcp_servers:
- description: 'Perkoon ships an official MCP server as a local stdio package, @perkoon/mcp on npm (author Perkoon, same maintainer as the perkoon CLI; homepage https://perkoon.com; proprietary licence). It is named '
  name: Perkoon MCP Server
  slug: perkoon-mcp-server
modified: '2026-09-19'
name: Perkoon
nav: Providers
network: true
overview: 'Perkoon publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include File Transfer, P2P, WebRTC, AI Agents, and A2A.


  Perkoon''s developer surface includes documentation, getting-started guide, pricing, CLI, authentication, and 18 more developer resources.'
plans:
- name: Perkoon Com Plans Pricing
  plan_count: 0
  slug: perkoon-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Perkoon Com Rate Limits
  slug: perkoon-com-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 73.3
    operational_transparency: 36.8
  previous_composite: 27.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Perkoon Com Authentication
  slug: perkoon-com-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Perkoon Com Domain Security
  slug: perkoon-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: perkoon-com
tags:
- File Transfer
- P2P
- WebRTC
- AI Agents
- A2A
- MCP
- CLI
- Agent Skills
- Cloud Storage
- Developer Tools
- Lithuania
website: https://perkoon.com/
---
