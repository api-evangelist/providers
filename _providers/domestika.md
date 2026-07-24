---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Domestika REST API at api.domestika.org is the internal backbone of the Domestika platform, providing access to course catalog listings, learner enrollment records, user profiles, community conten
  name: Domestika API
  slug: domestika-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domestika-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.domestika.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.domestika.org/en/organizations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/domestika
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/domestika
- group: company
  title: ''
  type: Blog
  url: https://www.domestika.org/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.domestika.org/en/organizations
- group: other
  title: ''
  type: X
  url: https://x.com/Domestika
- group: commercial
  title: ''
  type: Plans
  url: plans/domestika-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/domestika-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/domestika-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/domestika-context.jsonld
created: 2026-06-13
description: Domestika is an online creative education platform that connects over 8 million creative professionals and learners with high-quality courses across illustration, design, photography, marketing, and more. The platform provides a REST API at api.domestika.org that powers its web and mobile applications, exposing course catalog data, user enrollment information, and community features. Domestika for Business extends the platform to organizations, enabling teams to purchase seat licenses and track learner progress through a management dashboard. Creative professionals and businesses can leverage Domestika's catalog and learner data to integrate creative skills development into their workflows and tooling.
finops:
- name: Domestika Finops
  service_category: ''
  slug: domestika-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domestika.png
jsonld:
- class_count: 10
  name: Domestika Context
  property_count: 1
  slug: domestika-context
layout: provider
modified: 2026-06-13
name: Domestika
nav: Providers
network: true
overview: 'Domestika publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Creative Education, Online Learning, Courses, Design, and Photography.


  The Domestika catalog on APIs.io includes 1 JSON-LD context.


  Domestika''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Domestika Plans Pricing
  plan_count: 6
  slug: domestika-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 0
  name: Domestika Rate Limits
  slug: domestika-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 52.8
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domestika/refs/heads/main/screenshots/domestika-2026-06-20T180145.png
security:
- kind: domain-security
  name: Domestika Domain Security
  slug: domestika-domain-security
  summary_line: TLSv1.3 · DMARC
slug: domestika
tags:
- Creative Education
- Online Learning
- Courses
- Design
- Photography
- Illustration
- Enterprise Learning
- REST API
website: https://www.domestika.org
---
