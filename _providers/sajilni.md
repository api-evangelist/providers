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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sajilni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sajilni.com
- group: start
  title: ''
  type: Portal
  url: https://business.sajilni.com
- group: commercial
  title: ''
  type: Pricing
  url: https://business.sajilni.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://business.sajilni.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.sajilni.com/user/login.html
- group: operate
  title: ''
  type: Support
  url: https://business.sajilni.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://business.sajilni.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://business.sajilni.com/privacy-policy/
created: '2026-07-17'
description: Sajilni is a Middle East / MENA event ticketing and event-management platform built for organizers who care about data and branding. Organizers use it to create events, design branded registration pages, sell and scan tickets, manage seating and booths, run promo/discount codes, collect payments, and analyze attendee data. The consumer-facing site is sajilni.com with an organizer/business portal at business.sajilni.com; the platform is a Java/Spring web application with an internal authentication service at auth.sajilni.com. As of this enrichment pass Sajilni publishes no public API, developer portal, OpenAPI, or webhook surface, so this profile captures the company identity, commercial pages, and a live domain-security probe rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sajilni.png
layout: provider
modified: '2026-07-21'
name: Sajilni
nav: Providers
network: true
overview: 'Sajilni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Events, Event Management, Ticketing, and Event Registration.


  Sajilni''s developer surface includes developer portal, pricing, signup flow, support, and 5 more developer resources.'
random_paper: 32
score:
  band: emerging
  composite: 20.1
  delta: 1.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Sajilni Domain Security
  slug: sajilni-domain-security
  summary_line: TLSv1.2 · DMARC
slug: sajilni
tags:
- Company
- Events
- Event Management
- Ticketing
- Event Registration
- Payments
- MENA
- Middle East
website: https://sajilni.com
---
