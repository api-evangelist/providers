---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Berrergate Com Agentic Access
  operation_count: 25
  slug: berrergate-com-agentic-access
  summary_line: 25 operations · 11 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: 'Agent-consumable REST API at https://api.berrergate.com: free procurement and discovery previews over ten capability categories and eight prewarmed sources, a 32-product free-trial catalog, x402-paid '
  name: BerrerGate Tool & Provider Intelligence API
  slug: berrergate-tool-provider-intelligence-api
- description: Remote Model Context Protocol endpoint at https://api.berrergate.com/mcp (Streamable HTTP, POST only), declared in the provider's llms.txt, in an MCP server.json manifest at /.well-known/mcp/server.js
  name: BerrerGate MCP Server
  slug: berrergate-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://api.berrergate.com/.well-known/agent-card.json (content-type application/a2a+json, version 2.9.0) declaring two interfaces — HTTP+JSON at /a2a/v1'
  name: BerrerGate A2A Agent
  slug: berrergate-a2a-agent
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://berrergate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://berrergate.com/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://berrergate.com/privacy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/llms/berrergate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/berrergate-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.berrergate.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/a2a/berrergate-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/berrergate-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/mcp/berrergate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/berrergate-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/mcp/berrergate-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/berrergate-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/well-known/berrergate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/berrergate-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/agentic-access/berrergate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/berrergate-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/security/berrergate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/berrergate-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/authentication/berrergate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/berrergate-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/conventions/berrergate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/berrergate-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/conventions/berrergate-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/berrergate-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/errors/berrergate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/berrergate-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/data-model/berrergate-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/berrergate-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/rate-limits/berrergate-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/berrergate-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/plans/berrergate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/berrergate-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/conformance/berrergate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/berrergate-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/lifecycle/berrergate-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/berrergate-com-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/skills/berrergate-com-provider-skill.md
  title: ''
  type: AgentSkill
  url: skills/berrergate-com-provider-skill.md
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/packages/berrergate-com-packages.yml
  title: ''
  type: Packages
  url: packages/berrergate-com-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/berrergate-com/refs/heads/main/overlays/berrergate-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/berrergate-com-openapi-overlay.yaml
- group: other
  title: ''
  type: AITransparency
  url: https://berrergate.com/privacy/
created: '2026-09-19'
description: 'Berrer runs BerrerGate (berrergate.com), an agent-native "tool and provider intelligence" service: an AI agent describes a task in natural language and BerrerGate maps it to agent-usable tools, APIs and provider categories, returns a free, cache-only procurement preview, and sells tightly bounded "decision packets" — evidence-backed shortlists of commercially cleared open-source implementations for observability, orchestration, scraping, analytics and browser automation — plus a paid Evidence Brief and a low-cost pay-per-call AI answer, all settled in USDC on Base through x402 with no account. The same surface is published three ways from api.berrergate.com: a 25-operation OpenAPI 3.1 contract at /openapi.json, an A2A agent card at /.well-known/agent-card.json with twelve skills (listed as Verified in the Global A2A Registry), and a remote MCP endpoint at /mcp declared in an MCP server.json manifest; discovery is rounded out by an x402 manifest, an AI Registry catalog, an llms.txt
  and a provider-written skill.md. The company states it is experimental, publishes no terms of service, no contact address and no pricing page.'
layout: provider
mcp_servers:
- description: ''
  name: Berrer MCP Server
  slug: berrer-mcp-server
- description: ''
  name: BerrerGate MCP endpoint (Streamable HTTP)
  slug: berrergate-mcp-endpoint-streamable-http
- description: ''
  name: MCP server.json manifest (provider-hosted)
  slug: mcp-serverjson-manifest-provider-hosted
modified: '2026-09-19'
name: Berrer
nav: Providers
network: true
overview: 'Berrer publishes 1 API on the [APIs.io](https://apis.io/) network: BerrerGate Tool & Provider Intelligence API. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  Berrer''s developer surface includes documentation, authentication, and 23 more developer resources.'
plans:
- name: Berrergate Com Plans Pricing
  plan_count: 6
  slug: berrergate-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Berrergate Com Rate Limits
  slug: berrergate-com-rate-limits
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 34.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 30.6
    developer_ergonomics: 47.6
    discoverability: 77.8
    operational_transparency: 31.6
  previous_composite: 5.0
  provenance:
    agentic_access: derived
    conformance: first-party
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
  name: Berrergate Com Authentication
  slug: berrergate-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Berrergate Com Domain Security
  slug: berrergate-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: berrergate-com
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Procurement
- Tool Discovery
- API Discovery
- AI Inference
- Research
- agent-native
website: https://berrergate.com/
---
