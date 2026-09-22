---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Fashionbyu Com Agentic Access
  operation_count: 108
  slug: fashionbyu-com-agentic-access
  summary_line: 108 operations · 20 acting
api_count: 1
apis:
- baseURL: https://mirror.fashionbyu.com/iriz/v1
  baseurl_source: declared
  description: First-party REST API of the IRIZ storefront platform, described by an auto-generated OpenAPI 3.0.0 document (info.title "IRIZ Platform API", info.version v4.10.829+api-v1, 108 operations, no operation
  name: IRIZ Platform API
  slug: iriz-platform-api
- description: Hosted, remote MCP server (serverInfo iriz-agent-commerce 1.0.0, protocolVersion 2025-06-18, transport streamable-http) at https://mirror.fashionbyu.com/iriz/v1/agent/mcp (the legacy /iriz/agent/mcp s
  name: IRIZ Storefront Commerce MCP Server
  slug: iriz-storefront-commerce-mcp-server
- description: A2A agent card ("IRIZ Platform Agent", version 1.0.0, protocolVersions ["0.3","A2A-1.4"]) served at the legacy path https://mirror.fashionbyu.com/.well-known/agent.json and at https://fashionbyu.com/.
  name: IRIZ Platform A2A Interop Agent
  slug: iriz-platform-a2a-interop-agent
artifact_total: 10
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/security/fashionbyu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fashionbyu-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/agentic-access/fashionbyu-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fashionbyu-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/authentication/fashionbyu-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fashionbyu-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fashionbyu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mirror.fashionbyu.com/iriz/docs
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/llms/fashionbyu-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fashionbyu-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://fashionbyu.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/a2a/fashionbyu-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fashionbyu-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/mcp/fashionbyu-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fashionbyu-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/mcp/fashionbyu-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fashionbyu-com-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/conventions/fashionbyu-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fashionbyu-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/errors/fashionbyu-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fashionbyu-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/lifecycle/fashionbyu-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fashionbyu-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://mirror.fashionbyu.com/iriz/docs/versioning
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/conformance/fashionbyu-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fashionbyu-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/plans/fashionbyu-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fashionbyu-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fashionbyu-com/refs/heads/main/rate-limits/fashionbyu-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fashionbyu-com-rate-limits.yml
created: '2026-09-19'
description: 'IRIZ Platform is the multi-brand, agent-first fashion storefront platform behind fashionbyu.com (brands such as BWET Swimwear, Me+Em, Kitri Studio, Lisou London and Réalisation Par are hosted as /brand/<slug> storefronts). It publishes a first-party OpenAPI 3.0.0 ("IRIZ Platform API", 108 operations, canonical base path /iriz/v1/) at https://mirror.fashionbyu.com/iriz/v1/docs/spec.json with a Swagger UI at /iriz/docs, a live hosted MCP server (iriz-agent-commerce, protocol 2025-06-18, nine tools: search_catalog, get_product_feed, get_policies, create_cart, mutate_cart, get_cart, quote_cart, confirm_checkout, get_order) whose tools/list answers unauthenticated, two A2A agent cards (a Storefront Commerce card at the canonical /.well-known/agent-card.json and a Platform Interop card at the legacy /.well-known/agent.json, both flavored: protocolVersions[] instead of protocolVersion), an llms.txt and an agent-welcoming robots.txt, and per-brand OpenAI/ACP-compatible product feeds
  (/brand/<slug>/feed.json) with schema.org Product JSON-LD. The platform runs on Cloudflare Workers (D1/KV/R2/queues/Durable Objects per /iriz/health); HTML pages sit behind a Cloudflare managed challenge while the JSON surfaces answer directly. The registrable domain fashionbyu.com serves the interop card, llms.txt and the brand feeds but 404s the MCP and REST routes, which live on mirror.fashionbyu.com; every link inside the provider''s own llms.txt and robots.txt points at www.fashionbyu.com, which does not resolve (NXDOMAIN on 2026-09-19).'
layout: provider
mcp_servers:
- description: ''
  name: IRIZ Platform MCP Server
  slug: iriz-platform-mcp-server
- description: ''
  name: MCP endpoint (streamable-http, canonical v1)
  slug: mcp-endpoint-streamable-http-canonical-v1
modified: '2026-09-19'
name: IRIZ Platform
nav: Providers
network: true
overview: 'IRIZ Platform publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, E-Commerce, Agentic Commerce, and Storefront.


  IRIZ Platform''s developer surface includes authentication, documentation, and 16 more developer resources.'
plans:
- name: Fashionbyu Com Plans Pricing
  plan_count: 0
  slug: fashionbyu-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Fashionbyu Com Rate Limits
  slug: fashionbyu-com-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 10.4
    developer_ergonomics: 30.4
    discoverability: 72.2
    operational_transparency: 7.9
  previous_composite: 17.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Fashionbyu Com Authentication
  slug: fashionbyu-com-authentication
  summary_line: apiKey/http/none/hmac-signature/http-message-signature · 6 schemes
- kind: domain-security
  name: Fashionbyu Com Domain Security
  slug: fashionbyu-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fashionbyu-com
tags:
- Company
- Fashion
- E-Commerce
- Agentic Commerce
- Storefront
- Product Feeds
- MCP
- A2A
- AI Agents
- Checkout
- Cart
- Order
- Cloudflare Workers
website: https://fashionbyu.com/
---
