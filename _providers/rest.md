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
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: 'Representational State Transfer (REST) is an architectural style originally defined by Roy Fielding. REST provides six guiding constraints: client-server separation, statelessness, cacheability, unifo'
  name: REST Architectural Style
  slug: rest-architectural-style
- description: The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand capabilities of a service without acce
  name: OpenAPI Specification
  slug: openapi-specification
- description: RFC 9110 defines the semantics of the Hypertext Transfer Protocol (HTTP), the foundation of the World Wide Web and RESTful API communication, including methods, status codes, headers, and content nego
  name: HTTP Semantics
  slug: http-semantics
- description: JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests, built on top of REST principles with conventions f
  name: JSON:API
  slug: json-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restfulapi.net
- group: docs
  title: ''
  type: Specification
  url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- group: other
  title: ''
  type: RFC
  url: https://www.rfc-editor.org/rfc/rfc9110
- group: docs
  title: ''
  type: OpenAPI
  url: https://spec.openapis.org/oas/latest.html
- group: learn
  title: ''
  type: Tutorials
  url: https://restfulapi.net/rest-api-tutorial/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OAI/OpenAPI-Specification
- group: build
  title: ''
  type: Tooling
  url: https://openapi.tools
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rest/refs/heads/main/json-schema/rest-api-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rest/refs/heads/main/vocabulary/rest-vocabulary.yml
created: '2025-01-01'
description: REST (Representational State Transfer) is an architectural style for designing networked applications, defined by Roy Fielding in his 2000 doctoral dissertation. REST uses stateless communication, standard HTTP methods (GET, POST, PUT, DELETE, PATCH), and resource-oriented URLs to provide scalable, cacheable, and loosely coupled interfaces. It has become the dominant approach for building web APIs, forming the foundation of modern API design principles and tooling ecosystems.
finops:
- name: Rest Finops
  service_category: API
  slug: rest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rest.png
json_schemas:
- name: REST API
  property_count: 7
  slug: rest-api
json_structures:
- name: Rest Architecture Structure
  property_count: 0
  slug: rest-architecture-structure
jsonld:
- class_count: 9
  name: Rest Context
  property_count: 5
  slug: rest-context
layout: provider
modified: '2026-05-02'
name: REST
nav: Providers
network: true
overview: 'REST publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Architecture, HTTP, REST, and RESTful.


  The REST catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  REST''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Rest Plans Pricing
  plan_count: 3
  slug: rest-plans-pricing
random_paper: 148
rate_limits:
- limit_count: 5
  name: Rest Rate Limits
  slug: rest-rate-limits
rules:
- name: REST API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rest-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 22.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rest/refs/heads/main/screenshots/rest-2026-06-20T192958.png
security:
- kind: domain-security
  name: Rest Domain Security
  slug: rest-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rest
tags:
- API Design
- Architecture
- HTTP
- REST
- RESTful
- Web Services
website: https://restfulapi.net
---
