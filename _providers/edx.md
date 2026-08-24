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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: 'Open-source REST API surface across the Open edX platform: Enrollment API, Courses API, User API, Catalog API, Discussion API, Grades API, LTI APIs, Enterprise API. Implementations expose endpoints un'
  name: Open edX REST API
  slug: open-edx-rest
- description: Public/partner API surface hosted at api.edx.org for the edx.org learning marketplace. Access scopes vary by partner agreement.
  name: edX Public API
  slug: edx-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edx-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edx1
- group: company
  title: ''
  type: Website
  url: https://www.edx.org/
- group: other
  title: ''
  type: Developer
  url: https://docs.openedx.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/edx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edx-finops.yml
created: '2026-05-08'
description: edX is an online learning platform now operated by 2U; the underlying Open edX software is open source. Open edX exposes a comprehensive REST API surface (Enrollment, Courses, Users, Catalog, Discussion, Grades, LTI, Enterprise) and hosts a public API at api.edx.org for partners.
finops:
- name: Edx Finops
  service_category: Education & Training
  slug: edx-finops
graphqls:
- description: edX is an online learning platform offering MOOCs from universities and institutions. The API covers course catalog, enrollment management, course grades, certificates, user profiles, learner activity
  name: edX GraphQL API
  slug: edx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edx.png
layout: provider
modified: '2026-05-08'
name: edX
nav: Providers
network: true
overview: edX publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EdTech, Online Learning, Open-Source, and MOOC.
plans:
- name: Edx Plans Pricing
  plan_count: 2
  slug: edx-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Edx Rate Limits
  slug: edx-rate-limits
score:
  band: emerging
  composite: 15.6
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edx/refs/heads/main/screenshots/edx-2026-06-20T180510.png
security:
- kind: domain-security
  name: Edx Domain Security
  slug: edx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edx
tags:
- EdTech
- Online Learning
- Open-Source
- MOOC
website: https://www.edx.org/
---
