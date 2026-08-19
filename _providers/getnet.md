---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
api_count: 19
apis:
- description: Getnet's core REST API and Single Entry Point (SEP) for direct payment integration across Argentina, Brazil, Chile, Colombia, Mexico, Portugal, Spain, and Uruguay. One contract gives merchants omnicha
  name: Getnet Regional API (Single Entry Point)
  slug: getnet-regional-api
- description: 'Plug-and-play hosted payment surface that reduces PCI scope. Available in three integration modes: embedded iframe, lightbox pop-up, and redirect to a Getnet-hosted page. Supports credit card, debit, '
  name: Getnet Web Checkout
  slug: getnet-web-checkout
- description: 'Payment processing for multi-seller platforms: sub-seller onboarding, card capture (Visa, Mastercard, Elo, Amex, Hipercard), programmable payment splits with commission rules, receivables management, '
  name: Getnet Marketplace API
  slug: getnet-marketplace-api
- description: Programmatically generate shareable payment links so Brazilian merchants can sell without a website or virtual store. Used to distribute checkout via WhatsApp, email, SMS, and social channels, with fu
  name: Getnet Payment Link API (BR)
  slug: getnet-payment-link-api
- description: 100%-online self-accreditation API for new Getnet Brasil merchants. Covers the offer showcase (GET /v1/offerings, pricing, priced offers), establishment registration (POST/PUT /merchants, qualificatio
  name: Getnet Onboarding API (BR)
  slug: getnet-onboarding-api
- description: Dispute management API for listing, viewing, contesting, accepting, and documenting chargebacks. Three actor roles (Merchant, Platform, Auditor) with OAuth 2.0 Bearer tokens, one-hour token TTL, and s
  name: Getnet Chargeback API
  slug: getnet-chargeback-api
- description: Standardized merchant report retrieval API that simplifies multi-country reconciliation. Surfaces capture, settlement, and adjustment data sets aligned to a unified schema across Getnet markets.
  name: Getnet Merchant Reporting API
  slug: getnet-merchant-reporting-api
- description: Inter-app integration that lets a merchant's mobile or terminal app hand off a transaction to the Getnet payment app on the same device, then receive the signed result back. Covers the Get Smart and S
  name: Getnet App2App In-Store Integration
  slug: getnet-app2app
- description: Direct host-to-host terminal connectivity for back-of-house systems (PDV, ERP, automation gateways) that originate and capture transactions through Getnet terminals without the operator interacting wi
  name: Getnet Host-to-Host Terminal Integration
  slug: getnet-host-to-host
- description: POS-system integration model where the Getnet terminal is driven from a merchant point-of-sale or PDV stack. Includes capture, cancellation, reprint, totals, settlement, and consolidated lifecycle hoo
  name: Getnet Integrated POS
  slug: getnet-integrated-pos
- description: Cloud-mediated terminal command and event delivery so a remote merchant system can drive a Getnet POS terminal without on-prem middleware. Designed for omnichannel use cases that blend in-store and re
  name: Getnet Cloud-to-Cloud
  slug: getnet-cloud-to-cloud
- description: Payment surface designed for autonomous AI agents acting as the buying party in a commerce interaction. Provides agent-friendly payment intent, authorization, and capture flows aligned with Getnet's R
  name: Getnet Agentic Commerce
  slug: getnet-agentic-commerce
- description: Model Context Protocol toolkit that exposes Getnet payment operations to AI assistants such as ChatGPT, Claude, and Gemini, so an LLM-driven agent can quote, charge, refund, and inspect transactions t
  name: Getnet MCP AI Toolkit
  slug: getnet-mcp-ai-toolkit
- description: OAuth 2.0 client-credentials token endpoint used to mint bearer access tokens for Getnet APIs. Tokens are short-lived (one hour for chargeback) and must be refreshed before passing in the Authorizatio
  name: Getnet OAuth 2.0 Token API
  slug: getnet-oauth2-token-api
- description: 'Idempotency endpoint set for the legacy Plataforma Digital that lets merchants pre-register and replay request keys so retries do not result in duplicate charges or duplicate split allocations. Being '
  name: Getnet Idempotency API
  slug: getnet-idempotency-api
- description: Canais Digitais surface inside the legacy Brazilian Plataforma Digital that powers merchant-facing self-service flows and internal digital channel automations. Being migrated to docs.globalgetnet.com.
  name: Getnet Canais Digitais API
  slug: getnet-canais-digitais
- description: SAP-integrated white-label APIs covering inventory management, service order closure, evidence upload, and event webhooks for Getnet's immediate-delivery (entrega imediata) terminal logistics flow.
  name: Getnet SAP Immediate Delivery APIs
  slug: getnet-sap-immediate-delivery
- description: White-label merchant operations APIs covering terminal paper-roll ordering and merchant fee viewing and negotiation surfaces that partners can embed in their own back-office.
  name: Getnet White Label Merchant Operations
  slug: getnet-white-label-ops
- description: Spain-specific Get Smart App2App terminal-integration model for the local processor footprint, with Bizum and Spanish card-scheme support.
  name: Getnet Get Smart App2App (Spain)
  slug: getnet-local-processor-spain
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getnet-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.globalgetnet.com/en
- group: auth
  title: ''
  type: Authentication
  url: https://docs.globalgetnet.com/en/products/online-payments/regional-api?doc=first-step-authentication
- group: operate
  title: ''
  type: FAQ
  url: https://site.getnet.com.br/duvidas/
- group: commercial
  title: ''
  type: Pricing
  url: https://site.getnet.com.br/taxas/
- group: start
  title: ''
  type: Sandbox
  url: https://api-homologacao.getnet.com.br/api-doc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Getnet-Brasil
created: '2026-05-25'
description: Getnet is a leading merchant acquirer in Latin America and a payments subsidiary of Banco Santander, operating across Brazil, Argentina, Chile, Colombia, Mexico, Uruguay, Spain, and Portugal. Getnet is positioned as the region's second-largest acquirer by transaction volume and powers card processing, alternative payment methods, gateway, anti-fraud, tokenization, installments, marketplaces, and POS for over a million merchants. Its API ecosystem is now consolidated under the global Getnet Docs portal (docs.globalgetnet.com) with a Single Entry Point (SEP) Regional API alongside Web Checkout, Marketplace, Payment Link, Chargeback, Onboarding, in-store terminal integrations (App2App, Host-to-Host, Integrated POS, Cloud-to-Cloud), and an emerging Agentic Commerce / MCP AI Toolkit surface for AI-driven payments. The Brazilian developer hub at developers.getnet.com.br is being migrated to the unified global portal.
image: https://site.getnet.com.br/wp-content/themes/getnet/dist/img/logo-getnet.svg
layout: provider
modified: '2026-05-25'
name: Getnet
nav: Providers
network: true
overview: 'Getnet publishes 1 API on the [APIs.io](https://apis.io/) network: SAP Immediate Delivery APIs. Tagged areas include Payments, Acquirer, Brazil, LATAM, and Santander.


  Getnet''s developer surface includes documentation, authentication, FAQ, pricing, sandbox, and 2 more developer resources.'
random_paper: 51
score:
  band: emerging
  composite: 25.1
  delta: -1.8
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 26.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getnet/refs/heads/main/screenshots/getnet-2026-06-20T181816.png
security:
- kind: domain-security
  name: Getnet Domain Security
  slug: getnet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getnet
tags:
- Payments
- Acquirer
- Brazil
- LATAM
- Santander
- E-Commerce
- In-Store Payments
- POS
- Pix
- Boleto
- Cards
- 3DS
- Tokenization
- Marketplace
- Split Payments
- Payment Link
- Web Checkout
- Onboarding
- Chargeback
- Webhooks
- OAuth 2.0
- Agentic Commerce
- MCP
---
