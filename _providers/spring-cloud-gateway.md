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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Spring Cloud Gateway Agentic Access
  operation_count: 9
  slug: spring-cloud-gateway-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- description: Core routing and filtering capabilities including predicate factories (Path, Host, Method, Header, Query, Cookie, Weight, RemoteAddr), gateway filter factories (AddRequestHeader, RewritePath, RequestR
  name: Spring Cloud Gateway Core
  slug: spring-cloud-gateway-core
- baseURL: http://localhost:8080/actuator/gateway
  baseurl_source: declared
  description: Manage global and route filter factories
  name: Spring Cloud Gateway Filters API
  slug: spring-cloud-gateway-filters-api
- baseURL: http://localhost:8080/actuator/gateway
  baseurl_source: declared
  description: Query available route predicate factories
  name: Spring Cloud Gateway Predicates API
  slug: spring-cloud-gateway-predicates-api
- baseURL: http://localhost:8080/actuator/gateway
  baseurl_source: declared
  description: Manage gateway route definitions at runtime
  name: Spring Cloud Gateway Routes API
  slug: spring-cloud-gateway-routes-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spring Cloud Gateway Actuator API
  slug: open-spring-cloud-gateway-actuator
- collection_type: open
  name: Spring Cloud Gateway Actuator Filters API
  slug: open-spring-cloud-gateway-filters-api
- collection_type: open
  name: Spring Cloud Gateway Actuator Filters Predicates API
  slug: open-spring-cloud-gateway-predicates-api
- collection_type: open
  name: Spring Cloud Gateway Actuator Filters Routes API
  slug: open-spring-cloud-gateway-routes-api
common:
- group: operate
  title: ''
  type: Support
  url: https://spring.io/support
- group: auth
  title: ''
  type: Security
  url: https://spring.io/security
- group: start
  title: ''
  type: GettingStarted
  url: https://spring.io/quickstart
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


  Spring Cloud Gateway''s developer surface includes support, getting-started guide, engineering blog, documentation, GitHub presence, release notes, Stack Overflow tag, and 9 more developer resources.'
plans:
- name: Spring Cloud Gateway Plans Pricing
  plan_count: 3
  slug: spring-cloud-gateway-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Spring Cloud Gateway Rate Limits
  slug: spring-cloud-gateway-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spring Cloud Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spring-cloud-gateway-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Spring Cloud Gateway API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: spring-cloud-gateway-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 55.3
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
