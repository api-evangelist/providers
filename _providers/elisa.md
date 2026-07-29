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
- description: Programmatic access to ELISA safety certification tools, functional safety resources, and Linux safety analysis APIs.
  name: ELISA API
  slug: elisa-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elisa-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://elisa.tech/resources/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/elisa-tech
- group: company
  title: ''
  type: Blog
  url: https://elisa.tech/feed/
created: '2026-03-16'
description: ELISA (Enabling Linux in Safety Applications) is a Linux Foundation project that creates shared tools and processes to help companies build and certify Linux-based safety-critical applications. It addresses functional safety requirements for automotive, medical, and industrial systems using Linux.
finops:
- name: Elisa Finops
  service_category: API
  slug: elisa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elisa.png
layout: provider
modified: '2026-03-16'
name: ELISA
nav: Providers
network: true
overview: 'ELISA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded, Linux, Linux Foundation, and Safety.


  ELISA''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Elisa Plans Pricing
  plan_count: 3
  slug: elisa-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Elisa Rate Limits
  slug: elisa-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elisa/refs/heads/main/screenshots/elisa-2026-06-20T180611.png
security:
- kind: domain-security
  name: Elisa Domain Security
  slug: elisa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elisa
tags:
- Embedded
- Linux
- Linux Foundation
- Safety
---
