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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Workleap Agentic Access
  operation_count: 29
  slug: workleap-agentic-access
  summary_line: 29 operations · 17 acting
api_count: 7
apis:
- description: User and system attribute management
  name: Workleap Attributes API
  slug: workleap-attributes-api
- description: Engagement scores and metrics for teams and organizations
  name: Workleap Engagement API
  slug: workleap-engagement-api
- description: Feedback retrieval and management
  name: Workleap Feedback API
  slug: workleap-feedback-api
- description: GoodVibes recognition items and collections
  name: Workleap GoodVibes API
  slug: workleap-goodvibes-api
- description: Group management within an organization
  name: Workleap Groups API
  slug: workleap-groups-api
- description: CSV and JSON-based provisioning workflows
  name: Workleap Provisioning API
  slug: workleap-provisioning-api
- description: User management and provisioning
  name: Workleap Users API
  slug: workleap-users-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workleap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workleap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workleap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workleap-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://workleap.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.workleap.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/workleap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workleaphq
- group: company
  title: ''
  type: Blog
  url: https://workleap.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://workleap.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workleap.com/
- group: other
  title: ''
  type: X
  url: https://x.com/workleaphq
- group: commercial
  title: ''
  type: Plans
  url: plans/workleap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workleap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/workleap-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workleap-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/workleap-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workleap-user.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workleap-group.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workleap-feedback.json
created: '2026-06-13'
description: Workleap is an employee experience platform (formerly GSoft/Officevibe) that provides a suite of products covering engagement surveys, performance management, recognition, onboarding, and learning management. The Workleap REST API allows developers and HR teams to automate user provisioning, group management, and organization-wide sync operations with their HRIS. The API also exposes engagement scores, pulse survey results, feedback data, GoodVibes recognition items, and team sentiment analytics collected by the Officevibe product. Authentication uses an API key passed via the workleap-subscription-key header, and API access is available on the Pro and Enterprise subscription plans.
examples:
- key_count: 5
  name: Workleap Create User Example
  slug: workleap-create-user-example
- key_count: 5
  name: Workleap Search Feedback Example
  slug: workleap-search-feedback-example
finops:
- name: Workleap Finops
  service_category: ''
  slug: workleap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workleap.png
json_schemas:
- name: Workleap Feedback
  property_count: 8
  slug: workleap-feedback
- name: Workleap Group
  property_count: 6
  slug: workleap-group
- name: Workleap User
  property_count: 10
  slug: workleap-user
jsonld:
- class_count: 11
  name: Workleap Context
  property_count: 52
  slug: workleap-context
layout: provider
modified: '2026-06-13'
name: Workleap
nav: Providers
network: true
overview: 'Workleap publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Engagement API, Feedback API, and 4 more. Tagged areas include Employee Experience, HR, Engagement, Pulse Surveys, and Performance Management.


  The Workleap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Workleap''s developer surface includes authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Workleap Plans Pricing
  plan_count: 4
  slug: workleap-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Workleap Rate Limits
  slug: workleap-rate-limits
rules:
- name: Workleap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workleap-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  delta: -0.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 69.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workleap/refs/heads/main/screenshots/workleap-2026-06-20T201612.png
security:
- kind: authentication
  name: Workleap Authentication
  slug: workleap-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Workleap Domain Security
  slug: workleap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Workleap Trust Center
  slug: workleap-trust-center
  summary_line: SOC 2, ISO 27001
slug: workleap
tags:
- Employee Experience
- HR
- Engagement
- Pulse Surveys
- Performance Management
- Officevibe
- User Provisioning
- HRIS
- Recognition
- Onboarding
website: https://workleap.com
---
