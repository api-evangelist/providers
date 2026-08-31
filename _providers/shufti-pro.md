---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- acting_count: 3
  human_in_the_loop: 0
  name: Shufti Pro Agentic Access
  operation_count: 3
  slug: shufti-pro-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: 'REST API for end-to-end identity verification including document verification, facial biometrics with liveness detection, address verification, AML screening against 1700+ watchlists, phone and email '
  name: Shufti Pro Verification API
  slug: verification-api
- description: Business verification API providing Know Your Business (KYB) checks from official registries, business AML screening, and Know Your Investor (KYI) services. Enables companies to verify business entiti
  name: Shufti Pro KYB API
  slug: kyb-api
- description: Anti-money laundering screening API covering 1700+ global watchlists, sanctions lists, PEP databases, and adverse media sources. Provides ongoing monitoring and batch screening for individuals and bus
  name: Shufti Pro AML Screening API
  slug: aml-screening-api
- description: Biometric authentication and re-verification API enabling face-based login and identity re-confirmation for returning users. Uses liveness detection to prevent spoofing and supports fast ID reusabilit
  name: Shufti Pro Biometric Authentication API
  slug: biometric-auth-api
- description: The Status API from Shufti Pro — 2 operation(s) for status.
  name: Shufti Pro Status API
  slug: shufti-pro-status-api
- description: The Verification API from Shufti Pro — 1 operation(s) for verification.
  name: Shufti Pro Verification API
  slug: shufti-pro-verification-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shufti Pro Verification Status API
  slug: open-shufti-pro-status-api
- collection_type: open
  name: Shufti Pro Status Verification API
  slug: open-shufti-pro-verification-api
- collection_type: open
  name: Shufti Pro Verification API
  slug: open-shuftipro
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shufti-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shuftipro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shuftipro.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/shuftipro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shufti-pro
- group: company
  title: ''
  type: Blog
  url: https://shuftipro.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://shuftipro.com/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shuftipro.com/
- group: other
  title: ''
  type: X
  url: https://x.com/shufti_pro
- group: commercial
  title: ''
  type: Plans
  url: plans/shufti-pro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shufti-pro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shufti-pro-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shufti-pro-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shufti-pro-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shuftipro
created: '2026-06-13'
description: Shufti Pro is an AI-powered identity verification platform offering a REST API for document verification, face biometrics, AML screening, business verification (KYB), and address verification. The platform supports 10,000+ document types across 230+ countries and territories, integrates with 1700+ AML watchlists, and provides mobile SDKs for Android, iOS, Flutter, and React Native.
finops:
- name: Shufti Pro Finops
  service_category: ''
  slug: shufti-pro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shufti-pro.png
jsonld:
- class_count: 18
  name: Shufti Pro Context
  property_count: 27
  slug: shufti-pro-context
layout: provider
modified: '2026-08-08'
name: Shufti Pro
nav: Providers
network: true
overview: 'Shufti Pro publishes 2 APIs on the [APIs.io](https://apis.io/) network: Status API and Verification API. Tagged areas include Identity Verification, KYC, AML, KYB, and Face Biometrics.


  The Shufti Pro catalog on APIs.io includes 1 JSON-LD context.


  Shufti Pro''s developer surface includes documentation, engineering blog, pricing, authentication, and 11 more developer resources.'
plans:
- name: Shufti Pro Plans Pricing
  plan_count: 3
  slug: shufti-pro-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Shufti Pro Rate Limits
  slug: shufti-pro-rate-limits
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 62.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shufti-pro/refs/heads/main/screenshots/shufti-pro-2026-06-20T193953.png
security:
- kind: authentication
  name: Shufti Pro Authentication
  slug: shufti-pro-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Shufti Pro Domain Security
  slug: shufti-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shufti-pro
tags:
- Identity Verification
- KYC
- AML
- KYB
- Face Biometrics
- Document Verification
- Address Verification
- Liveness Detection
- eIDV
- Compliance
- Fraud Prevention
website: https://shuftipro.com/
---
