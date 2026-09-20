---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: Upway's agent-facing commerce surface. A remote Model Context Protocol server at https://upway.co/api/ucp/mcp implementing the Universal Commerce Protocol shopping service, version 2026-08-25. Anonymo
  name: Upway Commerce (UCP MCP) API
  slug: upway-commerce-ucp-mcp
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/security/upway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upway.co/
- group: docs
  title: ''
  type: Documentation
  url: https://upway.co/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.upway.co/en-US
- group: company
  title: ''
  type: Blog
  url: https://upway.co/blogs/news
- group: start
  title: ''
  type: Login
  url: https://upway.co/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upway.co/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upway.co/policies/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopupway
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/llms/upway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upway-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/well-known/upway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upway-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/mcp/upway-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/upway-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/authentication/upway-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upway-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/scopes/upway-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/upway-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/conventions/upway-conventions.yml
  title: ''
  type: Conventions
  url: conventions/upway-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/conventions/upway-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/upway-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/errors/upway-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/upway-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/rate-limits/upway-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/upway-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/plans/upway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/upway-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/lifecycle/upway-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/upway-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/conformance/upway-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upway-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/data-model/upway-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upway-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/packages/upway-packages.yml
  title: ''
  type: Packages
  url: packages/upway-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upway/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-02'
description: 'Upway is the largest marketplace for certified pre-owned electric bikes, founded in 2021 by former Uber executives Toussaint Wattinne and Stephane Ficaja. It buys used e-bikes from individuals, retailers and manufacturers, reconditions them through a 50-point inspection at its own UpCenter facilities in France, Germany, Belgium, the Netherlands, Spain, Italy and the United States, and resells them at up to 60% off with a one-year warranty. Upway has no developer program and publishes no OpenAPI, but it does run a real agent-facing commerce API: each of its storefronts serves an llms.txt and an /agents.md, a Universal Commerce Protocol merchant profile at /.well-known/ucp, and an anonymous Model Context Protocol endpoint whose tools/list returns 13 tools with full JSON Schema inputSchemas covering catalog search, cart, checkout and order retrieval.'
image: https://cdn.shopify.com/s/files/1/0658/6404/0675/files/Upway_Logo_RGB_Electric_Blue.png?v=1677147770
layout: provider
mcp_servers:
- description: 'Upway''s storefront exposes a live, anonymous Model Context Protocol endpoint at https://upway.co/api/ucp/mcp, advertised from https://upway.co/llms.txt and https://upway.co/agents.md and discoverable '
  name: Upway UCP Commerce MCP Server
  slug: upway-ucp-commerce-mcp-server
modified: '2026-09-02'
name: Upway
nav: Providers
network: true
overview: 'Upway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Marketplace, and Agentic Commerce.


  Upway''s developer surface includes documentation, support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Upway Plans Pricing
  plan_count: 0
  slug: upway-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Upway Rate Limits
  slug: upway-rate-limits
scopes:
- name: Upway Scopes
  scope_count: 0
  slug: upway-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 24.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Upway Authentication
  slug: upway-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Upway Domain Security
  slug: upway-domain-security
  summary_line: TLSv1.3 · HSTS
slug: upway
tags:
- Company
- E-Commerce
- Retail
- Marketplace
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Electric Bikes
- Micromobility
- Circular Economy
- Refurbished Goods
- Shopping Agents
website: https://upway.co/
---
