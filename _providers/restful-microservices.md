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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restful-microservices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://microservices.io/
- group: other
  title: ''
  type: 12 Factor App
  url: https://12factor.net/
- group: other
  title: ''
  type: CNCF Cloud Native Landscape
  url: https://landscape.cncf.io/
- group: docs
  title: ''
  type: Kubernetes Documentation
  url: https://kubernetes.io/docs/
- group: other
  title: ''
  type: Istio Service Mesh
  url: https://istio.io/
- group: other
  title: ''
  type: Kong API Gateway
  url: https://konghq.com/
- group: start
  title: ''
  type: OpenTelemetry
  url: https://opentelemetry.io/
- group: other
  title: ''
  type: Prometheus Monitoring
  url: https://prometheus.io/
- group: other
  title: ''
  type: gRPC Framework
  url: https://grpc.io/
- group: other
  title: ''
  type: Spring Cloud
  url: https://spring.io/cloud
- group: other
  title: ''
  type: Open Liberty RESTful Microservices
  url: https://openliberty.io/docs/latest/rest-microservices.html
created: '2025-01-01'
description: An architectural style that structures an application as a collection of loosely coupled, independently deployable services that communicate via REST APIs using HTTP methods and standard web protocols. This collection covers RESTful microservices patterns, tools, service mesh technologies, API gateways, observability, and the ecosystem of frameworks and platforms for building, deploying, and scaling microservice architectures.
examples:
- key_count: 5
  name: Restful Microservices Inter Service Example
  slug: restful-microservices-inter-service-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restful-microservices.png
json_schemas:
- name: Microservice
  property_count: 12
  slug: restful-microservices-service
json_structures:
- name: Restful Microservices Service Structure
  property_count: 0
  slug: restful-microservices-service-structure
jsonld:
- class_count: 29
  name: Restful Microservices Context
  property_count: 0
  slug: restful-microservices-context
layout: provider
modified: '2026-05-02'
name: RESTful Microservices
nav: Providers
network: true
overview: 'RESTful Microservices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, Distributed Systems, Microservices, REST, and Kubernetes.


  The RESTful Microservices catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 138
rules:
- effective_rule_count: 5
  extends: []
  name: RESTful Microservices API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restful-microservices-jsonschema-spectral-rules
score:
  band: minimal
  composite: 9.0
  delta: -6.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 15.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/restful-microservices/refs/heads/main/screenshots/restful-microservices-2026-06-20T193024.png
security:
- kind: domain-security
  name: Restful Microservices Domain Security
  slug: restful-microservices-domain-security
  summary_line: TLSv1.3
slug: restful-microservices
tags:
- Architecture
- Distributed Systems
- Microservices
- REST
- Kubernetes
- Service Mesh
- Cloud Native
website: https://microservices.io/
---
