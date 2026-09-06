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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Prove Agentic Access
  operation_count: 26
  slug: prove-agentic-access
  summary_line: 26 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: Phone-based authentication and device binding.
  name: Prove Auth API
  slug: prove-auth-api
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: OAuth 2.0 token issuance.
  name: Prove Authentication API
  slug: prove-authentication-api
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: Cross-domain linking of identity scopes.
  name: Prove Domain API
  slug: prove-domain-api
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: Persistent identity lifecycle management.
  name: Prove Identity API
  slug: prove-identity-api
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: Ordered Pre-Fill verification flow - start, validate, challenge, complete.
  name: Prove Identity Verification API
  slug: prove-identity-verification-api
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: Identity discovery and verified attribute retrieval.
  name: Prove Pre-Fill API
  slug: prove-pre-fill-api
- baseURL: https://api.prove.com/v3
  baseurl_source: declared
  description: Unified Authentication possession and trust evaluation.
  name: Prove Trust Score API
  slug: prove-trust-score-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prove Auth API
  slug: open-prove-auth-api
- collection_type: open
  name: Prove Auth Authentication API
  slug: open-prove-authentication-api
- collection_type: open
  name: Prove Auth Domain API
  slug: open-prove-domain-api
- collection_type: open
  name: Prove Auth Identity API
  slug: open-prove-identity-api
- collection_type: open
  name: Prove Auth Identity Verification API
  slug: open-prove-identity-verification-api
- collection_type: open
  name: Prove Auth Pre-Fill API
  slug: open-prove-pre-fill-api
- collection_type: open
  name: Prove Auth Trust Score API
  slug: open-prove-trust-score-api
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
random_paper: 10
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
  composite: 33.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 15.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prove/refs/heads/main/screenshots/prove-2026-09-02T152234.png
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
