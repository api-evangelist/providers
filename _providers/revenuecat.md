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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 2
  name: Revenuecat Agentic Access
  operation_count: 34
  slug: revenuecat-agentic-access
  summary_line: 34 operations · 19 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Outbound webhooks that POST subscription lifecycle events (INITIAL_PURCHASE, RENEWAL, CANCELLATION, EXPIRATION, BILLING_ISSUE, PRODUCT_CHANGE, and more) to a customer endpoint, secured with an Authori
  name: RevenueCat Webhooks
  slug: revenuecat-webhooks
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 app (platform integration) management.
  name: RevenueCat Apps API
  slug: revenuecat-apps-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 customer management.
  name: RevenueCat Customers API
  slug: revenuecat-customers-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v1 promotional entitlement grant and revoke.
  name: RevenueCat Entitlements (v1) API
  slug: revenuecat-entitlements-v1-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 entitlement definitions.
  name: RevenueCat Entitlements (v2) API
  slug: revenuecat-entitlements-v2-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v1 offering fetch and override.
  name: RevenueCat Offerings (v1) API
  slug: revenuecat-offerings-v1-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 offering definitions.
  name: RevenueCat Offerings (v2) API
  slug: revenuecat-offerings-v2-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 package definitions within an offering.
  name: RevenueCat Packages API
  slug: revenuecat-packages-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 product catalog management.
  name: RevenueCat Products API
  slug: revenuecat-products-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v2 project management.
  name: RevenueCat Projects API
  slug: revenuecat-projects-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v1 receipt validation and transaction lifecycle operations.
  name: RevenueCat Purchases API
  slug: revenuecat-purchases-api
- baseURL: https://api.revenuecat.com/v1
  baseurl_source: declared
  description: v1 customer (app user) records, attributes, and state.
  name: RevenueCat Subscribers API
  slug: revenuecat-subscribers-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RevenueCat REST Apps API
  slug: open-revenuecat-apps-api
- collection_type: open
  name: RevenueCat REST Apps Customers API
  slug: open-revenuecat-customers-api
- collection_type: open
  name: RevenueCat REST Apps Entitlements (v1) API
  slug: open-revenuecat-entitlements-v1-api
- collection_type: open
  name: RevenueCat REST Apps Entitlements (v2) API
  slug: open-revenuecat-entitlements-v2-api
- collection_type: open
  name: RevenueCat REST Apps Offerings (v1) API
  slug: open-revenuecat-offerings-v1-api
- collection_type: open
  name: RevenueCat REST Apps Offerings (v2) API
  slug: open-revenuecat-offerings-v2-api
- collection_type: open
  name: RevenueCat REST Apps Packages API
  slug: open-revenuecat-packages-api
- collection_type: open
  name: RevenueCat REST Apps Products API
  slug: open-revenuecat-products-api
- collection_type: open
  name: RevenueCat REST Apps Projects API
  slug: open-revenuecat-projects-api
- collection_type: open
  name: RevenueCat REST Apps Purchases API
  slug: open-revenuecat-purchases-api
- collection_type: open
  name: RevenueCat REST Apps Subscribers API
  slug: open-revenuecat-subscribers-api
- collection_type: open
  name: RevenueCat REST API
  slug: open-revenuecat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revenuecat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revenuecat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revenuecat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RevenueCat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenuecat
- group: company
  title: ''
  type: Website
  url: https://www.revenuecat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.revenuecat.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/revenuecat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revenuecat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revenuecat-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.revenuecat.com/blog/rss.xml
created: '2026-07-01'
description: RevenueCat provides in-app subscription and purchase infrastructure for mobile and web apps. It abstracts App Store, Google Play, Amazon, Stripe, Roku, and Paddle billing behind cross-platform SDKs and a REST API, handling receipt validation, entitlements, subscriber state, offerings and paywalls, experiments, and subscription analytics. A v1 REST API manages live subscribers and purchases; a v2 REST API manages the project catalog (projects, apps, products, entitlements, offerings, packages); webhooks stream subscription lifecycle events.
finops:
- name: Revenuecat Finops
  service_category: Developer Tools
  slug: revenuecat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revenuecat.png
layout: provider
modified: '2026-07-01'
name: RevenueCat
nav: Providers
network: true
overview: 'RevenueCat publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Customers API, Entitlements (v1) API, and 8 more. Tagged areas include Subscription, In-App Purchases, Billing, Mobile, and Entitlements.


  RevenueCat''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Revenuecat Plans Pricing
  plan_count: 4
  slug: revenuecat-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Revenuecat Rate Limits
  slug: revenuecat-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revenuecat/refs/heads/main/screenshots/revenuecat-2026-09-02T153711.png
security:
- kind: authentication
  name: Revenuecat Authentication
  slug: revenuecat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Revenuecat Domain Security
  slug: revenuecat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revenuecat
tags:
- Subscription
- In-App Purchases
- Billing
- Mobile
- Entitlements
website: https://www.revenuecat.com/
---
