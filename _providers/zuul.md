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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Netflix Zuul is a gateway service that provides dynamic routing, monitoring, resiliency, and security.
  name: Netflix Zuul
  slug: zuul
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/Netflix/zuul
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Netflix/zuul/wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netflix
created: '2026-03-27'
description: Netflix Zuul is a JVM-based API gateway providing dynamic routing, monitoring, resiliency, and security for microservice architectures.
finops:
- name: Zuul Finops
  service_category: API
  slug: zuul-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zuul.png
layout: provider
modified: '2026-03-27'
name: Netflix Zuul
nav: Providers
network: true
overview: 'Netflix Zuul publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, Microservices, and Netflix.


  Netflix Zuul''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Zuul Plans Pricing
  plan_count: 3
  slug: zuul-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Zuul Rate Limits
  slug: zuul-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 4
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zuul/refs/heads/main/screenshots/zuul-2026-06-20T202005.png
slug: zuul
tags:
- API Gateway
- Microservices
- Netflix
---
