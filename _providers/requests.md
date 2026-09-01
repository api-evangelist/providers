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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Requests is a simple and elegant HTTP library for Python, designed for human beings. It provides a clean, human-friendly API for all standard HTTP methods with automatic content handling, authenticati
  name: Requests
  slug: requests
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/requests-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://requests.readthedocs.io
- group: docs
  title: ''
  type: Documentation
  url: https://requests.readthedocs.io/en/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/psf/requests
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/requests/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-schema/requests-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-schema/requests-response-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-structure/requests-response-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/json-ld/requests-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/examples/requests-get-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/examples/requests-post-example.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/vocabulary/requests-vocabulary.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://requests.readthedocs.io/en/latest/community/updates/
created: '2026-03-27'
description: 'Requests is a simple and elegant HTTP library for Python, designed for human beings. Published under the Apache2 license by the Python Software Foundation (PSF), it is one of the most downloaded Python packages with approximately 300 million weekly downloads and over 4 million dependent repositories. Requests abstracts urllib3 to provide idiomatic HTTP method functions (get, post, put, patch, delete, head, options), persistent Sessions with connection pooling, automatic content decompression, TLS/SSL verification, Basic and Digest authentication, cookie persistence, streaming downloads, multipart file uploads, SOCKS proxy support, and configurable timeouts. Current stable version: 2.33.1 (March 2026). Supports Python 3.10+.'
examples:
- key_count: 3
  name: Requests Get Example
  slug: requests-get-example
- key_count: 3
  name: Requests Post Example
  slug: requests-post-example
finops:
- name: Requests Finops
  service_category: API
  slug: requests-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/requests.png
json_schemas:
- name: Requests Request
  property_count: 15
  slug: requests-request
- name: Requests Response
  property_count: 13
  slug: requests-response
json_structures:
- name: Requests Response Structure
  property_count: 0
  slug: requests-response-structure
jsonld:
- class_count: 13
  name: Requests Context
  property_count: 12
  slug: requests-context
layout: provider
modified: '2026-05-02'
name: Requests
nav: Providers
network: true
overview: 'Requests publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clients, HTTP Client, HTTP Library, Open-Source, and Python.


  The Requests catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Requests'' developer surface includes documentation, code examples, changelog, and 10 more developer resources.'
plans:
- name: Requests Plans Pricing
  plan_count: 3
  slug: requests-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Requests Rate Limits
  slug: requests-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Requests API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: requests-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 21.3
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 25.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/requests/refs/heads/main/screenshots/requests-2026-06-20T192923.png
security:
- kind: domain-security
  name: Requests Domain Security
  slug: requests-domain-security
  summary_line: TLSv1.3 · HSTS
slug: requests
tags:
- Clients
- HTTP Client
- HTTP Library
- Open-Source
- Python
- Python Software Foundation
website: https://requests.readthedocs.io
---
