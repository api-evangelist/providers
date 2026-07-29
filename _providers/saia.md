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
- description: The Saia Inc API provides access to platform services and data for enterprise integration and automation.
  name: Saia Inc API
  slug: saia-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saia-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saia-inc
- group: company
  title: ''
  type: Website
  url: https://www.saia.com
- group: agent
  title: ''
  type: LlmsText
  url: https://saia.com/llms.txt
created: '2026-04-19'
description: Saia Inc is a major US corporation and Fortune 1000 company. The Saia Inc API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Saia Finops
  service_category: Freight / LTL Carrier
  slug: saia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saia.png
layout: provider
modified: '2026-04-19'
name: Saia Inc
nav: Providers
network: true
overview: Saia Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Freight, Trucking, and Logistics.
plans:
- name: Saia Plans Pricing
  plan_count: 1
  slug: saia-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Saia Rate Limits
  slug: saia-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: -1.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saia/refs/heads/main/screenshots/saia-2026-06-20T193331.png
security:
- kind: domain-security
  name: Saia Domain Security
  slug: saia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saia
tags:
- Freight
- Trucking
- Logistics
website: https://www.saia.com
---
