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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Idnow Agentic Access
  operation_count: 5
  slug: idnow-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 4
apis:
- description: The Authentication API from IDnow — 1 operation(s) for authentication.
  name: IDnow Authentication API
  slug: idnow-authentication-api
- description: The Identifications API from IDnow — 2 operation(s) for identifications.
  name: IDnow Identifications API
  slug: idnow-identifications-api
- description: The Results API from IDnow — 1 operation(s) for results.
  name: IDnow Results API
  slug: idnow-results-api
- description: The VideoIdent API from IDnow — 1 operation(s) for videoident.
  name: IDnow VideoIdent API
  slug: idnow-videoident-api
artifact_total: 11
collections:
- collection_type: open
  name: IDnow Gateway API
  slug: open-idnow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/idnow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idnow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/idnow-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/idnow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/idnow
- group: company
  title: ''
  type: Website
  url: https://www.idnow.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.idnow.io/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/idnow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/idnow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/idnow-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://idnow.io/feed/
created: '2026-06-25'
description: IDnow is a European identity-verification platform offering automated (AutoIdent) and human-assisted (VideoIdent) KYC/identity proofing, plus eID and qualified electronic signing (eSign). Its RESTful gateway API lets companies create identification orders, drive the verification flow, retrieve results and documents, and subscribe to status webhooks.
finops:
- name: Idnow Finops
  service_category: Identity and Compliance
  slug: idnow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idnow.png
layout: provider
modified: '2026-06-25'
name: IDnow
nav: Providers
network: true
overview: 'IDnow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Identifications API, Results API, and 1 more. Tagged areas include Identity Verification, KYC, Identity Proofing, AML, and eSign.


  IDnow''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Idnow Plans Pricing
  plan_count: 1
  slug: idnow-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 2
  name: Idnow Rate Limits
  slug: idnow-rate-limits
score:
  band: thin
  composite: 34.8
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idnow/refs/heads/main/screenshots/idnow-2026-07-25T222031.png
security:
- kind: authentication
  name: Idnow Authentication
  slug: idnow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Idnow Domain Security
  slug: idnow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: idnow
tags:
- Identity Verification
- KYC
- Identity Proofing
- AML
- eSign
website: https://www.idnow.io
---
