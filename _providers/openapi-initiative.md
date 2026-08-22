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
- description: API for accessing OpenAPI Initiative resources, specifications, and tooling ecosystem documentation for defining standard interfaces to RESTful APIs.
  name: OpenAPI Initiative API
  slug: openapi-initiative-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openapi-initiative-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-api-initiative
- group: docs
  title: ''
  type: Documentation
  url: https://spec.openapis.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/OAI
created: '2026-03-16'
description: The OpenAPI Initiative is a Linux Foundation project that promotes the OpenAPI Specification for defining standard, language-agnostic interfaces to RESTful APIs. It provides governance, tooling ecosystem support, and community collaboration for the most widely adopted API description format.
finops:
- name: Openapi Initiative Finops
  service_category: API
  slug: openapi-initiative-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openapi-initiative.png
layout: provider
modified: '2026-04-28'
name: OpenAPI Initiative
nav: Providers
network: true
overview: 'OpenAPI Initiative publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Linux Foundation, Specifications, and Standards.


  OpenAPI Initiative''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Openapi Initiative Plans Pricing
  plan_count: 3
  slug: openapi-initiative-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Openapi Initiative Rate Limits
  slug: openapi-initiative-rate-limits
score:
  band: emerging
  composite: 11.8
  delta: 0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openapi-initiative/refs/heads/main/screenshots/openapi-initiative-2026-06-20T190907.png
security:
- kind: domain-security
  name: Openapi Initiative Domain Security
  slug: openapi-initiative-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openapi-initiative
tags:
- Linux Foundation
- Specifications
- Standards
---
