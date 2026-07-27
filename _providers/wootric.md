---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Wootric Agentic Access
  operation_count: 32
  slug: wootric-agentic-access
  summary_line: 32 operations · 13 acting
api_count: 8
apis:
- description: Manage survey decline records
  name: Wootric Declines API
  slug: wootric-declines-api
- description: Send email surveys and retrieve email statistics
  name: Wootric Email Surveys API
  slug: wootric-email-surveys-api
- description: Manage end user profiles and metadata
  name: Wootric End Users API
  slug: wootric-end-users-api
- description: Retrieve NPS summary metrics
  name: Wootric Metrics API
  slug: wootric-metrics-api
- description: Manage NPS/CSAT/CES survey responses
  name: Wootric Responses API
  slug: wootric-responses-api
- description: Access segment definitions
  name: Wootric Segments API
  slug: wootric-segments-api
- description: Manage end user survey settings
  name: Wootric Settings API
  slug: wootric-settings-api
- description: Access survey template configurations
  name: Wootric Survey Templates API
  slug: wootric-survey-templates-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wootric-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wootric-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wootric-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wootric.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wootric.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Wootric
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wootric
- group: company
  title: ''
  type: Blog
  url: https://www.wootric.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://wootric.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/Wootric/status_pages
- group: other
  title: ''
  type: X
  url: https://twitter.com/wootric
- group: commercial
  title: ''
  type: Plans
  url: plans/wootric-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wootric-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wootric-finops.yml
created: '2026-06-13'
description: Wootric (now part of InMoment) is a customer experience platform with a REST API for managing NPS, CSAT, and CES surveys, accessing feedback responses, and managing customer experience programs. The API supports end user management, survey distribution via email and SMS, response retrieval with promoter/passive/detractor filtering, metric summaries, and multi-region deployments across US, EU, and AU environments.
examples:
- key_count: 4
  name: Create End User
  slug: create-end-user
- key_count: 4
  name: Create Survey Response
  slug: create-survey-response
- key_count: 4
  name: Get Nps Summary
  slug: get-nps-summary
- key_count: 4
  name: Send Email Survey
  slug: send-email-survey
finops:
- name: Wootric Finops
  service_category: ''
  slug: wootric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wootric.png
json_schemas:
- name: EndUser
  property_count: 9
  slug: end-user
- name: NpsSummary
  property_count: 7
  slug: nps-summary
- name: SurveyResponse
  property_count: 10
  slug: survey-response
jsonld:
- class_count: 14
  name: Wootric Context
  property_count: 24
  slug: wootric-context
layout: provider
modified: '2026-06-13'
name: Wootric
nav: Providers
network: true
overview: 'Wootric publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Declines API, Email Surveys API, End Users API, and 5 more. Tagged areas include Customer Experience, NPS, CSAT, CES, and Net Promoter Score.


  The Wootric catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wootric''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Wootric Plans Pricing
  plan_count: 3
  slug: wootric-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: Wootric Rate Limits
  slug: wootric-rate-limits
rules:
- name: Wootric API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wootric-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.8
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 54.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wootric/refs/heads/main/screenshots/wootric-2026-06-20T201542.png
security:
- kind: authentication
  name: Wootric Authentication
  slug: wootric-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wootric Domain Security
  slug: wootric-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: wootric
tags:
- Customer Experience
- NPS
- CSAT
- CES
- Net Promoter Score
- Customer Satisfaction
- Customer Effort Score
- Surveys
- Feedback
- Voice of the Customer
website: https://wootric.com/
---
