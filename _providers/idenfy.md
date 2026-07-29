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
- acting_count: 25
  human_in_the_loop: 1
  name: Idenfy Agentic Access
  operation_count: 36
  slug: idenfy-agentic-access
  summary_line: 36 operations · 25 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: The iDenfy Identity Verification (KYC) API provides document verification, selfie checks, and liveness detection through redirect, iFrame, mobile SDK, or direct API integration.
  name: iDenfy Identity Verification API
  slug: idenfy-verification-api
- description: The iDenfy Business Verification (KYB) API enables company verification using registry lookups, ultimate beneficial owner identification, and credit report checks via redirect or iFrame integration.
  name: iDenfy Business Verification API
  slug: idenfy-business-verification-api
- description: The iDenfy AML Screening API screens individuals and companies against sanctions lists, politically exposed persons (PEPs), and adverse media, with one-time and ongoing monitoring options.
  name: iDenfy AML Screening API
  slug: idenfy-aml-screening-api
- description: The iDenfy Fraud Prevention API provides risk scoring, proxy detection, phone and address verification, and proof of address checks to identify and stop fraudulent activities.
  name: iDenfy Fraud Prevention API
  slug: idenfy-fraud-api
- description: The iDenfy Face Authentication API re-authenticates returning users by comparing a live facial scan against a previously verified identity.
  name: iDenfy Face Authentication API
  slug: idenfy-face-authentication-api
- description: The iDenfy Bank Verification API verifies bank accounts via open banking connections to over 2,500 European banks.
  name: iDenfy Bank Verification API
  slug: idenfy-bank-verification-api
- description: The Aml API from iDenfy — 6 operation(s) for aml.
  name: iDenfy Aml API
  slug: idenfy-aml-api
- description: The Bank API from iDenfy — 2 operation(s) for bank.
  name: iDenfy Bank API
  slug: idenfy-bank-api
- description: The Face Authentication API from iDenfy — 2 operation(s) for face authentication.
  name: iDenfy Face Authentication API
  slug: idenfy-face-authentication-api
- description: The Fraud API from iDenfy — 5 operation(s) for fraud.
  name: iDenfy Fraud API
  slug: idenfy-fraud-api
- description: The Kyb API from iDenfy — 7 operation(s) for kyb.
  name: iDenfy Kyb API
  slug: idenfy-kyb-api
- description: The Kyc API from iDenfy — 5 operation(s) for kyc.
  name: iDenfy Kyc API
  slug: idenfy-kyc-api
- description: The Token API from iDenfy — 1 operation(s) for token.
  name: iDenfy Token API
  slug: idenfy-token-api
artifact_total: 21
collections:
- collection_type: open
  name: iDenfy API
  slug: open-idenfy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/idenfy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/idenfy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idenfy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/idenfy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/idenfy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/idenfy
- group: company
  title: ''
  type: Website
  url: https://www.idenfy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.idenfy.com/
- group: operate
  title: ''
  type: Support
  url: https://www.idenfy.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://idenfy.com/llms.txt
created: '2024-11-13'
description: iDenfy is an identity verification platform providing KYC, KYB, and AML compliance solutions. The iDenfy API enables businesses to verify identities, check for fraud, and comply with regulatory requirements through automated document verification, facial recognition, AML screening, business verification, and bank verification services.
finops:
- name: Idenfy Finops
  service_category: API
  slug: idenfy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idenfy.png
layout: provider
modified: '2026-04-28'
name: iDenfy
nav: Providers
network: true
overview: 'iDenfy publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Fraud Prevention API, Face Authentication API, Aml API, and 6 more. Tagged areas include AML, Compliance, Fraud Detection, Identity Verification, and KYB.


  iDenfy''s developer surface includes authentication, documentation, support, and 7 more developer resources.'
plans:
- name: Idenfy Plans Pricing
  plan_count: 3
  slug: idenfy-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 5
  name: Idenfy Rate Limits
  slug: idenfy-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -1.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.4
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idenfy/refs/heads/main/screenshots/idenfy-2026-06-20T183205.png
security:
- kind: authentication
  name: Idenfy Authentication
  slug: idenfy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Idenfy Domain Security
  slug: idenfy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Idenfy Trust Center
  slug: idenfy-trust-center
  summary_line: ISO 27001, GDPR
slug: idenfy
tags:
- AML
- Compliance
- Fraud Detection
- Identity Verification
- KYB
- KYC
website: https://www.idenfy.com/
---
