---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Claim Md Agentic Access
  operation_count: 15
  slug: claim-md-agentic-access
  summary_line: 15 operations · 15 acting
api_count: 5
apis:
- description: Claim status responses, modifications, and notes.
  name: Claim.MD Claim Status API
  slug: claim-md-claim-status-api
- description: Claim file upload and reconciliation.
  name: Claim.MD Claims API
  slug: claim-md-claims-api
- description: Real-time eligibility and benefit verification (270/271).
  name: Claim.MD Eligibility API
  slug: claim-md-eligibility-api
- description: Electronic remittance advice (835) listing and retrieval.
  name: Claim.MD ERA API
  slug: claim-md-era-api
- description: Payer directory, enrollment, appeals, and webhooks.
  name: Claim.MD Reference API
  slug: claim-md-reference-api
artifact_total: 12
collections:
- collection_type: open
  name: Claim.MD API
  slug: open-claim-md
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/claim-md-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/claim-md-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/claim-md-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/claim.md
- group: company
  title: ''
  type: Website
  url: https://www.claim.md
- group: docs
  title: ''
  type: Documentation
  url: https://docs.claim.md/docs/index
- group: commercial
  title: ''
  type: Plans
  url: plans/claim-md-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/claim-md-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/claim-md-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.claim.md/news
created: '2026-06-21'
description: Claim.MD is a medical-claims clearinghouse that connects healthcare providers and software vendors to thousands of payers. Its REST API (authenticated with an AccountKey) supports electronic claim submission (837P/837I), claim status tracking, electronic remittance advice (835 ERA), real-time eligibility (270/271), and file upload/download workflows.
finops:
- name: Claim Md Finops
  service_category: Healthcare Clearinghouse
  slug: claim-md-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/claim-md.png
layout: provider
modified: '2026-06-21'
name: Claim.MD
nav: Providers
network: true
overview: 'Claim.MD publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Claim Status API, Claims API, Eligibility API, and 2 more. Tagged areas include Healthcare, Medical Claims, Clearinghouse, EDI, and X12.


  Claim.MD''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Claim Md Plans Pricing
  plan_count: 2
  slug: claim-md-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Claim Md Rate Limits
  slug: claim-md-rate-limits
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.0
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/claim-md/refs/heads/main/screenshots/claim-md-2026-07-25T205451.png
security:
- kind: authentication
  name: Claim Md Authentication
  slug: claim-md-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Claim Md Domain Security
  slug: claim-md-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: claim-md
tags:
- Healthcare
- Medical Claims
- Clearinghouse
- EDI
- X12
- Revenue Cycle
website: https://www.claim.md
---
