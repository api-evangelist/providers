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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: 99 Minutos Agentic Access
  operation_count: 29
  slug: 99-minutos-agentic-access
  summary_line: 29 operations · 16 acting
api_count: 9
apis:
- description: The coverage API from 99 Minutos — 1 operation(s) for coverage.
  name: 99 Minutos coverage API
  slug: 99-minutos-coverage-api
- description: The documents API from 99 Minutos — 2 operation(s) for documents.
  name: 99 Minutos documents API
  slug: 99-minutos-documents-api
- description: The locations API from 99 Minutos — 3 operation(s) for locations.
  name: 99 Minutos locations API
  slug: 99-minutos-locations-api
- description: The oauth API from 99 Minutos — 1 operation(s) for oauth.
  name: 99 Minutos oauth API
  slug: 99-minutos-oauth-api
- description: The Orders API from 99 Minutos — 5 operation(s) for orders.
  name: 99 Minutos Orders API
  slug: 99-minutos-orders-api
- description: The shipments API from 99 Minutos — 3 operation(s) for shipments.
  name: 99 Minutos shipments API
  slug: 99-minutos-shipments-api
- description: The shipping-rates API from 99 Minutos — 5 operation(s) for shipping-rates.
  name: 99 Minutos shipping-rates API
  slug: 99-minutos-shipping-rates-api
- description: The super-geocoding API from 99 Minutos — 1 operation(s) for super-geocoding.
  name: 99 Minutos super-geocoding API
  slug: 99-minutos-super-geocoding-api
- description: The webhooks API from 99 Minutos — 3 operation(s) for webhooks.
  name: 99 Minutos webhooks API
  slug: 99-minutos-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: 99 Minutos Webhooks
  slug: 99-minutos-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Version 3 coverage API
  slug: open-99-minutos-coverage-api
- collection_type: open
  name: API Version 3 coverage documents API
  slug: open-99-minutos-documents-api
- collection_type: open
  name: API Version 3 coverage locations API
  slug: open-99-minutos-locations-api
- collection_type: open
  name: API Version 3 coverage oauth API
  slug: open-99-minutos-oauth-api
- collection_type: open
  name: API Version 3 coverage Orders API
  slug: open-99-minutos-orders-api
- collection_type: open
  name: API Version 3 coverage shipments API
  slug: open-99-minutos-shipments-api
- collection_type: open
  name: API Version 3 coverage shipping-rates API
  slug: open-99-minutos-shipping-rates-api
- collection_type: open
  name: API Version 3 coverage super-geocoding API
  slug: open-99-minutos-super-geocoding-api
- collection_type: open
  name: API Version 3 coverage webhooks API
  slug: open-99-minutos-webhooks-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.99minutos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.99minutos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.99minutos.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.99minutos.com/recipes/autenticarse-login
- group: operate
  title: ''
  type: Support
  url: https://www.99minutos.com/preguntas-frecuentes/
- group: company
  title: ''
  type: Blog
  url: https://www.99minutos.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/99minutos
- group: start
  title: ''
  type: SignUp
  url: https://envios.99minutos.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.99minutos.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.99minutos.com/politicas-de-privacidad
- group: auth
  title: ''
  type: Compliance
  url: https://security.99minutos.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/99-minutos-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/99-minutos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/99-minutos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/99-minutos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/99-minutos-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/99-minutos-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/99-minutos-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/99-minutos-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/99-minutos-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/99-minutos-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/99-minutos-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/99-minutos-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/99-minutos-api-v3-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/99-minutos-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/99-minutos-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/99-minutos-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://99minutos.com
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/99-minutos-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.99minutos.com/release-notes
- group: start
  title: ''
  type: Login
  url: https://auth.99minutos.com/
created: '2026-07-17'
description: 99minutos (99 Minutos) is a Latin American last-mile logistics and delivery platform serving ecommerce businesses across Mexico, Chile, Colombia and Peru. It offers express parcel delivery (envios99), full-truck-load and drayage freight (freight99), fulfillment and warehousing (fulfill99) and custom logistics operations (tailor99), backed by a network of pickup/delivery points (Punto99). Its public REST API v3 lets developers resolve addresses to reusable location ids, quote shipping rates and coverage, create/confirm orders (including multibox), print PDF and ZPL labels, track shipments and subscribe to real-time status webhooks. Authentication is OAuth2 client-credentials that returns a bearer JWT. Surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline from the provider's own developer portal.
image: https://www.99minutos.com/_next/static/media/logo_99minutos.230a642b.svg
layout: provider
mcp_servers:
- description: ''
  name: 99-minutos-mcp.yml
  slug: 99-minutos-mcpyml
modified: '2026-08-08'
name: 99 Minutos
nav: Providers
network: true
overview: '99 Minutos publishes 9 APIs on the [APIs.io](https://apis.io/) network, including coverage API, documents API, locations API, and 6 more. Tagged areas include Company, Logistics, Last Mile Delivery, Shipping, and Ecommerce.


  The 99 Minutos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  99 Minutos'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 48
rate_limits:
- limit_count: 1
  name: 99 Minutos Rate Limits
  slug: 99-minutos-rate-limits
score:
  band: developing
  composite: 48.2
  delta: -5.6
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/99-minutos/refs/heads/main/screenshots/99-minutos-2026-07-25T181252.png
security:
- kind: authentication
  name: 99 Minutos Authentication
  slug: 99-minutos-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 99 Minutos Domain Security
  slug: 99-minutos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 99 Minutos Trust Center
  slug: 99-minutos-trust-center
  summary_line: ISO 27001
slug: 99-minutos
tags:
- Company
- Logistics
- Last Mile Delivery
- Shipping
- Ecommerce
- Fulfillment
- Freight
- Tracking
- Webhooks
- Latin America
- Mexico
website: https://99minutos.com
---
