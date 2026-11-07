---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only remote MCP server (Streamable HTTP, no login) that lets an AI assistant search the live catalogue of diamond painting kits (search_products), get canvas size and price advice for a custom ki
  name: DiamondPaintingWinkel.nl Shop Advisor MCP Server
  slug: shop-advisor-mcp
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/diamondpaintingwinkel-nl/conventions/diamondpaintingwinkel-nl-conventions.yml
  title: ''
  type: Conventions
  url: conventions/diamondpaintingwinkel-nl-conventions.yml
- group: auth
  href: https://artifacts.apis.io/diamondpaintingwinkel-nl/authentication/diamondpaintingwinkel-nl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diamondpaintingwinkel-nl-authentication.yml
- group: agent
  href: https://artifacts.apis.io/diamondpaintingwinkel-nl/mcp/diamondpaintingwinkel-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/diamondpaintingwinkel-nl-mcp.yml
- group: other
  href: https://artifacts.apis.io/diamondpaintingwinkel-nl/hosts/diamondpaintingwinkel-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diamondpaintingwinkel-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/diamondpaintingwinkel-nl/vendors/diamondpaintingwinkel-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diamondpaintingwinkel-nl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/diamondpaintingwinkel-nl/security/diamondpaintingwinkel-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diamondpaintingwinkel-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diamondpaintingwinkel.nl/
- group: company
  title: ''
  type: Blog
  url: https://diamondpaintingwinkel.nl/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diamondpaintingwinkel.nl/privacy/
- group: operate
  title: ''
  type: Support
  url: https://diamondpaintingwinkel.nl/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://diamondpaintingwinkel.nl/faq/
- group: other
  title: ''
  type: X
  url: https://x.com/DiamondpaintNL
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Diamondpaintingwinkel
created: '2026-11-05'
description: 'DiamondPaintingWinkel.nl is a Dutch online shop (founded 2021, serving the Netherlands and Belgium) selling diamond painting kits: complete sets, custom kits made from your own photo, XXL formats and accessories, each package including canvas, drills, pen and wax. The WordPress/WooCommerce site also publishes guides, calculators and size-picker tools, and an AI assistant page. It was surfaced via the MCP registry harvest; no developer API documentation was found on its site.'
examples:
- key_count: 3
  name: Diamondpaintingwinkel Nl Mcp Initialize
  slug: diamondpaintingwinkel-nl-mcp-initialize
- key_count: 3
  name: Diamondpaintingwinkel Nl Mcp Tools List
  slug: diamondpaintingwinkel-nl-mcp-tools-list
image: https://diamondpaintingwinkel.nl/wp-content/uploads/2026/03/dp-logo.svg
json_schemas:
- name: photo_size_advice
  property_count: 5
  slug: diamondpaintingwinkel-nl-photo-size-advice-input
- name: search_products
  property_count: 5
  slug: diamondpaintingwinkel-nl-search-products-input
- name: shop_info
  property_count: 1
  slug: diamondpaintingwinkel-nl-shop-info-input
layout: provider
mcp_servers:
- description: Official read-only remote MCP server of DiamondPaintingWinkel.nl. Search the live catalogue of diamond painting kits, get canvas size and price advice for a custom kit made from your own photo, and re
  name: DiamondPaintingWinkel.nl Shop Advisor MCP Server
  slug: diamondpaintingwinkel-nl-shop-advisor-mcp-server
modified: '2026-11-05'
name: DiamondPaintingWinkel.nl
nav: Providers
network: true
overview: 'DiamondPaintingWinkel.nl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diamond Painting, E-Commerce, Arts and Crafts, and Netherlands.


  DiamondPaintingWinkel.nl''s developer surface includes authentication, engineering blog, support, FAQ, YouTube channel, and 8 more developer resources.'
plans:
- name: Diamondpaintingwinkel Nl Plans Pricing
  plan_count: 0
  slug: diamondpaintingwinkel-nl-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Diamondpaintingwinkel Nl Rate Limits
  slug: diamondpaintingwinkel-nl-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 18.5
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Diamondpaintingwinkel Nl Authentication
  slug: diamondpaintingwinkel-nl-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Diamondpaintingwinkel Nl Domain Security
  slug: diamondpaintingwinkel-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diamondpaintingwinkel-nl
tags:
- Company
- Diamond Painting
- E-Commerce
- Arts and Crafts
- Netherlands
- Retail
website: https://diamondpaintingwinkel.nl/
---
