---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- description: Zenoss is an AIOps and full-stack monitoring platform for hybrid IT infrastructure observability and event management.
  name: Zenoss
  slug: zenoss
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenoss-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenoss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenoss-inc-
- group: company
  title: ''
  type: Website
  url: https://www.zenoss.com
- group: docs
  title: ''
  type: Documentation
  url: https://zenoss.github.io/zenoss-prodbin/
- group: company
  title: ''
  type: Blog
  url: https://www.virtana.com/feed/
created: '2026-03-27'
description: Zenoss is an AIOps and full-stack monitoring platform for hybrid IT infrastructure observability and event management.
finops:
- name: Zenoss Finops
  service_category: API
  slug: zenoss-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenoss.png
layout: provider
modified: '2026-03-27'
name: Zenoss
nav: Providers
network: true
overview: 'Zenoss publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps and Monitoring.


  Zenoss'' developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Zenoss Plans Pricing
  plan_count: 3
  slug: zenoss-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 5
  name: Zenoss Rate Limits
  slug: zenoss-rate-limits
score:
  band: minimal
  composite: 9.1
  delta: -2.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenoss/refs/heads/main/screenshots/zenoss-2026-06-20T201817.png
security:
- kind: domain-security
  name: Zenoss Domain Security
  slug: zenoss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenoss
tags:
- AIOps
- Monitoring
website: https://www.zenoss.com
---
