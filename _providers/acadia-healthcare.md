---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Acadia Healthcare API provides access to platform services and data for enterprise integration and automation.
  name: Acadia Healthcare API
  slug: acadia-healthcare-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadia-healthcare-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acadiahealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acadia-healthcare
- group: company
  title: ''
  type: Website
  url: https://www.acadiahealthcare.com
created: '2026-04-19'
description: Acadia Healthcare is a major US corporation and Fortune 1000 company. The Acadia Healthcare API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Acadia Healthcare Finops
  service_category: Behavioral Health Services
  slug: acadia-healthcare-finops
image: /assets/icons/acadia-healthcare.png
layout: provider
modified: '2026-04-19'
name: Acadia Healthcare
nav: Providers
network: true
overview: Acadia Healthcare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health and Mental Health.
plans:
- name: Acadia Healthcare Plans Pricing
  plan_count: 0
  slug: acadia-healthcare-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Acadia Healthcare Rate Limits
  slug: acadia-healthcare-rate-limits
score:
  band: minimal
  composite: 8.1
  delta: -0.1
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acadia-healthcare/refs/heads/main/screenshots/acadia-healthcare-2026-08-07T160746.png
security:
- kind: domain-security
  name: Acadia Healthcare Domain Security
  slug: acadia-healthcare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acadia-healthcare
tags:
- Behavioral Health
- Mental Health
website: https://www.acadiahealthcare.com
---
