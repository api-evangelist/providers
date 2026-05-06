---
aid: rest
name: REST
description: REST (Representational State Transfer) is an architectural style for designing networked applications, defined by Roy Fielding in his 2000 doctoral dissertation. REST uses stateless communication, standard HTTP methods (GET, POST, PUT, DELETE, PATCH), and resource-oriented URLs to provide scalable, cacheable, and loosely coupled interfaces. It has become the dominant approach for building web APIs, forming the foundation of modern API design principles and tooling ecosystems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - Architecture
  - HTTP
  - REST
  - RESTful
  - Web Services
url: https://raw.githubusercontent.com/api-evangelist/rest/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rest:rest-architectural-style
    name: REST Architectural Style
    description: 'Representational State Transfer (REST) is an architectural style originally defined by Roy Fielding. REST provides six guiding constraints: client-server separation, statelessness, cacheability, uniform interface, layered system, and optional code-on-demand. Any API conforming to these constraints is considered RESTful.'
    humanURL: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
    tags:
      - Architecture
      - HTTP
      - REST
      - Web Services
    properties:
      - type: Documentation
        url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc7231
  - aid: rest:openapi-specification
    name: OpenAPI Specification
    description: The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand capabilities of a service without access to source code, documentation, or network traffic inspection.
    humanURL: https://spec.openapis.org/oas/latest.html
    tags:
      - API Design
      - API Documentation
      - OpenAPI
      - Specification
    properties:
      - type: Documentation
        url: https://spec.openapis.org/oas/latest.html
      - type: GitHub
        url: https://github.com/OAI/OpenAPI-Specification
  - aid: rest:http-semantics
    name: HTTP Semantics
    description: RFC 9110 defines the semantics of the Hypertext Transfer Protocol (HTTP), the foundation of the World Wide Web and RESTful API communication, including methods, status codes, headers, and content negotiation.
    humanURL: https://www.rfc-editor.org/rfc/rfc9110
    tags:
      - HTTP
      - RFC
      - Semantics
      - Standards
    properties:
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc9110
  - aid: rest:json-api
    name: JSON:API
    description: JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests, built on top of REST principles with conventions for relationships, pagination, filtering, and sparse fieldsets.
    humanURL: https://jsonapi.org
    tags:
      - API Design
      - JSON
      - REST
      - Specification
    properties:
      - type: Documentation
        url: https://jsonapi.org/format/
      - type: GitHub
        url: https://github.com/json-api/json-api
common:
  - type: Website
    url: https://restfulapi.net
  - type: Specification
    url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
  - type: RFC
    url: https://www.rfc-editor.org/rfc/rfc9110
  - type: OpenAPI
    url: https://spec.openapis.org/oas/latest.html
  - type: Tutorials
    url: https://restfulapi.net/rest-api-tutorial/
  - type: GitHub
    url: https://github.com/OAI/OpenAPI-Specification
  - type: Tooling
    url: https://openapi.tools
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rest/refs/heads/main/json-schema/rest-api-schema.json
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rest/refs/heads/main/vocabulary/rest-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
