---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Fourthwall Agentic Access
  operation_count: 43
  slug: fourthwall-agentic-access
  summary_line: 43 operations · 18 acting
api_count: 12
apis:
- description: The Collections API from Fourthwall — 3 operation(s) for collections.
  name: Fourthwall Collections API
  slug: fourthwall-collections-api
- description: The Gifting API from Fourthwall — 4 operation(s) for gifting.
  name: Fourthwall Gifting API
  slug: fourthwall-gifting-api
- description: The Giveaways API from Fourthwall — 1 operation(s) for giveaways.
  name: Fourthwall Giveaways API
  slug: fourthwall-giveaways-api
- description: The Memberships API from Fourthwall — 3 operation(s) for memberships.
  name: Fourthwall Memberships API
  slug: fourthwall-memberships-api
- description: The Orders API from Fourthwall — 4 operation(s) for orders.
  name: Fourthwall Orders API
  slug: fourthwall-orders-api
- description: The Products API from Fourthwall — 3 operation(s) for products.
  name: Fourthwall Products API
  slug: fourthwall-products-api
- description: The Promotions API from Fourthwall — 2 operation(s) for promotions.
  name: Fourthwall Promotions API
  slug: fourthwall-promotions-api
- description: The Storefront Carts API from Fourthwall — 5 operation(s) for storefront carts.
  name: Fourthwall Storefront Carts API
  slug: fourthwall-storefront-carts-api
- description: The Storefront Collections API from Fourthwall — 3 operation(s) for storefront collections.
  name: Fourthwall Storefront Collections API
  slug: fourthwall-storefront-collections-api
- description: The Storefront Products API from Fourthwall — 1 operation(s) for storefront products.
  name: Fourthwall Storefront Products API
  slug: fourthwall-storefront-products-api
- description: The Storefront Shop API from Fourthwall — 1 operation(s) for storefront shop.
  name: Fourthwall Storefront Shop API
  slug: fourthwall-storefront-shop-api
- description: The Webhooks API from Fourthwall — 3 operation(s) for webhooks.
  name: Fourthwall Webhooks API
  slug: fourthwall-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: Fourthwall API
  slug: open-fourthwall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fourthwall-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fourthwall-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fourthwall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fourthwall-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fourthwall-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FourthwallHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fourthwall
- group: company
  title: ''
  type: Website
  url: https://fourthwall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fourthwall.com
- group: commercial
  title: ''
  type: Plans
  url: plans/fourthwall-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fourthwall-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fourthwall-finops.yml
created: '2026-07-01'
description: Fourthwall is a creator commerce platform for building a branded online shop and storefront, selling physical merch, digital products, memberships, and accepting donations and gifts. It exposes a public Storefront API (storefront token) for headless product/collection/cart experiences and a Platform / Open API (Basic Auth API key or OAuth) for managing orders, products, promotions, gifting, memberships, and webhooks.
finops:
- name: Fourthwall Finops
  service_category: Commerce and Creator Economy
  slug: fourthwall-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fourthwall.png
layout: provider
modified: '2026-07-01'
name: Fourthwall
nav: Providers
network: true
overview: 'Fourthwall publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Gifting API, Giveaways API, and 9 more. Tagged areas include Creator Commerce, Ecommerce, Merch, Storefront, and Memberships.


  Fourthwall''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Fourthwall Plans Pricing
  plan_count: 2
  slug: fourthwall-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 4
  name: Fourthwall Rate Limits
  slug: fourthwall-rate-limits
scopes:
- name: Fourthwall Scopes
  scope_count: 14
  slug: fourthwall-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fourthwall/refs/heads/main/screenshots/fourthwall-2026-07-25T215052.png
security:
- kind: authentication
  name: Fourthwall Authentication
  slug: fourthwall-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Fourthwall Domain Security
  slug: fourthwall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fourthwall Vulnerability Disclosure
  slug: fourthwall-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fourthwall
tags:
- Creator Commerce
- Ecommerce
- Merch
- Storefront
- Memberships
- Donations
- Print on Demand
website: https://fourthwall.com/
---
