---
aid: restful
name: RESTful
description: 'Representational State Transfer (REST) is an architectural style for designing networked applications using stateless HTTP communication and uniform interfaces. RESTful describes systems and APIs that conform to the REST constraints: client-server separation, statelessness, cacheability, layered system, uniform interface, and (optionally) code-on-demand. This index covers the RESTful design paradigm including maturity models, API design patterns, documentation formats, and key reference implementations.'
type: Index
url: https://raw.githubusercontent.com/api-evangelist/restful/refs/heads/main/apis.yml
tags:
  - Architecture
  - HTTP
  - Web Services
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: restful:richardson-maturity-model
    name: Richardson Maturity Model
    description: 'A model by Leonard Richardson that breaks down the maturity of a RESTful API into four levels: Level 0 (The Swamp of POX), Level 1 (Resources), Level 2 (HTTP Verbs), and Level 3 (Hypermedia Controls / HATEOAS). Most modern APIs target Level 2.'
    humanURL: https://martinfowler.com/articles/richardsonMaturityModel.html
    tags:
      - Best Practices
      - Design Patterns
      - Maturity Model
    properties:
      - type: Documentation
        url: https://martinfowler.com/articles/richardsonMaturityModel.html
  - aid: restful:json-api
    name: JSON:API
    description: A specification for building APIs in JSON that standardizes resource representation, relationships, error handling, and metadata. Reduces over-fetching and under-fetching with sparse fieldsets and compound documents.
    humanURL: https://jsonapi.org/
    tags:
      - Hypermedia
      - JSON
      - Standards
    properties:
      - type: Documentation
        url: https://jsonapi.org/format/
      - type: Website
        url: https://jsonapi.org/
  - aid: restful:hal-specification
    name: HAL - Hypertext Application Language
    description: A simple format for including hypermedia links in JSON or XML API responses. HAL uses _links for links and _embedded for embedded resources, providing a consistent way to make REST APIs navigable.
    humanURL: https://stateless.co/hal_specification.html
    tags:
      - Hypermedia
      - JSON
      - Standards
    properties:
      - type: Documentation
        url: https://stateless.co/hal_specification.html
      - type: IETF Draft
        url: https://datatracker.ietf.org/doc/html/draft-kelly-json-hal
  - aid: restful:openapi-specification
    name: OpenAPI Specification
    description: The OpenAPI Specification (OAS) defines a standard, language-agnostic interface for HTTP APIs. OpenAPI 3.x is the most widely-used format for describing RESTful APIs, enabling documentation, code generation, and validation.
    humanURL: https://spec.openapis.org/oas/latest.html
    tags:
      - Documentation
      - Standards
      - Tooling
    properties:
      - type: Specification
        url: https://spec.openapis.org/oas/latest.html
      - type: Website
        url: https://www.openapis.org/
  - aid: restful:http-rfc-9110
    name: RFC 9110 - HTTP Semantics
    description: 'The IETF standard defining HTTP semantics: methods, status codes, header fields, content negotiation, authentication, and request/response message formats. The authoritative reference for RESTful HTTP API design.'
    humanURL: https://datatracker.ietf.org/doc/html/rfc9110
    tags:
      - HTTP
      - RFC
      - Standards
    properties:
      - type: Standard
        url: https://datatracker.ietf.org/doc/html/rfc9110
common:
  - type: Roy Fielding REST Dissertation
    url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
  - type: IANA HTTP Status Codes
    url: https://www.iana.org/assignments/http-status-codes/
  - type: IANA Link Relations
    url: https://www.iana.org/assignments/link-relations/
  - type: RFC 6570 URI Templates
    url: https://datatracker.ietf.org/doc/html/rfc6570
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
