---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: REST API for accepting and managing card and BNPL payments — create and pay orders, capture or void authorised (pre-auth) transactions, issue refunds, save cards as payment sources, and run 3-D Secure
  name: Limepay Payments API
  slug: limepay-payments-api
- description: 'REST API for platform and marketplace integrations to onboard and manage sub-merchants: create platform merchants, merchant bank accounts and merchant persons, run KYC/identification, retrieve merchan'
  name: Limepay Platform API
  slug: limepay-platform-api
- description: Embeddable, customisable checkout that merchants drop into a web store (with plugins for WooCommerce, Magento, PrestaShop and Salesforce Commerce Cloud) to accept card payments and present the pay-in-
  name: Limepay Checkout
  slug: limepay-checkout
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limepay-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/limepay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/limepay-packages.yml
- group: design
  title: ''
  type: Components
  url: components/limepay-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/limepay-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/limepay-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/limepay-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/limepay-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.limepay.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.limepay.com.au/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.limepay.com.au/developer-portal/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.limepay.com.au/developer-portal/api-reference
created: '2026-07-24'
description: Limepay was a Melbourne-based Australian embedded-payments and white-label buy-now-pay-later (BNPL) company that let merchants and platforms accept card payments and offer pay-in-instalments through a single drop-in checkout and a REST API. Its developer surface covered an embeddable Checkout, a Payments API (orders, order-pay, transaction capture/void, refunds, 3-D Secure and wallet payments such as Apple Pay and Google Pay), and a Platform API for marketplaces to onboard and manage sub-merchants, run KYC/identification, and pull settlement reports. Authentication used a Publishable API key for frontend/checkout calls, a Secret API key for server-to-server calls, and a platform API key for administrative onboarding, all passed as Bearer tokens. After a failed 2021 IPO, Limepay was acquired by ASX-listed Spenda in 2024 and its product line was continued under the April Solutions brand; the primary domain limepay.com.au now redirects to meetapril.com and the docs.limepay.com.au
  developer portal is gated behind a Redocly login. This profile documents Limepay's real, historically public API family honestly; no machine-readable OpenAPI is currently downloadable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Limepay
nav: Providers
network: true
overview: 'Limepay publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, BNPL, Payment Gateway, and Checkout.


  Limepay''s developer surface includes authentication, documentation, API reference, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 11.7
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limepay/refs/heads/main/screenshots/limepay-2026-07-25T225213.png
security:
- kind: authentication
  name: Limepay Authentication
  slug: limepay-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Limepay Domain Security
  slug: limepay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: limepay
tags:
- Payments
- Australia
- BNPL
- Payment Gateway
- Checkout
- Embedded Payments
- White Label
- Card Payments
- Marketplace
- Instalments
website: https://www.limepay.com.au/
---
