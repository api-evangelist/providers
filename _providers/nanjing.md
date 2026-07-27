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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Nanjing University operates a unified identity authentication platform providing single sign-on across university systems. The login service is a CAS (Central Authentication Service) deployment suppor
  name: Nanjing University Unified Identity Authentication (CAS SSO)
  slug: auth
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nanjing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nju.edu.cn/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MCG-NJU
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nanjing-university/
- group: auth
  title: ''
  type: Authentication
  url: https://authserver.nju.edu.cn/authserver/login
- group: commercial
  title: ''
  type: Plans
  url: plans/nanjing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nanjing-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nanjing-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://lib.nju.edu.cn/
created: '2026-06-03'
description: 'Nanjing University (NJU), founded in 1902 and located in Nanjing, Jiangsu, China, is one of China''s oldest and most prestigious research universities and is ranked #145 in the QS World University Rankings 2025. The university operates a unified identity authentication (CAS-based single sign-on) platform at authserver.nju.edu.cn and runs library discovery systems (OPAC and Summon) and a campus map, but it does not publish a public, documented developer API program or an open-data portal. The footprint cataloged here reflects only publicly observable, institution-facing systems; no public API endpoints, signup, or developer documentation were confirmed.'
finops:
- name: Nanjing Finops
  service_category: Education
  slug: nanjing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nanjing.png
jsonld:
- class_count: 13
  name: Nanjing Context
  property_count: 0
  slug: nanjing-context
layout: provider
modified: '2026-07-25'
name: Nanjing University
nav: Providers
network: true
overview: 'Nanjing University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Nanjing University catalog on APIs.io includes 1 JSON-LD context.


  Nanjing University''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Nanjing Plans Pricing
  plan_count: 2
  slug: nanjing-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: Nanjing Rate Limits
  slug: nanjing-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nanjing/refs/heads/main/screenshots/nanjing-2026-06-20T190003.png
security:
- kind: domain-security
  name: Nanjing Domain Security
  slug: nanjing-domain-security
  summary_line: TLSv1.2 · DMARC
slug: nanjing
tags:
- Education
- Higher Education
- University
- Research
- China
- Authentication
website: https://www.nju.edu.cn/en/
---
