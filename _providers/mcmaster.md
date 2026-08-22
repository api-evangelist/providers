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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Institutional API management developer portal operated by McMaster University Technology Services. Access requires sign-in with a MacID and password plus a short registration step; APIs and products c
  name: McMaster API Service Developer Portal
  slug: developer-portal
- description: 'Publicly accessible OAI-PMH 2.0 metadata-harvesting interface for MacSphere, McMaster University Libraries'' DSpace institutional repository of theses, dissertations, and open-access research outputs. '
  name: MacSphere OAI-PMH Repository Interface
  slug: macsphere-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcmaster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mcmaster.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.mcmaster.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mcmaster-university
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/mcmaster-university/
- group: operate
  title: ''
  type: Status
  url: https://uts.mcmaster.ca/status/
- group: commercial
  title: ''
  type: Plans
  url: plans/mcmaster-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mcmaster-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mcmaster-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mcmaster-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'McMaster University is a public research university in Hamilton, Ontario, Canada, ranked #176 in the QS World University Rankings 2025. Its developer and API presence is centered on a gated API service developer portal operated by University Technology Services, which requires institutional MacID authentication and a registration step before any API can be subscribed to; the underlying API catalog is therefore not publicly browsable. The most openly accessible programmatic interface is the library''s MacSphere institutional repository, a DSpace platform that exposes a public OAI-PMH metadata-harvesting endpoint.'
finops:
- name: Mcmaster Finops
  service_category: Education
  slug: mcmaster-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcmaster.png
jsonld:
- class_count: 24
  name: Mcmaster Context
  property_count: 5
  slug: mcmaster-context
layout: provider
modified: '2026-06-03'
name: McMaster University
nav: Providers
network: true
overview: 'McMaster University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Canada, and Ontario.


  The McMaster University catalog on APIs.io includes 1 JSON-LD context.


  McMaster University''s developer surface includes GitHub presence, status page, engineering blog, and 9 more developer resources.'
plans:
- name: Mcmaster Plans Pricing
  plan_count: 2
  slug: mcmaster-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Mcmaster Rate Limits
  slug: mcmaster-rate-limits
score:
  band: emerging
  composite: 17.4
  delta: -3.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mcmaster/refs/heads/main/screenshots/mcmaster-2026-06-20T185102.png
security:
- kind: domain-security
  name: Mcmaster Domain Security
  slug: mcmaster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcmaster
tags:
- Education
- Higher Education
- University
- Canada
- Ontario
- Research
- Open Access
- Library
website: https://www.mcmaster.ca/
---
