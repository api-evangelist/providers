---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 3
apis:
- description: Public research information portal powered by Elsevier Pure, exposing Heriot-Watt University publications, projects, research data, activities, and researcher profiles. The portal is publicly browsabl
  name: Heriot-Watt Research Portal (Pure)
  slug: research-portal
- description: Library Discovery search across the catalogue, ebooks, journal articles, and news, delivered on the Ex Libris Alma library management platform with the Primo discovery interface. Ex Libris exposes Pri
  name: Heriot-Watt Library Discovery (Ex Libris Primo / Alma)
  slug: library-discovery
- description: Springshare LibCal service for library room bookings, events, and opening hours. LibCal offers a documented REST API behind an admin-configured OAuth client; the API surface is reachable at the instit
  name: Heriot-Watt LibCal (Springshare)
  slug: libcal
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heriot-watt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heriot-watt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hw.ac.uk/
- group: operate
  title: ''
  type: Status
  url: https://www.hwstatus.info/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/heriot-watt-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/heriot-watt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heriot-watt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/heriot-watt-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Heriot-Watt University is a public research university based in Edinburgh, Scotland, with additional campuses in the Scottish Borders, Orkney, Dubai, and Malaysia. It is ranked #257 in the QS World University Rankings 2025. Heriot-Watt''s public, machine-readable footprint centers on its Research Portal (powered by Elsevier Pure) for research outputs, projects, and expertise, and on Ex Libris Alma/Primo library Discovery and Springshare LibCal services. The university does not operate a public developer portal; programmatic interfaces such as the Pure OAI-PMH/REST API and the LibCal API exist as platform features but are gated and require credentials or institutional arrangement rather than being openly self-service.'
finops:
- name: Heriot Watt Finops
  service_category: Education
  slug: heriot-watt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heriot-watt.png
jsonld:
- class_count: 11
  name: Heriot Watt Context
  property_count: 4
  slug: heriot-watt-context
layout: provider
modified: '2026-06-03'
name: Heriot-Watt University
nav: Providers
network: true
overview: 'Heriot-Watt University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Scotland, and United Kingdom.


  The Heriot-Watt University catalog on APIs.io includes 1 JSON-LD context.


  Heriot-Watt University''s developer surface includes status page and 8 more developer resources.'
plans:
- name: Heriot Watt Plans Pricing
  plan_count: 2
  slug: heriot-watt-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Heriot Watt Rate Limits
  slug: heriot-watt-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heriot-watt/refs/heads/main/screenshots/heriot-watt-2026-06-20T182645.png
security:
- kind: domain-security
  name: Heriot Watt Domain Security
  slug: heriot-watt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Heriot Watt Vulnerability Disclosure
  slug: heriot-watt-vulnerability-disclosure
  summary_line: security.txt
slug: heriot-watt
tags:
- Education
- Higher Education
- University
- Scotland
- United Kingdom
- Research
- Library
- Open Access
website: https://www.hw.ac.uk/
---
