---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The HTTP API behind the Kueski Pay merchant widgets. The widgets.js library authenticates with the merchant public key as an HTTP bearer token and reads merchant configuration and installment-messagin
  name: Kueski Pay Widget Configuration API
  slug: kueski-pay-widget-configuration-api
- description: The merchant-facing Kueski Pay order API used by the first-party e-commerce plugins. It validates merchant API keys, creates a Kueski Pay order and returns a hosted checkout callback URL for redirect,
  name: Kueski Pay Merchant Orders API
  slug: kueski-pay-merchant-orders-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.kueski.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/kueski-dev/Dev-Center/wiki
- group: docs
  title: ''
  type: Documentation
  url: https://www.kueskipay.com/guias-de-integracion
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kueskipay.com/para-comercios
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kueski-dev
- group: operate
  title: ''
  type: Support
  url: https://preguntas.frecuentes.kueski.com/hc/es/categories/14632860970907-Kueski-Pay
- group: operate
  title: ''
  type: HelpCenter
  url: https://kueskib2b.zendesk.com/hc/es-mx
- group: company
  title: ''
  type: Blog
  url: https://blog.kueski.com/comercio-electronico/
- group: start
  title: ''
  type: SignUp
  url: https://www.kueskipay.com/registro-comercios
- group: start
  title: ''
  type: Login
  url: https://negocios.kueski.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kueskipay.com/tyc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://preguntas.frecuentes.kueski.com/hc/es/articles/12385599806747-PRIVACY-NOTICE-FOR-THIRD-PARTIES-AND-COMMERCIAL-ALLIES-OF-KUESKI-SAPI-DE-CV-SOFOM-ENR
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kueski.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kueski-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kueski-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/kueski-packages.yml
- group: design
  title: ''
  type: Components
  url: components/kueski-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kueski-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kueski-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kueski-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kueski-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kueski-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kueski-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kueski-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kueski-llms.txt
created: '2026-08-04'
description: Kueski is a Mexican financial technology company founded in 2012 and headquartered in Guadalajara, Jalisco, offering online consumer credit across Mexico. Its flagship product, Kueski Pay, is a buy-now-pay-later (BNPL) payment method that lets shoppers buy without a credit card and repay in biweekly installments at thousands of online and physical merchants. Kueski also offers personal loans and cash advances. For merchants, Kueski Pay is distributed as e-commerce platform plugins (WooCommerce, Shopify, VTEX IO, Magento, PrestaShop, Tiendanube, T1 Paginas) plus a JavaScript widget library and a bearer-token HTTP merchant API for order creation, order synchronization and refunds. Kueski operates as a SOFOM E.N.R. regulated entity registered with Mexico's CONDUSEF.
image: https://cdn.prod.website-files.com/614d688b383096276930acef/64e2c5d130257b8c874270de_kueskipay.svg
layout: provider
modified: '2026-08-04'
name: Kueski
nav: Providers
network: true
overview: 'Kueski publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Buy Now Pay Later, Lending, and Fintech.


  Kueski''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, changelog, authentication, and 18 more developer resources.'
random_paper: 72
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 32.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kueski/refs/heads/main/screenshots/kueski-2026-08-07T171345.png
security:
- kind: authentication
  name: Kueski Authentication
  slug: kueski-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Kueski Domain Security
  slug: kueski-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kueski
tags:
- Company
- Payments
- Buy Now Pay Later
- Lending
- Fintech
- Financial Services
- Consumer Credit
- E-Commerce
- Checkout
- Mexico
- Latin America
website: https://www.kueski.com/
---
