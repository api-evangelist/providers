---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-09-16'
api_count: 2
apis:
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Query available booking slots for a service at a location
  name: AgendaPro Available Slots API
  slug: agendapro-available-slots-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Booking management (list, show, create, update, cancel)
  name: AgendaPro Bookings API
  slug: agendapro-bookings-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Shopping carts for the online payment flow
  name: AgendaPro Carts API
  slug: agendapro-carts-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Client management (list, show, create, update) and custom attributes
  name: AgendaPro Clients API
  slug: agendapro-clients-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Custom attribute templates (company-level definitions)
  name: AgendaPro Custom Attributes API
  slug: agendapro-custom-attributes-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Location listing and details
  name: AgendaPro Locations API
  slug: agendapro-locations-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Online payment requests (checkout URL) on a cart
  name: AgendaPro Payment Requests API
  slug: agendapro-payment-requests-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Service provider listing and details
  name: AgendaPro Providers API
  slug: agendapro-providers-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Sales records (read-only)
  name: AgendaPro Sales API
  slug: agendapro-sales-api
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Service catalog listing and details
  name: AgendaPro Services API
  slug: agendapro-services-api
artifact_total: 16
asyncapis:
- description: ''
  name: Agendapro Webhooks
  slug: agendapro-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://agendapro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.agendapro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.agendapro.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.agendapro.com/reference/getting-started-v3
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.agendapro.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://ayuda.agendapro.com/
- group: company
  title: ''
  type: Blog
  url: https://agendapro.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://agendapro.com/en/planes
- group: start
  title: ''
  type: SignUp
  url: https://agendapro.com/lead/registro
- group: start
  title: ''
  type: Login
  url: https://app.agendapro.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agendapro.com/en/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agendapro.com/en/politica-de-privacidad
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agendapro.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agendapro
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/llms/agendapro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agendapro-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/authentication/agendapro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agendapro-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/scopes/agendapro-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agendapro-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/conventions/agendapro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agendapro-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/errors/agendapro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agendapro-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/data-model/agendapro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agendapro-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/lifecycle/agendapro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agendapro-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/conformance/agendapro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agendapro-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/rate-limits/agendapro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agendapro-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/plans/agendapro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agendapro-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/packages/agendapro-packages.yml
  title: ''
  type: Packages
  url: packages/agendapro-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/asyncapi/agendapro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agendapro-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/security/agendapro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agendapro-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agendapro/refs/heads/main/overlays/agendapro-connect-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agendapro-connect-v3-overlay.yaml
created: '2026-09-12'
description: AgendaPro is a Latin American vertical SaaS platform for appointment-based service businesses — salons, barbershops, spas, aesthetic and medical clinics, gyms, veterinarians and wellness studios — combining online booking, calendar and staff scheduling, client CRM and treatment records, point of sale, inventory, commissions, marketing campaigns and WhatsApp/SMS/email reminders, plus online payments and gift cards. Founded in Chile and operating across Chile, Mexico, Colombia, Peru, Argentina, Brazil and Spain, it serves multi-location merchants from a single account. Its public developer surface is the Connect v3 API, an OpenAPI 3.0.3-described REST gateway at connect.agendapro.com that exposes bookings, availability slots, clients, custom attributes, locations, services, categories, service providers, sales, carts and online payment requests, with Bearer API-key auth, scoped keys, per-minute and per-day rate limiting, and HMAC-signed webhooks. API access requires an active
  Pro plan.
image: https://files.readme.io/6f50a41-small-Recurso_12x.png
layout: provider
modified: '2026-09-12'
name: AgendaPro
nav: Providers
network: true
overview: 'AgendaPro publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Available Slots API, Bookings API, Carts API, and 7 more. Tagged areas include Appointment Scheduling, Booking, Salon Software, Spa and Wellness, and Point-of-Sale.


  The AgendaPro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AgendaPro''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Agendapro Plans Pricing
  plan_count: 4
  slug: agendapro-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Agendapro Rate Limits
  slug: agendapro-rate-limits
scopes:
- name: Agendapro Scopes
  scope_count: 0
  slug: agendapro-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 59.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agendapro Authentication
  slug: agendapro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agendapro Domain Security
  slug: agendapro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agendapro
tags:
- Appointment Scheduling
- Booking
- Salon Software
- Spa and Wellness
- Point-of-Sale
- Clinic Management
- CRM
- Payments
- Webhook
- Vertical SaaS
- Latin America
- SMB Software
website: https://agendapro.com/
---
