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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: The Authologic Identity API enables businesses to initiate identity verification processes and receive results programmatically. Supports document verification, eID, Bank ID, and biometric liveness ch
  name: Authologic Identity API
  slug: authologic-identity-api
- description: The Authologic AML API enables Anti-Money Laundering screening combined with identity verification in a single integrated flow for KYC/AML compliance.
  name: Authologic AML API
  slug: authologic-aml-api
- description: The Authologic Data Verification API enables verification of personal data against authoritative sources including government databases and credit bureaus.
  name: Authologic Data Verification API
  slug: authologic-data-verification-api
- description: The Authologic Enquiry API enables background checks and identity enquiries against national and international data sources for enhanced due diligence.
  name: Authologic Enquiry API
  slug: authologic-enquiry-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authologic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authologic
- group: company
  title: ''
  type: Website
  url: https://authologic.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.authologic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.authologic.com/docs/developer-documentation/integration-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.authologic.com/docs/developer-documentation/integration-overview
- group: company
  title: ''
  type: Blog
  url: https://authologic.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://authologic.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authologic.com/privacy-policy/
created: '2025-05-02'
description: Authologic is an identity verification platform providing businesses with a single API to aggregate multiple ID verification methods including government-issued digital IDs, Bank IDs, document OCR, liveness checks, and AML screening. It supports seamless KYC/KYB workflow integration for businesses across multiple countries.
features:
- description: One API integration provides access to multiple identity verification methods without separate integrations per provider.
  name: Single API Integration
- description: Native support for government-issued digital IDs and Bank IDs across multiple European countries for high-trust verification.
  name: eID and Bank ID Support
- description: Automated document scanning with OCR and biometric liveness detection to prevent spoofing and fraud.
  name: Document OCR and Liveness
- description: Integrated anti-money laundering screening against sanctions lists, PEP databases, and adverse media sources.
  name: AML Screening
- description: No-integration verification flow using a hosted link for simple verification without technical implementation.
  name: OmniLink
- description: Compose verification workflows from modular steps combining document, biometric, data, and AML checks.
  name: Modular Workflows
finops:
- name: Authologic Finops
  service_category: API
  slug: authologic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authologic.png
layout: provider
modified: '2026-04-19'
name: Authologic
nav: Providers
network: true
overview: 'Authologic publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AML, Digital Identity, eID, Identity Verification, and KYB.


  Authologic''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, signup flow, and 4 more developer resources.'
plans:
- name: Authologic Plans Pricing
  plan_count: 3
  slug: authologic-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Authologic Rate Limits
  slug: authologic-rate-limits
score:
  band: thin
  composite: 30.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 30.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/screenshots/authologic-2026-06-20T172610.png
security:
- kind: domain-security
  name: Authologic Domain Security
  slug: authologic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authologic
solutions:
- description: Complete KYC solution for banks, fintechs, and payment providers with AML screening and document verification.
  name: Financial Services KYC
- description: Aggregate multiple ID verification methods via single API for flexible identity assurance across user populations.
  name: Digital Identity Verification
tags:
- AML
- Digital Identity
- eID
- Identity Verification
- KYB
- KYC
- Liveness Check
use_cases:
- description: Verify customer identities during registration and onboarding for financial services, fintech, and regulated industries.
  name: Customer Onboarding KYC
- description: Combine identity verification with AML screening to meet financial institution compliance requirements.
  name: AML Compliance
- description: Verify business identities and beneficial owners for B2B onboarding and corporate due diligence.
  name: Business Verification (KYB)
- description: Verify user ages using official ID documents for age-restricted products and services.
  name: Age Verification
website: https://authologic.com/
---
