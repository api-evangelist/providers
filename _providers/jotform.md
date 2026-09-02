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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Jotform Agentic Access
  operation_count: 45
  slug: jotform-agentic-access
  summary_line: 45 operations · 21 acting
api_count: 1
apis:
- description: EU-resident variant of the Jotform API for customers on EU plans / EU data residency.
  name: Jotform REST API (EU)
  slug: rest-eu
- description: HIPAA-compliant variant of the Jotform API for healthcare customers on Gold/Enterprise tiers.
  name: Jotform REST API (HIPAA)
  slug: rest-hipaa
- description: The Folder API from Jotform — 3 operation(s) for folder.
  name: Jotform Folder API
  slug: jotform-folder-api
- description: The Form API from Jotform — 10 operation(s) for form.
  name: Jotform Form API
  slug: jotform-form-api
- description: The Label API from Jotform — 4 operation(s) for label.
  name: Jotform Label API
  slug: jotform-label-api
- description: The Report API from Jotform — 3 operation(s) for report.
  name: Jotform Report API
  slug: jotform-report-api
- description: The Submission API from Jotform — 3 operation(s) for submission.
  name: Jotform Submission API
  slug: jotform-submission-api
- description: The System API from Jotform — 1 operation(s) for system.
  name: Jotform System API
  slug: jotform-system-api
- description: The User API from Jotform — 13 operation(s) for user.
  name: Jotform User API
  slug: jotform-user-api
- description: The Webhook API from Jotform — 2 operation(s) for webhook.
  name: Jotform Webhook API
  slug: jotform-webhook-api
artifact_total: 29
asyncapis:
- description: AsyncAPI definition for Jotform's webhook surface. Jotform delivers a POST request to a configured webhook URL each time a form receives a submission. The request body is sent as multipart/form-data a
  name: Jotform Webhooks AsyncAPI
  slug: jotform-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jotform REST Folder API
  slug: open-jotform-folder-api
- collection_type: open
  name: Jotform REST Folder Form API
  slug: open-jotform-form-api
- collection_type: open
  name: Jotform REST Folder Label API
  slug: open-jotform-label-api
- collection_type: open
  name: Jotform REST Folder Report API
  slug: open-jotform-report-api
- collection_type: open
  name: Jotform REST Folder Submission API
  slug: open-jotform-submission-api
- collection_type: open
  name: Jotform REST Folder System API
  slug: open-jotform-system-api
- collection_type: open
  name: Jotform REST Folder User API
  slug: open-jotform-user-api
- collection_type: open
  name: Jotform REST Folder Webhook API
  slug: open-jotform-webhook-api
- collection_type: open
  name: Jotform REST API
  slug: open-jotform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jotform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jotform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jotform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jotform-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.jotform.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jotform
- group: company
  title: ''
  type: Website
  url: https://www.jotform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.jotform.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jotform.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jotform
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jotform.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/jotform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jotform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jotform-finops.yml
created: '2026-05-08'
description: Jotform is an online form builder with strong workflow, payments and data collection capabilities. The Jotform API exposes forms, submissions, reports, folders, users, files and webhooks across three regional/compliance endpoints (US standard, EU, HIPAA). API-key authentication via header or query string.
finops:
- name: Jotform Finops
  service_category: Forms / Workflow
  slug: jotform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jotform.png
layout: provider
modified: '2026-05-30'
name: Jotform
nav: Providers
network: true
overview: 'Jotform publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Folder API, Form API, Label API, and 5 more. Tagged areas include Forms, Surveys, No-Code, Data Collection, and Workflows.


  The Jotform catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Jotform''s developer surface includes authentication, engineering blog, documentation, pricing, GitHub presence, and 9 more developer resources.'
plans:
- name: Jotform Plans Pricing
  plan_count: 5
  slug: jotform-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 9
  name: Jotform Rate Limits
  slug: jotform-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Jotform API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: jotform-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 57.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jotform/refs/heads/main/screenshots/jotform-2026-06-20T183806.png
security:
- kind: authentication
  name: Jotform Authentication
  slug: jotform-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Jotform Domain Security
  slug: jotform-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jotform Vulnerability Disclosure
  slug: jotform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jotform
tags:
- Forms
- Surveys
- No-Code
- Data Collection
- Workflows
- HIPAA
- EU
website: https://www.jotform.com/
---
