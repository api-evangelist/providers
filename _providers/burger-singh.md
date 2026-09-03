---
access_model:
  confidence: high
  label: Public read-only content API, no signup
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Burger Singh Agentic Access
  operation_count: 15
  slug: burger-singh-agentic-access
  summary_line: 15 operations
api_count: 6
apis:
- baseURL: https://www.burgersinghonline.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the site pages of burgersinghonline.com - Menu, Burgers, Fries and Sides, Desserts, Beverages, Franchise, Property Partners, Bulk Order, Store Locator, Hot Locat
  name: Burger Singh Pages API
  slug: burger-singh-pages-api
- baseURL: https://www.burgersinghonline.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind burgersinghonline.com - burger and menu photography, outlet imagery, franchise collateral and press assets with their generated size var
  name: Burger Singh Media API
  slug: burger-singh-media-api
- baseURL: https://www.burgersinghonline.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the site taxonomy - the franchise investment brackets (Less than 26 Lacs, 26 to 60 Lacs, 60 Lacs to 1 Crore), the store formats (Dine-in Only, Dine-in + Take Awa
  name: Burger Singh Taxonomy API
  slug: burger-singh-taxonomy-api
- baseURL: https://www.burgersinghonline.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over burgersinghonline.com, returning lightweight id / title / url / type / subtype records with an embeddable link to the full object.
  name: Burger Singh Search API
  slug: burger-singh-search-api
- baseURL: https://www.burgersinghonline.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated site, content-type, taxonomy, status and author metadata - the self-describing route index (200 routes across 12 namespaces) that makes the whole burgersinghonline.com surface '
  name: Burger Singh Discovery API
  slug: burger-singh-discovery-api
- baseURL: https://www.burgersinghonline.com/wp-json
  baseurl_source: declared
  description: Public Yoast SEO head endpoint returning the rendered SEO/head metadata and its schema.org JSON-LD graph for any burgersinghonline.com URL.
  name: Burger Singh SEO Metadata API
  slug: burger-singh-seo-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Burger Singh Discovery API
  slug: open-burger-singh-discovery-api
- collection_type: open
  name: Burger Singh Media API
  slug: open-burger-singh-media-api
- collection_type: open
  name: Burger Singh Pages API
  slug: open-burger-singh-pages-api
- collection_type: open
  name: Burger Singh Search API
  slug: open-burger-singh-search-api
- collection_type: open
  name: Burger Singh Metadata SEO API
  slug: open-burger-singh-seo-api
- collection_type: open
  name: Burger Singh Taxonomy API
  slug: open-burger-singh-taxonomy-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.burgersinghonline.com/
- group: company
  title: ''
  type: About
  url: https://www.burgersinghonline.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.burgersinghonline.com/feedback/
- group: operate
  title: ''
  type: Contact
  url: https://www.burgersinghonline.com/complaint/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.burgersinghonline.com/terms-and-conditions/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BurgerSinghs
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/BurgerSinghIndia
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/burgersinghofficial/
- group: auth
  title: ''
  type: Authentication
  url: authentication/burger-singh-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/burger-singh-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/burger-singh-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/burger-singh-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/burger-singh-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/burger-singh-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/burger-singh-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/burger-singh-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/burger-singh-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/burger-singh-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/burger-singh-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/burger-singh-agentic-access.yml
- group: build
  title: ''
  type: Examples
  url: examples/burger-singh-examples.yml
created: '2026-08-08'
description: 'Burger Singh is an Indian quick-service restaurant chain founded in 2014 by Kabir Jeet Singh with co-founders Nitin Rana and Rahul Seth, and operated by Tipping Mr Pink Private Limited out of Gurugram, Haryana. It sells Indian-flavoured "craft" burgers - regional recipes built on Indian spices and chutneys - alongside fries and sides, desserts and beverages, through a hybrid estate of company-owned and franchised outlets that spans high-street, food-court, express and dine-in formats across India and into the United Kingdom. The business grows primarily through franchising, and its public web surface is organised around that motion: a menu, a store locator, franchise investment brackets, property-partner and bulk-order intake, and a complaint and feedback channel. Burger Singh is a restaurant operator rather than a software vendor and publishes no developer program, no API documentation and no commercial or partner-facing API. The only machine-readable interface it exposes
  is the WordPress REST content API behind its corporate site at burgersinghonline.com, captured here for discovery purposes.'
image: https://www.burgersinghonline.com/wp-content/uploads/2024/04/cropped-logo-v0.1-2.png
layout: provider
modified: '2026-08-08'
name: Burger Singh
nav: Providers
network: true
overview: 'Burger Singh publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Pages API, Media API, Taxonomy API, and 3 more. Tagged areas include Company, Restaurant, Quick Service Restaurant, Food and Beverage, and Franchising.


  Burger Singh''s developer surface includes support, authentication, code examples, and 19 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 4.5
    contract_quality: 55.3
    developer_ergonomics: 18.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/burger-singh/refs/heads/main/screenshots/burger-singh-2026-09-02T144958.png
security:
- kind: authentication
  name: Burger Singh Authentication
  slug: burger-singh-authentication
  summary_line: none/cookie/http-basic · 3 schemes
- kind: domain-security
  name: Burger Singh Domain Security
  slug: burger-singh-domain-security
  summary_line: TLSv1.3
slug: burger-singh
tags:
- Company
- Restaurant
- Quick Service Restaurant
- Food and Beverage
- Franchising
- Consumer
- India
- Retail
- Content
- WordPress
website: https://www.burgersinghonline.com/
---
