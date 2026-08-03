---
access_model:
  confidence: high
  label: Commercial agreement · Accreditation required
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - https://agencyconnect.qantas.com/en-au/ndc/what-is-ndc
  - https://agencyconnect.qantas.com/en-au/ndc/distribution-platform-portal/register
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 9.5
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Qantas Distribution Platform (QDP) is Qantas' NDC XML API for airline retailing — shopping, offer and order creation, ticketing, ancillaries and post-booking servicing of Qantas (QF) content for t
  name: Qantas Distribution Platform NDC XML API
  slug: qantas-distribution-platform-ndc-xml-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qantas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qantas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qantas.com/
- group: start
  title: ''
  type: Portal
  url: https://agencyconnect.qantas.com/en-au
- group: docs
  title: ''
  type: Documentation
  url: https://agencyconnect.qantas.com/en-au/ndc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agencyconnect.qantas.com/en-au/standard-agency-terms-conditions
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.qantas.com/.well-known/security.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qantas
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qantas-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/qantas-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.qantas.com/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qantas-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/qantas-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qantas-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qantas-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qantas-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qantas-plans.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qantas-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/qantas-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qantasairways
- group: operate
  title: ''
  type: Support
  url: https://help.qantas.com/agencyconnect/s/topic/0TOMo000000MuMvOAK/qantas-ndc
- group: company
  title: ''
  type: Blog
  url: https://agencyconnect.qantas.com/en-au/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qantas.com/en-au/help/policies/privacy-and-security
- group: commercial
  title: ''
  type: Pricing
  url: https://agencyconnect.qantas.com/en-au/policies/fares-and-ticketing/distribution-surcharge-policy
- group: start
  title: ''
  type: SignUp
  url: https://agencyconnect.qantas.com/en-au/ndc/distribution-platform-portal/register
- group: start
  title: ''
  type: GettingStarted
  url: https://agencyconnect.qantas.com/en-au/ndc/distribution-platform-portal/knowledge-centre
- group: other
  title: ''
  type: Glossary
  url: https://agencyconnect.qantas.com/en-au/ndc/help-support/glossary
- group: company
  title: ''
  type: Partners
  url: https://agencyconnect.qantas.com/en-au/ndc/approved-technology-partners
created: '2026-07-28'
description: Qantas Airways Limited is Australia's flag carrier and, with its low-cost subsidiary Jetstar, one half of a domestic duopoly alongside Virgin Australia. In the distribution chain Qantas is the supplier of its own inventory — it sits upstream of the GDSs (Amadeus, Sabre, Travelport), the aggregators (Duffel, Travelfusion, Mystifly, Verteil, AirGateway, TPConnects, TravelSky) and the large Australian agency groups (Flight Centre, Corporate Travel Management, Webjet). Its API posture is distribution-only and fully gated. Qantas publishes no developer portal, no OpenAPI or Swagger definition, and no public consumer API; developer., developers., docs. and api.qantas.com.au do not resolve, and api.qantas.com returns 404 on every path probed. The one real API is the Qantas Distribution Platform (QDP) NDC XML API, built with Farelogix (now Accelya) and certified by IATA to NDC@Scale. It is documented in prose on Qantas Agency Connect but no endpoint, schema or specification is published;
  a technology partner must sign a Qantas Distribution Platform Access Agreement, subject to Qantas technical and commercial approval, before it is granted test-environment access, and an agency must hold IATA, ARC, TIDS or VTC accreditation. Public docs on how to get in, no public contract and no exit path.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qantas.png
layout: provider
modified: '2026-07-28'
name: Qantas
nav: Providers
network: true
overview: 'Qantas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Aviation, Airline, and Distribution.


  Qantas'' developer surface includes developer portal, documentation, changelog, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Qantas Plans
  plan_count: 4
  slug: qantas-plans
random_paper: 78
rate_limits:
- limit_count: 1
  name: Qantas Rate Limits
  slug: qantas-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 2.7
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 35.6
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Qantas Domain Security
  slug: qantas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qantas Vulnerability Disclosure
  slug: qantas-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: qantas
tags:
- Travel
- Australia
- Aviation
- Airline
- Distribution
- NDC
- Booking
- Corporate Travel
- Loyalty
website: https://www.qantas.com/
---
