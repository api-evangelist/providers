---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-09-16'
api_count: 12
apis:
- description: A first-party application backend on api.wowmomo.com behind an AWS Application Load Balancer, running an Express service scaffolded with DhiWise (its root serves a "welcome to node.js" page carrying t
  name: WOW! Momo App Backend
  slug: wow-momo-app-backend
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: Public author records for content published on the site.
  name: WOW! Momo Authors API
  slug: wow-momo-authors-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The `category` taxonomy terms registered on the site.
  name: WOW! Momo Categories API
  slug: wow-momo-categories-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The API root document and the oEmbed provider endpoint.
  name: WOW! Momo Discovery API
  slug: wow-momo-discovery-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The WOW! Momo media library — logos, campaign artwork and photography attached to the site.
  name: WOW! Momo Media API
  slug: wow-momo-media-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The marketing and policy pages published on www.wowmomo.com.
  name: WOW! Momo Pages API
  slug: wow-momo-pages-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: Cross-type search over everything published on www.wowmomo.com.
  name: WOW! Momo Search API
  slug: wow-momo-search-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The Yoast SEO head document for any wowmomo.com URL, including its schema.org JSON-LD graph.
  name: WOW! Momo SEO API
  slug: wow-momo-seo-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The publication statuses registered on the install.
  name: WOW! Momo Statuses API
  slug: wow-momo-statuses-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The `post_tag` taxonomy terms registered on the site.
  name: WOW! Momo Tags API
  slug: wow-momo-tags-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The taxonomies registered on the install and the routes that serve them.
  name: WOW! Momo Taxonomies API
  slug: wow-momo-taxonomies-api
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The post types registered on the install and the routes that serve them.
  name: WOW! Momo Types API
  slug: wow-momo-types-api
artifact_total: 16
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/security/wow-momo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wow-momo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wowmomo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wowmomo.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wowmomo.com/privacy/
- group: other
  title: ''
  type: Franchise
  url: https://www.wowmomo.com/franchise-form/
- group: other
  title: ''
  type: StoreLocator
  url: https://restaurants.wowmomo.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.wowmomo.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/wow-momo
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/openapi/_ae-authored/wow-momo-content-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/wow-momo-content-api-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/overlays/wow-momo-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wow-momo-content-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/llms/wow-momo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wow-momo-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/mcp/wow-momo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wow-momo-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/authentication/wow-momo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wow-momo-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/conventions/wow-momo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wow-momo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/errors/wow-momo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wow-momo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/data-model/wow-momo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wow-momo-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/lifecycle/wow-momo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wow-momo-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/conformance/wow-momo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wow-momo-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/packages/wow-momo-packages.yml
  title: ''
  type: Packages
  url: packages/wow-momo-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/plans/wow-momo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wow-momo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wow-momo/refs/heads/main/rate-limits/wow-momo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wow-momo-rate-limits.yml
created: '2026-09-04'
description: 'WOW! Momo Foods Private Limited is the Kolkata, India quick-service restaurant company founded in August 2008 by St. Xavier''s College alumni Sagar J. Daryani and Binod K. Homagai, which built a national chain around the momo and now operates three brands — WOW! Momo, WOW! China and WOW! Chicken (launched December 2021) — across roughly 650 outlets in more than 30 Indian cities, backed by Lighthouse Funds, Tiger Global, Khazanah Nasional and Oaks Capital. WOW! Momo runs no developer programme: it publishes no API documentation, developer portal, SDK, API pricing or support channel, and no company-authored OpenAPI, AsyncAPI or GraphQL contract exists anywhere public. It is catalogued here because www.wowmomo.com serves a live, anonymously readable WordPress REST API — advertised in the head of every page as <link rel="https://api.w.org/"> — exposing the site''s pages, media library, taxonomies, search index, oEmbed 1.0 provider endpoint and Yoast SEO head document, alongside
  a separate first-party application backend on api.wowmomo.com that answers every anonymous request, including a control path that cannot exist, with an identical NO_AUTH body.'
image: https://www.wowmomo.com/wp-content/uploads/2022/03/Wow-Momo-Logo.png
layout: provider
modified: '2026-09-04'
name: WOW! Momo
nav: Providers
network: true
overview: 'WOW! Momo publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authors API, Categories API, Discovery API, and 8 more. Tagged areas include Company, Restaurant, Food and Beverage, Quick Service Restaurant, and Retail.


  WOW! Momo''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Wow Momo Plans Pricing
  plan_count: 0
  slug: wow-momo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Wow Momo Rate Limits
  slug: wow-momo-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 13.1
    developer_ergonomics: 13.7
    discoverability: 74.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 19.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
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
  name: Wow Momo Authentication
  slug: wow-momo-authentication
  summary_line: http/apiKey/opaque-application-credential · 3 schemes
- kind: domain-security
  name: Wow Momo Domain Security
  slug: wow-momo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wow-momo
tags:
- Company
- Restaurant
- Food and Beverage
- Quick Service Restaurant
- Retail
- Hospitality
- Consumer
- Franchising
- Content
- WordPress
- oEmbed
- India
- Kolkata
website: https://www.wowmomo.com/
---
