---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://store.iconaircraft.com
  baseurl_source: declared
  description: Anonymous, read-only JSON access to the Shop ICON merchandise storefront at store.iconaircraft.com — products, variants, collections, predictive search, session cart and store metadata. The store's ow
  name: Shop ICON Storefront API
  slug: icon-aircraft-store-api
- description: 'A live, anonymously callable Model Context Protocol endpoint implementing the Universal Commerce Protocol 2026-04-08 for the Shop ICON storefront. An unauthenticated tools/list returned HTTP 200 with '
  name: Shop ICON UCP/MCP Server
  slug: icon-aircraft-ucp-mcp
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: Products and product variants.
  name: ICON Aircraft Catalog API
  slug: icon-aircraft-catalog-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: Merchandising collections.
  name: ICON Aircraft Collections API
  slug: icon-aircraft-collections-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: Self-describing metadata about the content types this site exposes.
  name: ICON Aircraft Discovery API
  slug: icon-aircraft-discovery-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: The site media library — photography, video posters and documents.
  name: ICON Aircraft Media API
  slug: icon-aircraft-media-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: Marketing, product, policy and landing pages.
  name: ICON Aircraft Pages API
  slug: icon-aircraft-pages-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: ICON Aircraft news and press releases.
  name: ICON Aircraft Posts API
  slug: icon-aircraft-posts-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: Cross-type site search.
  name: ICON Aircraft Search API
  slug: icon-aircraft-search-api
- baseURL: https://www.iconaircraft.com/wp-json
  baseurl_source: declared
  description: Categories and tags applied to posts.
  name: ICON Aircraft Taxonomy API
  slug: icon-aircraft-taxonomy-api
artifact_total: 16
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/icon-aircraft-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.iconaircraft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://store.iconaircraft.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.iconaircraft.com/company/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.iconaircraft.com/company/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.iconaircraft.com/updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.iconaircraft.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iconaircraft.com/how-to-buy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iconaircraft.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iconaircraft.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/icon-aircraft-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/icon-aircraft-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/icon-aircraft-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/icon-aircraft-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/icon-aircraft-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/icon-aircraft-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/icon-aircraft-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/icon-aircraft-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/icon-aircraft-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/icon-aircraft-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/icon-aircraft-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/icon-aircraft-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/icon-aircraft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/icon-aircraft-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icon-aircraft-domain-security.yml
created: '2026-08-22'
description: 'ICON Aircraft is an American light-sport aircraft manufacturer founded in 2006 by Kirk Hawkins and Steen Strand and headquartered in Vacaville, California. It designs, builds and sells the ICON A5, an amphibious two-seat S-LSA with folding wings, a spin-resistant airframe, an optional ICON Parachute System and a Rotax 912iS engine, sold alongside flight training, a certified pre-owned program and a service-provider network. The A5 entered production in 2016 and received FAA type certification in the primary category in December 2023. Since April 2025 ICON has been a sister company of Flight Design under Shang Gong Group. ICON is an aircraft manufacturer, not a software vendor: it operates no developer program, publishes no product API, no SDKs and no developer portal. Two machine-readable surfaces do exist on its own domains and are profiled here — the WordPress REST content API behind www.iconaircraft.com, which is anonymously readable and read-only, and the Shopify-hosted
  Shop ICON merchandise storefront at store.iconaircraft.com, which serves storefront JSON plus a live, anonymous Universal Commerce Protocol MCP endpoint with thirteen catalog, cart, checkout and order tools.'
image: https://www.iconaircraft.com/wp-content/themes/iconaircraft/assets/images/favicon/favicon-512.png
layout: provider
mcp_servers:
- description: ''
  name: Shop ICON UCP/MCP Server
  slug: shop-icon-ucpmcp-server
modified: '2026-08-22'
name: ICON Aircraft
nav: Providers
network: true
overview: 'ICON Aircraft publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Shop ICON Storefront API, Catalog API, Collections API, and 6 more. Tagged areas include Company, Aerospace, Aviation, Aircraft Manufacturing, and Light Sport Aircraft.


  ICON Aircraft''s developer surface includes documentation, support, engineering blog, pricing, authentication, and 21 more developer resources.'
plans:
- name: Icon Aircraft Plans Pricing
  plan_count: 0
  slug: icon-aircraft-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Icon Aircraft Rate Limits
  slug: icon-aircraft-rate-limits
scopes:
- name: Icon Aircraft Scopes
  scope_count: 0
  slug: icon-aircraft-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 49.1
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 34.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/icon-aircraft/refs/heads/main/screenshots/icon-aircraft-2026-09-02T145820.png
security:
- kind: authentication
  name: Icon Aircraft Authentication
  slug: icon-aircraft-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Icon Aircraft Domain Security
  slug: icon-aircraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: icon-aircraft
tags:
- Company
- Aerospace
- Aviation
- Aircraft Manufacturing
- Light Sport Aircraft
- Seaplanes
- General Aviation
- Flight Training
- Manufacturing
- Consumer Products
- E-Commerce
- Content
- Agentic Commerce
website: https://www.iconaircraft.com/
---
