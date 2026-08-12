---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Sardine REST API enables real-time fraud detection and compliance across the customer lifecycle. Core API categories include Device APIs for device fingerprinting and behavioral biometrics, Custom
  name: Sardine API
  slug: sardine-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sardine-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sardine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sardine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sardine.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/home
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sardine-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sardineai/
- group: company
  title: ''
  type: Blog
  url: https://www.sardine.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sardine.ai/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sardine.ai/
- group: other
  title: ''
  type: X
  url: https://x.com/sardine
- group: commercial
  title: ''
  type: Plans
  url: plans/sardine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sardine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sardine-finops.yml
created: '2026-06-13'
description: Sardine is an agentic financial crime platform offering fraud prevention, AML compliance, and transaction monitoring through a unified REST API. The platform provides real-time device intelligence, behavior biometrics, transaction risk scoring, KYC/KYB identity verification, AML screening, and chargeback protection for banks, fintechs, and commerce at enterprise scale.
finops:
- name: Sardine Finops
  service_category: ''
  slug: sardine-finops
graphqls:
- description: Sardine provides fraud prevention and compliance for fintech and crypto. The API covers device intelligence, behavioral biometrics, transaction risk scoring, AML screening, KYC verification, and charg
  name: Sardine GraphQL API
  slug: sardine-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sardine.png
jsonld:
- class_count: 31
  name: Sardine Context
  property_count: 1
  slug: sardine-context
layout: provider
modified: '2026-06-13'
name: Sardine
nav: Providers
network: true
overview: 'Sardine publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Prevention, AML, Compliance, KYC, and KYB.


  The Sardine catalog on APIs.io includes 1 JSON-LD context.


  Sardine''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Sardine Plans Pricing
  plan_count: 1
  slug: sardine-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 0
  name: Sardine Rate Limits
  slug: sardine-rate-limits
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sardine/refs/heads/main/screenshots/sardine-2026-06-20T193433.png
security:
- kind: domain-security
  name: Sardine Domain Security
  slug: sardine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sardine Vulnerability Disclosure
  slug: sardine-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Sardine Trust Center
  slug: sardine-trust-center
  summary_line: SOC 2
slug: sardine
tags:
- Fraud Prevention
- AML
- Compliance
- KYC
- KYB
- Device Intelligence
- Behavior Biometrics
- Transaction Risk
- Financial Crime
- Identity Verification
- Chargeback Protection
- FinTech
website: https://www.sardine.ai/
---
