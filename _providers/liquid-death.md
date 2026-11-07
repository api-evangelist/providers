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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Liquid Death Agentic Access
  operation_count: 7
  slug: liquid-death-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'Liquid Death''s hosted Model Context Protocol server implementing the Universal Commerce Protocol dev.ucp.shopping service — catalog search and lookup, cart, checkout, fulfillment, discount and order. '
  name: Liquid Death UCP Shopping MCP
  slug: liquid-death-ucp-shopping-mcp
- description: The OpenID Connect and OAuth 2.0 authorization server for the Liquid Death customer account, hosted at account.liquiddeath.com and discoverable from both /.well-known/openid-configuration and /.well-k
  name: Liquid Death Customer Account OAuth
  slug: liquid-death-customer-account-oauth
- baseURL: https://liquiddeath.com
  baseurl_source: spec
  description: Store-level discovery documents for crawlers and agents
  name: Liquid Death Discovery API
  slug: liquid-death-discovery-api
- description: 'The Shopify Storefront JSON surface that Shopify generates for every Shopify site or store, served on liquiddeath.com. Catalogued as one platform-generated record, not as separate APIs: nobody at Liqu'
  name: Liquid Death Storefront JSON (Shopify)
  slug: liquiddeath-com-shopify-storefront-json
artifact_total: 13
collections:
- collection_type: open
  name: Liquid Death Storefront Read-Only JSON API
  slug: open-liquid-death-storefront
common:
- group: other
  href: https://artifacts.apis.io/liquid-death/capabilities/liquid-death-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/liquid-death-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://liquiddeath.com/
- group: docs
  title: ''
  type: Documentation
  url: https://liquiddeath.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://liquiddeath.com/agents.md
- group: agent
  href: https://artifacts.apis.io/liquid-death/llms/liquid-death-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/liquid-death-llms.txt
- group: agent
  href: https://artifacts.apis.io/liquid-death/well-known/liquid-death-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/liquid-death-well-known.yml
- group: docs
  href: https://artifacts.apis.io/liquid-death/openapi/_original/liquid-death-storefront-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/liquid-death-storefront-openapi.yml
- group: other
  href: https://artifacts.apis.io/liquid-death/overlays/liquid-death-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/liquid-death-storefront-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/liquid-death/mcp/liquid-death-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/liquid-death-mcp.yml
- group: build
  href: https://artifacts.apis.io/liquid-death/mcp/liquid-death-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/liquid-death-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/liquid-death/authentication/liquid-death-authentication.yml
  title: ''
  type: Authentication
  url: authentication/liquid-death-authentication.yml
- group: auth
  href: https://artifacts.apis.io/liquid-death/scopes/liquid-death-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/liquid-death-scopes.yml
- group: design
  href: https://artifacts.apis.io/liquid-death/conventions/liquid-death-conventions.yml
  title: ''
  type: Conventions
  url: conventions/liquid-death-conventions.yml
- group: design
  href: https://artifacts.apis.io/liquid-death/conventions/liquid-death-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/liquid-death-conventions.yml
- group: design
  href: https://artifacts.apis.io/liquid-death/errors/liquid-death-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/liquid-death-problem-types.yml
- group: design
  href: https://artifacts.apis.io/liquid-death/conformance/liquid-death-conformance.yml
  title: ''
  type: Conformance
  url: conformance/liquid-death-conformance.yml
- group: design
  href: https://artifacts.apis.io/liquid-death/lifecycle/liquid-death-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/liquid-death-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/liquid-death/data-model/liquid-death-data-model.yml
  title: ''
  type: DataModel
  url: data-model/liquid-death-data-model.yml
- group: agent
  href: https://artifacts.apis.io/liquid-death/agentic-access/liquid-death-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/liquid-death-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/liquid-death/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/liquid-death/security/liquid-death-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liquid-death-domain-security.yml
- group: operate
  title: ''
  type: FAQ
  url: https://liquiddeath.com/pages/faq
- group: operate
  title: ''
  type: Support
  url: https://liquiddeath.com/pages/summon-us
- group: company
  title: ''
  type: Blog
  url: https://liquiddeath.com/blogs/news
- group: other
  title: ''
  type: Shop
  url: https://liquiddeath.com/collections/all
- group: other
  title: ''
  type: WhereToBuy
  url: https://liquiddeath.com/pages/where-to-buy
- group: company
  title: ''
  type: Careers
  url: https://liquiddeath.com/pages/careers
- group: company
  title: ''
  type: About
  url: https://liquiddeath.com/pages/manifesto
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liquiddeath.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liquiddeath.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://liquiddeath.com/policies/refund-policy
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/liquiddeath/
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@liquiddeath
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/liquid-death_stock/
created: '2026-08-01'
description: 'Liquid Death is a Los Angeles beverage company founded in 2014 by Mike Cessario, Pat Cook and JonRyan Riggins, selling still and sparkling mountain water, iced tea, flavored sparkling water, the Death Dust electrolyte powder and a Sparkling Energy line, all in recyclable aluminum tallboys and marketed through a deliberately horror-comedy brand voice. It has raised roughly $264M and was valued at $1.4B in its 2024 Series F. Liquid Death publishes no conventional developer portal, yet it is one of the more agent-forward direct-to-consumer storefronts in the catalog: liquiddeath.com serves a first-party agents.md (mirrored at /llms.txt), a dedicated agentic-discovery sitemap, an agent policy block inside robots.txt, a Universal Commerce Protocol merchant profile at /.well-known/ucp, a live UCP shopping MCP endpoint, and both OpenID Connect and RFC 8414 OAuth discovery documents for its customer account. The storefront exposes an anonymous read-only product and collection JSON
  surface, while every cart, checkout and order capability is confined to the identity-gated, idempotency-keyed MCP transport that requires contemporaneous human approval before payment.'
image: https://liquiddeath.com/cdn/shop/files/Liquid-Death-Preview-Image_7033558e-a84d-4880-8a70-87e84739f262.jpg?v=1681949476
layout: provider
mcp_servers:
- description: Liquid Death publishes a live, hosted MCP server as the Universal Commerce Protocol (UCP) shopping transport for its store. It is advertised in three independent places on the provider's own host — ro
  name: Liquid Death MCP Server
  slug: liquid-death-ucp-shopping
modified: '2026-09-16'
name: Liquid Death
nav: Providers
network: true
overview: 'Liquid Death publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, and 3 more. Tagged areas include Company, Beverages, Consumer Packaged Goods, Direct to Consumer, and E-Commerce.


  The Liquid Death catalog on APIs.io includes 1 Spectral governance ruleset.


  Liquid Death''s developer surface includes documentation, getting-started guide, authentication, FAQ, support, engineering blog, and 28 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Liquid Death API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: liquid-death-rules
scopes:
- name: Liquid Death Scopes
  scope_count: 4
  slug: liquid-death-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 11.6
    developer_ergonomics: 42.3
    discoverability: 58.3
    operational_transparency: 0.0
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: platform-generated
    skills: derived
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
screenshot: https://apis.io/screenshots/liquid-death/liquid-death-2026-08-07T171733.png
security:
- kind: authentication
  name: Liquid Death Authentication
  slug: liquid-death-authentication
  summary_line: none/openIdConnect/oauth2/agentProfile · 4 schemes
- kind: domain-security
  name: Liquid Death Domain Security
  slug: liquid-death-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Browse the Liquid Death catalog
  slug: liquid-death-browse-catalog
- name: Shop Liquid Death over UCP/MCP
  slug: liquid-death-shop-with-ucp
slug: liquid-death
tags:
- Company
- Beverages
- Consumer Packaged Goods
- Direct to Consumer
- E-Commerce
- Retail
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://liquiddeath.com/
---
