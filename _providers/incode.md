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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Incode Agentic Access
  operation_count: 14
  slug: incode-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Selfie capture, passive liveness, and face match.
  name: Incode Face and Liveness API
  slug: incode-face-and-liveness-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Validation against government databases.
  name: Incode Government Validation API
  slug: incode-government-validation-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Government ID capture and validation.
  name: Incode ID Verification API
  slug: incode-id-verification-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Create and complete onboarding sessions.
  name: Incode Onboarding API
  slug: incode-onboarding-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Fetch scores, OCR data, and images.
  name: Incode Results API
  slug: incode-results-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Sanctions, PEP, and warning-list screening.
  name: Incode Watchlist and AML API
  slug: incode-watchlist-and-aml-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Incode Omni Face and Liveness API
  slug: open-incode-face-and-liveness-api
- collection_type: open
  name: Incode Omni Face and Liveness Government Validation API
  slug: open-incode-government-validation-api
- collection_type: open
  name: Incode Omni Face and Liveness ID Verification API
  slug: open-incode-id-verification-api
- collection_type: open
  name: Incode Omni Face and Liveness Onboarding API
  slug: open-incode-onboarding-api
- collection_type: open
  name: Incode Omni Face and Liveness Results API
  slug: open-incode-results-api
- collection_type: open
  name: Incode Omni Face and Liveness Watchlist and AML API
  slug: open-incode-watchlist-and-aml-api
- collection_type: open
  name: Incode Omni API
  slug: open-incode
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/incode-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/incode-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/incode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Incode-Technologies-Example-Repos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/incodetech
- group: company
  title: ''
  type: Website
  url: https://incode.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.incode.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/incode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/incode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/incode-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://incode.com/blog
created: '2026-06-25'
description: Incode is an AI-powered identity verification and biometric authentication platform. The Incode Omni API runs configurable onboarding sessions that capture and validate government IDs, perform face match and passive liveness, run government-database and watchlist/AML checks, and return scores, OCR data, and images via REST.
finops:
- name: Incode Finops
  service_category: Identity and Compliance
  slug: incode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/incode.png
layout: provider
modified: '2026-06-25'
name: Incode
nav: Providers
network: true
overview: 'Incode publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Face and Liveness API, Government Validation API, ID Verification API, and 3 more. Tagged areas include Identity Verification, Biometrics, KYC, Liveness, and Onboarding.


  Incode''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Incode Plans Pricing
  plan_count: 2
  slug: incode-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Incode Rate Limits
  slug: incode-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incode/refs/heads/main/screenshots/incode-2026-07-25T222333.png
security:
- kind: authentication
  name: Incode Authentication
  slug: incode-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Incode Domain Security
  slug: incode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Incode Trust Center
  slug: incode-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP
slug: incode
tags:
- Identity Verification
- Biometrics
- KYC
- Liveness
- Onboarding
website: https://incode.com
---
