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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Spring Cloud Gateway Agentic Access
  operation_count: 9
  slug: spring-cloud-gateway-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 4
apis:
- description: Core routing and filtering capabilities including predicate factories (Path, Host, Method, Header, Query, Cookie, Weight, RemoteAddr), gateway filter factories (AddRequestHeader, RewritePath, RequestR
  name: Spring Cloud Gateway Core
  slug: spring-cloud-gateway-core
- description: Manage global and route filter factories
  name: Spring Cloud Gateway Filters API
  slug: spring-cloud-gateway-filters-api
- description: Query available route predicate factories
  name: Spring Cloud Gateway Predicates API
  slug: spring-cloud-gateway-predicates-api
- description: Manage gateway route definitions at runtime
  name: Spring Cloud Gateway Routes API
  slug: spring-cloud-gateway-routes-api
artifact_total: 18
collections:
- collection_type: open
  name: Spring Cloud Gateway Actuator API
  slug: open-spring-cloud-gateway-actuator
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-cloud-gateway-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-cloud-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-cloud-gateway-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog.atom
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-cloud-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spring-cloud/spring-cloud-gateway
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-cloud
- group: operate
  title: ''
  type: Issues
  url: https://github.com/spring-cloud/spring-cloud-gateway/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-cloud/spring-cloud-gateway/releases
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-cloud-gateway
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-gateway-server
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spring-cloud-gateway-vocabulary.yml
created: '2026-03-16'
description: Spring Cloud Gateway provides an intelligent, programmable router built on Spring WebFlux that serves as the entry point to microservice architectures. It offers routing, predicate evaluation, filter chaining, load balancing, circuit breaking, rate limiting, and runtime route management through an Actuator API.
examples:
- key_count: 6
  name: Spring Cloud Gateway Create Route Example
  slug: spring-cloud-gateway-create-route-example
- key_count: 6
  name: Spring Cloud Gateway List Routes Example
  slug: spring-cloud-gateway-list-routes-example
finops:
- name: Spring Cloud Gateway Finops
  service_category: API
  slug: spring-cloud-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spring-cloud-gateway.png
json_schemas:
- name: Spring Cloud Gateway Route Definition
  property_count: 6
  slug: spring-cloud-gateway-route
json_structures:
- name: Spring Cloud Gateway Route Structure
  property_count: 0
  slug: spring-cloud-gateway-route-structure
jsonld:
- class_count: 6
  name: Spring Cloud Gateway Context
  property_count: 9
  slug: spring-cloud-gateway-context
layout: provider
modified: '2026-05-19'
name: Spring Cloud Gateway
nav: Providers
network: true
overview: 'Spring Cloud Gateway publishes 3 APIs on the [APIs.io](https://apis.io/) network: Filters API, Predicates API, and Routes API. Tagged areas include API Gateway, Circuit Breaker, Load Balancing, Microservices, and Rate Limiting.


  The Spring Cloud Gateway catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Cloud Gateway''s developer surface includes engineering blog, documentation, GitHub presence, release notes, Stack Overflow tag, and 8 more developer resources.'
plans:
- name: Spring Cloud Gateway Plans Pricing
  plan_count: 3
  slug: spring-cloud-gateway-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Spring Cloud Gateway Rate Limits
  slug: spring-cloud-gateway-rate-limits
rules:
- name: Spring Cloud Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spring-cloud-gateway-jsonschema-spectral-rules
- name: Spring Cloud Gateway API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: spring-cloud-gateway-rules
score:
  band: developing
  composite: 47.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.2
    developer_ergonomics: 10.9
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-cloud-gateway/refs/heads/main/screenshots/spring-cloud-gateway-2026-06-20T194410.png
security:
- kind: domain-security
  name: Spring Cloud Gateway Domain Security
  slug: spring-cloud-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Cloud Gateway Vulnerability Disclosure
  slug: spring-cloud-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-cloud-gateway
tags:
- API Gateway
- Circuit Breaker
- Load Balancing
- Microservices
- Rate Limiting
- Routing
- Spring
- Spring WebFlux
website: https://spring.io/projects/spring-cloud-gateway
---
