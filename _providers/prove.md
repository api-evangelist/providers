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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Prove Agentic Access
  operation_count: 26
  slug: prove-agentic-access
  summary_line: 26 operations · 19 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Phone-based authentication and device binding.
  name: Prove Auth API
  slug: prove-auth-api
- description: OAuth 2.0 token issuance.
  name: Prove Authentication API
  slug: prove-authentication-api
- description: Cross-domain linking of identity scopes.
  name: Prove Domain API
  slug: prove-domain-api
- description: Persistent identity lifecycle management.
  name: Prove Identity API
  slug: prove-identity-api
- description: Ordered Pre-Fill verification flow - start, validate, challenge, complete.
  name: Prove Identity Verification API
  slug: prove-identity-verification-api
- description: Identity discovery and verified attribute retrieval.
  name: Prove Pre-Fill API
  slug: prove-pre-fill-api
- description: Unified Authentication possession and trust evaluation.
  name: Prove Trust Score API
  slug: prove-trust-score-api
artifact_total: 15
collections:
- collection_type: open
  name: Prove API
  slug: open-prove
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prove-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prove-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prove-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/prove-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prove-identity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proveidentity
- group: company
  title: ''
  type: Website
  url: https://www.prove.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.prove.com
- group: commercial
  title: ''
  type: Plans
  url: plans/prove-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prove-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prove-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.prove.com/blog
created: '2026-06-21'
description: Prove is a phone-centric digital identity verification and authentication platform. The Prove API (v3) uses the consumer's mobile phone number and cryptographic possession signals to power Pre-Fill identity prefill, passive Trust Score verification, Unified Authentication, and an Identity Manager - all behind an OAuth 2.0 secured REST interface at https://api.prove.com/v3.
finops:
- name: Prove Finops
  service_category: Identity and Security
  slug: prove-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prove.png
layout: provider
modified: '2026-06-21'
name: Prove
nav: Providers
network: true
overview: 'Prove publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Authentication API, Domain API, and 4 more. Tagged areas include Identity Verification, Authentication, Phone Intelligence, KYC, and Fraud Prevention.


  Prove''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Prove Plans Pricing
  plan_count: 2
  slug: prove-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 4
  name: Prove Rate Limits
  slug: prove-rate-limits
scopes:
- name: Prove Scopes
  scope_count: 0
  slug: prove-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Prove Authentication
  slug: prove-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Prove Domain Security
  slug: prove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prove
tags:
- Identity Verification
- Authentication
- Phone Intelligence
- KYC
- Fraud Prevention
website: https://www.prove.com
---
