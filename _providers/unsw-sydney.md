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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The front-facing developer portal exposing the UNSW Enterprise API gateway, built on Microsoft Azure API Management. It provides API documentation, an interactive API explorer, and subscription manage
  name: UNSW Enterprise Developer Portal
  slug: developer-portal
- description: 'UNSWorks is the UNSW institutional research repository running DSpace 7.0. It exposes a public DSpace REST/HAL API at /server/api for programmatic discovery and retrieval of communities, collections, '
  name: UNSWorks Repository REST API (DSpace)
  slug: unsworks-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for the UNSWorks Repository, enabling bulk harvesting of research-output and thesis metadata. The Identify verb confirms repository name "UNSWorks Repository" '
  name: UNSWorks Repository OAI-PMH
  slug: unsworks-oai
- description: A community-maintained scraper and public API for UNSW's timetable site (timetable.unsw.edu.au), produced by the UNSW Software Development Society (DevSoc). It powers student projects such as Notangle
  name: UNSW Timetable API (community)
  slug: timetable-scraper
- description: A community-maintained public API for fetching degree, specialisation, and course information from the UNSW Handbook, published by the UNSW Computer Science and Engineering Society (CSESoc). This is n
  name: UNSW Handbook API (community)
  slug: handbook-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unsw-sydney-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unsw.edu.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apideveloper.unsw.edu.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/unsw/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/devsoc-unsw
- group: commercial
  title: ''
  type: Plans
  url: plans/unsw-sydney-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unsw-sydney-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unsw-sydney-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of New South Wales (UNSW Sydney) is a public research university in Sydney, Australia, ranked #35 in the QS World University Rankings 2025. UNSW operates a gated Enterprise Developer Portal built on Microsoft Azure API Management at apideveloper.unsw.edu.au, exposing internal enterprise APIs for student-data and campus-services integration to authorised developers via a request-based onboarding process. Publicly accessible programmatic surfaces include the UNSWorks institutional repository (DSpace 7.0) with a REST API and an OAI-PMH endpoint. Community-maintained APIs for the UNSW timetable and handbook are published by UNSW student societies (DevSoc and CSESoc) on GitHub.'
finops:
- name: Unsw Sydney Finops
  service_category: Education
  slug: unsw-sydney-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unsw-sydney.png
jsonld:
- class_count: 19
  name: Unsw Sydney Context
  property_count: 5
  slug: unsw-sydney-context
layout: provider
modified: '2026-06-03'
name: University of New South Wales
nav: Providers
network: true
overview: 'University of New South Wales publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Repository.


  The University of New South Wales catalog on APIs.io includes 1 JSON-LD context.


  University of New South Wales'' developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Unsw Sydney Plans Pricing
  plan_count: 2
  slug: unsw-sydney-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 1
  name: Unsw Sydney Rate Limits
  slug: unsw-sydney-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unsw-sydney/refs/heads/main/screenshots/unsw-sydney-2026-06-20T200413.png
security:
- kind: domain-security
  name: Unsw Sydney Domain Security
  slug: unsw-sydney-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unsw-sydney
tags:
- Education
- Higher Education
- University
- Research
- Open Repository
- Australia
- Sydney
website: https://www.unsw.edu.au/
---
