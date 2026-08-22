---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 10
  name: Cj Affiliate Agentic Access
  operation_count: 24
  slug: cj-affiliate-agentic-access
  summary_line: 24 operations · 10 human-in-the-loop
api_count: 9
apis:
- description: GraphQL API serving near-real-time commission and transaction data. The publisherCommissions and advertiserCommissions queries return commission records filtered by posting, event or locking date rang
  name: CJ Commission Detail API
  slug: cj-affiliate-commission-detail-api
- description: 'GraphQL API for product discovery, product feeds and catalog management across advertiser feeds. Ten queries cover common products, retail shoppingProducts (including GTIN and Google product category '
  name: CJ Product Search API
  slug: cj-affiliate-product-search-api
- description: Publisher-side REST API for finding advertisers in the CJ network by CID, program name, program URL or keywords, joined or not joined, returning account status, 7-day and 3-month EPC, primary category
  name: CJ Affiliate Advertiser Lookup API
  slug: cj-affiliate-advertiser-lookup-api
- description: Publisher-side REST API for finding placeable advertiser links across the whole CJ network in one call - by keyword, sub-category, link type, promotion type and dates, language, targeted country, rela
  name: CJ Affiliate Link Search API
  slug: cj-affiliate-link-search-api
- description: Advertiser-side REST API for looking up the publishers joined to a program - program terms with accept and expiry dates and join status, promotional methods, websites and PIDs with categories, country
  name: CJ Affiliate Publisher Lookup API
  slug: cj-affiliate-publisher-lookup-api
- description: GraphQL API through which advertisers submit the full transaction lifecycle - createOrders for new orders, restateOrders for changes and additions, cancelOrders for full corrections. CJ takes a determ
  name: CJ Affiliate Advertiser Tracking API
  slug: cj-affiliate-tracking-api
- description: Server-to-server JSON REST API through which CJ partners register a consumer click and receive back the final landing-page URL carrying the cjevent tracking parameter. Supports bounceless tracking exp
  name: CJ Affiliate Click Events API
  slug: cj-affiliate-click-events-api
- description: Server-to-server JSON REST API through which publishers exchange a standard CJ tracking link for a final destination URL, taking the consumer straight to the advertiser where a bounceless journey is a
  name: CJ Affiliate Publisher Tracking API
  slug: cj-affiliate-publisher-tracking-api
- description: DEPRECATED XML REST API for near-real-time commission and item-detail data. CJ's own documentation states it was to be removed on 1 June 2019 and directs integrators to the GraphQL Commission Detail A
  name: CJ Affiliate Commission Detail API (Legacy)
  slug: cj-affiliate-commission-detail-legacy-api
artifact_total: 26
asyncapis:
- description: 'CJ Affiliate''s ONLY event/streaming surface: the GraphQL subscriptions declared on the ads API at https://ads.api.cj.com/query. These are bulk catalog downloads — a subscription requests an advertiser'
  name: CJ Affiliate Product Catalog Streaming API
  slug: cj-affiliate-ads-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CJ Affiliate Advertiser Lookup API
  slug: open-cj-affiliate-advertiser-lookup-api
- collection_type: open
  name: CJ Affiliate Click Events API
  slug: open-cj-affiliate-click-events-api
- collection_type: open
  name: CJ Affiliate Commission Detail (Legacy) API
  slug: open-cj-affiliate-commission-detail-legacy-api
- collection_type: open
  name: CJ Affiliate Link Search API
  slug: open-cj-affiliate-link-search-api
- collection_type: open
  name: CJ Affiliate Publisher Lookup API
  slug: open-cj-affiliate-publisher-lookup-api
- collection_type: open
  name: CJ Affiliate Publisher Tracking API
  slug: open-cj-affiliate-publisher-tracking-api
- collection_type: open
  name: CJ Affiliate APIs
  slug: open-cj-affiliate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cj-affiliate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cj-affiliate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cj-affiliate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cj.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cj-affiliate-by-conversant
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cj.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cj.com/account/personal-access-tokens
- group: commercial
  title: ''
  type: Plans
  url: plans/cj-affiliate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cj-affiliate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cj-affiliate-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://junction.cj.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cj.com/docs/rest-apis/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cj.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cj.com/graphql/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cj.com/account/personal-access-tokens
- group: operate
  title: ''
  type: Support
  url: https://www.cj.com/support
- group: start
  title: ''
  type: SignUp
  url: https://www.cj.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cj.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cj.com/legal/privacy
- group: company
  title: ''
  type: Partners
  url: https://www.cj.com/advertiser/tech-partners
- group: docs
  title: ''
  type: GraphQL
  url: graphql/cj-affiliate-graphql.md
- group: design
  title: ''
  type: Conventions
  url: conventions/cj-affiliate-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cj-affiliate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cj-affiliate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cj-affiliate-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cj-affiliate-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cj-affiliate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cj-affiliate-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cj-affiliate-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/cj-affiliate-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/cj-affiliate-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cj-affiliate-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cj-affiliate-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cj-affiliate-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/cj-affiliate-ads-asyncapi.yml
created: '2026-07-05'
description: CJ Affiliate (formerly Commission Junction) is one of the largest affiliate marketing networks, connecting publishers with thousands of advertiser programs. Its current developer platform is three GraphQL APIs - Commission Detail at commissions.api.cj.com for near-real-time commission and transaction data, Product Search / Ads at ads.api.cj.com for product discovery, product feeds and catalog writes, and Advertiser Tracking at tracking.api.cj.com for submitting, restating and cancelling orders. Alongside them CJ still documents a family of classic XML REST APIs - Link Search, Advertiser Lookup, Publisher Lookup, the Automated Offer Feed and a deprecated Commission Detail - plus two JSON click-tracking APIs, the Click Events API and the Publisher Tracking API. Everything authenticates with a single long-lived personal access token minted by hand in the CJ developer portal; there is no OAuth, no scopes and no programmatic token issuance. GraphQL introspection is open and unauthenticated
  on all three endpoints.
finops:
- name: Cj Affiliate Finops
  service_category: Marketing and Advertising
  slug: cj-affiliate-finops
graphqls:
- description: CJ Affiliate's current developer surface is **GraphQL**. There are **three**
  name: CJ Affiliate GraphQL APIs
  slug: cj-affiliate-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cj-affiliate.png
layout: provider
mcp_servers:
- description: ''
  name: cj-affiliate-mcp.yml
  slug: cj-affiliate-mcpyml
modified: '2026-08-13'
name: CJ Affiliate
nav: Providers
network: true
overview: 'CJ Affiliate publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CJ Commission Detail API, CJ Product Search API, Advertiser Lookup API, and 5 more. Tagged areas include Affiliate Marketing, Affiliate Network, Commission, Product Search, and Publisher.


  The CJ Affiliate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CJ Affiliate''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, signup flow, and 29 more developer resources.'
plans:
- name: Cj Affiliate Plans Pricing
  plan_count: 2
  slug: cj-affiliate-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Cj Affiliate Rate Limits
  slug: cj-affiliate-rate-limits
score:
  band: developing
  composite: 50.2
  delta: -11.3
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 30.3
    contract_quality: 69.6
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cj-affiliate/refs/heads/main/screenshots/cj-affiliate-2026-07-25T205448.png
security:
- kind: authentication
  name: Cj Affiliate Authentication
  slug: cj-affiliate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cj Affiliate Domain Security
  slug: cj-affiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cj-affiliate
tags:
- Affiliate Marketing
- Affiliate Network
- Commission
- Product Search
- Publisher
- Advertiser
- GraphQL
- Ecommerce
- Product Feeds
- Conversion Tracking
- Attribution
- Performance Marketing
- Retail
- Coupons
website: https://www.cj.com/
---
