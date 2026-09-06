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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: HTTPX is a fully featured HTTP client library for Python 3 with sync and async APIs, HTTP/1.1 and HTTP/2 support. It is consumed as a Python package rather than as a hosted API service.
  name: HTTPX
  slug: httpx
artifact_total: 6
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/encode/httpx/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/encode/httpx/blob/master/docs/code_of_conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/encode/httpx/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/encode/httpx/blob/master/LICENSE
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


  HTTPX''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Httpx Plans Pricing
  plan_count: 3
  slug: httpx-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Httpx Rate Limits
  slug: httpx-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: HTTPX API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: httpx-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
