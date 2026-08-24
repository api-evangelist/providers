---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - https://www.markable.ai/pricing
  - https://docs-dev.markable.ai/#getting-started
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Markable's visual search platform API. Index catalogs of products or styles, then search for visually similar items inside images and video. Covers catalog and catalog-item management, product search,
  name: Markable Lens API
  slug: markable-lens-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/markable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.markable.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs-dev.markable.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs-dev.markable.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-dev.markable.ai/#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/markable-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.markable.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/markable-ai/en
- group: start
  title: ''
  type: SignUp
  url: https://app-prod.markable.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.markable.ai/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/markable-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/markable-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/markable-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/markable-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/markable-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/markable-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/markable-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/markable-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/markable-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/markable-llms.txt
created: '2026-07-17'
description: Markable (markable.ai) is an all-in-one monetization platform for affiliate creators and social-commerce influencers. It turns social posts into revenue with smart affiliate deeplinks across Amazon, Target, and Walmart, a shop-in-bio storefront, storefront sync for product collections, Instagram auto-DM replies, AI-generated collages and captions, viral-product discovery, and performance analytics. It is offered as an iOS app and a desktop web app, with a creator performance/boosting program. Markable is backed by Partech. Markable also published an earlier developer product, the Markable Lens API — a visual search platform for finding products and styles inside images and video against indexed catalogs — whose reference is still publicly served at docs-dev.markable.ai. Access to that API is gated on manual developer verification, no machine-readable contract (OpenAPI/AsyncAPI/GraphQL/MCP) is published, and the API hosts it documents were not reachable when last probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/markable.png
layout: provider
modified: '2026-08-13'
name: Markable
nav: Providers
network: true
overview: 'Markable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Affiliate Marketing, Social Commerce, and Influencer Marketing.


  Markable''s developer surface includes documentation, API reference, getting-started guide, pricing, support, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Markable Plans Pricing
  plan_count: 5
  slug: markable-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Markable Rate Limits
  slug: markable-rate-limits
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 35.1
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/markable/refs/heads/main/screenshots/markable-2026-07-25T230203.png
security:
- kind: authentication
  name: Markable Authentication
  slug: markable-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Markable Domain Security
  slug: markable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: markable
tags:
- Company
- Creator Economy
- Affiliate Marketing
- Social Commerce
- Influencer Marketing
- Content Monetization
- Social-Media
- Visual Search
- Computer-Vision
- Product Discovery
- Image Recognition
- Video Search
website: https://www.markable.ai/
---
