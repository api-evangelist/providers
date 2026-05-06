---
aid: jakarta-ee
name: Jakarta EE
description: Jakarta EE is the open source successor to Java EE, providing a set of specifications for enterprise Java development. Jakarta EE is developed under the Eclipse Foundation and includes specifications for web services, messaging, persistence, security, and other enterprise computing needs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise
  - Jakarta EE
  - Java
  - Standards
url: https://raw.githubusercontent.com/api-evangelist/jakarta-ee/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jakarta-ee:jakarta-restful-web-services
    name: Jakarta RESTful Web Services
    description: Jakarta RESTful Web Services (formerly JAX-RS) is the API specification for developing web services that follow the REST architectural pattern. It defines a set of Java APIs and annotations that enable the development and deployment of RESTful web services on the Jakarta EE platform.
    humanURL: https://jakarta.ee/specifications/restful-ws/
    tags:
      - REST
      - Specification
      - Web Services
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/restful-ws/
      - type: GitHubRepository
        url: https://github.com/jakartaee/rest
  - aid: jakarta-ee:jakarta-json-processing
    name: Jakarta JSON Processing
    description: Jakarta JSON Processing (formerly JSON-P) provides an API to parse, generate, transform, and query JSON documents. It includes a streaming API similar to StAX and an object model API similar to DOM for working with JSON data in Jakarta EE applications.
    humanURL: https://jakarta.ee/specifications/jsonp/
    tags:
      - JSON
      - Parsing
      - Specification
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/jsonp/
      - type: GitHubRepository
        url: https://github.com/jakartaee/jsonp-api
  - aid: jakarta-ee:jakarta-json-binding
    name: Jakarta JSON Binding
    description: Jakarta JSON Binding (formerly JSON-B) is a binding framework for converting Java objects to and from JSON documents. It provides a default mapping between classes and JSON, with the ability to customize the mapping process through a comprehensive configuration API.
    humanURL: https://jakarta.ee/specifications/jsonb/
    tags:
      - Binding
      - JSON
      - Specification
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/jsonb/
      - type: GitHubRepository
        url: https://github.com/jakartaee/jsonb-api
  - aid: jakarta-ee:jakarta-websocket
    name: Jakarta WebSocket
    description: Jakarta WebSocket defines a standard API for creating server and client endpoints that communicate using the WebSocket protocol (RFC 6455). It enables full-duplex, bidirectional communication between clients and servers over a single TCP connection in Jakarta EE applications.
    humanURL: https://jakarta.ee/specifications/websocket/
    tags:
      - Specification
      - Streaming
      - WebSocket
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/websocket/
      - type: GitHubRepository
        url: https://github.com/jakartaee/websocket
  - aid: jakarta-ee:jakarta-servlet
    name: Jakarta Servlet
    description: Jakarta Servlet is a server-side Java API for handling HTTP requests and generating dynamic responses. It provides the foundational programming model for Java-based web applications and underpins many other Jakarta EE web technologies including RESTful Web Services and WebSocket.
    humanURL: https://jakarta.ee/specifications/servlet/
    tags:
      - HTTP
      - Specification
      - Web
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/servlet/
      - type: GitHubRepository
        url: https://github.com/jakartaee/servlet
  - aid: jakarta-ee:jakarta-validation
    name: Jakarta Validation
    description: Jakarta Validation (formerly Bean Validation) provides an object-level constraint declaration and validation facility through annotations and a runtime API. It is widely used to validate inputs in REST endpoints, persistence entities, and other Jakarta EE components.
    humanURL: https://jakarta.ee/specifications/bean-validation/
    tags:
      - Specification
      - Validation
    properties:
      - type: Documentation
        url: https://jakarta.ee/specifications/bean-validation/
      - type: GitHubRepository
        url: https://github.com/jakartaee/validation
common:
  - type: Website
    url: https://jakarta.ee/
  - type: Specifications
    url: https://jakarta.ee/specifications/
  - type: Documentation
    url: https://jakarta.ee/learn/
  - type: GitHub Organization
    url: https://github.com/jakartaee
  - type: News
    url: https://jakarta.ee/news/
  - type: Community
    url: https://jakarta.ee/community/
  - type: Eclipse Foundation
    url: https://www.eclipse.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
