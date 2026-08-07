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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The SoFi Technologies API provides access to platform services and data for enterprise integration and automation.
  name: SoFi Technologies API
  slug: sofi-technologies-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sofi-technologies-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sofi-technologies
- group: company
  title: ''
  type: Website
  url: https://www.sofi.com
created: '2026-04-19'
description: SoFi Technologies is a major US corporation and Fortune 1000 company. The SoFi Technologies API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Sofi Technologies Finops
  service_category: Consumer Banking and Lending
  slug: sofi-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sofi-technologies.png
layout: provider
modified: '2026-04-19'
name: SoFi Technologies
nav: Providers
network: true
overview: SoFi Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Personal Finance, and Banking.
plans:
- name: Sofi Technologies Plans Pricing
  plan_count: 1
  slug: sofi-technologies-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Sofi Technologies Rate Limits
  slug: sofi-technologies-rate-limits
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sofi-technologies/refs/heads/main/screenshots/sofi-technologies-2026-06-20T194126.png
security:
- kind: domain-security
  name: Sofi Technologies Domain Security
  slug: sofi-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sofi-technologies
tags:
- Fintech
- Personal Finance
- Banking
website: https://www.sofi.com
---
