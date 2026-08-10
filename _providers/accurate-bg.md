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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Accurate Bg Agentic Access
  operation_count: 26
  slug: accurate-bg-agentic-access
  summary_line: 26 operations · 11 acting
api_count: 10
apis:
- description: Webhook event notifications configured in the Accurate developer portal deliver order and report status updates (for example when an order completes) to a consumer-hosted HTTPS endpoint, so integrator
  name: Accurate Webhooks
  slug: accurate-bg-webhooks-api
- description: Pass/fail decisioning on completed orders.
  name: Accurate Background Adjudication API
  slug: accurate-bg-adjudication-api
- description: Screening subjects that background checks are run against.
  name: Accurate Background Candidates API
  slug: accurate-bg-candidates-api
- description: Supporting documents attached to an order.
  name: Accurate Background Documents API
  slug: accurate-bg-documents-api
- description: Candidate-facing notifications.
  name: Accurate Background Notifications API
  slug: accurate-bg-notifications-api
- description: Background-check orders placed against a candidate.
  name: Accurate Background Orders API
  slug: accurate-bg-orders-api
- description: Screening packages available on an account.
  name: Accurate Background Packages API
  slug: accurate-bg-packages-api
- description: Completed screening results and reports.
  name: Accurate Background Reports API
  slug: accurate-bg-reports-api
- description: Connectivity and health checks.
  name: Accurate Background Utility API
  slug: accurate-bg-utility-api
- description: Employment and education verification attempts.
  name: Accurate Background Verifications API
  slug: accurate-bg-verifications-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accurate-bg-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accurate-bg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accurate-bg-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/accurate-bg-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accurate-background
- group: company
  title: ''
  type: Website
  url: https://www.accurate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accuratebackground.com/
- group: docs
  title: ''
  type: APIReference
  url: https://accurate.readme.io/reference
- group: start
  title: ''
  type: SignUp
  url: https://developer.accuratebackground.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/accurate-bg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accurate-bg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/accurate-bg-finops.yml
created: '2026-07-03'
description: Accurate Background is an employment background screening and workforce compliance company. Its Accurate API (v3) lets HR platforms, ATS/HRIS vendors, and staffing tools embed background checks - criminal searches, SSN trace, employment and education verification, drug and health screening, driving records, identity/work authorization (Form I-9, E-Verify), and international screening - directly into their own applications. Integrators create candidates, order preset or custom screening packages, track order status and ETA, retrieve completed reports, adjudicate results, and receive status updates via webhooks. A free developer account and sandbox environment are available for testing; production access is provisioned under a screening services agreement.
finops:
- name: Accurate Bg Finops
  service_category: Background Screening and Compliance
  slug: accurate-bg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accurate-bg.png
layout: provider
modified: '2026-07-03'
name: Accurate Background
nav: Providers
network: true
overview: 'Accurate Background publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Adjudication API, Candidates API, Documents API, and 6 more. Tagged areas include Background Checks, Employment Screening, Identity Verification, Compliance, and HR Tech.


  Accurate Background''s developer surface includes authentication, documentation, API reference, signup flow, and 8 more developer resources.'
plans:
- name: Accurate Bg Plans Pricing
  plan_count: 3
  slug: accurate-bg-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Accurate Bg Rate Limits
  slug: accurate-bg-rate-limits
scopes:
- name: Accurate Bg Scopes
  scope_count: 0
  slug: accurate-bg-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 40.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 52.7
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accurate-bg/refs/heads/main/screenshots/accurate-bg-2026-07-25T181442.png
security:
- kind: authentication
  name: Accurate Bg Authentication
  slug: accurate-bg-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Accurate Bg Domain Security
  slug: accurate-bg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accurate-bg
tags:
- Background Checks
- Employment Screening
- Identity Verification
- Compliance
- HR Tech
- Screening
website: https://www.accurate.com/
---
