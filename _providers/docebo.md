---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: RESTful API for managing all aspects of the Docebo learning platform including courses, users, enrollments, certifications, learning plans, reports, gamification, and e-commerce.
  name: Docebo REST API
  slug: docebo-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docebo-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.docebo.com/docs/api-general-information
- group: start
  title: ''
  type: Portal
  url: https://developer.docebo.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.docebo.com/docs/api-guides
- group: design
  title: ''
  type: Webhooks
  url: https://developer.docebo.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.docebo.com/hc/en-us/articles/17920441206034-Deprecated-and-changed-API-calls
- group: operate
  title: ''
  type: Status
  url: https://status.docebo.com
- group: company
  title: ''
  type: Blog
  url: https://www.docebo.com/learning-network/blog/integration-type/apis-and-webhooks/
- group: operate
  title: ''
  type: Community
  url: https://community.docebo.com/integrations-apis-45
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.docebo.com/hc/en-us/articles/19807231971474-Product-updates
- group: commercial
  title: ''
  type: Plans
  url: plans/docebo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docebo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/docebo-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/docebo.json
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Docebo is an AI-powered learning management system (LMS) platform providing a REST API for managing courses, users, learning plans, certifications, custom reports, gamification data, and e-commerce transactions. It serves enterprise and mid-market organizations with 250+ learners across employee, customer, and partner training use cases.
finops:
- name: Docebo Finops
  service_category: ''
  slug: docebo-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Docebo LMS (Learning Management System) platform. Docebo provides a REST API at https://developers.docebo.com/reference — this GraphQL schema models the sam
  name: Docebo GraphQL Schema
  slug: docebo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docebo.png
layout: provider
modified: '2026-06-13'
name: Docebo
nav: Providers
network: true
overview: 'Docebo publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Learning Management System, LMS, E-Learning, Training, and Courses.


  Docebo''s developer surface includes documentation, developer portal, authentication, changelog, status page, engineering blog, release notes, and 8 more developer resources.'
plans:
- name: Docebo Plans Pricing
  plan_count: 2
  slug: docebo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Docebo Rate Limits
  slug: docebo-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 40.6
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 35.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docebo/refs/heads/main/screenshots/docebo-2026-06-20T180103.png
security:
- kind: domain-security
  name: Docebo Domain Security
  slug: docebo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docebo
tags:
- Learning Management System
- LMS
- E-Learning
- Training
- Courses
- Certifications
- Gamification
- Learning Plans
- HR Tech
- AI Learning
website: https://developer.docebo.com
---
