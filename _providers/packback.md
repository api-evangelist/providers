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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: Inquiry-based student discussion product with built-in AI coaching that helps students ask better questions and write stronger responses, plus automated moderation for instructors. Accessed by student
  name: Packback Questions / Discussions
  slug: questions-discussions
- description: Long-form writing and essay product (Writing, Deep Dives, Writing Lab) that gives students instant AI feedback on flow, structure, grammar, research quality, and formatting, with rubric-aligned AI-ass
  name: Packback Writing / Deep Dives
  slug: writing-deep-dives
- description: Packback's integration surface is the IMS Global LTI standard (1EdTech certified for LTI 1.0, 1.2, and 1.3 / LTI Advantage), providing single sign-on, deep linking, and gradebook/grade passback sync a
  name: Packback LTI Integration
  slug: lti-integration
artifact_total: 8
collections:
- collection_type: open
  name: Packback API
  slug: open-packback
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packback-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/packbackbooks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/packback
- group: company
  title: ''
  type: Website
  url: https://packback.co
- group: docs
  title: ''
  type: Documentation
  url: https://help.packback.co
- group: commercial
  title: ''
  type: Plans
  url: plans/packback-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/packback-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/packback-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://packback.co/feed/
created: '2026-06-21'
description: Packback is an AI-powered instructional platform for higher education and K-12 that delivers real-time, formative feedback on student discussion and writing. Its products - Questions/Discussions, Writing and Deep Dives, and Originality - embed into a school's LMS through the IMS Global LTI standard rather than a public REST API.
finops:
- name: Packback Finops
  service_category: Education and Learning Technology
  slug: packback-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packback.png
layout: provider
modified: '2026-06-21'
name: Packback
nav: Providers
network: true
overview: 'Packback publishes 3 APIs on the [APIs.io](https://apis.io/) network: Questions / Discussions, Writing / Deep Dives, and LTI Integration. Tagged areas include Education, EdTech, AI, Discussion, and Writing Feedback.


  Packback''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Packback Plans Pricing
  plan_count: 3
  slug: packback-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Packback Rate Limits
  slug: packback-rate-limits
score:
  band: emerging
  composite: 27.9
  delta: -0.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 31.8
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packback/refs/heads/main/screenshots/packback-2026-08-07T191240.png
security:
- kind: domain-security
  name: Packback Domain Security
  slug: packback-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: packback
tags:
- Education
- EdTech
- AI
- Discussion
- Writing Feedback
- LTI
- LMS
website: https://packback.co
---
