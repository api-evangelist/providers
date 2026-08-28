---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.4
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: REST-based interface for integrating external systems with Absorb LMS. Supports user management, course management, enrollment processing, certificate tracking, department administration, and e-learni
  name: Absorb Integration API
  slug: absorb-integration-api
- description: Implements the SCIM 2.0 standard for seamless user and group provisioning through standardized endpoints, enabling automated identity lifecycle management in Absorb LMS.
  name: Absorb SCIM API
  slug: absorb-scim-api
- description: Enables developers to embed Absorb LMS learning experiences directly within external applications. Requires a paid add-on license for access.
  name: Absorb Infuse API
  slug: absorb-infuse-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/absorb-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.myabsorb.com/
- group: operate
  title: ''
  type: Support
  url: https://support.absorblms.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.absorblms.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.absorblms.com/hc/en-us/articles/22151754631955-Integration-API-Change-Log
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.absorblms.com/hc/en-us/sections/204325708-Absorb-LMS-Release-Notes
- group: design
  title: ''
  type: Webhooks
  url: https://docs.myabsorb.com/integration-api/v2/docs#webhooks
- group: start
  title: ''
  type: GettingStarted
  url: https://support.absorblms.com/hc/en-us/articles/222482188-Getting-Started-with-the-Absorb-Integration-API
- group: other
  title: ''
  type: Glossary
  url: https://support.absorblms.com/hc/en-us/articles/26898046456467-Integration-API-Glossary
- group: commercial
  title: ''
  type: Plans
  url: plans/absorb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/absorb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/absorb-finops.yml
created: '2026-06-13'
description: Absorb LMS is a cloud-based learning management system with a REST API for managing learners, courses, certificates, departments, enrollments, and tracking e-learning completion data. The Integration API provides a REST-based interface for integrating external systems with Absorb LMS, supporting user and enrollment management, course administration, and reporting.
finops:
- name: Absorb Finops
  service_category: ''
  slug: absorb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/absorb.png
layout: provider
modified: '2026-06-13'
name: Absorb LMS
nav: Providers
network: true
overview: 'Absorb LMS publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LMS, Learning Management, E-Learning, Training, and Courses.


  Absorb LMS''s developer surface includes documentation, support, engineering blog, changelog, release notes, getting-started guide, and 6 more developer resources.'
plans:
- name: Absorb Plans Pricing
  plan_count: 3
  slug: absorb-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Absorb Rate Limits
  slug: absorb-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 4.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 24.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/absorb/refs/heads/main/screenshots/absorb-2026-06-20T163412.png
security:
- kind: domain-security
  name: Absorb Domain Security
  slug: absorb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: absorb
tags:
- LMS
- Learning Management
- E-Learning
- Training
- Courses
- Enrollments
- Certificates
---
