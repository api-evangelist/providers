---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restful-apis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restfulapi.net/
- group: docs
  title: ''
  type: OpenAPI Specification
  url: https://spec.openapis.org/oas/latest.html
- group: other
  title: ''
  type: RFC 7231 HTTP Semantics
  url: https://datatracker.ietf.org/doc/html/rfc7231
- group: other
  title: ''
  type: Roy Fielding REST Dissertation
  url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- group: other
  title: ''
  type: Richardson Maturity Model
  url: https://martinfowler.com/articles/richardsonMaturityModel.html
- group: auth
  title: ''
  type: OWASP API Security Top 10
  url: https://owasp.org/www-project-api-security/
- group: docs
  title: ''
  type: JSON API Specification
  url: https://jsonapi.org/
- group: docs
  title: ''
  type: HAL Specification
  url: https://stateless.group/hal_specification.html
- group: docs
  title: ''
  type: Swagger Tools
  url: https://swagger.io/tools/
- group: build
  title: ''
  type: Postman REST Client
  url: https://www.postman.com/
created: '2025-01-01'
description: Representational State Transfer (REST) is an architectural style for designing networked applications. RESTful APIs use HTTP methods to perform CRUD operations and communicate between client and server using stateless, cacheable requests with standard conventions. This collection covers RESTful API design principles, best practices, standards, tools, and the OpenAPI Specification ecosystem.
examples:
- key_count: 4
  name: Restful Apis Crud Example
  slug: restful-apis-crud-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restful-apis.png
json_schemas:
- name: RESTful API Error
  property_count: 7
  slug: restful-apis-error
- name: RESTful API Resource
  property_count: 6
  slug: restful-apis-resource
json_structures:
- name: Restful Apis Resource Structure
  property_count: 0
  slug: restful-apis-resource-structure
jsonld:
- class_count: 30
  name: Restful Apis Context
  property_count: 0
  slug: restful-apis-context
layout: provider
modified: '2026-05-02'
name: RESTful APIs
nav: Providers
network: true
overview: 'RESTful APIs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, HTTP, REST, Web Services, and OpenAPI.


  The RESTful APIs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 12
rules:
- name: RESTful APIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: restful-apis-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 15.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restful-apis/refs/heads/main/screenshots/restful-apis-2026-06-20T193024.png
security:
- kind: domain-security
  name: Restful Apis Domain Security
  slug: restful-apis-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: restful-apis
tags:
- Architecture
- HTTP
- REST
- Web Services
- OpenAPI
- Standards
- Design
website: https://restfulapi.net/
---
