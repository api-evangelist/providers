---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Trendyol Marketplace / Partner API for sellers and integrators — product, order/shipment, returns, invoice, settlement, and webhook operations.
  name: Trendyol Marketplace API
  slug: trendyol-marketplace-api
artifact_total: 9
asyncapis:
- description: ''
  name: Trendyol Webhooks
  slug: trendyol-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/trendyol/rate-limits/trendyol-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trendyol-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/trendyol/security/trendyol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trendyol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trendyol.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.trendyol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trendyol.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.trendyol.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.trendyol.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developers.trendyol.com/docs/support-request
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.trendyol.com/docs/api-status
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.trendyol.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://medium.com/trendyol-tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trendyol
- group: auth
  href: https://artifacts.apis.io/trendyol/authentication/trendyol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trendyol-authentication.yml
- group: design
  href: https://artifacts.apis.io/trendyol/asyncapi/trendyol-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trendyol-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/trendyol/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/trendyol/mcp/trendyol-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/trendyol-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trendyol/llms/trendyol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trendyol-llms.txt
created: '2026-07-17'
description: 'Trendyol is Turkey''s largest e-commerce marketplace and a leading fashion and retail platform operating across Türkiye, the Gulf, Azerbaijan, and Central & Eastern Europe. Its Marketplace (Partner) API lets sellers and integrators manage the full commerce lifecycle: product catalog with category/brand/ attribute data, price and stock updates, order and shipment-package fulfillment, returns and claims, invoicing, settlements and financial reconciliation, the Export Center, customer questions, and order webhooks. Authentication is HTTP Basic (API key/secret) with a mandatory User-Agent header, plus an OAuth 2.0 authorization-code flow for multi-supplier integrators. Bulk writes are asynchronous and confirmed via a batchRequestId.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trendyol.png
layout: provider
modified: '2026-07-21'
name: Trendyol
nav: Providers
network: true
overview: 'Trendyol is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Fashion.


  The Trendyol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trendyol''s developer surface includes documentation, API reference, getting-started guide, support, changelog, engineering blog, authentication, and 10 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 3
  name: Trendyol Rate Limits
  slug: trendyol-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 41.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trendyol/trendyol-2026-08-17T082435.png
security:
- kind: authentication
  name: Trendyol Authentication
  slug: trendyol-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Trendyol Domain Security
  slug: trendyol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Fulfill an order package
  slug: trendyol-fulfill-an-order
- name: Handle a customer return (claim)
  slug: trendyol-handle-a-return
- name: List a product on Trendyol
  slug: trendyol-list-a-product
- name: Subscribe to order webhooks
  slug: trendyol-subscribe-to-webhooks
slug: trendyol
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Fashion
- Turkey
- Order Management
- Fulfillment
- Logistics
- Webhook
website: https://trendyol.com
---
