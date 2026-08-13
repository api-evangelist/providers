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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Terminal Shop Agentic Access
  operation_count: 37
  slug: terminal-shop-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 11
apis:
- description: The Address API from Terminal — 2 operation(s) for address.
  name: Terminal Address API
  slug: terminal-shop-address-api
- description: The App API from Terminal — 2 operation(s) for app.
  name: Terminal App API
  slug: terminal-shop-app-api
- description: The Card API from Terminal — 3 operation(s) for card.
  name: Terminal Card API
  slug: terminal-shop-card-api
- description: The Cart API from Terminal — 5 operation(s) for cart.
  name: Terminal Cart API
  slug: terminal-shop-cart-api
- description: The Email API from Terminal — 1 operation(s) for email.
  name: Terminal Email API
  slug: terminal-shop-email-api
- description: The Order API from Terminal — 2 operation(s) for order.
  name: Terminal Order API
  slug: terminal-shop-order-api
- description: The Product API from Terminal — 2 operation(s) for product.
  name: Terminal Product API
  slug: terminal-shop-product-api
- description: The Profile API from Terminal — 1 operation(s) for profile.
  name: Terminal Profile API
  slug: terminal-shop-profile-api
- description: The Subscription API from Terminal — 2 operation(s) for subscription.
  name: Terminal Subscription API
  slug: terminal-shop-subscription-api
- description: The Token API from Terminal — 2 operation(s) for token.
  name: Terminal Token API
  slug: terminal-shop-token-api
- description: The View API from Terminal — 1 operation(s) for view.
  name: Terminal View API
  slug: terminal-shop-view-api
artifact_total: 18
collections:
- collection_type: open
  name: Terminal Shop API
  slug: open-terminal-shop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terminal-shop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terminal-shop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terminal-shop-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/terminaldotshop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/terminalshop
- group: company
  title: ''
  type: Website
  url: https://www.terminal.shop
- group: docs
  title: ''
  type: Documentation
  url: https://www.terminal.shop/api
- group: commercial
  title: ''
  type: Plans
  url: plans/terminal-shop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/terminal-shop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/terminal-shop-finops.yml
created: '2026-06-20'
description: Terminal is a developer-focused coffee company with an API-first, SSH-first ordering experience. The Terminal Shop API is a public REST API (Bearer token) for browsing coffee products, managing carts, placing orders, running subscriptions, and handling addresses, cards, and profiles - the same surface that powers the famous `ssh terminal.shop` storefront.
finops:
- name: Terminal Shop Finops
  service_category: E-Commerce and Retail
  slug: terminal-shop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terminal-shop.png
layout: provider
modified: '2026-06-20'
name: Terminal
nav: Providers
network: true
overview: 'Terminal publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Address API, App API, Card API, and 8 more. Tagged areas include Coffee, E-Commerce, Developer, SSH, and Ordering.


  Terminal''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Terminal Shop Plans Pricing
  plan_count: 3
  slug: terminal-shop-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Terminal Shop Rate Limits
  slug: terminal-shop-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terminal-shop/refs/heads/main/screenshots/terminal-shop-2026-06-20T195128.png
security:
- kind: authentication
  name: Terminal Shop Authentication
  slug: terminal-shop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Terminal Shop Domain Security
  slug: terminal-shop-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: terminal-shop
tags:
- Coffee
- E-Commerce
- Developer
- SSH
- Ordering
website: https://www.terminal.shop
---
