---
aid: restful-services
name: RESTful Services
description: Representational State Transfer (REST) services are web services built using the REST architectural style, which uses stateless HTTP communication and standard HTTP methods (GET, POST, PUT, DELETE, PATCH) to expose resources. RESTful services are the dominant pattern for modern public APIs and microservices. This index covers the REST architectural style, key design principles, tooling ecosystem, and notable frameworks for building REST services across all technology stacks.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/restful-services/refs/heads/main/apis.yml
tags:
  - Architecture
  - HTTP
  - Microservices
  - REST
  - Web Services
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: restful-services:standards-rest
    name: Standards.REST
    description: A curated collection of standards, conventions, and best practices for building RESTful APIs, including HAL, JSON:API, Siren, Collection+JSON, and HATEOAS patterns.
    humanURL: https://standards.rest/
    tags:
      - Best Practices
      - Standards
    properties:
      - type: Documentation
        url: https://standards.rest/
  - aid: restful-services:zalando-rest-guidelines
    name: Zalando RESTful API and Event Guidelines
    description: Zalando's comprehensive and widely-adopted RESTful API design guidelines, covering naming conventions, HTTP methods, versioning, error handling, pagination, and hypermedia.
    humanURL: https://opensource.zalando.com/restful-api-guidelines/
    tags:
      - Best Practices
      - Guidelines
      - Standards
    properties:
      - type: Documentation
        url: https://opensource.zalando.com/restful-api-guidelines/
  - aid: restful-services:azure-rest-guidelines
    name: Microsoft Azure REST API Guidelines
    description: Microsoft's official REST API design guidelines for Azure services, covering resource naming, versioning, HTTP semantics, long-running operations, and error responses.
    humanURL: https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
    tags:
      - Best Practices
      - Guidelines
      - Microsoft
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
  - aid: restful-services:aws-api-gateway
    name: AWS API Gateway
    description: Amazon Web Services fully managed service for creating, publishing, maintaining, monitoring, and securing REST APIs at any scale.
    humanURL: https://aws.amazon.com/api-gateway/
    tags:
      - AWS
      - Cloud
      - Managed Service
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/
      - type: Website
        url: https://aws.amazon.com/api-gateway/
  - aid: restful-services:google-apigee
    name: Google Apigee API Management
    description: Google Cloud's API management platform for building, managing, and securing RESTful APIs. Provides analytics, developer portal, rate limiting, and policy management.
    humanURL: https://cloud.google.com/apigee
    tags:
      - API Management
      - Cloud
      - Google
    properties:
      - type: Documentation
        url: https://cloud.google.com/apigee/docs
      - type: Website
        url: https://cloud.google.com/apigee
common:
  - type: Documentation
    url: https://restfulapi.net/
  - type: Reference
    url: https://www.w3.org/2001/sw/wiki/REST
  - type: Roy Fielding Dissertation
    url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
  - type: Standards
    url: https://standards.rest/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
