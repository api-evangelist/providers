---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Berrergate Com Agentic Access
  operation_count: 25
  slug: berrergate-com-agentic-access
  summary_line: 25 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Remote Model Context Protocol endpoint at https://api.berrergate.com/mcp (Streamable HTTP, POST only), declared in the provider's llms.txt, in an MCP server.json manifest at /.well-known/mcp/server.js
  name: BerrerGate MCP Server
  slug: berrergate-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://api.berrergate.com/.well-known/agent-card.json (content-type application/a2a+json, version 2.9.0) declaring two interfaces — HTTP+JSON at /a2a/v1'
  name: BerrerGate A2A Agent
  slug: berrergate-a2a-agent
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: The A2a API from Berrer — 2 operation(s) for a2a.
  name: Berrer A2a API
  slug: berrergate-com-a2a-api
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: The Agent API from Berrer — 18 operation(s) for agent.
  name: Berrer Agent API
  slug: berrergate-com-agent-api
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: The Research API from Berrer — 1 operation(s) for research.
  name: Berrer Research API
  slug: berrergate-com-research-api
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: The Search API from Berrer — 1 operation(s) for search.
  name: Berrer Search API
  slug: berrergate-com-search-api
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: The Skill.md API from Berrer — 1 operation(s) for skill.md.
  name: Berrer Skill.md API
  slug: berrergate-com-skill-md-api
- baseURL: https://api.berrergate.com
  baseurl_source: declared
  description: The .well Known API from Berrer — 2 operation(s) for .well known.
  name: Berrer .well Known API
  slug: berrergate-com-well-known-api
artifact_total: 19
common:
- group: other
  href: https://artifacts.apis.io/berrergate-com/capabilities/berrergate-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/berrergate-com-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://api.berrergate.com/v1/agent/beta/catalog
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
  href: https://artifacts.apis.io/berrergate-com/llms/berrergate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/berrergate-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.berrergate.com/llms.txt
- group: other
  href: https://artifacts.apis.io/berrergate-com/a2a/berrergate-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/berrergate-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/berrergate-com/mcp/berrergate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/berrergate-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/berrergate-com/mcp/berrergate-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/berrergate-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/berrergate-com/well-known/berrergate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/berrergate-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/berrergate-com/agentic-access/berrergate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/berrergate-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/berrergate-com/security/berrergate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/berrergate-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/berrergate-com/authentication/berrergate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/berrergate-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/berrergate-com/conventions/berrergate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/berrergate-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/berrergate-com/conventions/berrergate-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/berrergate-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/berrergate-com/errors/berrergate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/berrergate-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/berrergate-com/data-model/berrergate-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/berrergate-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/berrergate-com/rate-limits/berrergate-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/berrergate-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/berrergate-com/plans/berrergate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/berrergate-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/berrergate-com/conformance/berrergate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/berrergate-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/berrergate-com/lifecycle/berrergate-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/berrergate-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/berrergate-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/berrergate-com/skills/berrergate-com-provider-skill.md
  title: ''
  type: AgentSkill
  url: skills/berrergate-com-provider-skill.md
- group: build
  href: https://artifacts.apis.io/berrergate-com/packages/berrergate-com-packages.yml
  title: ''
  type: Packages
  url: packages/berrergate-com-packages.yml
- group: other
  href: https://artifacts.apis.io/berrergate-com/overlays/berrergate-com-openapi-overlay.yaml
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
finops:
- has_sources: true
  method: derived
  name: Berrergate Com Finops
  primary_unit: atomic units of usdc per paid query
  service_category: ''
  slug: berrergate-com-finops
  template: false
layout: provider
mcp_servers:
- description: 'BerrerGate publishes ONE remote MCP server at https://api.berrergate.com/mcp, declared in three places the provider controls: the API host''s llms.txt ("MCP: POST https://api.berrergate.com/mcp"), an M'
  name: Berrer MCP Server
  slug: berrergate-com-mcp-yml
- description: ''
  name: MCP server.json manifest (provider-hosted)
  slug: mcp-server-json-manifest-provider-hosted
modified: '2026-09-19'
name: Berrer
nav: Providers
network: true
overview: 'Berrer publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Agent API, Research API, and 5 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The Berrer catalog on APIs.io includes 1 Spectral governance ruleset.


  Berrer''s developer surface includes pricing, documentation, authentication, and 24 more developer resources.'
plans:
- name: Berrergate Com Plans Pricing
  plan_count: 5
  slug: berrergate-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Berrergate Com Rate Limits
  slug: berrergate-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Berrer API Rules
  rule_count: 34
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 6
  slug: berrergate-com-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 66.5
    catalog_earned_first_party: 24.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 44.6
    developer_ergonomics: 33.3
    discoverability: 71.7
    operational_transparency: 31.6
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/berrergate-com/berrergate-com-2026-10-11T101919.png
security:
- kind: authentication
  name: Berrergate Com Authentication
  slug: berrergate-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Berrergate Com Domain Security
  slug: berrergate-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: berrergate-com-evidence-brief
  slug: berrergate-com-evidence-brief
- name: berrergate-com-free-preview-then-buy-decision
  slug: berrergate-com-free-preview-then-buy-decision
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
- Inference
- Research
- Agent-Native
website: https://berrergate.com/
---
