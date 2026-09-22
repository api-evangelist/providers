---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 26
  human_in_the_loop: 3
  name: Agentspodium Com Agentic Access
  operation_count: 52
  slug: agentspodium-com-agentic-access
  summary_line: 52 operations · 26 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://agentspodium.com/api
  baseurl_source: declared
  description: 'The HTTP API behind the AgentsPodium dashboard, published as an agent-facing subset (OpenAPI 3.1.0, 52 operations): passwordless sign-in and API keys, the public catalog of personas, tiers, engines, t'
  name: AgentsPodium Account API
  slug: account-api
- description: Hosted, agent-native MCP server (Streamable HTTP, protocol 2025-06-18, server agentspodium-hosting 1.0.4) exposing hosting as 13 tools — list_platforms, list_instances, create_instance, get_instance_h
  name: AgentsPodium Hosting MCP Server
  slug: mcp-server
- description: The hosting service as an A2A agent (protocol 0.3.0, JSON-RPC message/send at https://a2a.agentspodium.com/hosting/) with five skills — create-instance, instance-health, instance-term, list-platforms,
  name: AgentsPodium Hosting A2A Agent
  slug: a2a-agent
artifact_total: 11
asyncapis:
- description: ''
  name: Agentspodium Com Webhooks
  slug: agentspodium-com-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/security/agentspodium-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentspodium-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentspodium.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hosting.defispace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hosting.defispace.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://hosting.defispace.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://hosting.defispace.com/docs/quickstart.html
- group: company
  title: ''
  type: Blog
  url: https://agentspodium.com/articles
- group: operate
  title: ''
  type: Roadmap
  url: https://agentspodium.com/articles/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentspodium
- group: commercial
  title: ''
  type: Pricing
  url: https://hosting.defispace.com/#pricing
- group: start
  title: ''
  type: Login
  url: https://agentspodium.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://agentspodium.com/api/status
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/llms/agentspodium-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentspodium-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agentspodium.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/llms/agentspodium-com-hosting-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentspodium-com-hosting-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/a2a/agentspodium-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentspodium-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/mcp/agentspodium-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentspodium-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/mcp/agentspodium-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentspodium-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://hosting.defispace.com/.well-known/agent-skills/index.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/agentic-access/agentspodium-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentspodium-com-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/well-known/agentspodium-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentspodium-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/well-known/agentspodium-com-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/agentspodium-com-openid-configuration.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/authentication/agentspodium-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentspodium-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/conventions/agentspodium-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentspodium-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/errors/agentspodium-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentspodium-com-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/rate-limits/agentspodium-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentspodium-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/plans/agentspodium-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentspodium-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/asyncapi/agentspodium-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentspodium-com-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/lifecycle/agentspodium-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentspodium-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/conformance/agentspodium-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentspodium-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/data-model/agentspodium-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentspodium-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentspodium-com/refs/heads/main/overlays/agentspodium-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentspodium-com-openapi-overlay.yaml
- group: other
  title: ''
  type: ExitAssistance
  url: https://hosting.defispace.com/docs/instances.html
created: '2026-09-19'
description: AgentsPodium runs personal AI agents around the clock, each on its own pod with its own memory and files, answering in the owner's messenger. It hosts ready-made personas and open-source agent platforms (Hermes, OpenClaw, n8n, Claude Code, OpenCode, Pi) on four per-pod plans from $2.49 a month with a 7-day free trial; the model key is the customer's own. The same service is driven by agents through an HTTP account API (OpenAPI 3.1, 52 operations, bearer API key), a hosted MCP server with 13 tools, an A2A agent with five skills, four published Agent Skills, and signed webhooks. The developer documentation lives on the operator's second brand, DefiSpace Hosting (hosting.defispace.com); the company behind both is Radiance Team.
image: https://agentspodium.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: AgentsPodium MCP Server
  slug: agentspodium-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP)
  slug: mcp-endpoint-streamable-http
modified: '2026-09-19'
name: AgentsPodium
nav: Providers
network: true
overview: 'AgentsPodium publishes 1 API on the [APIs.io](https://apis.io/) network: Account API. Tagged areas include AI Agents, Agent Hosting, MCP, A2A, and agent-native.


  The AgentsPodium catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AgentsPodium''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 28 more developer resources.'
plans:
- name: Agentspodium Com Plans Pricing
  plan_count: 4
  slug: agentspodium-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Agentspodium Com Rate Limits
  slug: agentspodium-com-rate-limits
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 61.5
    developer_ergonomics: 59.5
    discoverability: 75.9
    operational_transparency: 55.3
  previous_composite: 54.6
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
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agentspodium Com Authentication
  slug: agentspodium-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentspodium Com Domain Security
  slug: agentspodium-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentspodium-com
tags:
- AI Agents
- Agent Hosting
- MCP
- A2A
- agent-native
- Hosting
- Webhook
- Personal Assistants
- Company
website: https://agentspodium.com/
---
