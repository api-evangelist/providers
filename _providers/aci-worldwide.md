---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: The core RESTful payment API of the ACI Open Payment Platform (PAY.ON gateway). Server-to-Server integration lets merchants and PSPs run end-to-end payment workflows — preauthorization, debit, capture
  name: ACI Open Payment Platform — Server-to-Server API
  slug: open-payment-platform-server-to-server
- description: COPYandPAY is ACI's secure, PCI-friendly embedded payments widget for merchants and integrators. It renders a hosted card and alternative-payment form that tokenizes and submits sensitive data directl
  name: ACI COPYandPAY
  slug: copyandpay
- description: BackOffice operations on the Open Payment Platform let integrators process and manage previously authorized transactions — captures, refunds, reversals, and related post-authorization actions — via th
  name: ACI BackOffice API
  slug: backoffice
- description: Pay By Link lets merchants create secure, customizable hosted payment link pages and collect payments without a full checkout integration, built on the Open Payment Platform gateway.
  name: ACI Pay By Link API
  slug: pay-by-link
- description: The ACI Mobile SDK lets developers accept payments inside native mobile apps, wrapping the Open Payment Platform's card and alternative-payment flows with device-side tokenization and 3-D Secure suppo
  name: ACI Mobile SDK
  slug: mobile-sdk
artifact_total: 8
asyncapis:
- description: ''
  name: Aci Worldwide Webhooks
  slug: aci-worldwide-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aci-worldwide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aciworldwide.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aciworldwide.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aciworldwide.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aciworldwide.com/reference/parameters
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aciworldwide.com/integrations/widget
- group: operate
  title: ''
  type: Support
  url: https://docs.aciworldwide.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.aciworldwide.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aciworldwide.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aciworldwide.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/aci-worldwide-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aci-worldwide-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aci-worldwide-result-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/aci-worldwide-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aci-worldwide-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aci-worldwide-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aciworldwide.com/reference/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aci-worldwide-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aci-worldwide-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/aci-worldwide-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aci-worldwide-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/aci-worldwide-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/aci-worldwide-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aci-worldwide-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aci-worldwide-llms.txt
created: '2026-07-24'
description: 'ACI Worldwide (NASDAQ: ACIW) is a US-headquartered payment-software company that builds real-time payment, card, merchant/eCommerce, and bill-payment technology for banks, processors, merchants, and billers around the world. Its enterprise portfolio spans BASE24 card and ATM switching, the ACI Enterprise Payments Platform for real-time and ISO 20022 account-to-account rails, and ACI Speedpay bill payment — most of which ship as licensed, on-premise or hosted software rather than public self-serve APIs. ACI''s genuinely API-native surface is the ACI Open Payment Platform (the PAY.ON global payment gateway): a unified RESTful API documented at docs.aciworldwide.com that lets merchants and PSPs accept and manage card and alternative-payment transactions through Server-to-Server, COPYandPAY, Mobile SDK, BackOffice, and Pay By Link integrations, authenticated with an Authorization Bearer access token plus a channel entityId and complemented by PAYMENT and REGISTRATION webhook notifications.
  Its home market is the United States, inside the deep, fragmented, API-native US payments landscape.'
image: https://www.aciworldwide.com/wp-content/uploads/2021/05/cropped-android-chrome-512x512-1-192x192.png
layout: provider
modified: '2026-07-24'
name: ACI Worldwide
nav: Providers
network: true
overview: 'ACI Worldwide publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United States, Payment Gateway, Payment Processing, and Acquiring.


  The ACI Worldwide catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ACI Worldwide''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 18 more developer resources.'
random_paper: 47
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 49.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aci-worldwide/refs/heads/main/screenshots/aci-worldwide-2026-07-25T181458.png
security:
- kind: authentication
  name: Aci Worldwide Authentication
  slug: aci-worldwide-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Aci Worldwide Domain Security
  slug: aci-worldwide-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aci-worldwide
tags:
- Payments
- United States
- Payment Gateway
- Payment Processing
- Acquiring
- Card Payments
- eCommerce
- Fraud
- Tokenization
- 3D Secure
- Bill Payment
- Real-Time Payments
- ISO 20022
website: https://www.aciworldwide.com/
---
