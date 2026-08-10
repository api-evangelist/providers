---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Knoll Inc API provides access to platform services and data for enterprise integration and automation.
  name: Knoll Inc API
  slug: knoll-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knoll-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knoll
- group: company
  title: ''
  type: Website
  url: https://www.knoll.com
created: '2026-04-19'
description: Knoll Inc is a major US corporation and Fortune 1000 company. The Knoll Inc API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Knoll Finops
  service_category: Furniture & Manufacturing
  slug: knoll-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knoll.png
layout: provider
modified: '2026-04-19'
name: Knoll Inc
nav: Providers
network: true
overview: Knoll Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Furniture, Design, and Office.
plans:
- name: Knoll Plans Pricing
  plan_count: 1
  slug: knoll-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 1
  name: Knoll Rate Limits
  slug: knoll-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knoll/refs/heads/main/screenshots/knoll-2026-06-20T184112.png
security:
- kind: domain-security
  name: Knoll Domain Security
  slug: knoll-domain-security
  summary_line: TLSv1.3 · DMARC
slug: knoll
tags:
- Furniture
- Design
- Office
website: https://www.knoll.com
---
