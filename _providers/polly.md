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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Polly is a .NET resilience and transient-fault-handling library that allows developers to express resilience strategies such as Retry, Circuit Breaker, Hedging, Timeout, Rate Limiter, and Fallback in '
  name: Polly
  slug: polly
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pollyex
- group: company
  title: ''
  type: Website
  url: https://www.thepollyproject.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.pollydocs.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/App-vNext/Polly
- group: other
  title: ''
  type: NuGet
  url: https://www.nuget.org/packages/Polly
- group: operate
  title: ''
  type: Issues
  url: https://github.com/App-vNext/Polly/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/App-vNext/Polly/releases
created: '2026-03-26'
description: Polly is a .NET resilience and transient-fault-handling library that allows developers to express resilience strategies such as Retry, Circuit Breaker, Hedging, Timeout, Rate Limiter, and Fallback in a fluent and thread-safe manner. A .NET Foundation member project.
finops:
- name: Polly Finops
  service_category: API
  slug: polly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polly.png
json_schemas:
- name: Polly Resilience Pipeline Configuration
  property_count: 1
  slug: resilience-pipeline-configuration
layout: provider
modified: '2026-03-26'
name: Polly
nav: Providers
network: true
overview: 'Polly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, C#, Circuit Breaker, Fault Tolerance, and Microservices.


  The Polly catalog on APIs.io includes 1 Spectral governance ruleset.


  Polly''s developer surface includes documentation, GitHub presence, release notes, and 5 more developer resources.'
plans:
- name: Polly Plans Pricing
  plan_count: 3
  slug: polly-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Polly Rate Limits
  slug: polly-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Polly API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: polly-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 17.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polly/refs/heads/main/screenshots/polly-2026-06-20T191856.png
security:
- kind: domain-security
  name: Polly Domain Security
  slug: polly-domain-security
  summary_line: TLSv1.3
slug: polly
tags:
- .NET
- C#
- Circuit Breaker
- Fault Tolerance
- Microservices
- Rate Limiter
- Resilience
- Retry
- Timeout
website: https://www.thepollyproject.org
---
