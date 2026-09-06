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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apparta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apparta.co
- group: commercial
  title: ''
  type: Pricing
  url: https://apparta.co/#plan
- group: start
  title: ''
  type: SignUp
  url: https://tmp.apparta.co/contactanos
- group: start
  title: ''
  type: Login
  url: https://temp.apparta.co/
- group: operate
  title: ''
  type: Support
  url: https://tmp.apparta.co/contactanos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appartaco/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/appartacol/
created: '2026-07-17'
description: Apparta is a Colombian hospitality technology company providing a reservation-management and guest-engagement platform for restaurants, bars, and dining venues across Latin America (Bogota, Medellin, Cali, Barranquilla). The SaaS product covers AI-assisted table assignment and floor-plan zoning, no-show prevention with prepayments and cancellation policies, a WhatsApp AI chatbot for automated bookings, CRM campaigns over SMS/email/WhatsApp, POS integration, branded booking pages and digital menus, and marketing connectors to Google, Google Maps, Instagram, TripAdvisor, and Facebook. Apparta is offered in tiered monthly plans (Basico, Standard, Plus) and is a portfolio company of 500 Global. No public developer API or OpenAPI surface is published as of this profiling; higher tiers expose a WhatsApp Business API integration on behalf of venues rather than a first-party Apparta API.
image: https://tmp.apparta.co/img/banners.png
layout: provider
modified: '2026-07-17'
name: Apparta
nav: Providers
network: true
overview: 'Apparta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Restaurant, Reservations, and Booking.


  Apparta''s developer surface includes pricing, signup flow, support, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 9.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apparta/refs/heads/main/screenshots/apparta-2026-07-25T200714.png
security:
- kind: domain-security
  name: Apparta Domain Security
  slug: apparta-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apparta
tags:
- Company
- Hospitality
- Restaurant
- Reservations
- Booking
- CRM
- WhatsApp
- Latin America
- Software-as-a-Service
website: https://apparta.co
---
