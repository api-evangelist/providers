---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_tool_quality: full
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 68.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kannkidas De Agentic Access
  operation_count: 9
  slug: kannkidas-de-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: Remote Model Context Protocol server (Streamable HTTP, protocol revision 2025-06-18) at https://kannkidas.de/api/mcp named kannkidas-sponsorship. Anonymous initialize and tools/list succeed and return
  name: Kann KI das? Sponsorship MCP Server
  slug: kann-ki-das-sponsorship-mcp-server
- description: 'Read-only Agent2Agent JSON-RPC endpoint at https://kannkidas.de/api/a2a described by the agent card at /.well-known/agent-card.json (A2A protocolVersion 0.3.0). One skill, list-sponsor-slots, returns '
  name: Kann KI das? Sponsoring Agent (A2A)
  slug: kann-ki-das-sponsoring-agent-a2a
- baseURL: https://kannkidas.de/api
  baseurl_source: declared
  description: The Agent API from Kann KI das? Sponsoring Agent — 3 operation(s) for agent.
  name: Kann KI das? Sponsoring Agent Agent API
  slug: kannkidas-de-agent-api
- baseURL: https://kannkidas.de/api
  baseurl_source: declared
  description: The Kann KI Das? API API from Kann KI das? Sponsoring Agent — 1 operation(s) for kann ki das? api.
  name: Kann KI das? Sponsoring Agent Kann KI Das? API
  slug: kannkidas-de-kann-ki-das-api-api
- baseURL: https://kannkidas.de/api
  baseurl_source: declared
  description: The Oauth API from Kann KI das? Sponsoring Agent — 1 operation(s) for oauth.
  name: Kann KI das? Sponsoring Agent OAuth API
  slug: kannkidas-de-oauth-api
- baseURL: https://kannkidas.de/api
  baseurl_source: declared
  description: The Search API from Kann KI das? Sponsoring Agent — 3 operation(s) for search.
  name: Kann KI das? Sponsoring Agent Search API
  slug: kannkidas-de-search-api
- baseURL: https://kannkidas.de/api
  baseurl_source: declared
  description: The Slots API from Kann KI das? Sponsoring Agent — 1 operation(s) for slots.
  name: Kann KI das? Sponsoring Agent Slots API
  slug: kannkidas-de-slots-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/kannkidas-de/capabilities/kannkidas-de-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kannkidas-de-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kannkidas-de/agentic-access/kannkidas-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kannkidas-de-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kannkidas-de/security/kannkidas-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kannkidas-de-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kannkidas-de/authentication/kannkidas-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kannkidas-de-authentication.yml
- group: auth
  href: https://artifacts.apis.io/kannkidas-de/scopes/kannkidas-de-scopes.yml
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
  href: https://artifacts.apis.io/kannkidas-de/llms/kannkidas-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kannkidas-de-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://kannkidas.de/llms.txt
- group: agent
  href: https://artifacts.apis.io/kannkidas-de/well-known/kannkidas-de-well-known.yml
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
  href: https://artifacts.apis.io/kannkidas-de/mcp/kannkidas-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kannkidas-de-mcp.yml
- group: build
  href: https://artifacts.apis.io/kannkidas-de/mcp/kannkidas-de-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kannkidas-de-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/kannkidas-de/a2a/kannkidas-de-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kannkidas-de-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kannkidas-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kannkidas-de/skills/kannkidas-de-buy-sponsorship.md
  title: ''
  type: AgentSkill
  url: skills/kannkidas-de-buy-sponsorship.md
- group: agent
  href: https://artifacts.apis.io/kannkidas-de/skills/kannkidas-de-find-software.md
  title: ''
  type: AgentSkill
  url: skills/kannkidas-de-find-software.md
- group: design
  href: https://artifacts.apis.io/kannkidas-de/conventions/kannkidas-de-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kannkidas-de-conventions.yml
- group: design
  href: https://artifacts.apis.io/kannkidas-de/conventions/kannkidas-de-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kannkidas-de-conventions.yml
- group: design
  href: https://artifacts.apis.io/kannkidas-de/conformance/kannkidas-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kannkidas-de-conformance.yml
- group: design
  href: https://artifacts.apis.io/kannkidas-de/errors/kannkidas-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kannkidas-de-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kannkidas-de/lifecycle/kannkidas-de-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kannkidas-de-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kannkidas-de/data-model/kannkidas-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kannkidas-de-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/kannkidas-de/plans/kannkidas-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kannkidas-de-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kannkidas-de/rate-limits/kannkidas-de-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kannkidas-de-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/kannkidas-de/sandbox/kannkidas-de-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kannkidas-de-sandbox.yml
- group: other
  href: https://artifacts.apis.io/kannkidas-de/overlays/kannkidas-de-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kannkidas-de-openapi-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/kannkidas-de/json-schema/kannkidas-de-agent-purchase.json
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
finops:
- has_sources: true
  method: derived
  name: Kannkidas De Finops
  primary_unit: sponsorplatz (p01 bis p10)
  service_category: ''
  slug: kannkidas-de-finops
  template: false
image: https://kannkidas.de/og-default.jpg
json_schemas:
- name: Sponsor purchase request
  property_count: 2
  slug: kannkidas-de-agent-purchase
layout: provider
mcp_servers:
- description: Kann KI das? operates ONE remote MCP server, kannkidas-sponsorship, at https://kannkidas.de/api/mcp over Streamable HTTP. An anonymous initialize returned protocolVersion 2025-06-18 and serverInfo {na
  name: Kann KI das? Sponsoring Agent MCP Server
  slug: kannkidas-de-mcp-yml
modified: '2026-09-19'
name: Kann KI das? Sponsoring Agent
nav: Providers
network: true
overview: 'Kann KI das? Sponsoring Agent publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Kann KI Das? API, OAuth API, and 4 more. Tagged areas include Company, Sponsoring, Advertising, Software Reviews, and Build vs Buy.


  The Kann KI das? Sponsoring Agent catalog on APIs.io includes 1 Spectral governance ruleset.


  Kann KI das? Sponsoring Agent''s developer surface includes authentication, documentation, getting-started guide, API reference, sandbox, pricing, engineering blog, and 35 more developer resources.'
plans:
- name: Kannkidas De Plans Pricing
  plan_count: 1
  slug: kannkidas-de-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Kannkidas De Rate Limits
  slug: kannkidas-de-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Kann KI das? Sponsoring Agent API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 1
  slug: kannkidas-de-rules
scopes:
- name: Kannkidas De Scopes
  scope_count: 2
  slug: kannkidas-de-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 57.9
    catalog_earned_first_party: 8.0
    catalog_gap: 57.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 55.9
    developer_ergonomics: 40.5
    discoverability: 85.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kannkidas-de/kannkidas-de-2026-10-11T110049.png
security:
- kind: authentication
  name: Kannkidas De Authentication
  slug: kannkidas-de-authentication
  summary_line: none/http/oauth2 · 2 schemes
- kind: domain-security
  name: Kannkidas De Domain Security
  slug: kannkidas-de-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
skill_count: 2
skills:
- name: buy-sponsorship
  slug: kannkidas-de-buy-sponsorship
- name: find-software
  slug: kannkidas-de-find-software
slug: kannkidas-de
tags:
- Company
- Sponsoring
- Advertising
- Software Reviews
- Build vs Buy
- Search
- Agent-Native
- MCP
- A2A
- OAuth
- x402
- Stripe Checkout
- Germany
- Authentication
website: https://kannkidas.de/
---
