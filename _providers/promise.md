---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.promise-pay.com
- group: operate
  title: ''
  type: Support
  url: https://www.promise-pay.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.promise-pay.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promise-pay.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promise-pay.com/privacy-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/promise-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/promise-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/promise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.promise-pay.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/promise-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/promise-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/promise-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.promise-pay.com/security
created: '2026-07-17'
description: Promise is a government payments and relief-technology company (backed by 8vc) that provides AI-powered automation for state and local government agencies and utilities. Its platform helps agencies distribute relief faster and more securely, verify eligibility and income, audit programs for waste, fraud, and abuse, and offer flexible, AI-driven payment plans that recover revenue. Products include PromiseBenefits (relief-program distribution at scale), PromiseAudit (real-time waste/fraud/abuse detection), PromiseVerified (automated income verification), and PromisePay (AI-driven payment plans for utilities and government). Clients include Washington State, Mississippi, WSSC Water, Louisville Water, and Richmond DPU. Promise exposes no public developer API surface; this profile captures its security, compliance, and web presence.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/promise.png
layout: provider
modified: '2026-07-20'
name: Promise
nav: Providers
network: true
overview: 'Promise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Payments, GovTech, and Relief.


  Promise''s developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 23.3
  delta: -0.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 61.1
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 24.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Promise Domain Security
  slug: promise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Promise Vulnerability Disclosure
  slug: promise-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Promise Trust Center
  slug: promise-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, PCI DSS
slug: promise
tags:
- Company
- Government
- Payments
- GovTech
- Relief
- Utilities
- Fraud Detection
- Fintech
website: https://www.promise-pay.com
---
