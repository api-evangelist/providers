---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'A live, remote Model Context Protocol server on Rock The Bells'' own storefront host implementing the Universal Commerce Protocol shopping service. Thirteen tools let an agent search the catalog, look '
  name: Rock The Bells Commerce MCP Server (UCP)
  slug: rock-the-bells-commerce-mcp
- description: The Shopify Storefront GraphQL API as served on Rock The Bells' own domain. Full introspection succeeded anonymously on 2026-08-26, returning a 414-type schema with 34 root query fields and 41 mutatio
  name: Rock The Bells Storefront GraphQL API
  slug: rock-the-bells-storefront-graphql
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://shop.rockthebells.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.rockthebells.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rock-the-bells-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rock-the-bells-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rock-the-bells-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rock-the-bells-well-known.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/rock-the-bells-storefront.graphql
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rock-the-bells-ucp-tool-schemas.json
- group: design
  title: ''
  type: Conventions
  url: conventions/rock-the-bells-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rock-the-bells-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rock-the-bells-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rock-the-bells-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rock-the-bells-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rock-the-bells-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rock-the-bells-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rock-the-bells-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rock-the-bells-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rock-the-bells-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/rock-the-bells-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rock-the-bells-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://shop.rockthebells.com/blogs/articles
- group: operate
  title: ''
  type: Support
  url: https://shop.rockthebells.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://shop.rockthebells.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.rockthebells.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.rockthebells.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://shop.rockthebells.com/policies/refund-policy
created: '2026-08-26'
description: 'Rock The Bells is the hip-hop culture brand and direct-to-consumer merchandise retailer founded by LL COOL J, describing itself on its own storefront as "The Home For All Things Classic and Timeless Hip-Hop". It sells apparel and accessories and publishes editorial across five blogs (features, artists, videos, From Jamaica to the Bronx, and COHH). It ships no developer program and no OpenAPI, but it does serve a live, anonymously callable agent commerce surface: a Universal Commerce Protocol (UCP 2026-04-08) merchant profile at /.well-known/ucp, a 13-tool Model Context Protocol server at /api/ucp/mcp, a fully introspectable Storefront GraphQL API, and an agent instruction document at /llms.txt and /agents.md that its robots.txt and a purpose-built sitemap_agentic_discovery.xml both point at. Discovery is open; payment is gated by a stated human-approval invariant rather than by a credential.'
image: https://shop.rockthebells.com/cdn/shop/files/RTB-Logo_dbd6e9a5-9b51-485a-970c-04d742548a60.png?v=1749612774
json_schemas:
- name: Rock The Bells UCP/MCP tool input schemas
  property_count: 0
  slug: rock-the-bells-ucp-tool-schemas
layout: provider
mcp_servers:
- description: 'Rock The Bells serves a live, anonymously-listable Model Context Protocol server on its own storefront host at https://shop.rockthebells.com/api/ucp/mcp. It implements the Universal Commerce Protocol '
  name: Rock The Bells Commerce MCP Server (UCP)
  slug: rock-the-bells-commerce-mcp-server-ucp
modified: '2026-08-26'
name: Rock The Bells
nav: Providers
network: true
overview: 'Rock The Bells publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Merchandise, and Apparel.


  Rock The Bells'' developer surface includes documentation, authentication, engineering blog, support, and 23 more developer resources.'
plans:
- name: Rock The Bells Plans Pricing
  plan_count: 0
  slug: rock-the-bells-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Rock The Bells Rate Limits
  slug: rock-the-bells-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 43.6
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rock-the-bells/refs/heads/main/screenshots/rock-the-bells-2026-09-02T154032.png
security:
- kind: authentication
  name: Rock The Bells Authentication
  slug: rock-the-bells-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Rock The Bells Domain Security
  slug: rock-the-bells-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rock-the-bells
tags:
- Company
- Retail
- E-Commerce
- Merchandise
- Apparel
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- GraphQL
- Media
- Music
- Hip-Hop
website: https://shop.rockthebells.com/
---
