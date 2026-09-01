---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Delighted Agentic Access
  operation_count: 18
  slug: delighted-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 1
apis:
- description: Manage Autopilot drip campaign configuration and membership
  name: Delighted Autopilot API
  slug: delighted-autopilot-api
- description: Retrieve bounced email records
  name: Delighted Bounces API
  slug: delighted-bounces-api
- description: Retrieve NPS and satisfaction metrics
  name: Delighted Metrics API
  slug: delighted-metrics-api
- description: Manage people records for survey targeting
  name: Delighted People API
  slug: delighted-people-api
- description: Create and retrieve survey responses
  name: Delighted Survey Responses API
  slug: delighted-survey-responses-api
- description: Manage unsubscribe lists
  name: Delighted Unsubscribes API
  slug: delighted-unsubscribes-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Delighted Autopilot API
  slug: open-delighted-autopilot-api
- collection_type: open
  name: Delighted Autopilot Bounces API
  slug: open-delighted-bounces-api
- collection_type: open
  name: Delighted Autopilot Metrics API
  slug: open-delighted-metrics-api
- collection_type: open
  name: Delighted Autopilot People API
  slug: open-delighted-people-api
- collection_type: open
  name: Delighted Autopilot Survey Responses API
  slug: open-delighted-survey-responses-api
- collection_type: open
  name: Delighted Autopilot Unsubscribes API
  slug: open-delighted-unsubscribes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/delighted-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delighted-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/delighted-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://delighted.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.delighted.com/docs/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/delighted
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/delighted-inc-/
- group: company
  title: ''
  type: Blog
  url: https://delighted.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://delighted.com/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/delighted
- group: commercial
  title: ''
  type: Plans
  url: plans/delighted-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/delighted-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/delighted-finops.yml
created: '2026-06-13'
description: Delighted is an NPS and customer satisfaction survey platform with a REST API for managing surveys, collecting responses, segmenting results, and accessing trend data for CSAT, NPS, and CES. The API supports sending surveys to people, listing and adding survey responses, managing Autopilot configurations, retrieving metrics, handling webhooks, and managing unsubscribes and people records. Authentication is via HTTP Basic Auth using per-project API keys.
examples:
- key_count: 4
  name: Get Metrics
  slug: get-metrics
- key_count: 4
  name: List Survey Responses
  slug: list-survey-responses
- key_count: 4
  name: Send To Person
  slug: send-to-person
finops:
- name: Delighted Finops
  service_category: ''
  slug: delighted-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delighted.png
json_schemas:
- name: Metrics
  property_count: 8
  slug: metrics
- name: Person
  property_count: 8
  slug: person
- name: SurveyResponse
  property_count: 12
  slug: survey-response
jsonld:
- class_count: 1
  name: Delighted Context
  property_count: 42
  slug: delighted-context
layout: provider
modified: '2026-06-13'
name: Delighted
nav: Providers
network: true
overview: 'Delighted publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Autopilot API, Bounces API, Metrics API, and 3 more. Tagged areas include NPS, CSAT, Customer Satisfaction, CES, and Customer Effort Score.


  The Delighted catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Delighted''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Delighted Plans Pricing
  plan_count: 6
  slug: delighted-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Delighted Rate Limits
  slug: delighted-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Delighted API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: delighted-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 61.6
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delighted/refs/heads/main/screenshots/delighted-2026-06-20T175852.png
security:
- kind: authentication
  name: Delighted Authentication
  slug: delighted-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Delighted Domain Security
  slug: delighted-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: delighted
tags:
- NPS
- CSAT
- Customer Satisfaction
- CES
- Customer Effort Score
- Survey
- Customer Experience
- Feedback
- eNPS
website: https://delighted.com/
---
