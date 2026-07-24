---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 8
apis:
- description: Consumer-facing web application for conversational AI trip planning, itinerary building, collaboration, and booking of flights, hotels, restaurants, experiences, and events.
  name: Mindtrip Web Application
  slug: web
- description: Agentic AI flight discovery, booking, and payments experience launched in May 2026, powered by Sabre's travel content APIs and PayPal's payments API.
  name: Mindtrip Flights
  slug: flights
- description: In-app hotel discovery and booking experience using partner travel content for rates, availability, and reservations.
  name: Mindtrip Hotels
  slug: hotels
- description: In-app restaurant discovery and reservation experience.
  name: Mindtrip Restaurants
  slug: restaurants
- description: In-app booking for activities, experiences, concerts, comedy shows, farmers' markets, and family events.
  name: Mindtrip Experiences and Events
  slug: experiences-events
- description: Program that pays travel creators for sharing recommendations and itineraries on the Mindtrip platform.
  name: Mindtrip Creator Program
  slug: creator-program
- description: Partnerships and integrations for destinations, DMOs, hotels, and travel suppliers to reach Mindtrip travelers; the primary B2B surface and the channel for partner API conversations.
  name: Mindtrip for Business
  slug: business
- description: Inbound integrations Mindtrip consumes for travel content and payments, including Sabre (Mosaic platform, flight and lodging APIs), PayPal (payments), Ripe ITA Platform, and GuideGeek. No general-purp
  name: Mindtrip Partner Integrations
  slug: partner-integrations
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mindtrip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindtrip-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mindtrip-ai
- group: company
  title: ''
  type: Website
  url: https://mindtrip.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://mindtrip.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mindtrip-ai
- group: commercial
  title: ''
  type: Plans
  url: plans/mindtrip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mindtrip-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mindtrip-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://mindtrip.ai/
- group: company
  title: Mindtrip Flights Launch (May 2026)
  type: Press
  url: https://www.prnewswire.com/news-releases/mindtrip-launches-travels-first-all-in-one-agentic-ai-flight-booking-experience-powered-by-partnership-with-sabre-and-paypal-302763838.html
created: '2026-05-23'
description: Mindtrip is an AI-powered travel planning platform that lets travelers discover destinations, build itineraries, and book flights, hotels, restaurants, experiences, and events through a conversational interface and collaborative trip workspace. Mindtrip Flights launched in May 2026 as the industry's first end-to-end agentic AI flight booking experience, powered by partnership with Sabre (travel content / GDS APIs) and PayPal (payments). Mindtrip is primarily a consumer product; it does not currently expose a general-purpose public REST API, but participates in partner integrations (Sabre Mosaic, PayPal, Ripe ITA, GuideGeek) and runs a Creator and Business program for destinations and hotels.
finops:
- name: Mindtrip Finops
  service_category: Travel
  slug: mindtrip-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindtrip.png
layout: provider
modified: '2026-06-02'
name: Mindtrip
nav: Providers
network: true
overview: 'Mindtrip publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, AI, Agentic AI, Itinerary Planning, and Booking.


  Mindtrip''s developer surface includes documentation, GitHub presence, pricing, and 8 more developer resources.'
plans:
- name: Mindtrip Plans Pricing
  plan_count: 3
  slug: mindtrip-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Mindtrip Rate Limits
  slug: mindtrip-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Mindtrip Domain Security
  slug: mindtrip-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mindtrip Vulnerability Disclosure
  slug: mindtrip-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mindtrip
tags:
- Travel
- AI
- Agentic AI
- Itinerary Planning
- Booking
- Consumer
website: https://mindtrip.ai/
---
