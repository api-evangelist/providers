---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Student lifecycle actions exposed through Ruzuku's Zapier integration - enroll a student in a course, unenroll a student, and find a student by email or ID. Authentication uses an API Key, API Secret,
  name: Ruzuku Students and Enrollments API
  slug: ruzuku-students-enrollments-api
- description: Course-activity event triggers surfaced through Ruzuku's Zapier integration - New Student Enrolled (with pricing and coupon data), Lesson Completed, Course Completed, Quiz Submitted (with score), Assi
  name: Ruzuku Activity Events API
  slug: ruzuku-activity-events-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ruzuku-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ruzuku-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ruzuku-inc-
- group: company
  title: ''
  type: Website
  url: https://www.ruzuku.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.ruzuku.com/article/796-how-to-set-up-your-zapier-intergration
- group: commercial
  title: ''
  type: Plans
  url: plans/ruzuku-plans-pricing.yml
created: '2026-07-05'
description: Ruzuku is a hosted online course platform for coaches, authors, and subject matter experts to create, teach, and sell online courses and learning communities. Ruzuku does not publish a documented public REST API or developer program. Its programmatic surface is exposed exclusively through a Zapier integration - authenticated with an API Key, API Secret, and Site URL generated under Account then Integrations then Configure Zapier - that offers event triggers (enrollments, lesson and course completions, quiz and assignment submissions, comments, cancellations) and a small set of student enroll, unenroll, and lookup actions. The APIs modeled below are honest logical groupings of that Zapier-mediated surface, not endpoints from a public Ruzuku API reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ruzuku.png
layout: provider
modified: '2026-07-05'
name: Ruzuku
nav: Providers
network: true
overview: 'Ruzuku publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Online Courses, Learning Management, Education, Course Platform, and Zapier.


  Ruzuku''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Ruzuku Plans Pricing
  plan_count: 3
  slug: ruzuku-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 15.6
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Ruzuku Domain Security
  slug: ruzuku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ruzuku Trust Center
  slug: ruzuku-trust-center
  summary_line: PCI DSS, GDPR
slug: ruzuku
tags:
- Online Courses
- Learning Management
- Education
- Course Platform
- Zapier
- Gated
website: https://www.ruzuku.com
---
