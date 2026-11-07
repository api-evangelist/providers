---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-11-06'
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
- description: 'The public WordPress REST API (wp-json) of the ICON Aircraft website at www.iconaircraft.com: the route index of the site''s content management system, catalogued as one site surface rather than as sep'
  name: ICON Aircraft Website (WordPress REST)
  slug: iconaircraft-com-website-wordpress-rest
- baseURL: https://store.iconaircraft.com
  baseurl_source: declared
  description: Cross-type site search.
  name: ICON Aircraft Search API
  slug: icon-aircraft-search-api
- description: 'The Shopify Storefront JSON surface that Shopify generates for every Shopify site or store, served on store.iconaircraft.com. Catalogued as one platform-generated record, not as separate APIs: nobody '
  name: ICON Aircraft Storefront JSON (Shopify)
  slug: store-iconaircraft-com-shopify-storefront-json
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/icon-aircraft/capabilities/icon-aircraft-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/icon-aircraft-capability-edges.yml
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
  href: https://artifacts.apis.io/icon-aircraft/llms/icon-aircraft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/icon-aircraft-llms.txt
- group: agent
  href: https://artifacts.apis.io/icon-aircraft/well-known/icon-aircraft-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/icon-aircraft-well-known.yml
- group: agent
  href: https://artifacts.apis.io/icon-aircraft/mcp/icon-aircraft-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/icon-aircraft-mcp.yml
- group: agent
  href: https://artifacts.apis.io/icon-aircraft/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/icon-aircraft/conventions/icon-aircraft-conventions.yml
  title: ''
  type: Conventions
  url: conventions/icon-aircraft-conventions.yml
- group: design
  href: https://artifacts.apis.io/icon-aircraft/conventions/icon-aircraft-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/icon-aircraft-conventions.yml
- group: design
  href: https://artifacts.apis.io/icon-aircraft/errors/icon-aircraft-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/icon-aircraft-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/icon-aircraft/authentication/icon-aircraft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/icon-aircraft-authentication.yml
- group: auth
  href: https://artifacts.apis.io/icon-aircraft/scopes/icon-aircraft-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/icon-aircraft-scopes.yml
- group: design
  href: https://artifacts.apis.io/icon-aircraft/conformance/icon-aircraft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/icon-aircraft-conformance.yml
- group: design
  href: https://artifacts.apis.io/icon-aircraft/lifecycle/icon-aircraft-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/icon-aircraft-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/icon-aircraft/data-model/icon-aircraft-data-model.yml
  title: ''
  type: DataModel
  url: data-model/icon-aircraft-data-model.yml
- group: build
  href: https://artifacts.apis.io/icon-aircraft/packages/icon-aircraft-packages.yml
  title: ''
  type: Packages
  url: packages/icon-aircraft-packages.yml
- group: commercial
  href: https://artifacts.apis.io/icon-aircraft/plans/icon-aircraft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/icon-aircraft-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/icon-aircraft/rate-limits/icon-aircraft-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/icon-aircraft-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/icon-aircraft/security/icon-aircraft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icon-aircraft-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/icon-aircraft/openapi/icon-aircraft-search-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/icon-aircraft-search-api-openapi.yml
created: '2026-08-22'
description: 'ICON Aircraft is an American light-sport aircraft manufacturer founded in 2006 by Kirk Hawkins and Steen Strand and headquartered in Vacaville, California. It designs, builds and sells the ICON A5, an amphibious two-seat S-LSA with folding wings, a spin-resistant airframe, an optional ICON Parachute System and a Rotax 912iS engine, sold alongside flight training, a certified pre-owned program and a service-provider network. The A5 entered production in 2016 and received FAA type certification in the primary category in December 2023. Since April 2025 ICON has been a sister company of Flight Design under Shang Gong Group. ICON is an aircraft manufacturer, not a software vendor: it operates no developer program, publishes no product API, no SDKs and no developer portal. Two machine-readable surfaces do exist on its own domains and are profiled here — the WordPress REST content API behind www.iconaircraft.com, which is anonymously readable and read-only, and the Shopify-hosted
  Shop ICON merchandise storefront at store.iconaircraft.com, which serves storefront JSON plus a live, anonymous Universal Commerce Protocol MCP endpoint with thirteen catalog, cart, checkout and order tools.'
image: https://www.iconaircraft.com/wp-content/themes/iconaircraft/assets/images/favicon/favicon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at store.iconaircraft.com; 13 tools listed.
  name: Shop ICON UCP/MCP Server
  slug: shop-icon-ucp-mcp-server
modified: '2026-08-22'
name: ICON Aircraft
nav: Providers
network: true
overview: 'ICON Aircraft publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Shop ICON Storefront API, Search API, and 3 more. Tagged areas include Company, Aerospace, Aviation, Aircraft Manufacturing, and Light Sport Aircraft.


  The ICON Aircraft catalog on APIs.io includes 1 Spectral governance ruleset.


  ICON Aircraft''s developer surface includes documentation, support, engineering blog, pricing, authentication, and 22 more developer resources.'
plans:
- name: Icon Aircraft Plans Pricing
  plan_count: 0
  slug: icon-aircraft-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Icon Aircraft Rate Limits
  slug: icon-aircraft-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: ICON Aircraft API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: icon-aircraft-rules
scopes:
- name: Icon Aircraft Scopes
  scope_count: 4
  slug: icon-aircraft-scopes
  summary_line: 4 scopes · authorization_code/refresh_token/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 36.6
    developer_ergonomics: 30.4
    discoverability: 66.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 34.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
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
screenshot: https://apis.io/screenshots/icon-aircraft/icon-aircraft-2026-09-02T145820.png
security:
- kind: authentication
  name: Icon Aircraft Authentication
  slug: icon-aircraft-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Icon Aircraft Domain Security
  slug: icon-aircraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: browse-shop-icon-catalog
  slug: icon-aircraft-browse-store-catalog
- name: read-icon-aircraft-news
  slug: icon-aircraft-read-company-news
- name: transact-with-shop-icon
  slug: icon-aircraft-transact-with-approval
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
