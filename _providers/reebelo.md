---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The seller-side REST API behind Reebelo's Cobalt vendor back-office. Authenticated with a Reebelo-issued x-api-key header, it exposes offer management (list offers, look up an offer by SKU, create/upd
  name: Reebelo Vendor Integration API (Cobalt)
  slug: reebelo-vendor-api
artifact_total: 6
asyncapis:
- description: ''
  name: Reebelo Webhooks
  slug: reebelo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://reebelo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cobalt.reebelo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cobalt.reebelo.com/documentation/home
- group: docs
  title: ''
  type: APIReference
  url: https://cobalt.reebelo.com/documentation/custom-api
- group: start
  title: ''
  type: GettingStarted
  url: https://cobalt.reebelo.com/documentation/home
- group: start
  title: ''
  type: Login
  url: https://cobalt.reebelo.com/
- group: operate
  title: ''
  type: Support
  url: https://reebelo.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.reebelo.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reebelo.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reebelo.com/policies/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/reebelo-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reebelo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reebelo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reebelo-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reebelo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/reebelo-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reebelo-domain-security.yml
created: '2026-08-26'
description: 'Reebelo is a marketplace for certified refurbished consumer technology — smartphones, laptops, tablets, smartwatches, gaming and home electronics — sold by a vetted network of third-party refurbishers at up to 70% below new, with a 12-month warranty and a 30-day trial. Founded in 2019 and operating in the United States, Australia, New Zealand and Singapore, Reebelo positions refurbished tech as the sustainable alternative to new-device purchase. Its developer surface is seller-facing rather than buyer-facing: the Cobalt vendor back-office publishes a REST integration API on https://a.reebelo.com that lets a refurbisher list and reprice offers, pull orders, push carrier tracking and IMEI numbers, and upload seller invoices, alongside hosted-CSV feed and order-forwarding webhook alternatives for vendors without API resources.'
image: https://edge.reebelo.com/images/opengraph.png
layout: provider
modified: '2026-08-26'
name: Reebelo
nav: Providers
network: true
overview: 'Reebelo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Refurbished Electronics, Marketplace, E-Commerce, Consumer Electronics, and Reverse Logistics.


  The Reebelo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Reebelo''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 12 more developer resources.'
plans:
- name: Reebelo Plans Pricing
  plan_count: 0
  slug: reebelo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Reebelo Rate Limits
  slug: reebelo-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 27.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reebelo/refs/heads/main/screenshots/reebelo-2026-09-02T153209.png
security:
- kind: authentication
  name: Reebelo Authentication
  slug: reebelo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Reebelo Domain Security
  slug: reebelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reebelo
tags:
- Refurbished Electronics
- Marketplace
- E-Commerce
- Consumer Electronics
- Reverse Logistics
- Circular Economy
- Retail
- Inventory
- Order
- Seller Integration
website: https://reebelo.com/
---
