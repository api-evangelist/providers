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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: Aalto's 3scale-based API gateway exposing open interfaces about Aalto and its operations, sourced from systems such as Oodi and ASIO. Access requires signing in with an Aalto account (and the develope
  name: Aalto API Gateway
  slug: api-gateway
- description: Course-data API exposed through the Aalto API Gateway, providing course and realization information from the SISU student information system. A Swagger/OpenAPI reference is published, but the rendered
  name: Open Courses API (SISU)
  slug: open-courses-sisu
- description: Open data published by Aalto University expressed as Linked Data, offering a public SPARQL query endpoint, a Linked Data browser, and downloadable datasets covering courses, publications, research pro
  name: Linked Open Aalto Data (SPARQL)
  slug: linked-open-data
- description: Aaltodoc is Aalto University's DSpace-based institutional repository of theses, articles, conference publications, and research materials. It exposes a public, OAI-PMH 2.0 endpoint (OpenAIRE compliant
  name: Aaltodoc Repository (OAI-PMH and REST)
  slug: aaltodoc-oai
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aalto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aalto.fi/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.aalto.fi/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/AaltoSciComp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/aalto-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/aalto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aalto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aalto-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Aalto University is a multidisciplinary public research university in Espoo, Finland, formed in 2010 from the merger of three institutions and ranked #113 in the QS World University Rankings 2025. Its public developer footprint is modest and mostly research- or open-data-oriented: an authentication-gated Aalto API Gateway (3scale) exposing course/student information system APIs such as the Open Courses (SISU) API, a Linked Open Aalto Data service offering a public SPARQL endpoint, and the Aaltodoc institutional repository (DSpace) with public OAI-PMH and REST access. Active open-source development is published primarily through the AaltoSciComp GitHub organization.'
finops:
- name: Aalto Finops
  service_category: Education
  slug: aalto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aalto.png
jsonld:
- class_count: 20
  name: Aalto Context
  property_count: 7
  slug: aalto-context
layout: provider
modified: '2026-06-03'
name: Aalto University
nav: Providers
network: true
overview: 'Aalto University publishes 1 API on the [APIs.io](https://apis.io/) network: Aaltodoc Repository (OAI-PMH and REST). Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Aalto University catalog on APIs.io includes 1 JSON-LD context.


  Aalto University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Aalto Plans Pricing
  plan_count: 2
  slug: aalto-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Aalto Rate Limits
  slug: aalto-rate-limits
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 45.2
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aalto/refs/heads/main/screenshots/aalto-2026-06-20T162945.png
security:
- kind: domain-security
  name: Aalto Domain Security
  slug: aalto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aalto
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Linked Data
- Finland
website: https://www.aalto.fi/en
---
