---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://makeup.land/api/v1
  baseurl_source: declared
  description: 'REST API for the makeup.land storefront under https://makeup.land/api/v1 — 21 operations across Products (cross-lingual q, exact Hebrew tag, brand, ΔE 2000 near_hex shade matching, hue_family, sort), '
  name: makeup.land V1 API
  slug: makeup-land-v1-api
- description: Remote Model Context Protocol server at https://makeup.land/api/mcp — Streamable HTTP, stateless, protocol revision 2025-06-18. initialize and tools/list answer anonymously; 8 read-only tools (list_pr
  name: makeup.land MCP Server
  slug: makeup-land-mcp-server
- description: Public, token-free catalog feeds under https://makeup.land/api/merchant — a Google Merchant Center RSS 2.0 product feed (/feed), a Google Product Reviews 2.4 feed (/reviews) and an OpenAI Agentic Comm
  name: makeup.land Merchant & Agentic Commerce Feeds
  slug: makeup-land-merchant-feeds
artifact_total: 11
asyncapis:
- description: ''
  name: Makeup Land Webhooks
  slug: makeup-land-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://makeup.land/
- group: docs
  title: ''
  type: Documentation
  url: https://makeup.land/llms-full.txt
- group: docs
  title: ''
  type: APIReference
  url: https://makeup.land/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://makeup.land/llms-api.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/authentication/makeup-land-authentication.yml
  title: ''
  type: Authentication
  url: authentication/makeup-land-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://makeup.land/auth.md
- group: commercial
  title: ''
  type: Pricing
  url: https://makeup.land/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://makeup.land/%D7%AA%D7%A0%D7%90%D7%99-%D7%A9%D7%99%D7%9E%D7%95%D7%A9
- group: operate
  title: ''
  type: FAQ
  url: https://makeup.land/%D7%A9%D7%90%D7%9C%D7%95%D7%AA-%D7%A0%D7%A4%D7%95%D7%A6%D7%95%D7%AA
- group: company
  title: ''
  type: About
  url: https://makeup.land/%D7%90%D7%95%D7%93%D7%95%D7%AA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makeup-land
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/llms/makeup-land-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/makeup-land-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://makeup.land/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/well-known/makeup-land-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/makeup-land-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/a2a/makeup-land-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/makeup-land-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/mcp/makeup-land-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/makeup-land-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/mcp/makeup-land-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/makeup-land-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/openapi/makeup-land-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/makeup-land-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/overlays/makeup-land-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/makeup-land-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/conventions/makeup-land-conventions.yml
  title: ''
  type: Conventions
  url: conventions/makeup-land-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/conventions/makeup-land-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/makeup-land-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/errors/makeup-land-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/makeup-land-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/lifecycle/makeup-land-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/makeup-land-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://makeup.land/llms-full.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/rate-limits/makeup-land-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/makeup-land-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/plans/makeup-land-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/makeup-land-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/packages/makeup-land-packages.yml
  title: ''
  type: Packages
  url: packages/makeup-land-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/data-model/makeup-land-data-model.yml
  title: ''
  type: DataModel
  url: data-model/makeup-land-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/scopes/makeup-land-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/makeup-land-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/conformance/makeup-land-conformance.yml
  title: ''
  type: Conformance
  url: conformance/makeup-land-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/asyncapi/makeup-land-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/makeup-land-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/makeup-land/refs/heads/main/security/makeup-land-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/makeup-land-domain-security.yml
created: '2026-09-19'
description: 'makeup.land, operated by א. ט. הפקות בע״מ / A.T. Hafakot Ltd. (company no. 513942789, Zikhron Yaakov and Haifa, Israel), is a Hebrew-first professional cosmetics retailer carrying ~1,550 products from 34+ brands, with ℳ-credit loyalty wallet, M Club tiers, gift cards and a virtual try-on. It publishes a 21-operation OpenAPI 3.1 contract at makeup.land/openapi.json — product search with CIE ΔE 2000 shade matching and cross-lingual semantic search, customers and wallet, carts, orders, gift cards, payment links, partner registration and catalog proposals — every write idempotent via Idempotency-Key, bearer tokens issued by email with four scopes. Alongside it: a live remote MCP server at makeup.land/api/mcp (8 read-only tools, anonymous tools/list, Official MCP Registry land.makeup/v1), RFC 8414 and RFC 9728 OAuth metadata with a WorkOS-style auth.md, an A2A-shaped agent card, an ai-manifest and UCP merchant profile, llms.txt with markdown twins, and Google Merchant and OpenAI
  ACP product feeds.'
image: https://makeup.land/apple-icon.png
layout: provider
mcp_servers:
- description: ''
  name: makeup.land MCP server
  slug: makeupland-mcp-server
- description: ''
  name: Live endpoint (Streamable HTTP)
  slug: live-endpoint-streamable-http
modified: '2026-09-19'
name: makeup.land
nav: Providers
network: true
overview: 'makeup.land publishes 3 APIs on the [APIs.io](https://apis.io/) network, including V1 API, and 2 more. Tagged areas include Cosmetics, Beauty, Retail, E-Commerce, and Shopping.


  The makeup.land catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  makeup.land''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, FAQ, and 27 more developer resources.'
plans:
- name: Makeup Land Plans Pricing
  plan_count: 1
  slug: makeup-land-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Makeup Land Rate Limits
  slug: makeup-land-rate-limits
scopes:
- name: Makeup Land Scopes
  scope_count: 5
  slug: makeup-land-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 42.3
    discoverability: 85.0
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 61.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 72.2
security:
- kind: authentication
  name: Makeup Land Authentication
  slug: makeup-land-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Makeup Land Domain Security
  slug: makeup-land-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: makeup-land
tags:
- Cosmetics
- Beauty
- Retail
- E-Commerce
- Shopping
- Loyalty
- Gift Cards
- Product Search
- Agentic Commerce
- MCP
- Agent-Native
- Israel
- A2A
website: https://makeup.land/
---
