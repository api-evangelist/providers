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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Muj428 Com Agentic Access
  operation_count: 24
  slug: muj428-com-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 3
apis:
- baseURL: https://wepmhfjzckclvywolrek.supabase.co/functions/v1/trust-layer
  baseurl_source: declared
  description: REST facade for the MUJ428 Trust Layer, served as Supabase edge functions at https://wepmhfjzckclvywolrek.supabase.co/functions/v1/trust-layer and named as the canonical production facade by the provi
  name: MUJ428 Trust Layer API
  slug: muj428-trust-layer-api
- description: 'Remote Model Context Protocol server, Streamable HTTP, POST only, at https://wepmhfjzckclvywolrek.supabase.co/functions/v1/trust-layer-mcp (protocol version 2025-06-18, serverInfo "MUJ428 Trust Layer '
  name: MUJ428 Trust Layer MCP Server
  slug: muj428-trust-layer-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://agents.muj428.com/.well-known/agent-card.json (name "MUJ428 Trust Reflex", version 1.8.3, provider MUJ428 LLC) declaring eleven skills — agent re'
  name: MUJ428 Trust Reflex A2A Agent
  slug: muj428-trust-reflex-a2a-agent
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/security/muj428-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/muj428-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/agentic-access/muj428-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/muj428-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://agents.muj428.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agents.muj428.com/AGENTS.md
- group: docs
  title: ''
  type: APIReference
  url: https://agents.muj428.com/developer.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agents.muj428.com/index.md
- group: operate
  title: ''
  type: FAQ
  url: https://agents.muj428.com/muj428-trust-faq.html
- group: other
  title: ''
  type: Glossary
  url: https://agents.muj428.com/glossary.md
- group: commercial
  title: ''
  type: Pricing
  url: https://agents.muj428.com/pricing.json
- group: other
  title: ''
  type: Sitemap
  url: https://agents.muj428.com/sitemap.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/a2a/muj428-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/muj428-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/mcp/muj428-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/muj428-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/mcp/muj428-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/muj428-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/well-known/muj428-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/muj428-com-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://agents.muj428.com/.well-known/api-catalog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/llms/muj428-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/muj428-com-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/packages/muj428-com-packages.yml
  title: ''
  type: Packages
  url: packages/muj428-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/packages/muj428-com-packages.yml
  title: ''
  type: SDKs
  url: packages/muj428-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/authentication/muj428-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/muj428-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/conformance/muj428-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/muj428-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/errors/muj428-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/muj428-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/lifecycle/muj428-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/muj428-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/changelog/muj428-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/muj428-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/conventions/muj428-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/muj428-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/conventions/muj428-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/muj428-com-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/sandbox/muj428-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/muj428-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/data-model/muj428-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/muj428-com-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/plans/muj428-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/muj428-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/rate-limits/muj428-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/muj428-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/muj428-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'MUJ428 LLC operates the MUJ428 Trust Layer ("VERIFY BEFORE ACT"), a machine-native trust preflight service for autonomous agents: an agent POSTs the consequential action it is about to take (PAY, BUY, DELEGATE, TRUST, ACCEPT, APPROVE, WRITE, RELEASE, COMMIT, PROPOSE) and receives an ALLOW / VERIFY / REQUIRE_VERIFICATION / DENY decision plus a portable Trust Receipt v1.3, while the caller keeps execution authority and MUJ428 never moves funds. The first 1,000 qualifying decisions per caller_ref are free with no account, key or wallet; paid continuation and the evidence-signal, reputation-check, milestone-attestation, trust-report and transaction-assurance services are settled in USDC on Base (eip155:8453) through x402. The same surface is published as a 24-operation OpenAPI 3.1 REST facade hosted on Supabase edge functions, a remote Streamable-HTTP MCP server listed in the official MCP registry, an A2A agent card with a Trust Reflex extension, an RFC 9727 api-catalog, an llms.txt,
  AGENTS.md and a tarball-distributed JavaScript client, all discoverable from agents.muj428.com.'
layout: provider
mcp_servers:
- description: ''
  name: MUJ428 MCP Server
  slug: muj428-mcp-server
- description: ''
  name: MUJ428 Trust Layer MCP endpoint (canonical, Streamable HTTP)
  slug: muj428-trust-layer-mcp-endpoint-canonical-streamable-http
- description: ''
  name: MUJ428 Trust Layer MCP compatibility facade (Streamable HTTP)
  slug: muj428-trust-layer-mcp-compatibility-facade-streamable-http
modified: '2026-09-19'
name: MUJ428
nav: Providers
network: true
overview: 'MUJ428 publishes 1 API on the [APIs.io](https://apis.io/) network: Trust Layer API. Tagged areas include Agents, Agent Trust, Agentic Commerce, A2A, and MCP.


  MUJ428''s developer surface includes documentation, API reference, getting-started guide, FAQ, pricing, authentication, changelog, and 23 more developer resources.'
plans:
- name: Muj428 Com Plans Pricing
  plan_count: 7
  slug: muj428-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Muj428 Com Rate Limits
  slug: muj428-com-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 40.1
    developer_ergonomics: 61.9
    discoverability: 88.9
    operational_transparency: 36.8
  previous_composite: 45.1
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Muj428 Com Authentication
  slug: muj428-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Muj428 Com Domain Security
  slug: muj428-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: muj428-com
tags:
- Agents
- Agent Trust
- Agentic Commerce
- A2A
- MCP
- x402
- Payments
- Risk Management
- Verification
- Agent-Native
website: https://agents.muj428.com/
---
