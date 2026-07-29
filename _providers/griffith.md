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
api_count: 3
apis:
- description: REST API for Griffith Research Online, the university's institutional repository, running on DSpace 7.6. Provides programmatic access to communities, collections, items, bitstreams, and metadata for G
  name: Griffith Research Online (GRO) DSpace REST API
  slug: gro-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for Griffith Research Online. Supports the standard OAI verbs (Identify, ListMetadataFormats, ListRecords, etc.) for harvesting Dublin Core and other metadata '
  name: Griffith Research Online OAI-PMH
  slug: gro-oai
- description: 'Griffith University operates a Canvas (Instructure) learning management system at lms.griffith.edu.au. The Canvas LMS REST API documentation is publicly reachable and describes endpoints for courses, '
  name: Griffith Canvas LMS REST API
  slug: canvas-lms
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/griffith-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.griffith.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/GriffithUniLibrary
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gu-eresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/griffith-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/griffith-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/griffith-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/griffith-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Griffith University is a public research university in Queensland, Australia, ranked #255 in the QS World University Rankings 2025. Its public, machine-readable developer footprint centers on research and library infrastructure rather than a formal developer portal. Griffith Research Online (GRO), the institutional repository, runs on DSpace 7.6 and exposes both a REST API and an OAI-PMH 2.0 endpoint for harvesting publication and research-output metadata. The university also operates a Canvas LMS instance whose Instructure REST API documentation is publicly reachable, and maintains active GitHub organizations for its Library and eResearch Services teams. No unified, self-service Griffith developer portal was found; most administrative, course, timetable, and identity interfaces are gated behind institutional affiliation.'
finops:
- name: Griffith Finops
  service_category: Education
  slug: griffith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/griffith.png
jsonld:
- class_count: 19
  name: Griffith Context
  property_count: 12
  slug: griffith-context
layout: provider
modified: '2026-06-03'
name: Griffith University
nav: Providers
network: true
overview: 'Griffith University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Australia, and Research.


  The Griffith University catalog on APIs.io includes 1 JSON-LD context.


  Griffith University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Griffith Plans Pricing
  plan_count: 2
  slug: griffith-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 1
  name: Griffith Rate Limits
  slug: griffith-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/griffith/refs/heads/main/screenshots/griffith-2026-06-20T182409.png
security:
- kind: domain-security
  name: Griffith Domain Security
  slug: griffith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: griffith
tags:
- Education
- Higher Education
- University
- Australia
- Research
- Open Data
- Repository
website: https://www.griffith.edu.au/
---
