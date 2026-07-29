---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spring Agentic Access
  operation_count: 17
  slug: spring-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 14
apis:
- description: Spring Data REST automatically exports Spring Data repository interfaces as RESTful hypermedia-driven APIs using HAL (Hypertext Application Language). It enables CRUD operations on domain entities thr
  name: Spring Data REST API
  slug: spring-data-rest-api
- description: 'Spring Cloud Gateway provides an API Gateway built on Spring WebFlux and Reactor. It offers route configuration, request/response filtering, load balancing, circuit breaking, rate limiting, and retry '
  name: Spring Cloud Gateway API
  slug: spring-cloud-gateway-api
- description: Spring Authorization Server provides a full OAuth 2.1 and OpenID Connect 1.0 authorization server implementation built on Spring Security. It supports authorization code flow, client credentials, devi
  name: Spring Authorization Server API
  slug: spring-authorization-server-api
- description: Spring AI provides a Spring-friendly API and abstractions for building AI-powered applications. It offers a unified ChatClient API for interacting with AI models (OpenAI, Anthropic, Google Gemini, Oll
  name: Spring AI API
  slug: spring-ai-api
- description: Spring application context beans
  name: Spring Framework Beans API
  slug: spring-beans-api
- description: Environment properties and configuration
  name: Spring Framework Environment API
  slug: spring-environment-api
- description: Application health status and component health details
  name: Spring Framework Health API
  slug: spring-health-api
- description: Application information and build metadata
  name: Spring Framework Info API
  slug: spring-info-api
- description: Application logger configuration
  name: Spring Framework Loggers API
  slug: spring-loggers-api
- description: HTTP request handler mappings
  name: Spring Framework Mappings API
  slug: spring-mappings-api
- description: Discover available project options and capabilities
  name: Spring Framework Metadata API
  slug: spring-metadata-api
- description: Application performance and operational metrics
  name: Spring Framework Metrics API
  slug: spring-metrics-api
- description: Generate new Spring Boot project archives
  name: Spring Framework Project Generation API
  slug: spring-project-generation-api
- description: Thread dump and virtual thread information
  name: Spring Framework Threads API
  slug: spring-threads-api
artifact_total: 31
collections:
- collection_type: open
  name: Spring Boot Actuator API
  slug: open-spring-boot-actuator
- collection_type: open
  name: Spring Initializr API
  slug: open-spring-initializr-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spring-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spring.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spring-projects
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog
- group: operate
  title: ''
  type: Community
  url: https://spring.io/community
- group: docs
  title: ''
  type: Guides
  url: https://spring.io/guides
- group: other
  title: ''
  type: Events
  url: https://spring.io/events
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-projects/spring-framework/releases
created: '2026-05-02'
description: Spring is the leading open-source application framework for Java. The Spring ecosystem provides a comprehensive programming and configuration model for modern Java-based enterprise applications, covering web MVC, data access, security, messaging, cloud-native patterns, and AI integrations. Spring Boot enables rapid application development with embedded servers and auto-configuration. Spring is maintained by VMware and hosted under the Spring Projects GitHub organization.
examples:
- key_count: 4
  name: Spring Actuator Health Example
  slug: spring-actuator-health-example
- key_count: 4
  name: Spring Initializr Generate Example
  slug: spring-initializr-generate-example
finops:
- name: Spring Finops
  service_category: Open-Source Framework
  slug: spring-finops
image: https://spring.io/img/spring-logo.svg
json_schemas:
- name: Spring Boot Actuator Health Response
  property_count: 2
  slug: spring-actuator-health
- name: Spring Boot Application
  property_count: 12
  slug: spring-boot-application
json_structures:
- name: Spring Boot Application Structure
  property_count: 0
  slug: spring-boot-application-structure
jsonld:
- class_count: 23
  name: Spring Context
  property_count: 6
  slug: spring-context
layout: provider
modified: '2026-05-19'
name: Spring Framework
nav: Providers
network: true
overview: 'Spring Framework publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Beans API, Environment API, Health API, and 7 more. Tagged areas include AI, Cloud Native, Enterprise, Framework, and Java.


  The Spring Framework catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Framework''s developer surface includes authentication, GitHub presence, documentation, engineering blog, release notes, and 8 more developer resources.'
plans:
- name: Spring Plans Pricing
  plan_count: 2
  slug: spring-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Spring Rate Limits
  slug: spring-rate-limits
rules:
- name: Spring Framework API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-jsonschema-spectral-rules
- name: Spring Framework API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 8
  slug: spring-rules
score:
  band: developing
  composite: 46.7
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.7
    developer_ergonomics: 26.1
    discoverability: 63.0
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring/refs/heads/main/screenshots/spring-2026-06-20T194402.png
security:
- kind: authentication
  name: Spring Authentication
  slug: spring-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spring Domain Security
  slug: spring-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Vulnerability Disclosure
  slug: spring-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring
tags:
- AI
- Cloud Native
- Enterprise
- Framework
- Java
- Microservices
- Open Source
- REST
- Spring Boot
website: https://spring.io
---
