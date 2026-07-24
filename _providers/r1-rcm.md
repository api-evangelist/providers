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
api_count: 1
apis:
- description: The R1 RCM API provides access to platform services and data for enterprise integration and automation.
  name: R1 RCM API
  slug: r1-rcm-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/r1-rcm-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/r1-rcm-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/r1-rcm
- group: company
  title: ''
  type: Website
  url: https://www.r1rcm.com
created: '2026-04-19'
description: R1 RCM is a major US corporation and Fortune 1000 company. The R1 RCM API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: R1 Rcm Finops
  service_category: Healthcare Services
  slug: r1-rcm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/r1-rcm.png
layout: provider
modified: '2026-04-19'
name: R1 RCM
nav: Providers
network: true
overview: R1 RCM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Revenue Cycle, and Technology.
plans:
- name: R1 Rcm Plans Pricing
  plan_count: 1
  slug: r1-rcm-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: R1 Rcm Rate Limits
  slug: r1-rcm-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: 1.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/r1-rcm/refs/heads/main/screenshots/r1-rcm-2026-06-20T192500.png
security:
- kind: domain-security
  name: R1 Rcm Domain Security
  slug: r1-rcm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: R1 Rcm Trust Center
  slug: r1-rcm-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: r1-rcm
tags:
- Healthcare
- Revenue Cycle
- Technology
website: https://www.r1rcm.com
---
