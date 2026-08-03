---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Mercadopago Agentic Access
  operation_count: 14
  slug: mercadopago-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 20
apis:
- description: Core REST API for creating and managing payments across cards, account-money, bank transfer (Pix in Brazil), boleto, and other LATAM methods. Supports capture, refund, partial refund, and status retri
  name: Mercado Pago Payments API
  slug: payments
- description: Hosted, pre-configured checkout experience. Merchants create a preference via API, then redirect the buyer to the Mercado Pago hosted page that handles UI, payment-method selection, and 3DS, returning
  name: Mercado Pago Checkout Pro
  slug: checkout-pro
- description: Composable web components ("bricks") that merchants embed in their own checkout UI - card form, wallet, payment-method picker, status screen. Lets merchants assemble a branded checkout while Mercado P
  name: Mercado Pago Checkout Bricks
  slug: checkout-bricks
- description: 'Full server-side checkout control: tokenise cards client-side, create a payment server-side, manage 3DS challenges, and handle capture and refund - all without redirecting the buyer.'
  name: Mercado Pago Checkout API
  slug: checkout-api
- description: Recurring-payment subscriptions with scheduling, plans, free trial, proration, and pause / resume / cancel. Supports both subscription plans (shared) and per-customer pre-approved schedules.
  name: Mercado Pago Subscriptions API
  slug: subscriptions
- description: No-code / low-code link generation for collecting a one-off or recurring payment via shareable URL or button - SMS, WhatsApp, email, or social channels.
  name: Mercado Pago Payment Links API
  slug: payment-links
- description: Integrates merchant systems with Mercado Pago Point card readers for in-person payments. Push an amount to a paired terminal, receive the authorization result, and reconcile via the same payment APIs.
  name: Mercado Pago Point API (POS)
  slug: point
- description: Static and dynamic QR code APIs for in-person collection, with order-linked status retrieval and webhook callbacks.
  name: Mercado Pago QR API
  slug: qr
- description: Event-driven notifications for payments, refunds, chargebacks, subscriptions, and merchant-account changes. Webhooks are signed so receivers can verify authenticity.
  name: Mercado Pago Webhooks / Notifications
  slug: webhooks
- description: Official Node.js / TypeScript SDK wrapping the Mercado Pago REST APIs for payments, preferences, subscriptions, and merchant orders.
  name: Mercado Pago Node.js SDK
  slug: sdk-node
- description: Official Python SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago Python SDK
  slug: sdk-python
- description: Official PHP SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago PHP SDK
  slug: sdk-php
- description: Official Ruby SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago Ruby SDK
  slug: sdk-ruby
- description: Official Java SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago Java SDK
  slug: sdk-java
- description: Official .NET / C# SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago .NET SDK
  slug: sdk-dotnet
- description: Command-line interface for managing Mercado Pago integrations, triggering test events, inspecting webhook deliveries, and scaffolding sample apps.
  name: Mercado Pago CLI
  slug: cli
- description: Model Context Protocol server that exposes Mercado Pago APIs as tools for AI agents and IDE assistants, enabling agent-driven payment and checkout workflows.
  name: Mercado Pago MCP Server
  slug: mcp
- description: The Payments API from Mercado Pago — 4 operation(s) for payments.
  name: Mercado Pago Payments API
  slug: mercadopago-payments-api
- description: The Preferences API from Mercado Pago — 3 operation(s) for preferences.
  name: Mercado Pago Preferences API
  slug: mercadopago-preferences-api
- description: The Subscriptions API from Mercado Pago — 3 operation(s) for subscriptions.
  name: Mercado Pago Subscriptions API
  slug: mercadopago-subscriptions-api
artifact_total: 27
collections:
- collection_type: open
  name: Mercado Pago REST API
  slug: open-mercadopago
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mercadopago-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercadopago-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mercadopago-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mercadopago.com/
- group: other
  title: ''
  type: Developers
  url: https://www.mercadopago.com.ar/developers/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.mercadopago.com.ar/developers/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.mercadopago.com.ar/developers/en/reference
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercadopago
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mercadopago
- group: company
  title: ''
  type: Blog
  url: https://www.mercadopago.com.br/developers/en/news
created: '2026-05-23'
description: Mercado Pago is the payments and financial-services arm of Mercado Libre, Latin America's largest e-commerce and fintech platform. Its developer portal at developers.mercadopago.com exposes a rich payments stack - Checkout Pro (hosted), Checkout Bricks (composable web components), Checkout API (full server-side control), Subscriptions, Payment Links, Point (in-person card reader), and QR payments - backed by REST APIs and official SDKs in Node.js, Python, PHP, Ruby, Java, .NET, plus a CLI and an MCP server for AI agents. Regional portals (.com.ar, .com.br, .com.mx, etc.) localise the docs and pricing per LATAM market.
finops:
- name: Mercadopago Finops
  service_category: API
  slug: mercadopago-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercadopago.png
layout: provider
modified: '2026-05-23'
name: Mercado Pago
nav: Providers
network: true
overview: 'Mercado Pago publishes 3 APIs on the [APIs.io](https://apis.io/) network: Payments API, Preferences API, and Subscriptions API. Tagged areas include Payments, Checkout, Subscriptions, POS, and QR.


  Mercado Pago''s developer surface includes authentication, documentation, API reference, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Mercadopago Plans Pricing
  plan_count: 1
  slug: mercadopago-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Mercadopago Rate Limits
  slug: mercadopago-rate-limits
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.3
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Mercadopago Authentication
  slug: mercadopago-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mercadopago Domain Security
  slug: mercadopago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mercadopago
tags:
- Payments
- Checkout
- Subscriptions
- POS
- QR
- SDKs
- Latin America
- Brazil
- Argentina
- Mexico
- Fintech
website: https://www.mercadopago.com/
---
