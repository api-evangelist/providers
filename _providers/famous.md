---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://amazecommerce.com/pricing
  - https://api.teespring.com/docs
  trial: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: Operations about internals
  name: Famous Internal API
  slug: famous-internal-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: Operations about sellers
  name: Famous Seller API
  slug: famous-seller-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Auth Tokens API from Famous — 1 operation(s) for auth tokens.
  name: Famous Auth Tokens API
  slug: famous-auth-tokens-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Campaigns API from Famous — 1 operation(s) for campaigns.
  name: Famous Campaigns API
  slug: famous-campaigns-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Categories API from Famous — 2 operation(s) for categories.
  name: Famous Categories API
  slug: famous-categories-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Recommenders API from Famous — 1 operation(s) for recommenders.
  name: Famous Recommenders API
  slug: famous-recommenders-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Rush Prices API from Famous — 1 operation(s) for rush prices.
  name: Famous Rush Prices API
  slug: famous-rush-prices-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Search Suggestions API from Famous — 1 operation(s) for search suggestions.
  name: Famous Search Suggestions API
  slug: famous-search-suggestions-api
- baseURL: https://api.teespring.com/
  baseurl_source: declared
  description: The Users API from Famous — 3 operation(s) for users.
  name: Famous Users API
  slug: famous-users-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-famous-spring-api-swagger
common:
- group: other
  href: https://artifacts.apis.io/famous/capabilities/famous-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/famous-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.amaze.co/rss/
- group: other
  href: https://artifacts.apis.io/famous/overlays/famous-spring-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/famous-spring-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/famous/security/famous-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/famous-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/famous/authentication/famous-authentication.yml
  title: ''
  type: Authentication
  url: authentication/famous-authentication.yml
- group: design
  href: https://artifacts.apis.io/famous/conventions/famous-conventions.yml
  title: ''
  type: Conventions
  url: conventions/famous-conventions.yml
- group: design
  href: https://artifacts.apis.io/famous/errors/famous-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/famous-problem-types.yml
- group: design
  href: https://artifacts.apis.io/famous/data-model/famous-data-model.yml
  title: ''
  type: DataModel
  url: data-model/famous-data-model.yml
- group: operate
  href: https://artifacts.apis.io/famous/rate-limits/famous-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/famous-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/famous/conformance/famous-conformance.yml
  title: ''
  type: Conformance
  url: conformance/famous-conformance.yml
- group: design
  href: https://artifacts.apis.io/famous/lifecycle/famous-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/famous-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.teespring.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.teespring.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.teespring.com/docs
- group: auth
  href: https://artifacts.apis.io/famous/security/famous-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/famous-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://spri.ng/about/security
- group: build
  href: https://artifacts.apis.io/famous/packages/famous-packages.yml
  title: ''
  type: Packages
  url: packages/famous-packages.yml
- group: other
  href: https://artifacts.apis.io/famous/grpc/famous-user-identity-service.proto
  title: ''
  type: Protobuf
  url: grpc/famous-user-identity-service.proto
- group: other
  href: https://artifacts.apis.io/famous/grpc/famous-subscriptions-subscriptions.proto
  title: ''
  type: Protobuf
  url: grpc/famous-subscriptions-subscriptions.proto
- group: other
  href: https://artifacts.apis.io/famous/grpc/famous-onboarding-task_list_service.proto
  title: ''
  type: Protobuf
  url: grpc/famous-onboarding-task_list_service.proto
- group: other
  href: https://artifacts.apis.io/famous/grpc/famous-grpc.yml
  title: ''
  type: gRPC
  url: grpc/famous-grpc.yml
- group: agent
  href: https://artifacts.apis.io/famous/llms/famous-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/famous-llms.txt
- group: commercial
  href: https://artifacts.apis.io/famous/plans/famous-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/famous-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/famous/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://amaze.co/
- group: company
  title: ''
  type: About
  url: https://amaze.co/about-us
- group: company
  title: ''
  type: Blog
  url: https://blog.amaze.co/
- group: operate
  title: ''
  type: Support
  url: https://amaze.co/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.spri.ng/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teespring
- group: commercial
  title: ''
  type: Pricing
  url: https://amazecommerce.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.amazecommerce.com/signup
- group: start
  title: ''
  type: Login
  url: https://teespring.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amaze.co/policies/commerce/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amaze.co/policies/corporate/privacy-policy
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.amaze.co/
- group: company
  title: ''
  type: Careers
  url: https://jobs.lever.co/amaze
created: '2026-07-17'
description: 'Famous (famous.co) returns a 301 to Amaze (amaze.co), the creator-commerce platform operated by Amaze Holdings, Inc. Amaze describes itself as building the operating system for creator-led businesses, bringing commerce, content, media, and live shopping into one connected ecosystem. Its products include Amaze Commerce (creator storefronts and AI-powered product creation, at amazecommerce.com), Spring (spri.ng, the creator storefront brand formerly known as Teespring), Amaze Live (shoppable livestreams), and Amaze Media (performance marketing and audience targeting for brands). The company reports 190K+ creators, 1.7B+ lifetime fan reach, and operations across 183 countries. Surfaced originally as a portfolio company of Insight Partners. A public, machine-readable API surface WAS found on the second enrichment pass: the Spring Seller API, a Swagger 2.0 contract with 24 operations served live at api.teespring.com (Spring''s legacy API host), documented behind a Swagger UI at
  https://api.teespring.com/docs. Amaze also publishes first-party Protobuf/gRPC service contracts to npm under the @teespring scope.'
finops:
- has_sources: true
  method: derived
  name: Famous Finops
  primary_unit: subscription
  service_category: ''
  slug: famous-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/famous.png
layout: provider
modified: '2026-10-06'
name: Famous
nav: Providers
network: true
overview: 'Famous publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Internal API, Seller API, Auth Tokens API, and 6 more. Tagged areas include Company, Creator Economy, Commerce, Live Shopping, and Media.


  The Famous catalog on APIs.io includes 1 Spectral governance ruleset.


  Famous'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 30 more developer resources.'
plans:
- name: Famous Plans Pricing
  plan_count: 3
  slug: famous-plans-pricing
- name: Famous Price Estimates
  plan_count: 0
  slug: famous-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: Famous Rate Limits
  slug: famous-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Famous API Rules
  rule_count: 37
  severity_counts:
    error: 29
    hint: 0
    info: 3
    warn: 5
  slug: famous-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 38.4
    developer_ergonomics: 48.2
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 48.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/famous/famous-2026-07-25T214205.png
security:
- kind: authentication
  name: Famous Authentication
  slug: famous-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Famous Domain Security
  slug: famous-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Famous Vulnerability Disclosure
  slug: famous-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 4
skills:
- name: famous-authenticate-spring-seller
  slug: famous-authenticate-spring-seller
- name: famous-campaign-performance-review
  slug: famous-campaign-performance-review
- name: famous-message-buyers
  slug: famous-message-buyers
- name: famous-reconcile-seller-orders
  slug: famous-reconcile-seller-orders
slug: famous
tags:
- Company
- Creator Economy
- Commerce
- Live Shopping
- Media
- E-Commerce
- Marketing
- Print on Demand
- Merchandise
- Storefront
- Order
- Payouts
website: https://amaze.co/
---
