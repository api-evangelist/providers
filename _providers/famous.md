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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-03'
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
  description: Operations about v1s
  name: Famous V1 API
  slug: famous-v1-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-famous-spring-api-swagger
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/famous-spring-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/famous-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/famous-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/famous-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/famous-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/famous-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/famous-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/famous-conformance.yml
- group: design
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
  title: ''
  type: VulnerabilityDisclosure
  url: security/famous-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://spri.ng/about/security
- group: build
  title: ''
  type: Packages
  url: packages/famous-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/famous-user-identity-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/famous-subscriptions-subscriptions.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/famous-onboarding-task_list_service.proto
- group: other
  title: ''
  type: gRPC
  url: grpc/famous-grpc.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/famous-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/famous-plans-pricing.yml
- group: agent
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/famous.png
layout: provider
modified: '2026-08-13'
name: Famous
nav: Providers
network: true
overview: 'Famous publishes 3 APIs on the [APIs.io](https://apis.io/) network: Internal API, Seller API, and V1 API. Tagged areas include Company, Creator Economy, Commerce, Live Shopping, and Media.


  Famous'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 28 more developer resources.'
plans:
- name: Famous Plans Pricing
  plan_count: 3
  slug: famous-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Famous Rate Limits
  slug: famous-rate-limits
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 38.1
    developer_ergonomics: 48.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 43.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/famous/refs/heads/main/screenshots/famous-2026-07-25T214205.png
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
- Storefronts
- Order
- Payouts
website: https://amaze.co/
---
