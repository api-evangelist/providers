---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 18.0
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: The Zip Global Merchant API provides checkout, charge, capture, refund, and cancellation operations for merchants integrating Zip BNPL payments into their online storefront. It uses Bearer token authe
  name: Zip Global Merchant API
  slug: zip-global-merchant-api
- description: The Zip US Gateway API enables North American merchants to authorize, capture, refund, void, and confirm orders. It uses HMAC-SHA256 signature authentication via the X-QP-Signature header and supports
  name: Zip US Gateway API
  slug: zip-us-gateway-api
- description: The Zip New Zealand In-Store API enables point-of-sale merchants to create, commit, cancel, rollback, and query orders in physical retail environments. It uses Bearer token authentication derived from
  name: Zip NZ In-Store API
  slug: zip-nz-in-store-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zip-co-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.zip.co
- group: company
  title: ''
  type: Website
  url: https://zip.co
- group: start
  title: ''
  type: MerchantPortal
  url: https://merchant.us.zip.co
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zipMoney
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zipMoney
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/zip-co/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/zip-co/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/zip-co/refs/heads/main/finops/finops.yml
- group: auth
  title: ''
  type: Security
  url: https://zip.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zip.co/au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zip.co/au/terms
- group: operate
  title: ''
  type: Help
  url: https://help.zip.co
- group: company
  title: ''
  type: Blog
  url: https://zip.co/au/blog
- group: operate
  title: ''
  type: Status
  url: https://status.zip.co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zip-co
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/zipmoney
created: '2026-06-13'
description: Zip is a global BNPL (Buy Now Pay Later) and digital wallet platform that enables merchants to offer flexible payment plans to consumers at checkout. Zip provides REST APIs for checkout integration, order creation, payment capture, refunds, voids, merchant management, disputes, and consumer payment plan verification. The platform supports in-store, online, and ecommerce plugin integrations across Australia, New Zealand, the United States, Canada, and other markets.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zip-co.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Zip
nav: Providers
network: true
overview: 'Zip publishes 1 API on the [APIs.io](https://apis.io/) network: Global Merchant API. Tagged areas include BNPL, Buy Now Pay Later, Digital Wallet, Payments, and Fintech.


  The Zip catalog on APIs.io includes 1 JSON-LD context.


  Zip''s developer surface includes developer portal, engineering blog, status page, and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 46.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 37.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zip-co/refs/heads/main/screenshots/zip-co-2026-06-20T201915.png
security:
- kind: domain-security
  name: Zip Co Domain Security
  slug: zip-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zip-co
tags:
- BNPL
- Buy Now Pay Later
- Digital Wallet
- Payments
- Fintech
- Checkout
- Merchant Services
website: https://zip.co
---
