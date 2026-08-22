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
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tianjin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.tju.edu.cn/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TJUBlockchainLab
- group: company
  title: ''
  type: LinkedIn
  url: https://cn.linkedin.com/school/tianjinuniversity/
- group: commercial
  title: ''
  type: Plans
  url: plans/tianjin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tianjin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tianjin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://opac.lib.tju.edu.cn
created: '2026-06-03'
description: 'Tianjin University (TJU) is a national public research university in Tianjin, China, founded in 1895 as Peiyang University and recognized as the oldest modern university in China. It is ranked #269 in the QS World University Rankings 2025. TJU operates the usual institutional web properties (official site, library OPAC, faculty and international-cooperation portals) but does not publish a public developer portal or documented, openly accessible API. No public API documentation, base URLs, or sign-up flows could be verified at the time of cataloging; the entries below reflect only confirmed public web properties, not documented APIs.'
finops:
- name: Tianjin Finops
  service_category: Education
  slug: tianjin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tianjin.png
jsonld:
- class_count: 8
  name: Tianjin Context
  property_count: 3
  slug: tianjin-context
layout: provider
modified: '2026-07-25'
name: Tianjin University
nav: Providers
network: true
overview: 'Tianjin University is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Tianjin University catalog on APIs.io includes 1 JSON-LD context.


  Tianjin University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Tianjin Plans Pricing
  plan_count: 2
  slug: tianjin-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Tianjin Rate Limits
  slug: tianjin-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: -1.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tianjin/refs/heads/main/screenshots/tianjin-2026-06-20T195443.png
security:
- kind: domain-security
  name: Tianjin Domain Security
  slug: tianjin-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: tianjin
tags:
- Education
- Higher Education
- University
- Research
- China
- Tianjin
website: https://en.tju.edu.cn/
---
