---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Astrology API provides comprehensive astrological data including Indian (Vedic) astrology with panchang and dosha data, Western astrology with planetary transits and synastry, daily and monthly ho
  name: Astrology API
  slug: astrology-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-astrology-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrology-api-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astrologyapi
- group: start
  title: Astrology API Website
  type: Portal
  url: https://astrologyapi.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://astrologyapi.com/docs
- group: start
  title: Sign Up
  type: Signup
  url: https://astrologyapi.com/signup
- group: commercial
  title: Pricing
  type: Pricing
  url: https://astrologyapi.com/pricing
created: '2025-01-07'
description: Astrology API (astrologyapi.com) is a powerful tool that provides developers with access to accurate and reliable astrological data. The API offers Indian (Vedic) astrology, Western astrology, horoscope predictions, tarot readings, and PDF report generation. It provides planetary positions, zodiac sign information, birth chart calculations, compatibility analysis, panchang data, moon phases, and daily/monthly horoscope predictions. The API is JSON-based with SDK support and Postman collections available for testing.
features:
- description: Vedic astrology data including birth chart basics, horoscope dosha analysis, yearly predictions (Varshaphal), daily nakshatra forecasts, and panchang (Hindu almanac) data.
  name: Indian (Vedic) Astrology
- description: Western astrology data including birth chart basics, numerology, synastry (relationship analysis), moon phases, planetary transits, and zodiac compatibility.
  name: Western Astrology
- description: Daily, weekly, and monthly horoscope predictions for all sun signs in both Western and Vedic astrology traditions.
  name: Horoscope Predictions
- description: General tarot card readings and yes/no tarot predictions for integrating tarot functionality into applications.
  name: Tarot API
- description: Generate detailed PDF horoscope reports in five types covering both Western and Indian astrology formats for end-user delivery.
  name: PDF Report Generation
finops:
- name: Astrology Api Finops
  service_category: API
  slug: astrology-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astrology-api.png
integrations:
- description: Official Postman collection available for testing Astrology API endpoints before integration.
  name: Postman Collection
- description: Language-specific SDK downloads available for easier integration with the Astrology API.
  name: SDK Downloads
layout: provider
modified: '2026-04-19'
name: Astrology API
nav: Providers
network: true
overview: 'Astrology API publishes 1 API on the [APIs.io](https://apis.io/) network: Astrology API. Tagged areas include Astrology, Horoscopes, Zodiac, Vedic Astrology, and Western Astrology.


  Astrology API''s developer surface includes developer portal, documentation, signup flow, pricing, and 2 more developer resources.'
plans:
- name: Astrology Api Plans Pricing
  plan_count: 3
  slug: astrology-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Astrology Api Rate Limits
  slug: astrology-api-rate-limits
score:
  band: thin
  composite: 26.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astrology-api/refs/heads/main/screenshots/astrology-api-2026-06-20T172511.png
security:
- kind: domain-security
  name: Astrology Api Domain Security
  slug: astrology-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: astrology-api
tags:
- Astrology
- Horoscopes
- Zodiac
- Vedic Astrology
- Western Astrology
use_cases:
- description: Developers build mobile and web astrology applications integrating daily horoscopes, birth charts, and compatibility analysis.
  name: Astrology App Development
- description: Content websites add personalized horoscope sections using the Astrology API's daily and monthly prediction endpoints.
  name: Horoscope Website Integration
- description: Astrology consultation platforms use the Vedic API for birth chart calculations and panchang data to support professional astrologers.
  name: Vedic Consultation Platforms
website: https://astrologyapi.com/
---
