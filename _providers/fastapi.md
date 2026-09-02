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
- description: Modern, fast web framework for building APIs with Python based on standard Python type hints.
  name: FastAPI Framework
  slug: fastapi
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastapi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fastapi
- group: company
  title: ''
  type: Website
  url: https://fastapi.tiangolo.com
- group: docs
  title: ''
  type: Documentation
  url: https://fastapi.tiangolo.com
- group: start
  title: ''
  type: GettingStarted
  url: https://fastapi.tiangolo.com/tutorial/
- group: operate
  title: ''
  type: ChangeLog
  url: https://fastapi.tiangolo.com/release-notes/
- group: operate
  title: ''
  type: Support
  url: https://fastapi.tiangolo.com/help-fastapi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiangolo/fastapi
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/VQjSZaeJmf
created: '2024-01-01'
description: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
finops:
- name: Fastapi Finops
  service_category: API
  slug: fastapi-finops
image: https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png
json_schemas:
- name: FastAPI Application Configuration
  property_count: 2
  slug: fastapi-app-config
layout: provider
modified: '2026-04-28'
name: FastAPI
nav: Providers
network: true
overview: 'FastAPI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Async, High Performance, OpenAPI, Pydantic, and Python.


  The FastAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  FastAPI''s developer surface includes documentation, getting-started guide, changelog, support, and 5 more developer resources.'
plans:
- name: Fastapi Plans Pricing
  plan_count: 3
  slug: fastapi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Fastapi Rate Limits
  slug: fastapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FastAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fastapi-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 20.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fastapi/refs/heads/main/screenshots/fastapi-2026-06-20T181048.png
security:
- kind: domain-security
  name: Fastapi Domain Security
  slug: fastapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fastapi
tags:
- Async
- High Performance
- OpenAPI
- Pydantic
- Python
- REST
- Swagger
- Type Hints
- Web Framework
website: https://fastapi.tiangolo.com
---
