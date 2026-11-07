---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RESTful API for managing all aspects of the Docebo learning platform including courses, users, enrollments, certifications, learning plans, reports, gamification, and e-commerce.
  name: Docebo REST API
  slug: docebo-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.docebo.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.docebo.com/
- group: auth
  href: https://artifacts.apis.io/docebo/security/docebo-domain-security.yml
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
  href: https://artifacts.apis.io/docebo/plans/docebo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docebo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/docebo/rate-limits/docebo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/docebo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/docebo/finops/docebo-finops.yml
  title: ''
  type: FinOps
  url: finops/docebo-finops.yml
- group: design
  href: https://artifacts.apis.io/docebo/json-ld/docebo.json
  title: ''
  type: JSONLD
  url: json-ld/docebo.json
- group: company
  href: https://artifacts.apis.io/docebo/blogs/blogs.json
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Docebo is an AI-powered learning management system (LMS) platform providing a REST API for managing courses, users, learning plans, certifications, custom reports, gamification data, and e-commerce transactions. It serves enterprise and mid-market organizations with 250+ learners across employee, customer, and partner training use cases.
finops:
- has_sources: false
  method: generated
  name: Docebo Finops
  primary_unit: ''
  service_category: ''
  slug: docebo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docebo.png
layout: provider
modified: '2026-10-06'
name: Docebo
nav: Providers
network: true
overview: 'Docebo is listed with 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include LMS, E-Learning, Training, Courses, and Certification.


  Docebo''s developer surface includes documentation, developer portal, authentication, changelog, status page, engineering blog, release notes, and 10 more developer resources.'
plans:
- name: Docebo Plans Pricing
  plan_count: 2
  slug: docebo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Docebo Rate Limits
  slug: docebo-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 23.4
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 23.4
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Education & Research
    regime_id: education
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/docebo/docebo-2026-06-20T180103.png
security:
- kind: domain-security
  name: Docebo Domain Security
  slug: docebo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docebo
tags:
- LMS
- E-Learning
- Training
- Courses
- Certification
- Gamification
- Learning Plans
- Human Resources
- AI Learning
website: https://www.docebo.com/
---
