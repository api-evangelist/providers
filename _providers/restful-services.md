---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
api_count: 5
apis:
- description: A curated collection of standards, conventions, and best practices for building RESTful APIs, including HAL, JSON:API, Siren, Collection+JSON, and HATEOAS patterns.
  name: Standards.REST
  slug: standards-rest
- description: Zalando's comprehensive and widely-adopted RESTful API design guidelines, covering naming conventions, HTTP methods, versioning, error handling, pagination, and hypermedia.
  name: Zalando RESTful API and Event Guidelines
  slug: zalando-rest-guidelines
- description: Microsoft's official REST API design guidelines for Azure services, covering resource naming, versioning, HTTP semantics, long-running operations, and error responses.
  name: Microsoft Azure REST API Guidelines
  slug: azure-rest-guidelines
- description: Amazon Web Services fully managed service for creating, publishing, maintaining, monitoring, and securing REST APIs at any scale.
  name: AWS API Gateway
  slug: aws-api-gateway
- description: Google Cloud's API management platform for building, managing, and securing RESTful APIs. Provides analytics, developer portal, rate limiting, and policy management.
  name: Google Apigee API Management
  slug: google-apigee
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/restful-services/plans/restful-services-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/restful-services-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/restful-services/rate-limits/restful-services-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/restful-services-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/restful-services/finops/restful-services-finops.yml
  title: ''
  type: FinOps
  url: finops/restful-services-finops.yml
- group: auth
  href: https://artifacts.apis.io/restful-services/security/restful-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/restful-services-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://restfulapi.net/
- group: docs
  title: ''
  type: Reference
  url: https://www.w3.org/2001/sw/wiki/REST
- group: other
  title: ''
  type: Roy Fielding Dissertation
  url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- group: other
  title: ''
  type: Standards
  url: https://standards.rest/
created: '2025-01-01'
description: Representational State Transfer (REST) services are web services built using the REST architectural style, which uses stateless HTTP communication and standard HTTP methods (GET, POST, PUT, DELETE, PATCH) to expose resources. RESTful services are the dominant pattern for modern public APIs and microservices. This index covers the REST architectural style, key design principles, tooling ecosystem, and notable frameworks for building REST services across all technology stacks.
finops:
- has_sources: false
  method: generated
  name: Restful Services Finops
  primary_unit: request
  service_category: API
  slug: restful-services-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restful-services.png
json_schemas:
- name: REST Error Response
  property_count: 6
  slug: restful-services-error
- name: REST Resource
  property_count: 6
  slug: restful-services-resource
json_structures:
- name: Restful Services Resource Structure
  property_count: 0
  slug: restful-services-resource-structure
jsonld:
- class_count: 13
  name: Restful Services Context
  property_count: 9
  slug: restful-services-context
layout: provider
modified: '2026-05-02'
name: RESTful Services
nav: Providers
network: true
overview: 'RESTful Services is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, HTTP, Microservices, REST, and Web Services.


  The RESTful Services catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RESTful Services'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Restful Services Plans Pricing
  plan_count: 3
  slug: restful-services-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Restful Services Rate Limits
  slug: restful-services-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: RESTful Services — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restful-services-jsonschema-spectral-rules
screenshot: https://apis.io/screenshots/restful-services/restful-services-2026-06-20T193027.png
security:
- kind: domain-security
  name: Restful Services Domain Security
  slug: restful-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: restful-services
tags:
- Architecture
- HTTP
- Microservices
- REST
- Web Services
---
