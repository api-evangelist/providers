---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 3
  human_in_the_loop: 0
  name: Shuftipro Agentic Access
  operation_count: 3
  slug: shuftipro-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: The Status API from Shufti Pro — 2 operation(s) for status.
  name: Shufti Pro Status API
  slug: shuftipro-status-api
- description: The Verification API from Shufti Pro — 1 operation(s) for verification.
  name: Shufti Pro Verification API
  slug: shuftipro-verification-api
artifact_total: 9
collections:
- collection_type: open
  name: Shufti Pro Verification API
  slug: open-shuftipro
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shuftipro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shuftipro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shuftipro-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shuftipro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shufti-pro
- group: company
  title: ''
  type: Website
  url: https://shuftipro.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shuftipro.com
- group: commercial
  title: ''
  type: Plans
  url: plans/shuftipro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shuftipro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shuftipro-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://shuftipro.com/blog/
created: '2026-06-25'
description: Shufti Pro is a global identity-verification provider offering KYC, KYB, and AML compliance through a single REST API. The Shufti Pro API runs document, facial biometric, address, consent, and AML/background-check verifications across 240+ countries and territories, with asynchronous callbacks, status retrieval, and data deletion.
finops:
- name: Shuftipro Finops
  service_category: Identity and Compliance
  slug: shuftipro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shuftipro.png
layout: provider
modified: '2026-06-25'
name: Shufti Pro
nav: Providers
network: true
overview: 'Shufti Pro publishes 2 APIs on the [APIs.io](https://apis.io/) network: Status API and Verification API. Tagged areas include Identity Verification, KYC, KYB, AML, and Compliance.


  Shufti Pro''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Shuftipro Plans Pricing
  plan_count: 3
  slug: shuftipro-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Shuftipro Rate Limits
  slug: shuftipro-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Shuftipro Authentication
  slug: shuftipro-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Shuftipro Domain Security
  slug: shuftipro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shuftipro
tags:
- Identity Verification
- KYC
- KYB
- AML
- Compliance
website: https://shuftipro.com
---
