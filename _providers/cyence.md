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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Partner-gated REST API that exposes Cyence cyber risk analytics — exposure signals, breach-probability and loss estimates, and portfolio accumulation data — for pricing, risk selection, and underwriti
  name: Cyence Cyber Risk API
  slug: cyence-cyber-risk-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.guidewire.com/products/analytics/cyence
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.guidewire.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.guidewire.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.guidewire.com/developers/apis
- group: company
  title: ''
  type: Blog
  url: https://www.guidewire.com/resources/blog
- group: auth
  title: ''
  type: TrustCenter
  url: security/cyence-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.guidewire.com/resources/help-and-support/trust-and-security
created: '2026-07-17'
description: Cyence is a cyber risk analytics and modeling solution — originally an independent InsurTech startup (backed by IVP and others) and acquired by Guidewire in 2017 — that helps insurers, reinsurers, brokers, and managing general agents quantify, underwrite, and manage cyber insurance risk in financial terms. It combines internet-scale data collection, data science, and economic loss modeling to produce exposure signals, breach-probability estimates, and portfolio accumulation and catastrophe scenarios. Cyence data and scores are delivered to carriers through Guidewire Cloud and are available via a REST API for pricing, risk selection, and underwriting workflow automation. API access is partner-gated through a Guidewire account rather than a public self-serve developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyence.png
layout: provider
modified: '2026-07-18'
name: Cyence
nav: Providers
network: true
overview: 'Cyence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Cyber Risk, Insurance, and InsurTech.


  Cyence''s developer surface includes documentation, API reference, engineering blog, and 5 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 17.5
  delta: 1.1
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.4
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Cyence Domain Security
  slug: cyence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cyence Trust Center
  slug: cyence-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, SOC 3, ISO 27001, ISO 27701, PCI DSS
slug: cyence
tags:
- Company
- Cybersecurity
- Cyber Risk
- Insurance
- InsurTech
- Risk Analytics
- Underwriting
- Guidewire
website: https://www.guidewire.com/products/analytics/cyence
---
