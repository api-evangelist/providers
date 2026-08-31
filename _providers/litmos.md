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
    auth_clarity: false
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
  score: 19.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: RESTful API for the Litmos learning management system enabling management of users, teams, courses, learning paths, enrollments, assessments, and completion records. Supports JSON and XML data formats
  name: Litmos API
  slug: litmos-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litmos-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.litmos.com/docs/litmos/apis/overview-of-developer-api
- group: start
  title: ''
  type: Signup
  url: https://www.litmos.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://www.litmos.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.litmos.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.litmos.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.litmos.com/litmos-pricing
- group: design
  title: ''
  type: Webhooks
  url: https://www.litmos.com/docs/litmos/webhooks
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.litmos.com/release-notes/tags/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trifoia/litmos-sdk
- group: commercial
  title: ''
  type: Plans
  url: plans/litmos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/litmos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/litmos-finops.yml
created: '2026-06-13'
description: SAP Litmos is a cloud-based learning management system (LMS) with a REST API for managing courses, learning paths, user enrollment, completions, assessments, and training compliance reporting. The API enables organizations to automate user provisioning, synchronize training data with HR and CRM systems, manage teams, and retrieve completion records for compliance workflows.
finops:
- name: Litmos Finops
  service_category: ''
  slug: litmos-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the SAP Litmos Learning Management System (LMS) REST API. The schema models the core Litmos domain — courses, modules, learning paths, assessmen
  name: SAP Litmos GraphQL Schema
  slug: litmos-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litmos.png
layout: provider
modified: '2026-06-13'
name: Litmos
nav: Providers
network: true
overview: 'Litmos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Learning Management System, LMS, E-Learning, Training, and SAP.


  Litmos'' developer surface includes documentation, signup flow, engineering blog, support, pricing, release notes, and 7 more developer resources.'
plans:
- name: Litmos Plans Pricing
  plan_count: 3
  slug: litmos-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Litmos Rate Limits
  slug: litmos-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 33.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litmos/refs/heads/main/screenshots/litmos-2026-06-20T184608.png
security:
- kind: domain-security
  name: Litmos Domain Security
  slug: litmos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: litmos
tags:
- Learning Management System
- LMS
- E-Learning
- Training
- SAP
- Course Management
- User Enrollment
- Compliance
- Assessments
---
