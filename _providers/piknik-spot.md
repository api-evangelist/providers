---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.9
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 362
  human_in_the_loop: 4
  name: Piknik Spot Agentic Access
  operation_count: 683
  slug: piknik-spot-agentic-access
  summary_line: 683 operations · 362 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: REST API under https://piknik.spot/api covering participants (places), offerings and pack prices, service locations, marketplace listings, events and RSVPs, jobs, recipes, associations and place tours
  name: Piknik.Spot REST API
  slug: piknikspot-rest-api
- description: Hosted, remote Model Context Protocol server (protocol 2025-03-26, Streamable HTTP with an SSE endpoint at /api/mcp/sse) exposing 62 tools and 7 piknik:// resources for local-food discovery, Local Foo
  name: Piknik.Spot MCP Server
  slug: piknikspot-mcp-server
- description: 'Agent-to-Agent (A2A 1.0) agent served from the provider''s own host: the agent card at /.well-known/agent-card.json (also at the legacy /.well-known/agent.json, byte-identical) declares five public ski'
  name: Piknik.Spot A2A Agent
  slug: piknikspot-a2a-agent
artifact_total: 12
asyncapis:
- description: ''
  name: Piknik Spot Webhooks
  slug: piknik-spot-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://piknik.spot/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/security/piknik-spot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/piknik-spot-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/agentic-access/piknik-spot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/piknik-spot-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/scopes/piknik-spot-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/piknik-spot-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/authentication/piknik-spot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/piknik-spot-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://piknik.spot/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://piknik.spot/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://piknik.spot/skills/piknik-rest-api/SKILL.md
- group: operate
  title: ''
  type: Support
  url: https://piknik.spot/contact
- group: start
  title: ''
  type: SignUp
  url: https://piknik.spot/signup
- group: start
  title: ''
  type: Login
  url: https://piknik.spot/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://piknik.spot/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://piknik.spot/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://piknik.spot/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/mcp/piknik-spot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/piknik-spot-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/a2a/piknik-spot-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/piknik-spot-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/llms/piknik-spot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/piknik-spot-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/well-known/piknik-spot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/piknik-spot-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/mcp/piknik-spot-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/piknik-spot-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/conventions/piknik-spot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/piknik-spot-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/conventions/piknik-spot-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/piknik-spot-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/errors/piknik-spot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/piknik-spot-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/data-model/piknik-spot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/piknik-spot-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/rate-limits/piknik-spot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/piknik-spot-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/plans/piknik-spot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/piknik-spot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/lifecycle/piknik-spot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/piknik-spot-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/conformance/piknik-spot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/piknik-spot-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/overlays/piknik-spot-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/piknik-spot-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/piknik-spot/refs/heads/main/asyncapi/piknik-spot-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/piknik-spot-webhooks.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://piknik.spot/privacy-policy
created: '2026-09-19'
description: 'Piknik (piknik.spot) is a local food system platform based in Waterloo Region, Ontario, Canada that maps farms, processors, markets, shops, restaurants, community gardens and food hubs, the supply links between them, marketplace listings, community events, jobs and volunteer posts, recipes, and a Local Food Score for any address. It is built agent-first: a REST API under https://piknik.spot/api described by a 683-operation OpenAPI 3.0.3 document, a hosted Model Context Protocol server at https://piknik.spot/api/mcp exposing 62 tools (public discovery tools anonymously, write tools behind OAuth 2.0 with PKCE and dynamic client registration or pik_pat_ personal access tokens), an A2A 1.0 agent card served at /.well-known/agent-card.json with a JSON-RPC endpoint at /api/a2a, an llms.txt, provider-published Agent Skills, and a published Agent Ethics policy that permits only immediate-use access and forbids bulk extraction, retention and model training.'
image: https://piknik.spot/icons/icon-512x512.png
layout: provider
mcp_servers:
- description: ''
  name: Piknik.Spot MCP Server
  slug: piknikspot-mcp-server
- description: ''
  name: Piknik.Spot MCP Server
  slug: piknikspot-mcp-server-2
modified: '2026-09-19'
name: Piknik.Spot
nav: Providers
network: true
overview: 'Piknik.Spot publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Local Food, Agriculture, Farmers Markets, Marketplace, and Event.


  The Piknik.Spot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Piknik.Spot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 25 more developer resources.'
plans:
- name: Piknik Spot Plans Pricing
  plan_count: 0
  slug: piknik-spot-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Piknik Spot Rate Limits
  slug: piknik-spot-rate-limits
scopes:
- name: Piknik Spot Scopes
  scope_count: 4
  slug: piknik-spot-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 58.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Piknik Spot Authentication
  slug: piknik-spot-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Piknik Spot Domain Security
  slug: piknik-spot-domain-security
  summary_line: TLSv1.3 · HSTS
slug: piknik-spot
tags:
- Local Food
- Agriculture
- Farmers Markets
- Marketplace
- Event
- Job
- Recipes
- Geolocation
- Community
- Food Systems
- MCP
- A2A
- Agent-Native
- Ontario
- Canada
website: https://piknik.spot/
---
