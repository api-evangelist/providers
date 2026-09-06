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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spring Boot 3 Agentic Access
  operation_count: 12
  slug: spring-boot-3-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 1
apis:
- description: Core Spring Boot 3 framework providing auto-configuration, embedded server support (Tomcat, Jetty, Undertow), externalized configuration, profiles, and conditional bean registration.
  name: Spring Boot Core Framework
  slug: spring-boot-core-framework
- description: Web MVC framework for building web applications and RESTful services with Spring Boot 3. Includes controllers, filters, interceptors, and content negotiation.
  name: Spring Web MVC API
  slug: spring-web-mvc-api
- description: Automatically expose Spring Data repositories as hypermedia-driven REST resources using HAL. Integrates with Spring Data JPA, MongoDB, Neo4j, and other stores.
  name: Spring Data REST API
  slug: spring-data-rest-api
- description: Security framework for authentication and authorization in Spring Boot 3 applications. Supports OAuth2, OIDC, SAML2, JWT, and method-level security.
  name: Spring Security API
  slug: spring-security-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Application environment properties and configuration
  name: Spring Boot 3 Environment API
  slug: spring-boot-3-environment-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Application and component health indicators
  name: Spring Boot 3 Health API
  slug: spring-boot-3-health-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Application information endpoints
  name: Spring Boot 3 Info API
  slug: spring-boot-3-info-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Logger configuration management
  name: Spring Boot 3 Loggers API
  slug: spring-boot-3-loggers-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Micrometer-based application metrics
  name: Spring Boot 3 Metrics API
  slug: spring-boot-3-metrics-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Scheduled task inspection
  name: Spring Boot 3 Scheduling API
  slug: spring-boot-3-scheduling-api
- baseURL: http://localhost:8080/actuator
  baseurl_source: declared
  description: Thread and heap diagnostics
  name: Spring Boot 3 Threads API
  slug: spring-boot-3-threads-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spring Boot 3 Actuator API
  slug: open-spring-boot-3-actuator
- collection_type: open
  name: Spring Boot 3 Actuator Environment API
  slug: open-spring-boot-3-environment-api
- collection_type: open
  name: Spring Boot 3 Actuator Environment Health API
  slug: open-spring-boot-3-health-api
- collection_type: open
  name: Spring Boot 3 Actuator Environment Info API
  slug: open-spring-boot-3-info-api
- collection_type: open
  name: Spring Boot 3 Actuator Environment Loggers API
  slug: open-spring-boot-3-loggers-api
- collection_type: open
  name: Spring Boot 3 Actuator Environment Metrics API
  slug: open-spring-boot-3-metrics-api
- collection_type: open
  name: Spring Boot 3 Actuator Environment Scheduling API
  slug: open-spring-boot-3-scheduling-api
- collection_type: open
  name: Spring Boot 3 Actuator Environment Threads API
  slug: open-spring-boot-3-threads-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/spring-projects/spring-boot/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spring-projects/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.adoc
- group: commercial
  title: ''
  type: License
  url: https://github.com/spring-projects/spring-boot/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-boot-3-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-boot-3-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-boot-3-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://spring.io/guides/gs/spring-boot/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/spring-projects/spring-boot
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-projects/spring-boot/releases
- group: docs
  title: ''
  type: Migration Guide
  url: https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide
- group: operate
  title: ''
  type: Community
  url: https://spring.io/community
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog
created: '2024-01-15'
description: Spring Boot 3 is the major release of the opinionated Spring application framework, now built on Spring Framework 6, requiring Java 17 baseline and Jakarta EE 10. It delivers native image support via GraalVM, improved observability with Micrometer tracing, and a modernized auto-configuration system. Spring Boot 3 simplifies the development of production-ready stand-alone Spring applications with embedded servers, health endpoints, and externalized configuration.
examples:
- key_count: 2
  name: Spring Boot 3 Get Health Example
  slug: spring-boot-3-get-health-example
- key_count: 2
  name: Spring Boot 3 Get Metric Example
  slug: spring-boot-3-get-metric-example
- key_count: 3
  name: Spring Boot 3 Set Logger Level Example
  slug: spring-boot-3-set-logger-level-example
finops:
- name: Spring Boot 3 Finops
  service_category: Open-Source Framework
  slug: spring-boot-3-finops
json_schemas:
- name: Spring Boot 3 Health Response
  property_count: 2
  slug: spring-boot-3-health
- name: Spring Boot 3 Metric Detail
  property_count: 5
  slug: spring-boot-3-metrics
json_structures:
- name: Spring Boot 3 Actuator Structure
  property_count: 0
  slug: spring-boot-3-actuator-structure
jsonld:
- class_count: 8
  name: Spring Boot 3 Context
  property_count: 24
  slug: spring-boot-3-context
layout: provider
modified: '2026-05-19'
name: Spring Boot 3
nav: Providers
network: true
overview: 'Spring Boot 3 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Environment API, Health API, Info API, and 4 more. Tagged areas include Enterprise, Framework, Java, Microservices, and REST API.


  The Spring Boot 3 catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Boot 3''s developer surface includes getting-started guide, release notes, engineering blog, and 10 more developer resources.'
plans:
- name: Spring Boot 3 Plans Pricing
  plan_count: 2
  slug: spring-boot-3-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Spring Boot 3 Rate Limits
  slug: spring-boot-3-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spring Boot 3 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-boot-3-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Spring Boot 3 API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: spring-boot-3-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 53.3
    developer_ergonomics: 33.3
    discoverability: 63.0
    governance: 13.6
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-boot-3/refs/heads/main/screenshots/spring-boot-3-2026-06-20T194407.png
security:
- kind: domain-security
  name: Spring Boot 3 Domain Security
  slug: spring-boot-3-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Boot 3 Vulnerability Disclosure
  slug: spring-boot-3-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-boot-3
tags:
- Enterprise
- Framework
- Java
- Microservices
- REST API
- Spring Boot
website: https://spring.io/projects/spring-boot
---
