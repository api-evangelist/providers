---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
- acting_count: 25
  human_in_the_loop: 0
  name: Dodo Payments Agentic Access
  operation_count: 49
  slug: dodo-payments-agentic-access
  summary_line: 49 operations · 25 acting
api_count: 1
apis:
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Checkout Sessions API from Dodo Payments — 2 operation(s) for checkout sessions.
  name: Dodo Payments Checkout Sessions API
  slug: dodo-payments-checkout-sessions-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Customers API from Dodo Payments — 3 operation(s) for customers.
  name: Dodo Payments Customers API
  slug: dodo-payments-customers-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Discounts API from Dodo Payments — 2 operation(s) for discounts.
  name: Dodo Payments Discounts API
  slug: dodo-payments-discounts-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Disputes API from Dodo Payments — 2 operation(s) for disputes.
  name: Dodo Payments Disputes API
  slug: dodo-payments-disputes-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The License Keys API from Dodo Payments — 2 operation(s) for license keys.
  name: Dodo Payments License Keys API
  slug: dodo-payments-license-keys-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Licenses API from Dodo Payments — 3 operation(s) for licenses.
  name: Dodo Payments Licenses API
  slug: dodo-payments-licenses-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Payments API from Dodo Payments — 4 operation(s) for payments.
  name: Dodo Payments Payments API
  slug: dodo-payments-payments-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Payouts API from Dodo Payments — 1 operation(s) for payouts.
  name: Dodo Payments Payouts API
  slug: dodo-payments-payouts-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Products API from Dodo Payments — 4 operation(s) for products.
  name: Dodo Payments Products API
  slug: dodo-payments-products-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Refunds API from Dodo Payments — 2 operation(s) for refunds.
  name: Dodo Payments Refunds API
  slug: dodo-payments-refunds-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Subscriptions API from Dodo Payments — 4 operation(s) for subscriptions.
  name: Dodo Payments Subscriptions API
  slug: dodo-payments-subscriptions-api
- baseURL: https://live.dodopayments.com
  baseurl_source: declared
  description: The Webhooks API from Dodo Payments — 4 operation(s) for webhooks.
  name: Dodo Payments Webhooks API
  slug: dodo-payments-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dodo Payments Checkout Sessions API
  slug: open-dodo-payments-checkout-sessions-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Customers API
  slug: open-dodo-payments-customers-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Discounts API
  slug: open-dodo-payments-discounts-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Disputes API
  slug: open-dodo-payments-disputes-api
- collection_type: open
  name: Dodo Payments Checkout Sessions License Keys API
  slug: open-dodo-payments-license-keys-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Licenses API
  slug: open-dodo-payments-licenses-api
- collection_type: open
  name: Dodo Checkout Sessions Payments API
  slug: open-dodo-payments-payments-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Payouts API
  slug: open-dodo-payments-payouts-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Products API
  slug: open-dodo-payments-products-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Refunds API
  slug: open-dodo-payments-refunds-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Subscriptions API
  slug: open-dodo-payments-subscriptions-api
- collection_type: open
  name: Dodo Payments Checkout Sessions Webhooks API
  slug: open-dodo-payments-webhooks-api
- collection_type: open
  name: Dodo Payments API
  slug: open-dodo-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dodo-payments-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dodo-payments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dodo-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dodo-payments-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dodopayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dodopayments
- group: company
  title: ''
  type: Website
  url: https://dodopayments.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dodopayments.com
- group: commercial
  title: ''
  type: Plans
  url: plans/dodo-payments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dodo-payments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dodo-payments-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dodopayments.com/rss.xml
created: '2026-06-21'
description: Dodo Payments is a merchant-of-record (MoR) payments platform for global digital businesses. Its REST API handles one-time payments, subscriptions, checkout sessions, customers, products, discounts, license keys, payouts, refunds, disputes, and webhooks, while Dodo acts as the seller of record and calculates, collects, and remits sales tax, VAT, and GST across 190+ jurisdictions.
finops:
- name: Dodo Payments Finops
  service_category: Payments and Commerce
  slug: dodo-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dodo-payments.png
layout: provider
modified: '2026-06-21'
name: Dodo Payments
nav: Providers
network: true
overview: 'Dodo Payments publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Checkout Sessions API, Customers API, Discounts API, and 9 more. Tagged areas include Payments, Merchant of Record, Subscription, Billing, and Global Commerce.


  Dodo Payments'' developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Dodo Payments Plans Pricing
  plan_count: 3
  slug: dodo-payments-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Dodo Payments Rate Limits
  slug: dodo-payments-rate-limits
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dodo-payments/refs/heads/main/screenshots/dodo-payments-2026-07-25T212230.png
security:
- kind: authentication
  name: Dodo Payments Authentication
  slug: dodo-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dodo Payments Domain Security
  slug: dodo-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dodo Payments Vulnerability Disclosure
  slug: dodo-payments-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dodo-payments
tags:
- Payments
- Merchant of Record
- Subscription
- Billing
- Global Commerce
website: https://dodopayments.com
---
