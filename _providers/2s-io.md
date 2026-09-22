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
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 105
  human_in_the_loop: 2
  name: 2S Io Agentic Access
  operation_count: 575
  slug: 2s-io-agentic-access
  summary_line: 575 operations · 105 acting · 2 human-in-the-loop
api_count: 3
apis:
- baseURL: https://2s.io
  baseurl_source: declared
  description: 'The full 2s REST catalog: 575 operations (470 GET, 105 POST) in one OpenAPI 3.1.0 document with servers[] https://2s.io, one tag per operation across 112 groups, a unique operationId (group_name) and '
  name: 2s API
  slug: 2s-api
- description: Remote Model Context Protocol server at https://2s.io/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo 2s.io 1.0.0). initialize and tools/list answer anonymously with 575 tools
  name: 2s MCP Server
  slug: 2s-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://2s.io/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 1.0.0, provider 2s) advertising a single skil'
  name: 2s A2A Agent
  slug: 2s-a2a-agent
artifact_total: 11
asyncapis:
- description: ''
  name: 2S Io Watchers Webhooks
  slug: 2s-io-watchers-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://2s.io/
- group: docs
  title: ''
  type: Documentation
  url: https://2s.io/learn/x402
- group: docs
  title: ''
  type: APIReference
  url: https://2s.io/discover
- group: start
  title: ''
  type: GettingStarted
  url: https://2s.io/learn/x402/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://2s.io/discover
- group: operate
  title: ''
  type: StatusPage
  url: https://2s.io/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/changelog/2s-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/2s-io-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://2s.io/changelog.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/2s-io
- group: operate
  title: ''
  type: Support
  url: https://github.com/2s-io/sdk/issues
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/a2a/2s-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/2s-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/mcp/2s-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/2s-io-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/llms/2s-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/2s-io-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/well-known/2s-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/2s-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/well-known/2s-io-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/2s-io-api-catalog.json
- group: other
  title: ''
  type: APIsJson
  url: https://2s.io/apis.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/well-known/2s-io-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/2s-io-ai-plugin.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/packages/2s-io-packages.yml
  title: ''
  type: Packages
  url: packages/2s-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/packages/2s-io-packages.yml
  title: ''
  type: SDKs
  url: packages/2s-io-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/authentication/2s-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/2s-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/conventions/2s-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/2s-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/conventions/2s-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/2s-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/errors/2s-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/2s-io-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/rate-limits/2s-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/2s-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/plans/2s-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/2s-io-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/sandbox/2s-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/2s-io-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/conformance/2s-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/2s-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/lifecycle/2s-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/2s-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/asyncapi/2s-io-watchers-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/2s-io-watchers-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/agentic-access/2s-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/2s-io-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/data-model/2s-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/2s-io-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/2s-io/refs/heads/main/security/2s-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2s-io-domain-security.yml
created: '2026-09-19'
description: '2s ("the (most) everything API", 2s.io) is a pay-per-call REST API built for AI agents: 575 endpoints across 112 groups on one origin — US public records and government data, company and legal identifiers (GLEIF, OFAC, state registries), SEC filings, crypto and web3, security and CVEs, patents and case law, medical codes, weather and geocoding, ANSI X12 / EDIFACT EDI, an OpenAI-compatible AI gateway (chat, image, multi-model council) and wallet-scoped agent infrastructure (kv/doc/vector/blob store, locks, queues, schedules, pub/sub and 26 kinds of signed-callback watchers). There are no accounts and no API keys: every call is paid in USDC on Base or Solana through the x402 protocol (HTTP 402 → sign → retry), with a free trial call per endpoint per hour and actual-usage "upto" billing on AI endpoints. The same catalog is published as an OpenAPI 3.1.0 contract at https://2s.io/openapi.json, a remote MCP server at https://2s.io/mcp (plus the npx @2sio/mcp local server), an A2A
  0.3.0 agent card whose one skill is endpoint discovery, an RFC 9727 API catalog, an APIs.json index, an llms.txt, an MCP server card, an x402 manifest and an ERC-8004 on-chain agent registration. Maintained by an individual operator (alley@2s.io); the SDK monorepo is github.com/2s-io/sdk.'
image: https://2s.io/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: 2s MCP Server
  slug: 2s-mcp-server
- description: ''
  name: 2s hosted MCP endpoint (Streamable HTTP)
  slug: 2s-hosted-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: 2s
nav: Providers
network: true
overview: '2s publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Agentic Commerce, x402, MCP, and A2A.


  The 2s catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  2s'' developer surface includes documentation, API reference, getting-started guide, pricing, changelog, support, authentication, and 26 more developer resources.'
plans:
- name: 2S Io Plans Pricing
  plan_count: 0
  slug: 2s-io-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: 2S Io Rate Limits
  slug: 2s-io-rate-limits
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 66.7
    discoverability: 81.5
    operational_transparency: 76.3
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 50.0
security:
- kind: authentication
  name: 2S Io Authentication
  slug: 2s-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: 2S Io Domain Security
  slug: 2s-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 2s-io
tags:
- Agents
- Agentic Commerce
- x402
- MCP
- A2A
- Public Records
- Government Data
- Finance
- Crypto
- Security
- Legal
- Weather
- Geocoding
- EDI
- AI Gateway
- Agent Infrastructure
- Webhook
- agent-native
website: https://2s.io/
---
