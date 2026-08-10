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
- acting_count: 7
  human_in_the_loop: 0
  name: Pverify Agentic Access
  operation_count: 10
  slug: pverify-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 6
apis:
- description: The Authentication API from pVerify — 1 operation(s) for authentication.
  name: pVerify Authentication API
  slug: pverify-authentication-api
- description: The Batch API from pVerify — 1 operation(s) for batch.
  name: pVerify Batch API
  slug: pverify-batch-api
- description: The Claim Status API from pVerify — 1 operation(s) for claim status.
  name: pVerify Claim Status API
  slug: pverify-claim-status-api
- description: The Eligibility API from pVerify — 5 operation(s) for eligibility.
  name: pVerify Eligibility API
  slug: pverify-eligibility-api
- description: The Estimation API from pVerify — 1 operation(s) for estimation.
  name: pVerify Estimation API
  slug: pverify-estimation-api
- description: The Payers API from pVerify — 1 operation(s) for payers.
  name: pVerify Payers API
  slug: pverify-payers-api
artifact_total: 13
collections:
- collection_type: open
  name: pVerify API
  slug: open-pverify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pverify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pverify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pverify-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pVerify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pverify
- group: company
  title: ''
  type: Website
  url: https://www.pverify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pverify.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/pverify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pverify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pverify-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pverify.com/blog/
created: '2026-06-21'
description: pVerify provides real-time healthcare insurance eligibility verification and revenue-cycle APIs. Its RESTful API at https://api.pverify.com exchanges EDI 270/271 eligibility transactions, returns plan and benefit summaries, checks claim status (276/277), lists supported payers, and estimates patient financial responsibility, secured with OAuth2 bearer tokens.
finops:
- name: Pverify Finops
  service_category: Healthcare and Insurance
  slug: pverify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pverify.png
layout: provider
modified: '2026-06-21'
name: pVerify
nav: Providers
network: true
overview: 'pVerify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Batch API, Claim Status API, and 3 more. Tagged areas include Healthcare, Insurance, Eligibility, Claims, and EDI.


  pVerify''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pverify Plans Pricing
  plan_count: 2
  slug: pverify-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 4
  name: Pverify Rate Limits
  slug: pverify-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Pverify Authentication
  slug: pverify-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Pverify Domain Security
  slug: pverify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pverify
tags:
- Healthcare
- Insurance
- Eligibility
- Claims
- EDI
- 270/271
website: https://www.pverify.com
---
