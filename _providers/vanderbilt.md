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
api_count: 2
apis:
- description: 'Azure API Management developer portal operated by Vanderbilt IT (VUIT) where authorized users can discover APIs, learn how to use them, try them interactively, and sign up to acquire keys. The portal '
  name: Vanderbilt API Management Developer Portal
  slug: apim-portal
- description: Vanderbilt IT Cloud Services builds integrations with third-party systems via web-based APIs and develops custom HTTP REST APIs running from Vanderbilt public or private cloud. This is a staff/faculty
  name: Vanderbilt IT API Services
  slug: vuit-api-services
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vanderbilt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vanderbilt.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/vanderbiltu
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/heardlibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/vanderbilt-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apim-portal.app.vanderbilt.edu/
- group: commercial
  title: ''
  type: Plans
  url: plans/vanderbilt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vanderbilt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vanderbilt-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vanderbilt-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'Vanderbilt University is a private research university in Nashville, Tennessee, ranked #248 in the QS World University Rankings 2025. Its public developer/API footprint is limited and largely gated: Vanderbilt IT (VUIT) offers API integration and management services to faculty and staff, fronted by an Azure API Management developer portal that does not resolve for the general public (internal/network-gated). The Jean and Alexander Heard Libraries maintain an open GitHub presence (linked data, semantic web, institutional repository tooling) and run an Ex Libris Alma/Primo library platform that supports standard OAI-PMH and discovery APIs. No official, publicly documented, self-service Vanderbilt API was confirmed during review.'
finops:
- name: Vanderbilt Finops
  service_category: Education
  slug: vanderbilt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vanderbilt.png
jsonld:
- class_count: 10
  name: Vanderbilt Context
  property_count: 4
  slug: vanderbilt-context
layout: provider
modified: '2026-06-03'
name: Vanderbilt University
nav: Providers
network: true
overview: 'Vanderbilt University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Nashville.


  The Vanderbilt University catalog on APIs.io includes 1 JSON-LD context.


  Vanderbilt University''s developer surface includes GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Vanderbilt Plans Pricing
  plan_count: 2
  slug: vanderbilt-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: Vanderbilt Rate Limits
  slug: vanderbilt-rate-limits
score:
  band: emerging
  composite: 20.5
  delta: -2.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vanderbilt/refs/heads/main/screenshots/vanderbilt-2026-06-20T200807.png
security:
- kind: domain-security
  name: Vanderbilt Domain Security
  slug: vanderbilt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vanderbilt
tags:
- Education
- Higher Education
- University
- Research
- Nashville
- Tennessee
- United States
website: https://www.vanderbilt.edu/
---
