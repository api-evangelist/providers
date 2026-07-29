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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lattice Agentic Access
  operation_count: 29
  slug: lattice-agentic-access
  summary_line: 29 operations · 6 acting
api_count: 11
apis:
- description: Retrieve competencies
  name: Lattice Competencies API
  slug: lattice-competencies-api
- description: Manage and retrieve department records
  name: Lattice Departments API
  slug: lattice-departments-api
- description: Retrieve continuous feedback
  name: Lattice Feedbacks API
  slug: lattice-feedbacks-api
- description: Create and retrieve goal progress updates
  name: Lattice Goal Updates API
  slug: lattice-goal-updates-api
- description: Create, read, and update goals and OKRs
  name: Lattice Goals API
  slug: lattice-goals-api
- description: Retrieve information about the authenticated user
  name: Lattice Me API
  slug: lattice-me-api
- description: Manage performance review cycles
  name: Lattice Review Cycles API
  slug: lattice-review-cycles-api
- description: Manage reviewees within a review cycle
  name: Lattice Reviewees API
  slug: lattice-reviewees-api
- description: Create, update, and submit performance reviews (v2)
  name: Lattice Reviews API
  slug: lattice-reviews-api
- description: Retrieve tags used across goals and feedback
  name: Lattice Tags API
  slug: lattice-tags-api
- description: Manage and retrieve user records
  name: Lattice Users API
  slug: lattice-users-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lattice-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lattice-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lattice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lattice-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lattice.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lattice.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lattice-hq
- group: other
  title: ''
  type: X
  url: https://x.com/latticehq
- group: company
  title: ''
  type: Blog
  url: https://lattice.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lattice.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.latticehq.com
- group: commercial
  title: ''
  type: Plans
  url: plans/lattice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lattice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lattice-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lattice-goal.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lattice-user.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lattice-review-cycle.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/lattice-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lattice-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/lattice-list-goals-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lattice-create-goal-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lattice-create-draft-review-example.json
created: 2026-06-12
description: 'Lattice is a people management platform used by over 5,000 companies to run performance reviews, track OKRs and goals, collect employee engagement survey data, manage compensation, and handle core HR (HRIS) workflows. The platform exposes two public REST APIs: the Lattice Talent API (v1) for performance, goals, feedback, and review data, and the Lattice HRIS API (v2) for employee records and organizational data. Both APIs use API-key authentication and are documented on the Lattice Developer Hub at developers.lattice.com. Lattice integrates with Slack, Gmail, Microsoft Teams, Salesforce, BambooHR, Okta, and other enterprise tools, and supports SCIM provisioning for identity management.'
examples:
- key_count: 2
  name: Lattice Create Draft Review Example
  slug: lattice-create-draft-review-example
- key_count: 2
  name: Lattice Create Goal Example
  slug: lattice-create-goal-example
- key_count: 4
  name: Lattice List Goals Example
  slug: lattice-list-goals-example
finops:
- name: Lattice Finops
  service_category: ''
  slug: lattice-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Lattice people success platform. Lattice publicly exposes REST APIs (Talent API v1 and HRIS API v2), but the types defined here model the fu
  name: Lattice GraphQL Schema
  slug: lattice-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lattice.png
json_schemas:
- name: Goal
  property_count: 27
  slug: lattice-goal
- name: ReviewCycle
  property_count: 18
  slug: lattice-review-cycle
- name: User
  property_count: 24
  slug: lattice-user
jsonld:
- class_count: 74
  name: Lattice Context
  property_count: 28
  slug: lattice-context
layout: provider
modified: 2026-06-12
name: Lattice
nav: Providers
network: true
overview: 'Lattice publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Competencies API, Departments API, Feedbacks API, and 8 more. Tagged areas include HR, People Management, Performance Management, OKRs, and Goals.


  The Lattice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lattice''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, and 17 more developer resources.'
plans:
- name: Lattice Plans Pricing
  plan_count: 6
  slug: lattice-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Lattice Rate Limits
  slug: lattice-rate-limits
rules:
- name: Lattice API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lattice-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.2
  delta: -3.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 73.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lattice/refs/heads/main/screenshots/lattice-2026-06-20T184350.png
security:
- kind: authentication
  name: Lattice Authentication
  slug: lattice-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lattice Domain Security
  slug: lattice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lattice Trust Center
  slug: lattice-trust-center
  summary_line: SOC 2, GDPR
slug: lattice
tags:
- HR
- People Management
- Performance Management
- OKRs
- Goals
- Employee Engagement
- HRIS
- Compensation
- Feedback
- Surveys
website: https://lattice.com
---
