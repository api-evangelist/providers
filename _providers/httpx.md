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
- description: HTTPX is a fully featured HTTP client library for Python 3 with sync and async APIs, HTTP/1.1 and HTTP/2 support. It is consumed as a Python package rather than as a hosted API service.
  name: HTTPX
  slug: httpx
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/httpx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.python-httpx.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.python-httpx.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/encode/httpx
created: '2026-03-27'
description: HTTPX is a fully featured HTTP client for Python 3 with sync and async APIs, HTTP/1.1 and HTTP/2 support. It is broadly compatible with the popular requests library while adding modern features such as strict timeouts, type annotations, direct WSGI and ASGI transport, SSL verification, cookie persistence, proxy support, and multipart uploads.
finops:
- name: Httpx Finops
  service_category: API
  slug: httpx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/httpx.png
layout: provider
modified: '2026-04-28'
name: HTTPX
nav: Providers
network: true
overview: 'HTTPX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Async, Clients, HTTP Client, Library, and Python.


  The HTTPX catalog on APIs.io includes 1 Spectral governance ruleset.


  HTTPX''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Httpx Plans Pricing
  plan_count: 3
  slug: httpx-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Httpx Rate Limits
  slug: httpx-rate-limits
rules:
- name: HTTPX API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: httpx-rules
score:
  band: emerging
  composite: 21.6
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 24.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/httpx/refs/heads/main/screenshots/httpx-2026-06-20T182917.png
security:
- kind: domain-security
  name: Httpx Domain Security
  slug: httpx-domain-security
  summary_line: TLSv1.3
slug: httpx
tags:
- Async
- Clients
- HTTP Client
- Library
- Python
website: https://www.python-httpx.org
---
