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
- acting_count: 27
  human_in_the_loop: 1
  name: Orb Billing Agentic Access
  operation_count: 51
  slug: orb-billing-agentic-access
  summary_line: 51 operations · 27 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Alerts API from Orb — 4 operation(s) for alerts.
  name: Orb Alerts API
  slug: orb-billing-alerts-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Coupons API from Orb — 2 operation(s) for coupons.
  name: Orb Coupons API
  slug: orb-billing-coupons-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Credits API from Orb — 4 operation(s) for credits.
  name: Orb Credits API
  slug: orb-billing-credits-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Customers API from Orb — 5 operation(s) for customers.
  name: Orb Customers API
  slug: orb-billing-customers-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Events API from Orb — 4 operation(s) for events.
  name: Orb Events API
  slug: orb-billing-events-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Invoices API from Orb — 4 operation(s) for invoices.
  name: Orb Invoices API
  slug: orb-billing-invoices-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Items API from Orb — 2 operation(s) for items.
  name: Orb Items API
  slug: orb-billing-items-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Metrics API from Orb — 2 operation(s) for metrics.
  name: Orb Metrics API
  slug: orb-billing-metrics-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Plans API from Orb — 2 operation(s) for plans.
  name: Orb Plans API
  slug: orb-billing-plans-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Prices API from Orb — 3 operation(s) for prices.
  name: Orb Prices API
  slug: orb-billing-prices-api
- baseURL: https://api.withorb.com/v1
  baseurl_source: declared
  description: The Subscriptions API from Orb — 5 operation(s) for subscriptions.
  name: Orb Subscriptions API
  slug: orb-billing-subscriptions-api
- description: The Alerts API from Orb — 3 operation(s) for alerts.
  name: Orb Alerts API
  slug: orb-alerts-api
- description: The Availability API from Orb — 1 operation(s) for availability.
  name: Orb Availability API
  slug: orb-availability-api
- description: The Coupons API from Orb — 1 operation(s) for coupons.
  name: Orb Coupons API
  slug: orb-coupons-api
- description: The Credit Notes API from Orb — 1 operation(s) for credit notes.
  name: Orb Credit Notes API
  slug: orb-credit-notes-api
- description: The Customers API from Orb — 2 operation(s) for customers.
  name: Orb Customers API
  slug: orb-customers-api
- description: The Events API from Orb — 1 operation(s) for events.
  name: Orb Events API
  slug: orb-events-api
- description: The Invoices API from Orb — 1 operation(s) for invoices.
  name: Orb Invoices API
  slug: orb-invoices-api
- description: The Plans API from Orb — 1 operation(s) for plans.
  name: Orb Plans API
  slug: orb-plans-api
- description: The Prices API from Orb — 1 operation(s) for prices.
  name: Orb Prices API
  slug: orb-prices-api
- description: The Subscriptions API from Orb — 2 operation(s) for subscriptions.
  name: Orb Subscriptions API
  slug: orb-subscriptions-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orb Alerts API
  slug: open-orb-billing-alerts-api
- collection_type: open
  name: Orb Alerts Coupons API
  slug: open-orb-billing-coupons-api
- collection_type: open
  name: Orb Alerts Credits API
  slug: open-orb-billing-credits-api
- collection_type: open
  name: Orb Alerts Customers API
  slug: open-orb-billing-customers-api
- collection_type: open
  name: Orb Alerts Events API
  slug: open-orb-billing-events-api
- collection_type: open
  name: Orb Alerts Invoices API
  slug: open-orb-billing-invoices-api
- collection_type: open
  name: Orb Alerts Items API
  slug: open-orb-billing-items-api
- collection_type: open
  name: Orb Alerts Metrics API
  slug: open-orb-billing-metrics-api
- collection_type: open
  name: Orb Alerts Plans API
  slug: open-orb-billing-plans-api
- collection_type: open
  name: Orb Alerts Prices API
  slug: open-orb-billing-prices-api
- collection_type: open
  name: Orb Alerts Subscriptions API
  slug: open-orb-billing-subscriptions-api
- collection_type: open
  name: Orb API
  slug: open-orb-billing
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orb-billing-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/orb-billing-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orb-billing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orb-billing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orb-billing-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orbcorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withorb
- group: company
  title: ''
  type: Website
  url: https://www.withorb.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withorb.com
- group: commercial
  title: ''
  type: Plans
  url: plans/orb-billing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orb-billing-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/orb-billing-finops.yml
created: '2026-06-20'
description: Orb is a usage-based billing and metering platform that turns product usage events into subscriptions, prices, invoices, and credits. The Orb REST API ingests metered events, models customers, plans, prices, and items, runs subscriptions, and automates invoicing, credit ledgers, alerts, and webhooks for modern revenue teams.
finops:
- name: Orb Billing Finops
  service_category: Billing and Revenue Operations
  slug: orb-billing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orb-billing.png
layout: provider
modified: '2026-06-20'
name: Orb
nav: Providers
network: true
overview: 'Orb publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Coupons API, Credits API, and 18 more. Tagged areas include Billing, Usage-Based Billing, Metering, Subscription, and Invoicing.


  Orb''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Orb Billing Plans Pricing
  plan_count: 2
  slug: orb-billing-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Orb Billing Rate Limits
  slug: orb-billing-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 41.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/orb-billing/refs/heads/main/screenshots/orb-billing-2026-06-20T191155.png
security:
- kind: authentication
  name: Orb Billing Authentication
  slug: orb-billing-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orb Billing Domain Security
  slug: orb-billing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orb Billing Vulnerability Disclosure
  slug: orb-billing-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Orb Billing Trust Center
  slug: orb-billing-trust-center
  summary_line: SOC 2
slug: orb-billing
tags:
- Billing
- Usage-Based Billing
- Metering
- Subscription
- Invoicing
- FinOps
website: https://www.withorb.com
---
