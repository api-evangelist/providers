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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Gin is a high-performance HTTP web framework for Go that provides a fast and productive way to build microservices and APIs.
  name: Gin
  slug: gin
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gin-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gin-gonic
- group: company
  title: ''
  type: Website
  url: https://gin-gonic.com/
created: '2026-03-26'
description: Gin is a high-performance HTTP web framework for Go that provides a fast and productive way to build microservices and APIs.
finops:
- name: Gin Finops
  service_category: API
  slug: gin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gin.png
json_schemas:
- name: Gin Router and Middleware Configuration
  property_count: 12
  slug: gin-configuration
layout: provider
modified: '2026-04-28'
name: Gin
nav: Providers
network: true
overview: 'Gin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Microservices.


  The Gin catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Gin Plans Pricing
  plan_count: 3
  slug: gin-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Gin Rate Limits
  slug: gin-rate-limits
rules:
- name: Gin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gin-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 9.7
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 26.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gin/refs/heads/main/screenshots/gin-2026-06-20T181824.png
security:
- kind: domain-security
  name: Gin Domain Security
  slug: gin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gin
tags:
- Microservices
website: https://gin-gonic.com/
---
