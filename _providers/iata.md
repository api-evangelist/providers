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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: The IATA Open API Hub aggregates airline-published APIs covering flight status, customer flight info, destinations, port lists, ticket validation, baggage claims, pet travel, and verifiable credential
  name: IATA Open API Hub
  slug: iata-open-api-hub
- description: ONE Record is IATA's standard for data sharing in air cargo, defining a single record view of shipments accessible across stakeholders via standardized APIs and a shared data model.
  name: IATA ONE Record
  slug: one-record
- description: NDC is an XML-based data transmission standard that enhances the capability of communications between airlines and travel agents, enabling rich content and personalized offers across the airline distr
  name: IATA New Distribution Capability (NDC)
  slug: ndc
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/iata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iata-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/international-air-transport-association-iata
- group: start
  title: ''
  type: Portal
  url: https://developer.iata.org/en/
- group: other
  title: ''
  type: Hub
  url: https://api.developer.iata.org/hub/
- group: company
  title: ''
  type: Website
  url: https://www.iata.org/
- group: operate
  title: ''
  type: Support
  url: https://www.iata.org/en/contact-us/
- group: build
  title: ''
  type: Code Samples
  url: https://github.com/airtechzone
- group: company
  title: ''
  type: Blog
  url: https://www.iata.org/api/rss/pressrelease
created: '2025-03-01'
description: The International Air Transport Association (IATA) is the global trade association representing and serving the airline industry. IATA sets standards for the aviation industry, promotes cooperation among airlines, and operates an Open API Hub providing access to airline-published APIs for flight status, destinations, baggage, ticket validation, cargo, digital identity, and related aviation data services.
finops:
- name: Iata Finops
  service_category: API
  slug: iata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iata.png
layout: provider
modified: '2026-04-28'
name: IATA
nav: Providers
network: true
overview: 'IATA publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Airlines, Airports, Aviation, Cargo, and Standards.


  IATA''s developer surface includes developer portal, support, engineering blog, and 6 more developer resources.'
plans:
- name: Iata Plans Pricing
  plan_count: 3
  slug: iata-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Iata Rate Limits
  slug: iata-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iata/refs/heads/main/screenshots/iata-2026-06-20T183109.png
security:
- kind: domain-security
  name: Iata Domain Security
  slug: iata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Iata Vulnerability Disclosure
  slug: iata-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: iata
tags:
- Airlines
- Airports
- Aviation
- Cargo
- Standards
- Travel
website: https://www.iata.org/
---
