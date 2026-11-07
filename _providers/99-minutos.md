---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: 99 Minutos Agentic Access
  operation_count: 29
  slug: 99-minutos-agentic-access
  summary_line: 29 operations · 16 acting
api_count: 1
apis:
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The coverage API from 99 Minutos — 1 operation(s) for coverage.
  name: 99 Minutos Coverage API
  slug: 99-minutos-coverage-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The documents API from 99 Minutos — 2 operation(s) for documents.
  name: 99 Minutos Documents API
  slug: 99-minutos-documents-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The locations API from 99 Minutos — 3 operation(s) for locations.
  name: 99 Minutos Locations API
  slug: 99-minutos-locations-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The Orders API from 99 Minutos — 5 operation(s) for orders.
  name: 99 Minutos Orders API
  slug: 99-minutos-orders-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The shipments API from 99 Minutos — 3 operation(s) for shipments.
  name: 99 Minutos Shipments API
  slug: 99-minutos-shipments-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The shipping-rates API from 99 Minutos — 5 operation(s) for shipping-rates.
  name: 99 Minutos Shipping Rates API
  slug: 99-minutos-shipping-rates-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The super-geocoding API from 99 Minutos — 1 operation(s) for super-geocoding.
  name: 99 Minutos Super Geocoding API
  slug: 99-minutos-super-geocoding-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The webhooks API from 99 Minutos — 3 operation(s) for webhooks.
  name: 99 Minutos Webhooks API
  slug: 99-minutos-webhooks-api
- baseURL: https://delivery.99minutos.com
  baseurl_source: declared
  description: The oauth API from 99 Minutos — 1 operation(s) for oauth.
  name: 99 Minutos OAUTH API
  slug: 99-minutos-oauth-api
artifact_total: 28
asyncapis:
- description: ''
  name: 99 Minutos Webhooks
  slug: 99-minutos-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/99-minutos/capabilities/99-minutos-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/99-minutos-capability-edges.yml
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
  href: https://artifacts.apis.io/99-minutos/security/99-minutos-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/99-minutos-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/99-minutos/security/99-minutos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/99-minutos-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/99-minutos/authentication/99-minutos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/99-minutos-authentication.yml
- group: design
  href: https://artifacts.apis.io/99-minutos/conventions/99-minutos-conventions.yml
  title: ''
  type: Conventions
  url: conventions/99-minutos-conventions.yml
- group: design
  href: https://artifacts.apis.io/99-minutos/errors/99-minutos-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/99-minutos-problem-types.yml
- group: design
  href: https://artifacts.apis.io/99-minutos/lifecycle/99-minutos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/99-minutos-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/99-minutos/sandbox/99-minutos-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/99-minutos-sandbox.yml
- group: design
  href: https://artifacts.apis.io/99-minutos/asyncapi/99-minutos-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/99-minutos-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/99-minutos/mcp/99-minutos-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/99-minutos-mcp.yml
- group: agent
  href: https://artifacts.apis.io/99-minutos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/99-minutos/packages/99-minutos-packages.yml
  title: ''
  type: Packages
  url: packages/99-minutos-packages.yml
- group: design
  href: https://artifacts.apis.io/99-minutos/conformance/99-minutos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/99-minutos-conformance.yml
- group: design
  href: https://artifacts.apis.io/99-minutos/data-model/99-minutos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/99-minutos-data-model.yml
- group: other
  href: https://artifacts.apis.io/99-minutos/overlays/99-minutos-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/99-minutos-api-v3-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/99-minutos/llms/99-minutos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/99-minutos-llms.txt
- group: agent
  href: https://artifacts.apis.io/99-minutos/well-known/99-minutos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/99-minutos-well-known.yml
- group: agent
  href: https://artifacts.apis.io/99-minutos/agentic-access/99-minutos-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/99-minutos-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://99minutos.com
- group: operate
  href: https://artifacts.apis.io/99-minutos/rate-limits/99-minutos-rate-limits.yml
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
modified: '2026-08-08'
name: 99 Minutos
nav: Providers
network: true
overview: '99 Minutos publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Coverage API, Documents API, Locations API, and 6 more. Tagged areas include Company, Logistics, Last Mile Delivery, Shipping, and E-Commerce.


  The 99 Minutos catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  99 Minutos'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 26 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: 99 Minutos Rate Limits
  slug: 99-minutos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: 99 Minutos API Rules
  rule_count: 53
  severity_counts:
    error: 37
    hint: 0
    info: 8
    warn: 8
  slug: 99-minutos-rules
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 55.3
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 48.0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/99-minutos/99-minutos-2026-07-25T181252.png
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
skill_count: 3
skills:
- name: Create and track a shipment
  slug: 99-minutos-create-and-track-shipment
- name: Quote a shipping rate and check coverage
  slug: 99-minutos-quote-shipping-rate
- name: Subscribe to shipment status webhooks
  slug: 99-minutos-subscribe-webhooks
slug: 99-minutos
tags:
- Company
- Logistics
- Last Mile Delivery
- Shipping
- E-Commerce
- Fulfillment
- Freight
- Tracking
- Webhook
- Latin America
- Mexico
website: https://99minutos.com
---
