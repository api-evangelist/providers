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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The HealthEquity API provides access to platform services and data for enterprise integration and automation.
  name: HealthEquity API
  slug: healthequity-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/healthequity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthequity-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/healthequity
- group: company
  title: ''
  type: Website
  url: https://www.healthequity.com
created: '2026-04-19'
description: HealthEquity is a major US corporation and Fortune 1000 company. The HealthEquity API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Healthequity Finops
  service_category: Healthcare Benefits / HSA Custodian Partner API
  slug: healthequity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/healthequity.png
layout: provider
modified: '2026-04-19'
name: HealthEquity
nav: Providers
network: true
overview: HealthEquity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, HSA, and Benefits.
plans:
- name: Healthequity Plans Pricing
  plan_count: 1
  slug: healthequity-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Healthequity Rate Limits
  slug: healthequity-rate-limits
score:
  band: minimal
  composite: 8.7
  delta: -1.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/screenshots/healthequity-2026-07-25T220836.png
security:
- kind: domain-security
  name: Healthequity Domain Security
  slug: healthequity-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Healthequity Vulnerability Disclosure
  slug: healthequity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: healthequity
tags:
- Healthcare
- HSA
- Benefits
website: https://www.healthequity.com
---
