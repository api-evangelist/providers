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
- acting_count: 21
  human_in_the_loop: 0
  name: Idanalyzer Agentic Access
  operation_count: 34
  slug: idanalyzer-agentic-access
  summary_line: 34 operations · 21 acting
api_count: 13
apis:
- description: REST API for 1:1 face matching between an identity document photo and a live selfie or uploaded image. Includes passive liveness detection to prevent spoofing with photos, videos, or masks, and deepfa
  name: ID Analyzer Biometric API
  slug: biometric-api
- description: REST API for Anti-Money Laundering (AML) and Politically Exposed Persons (PEP) screening. Searches global sanctions lists, watchlists, and PEP databases to support regulatory compliance obligations.
  name: ID Analyzer AML Screening API
  slug: aml-api
- description: Hosted drop-in KYC verification flow with embedded pages and QR code support. Enables businesses to launch a fully branded identity verification experience without building a front-end, with webhook c
  name: ID Analyzer DocuPass API
  slug: docupass-api
- description: 'REST API for storing, retrieving, updating, and exporting identity verification records with audit trails. Supports GDPR-compliant data lifecycle management including file attachments and transaction '
  name: ID Analyzer Transaction Vault API
  slug: transaction-vault-api
- description: Account profile and usage
  name: ID Analyzer Account API
  slug: idanalyzer-account-api
- description: Anti-Money Laundering and sanctions screening
  name: ID Analyzer AML API
  slug: idanalyzer-aml-api
- description: Face matching and liveness detection
  name: ID Analyzer Biometric API
  slug: idanalyzer-biometric-api
- description: Contract template management and document generation
  name: ID Analyzer Contract API
  slug: idanalyzer-contract-api
- description: Hosted KYC verification sessions
  name: ID Analyzer Docupass API
  slug: idanalyzer-docupass-api
- description: KYC profile management
  name: ID Analyzer Profile API
  slug: idanalyzer-profile-api
- description: Document scanning and OCR operations
  name: ID Analyzer Scanner API
  slug: idanalyzer-scanner-api
- description: Transaction record management and export
  name: ID Analyzer Transaction API
  slug: idanalyzer-transaction-api
- description: Webhook delivery log management
  name: ID Analyzer Webhook API
  slug: idanalyzer-webhook-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/idanalyzer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/idanalyzer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idanalyzer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/idanalyzer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.idanalyzer.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://developer.idanalyzer.com/docs/about-id-analyzer
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/idanalyzer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/services/products/evith-technology-id-analyzer
- group: company
  title: ''
  type: Blog
  url: https://www.idanalyzer.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.idanalyzer.com/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.idanalyzer.com
- group: other
  title: ''
  type: X
  url: https://x.com/idanalyzer
- group: commercial
  title: ''
  type: Plans
  url: plans/idanalyzer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/idanalyzer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/idanalyzer-finops.yml
created: '2026-06-13'
description: ID Analyzer is a cloud-based identity verification platform providing REST APIs for extracting and validating data from passports, driver licenses, and ID cards across 190+ countries. Core capabilities include document OCR with anti-forgery detection, biometric face matching and liveness verification, AML/PEP sanctions screening, and a hosted DocuPass KYC onboarding flow. The platform is ISO 27001 certified and compliant with GDPR, HIPAA, and NIST IAL2 standards.
examples:
- key_count: 4
  name: Idanalyzer Aml Example
  slug: idanalyzer-aml-example
- key_count: 4
  name: Idanalyzer Docupass Example
  slug: idanalyzer-docupass-example
- key_count: 4
  name: Idanalyzer Scan Example
  slug: idanalyzer-scan-example
finops:
- name: Idanalyzer Finops
  service_category: ''
  slug: idanalyzer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idanalyzer.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: ID Analyzer AML Search Request
  property_count: 6
  slug: idanalyzer-aml-request
- name: ID Analyzer DocuPass Create Request
  property_count: 19
  slug: idanalyzer-docupass-request
- name: ID Analyzer Scan Request
  property_count: 21
  slug: idanalyzer-scan-request
jsonld:
- class_count: 0
  name: Idanalyzer Context
  property_count: 83
  slug: idanalyzer-context
layout: provider
modified: '2026-06-13'
name: ID Analyzer
nav: Providers
network: true
overview: 'ID Analyzer publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, AML API, Biometric API, and 6 more. Tagged areas include Identity Verification, KYC, AML, Document OCR, and Biometrics.


  The ID Analyzer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ID Analyzer''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Idanalyzer Plans Pricing
  plan_count: 5
  slug: idanalyzer-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Idanalyzer Rate Limits
  slug: idanalyzer-rate-limits
rules:
- name: ID Analyzer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: idanalyzer-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.9
  delta: -4.8
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idanalyzer/refs/heads/main/screenshots/idanalyzer-2026-06-20T183201.png
security:
- kind: authentication
  name: Idanalyzer Authentication
  slug: idanalyzer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Idanalyzer Domain Security
  slug: idanalyzer-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Idanalyzer Trust Center
  slug: idanalyzer-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: idanalyzer
tags:
- Identity Verification
- KYC
- AML
- Document OCR
- Biometrics
- Face Matching
- Fraud Detection
- Passport
- Driver License
- Liveness Detection
website: https://www.idanalyzer.com/en
---
