---
aid: restful-web-services
name: RESTful Web Services
description: RESTful web services are web services built using the Representational State Transfer (REST) architectural style, using HTTP as the transport protocol with standard methods to perform CRUD operations on resources. This index covers RESTful web service design patterns, frameworks for building REST services, developer tooling, API testing tools, and best practice guidelines from across the ecosystem.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/restful-web-services/refs/heads/main/apis.yml
tags:
  - Architecture
  - HTTP
  - REST
  - Web Services
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: restful-web-services:postman
    name: Postman API Platform
    description: Industry-leading API development platform for building, testing, documenting, and collaborating on RESTful APIs. Includes API client, collections, environments, mock servers, and automated testing.
    humanURL: https://www.postman.com/
    tags:
      - API Testing
      - Developer Tools
      - Documentation
    properties:
      - type: Documentation
        url: https://learning.postman.com/
      - type: Website
        url: https://www.postman.com/
  - aid: restful-web-services:swagger-openapi
    name: Swagger / OpenAPI
    description: The OpenAPI Specification (formerly Swagger) is the most widely-used standard for describing RESTful APIs. Provides tooling for API design, documentation generation, code generation, and validation.
    humanURL: https://swagger.io/
    tags:
      - API Design
      - Documentation
      - OpenAPI
      - Standards
    properties:
      - type: Documentation
        url: https://swagger.io/docs/
      - type: Specification
        url: https://spec.openapis.org/oas/latest.html
      - type: Website
        url: https://swagger.io/
  - aid: restful-web-services:spring-boot
    name: Spring Boot REST
    description: Java framework from the Spring ecosystem for building production-ready RESTful web services with embedded servers, auto-configuration, and a rich ecosystem of integrations.
    humanURL: https://spring.io/guides/gs/rest-service/
    tags:
      - Frameworks
      - Java
      - Microservices
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/docs/current/reference/html/web.html
      - type: Website
        url: https://spring.io/
  - aid: restful-web-services:fastapi
    name: FastAPI
    description: Modern, high-performance Python web framework for building RESTful APIs based on Python type hints. Automatically generates OpenAPI documentation and supports async operations natively.
    humanURL: https://fastapi.tiangolo.com/
    tags:
      - Frameworks
      - OpenAPI
      - Python
    properties:
      - type: Documentation
        url: https://fastapi.tiangolo.com/
      - type: GitHub
        url: https://github.com/tiangolo/fastapi
      - type: Website
        url: https://fastapi.tiangolo.com/
  - aid: restful-web-services:express
    name: Express.js
    description: Minimal and flexible Node.js web application framework widely used for building RESTful APIs and web services in JavaScript and TypeScript.
    humanURL: https://expressjs.com/
    tags:
      - Frameworks
      - JavaScript
      - Node.js
    properties:
      - type: Documentation
        url: https://expressjs.com/en/4x/api.html
      - type: Website
        url: https://expressjs.com/
common:
  - type: Roy Fielding Dissertation
    url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
  - type: OpenAPI Specification
    url: https://spec.openapis.org/oas/latest.html
  - type: RFC 7231 HTTP Semantics
    url: https://datatracker.ietf.org/doc/html/rfc7231
  - type: RFC 7807 Problem Details
    url: https://datatracker.ietf.org/doc/html/rfc7807
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
