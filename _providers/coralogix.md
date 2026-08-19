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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.7
  scored_at: '2026-08-19'
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
random_paper: 74
rate_limits:
- limit_count: 5
  name: Coralogix Rate Limits
  slug: coralogix-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Coralogix API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: coralogix-asyncapi-spectral-rules
score:
  band: emerging
  composite: 23.7
  delta: -6.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 45.6
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 30.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
