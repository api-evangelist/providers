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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Creem Agentic Access
  operation_count: 22
  slug: creem-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Checkouts API from Creem — 1 operation(s) for checkouts.
  name: Creem Checkouts API
  slug: creem-checkouts-api
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Customers API from Creem — 2 operation(s) for customers.
  name: Creem Customers API
  slug: creem-customers-api
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Discounts API from Creem — 2 operation(s) for discounts.
  name: Creem Discounts API
  slug: creem-discounts-api
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Licenses API from Creem — 3 operation(s) for licenses.
  name: Creem Licenses API
  slug: creem-licenses-api
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Products API from Creem — 2 operation(s) for products.
  name: Creem Products API
  slug: creem-products-api
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Subscriptions API from Creem — 7 operation(s) for subscriptions.
  name: Creem Subscriptions API
  slug: creem-subscriptions-api
- baseURL: https://api.creem.io/v1
  baseurl_source: declared
  description: The Transactions API from Creem — 2 operation(s) for transactions.
  name: Creem Transactions API
  slug: creem-transactions-api
artifact_total: 23
collections:
- collection_type: open
  name: Creem Checkouts API
  slug: open-creem-checkouts-api
- collection_type: open
  name: Creem Checkouts Customers API
  slug: open-creem-customers-api
- collection_type: open
  name: Creem Checkouts Discounts API
  slug: open-creem-discounts-api
- collection_type: open
  name: Creem Checkouts Licenses API
  slug: open-creem-licenses-api
- collection_type: open
  name: Creem Checkouts Products API
  slug: open-creem-products-api
- collection_type: open
  name: Creem Checkouts Subscriptions API
  slug: open-creem-subscriptions-api
- collection_type: open
  name: Creem Checkouts Transactions API
  slug: open-creem-transactions-api
- collection_type: open
  name: Creem API
  slug: open-creem
common:
- group: company
  title: ''
  type: Blog
  url: https://www.creem.io/blog
- group: other
  href: https://artifacts.apis.io/creem/capabilities/creem-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/creem-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/creem/agentic-access/creem-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/creem-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/creem/security/creem-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/creem-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/creem/security/creem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creem-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/creem/authentication/creem-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creem-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armitage-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/creem-io
- group: company
  title: ''
  type: Website
  url: https://www.creem.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.creem.io
- group: commercial
  href: https://artifacts.apis.io/creem/plans/creem-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/creem-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/creem/rate-limits/creem-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/creem-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/creem/finops/creem-finops.yml
  title: ''
  type: FinOps
  url: finops/creem-finops.yml
created: '2026-06-21'
description: Creem is a merchant-of-record payments platform built for SaaS and AI startups. Its REST API handles products, hosted checkouts, customers, subscriptions, transactions, discounts, and software license keys, while Creem acts as the merchant of record to manage global sales tax, VAT, fraud, and compliance on the seller's behalf.
finops:
- has_sources: true
  method: generated
  name: Creem Finops
  primary_unit: ''
  service_category: Payments and Billing
  slug: creem-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/creem.png
layout: provider
modified: '2026-10-06'
name: Creem
nav: Providers
network: true
overview: 'Creem publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkouts API, Customers API, Discounts API, and 4 more. Tagged areas include Payments, Merchant of Record, Subscription, Software-as-a-Service, and Billing.


  The Creem catalog on APIs.io includes 1 Spectral governance ruleset.


  Creem''s developer surface includes engineering blog, authentication, documentation, and 10 more developer resources.'
plans:
- name: Creem Plans Pricing
  plan_count: 1
  slug: creem-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Creem Rate Limits
  slug: creem-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Creem API Rules
  rule_count: 63
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 1
  slug: creem-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 48.5
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 16.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/creem/creem-2026-07-25T210726.png
security:
- kind: authentication
  name: Creem Authentication
  slug: creem-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Creem Domain Security
  slug: creem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Creem Vulnerability Disclosure
  slug: creem-vulnerability-disclosure
  summary_line: no policy recorded
slug: creem
tags:
- Payments
- Merchant of Record
- Subscription
- Software-as-a-Service
- Billing
website: https://www.creem.io/
---
