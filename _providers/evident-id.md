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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Evident Id Agentic Access
  operation_count: 3
  slug: evident-id-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: The Results API from Evident — 1 operation(s) for results.
  name: Evident Results API
  slug: evident-id-results-api
- description: The Submission API from Evident — 1 operation(s) for submission.
  name: Evident Submission API
  slug: evident-id-submission-api
- description: The Verification Requests API from Evident — 2 operation(s) for verification requests.
  name: Evident Verification Requests API
  slug: evident-id-verification-requests-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Evident VerifyAPI and Submit Results API
  slug: open-evident-id-results-api
- collection_type: open
  name: Evident VerifyAPI and Submit Results Submission API
  slug: open-evident-id-submission-api
- collection_type: open
  name: Evident VerifyAPI and Submit Results Verification Requests API
  slug: open-evident-id-verification-requests-api
- collection_type: open
  name: Evident VerifyAPI and SubmitAPI
  slug: open-evident-id
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evident-id-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evident-id-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evident-id-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evidentid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evident-id
- group: company
  title: ''
  type: Website
  url: https://www.evidentid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evidentid.com/v1
- group: commercial
  title: ''
  type: Plans
  url: plans/evident-id-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evident-id-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/evident-id-finops.yml
created: '2026-06-25'
description: Evident (Evident ID) is an identity and credential verification platform that lets businesses verify identity, background, certifications, licenses, and insurance (Certificate of Insurance / COI) on third parties through a single REST API. Its VerifyAPI and SubmitAPI orchestrate verification requests across thousands of attributes and authoritative data sources, returning fact-checked results with webhook notifications.
finops:
- name: Evident Id Finops
  service_category: Identity and Verification
  slug: evident-id-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evident-id.png
layout: provider
modified: '2026-06-25'
name: Evident
nav: Providers
network: true
overview: 'Evident publishes 3 APIs on the [APIs.io](https://apis.io/) network: Results API, Submission API, and Verification Requests API. Tagged areas include Identity Verification, Credential Verification, Background Check, Insurance Verification, and COI.


  Evident''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Evident Id Plans Pricing
  plan_count: 4
  slug: evident-id-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Evident Id Rate Limits
  slug: evident-id-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evident-id/refs/heads/main/screenshots/evident-id-2026-07-25T213758.png
security:
- kind: authentication
  name: Evident Id Authentication
  slug: evident-id-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Evident Id Domain Security
  slug: evident-id-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evident-id
tags:
- Identity Verification
- Credential Verification
- Background Check
- Insurance Verification
- COI
website: https://www.evidentid.com
---
