---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: REST Affiliate API exposing the Udemy course catalog for course discovery and search by category, subcategory, price, language, and keyword. Authentication uses a base64-encoded HTTP Basic header deri
  name: Udemy Affiliate API
  slug: affiliate-api
- description: REST Instructor API providing programmatic access to instructor-owned courses, students, revenue reports, and course resources. Authentication uses bearer tokens scoped to instructor accounts.
  name: Udemy Instructor API
  slug: instructor-api
- description: REST API for Udemy Business customers to programmatically manage users, groups, course assignments, learning activity, and reporting for their enterprise learning environment.
  name: Udemy Business API
  slug: business-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/udemy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/udemy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/udemy
- group: company
  title: ''
  type: Website
  url: https://www.udemy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.udemy.com/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://business.udemy.com/request-demo/
- group: start
  title: ''
  type: Signup
  url: https://www.udemy.com/join/signup-popup/
- group: other
  title: ''
  type: Affiliate Program
  url: https://www.udemy.com/affiliate/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.udemy.com/terms/api/
- group: operate
  title: ''
  type: Support
  url: https://support.udemy.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/udemy
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/udemy-engineering
created: '2026-05-11'
description: Udemy is a global online learning marketplace offering tens of thousands of on-demand video courses across business, technology, design, and personal development, alongside Udemy Business, an enterprise learning subscription for workforce skills development. Udemy exposes REST APIs including the Affiliate API for course discovery and the Instructor API for instructor resources, both using bearer token authentication over HTTPS with JSON-formatted responses.
graphqls:
- description: This conceptual GraphQL schema models the Udemy online learning platform, covering the full lifecycle of courses, instructors, students, enrollment, learning progress, purchases, and enterprise learni
  name: Udemy GraphQL Schema
  slug: udemy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/udemy.png
layout: provider
modified: '2026-05-11'
name: Udemy
nav: Providers
network: true
overview: 'Udemy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Online Learning, E-Learning, Education, Courses, and Corporate Training.


  Udemy''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 56
score:
  band: thin
  composite: 28.9
  delta: 9.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 48.1
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/udemy/refs/heads/main/screenshots/udemy-2026-06-20T195955.png
security:
- kind: domain-security
  name: Udemy Domain Security
  slug: udemy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Udemy Trust Center
  slug: udemy-trust-center
  summary_line: SOC 2, ISO 27001
slug: udemy
tags:
- Online Learning
- E-Learning
- Education
- Courses
- Corporate Training
- Workforce Development
website: https://www.udemy.com
---
