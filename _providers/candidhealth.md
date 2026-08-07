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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Candidhealth Agentic Access
  operation_count: 15
  slug: candidhealth-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 8
apis:
- description: OAuth client-credentials token exchange.
  name: Candid Health Auth API
  slug: candidhealth-auth-api
- description: Capture charges and service lines ahead of claim assembly.
  name: Candid Health Charge Capture API
  slug: candidhealth-charge-capture-api
- description: Real-time and batch insurance eligibility checks.
  name: Candid Health Eligibility API
  slug: candidhealth-eligibility-api
- description: Submit and manage encounters that drive claim generation.
  name: Candid Health Encounters API
  slug: candidhealth-encounters-api
- description: Scan and retrieve billing lifecycle events.
  name: Candid Health Events API
  slug: candidhealth-events-api
- description: Resolve contracted rates for service lines.
  name: Candid Health Fee Schedules API
  slug: candidhealth-fee-schedules-api
- description: Retrieve ERA / 835 remittance adjudication detail.
  name: Candid Health Insurance Adjudications API
  slug: candidhealth-insurance-adjudications-api
- description: Look up insurance payers.
  name: Candid Health Payers API
  slug: candidhealth-payers-api
artifact_total: 15
collections:
- collection_type: open
  name: Candid Health API
  slug: open-candidhealth
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/candidhealth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/candidhealth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/candidhealth-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/candidhealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/candidhealth
- group: company
  title: ''
  type: Website
  url: https://www.joincandidhealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joincandidhealth.com
- group: commercial
  title: ''
  type: Plans
  url: plans/candidhealth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/candidhealth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/candidhealth-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://candidhealth.com/blog
created: '2026-06-21'
description: Candid Health is an autonomous medical-billing and revenue-cycle management platform. Its REST API lets digital health providers submit encounters and claims, run real-time eligibility checks, capture charges, look up payers and fee schedules, reconcile remits/ERAs, and subscribe to billing events end-to-end.
finops:
- name: Candidhealth Finops
  service_category: Healthcare and Revenue Cycle Management
  slug: candidhealth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/candidhealth.png
layout: provider
modified: '2026-06-21'
name: Candid Health
nav: Providers
network: true
overview: 'Candid Health publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Charge Capture API, Eligibility API, and 5 more. Tagged areas include Healthcare, Medical Billing, Revenue Cycle, Claims, and Eligibility.


  Candid Health''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Candidhealth Plans Pricing
  plan_count: 3
  slug: candidhealth-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 3
  name: Candidhealth Rate Limits
  slug: candidhealth-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/candidhealth/refs/heads/main/screenshots/candidhealth-2026-07-25T204340.png
security:
- kind: authentication
  name: Candidhealth Authentication
  slug: candidhealth-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Candidhealth Domain Security
  slug: candidhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: candidhealth
tags:
- Healthcare
- Medical Billing
- Revenue Cycle
- Claims
- Eligibility
website: https://www.joincandidhealth.com
---
