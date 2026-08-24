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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wuhan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.whu.edu.cn
- group: build
  title: ''
  type: GitHub
  url: https://github.com/WHUIR
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/wuhan-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/WHU_1893
- group: commercial
  title: ''
  type: Plans
  url: plans/wuhan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wuhan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wuhan-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Wuhan University (WHU), founded in 1893 and located in Wuhan, Hubei, China, is one of China''s oldest and most prestigious comprehensive research universities, ranked #194 in the QS World University Rankings 2025. It operates under the Ministry of Education of China and is recognized for surveying and remote sensing, geoinformatics, and the sciences. WHU does not publish a centralized, publicly documented developer or API portal; its official web presence (en.whu.edu.cn) is informational only. Discoverable developer activity is concentrated in research-group GitHub organizations rather than institutional API products. No public, documented institutional API endpoints could be confirmed at the time of review.'
finops:
- name: Wuhan Finops
  service_category: Education
  slug: wuhan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wuhan.png
jsonld:
- class_count: 11
  name: Wuhan Context
  property_count: 1
  slug: wuhan-context
layout: provider
modified: '2026-07-25'
name: Wuhan University
nav: Providers
network: true
overview: 'Wuhan University is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Wuhan University catalog on APIs.io includes 1 JSON-LD context.


  Wuhan University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Wuhan Plans Pricing
  plan_count: 2
  slug: wuhan-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Wuhan Rate Limits
  slug: wuhan-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wuhan/refs/heads/main/screenshots/wuhan-2026-06-20T201647.png
security:
- kind: domain-security
  name: Wuhan Domain Security
  slug: wuhan-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wuhan
tags:
- Education
- Higher Education
- University
- Research
- China
- Open-Source
website: https://en.whu.edu.cn
---
