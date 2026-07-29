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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for ingesting entities, instruments, and transaction events into the Unit21 risk and compliance platform. Enables creation and management of alerts, cases, rules, and suspicious activity repo
  name: Unit21 API
  slug: unit21-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/unit21-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unit21-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unit21-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unit21.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unit21.ai/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/u21
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unit21/
- group: company
  title: ''
  type: Blog
  url: https://www.unit21.ai/resources/risk-compliance-blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unit21.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unit21.ai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/unit21inc
- group: operate
  title: ''
  type: Support
  url: https://support.unit21.ai/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.unit21.ai/security
- group: commercial
  title: ''
  type: Plans
  url: plans/unit21-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unit21-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unit21-finops.yml
created: '2026-06-13'
description: Unit21 is an agentic AI platform for fraud and AML (Anti-Money Laundering) detection and compliance operations. It provides a REST API for ingesting transaction data, managing detection rules, reviewing alerts, and filing suspicious activity reports (SARs). The platform supports real-time transaction monitoring, case management, entity and instrument tracking, and automated regulatory filing including SARs, STRs, CTRs, and goAML reports.
finops:
- name: Unit21 Finops
  service_category: ''
  slug: unit21-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unit21.png
jsonld:
- class_count: 0
  name: Unit21 Context
  property_count: 0
  slug: unit21-context
layout: provider
modified: '2026-06-13'
name: Unit21
nav: Providers
network: true
overview: 'Unit21 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Detection, AML, Anti-Money Laundering, Compliance, and FinTech.


  The Unit21 catalog on APIs.io includes 1 JSON-LD context.


  Unit21''s developer surface includes documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Unit21 Plans Pricing
  plan_count: 1
  slug: unit21-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Unit21 Rate Limits
  slug: unit21-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: -2.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 8.1
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 28.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unit21/refs/heads/main/screenshots/unit21-2026-06-20T200036.png
security:
- kind: domain-security
  name: Unit21 Domain Security
  slug: unit21-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unit21 Vulnerability Disclosure
  slug: unit21-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unit21 Trust Center
  slug: unit21-trust-center
  summary_line: SOC 2, GDPR
slug: unit21
tags:
- Fraud Detection
- AML
- Anti-Money Laundering
- Compliance
- FinTech
- Transaction Monitoring
- Risk
- SAR
- Financial Crime
- Suspicious Activity Reports
website: https://www.unit21.ai/
---
