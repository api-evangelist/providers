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
- acting_count: 5
  human_in_the_loop: 0
  name: Opkit Agentic Access
  operation_count: 15
  slug: opkit-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 5
apis:
- description: Read structured benefit details from completed eligibility inquiries.
  name: Opkit Benefits API
  slug: opkit-benefits-api
- description: Create and retrieve real-time insurance eligibility inquiries.
  name: Opkit Eligibility Inquiries API
  slug: opkit-eligibility-inquiries-api
- description: Manage patient records that are the subject of eligibility inquiries.
  name: Opkit Patients API
  slug: opkit-patients-api
- description: Look up insurance carriers (payers) Opkit connects to.
  name: Opkit Payers API
  slug: opkit-payers-api
- description: Register and manage webhook endpoints for event notifications.
  name: Opkit Webhooks API
  slug: opkit-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Opkit API
  slug: open-opkit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opkit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opkit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opkit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opkit
- group: company
  title: ''
  type: Website
  url: https://www.opkit.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opkit.co
- group: commercial
  title: ''
  type: Plans
  url: plans/opkit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opkit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opkit-finops.yml
created: '2026-06-21'
description: Opkit was a healthcare automation company that built an automated health insurance verification platform purpose-built for telehealth companies and virtual medical practices. The Opkit REST API let engineering teams run insurance eligibility checks, read benefits, look up payers, manage patients, and receive webhook events programmatically. Opkit (YC S21) later pivoted to a generative-AI healthcare call center and was acqui-hired by 11x in late 2024, after which the platform was wound down. This catalog documents the API as it was publicly described while it was operating.
finops:
- name: Opkit Finops
  service_category: Healthcare and Insurance Verification
  slug: opkit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opkit.png
layout: provider
modified: '2026-06-21'
name: Opkit
nav: Providers
network: true
overview: 'Opkit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Benefits API, Eligibility Inquiries API, Patients API, and 2 more. Tagged areas include Healthcare, Insurance, Eligibility, Benefits, and Verification.


  Opkit''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Opkit Plans Pricing
  plan_count: 1
  slug: opkit-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 2
  name: Opkit Rate Limits
  slug: opkit-rate-limits
score:
  band: thin
  composite: 31.7
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Opkit Authentication
  slug: opkit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opkit Domain Security
  slug: opkit-domain-security
  summary_line: no transport/DNS hardening detected
slug: opkit
tags:
- Healthcare
- Insurance
- Eligibility
- Benefits
- Verification
- Telehealth
website: https://www.opkit.co
---
