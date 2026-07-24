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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Official institutional data and capability API platform for Tongji University. Provides documented APIs spanning personnel and student information, teaching and course/classroom data, library systems,
  name: Tongji University Open Platform
  slug: open-platform
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tongji-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tongji.edu.cn/
- group: company
  title: ''
  type: Website
  url: https://en.tongji.edu.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tongji.edu.cn/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tongji-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/tongji-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tongji-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tongji-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tongji University is a leading public research university in Shanghai, China (Mainland), ranked #192 in the QS World University Rankings 2025. It operates an official institutional Open Platform at api.tongji.edu.cn that exposes campus data and capability APIs (personnel, teaching, library, one-card, research, notifications and more) to faculty and students. The platform is governed by an application-and-approval process with OAuth-style authorization codes, token-based access, scope-based permissions and rate limiting, so the documentation is publicly reachable but the APIs themselves are gated to authorized institutional users rather than open to the general public.'
finops:
- name: Tongji Finops
  service_category: Education
  slug: tongji-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tongji.png
jsonld:
- class_count: 7
  name: Tongji Context
  property_count: 4
  slug: tongji-context
layout: provider
modified: '2026-06-03'
name: Tongji University
nav: Providers
network: true
overview: 'Tongji University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, China, and Shanghai.


  The Tongji University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Tongji Plans Pricing
  plan_count: 2
  slug: tongji-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 1
  name: Tongji Rate Limits
  slug: tongji-rate-limits
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/screenshots/tongji-2026-06-20T195456.png
security:
- kind: domain-security
  name: Tongji Domain Security
  slug: tongji-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tongji
tags:
- Education
- Higher Education
- University
- China
- Shanghai
- Open Platform
- Campus Data
website: https://www.tongji.edu.cn/
---
