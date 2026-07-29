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
api_count: 1
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH v2.0) endpoint for Oxford's institutional open-access repository (theses, datasets, and journal articles). Supports verbs such as Ide
  name: ORA — Oxford University Research Archive API
  slug: ora
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-oxford-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ox.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ox-it
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OxfordRSE
- group: operate
  title: ''
  type: Status
  url: https://status.it.ox.ac.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-oxford/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-oxford-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-oxford-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-oxford-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-oxford-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The University of Oxford (Oxford, UK; QS World 2025 #3) is a collegiate research university. Historically it ran a notable open-data and developer program via the IT Services Open Data Service (data.ox.ac.uk) and the Mobile Oxford platform, exposing OxPoints, places, courses, and vacancies via REST, SPARQL, and a JavaScript API; that service is now deprecated and its API/docs/mobile domains no longer resolve. The clearly live, documented public API today is the Bodleian Libraries'' ORA (Oxford University Research Archive) OAI-PMH metadata interface.'
finops:
- name: University Of Oxford Finops
  service_category: Education
  slug: university-of-oxford-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-oxford.png
jsonld:
- class_count: 14
  name: University Of Oxford Context
  property_count: 5
  slug: university-of-oxford-context
layout: provider
modified: '2026-06-03'
name: University of Oxford
nav: Providers
network: true
overview: 'University of Oxford publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and United Kingdom.


  The University of Oxford catalog on APIs.io includes 1 JSON-LD context.


  University of Oxford''s developer surface includes GitHub presence, status page, engineering blog, and 9 more developer resources.'
plans:
- name: University Of Oxford Plans Pricing
  plan_count: 2
  slug: university-of-oxford-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: University Of Oxford Rate Limits
  slug: university-of-oxford-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-oxford/refs/heads/main/screenshots/university-of-oxford-2026-06-20T200220.png
security:
- kind: domain-security
  name: University Of Oxford Domain Security
  slug: university-of-oxford-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-oxford
tags:
- Education
- Higher Education
- University
- Research
- United Kingdom
- Open Access
- OAI-PMH
- Repository
website: https://www.ox.ac.uk/
---
