---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API v3 for ecommerce logistics — orders, shipments, tracking, shipping-rate and coverage calculation, PDF/ZPL label generation, location resolution and webhook subscriptions.
  name: 99minutos API v3
  slug: 99minutos-api-v3
artifact_total: 7
asyncapis:
- description: ''
  name: 99Minutos Webhooks
  slug: 99minutos-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://99minutos.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.99minutos.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.99minutos.com/docs/tipo-de-envios
- group: docs
  title: ''
  type: APIReference
  url: https://developers.99minutos.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.99minutos.com/recipes/autenticarse-login
- group: auth
  title: ''
  type: Authentication
  url: authentication/99minutos-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/99minutos-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/99minutos-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/99minutos-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/99minutos-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/99minutos-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/99minutos-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/99minutos-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.99minutos.com/release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/99minutos-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.99minutos.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/99minutos-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/99minutos-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/99minutos-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://99minutos.com/preguntas-frecuentes
- group: company
  title: ''
  type: Blog
  url: https://99minutos.com/blog
- group: start
  title: ''
  type: Login
  url: https://auth.99minutos.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://99minutos.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://99minutos.com/politicas-de-privacidad
created: '2026-07-17'
description: 99minutos is a Latin American last-mile logistics and delivery company founded in 2014 and headquartered in Mexico City, operating across Mexico, Chile, Colombia and Peru. It provides same-day, next-day and national parcel delivery, dedicated logistics, freight, returns and fulfillment services for ecommerce merchants, plus its Punto99 pickup-point network and cash-on-delivery. Developers integrate through the 99minutos REST API v3 (OAuth2 client-credentials) to create and confirm orders, calculate shipping rates and validate coverage, generate PDF and ZPL shipping labels, track shipments and receive real-time status updates via webhooks, along with prebuilt ecommerce plugins for Shopify, WooCommerce, Magento, PrestaShop, BigCommerce, Tienda Nube, JumpSeller, Mercado Libre Flex and TikTok Shop. Backed by Prosus Ventures. This profile was enriched from 99minutos' public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/99minutos.png
layout: provider
mcp_servers:
- description: ''
  name: 99minutos-mcp.yml
  slug: 99minutos-mcpyml
modified: '2026-07-17'
name: 99minutos
nav: Providers
network: true
overview: '99minutos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Last-Mile Delivery, and Ecommerce.


  The 99minutos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  99minutos'' developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, changelog, support, and 17 more developer resources.'
random_paper: 106
rate_limits:
- limit_count: 1
  name: 99Minutos Rate Limits
  slug: 99minutos-rate-limits
score:
  band: developing
  composite: 50.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 50.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/99minutos/refs/heads/main/screenshots/99minutos-2026-07-25T181252.png
security:
- kind: authentication
  name: 99Minutos Authentication
  slug: 99minutos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: 99Minutos Domain Security
  slug: 99minutos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 99Minutos Trust Center
  slug: 99minutos-trust-center
  summary_line: ISO 27001
slug: 99minutos
tags:
- Company
- Logistics
- Shipping
- Last-Mile Delivery
- Ecommerce
- Fulfillment
- Package Tracking
- Latin America
- Parcel Delivery
- Webhooks
website: https://99minutos.com
---
