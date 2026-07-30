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
- description: 'REST API for UQ eSpace providing programmatic access to research outputs and dataset records held in the repository. UQ Library has published API documentation with executable examples describing the '
  name: UQ eSpace REST API
  slug: espace-api
- description: UQ's API platform for transactional and business data, used to integrate institutional systems. Access is not open or self-service; developers must request access via the Integration Services Team and
  name: Central Integration Platform
  slug: central-integration
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uq.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uqlibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-queensland/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.uq.edu.au/
- group: commercial
  title: ''
  type: Plans
  url: plans/uq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uq-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/uq-context.jsonld
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
- group: company
  title: ''
  type: About
  url: https://espace.library.uq.edu.au/
created: '2026-06-03'
description: 'The University of Queensland (UQ) is a public research university in Brisbane, Australia, ranked #54 in the QS World University Rankings 2025. UQ''s public developer and API footprint is concentrated in its library and research infrastructure: UQ eSpace, the institutional digital repository (built on the Fez/Fedora platform), exposes an OAI-PMH metadata harvesting endpoint and a documented REST API with executable examples. The UQ Library maintains an active public GitHub organisation (uqlibrary) with 150+ repositories. Broader institutional/transactional data access is governed through the Central Integration Platform and Data Hub, which are gated and require approval rather than offering open self-service APIs.'
finops:
- name: Uq Finops
  service_category: Education
  slug: uq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uq.png
jsonld:
- class_count: 13
  name: Uq Context
  property_count: 5
  slug: uq-context
layout: provider
modified: '2026-07-25'
name: University of Queensland
nav: Providers
network: true
overview: 'University of Queensland publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The University of Queensland catalog on APIs.io includes 1 JSON-LD context.


  University of Queensland''s developer surface includes GitHub presence and 11 more developer resources.'
plans:
- name: Uq Plans Pricing
  plan_count: 2
  slug: uq-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: Uq Rate Limits
  slug: uq-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uq/refs/heads/main/screenshots/uq-2026-06-20T200520.png
security:
- kind: domain-security
  name: Uq Domain Security
  slug: uq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uq
tags:
- Education
- Higher Education
- University
- Research
- Library
- Institutional Repository
- Open Data
- Australia
website: https://www.uq.edu.au/
---
