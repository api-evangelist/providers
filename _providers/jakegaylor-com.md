---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 18.0
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: Hosted MCP server exposing Jake Gaylor's resume, links and website text as resources and tools, structured screening preferences, an LLM-backed role-fit assessment and interview-question generator, li
  name: Jake Gaylor MCP Server
  slug: jake-gaylor-mcp-server
- description: 'A2A agent representing Jake Gaylor, discovered at /.well-known/agent-card.json on ai.jakegaylor.com (and as a static copy on jakegaylor.com) with a JSON-RPC interface at /a2a serving protocol 1.0 and '
  name: Jake Gaylor A2A Agent
  slug: jake-gaylor-a2a-agent
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://jakegaylor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ai.jakegaylor.com/
- group: company
  title: ''
  type: Blog
  url: https://jakegaylor.com/blog/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jhgaylor/ai-jakegaylor-com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/llms/jakegaylor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jakegaylor-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://ai.jakegaylor.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/well-known/jakegaylor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jakegaylor-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/a2a/jakegaylor-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/jakegaylor-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/mcp/jakegaylor-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jakegaylor-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/packages/jakegaylor-com-packages.yml
  title: ''
  type: Packages
  url: packages/jakegaylor-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/conformance/jakegaylor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jakegaylor-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/lifecycle/jakegaylor-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jakegaylor-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/authentication/jakegaylor-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jakegaylor-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/conventions/jakegaylor-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jakegaylor-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/errors/jakegaylor-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jakegaylor-com-problem-types.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/plans/jakegaylor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jakegaylor-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/rate-limits/jakegaylor-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jakegaylor-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jakegaylor-com/refs/heads/main/security/jakegaylor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jakegaylor-com-domain-security.yml
created: '2026-09-19'
description: 'Jake Gaylor is a software engineer (platform engineering, Kubernetes, developer tooling) whose personal site publishes an agent-native representation of his resume. ai.jakegaylor.com serves a hosted Model Context Protocol server (Streamable HTTP at /mcp, a legacy SSE transport, and the same server as the npm stdio package @jhgaylor/me-mcp) with 12 tools, 6 resources and 7 prompts; an Agent2Agent (A2A) agent published at /.well-known/agent-card.json - JWS-signed, served in 0.3 and 1.0 shapes negotiated on the A2A-Version header - with six skills; and an llms.txt. Every surface answers anonymously: read the resume and structured screening preferences, assess role fit against a job description, generate interview questions, read live intro-call availability and create a pending-confirmation booking, or relay a message by email. The server is open source (MIT) at github.com/jhgaylor/ai-jakegaylor-com.'
image: https://jakegaylor.com/images/og-card.jpg?v=7
layout: provider
mcp_servers:
- description: 'Hosted Model Context Protocol server that makes Jake Gaylor''s resume, links, screening preferences and calendar legible to AI assistants: read tools, an LLM-backed role-fit assessment and interview-qu'
  name: Jake Gaylor MCP Server
  slug: jake-gaylor-mcp-server
- description: ''
  name: Jake Gaylor MCP Server
  slug: jake-gaylor-mcp-server-2
modified: '2026-09-19'
name: Jake Gaylor
nav: Providers
network: true
overview: 'Jake Gaylor publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, AI Agents, A2A, and MCP.


  Jake Gaylor''s developer surface includes documentation, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Jakegaylor Com Plans Pricing
  plan_count: 0
  slug: jakegaylor-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Jakegaylor Com Rate Limits
  slug: jakegaylor-com-rate-limits
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 18.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jakegaylor Com Authentication
  slug: jakegaylor-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Jakegaylor Com Domain Security
  slug: jakegaylor-com-domain-security
  summary_line: TLSv1.3
slug: jakegaylor-com
tags:
- Company
- Agents
- AI Agents
- A2A
- MCP
- Hiring
- Recruiting
- Resume
- Scheduling
- Personal Agent
website: https://jakegaylor.com/
---
