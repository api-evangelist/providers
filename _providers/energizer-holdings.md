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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Energizer Holdings API provides access to platform services and data for enterprise integration and automation.
  name: Energizer Holdings API
  slug: energizer-holdings-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energizer-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energizer
- group: company
  title: ''
  type: Website
  url: https://www.energizer.com
created: '2026-04-19'
description: Energizer Holdings is a major US corporation and Fortune 1000 company. The Energizer Holdings API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Energizer Holdings Finops
  service_category: Consumer Products Integration
  slug: energizer-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energizer-holdings.png
layout: provider
modified: '2026-04-19'
name: Energizer Holdings
nav: Providers
network: true
overview: Energizer Holdings publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Consumer Products and Batteries.
plans:
- name: Energizer Holdings Plans Pricing
  plan_count: 1
  slug: energizer-holdings-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Energizer Holdings Rate Limits
  slug: energizer-holdings-rate-limits
score:
  band: minimal
  composite: 9.3
  delta: -5.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/energizer-holdings/refs/heads/main/screenshots/energizer-holdings-2026-06-20T180707.png
security:
- kind: domain-security
  name: Energizer Holdings Domain Security
  slug: energizer-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: energizer-holdings
tags:
- Consumer Products
- Batteries
website: https://www.energizer.com
---
