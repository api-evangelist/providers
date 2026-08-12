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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Ennis Inc API provides access to platform services and data for enterprise integration and automation.
  name: Ennis Inc API
  slug: ennis-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ennis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ennis.com
- group: agent
  title: ''
  type: LlmsText
  url: https://ennis.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.ennis.com/feed/
created: '2026-04-19'
description: Ennis Inc is a major US corporation and Fortune 1000 company. The Ennis Inc API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Ennis Finops
  service_category: Print & Forms Integration
  slug: ennis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ennis.png
layout: provider
modified: '2026-04-19'
name: Ennis Inc
nav: Providers
network: true
overview: 'Ennis Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Forms, Printing, and Promotional.


  Ennis Inc''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Ennis Plans Pricing
  plan_count: 1
  slug: ennis-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Ennis Rate Limits
  slug: ennis-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: -4.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ennis/refs/heads/main/screenshots/ennis-2026-06-20T180720.png
security:
- kind: domain-security
  name: Ennis Domain Security
  slug: ennis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ennis
tags:
- Business Forms
- Printing
- Promotional
website: https://www.ennis.com
---
