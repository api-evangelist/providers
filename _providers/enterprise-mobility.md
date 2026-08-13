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
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: The Rental business line of the EHI API Marketplace, covering Enterprise Rent-A-Car's network of neighborhood and airport branches. The public overview page describes the capabilities as vehicle renta
  name: EHI Rental APIs
  slug: ehi-rental-apis
- description: The Replacement Rental business line of the EHI API Marketplace, exposing the ARMS (Automated Rental Management System) and Entegral platforms to insurance providers, collision repair shops, dealershi
  name: EHI Replacement Rental APIs
  slug: ehi-replacement-rental-apis
- description: The Commute business line of the EHI API Marketplace, covering Commute with Enterprise vanpooling and rideshare-to-work programs sold to employers. The public overview page describes the capability as
  name: EHI Commute APIs
  slug: ehi-commute-apis
- description: The backend-for-frontend that powers the EHI API Marketplace itself, and the only Enterprise Mobility API surface with endpoints published anonymously. Three POST operations are declared verbatim in t
  name: EHI API Marketplace Experience API
  slug: ehi-marketplace-experience-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enterprise-mobility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enterprisemobility.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.ehi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ehi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ehi.com/apis-overview.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/enterprise-mobility-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/enterprise-mobility-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enterprise-mobility-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/enterprise-mobility-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/enterprise-mobility-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enterprise-mobility-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enterprise-mobility-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enterprise-mobility-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enterprise-mobility-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enterprise-mobility-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ehi.com/general/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.ehi.com/general/privacy-policy.html
- group: operate
  title: ''
  type: Contact
  url: https://developer.ehi.com/general/contact-us.html
- group: operate
  title: ''
  type: Support
  url: https://developer.ehi.com/general/contact-us.html
- group: company
  title: ''
  type: Blog
  url: https://www.enterprisemobility.com/en/news-stories.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enterprise-mobility
created: '2026-07-28'
description: 'Enterprise Mobility is the Clayton, Missouri parent of Enterprise Rent-A-Car, National Car Rental and Alamo Rent a Car, and the largest car rental provider in the world — 90,000+ team members, 9,500+ rental branches across more than 90 countries and territories, a global fleet of over 2.4 million vehicles and $39 billion in 2025 fiscal-year revenue. Beyond leisure and corporate car rental it operates fleet management, flexible vehicle hire, carsharing, vanpooling, truck rental, car sales, vehicle subscription and the ARMS / Entegral replacement-rental technology used by insurers, collision repairers and dealerships. In the United States travel distribution chain it is a ground-transportation supplier whose inventory reaches buyers through GDS and OTA intermediaries, corporate travel programs and its own direct brand sites, rather than through any published public booking API. Its API posture is partner-gated and honestly so: EHI runs a real API Marketplace at developer.ehi.com
  with public marketing overviews for three business lines — Rental, Replacement Rental and Commute — but the API catalog, API specs, guides and release notes all sit behind Azure AD B2C sign-in and the portal states access is for "an Enterprise employee or trusted Partner" who should "contact your account manager ... to request access". No OpenAPI is published for those business lines; probes of /openapi.json, /swagger.json, /api-docs and /.well-known/ return AEM soft-404 HTML or 404. What is public is the plumbing around the gate: the production API gateway at api.ehi.com is a live Kong Gateway behind Imperva, the marketplace''s own experience API publishes three POST endpoints in the portal''s anonymous page source, the Azure AD B2C tenant serves two readable OpenID Connect discovery documents, and the sign-in link enumerates fourteen OAuth scopes covering catalog search, client-application registration and authorization requests. The published API License Agreement grants only a "limited,
  revocable, non-transferable, non-sublicensable, non-exclusive" right, restricts use to the licensee''s internal purpose, states the licensee has no ownership rights in Renter Information, and on termination requires the licensee to "delete or return any copies of the APIs and Enterprise Content" — public docs shell, gated specs, no exit path.'
image: https://www.enterprisemobility.com/content/dam/enterpriseholdings/functional/logos/png/em-og-image-default.png
layout: provider
modified: '2026-07-28'
name: Enterprise Mobility
nav: Providers
network: true
overview: 'Enterprise Mobility publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United States, Car Rental, Ground Transportation, and Mobility.


  Enterprise Mobility''s developer surface includes developer portal, documentation, authentication, support, engineering blog, and 16 more developer resources.'
random_paper: 87
scopes:
- name: Enterprise Mobility Scopes
  scope_count: 14
  slug: enterprise-mobility-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 27.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 27.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enterprise-mobility/refs/heads/main/screenshots/enterprise-mobility-2026-08-07T164933.png
security:
- kind: authentication
  name: Enterprise Mobility Authentication
  slug: enterprise-mobility-authentication
  summary_line: openIdConnect/oauth2/http · 3 schemes
- kind: domain-security
  name: Enterprise Mobility Domain Security
  slug: enterprise-mobility-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enterprise Mobility Vulnerability Disclosure
  slug: enterprise-mobility-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: enterprise-mobility
tags:
- Travel
- United States
- Car Rental
- Ground Transportation
- Mobility
- Corporate Travel
- Distribution
- Fleet Management
- Insurance Replacement Rental
- Booking
website: https://www.enterprisemobility.com/
---
