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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Terminal Shop Agentic Access
  operation_count: 37
  slug: terminal-shop-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Address API from Terminal — 2 operation(s) for address.
  name: Terminal Address API
  slug: terminal-shop-address-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The App API from Terminal — 2 operation(s) for app.
  name: Terminal App API
  slug: terminal-shop-app-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Card API from Terminal — 3 operation(s) for card.
  name: Terminal Card API
  slug: terminal-shop-card-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Cart API from Terminal — 5 operation(s) for cart.
  name: Terminal Cart API
  slug: terminal-shop-cart-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Email API from Terminal — 1 operation(s) for email.
  name: Terminal Email API
  slug: terminal-shop-email-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Order API from Terminal — 2 operation(s) for order.
  name: Terminal Order API
  slug: terminal-shop-order-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Product API from Terminal — 2 operation(s) for product.
  name: Terminal Product API
  slug: terminal-shop-product-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Profile API from Terminal — 1 operation(s) for profile.
  name: Terminal Profile API
  slug: terminal-shop-profile-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Subscription API from Terminal — 2 operation(s) for subscription.
  name: Terminal Subscription API
  slug: terminal-shop-subscription-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The Token API from Terminal — 2 operation(s) for token.
  name: Terminal Token API
  slug: terminal-shop-token-api
- baseURL: https://api.terminal.shop
  baseurl_source: declared
  description: The View API from Terminal — 1 operation(s) for view.
  name: Terminal View API
  slug: terminal-shop-view-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Terminal Shop Address API
  slug: open-terminal-shop-address-api
- collection_type: open
  name: Terminal Shop Address App API
  slug: open-terminal-shop-app-api
- collection_type: open
  name: Terminal Shop Address Card API
  slug: open-terminal-shop-card-api
- collection_type: open
  name: Terminal Shop Address Cart API
  slug: open-terminal-shop-cart-api
- collection_type: open
  name: Terminal Shop Address Email API
  slug: open-terminal-shop-email-api
- collection_type: open
  name: Terminal Shop Address Order API
  slug: open-terminal-shop-order-api
- collection_type: open
  name: Terminal Shop Address Product API
  slug: open-terminal-shop-product-api
- collection_type: open
  name: Terminal Shop Address Profile API
  slug: open-terminal-shop-profile-api
- collection_type: open
  name: Terminal Shop Address Subscription API
  slug: open-terminal-shop-subscription-api
- collection_type: open
  name: Terminal Shop Address Token API
  slug: open-terminal-shop-token-api
- collection_type: open
  name: Terminal Shop Address View API
  slug: open-terminal-shop-view-api
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
overview: 'Terminal publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Address API, App API, Card API, and 8 more. Tagged areas include Coffee, E-Commerce, Developers, SSH, and Ordering.


  Terminal''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Terminal Shop Plans Pricing
  plan_count: 3
  slug: terminal-shop-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Terminal Shop Rate Limits
  slug: terminal-shop-rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Developers
- SSH
- Ordering
website: https://www.terminal.shop
---
