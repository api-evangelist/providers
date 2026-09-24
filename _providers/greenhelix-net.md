---
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.3
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://api.greenhelix.net
  baseurl_source: declared
  description: 'REST API for agent-to-agent commerce: billing and wallets, payment intents and escrow, subscriptions, identity and reputation, marketplace, trust scoring, messaging and negotiation, disputes, webhooks'
  name: A2A Commerce Gateway API
  slug: a2a-commerce-gateway-api
artifact_total: 7
asyncapis:
- description: ''
  name: Greenhelix Net Webhooks
  slug: greenhelix-net-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/security/greenhelix-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greenhelix-net-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/authentication/greenhelix-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/greenhelix-net-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://greenhelix.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.greenhelix.net/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.greenhelix.net/docs.html#getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://api.greenhelix.net/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mirni/a2a
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/mirni/a2a#pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/mirni/a2a/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Support
  url: https://www.greenhelix.net/index.html#contact
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/sandbox/greenhelix-net-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/greenhelix-net-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/a2a/greenhelix-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/greenhelix-net-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/well-known/greenhelix-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greenhelix-net-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/mcp/greenhelix-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/greenhelix-net-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/mcp/greenhelix-net-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/greenhelix-net-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/packages/greenhelix-net-packages.yml
  title: ''
  type: Packages
  url: packages/greenhelix-net-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/packages/greenhelix-net-packages.yml
  title: ''
  type: SDKs
  url: packages/greenhelix-net-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/llms/greenhelix-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greenhelix-net-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/conformance/greenhelix-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/greenhelix-net-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/errors/greenhelix-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/greenhelix-net-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/lifecycle/greenhelix-net-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/greenhelix-net-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/lifecycle/greenhelix-net-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/greenhelix-net-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/conventions/greenhelix-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/greenhelix-net-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/conventions/greenhelix-net-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/greenhelix-net-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/changelog/greenhelix-net-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/greenhelix-net-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/plans/greenhelix-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greenhelix-net-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/rate-limits/greenhelix-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/greenhelix-net-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/asyncapi/greenhelix-net-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/greenhelix-net-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/data-model/greenhelix-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/greenhelix-net-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenhelix-net/refs/heads/main/regulatory/greenhelix-net-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/greenhelix-net-regulatory-posture.yml
created: '2026-09-19'
description: 'Green Helix Consulting, LLC builds infrastructure for autonomous AI-agent commerce. Its A2A Commerce Gateway (api.greenhelix.net, v1.4.10) is a single REST API of 137 tools across 16 services: per-agent wallets and metered billing, authorize-then-capture payment intents, standard and performance-gated escrow, subscriptions and split payments, Ed25519 cryptographic agent identity with verifiable claims and reputation, a service marketplace with matching and ratings, composite trust scoring and SLA checks, end-to-end encrypted agent messaging with price negotiation, dispute resolution, HMAC-signed webhooks and an event bus, plus Stripe, GitHub and PostgreSQL connectors. It publishes an OpenAPI 3.1 contract, a machine-readable tool and tier catalog, an A2A agent card, an ai-plugin.json, Python and TypeScript SDKs, a local MCP server, and a sandbox that resets on every deploy. Errors are RFC 9457, rate limits are signaled in headers, and x402 payment proofs are accepted as an alternative
  to API keys.'
layout: provider
mcp_servers:
- description: Green Helix ships a first-party LOCAL (stdio) MCP server, @greenhelix/mcp-server 0.1.0 on npm, that exposes the A2A Commerce Gateway's tool catalog to Claude Desktop, Cursor, Claude Code, Windsurf and
  name: Green Helix MCP Server
  slug: green-helix-mcp-server
modified: '2026-09-19'
name: Green Helix
nav: Providers
network: true
overview: 'Green Helix publishes 1 API on the [APIs.io](https://apis.io/) network: A2A Commerce Gateway API. Tagged areas include Agents, Agentic Commerce, Payments, Escrow, and Billing.


  The Green Helix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Green Helix''s developer surface includes authentication, documentation, getting-started guide, API reference, GitHub presence, pricing, changelog, and 24 more developer resources.'
plans:
- name: Greenhelix Net Plans Pricing
  plan_count: 4
  slug: greenhelix-net-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Greenhelix Net Rate Limits
  slug: greenhelix-net-rate-limits
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 62.7
    developer_ergonomics: 64.3
    discoverability: 64.8
    operational_transparency: 68.4
  previous_composite: 55.7
  provenance:
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
    score: 27.8
security:
- kind: authentication
  name: Greenhelix Net Authentication
  slug: greenhelix-net-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Greenhelix Net Domain Security
  slug: greenhelix-net-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: greenhelix-net
tags:
- Agents
- Agentic Commerce
- Payments
- Escrow
- Billing
- Marketplace
- Identity
- Trust
- Messaging
- Webhook
- MCP
- A2A
- x402
website: https://greenhelix.net/
---
