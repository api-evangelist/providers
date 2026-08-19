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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Hyperverge Agentic Access
  operation_count: 18
  slug: hyperverge-agentic-access
  summary_line: 18 operations · 16 acting
api_count: 6
apis:
- description: Passive liveness / presentation-attack detection from a single selfie, trained on 850M+ liveness checks. Delivered primarily through HyperVerge's mobile SDKs and the hosted onboarding Workflow; a stan
  name: HyperVerge Liveness Detection
  slug: hyperverge-liveness-api
- description: Central/government database verification for Indian documents.
  name: HyperVerge Database Verification API
  slug: hyperverge-database-verification-api
- description: Selfie-to-ID / selfie-to-selfie face comparison.
  name: HyperVerge Face Match API
  slug: hyperverge-face-match-api
- description: Cross-validation of user input against OCR/QR extraction output.
  name: HyperVerge Input Validation API
  slug: hyperverge-input-validation-api
- description: Document OCR and KYC field extraction for Indian identity documents.
  name: HyperVerge KYC OCR API
  slug: hyperverge-kyc-ocr-api
- description: Fuzzy and direct field matching.
  name: HyperVerge Matching API
  slug: hyperverge-matching-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HyperVerge Identity Verification Database Verification API
  slug: open-hyperverge-database-verification-api
- collection_type: open
  name: HyperVerge Identity Verification Database Verification Face Match API
  slug: open-hyperverge-face-match-api
- collection_type: open
  name: HyperVerge Identity Verification Database Verification Input Validation API
  slug: open-hyperverge-input-validation-api
- collection_type: open
  name: HyperVerge Identity Verification Database Verification KYC OCR API
  slug: open-hyperverge-kyc-ocr-api
- collection_type: open
  name: HyperVerge Identity Verification Database Verification Matching API
  slug: open-hyperverge-matching-api
- collection_type: open
  name: HyperVerge Identity Verification API
  slug: open-hyperverge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperverge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperverge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperverge-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyperverge
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperverge
- group: company
  title: ''
  type: Website
  url: https://hyperverge.co
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.hyperverge.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperverge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperverge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperverge-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hyperverge.co/blog/
created: '2026-07-12'
description: HyperVerge is an AI-based identity verification and customer onboarding platform (India-HQ, global) providing document OCR and KYC extraction, face match, passive liveness, government/central database verification, and field matching. Its REST APIs extract and verify Indian identity documents (PAN, Aadhaar, Passport, Voter ID, Driving License), match a selfie against an ID photo, and validate user input against central databases for onboarding, AML, and fraud prevention. APIs are region-hosted (India `ind-*`, plus APAC/other regions) and authenticated with an appId and appKey issued by HyperVerge; enterprise onboarding is required to obtain credentials.
finops:
- name: Hyperverge Finops
  service_category: Identity and Fraud Prevention
  slug: hyperverge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperverge.png
layout: provider
modified: '2026-07-12'
name: HyperVerge
nav: Providers
network: true
overview: 'HyperVerge publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Database Verification API, Face Match API, Input Validation API, and 2 more. Tagged areas include Identity Verification, KYC, Face Authentication, Liveness, and Document Verification.


  HyperVerge''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hyperverge Plans Pricing
  plan_count: 3
  slug: hyperverge-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Hyperverge Rate Limits
  slug: hyperverge-rate-limits
score:
  band: thin
  composite: 37.8
  delta: -0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 58.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperverge/refs/heads/main/screenshots/hyperverge-2026-07-25T221937.png
security:
- kind: authentication
  name: Hyperverge Authentication
  slug: hyperverge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hyperverge Domain Security
  slug: hyperverge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperverge
tags:
- Identity Verification
- KYC
- Face Authentication
- Liveness
- Document Verification
- India
- AML
- Onboarding
- Fraud Prevention
- AI
website: https://hyperverge.co
---
