---
api_count: 1
apis:
- baseURL: https://connect.agendapro.com
  baseurl_source: declared
  description: Public REST API gateway for AgendaPro. Authenticates external developers with a per-company Bearer API key, enforces scopes and rate limits, and proxies to internal services. 28 operations across 11 r
  name: AgendaPro Connect v3 API
  slug: agendapro-connect-v3-api
artifact_total: 7
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
  title: ''
  type: LLMsTxt
  url: llms/agendapro-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/agendapro-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agendapro-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agendapro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agendapro-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agendapro-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agendapro-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agendapro-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agendapro-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agendapro-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/agendapro-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agendapro-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agendapro-domain-security.yml
- group: other
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
overview: 'AgendaPro publishes 1 API on the [APIs.io](https://apis.io/) network: Connect v3 API. Tagged areas include Appointment Scheduling, Booking, Salon Software, Spa and Wellness, and Point of Sale.


  The AgendaPro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AgendaPro''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Agendapro Plans Pricing
  plan_count: 4
  slug: agendapro-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Agendapro Rate Limits
  slug: agendapro-rate-limits
scopes:
- name: Agendapro Scopes
  scope_count: 0
  slug: agendapro-scopes
  summary_line: OAuth 2.0 · no documented scopes
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
- Point of Sale
- Clinic Management
- CRM
- Payments
- Webhooks
- Vertical SaaS
- Latin America
- SMB Software
website: https://agendapro.com/
---
