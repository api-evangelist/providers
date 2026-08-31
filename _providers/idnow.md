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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Idnow Agentic Access
  operation_count: 5
  slug: idnow-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IDnow Gateway Authentication API
  slug: open-idnow-authentication-api
- collection_type: open
  name: IDnow Gateway Authentication Identifications API
  slug: open-idnow-identifications-api
- collection_type: open
  name: IDnow Gateway Authentication Results API
  slug: open-idnow-results-api
- collection_type: open
  name: IDnow Gateway Authentication VideoIdent API
  slug: open-idnow-videoident-api
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
random_paper: 20
rate_limits:
- limit_count: 2
  name: Idnow Rate Limits
  slug: idnow-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
