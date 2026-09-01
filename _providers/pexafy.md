---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Pexafy Agentic Access
  operation_count: 37
  slug: pexafy-agentic-access
  summary_line: 37 operations · 10 acting
api_count: 2
apis:
- description: Saved sets, owned by an API key.
  name: Pexafy Collections API
  slug: pexafy-collections-api
- description: What the filters accept.
  name: Pexafy Facets API
  slug: pexafy-facets-api
- description: One photo at a time.
  name: Pexafy Photos API
  slug: pexafy-photos-api
- description: Finding photos.
  name: Pexafy Search API
  slug: pexafy-search-api
- description: Quota counters.
  name: Pexafy Usage API
  slug: pexafy-usage-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.pexafy.com/mcp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pexafy.com
- group: operate
  title: ''
  type: Support
  url: https://pexafy.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://pexafy.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://pexafy.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pexafy
- group: start
  title: ''
  type: Login
  url: https://pexafy.com/auth/login/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pexafy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pexafy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pexafy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pexafy-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pexafy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pexafy-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pexafy-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/pexafy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pexafy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pexafy-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pexafy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pexafy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pexafy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/Pexafy/pexafy-openapi
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pexafy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pexafy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pexafy-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexafy-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pexafy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pexafy-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-27'
description: Pexafy is a semantic (meaning-based) search engine over free-licence stock photography. One request queries nine free stock-photo libraries — Unsplash, Pexels, Pixabay, StockSnap, Picjumbo, Kaboompics, Burst, Skitterphoto and NegativeSpace, plus Wikimedia Commons since description 1.3.0 — and returns every photo in one normalised JSON schema with dimensions, dominant colour, orientation, photographer, licence and a ready-made attribution string. Queries are written as full sentences in any of 100+ languages and ranked by meaning rather than keyword overlap; an image can be posted instead of text to find visually similar photos, and results can be filtered by colour, orientation, licence, source, photographer or date. The API is self-serve — a key is issued immediately from the dashboard with no application review and no mandatory download-tracking callback — and the same catalogue is exposed to LLM clients through a hosted, OAuth-protected MCP server at mcp.pexafy.com.
image: https://pexafy.com/static/img/favicon.png
layout: provider
mcp_servers:
- description: 'Live MCP, gated: initialize returns 401 with an explicit OAuth prompt ("This MCP server needs to know who you are"). Present and auth-required, not absent. Verified 2026-08-31.'
  name: Pexafy MCP Server
  slug: pexafy-mcp-server
- description: ''
  name: Pexafy MCP Server
  slug: pexafy-mcp-server-2
modified: '2026-08-27'
name: Pexafy
nav: Providers
network: true
overview: 'Pexafy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Facets API, Photos API, and 2 more. Tagged areas include Image, Photos, Stock Photos, Image Search, and Semantic Search.


  Pexafy''s developer surface includes support, engineering blog, authentication, CLI, changelog, and 23 more developer resources.'
plans:
- name: Pexafy Plans Pricing
  plan_count: 7
  slug: pexafy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Pexafy Rate Limits
  slug: pexafy-rate-limits
scopes:
- name: Pexafy Scopes
  scope_count: 2
  slug: pexafy-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 52.6
    developer_ergonomics: 78.6
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 64.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Pexafy Authentication
  slug: pexafy-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Pexafy Domain Security
  slug: pexafy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pexafy
tags:
- Image
- Photos
- Stock Photos
- Image Search
- Semantic Search
- Computer-Vision
- Embeddings
- MCP
- agent-native
- Content Licensing
website: https://docs.pexafy.com
---
