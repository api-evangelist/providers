---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: The core Learning Platform API provides access to organizational units, user accounts, enrollments, roles, permissions, and configuration variables. Manage courses, departments, semesters, and the ful
  name: Brightspace Learning Platform (LP) API
  slug: brightspace-lp-api
- description: The Learning Environment API provides access to course content, dropbox folders, grade objects, grade values, quizzes, surveys, discussions, forums, checklists, rubrics, release conditions, and intell
  name: Brightspace Learning Environment (LE) API
  slug: brightspace-le-api
- description: The ePortfolio API enables management of ePortfolio objects including artifacts, reflections, collections, activities, presentations, and objectives. Supports sharing, subscriptions, invites, comments
  name: Brightspace ePortfolio API
  slug: brightspace-eportfolio-api
- description: The Data Hub API provides access to bulk data export functionality, enabling institutions to extract large datasets of users, enrollments, grades, activity, and content for analytics, reporting, and d
  name: Brightspace Data Hub (BDS) API
  slug: brightspace-data-hub-api
- description: The IPSIS API provides a standardized interface for Student Information System (SIS) integration with Brightspace, enabling automated provisioning and management of courses, sections, users, enrollmen
  name: Brightspace IPSIS (SIS Integration) API
  slug: brightspace-ipsis-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/d2l-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.d2l.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.valence.desire2learn.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Brightspace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/d2l/
- group: company
  title: ''
  type: Blog
  url: https://community.d2l.com/brightspace/categories/product-news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.d2l.com/products/brightspace/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.d2l.com/
- group: other
  title: ''
  type: X
  url: https://x.com/D2L
- group: commercial
  title: ''
  type: Plans
  url: plans/d2l-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/d2l-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/d2l-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/d2l-context.jsonld
created: '2026-06-13'
description: D2L Brightspace is a leading cloud-based learning management system (LMS) used by educational institutions and organizations worldwide to deliver, manage, and personalize learning experiences. The Brightspace Learning Framework REST API provides comprehensive programmatic access to courses, users, enrollments, grades, content, quizzes, discussions, and learning outcomes. Developers can extend and integrate Brightspace using OAuth 2.0 authentication, with SDKs available for JavaScript, Java, and .NET. The API supports a wide range of use cases including SIS integration, third-party LTI tool connections, data export, intelligent agents, ePortfolio management, and automated workflow orchestration across the full academic lifecycle.
finops:
- name: D2L Finops
  service_category: ''
  slug: d2l-finops
graphqls:
- description: 'specificationVersion: "0.1.0"'
  name: D2L Brightspace GraphQL Schema
  slug: d2l-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/d2l.png
jsonld:
- class_count: 48
  name: D2L Context
  property_count: 30
  slug: d2l-context
layout: provider
modified: '2026-06-13'
name: D2L Brightspace
nav: Providers
network: true
overview: 'D2L Brightspace publishes 1 API on the [APIs.io](https://apis.io/) network: Brightspace Learning Platform (LP) API. Tagged areas include Learning Management System, LMS, Education Technology, EdTech, and E-Learning.


  The D2L Brightspace catalog on APIs.io includes 1 JSON-LD context.


  D2L Brightspace''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: D2L Plans Pricing
  plan_count: 2
  slug: d2l-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: D2L Rate Limits
  slug: d2l-rate-limits
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 45.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.2
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 33.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/d2l/refs/heads/main/screenshots/d2l-2026-06-20T175420.png
security:
- kind: domain-security
  name: D2L Domain Security
  slug: d2l-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: d2l
tags:
- Learning Management System
- LMS
- Education Technology
- EdTech
- E-Learning
- Courses
- Grades
- User
- Enrollments
- Quizzes
- Discussions
- Learning Outcomes
- ePortfolio
- SIS Integration
- LTI
website: https://www.d2l.com/
---
