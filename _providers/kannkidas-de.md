---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.6
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kannkidas De Agentic Access
  operation_count: 9
  slug: kannkidas-de-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://kannkidas.de/api
  baseurl_source: declared
  description: Faceted product and category search over the published build-or-buy analyses, suggestions and nearest-neighbour products, live availability of the ten fixed sponsor slots, anonymous OAuth 2.0 client r
  name: Kann KI das? API
  slug: kann-ki-das-api
- description: Remote Model Context Protocol server (Streamable HTTP, protocol revision 2025-06-18) at https://kannkidas.de/api/mcp named kannkidas-sponsorship. Anonymous initialize and tools/list succeed and return
  name: Kann KI das? Sponsorship MCP Server
  slug: kann-ki-das-sponsorship-mcp-server
- description: 'Read-only Agent2Agent JSON-RPC endpoint at https://kannkidas.de/api/a2a described by the agent card at /.well-known/agent-card.json (A2A protocolVersion 0.3.0). One skill, list-sponsor-slots, returns '
  name: Kann KI das? Sponsoring Agent (A2A)
  slug: kann-ki-das-sponsoring-agent-a2a
artifact_total: 17
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/agentic-access/kannkidas-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kannkidas-de-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/security/kannkidas-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kannkidas-de-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/authentication/kannkidas-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kannkidas-de-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/scopes/kannkidas-de-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/kannkidas-de-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://kannkidas.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kannkidas.de/agents/
- group: docs
  title: ''
  type: Documentation
  url: https://kannkidas.de/agents/
- group: start
  title: ''
  type: GettingStarted
  url: https://kannkidas.de/AGENTS.md
- group: other
  title: ''
  type: AgentsMd
  url: https://kannkidas.de/AGENTS.md
- group: docs
  title: ''
  type: APIReference
  url: https://kannkidas.de/openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/llms/kannkidas-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kannkidas-de-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://kannkidas.de/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/well-known/kannkidas-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kannkidas-de-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://kannkidas.de/.well-known/api-catalog
- group: other
  title: ''
  type: OpenIDConnect
  url: https://kannkidas.de/.well-known/openid-configuration
- group: other
  title: ''
  type: ContentSignal
  url: https://kannkidas.de/robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/mcp/kannkidas-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kannkidas-de-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/mcp/kannkidas-de-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kannkidas-de-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/a2a/kannkidas-de-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kannkidas-de-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/skills/kannkidas-de-buy-sponsorship.md
  title: ''
  type: AgentSkill
  url: skills/kannkidas-de-buy-sponsorship.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/skills/kannkidas-de-find-software.md
  title: ''
  type: AgentSkill
  url: skills/kannkidas-de-find-software.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/conventions/kannkidas-de-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kannkidas-de-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/conventions/kannkidas-de-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kannkidas-de-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/conformance/kannkidas-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kannkidas-de-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/errors/kannkidas-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kannkidas-de-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/lifecycle/kannkidas-de-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kannkidas-de-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/data-model/kannkidas-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kannkidas-de-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/plans/kannkidas-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kannkidas-de-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/rate-limits/kannkidas-de-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kannkidas-de-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/sandbox/kannkidas-de-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kannkidas-de-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/overlays/kannkidas-de-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kannkidas-de-openapi-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/kannkidas-de/refs/heads/main/json-schema/kannkidas-de-agent-purchase.json
  title: ''
  type: JSONSchema
  url: json-schema/kannkidas-de-agent-purchase.json
- group: commercial
  title: ''
  type: Pricing
  url: https://kannkidas.de/sponsoring/
- group: commercial
  title: ''
  type: Pricing
  url: https://kannkidas.de/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kannkidas.de/nutzungsbedingungen/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kannkidas.de/datenschutz/
- group: company
  title: ''
  type: About
  url: https://kannkidas.de/ueber-uns/
- group: company
  title: ''
  type: Blog
  url: https://kannkidas.de/ratgeber/
- group: company
  title: ''
  type: BlogRSS
  url: https://kannkidas.de/feed.xml
- group: other
  title: ''
  type: Sitemap
  url: https://kannkidas.de/sitemap-index.xml
created: '2026-09-19'
description: 'Kann KI das? is an independent German-language publisher of build-or-buy test reports that assess whether well-known business software can realistically be rebuilt with AI, and where buying remains the better decision. The site is financed by ten fixed, clearly labelled sponsor placements (P01-P10, 990 EUR net for 30 days) that are sold through an agent-native commerce path: a public OpenAPI 3.1.1 contract at kannkidas.de/openapi.json (faceted product search, live slot availability, anonymous OAuth 2.0 client registration and client-credentials tokens, and a buyer-confirmed, idempotent Stripe hosted checkout), a remote Streamable HTTP MCP server with two tools, a read-only A2A agent at /api/a2a with a published agent card, RFC 8414/9728 OAuth discovery, an RFC 9727 API catalog, provider-published Agent Skills with SHA-256 digests, llms.txt and AGENTS.md, a UCP profile, DNS-AID records and a separately marked x402 v2 testnet demo endpoint. The sponsor agent operates in read-only
  mode; commercial writes require OAuth scopes and explicit buyer confirmation.'
examples:
- key_count: 3
  name: Kannkidas De A2A Message Send Example
  slug: kannkidas-de-a2a-message-send-example
- key_count: 3
  name: Kannkidas De List Sponsor Slots Example
  slug: kannkidas-de-list-sponsor-slots-example
- key_count: 3
  name: Kannkidas De Mcp Tools List Example
  slug: kannkidas-de-mcp-tools-list-example
- key_count: 3
  name: Kannkidas De Search Products Example
  slug: kannkidas-de-search-products-example
- key_count: 3
  name: Kannkidas De X402 Buyer Brief 402 Example
  slug: kannkidas-de-x402-buyer-brief-402-example
image: https://kannkidas.de/og-default.jpg
json_schemas:
- name: Sponsor purchase request
  property_count: 2
  slug: kannkidas-de-agent-purchase
layout: provider
mcp_servers:
- description: ''
  name: Kann KI das? Sponsoring Agent MCP Server
  slug: kann-ki-das-sponsoring-agent-mcp-server
- description: ''
  name: Kann KI das? Sponsoring Agent MCP Server
  slug: kann-ki-das-sponsoring-agent-mcp-server-2
modified: '2026-09-19'
name: Kann KI das? Sponsoring Agent
nav: Providers
network: true
overview: 'Kann KI das? Sponsoring Agent publishes 1 API on the [APIs.io](https://apis.io/) network: Kann KI das? API. Tagged areas include Company, Sponsoring, Advertising, Software Reviews, and Build vs Buy.


  Kann KI das? Sponsoring Agent''s developer surface includes authentication, documentation, getting-started guide, API reference, sandbox, pricing, engineering blog, and 34 more developer resources.'
plans:
- name: Kannkidas De Plans Pricing
  plan_count: 3
  slug: kannkidas-de-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Kannkidas De Rate Limits
  slug: kannkidas-de-rate-limits
scopes:
- name: Kannkidas De Scopes
  scope_count: 2
  slug: kannkidas-de-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 51.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 66.7
    discoverability: 87.0
    operational_transparency: 0.0
  previous_composite: 2.8
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
    score: 54.7
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Kannkidas De Authentication
  slug: kannkidas-de-authentication
  summary_line: none/http/oauth2 · 2 schemes
- kind: domain-security
  name: Kannkidas De Domain Security
  slug: kannkidas-de-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
slug: kannkidas-de
tags:
- Company
- Sponsoring
- Advertising
- Software Reviews
- Build vs Buy
- Search
- agent-native
- MCP
- A2A
- Authentication
- x402
- Stripe Checkout
- Germany
website: https://kannkidas.de/
---
