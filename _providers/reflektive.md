---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reflektive Agentic Access
  operation_count: 4
  slug: reflektive-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 4
apis:
- description: V1 endpoint for real-time peer feedback between a single sender and recipient.
  name: Reflektive Real-time Feedback (v1) API
  slug: reflektive-real-time-feedback-v1-api
- description: V2 endpoint for real-time feedback with support for Team Recognition (multiple recipients).
  name: Reflektive Real-time Feedback (v2) API
  slug: reflektive-real-time-feedback-v2-api
- description: Report generation endpoints that kick off asynchronous jobs and return a task UUID for status polling.
  name: Reflektive Reports API
  slug: reflektive-reports-api
- description: Asynchronous task objects used to track the status of report generation jobs.
  name: Reflektive Tasks API
  slug: reflektive-tasks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reflektive Real-time Feedback (v1) Real-time Feedback (v1) Real-time Feedback (v1) API
  slug: open-reflektive-real-time-feedback-v1-api
- collection_type: open
  name: Reflektive Real-time Feedback (v1) Real-time Feedback (v1) Real-time Feedback (v2) API
  slug: open-reflektive-real-time-feedback-v2-api
- collection_type: open
  name: Reflektive Real-time Feedback (v1) Real-time Feedback (v1) Reports API
  slug: open-reflektive-reports-api
- collection_type: open
  name: Reflektive Real-time Feedback (v1) Real-time Feedback (v1) Tasks API
  slug: open-reflektive-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reflektive-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/reflektive-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reflektive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reflektive-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.reflektive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.reflektive.com/hc/en-us/articles/19691532062483-Technical-API-Documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/reflektive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reflektive
- group: company
  title: ''
  type: Blog
  url: https://www.peoplefluent.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.capterra.com/p/158192/Reflektive/
- group: operate
  title: ''
  type: StatusPage
  url: https://support.reflektive.com/
- group: other
  title: ''
  type: X
  url: https://x.com/reflektive
- group: commercial
  title: ''
  type: Plans
  url: plans/reflektive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reflektive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reflektive-finops.yml
created: '2026-06-13'
description: Reflektive is a cloud-based performance management platform that enables organizations to scale constructive, ongoing conversations across their workforce. The platform provides a REST API for managing performance reviews, real-time feedback, goal tracking, and engagement survey data, allowing engineering teams to integrate Reflektive data into their own systems and workflows. The API supports GET, POST, PATCH, and DELETE operations against company data using token-based authentication, with versioned endpoints covering real-time feedback, tasks, reports, goals, and review cycles. Hosted API reference documentation is available via SwaggerHub and a dedicated developer portal, enabling developers to explore and test endpoints interactively. Reflektive is now part of PeopleFluent, a learning and talent management suite operating under the Learning Technologies Group.
examples:
- key_count: 1
  name: Report Generation Response
  slug: report-generation-response
- key_count: 1
  name: Task Completed
  slug: task-completed
- key_count: 1
  name: Task Pending
  slug: task-pending
- key_count: 2
  name: V1 Real Time Feedback List
  slug: v1-real-time-feedback-list
- key_count: 2
  name: V2 Real Time Feedback List
  slug: v2-real-time-feedback-list
finops:
- name: Reflektive Finops
  service_category: ''
  slug: reflektive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reflektive.png
json_schemas:
- name: Employee
  property_count: 4
  slug: employee
- name: Real-time Feedback (v1)
  property_count: 5
  slug: feedback-v1
- name: Real-time Feedback (v2)
  property_count: 5
  slug: feedback-v2
- name: Task
  property_count: 3
  slug: task
jsonld:
- class_count: 6
  name: Reflektive Context
  property_count: 19
  slug: reflektive-context
layout: provider
modified: '2026-06-13'
name: Reflektive
nav: Providers
network: true
overview: 'Reflektive publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Real-time Feedback (v1) API, Real-time Feedback (v2) API, Reports API, and 1 more. Tagged areas include Performance Management, HR, Employee Feedback, Goal Tracking, and Engagement Surveys.


  The Reflektive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Reflektive''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Reflektive Plans Pricing
  plan_count: 1
  slug: reflektive-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Reflektive Rate Limits
  slug: reflektive-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Reflektive API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: reflektive-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.6
  delta: -6.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 75.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/reflektive/refs/heads/main/screenshots/reflektive-2026-06-20T192747.png
security:
- kind: authentication
  name: Reflektive Authentication
  slug: reflektive-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reflektive Domain Security
  slug: reflektive-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Reflektive Trust Center
  slug: reflektive-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: reflektive
tags:
- Performance Management
- HR
- Employee Feedback
- Goal Tracking
- Engagement Surveys
- Reviews
- People Analytics
- REST API
website: https://www.reflektive.com/
---
