---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.5
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: 'The Moz API is a JSON-RPC 2.0 API accessed through HTTP POST requests to a single universal endpoint, https://api.moz.com/jsonrpc. The method name in the request body selects the operation. 62 public '
  name: Moz API
  slug: moz-api
- description: Beta remote Model Context Protocol server exposing Moz Data API tools (site metrics, links, keywords, rankings) to LLM hosts such as Claude Desktop, ChatGPT Desktop and Claude Code. Streamable HTTP tr
  name: Moz MCP Server - Data
  slug: moz-mcp-server-data
- description: 'Beta remote Model Context Protocol server exposing Moz Local tools for managing and reporting on business locations and listings. Streamable HTTP transport; OAuth 2.1 sign-in inside the client, or an '
  name: Moz MCP Server - Local
  slug: moz-mcp-server-local
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://moz.com/products/api
- group: docs
  title: ''
  type: Documentation
  url: https://moz.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://moz.com/api/docs/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://moz.com/api/docs/guides/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://moz.com/products/api/pricing
- group: start
  title: ''
  type: Login
  url: https://moz.com/api/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moz.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moz.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://moz.com/help
- group: operate
  title: ''
  type: Community
  url: https://moz.com/community
- group: company
  title: ''
  type: Blog
  url: https://moz.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seomoz
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moz-mcp.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/moz-api-schema.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/moz-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moz-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moz-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moz-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moz-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moz-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moz-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moz-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/moz-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/moz-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moz-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/moz-security.txt
- group: auth
  title: ''
  type: Security
  url: security/moz-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moz-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/moz-examples.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moz-vulnerability-disclosure.yml
created: '2026-08-26'
description: 'Moz is a Seattle-based search-marketing software company, founded in 2004 as SEOmoz and part of Ziff Davis since 2021, whose products include Moz Pro, Moz Local, STAT and Moz Data. Its developer surface is the Moz API, a JSON-RPC 2.0 API served from a single universal endpoint at https://api.moz.com/jsonrpc, exposing 62 public methods across five namespaces: site metrics (Domain Authority, Page Authority, Brand Authority, Spam Score), the Moz Link Index (links, linking root domains, anchor text, link intersect, link status, final redirect), keyword metrics (volume, difficulty, opportunity, priority, search intent, related keywords), ranking and top-page data, and Moz Local location, group, account, listing-network and Google Business Profile insight management. Requests are authenticated with a Moz API token in an x-moz-token header, billed against a row-based monthly quota, and Moz additionally runs two beta remote MCP servers - Moz Data and Moz Local - at https://api.moz.com/mcp/v1/data
  and https://api.moz.com/mcp/v1/local, protected by OAuth 2.1 with PKCE and RFC 9728 protected-resource metadata.'
image: https://moz.com/images/cms/Moz-OG-Image-2024.jpg
json_schemas:
- name: Moz Api
  property_count: 0
  slug: moz-api
layout: provider
mcp_servers:
- description: Moz operates two first-party remote MCP servers, split by product. Both are documented on the Moz API docs site and both answered a live tools/list probe with an RFC 9728 OAuth challenge, which confir
  name: Moz MCP Servers
  slug: moz-mcp-servers
modified: '2026-08-26'
name: Moz
nav: Providers
network: true
overview: 'Moz publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Search, Marketing, Analytics, and Keywords.


  Moz''s developer surface includes documentation, API reference, getting-started guide, pricing, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Moz Plans Pricing
  plan_count: 7
  slug: moz-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Moz Rate Limits
  slug: moz-rate-limits
scopes:
- name: Moz Scopes
  scope_count: 0
  slug: moz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 49.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 58.9
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 43.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moz/refs/heads/main/screenshots/moz-2026-09-02T150638.png
security:
- kind: authentication
  name: Moz Authentication
  slug: moz-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Moz Domain Security
  slug: moz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moz Vulnerability Disclosure
  slug: moz-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Moz Trust Center
  slug: moz-trust-center
  summary_line: trust center published
slug: moz
tags:
- SEO
- Search
- Marketing
- Analytics
- Keywords
- Backlinks
- Local Marketing
- Domain Authority
- Link Index
- JSON-RPC
- MCP
- Company
website: https://moz.com/
---
