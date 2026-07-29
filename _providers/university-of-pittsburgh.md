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
api_count: 4
apis:
- description: 'WPRDC is an open data portal operated as a partnership between the University of Pittsburgh, Allegheny County, and the City of Pittsburgh. It runs on CKAN and exposes the standard CKAN Action API for '
  name: Western Pennsylvania Regional Data Center (WPRDC) CKAN API
  slug: wprdc
- description: Project Tycho, hosted at the University of Pittsburgh, provides standardized global health and epidemiological surveillance data. Its public API supports listing reference variables (conditions, count
  name: Project Tycho API
  slug: project-tycho
- description: PittAPI is an unofficial, community-maintained Python library (developed by the Pitt Computer Science Club) that retrieves data from University of Pittsburgh sources, including courses, dining, librar
  name: PittAPI (community)
  slug: pittapi
- description: D-Scholarship@Pitt is the University Library System's institutional repository of research and scholarly output. It exposes an OAI-PMH metadata harvesting endpoint for programmatic access to repositor
  name: D-Scholarship@Pitt OAI-PMH
  slug: d-scholarship-oai
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-pittsburgh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pitt.edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/University-of-Pittsburgh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-pittsburgh/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ulsdevteam
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-pittsburgh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-pittsburgh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-pittsburgh-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Pittsburgh is a public research university in Pittsburgh, Pennsylvania, United States, ranked #271 in the QS World University Rankings 2025. Its public developer and API footprint is partly institutional and partly community-driven: the university co-operates the Western Pennsylvania Regional Data Center (WPRDC), a CKAN-based open data portal, and hosts the Project Tycho epidemiological data API. A widely used community Python library, PittAPI, exposes course, dining, library and other campus data, and the University Library System publishes an OAI-PMH feed from its D-Scholarship institutional repository. The university maintains an official GitHub organization plus several department/research-computing orgs.'
finops:
- name: University Of Pittsburgh Finops
  service_category: Education
  slug: university-of-pittsburgh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-pittsburgh.png
jsonld:
- class_count: 13
  name: University Of Pittsburgh Context
  property_count: 9
  slug: university-of-pittsburgh-context
layout: provider
modified: '2026-06-03'
name: University of Pittsburgh
nav: Providers
network: true
overview: 'University of Pittsburgh publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Research Data.


  The University of Pittsburgh catalog on APIs.io includes 1 JSON-LD context.


  University of Pittsburgh''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Pittsburgh Plans Pricing
  plan_count: 2
  slug: university-of-pittsburgh-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: University Of Pittsburgh Rate Limits
  slug: university-of-pittsburgh-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-pittsburgh/refs/heads/main/screenshots/university-of-pittsburgh-2026-06-20T200224.png
security:
- kind: domain-security
  name: University Of Pittsburgh Domain Security
  slug: university-of-pittsburgh-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: university-of-pittsburgh
tags:
- Education
- Higher Education
- University
- Open Data
- Research Data
- Library
- United States
website: https://www.pitt.edu
---
