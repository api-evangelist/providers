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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: 'A model by Leonard Richardson that breaks down the maturity of a RESTful API into four levels: Level 0 (The Swamp of POX), Level 1 (Resources), Level 2 (HTTP Verbs), and Level 3 (Hypermedia Controls /'
  name: Richardson Maturity Model
  slug: richardson-maturity-model
- description: A specification for building APIs in JSON that standardizes resource representation, relationships, error handling, and metadata. Reduces over-fetching and under-fetching with sparse fieldsets and com
  name: JSON:API
  slug: json-api
- description: A simple format for including hypermedia links in JSON or XML API responses. HAL uses _links for links and _embedded for embedded resources, providing a consistent way to make REST APIs navigable.
  name: HAL - Hypertext Application Language
  slug: hal-specification
- description: The OpenAPI Specification (OAS) defines a standard, language-agnostic interface for HTTP APIs. OpenAPI 3.x is the most widely-used format for describing RESTful APIs, enabling documentation, code gene
  name: OpenAPI Specification
  slug: openapi-specification
- description: 'The IETF standard defining HTTP semantics: methods, status codes, header fields, content negotiation, authentication, and request/response message formats. The authoritative reference for RESTful HTTP'
  name: RFC 9110 - HTTP Semantics
  slug: http-rfc-9110
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restful-domain-security.yml
- group: other
  title: ''
  type: Roy Fielding REST Dissertation
  url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- group: build
  title: ''
  type: IANA HTTP Status Codes
  url: https://www.iana.org/assignments/http-status-codes/
- group: other
  title: ''
  type: IANA Link Relations
  url: https://www.iana.org/assignments/link-relations/
- group: other
  title: ''
  type: RFC 6570 URI Templates
  url: https://datatracker.ietf.org/doc/html/rfc6570
created: '2025-01-01'
description: 'Representational State Transfer (REST) is an architectural style for designing networked applications using stateless HTTP communication and uniform interfaces. RESTful describes systems and APIs that conform to the REST constraints: client-server separation, statelessness, cacheability, layered system, uniform interface, and (optionally) code-on-demand. This index covers the RESTful design paradigm including maturity models, API design patterns, documentation formats, and key reference implementations.'
finops:
- name: Restful Finops
  service_category: API
  slug: restful-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restful.png
json_schemas:
- name: RESTful API Description
  property_count: 10
  slug: restful-api-description
json_structures:
- name: Restful Api Description Structure
  property_count: 0
  slug: restful-api-description-structure
jsonld:
- class_count: 13
  name: Restful Context
  property_count: 7
  slug: restful-context
layout: provider
modified: '2026-05-02'
name: RESTful
nav: Providers
network: true
overview: 'RESTful publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, HTTP, and Web Services.


  The RESTful catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Restful Plans Pricing
  plan_count: 3
  slug: restful-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Restful Rate Limits
  slug: restful-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RESTful API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restful-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 15.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restful/refs/heads/main/screenshots/restful-2026-06-20T193020.png
security:
- kind: domain-security
  name: Restful Domain Security
  slug: restful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: restful
tags:
- Architecture
- HTTP
- Web Services
---
