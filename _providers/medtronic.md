---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
- description: The Medtronic API provides access to platform services and data for enterprise integration and automation.
  name: Medtronic API
  slug: medtronic-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medtronic-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Medtronic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medtronic
- group: company
  title: ''
  type: Website
  url: https://www.medtronic.com
- group: company
  title: ''
  type: Blog
  url: https://news.medtronic.com/press-releases?pagetemplate=rss
created: '2026-04-19'
description: Medtronic is a major US corporation and Fortune 1000 company. The Medtronic API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Medtronic Finops
  service_category: Medical Devices / Connected Health
  slug: medtronic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medtronic.png
layout: provider
modified: '2026-04-19'
name: Medtronic
nav: Providers
network: true
overview: 'Medtronic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare and Medical Devices.


  Medtronic''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Medtronic Plans Pricing
  plan_count: 1
  slug: medtronic-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 1
  name: Medtronic Rate Limits
  slug: medtronic-rate-limits
score:
  band: emerging
  composite: 13.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medtronic/refs/heads/main/screenshots/medtronic-2026-06-20T185126.png
security:
- kind: domain-security
  name: Medtronic Domain Security
  slug: medtronic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medtronic
tags:
- Healthcare
- Medical Devices
website: https://www.medtronic.com
---
