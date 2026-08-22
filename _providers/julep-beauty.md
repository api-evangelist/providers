---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Julep's agent-commerce surface. The storefront advertises a Universal Commerce Protocol merchant profile and a live JSON-RPC Model Context Protocol endpoint covering catalog search and lookup, cart, d
  name: Julep UCP Commerce MCP Endpoint
  slug: ucp-commerce
- description: Read-only view of the current session cart.
  name: Julep Beauty Cart API
  slug: julep-beauty-cart-api
- description: Products and collections.
  name: Julep Beauty Catalog API
  slug: julep-beauty-catalog-api
- description: Store metadata and agent-discovery documents.
  name: Julep Beauty Discovery API
  slug: julep-beauty-discovery-api
- description: Storefront product search.
  name: Julep Beauty Search API
  slug: julep-beauty-search-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Julep Storefront Read-Only JSON Cart API
  slug: open-julep-beauty-cart-api
- collection_type: open
  name: Julep Storefront Read-Only JSON Cart Catalog API
  slug: open-julep-beauty-catalog-api
- collection_type: open
  name: Julep Storefront Read-Only JSON Cart Discovery API
  slug: open-julep-beauty-discovery-api
- collection_type: open
  name: Julep Storefront Read-Only JSON Cart Search API
  slug: open-julep-beauty-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/julep-beauty-storefront-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/julep-beauty-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/julep-beauty-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/julep-beauty-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/julep-beauty-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/julep-beauty-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/julep-beauty-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/julep-beauty-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/julep-beauty-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/julep-beauty-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/julep-beauty-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/julep-beauty-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/julep-beauty-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/julep-beauty-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.julep.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.julep.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://www.julep.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://www.julep.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.julep.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.julep.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.julep.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://www.julep.com/policies/shipping-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/julep
- group: company
  title: ''
  type: Website
  url: https://www.julep.com
created: '2026-07-17'
description: 'Julep is a direct-to-consumer beauty brand selling makeup, skincare, nail polish, and value sets, founded in Seattle by Jane Park and backed by Andreessen Horowitz, Maveron, and others before its 2016 acquisition. The brand positions itself around effortless, low-effort beauty for women who "do a lot but don''t want to spend a lot of time doing their makeup," with skincare inspired by its founder''s Korean heritage. Julep runs its storefront on Shopify at www.julep.com and also sells through Amazon and Target. It is not an API platform and publishes no developer program, but the storefront carries a substantive agent-facing surface: published agent instructions at /agents.md and /llms.txt, a Universal Commerce Protocol merchant profile at /.well-known/ucp, a live MCP commerce endpoint, OpenID Connect discovery for customer accounts, and a public read-only catalog JSON API.'
image: https://www.julep.com/cdn/shop/files/Julep_Favicon.png?v=1631633077
layout: provider
mcp_servers:
- description: ''
  name: julep-beauty-mcp.yml
  slug: julep-beauty-mcpyml
modified: '2026-07-19'
name: Julep Beauty
nav: Providers
network: true
overview: 'Julep Beauty publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Catalog API, Discovery API, and 1 more. Tagged areas include Company, Beauty, Cosmetics, Skincare, and Retail.


  Julep Beauty''s developer surface includes authentication, documentation, support, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 0
  name: Julep Beauty Rate Limits
  slug: julep-beauty-rate-limits
scopes:
- name: Julep Beauty Scopes
  scope_count: 0
  slug: julep-beauty-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.5
  delta: -1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 53.7
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 40.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/julep-beauty/refs/heads/main/screenshots/julep-beauty-2026-08-07T171031.png
security:
- kind: authentication
  name: Julep Beauty Authentication
  slug: julep-beauty-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Julep Beauty Domain Security
  slug: julep-beauty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: julep-beauty
tags:
- Company
- Beauty
- Cosmetics
- Skincare
- Retail
- E-Commerce
- Direct to Consumer
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
website: https://www.julep.com
---
