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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Coralogix is an observability platform providing log analytics, metrics, tracing, and AI-powered insights.
  name: Coralogix
  slug: coralogix
artifact_total: 7
asyncapis:
- description: AsyncAPI description of Coralogix's publicly documented streaming and event-driven surfaces. This document covers only what Coralogix publishes in https://coralogix.com/docs/ and does not enumerate un
  name: Coralogix Streaming Surfaces
  slug: coralogix-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coralogix-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coralogix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coralogix
- group: company
  title: ''
  type: Website
  url: https://coralogix.com
- group: docs
  title: ''
  type: Documentation
  url: https://coralogix.com/docs
- group: company
  title: ''
  type: Blog
  url: https://coralogix.com/feed/
created: '2026-03-27'
description: Coralogix is an observability platform providing log analytics, metrics, tracing, and AI-powered insights.
finops:
- name: Coralogix Finops
  service_category: API
  slug: coralogix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coralogix.png
layout: provider
modified: '2026-05-29'
name: Coralogix
nav: Providers
network: true
overview: 'Coralogix publishes 1 API on the [APIs.io](https://apis.io/) network: Coralogix. Tagged areas include AIOps and Observability.


  The Coralogix catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Coralogix''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Coralogix Plans Pricing
  plan_count: 3
  slug: coralogix-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Coralogix Rate Limits
  slug: coralogix-rate-limits
rules:
- name: Coralogix API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: coralogix-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.1
  delta: 4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.6
    developer_ergonomics: 10.9
    discoverability: 40.7
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 33.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/screenshots/coralogix-2026-06-20T175022.png
security:
- kind: domain-security
  name: Coralogix Domain Security
  slug: coralogix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coralogix
tags:
- AIOps
- Observability
website: https://coralogix.com
---
