---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-09-16'
api_count: 9
apis:
- description: 'A live Model Context Protocol server served from www.aerofarms.com at /wp-json/mcp/mcp-oauth-server. It answers JSON-RPC over HTTP and is protected by OAuth 2.1: an anonymous tools/list returns HTTP 4'
  name: AeroFarms MCP Server
  slug: aerofarms-mcp-server
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Anonymous WooCommerce Store API session cart.
  name: AeroFarms Cart API
  slug: aerofarms-cart-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Approved reader comments and AeroFarms replies on news posts.
  name: AeroFarms Comments API
  slug: aerofarms-comments-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Route index, content types, taxonomies and statuses.
  name: AeroFarms Discovery API
  slug: aerofarms-discovery-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: AeroFarms image and document library with size variants.
  name: AeroFarms Media API
  slug: aerofarms-media-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: AeroFarms press releases, announcements and articles.
  name: AeroFarms News API
  slug: aerofarms-news-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Static marketing and policy pages of the AeroFarms website.
  name: AeroFarms Pages API
  slug: aerofarms-pages-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Product category, brand and tag taxonomies.
  name: AeroFarms Product Taxonomy API
  slug: aerofarms-product-taxonomy-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: AeroFarms microgreens products as WordPress product posts.
  name: AeroFarms Products API
  slug: aerofarms-products-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Cross-content search over the AeroFarms website.
  name: AeroFarms Search API
  slug: aerofarms-search-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: WooCommerce Store API — public storefront catalog and cart.
  name: AeroFarms Store API
  slug: aerofarms-store-api
- baseURL: https://www.aerofarms.com/wp-json
  baseurl_source: declared
  description: Editorial categories and tags applied to AeroFarms news posts.
  name: AeroFarms Taxonomy API
  slug: aerofarms-taxonomy-api
- baseURL: https://www.aerofarms.com/wp-json/mcp/mcp-oauth-server
  baseurl_source: declared
  description: AeroFarms customer FAQ entries and their categories.
  name: AeroFarms FA Qs API
  slug: aerofarms-faqs-api
artifact_total: 19
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-news-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-news-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-pages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-pages-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-products-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-products-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-store-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-store-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-faq-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-faq-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-taxonomy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-taxonomy-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-media-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-media-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-search-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/overlays/aerofarms-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aerofarms-discovery-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.aerofarms.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aerofarms.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.aerofarms.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerofarms.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerofarms.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AeroFarms
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/llms/aerofarms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerofarms-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/well-known/aerofarms-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aerofarms-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/mcp/aerofarms-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aerofarms-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/mcp/aerofarms-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aerofarms-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/authentication/aerofarms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aerofarms-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/scopes/aerofarms-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aerofarms-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/conformance/aerofarms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aerofarms-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/conventions/aerofarms-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aerofarms-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/errors/aerofarms-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aerofarms-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/lifecycle/aerofarms-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aerofarms-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/data-model/aerofarms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aerofarms-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/plans/aerofarms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aerofarms-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/rate-limits/aerofarms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aerofarms-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/security/aerofarms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerofarms-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aerofarms/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-10'
description: 'AeroFarms is an indoor vertical farming company founded in 2004 and headquartered in Newark, New Jersey, where it grows leafy greens and nutrient-dense microgreens — micro broccoli, micro arugula, micro wasabi mustard and the FlavorSpectrum blends — aeroponically, without sun or soil, under LED light recipes driven by its proprietary agSTACK PLC/SCADA control stack. It sells through US grocery retail rather than through software, is a Certified B Corporation, and was acquired by an affiliate of Palm Ventures in June 2026. AeroFarms is a produce grower, not a software vendor: no developer portal, no API documentation, no SDKs, no API product. The machine-readable surface profiled here is the anonymous, read-only WordPress and WooCommerce REST API behind www.aerofarms.com, a live OAuth-protected MCP server at /wp-json/mcp/mcp-oauth-server, and a published llms.txt.'
image: https://www.aerofarms.com/wp-content/uploads/2021/04/cropped-AF-Favicon-copy.png
layout: provider
mcp_servers:
- description: 'AeroFarms serves a live, reachable Model Context Protocol server from its own website host. This is not a candidate derived from OpenAPI operations: the endpoint exists, answers JSON-RPC, and defends '
  name: AeroFarms MCP Server
  slug: aerofarms-mcp-server
modified: '2026-09-10'
name: AeroFarms
nav: Providers
network: true
overview: 'AeroFarms publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Comments API, Discovery API, and 9 more. Tagged areas include Company, Agriculture, Vertical Farming, Indoor Farming, and AgTech.


  AeroFarms'' developer surface includes engineering blog, support, authentication, and 27 more developer resources.'
plans:
- name: Aerofarms Plans Pricing
  plan_count: 0
  slug: aerofarms-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aerofarms Rate Limits
  slug: aerofarms-rate-limits
scopes:
- name: Aerofarms Scopes
  scope_count: 0
  slug: aerofarms-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 13.1
    developer_ergonomics: 20.8
    discoverability: 81.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Aerofarms Authentication
  slug: aerofarms-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aerofarms Domain Security
  slug: aerofarms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aerofarms
tags:
- Company
- Agriculture
- Vertical Farming
- Indoor Farming
- AgTech
- Food and Beverage
- Consumer Packaged Goods
- Microgreens
- Sustainability
- Content
- Commerce
- MCP
website: https://www.aerofarms.com/
---
