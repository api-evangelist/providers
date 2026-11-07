---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: Julep's agent-commerce surface. The storefront advertises a Universal Commerce Protocol merchant profile and a live JSON-RPC Model Context Protocol endpoint covering catalog search and lookup, cart, d
  name: Julep UCP Commerce MCP Endpoint
  slug: ucp-commerce
- baseURL: https://www.julep.com
  baseurl_source: spec
  description: Read-only view of the current session cart.
  name: Julep Beauty Cart API
  slug: julep-beauty-cart-api
- baseURL: https://www.julep.com
  baseurl_source: spec
  description: Store metadata and agent-discovery documents.
  name: Julep Beauty Discovery API
  slug: julep-beauty-discovery-api
- baseURL: https://www.julep.com
  baseurl_source: spec
  description: Storefront product search.
  name: Julep Beauty Search API
  slug: julep-beauty-search-api
- description: 'The Shopify Storefront JSON surface that Shopify generates for every Shopify site or store, served on julep.com. Catalogued as one platform-generated record, not as separate APIs: nobody at Julep Beau'
  name: Julep Beauty Storefront JSON (Shopify)
  slug: julep-com-shopify-storefront-json
artifact_total: 17
collections:
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
  href: https://artifacts.apis.io/julep-beauty/overlays/julep-beauty-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/julep-beauty-storefront-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/julep-beauty/security/julep-beauty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/julep-beauty-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/julep-beauty/well-known/julep-beauty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/julep-beauty-well-known.yml
- group: agent
  href: https://artifacts.apis.io/julep-beauty/llms/julep-beauty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/julep-beauty-llms.txt
- group: agent
  href: https://artifacts.apis.io/julep-beauty/mcp/julep-beauty-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/julep-beauty-mcp.yml
- group: agent
  href: https://artifacts.apis.io/julep-beauty/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/julep-beauty/authentication/julep-beauty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/julep-beauty-authentication.yml
- group: auth
  href: https://artifacts.apis.io/julep-beauty/scopes/julep-beauty-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/julep-beauty-scopes.yml
- group: design
  href: https://artifacts.apis.io/julep-beauty/conventions/julep-beauty-conventions.yml
  title: ''
  type: Conventions
  url: conventions/julep-beauty-conventions.yml
- group: operate
  href: https://artifacts.apis.io/julep-beauty/rate-limits/julep-beauty-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/julep-beauty-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/julep-beauty/errors/julep-beauty-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/julep-beauty-problem-types.yml
- group: design
  href: https://artifacts.apis.io/julep-beauty/lifecycle/julep-beauty-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/julep-beauty-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/julep-beauty/conformance/julep-beauty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/julep-beauty-conformance.yml
- group: design
  href: https://artifacts.apis.io/julep-beauty/data-model/julep-beauty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/julep-beauty-data-model.yml
- group: build
  href: https://artifacts.apis.io/julep-beauty/packages/julep-beauty-packages.yml
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
- description: 'Julep''s storefront exposes a live, hosted Model Context Protocol endpoint as the MCP transport for the Universal Commerce Protocol (UCP) shopping service. The endpoint is advertised in the merchant''s '
  name: Julep UCP Commerce MCP Server
  slug: julep-ucp-commerce-mcp-server
modified: '2026-07-19'
name: Julep Beauty
nav: Providers
network: true
overview: 'Julep Beauty is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Discovery API, Search API, and 2 more. Tagged areas include Company, Beauty, Cosmetics, Skincare, and Retail.


  The Julep Beauty catalog on APIs.io includes 1 Spectral governance ruleset.


  Julep Beauty''s developer surface includes authentication, documentation, support, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Julep Beauty Rate Limits
  slug: julep-beauty-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Julep Beauty API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: julep-beauty-rules
scopes:
- name: Julep Beauty Scopes
  scope_count: 4
  slug: julep-beauty-scopes
  summary_line: 4 scopes · authorization_code/refresh_token/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 12.9
    developer_ergonomics: 35.7
    discoverability: 60.0
    operational_transparency: 2.6
  previous_composite: 30.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/julep-beauty/julep-beauty-2026-08-07T171031.png
security:
- kind: authentication
  name: Julep Beauty Authentication
  slug: julep-beauty-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Julep Beauty Domain Security
  slug: julep-beauty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: julep-storefront-agent
  slug: julep-beauty-agents
- name: julep-browse-catalog
  slug: julep-beauty-browse-catalog
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
