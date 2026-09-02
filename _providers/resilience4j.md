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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Resilience4j is a lightweight fault tolerance library for Java 17+ using functional programming patterns. It provides six core resilience patterns: Circuit Breaker (prevents cascading failures), Rate '
  name: Resilience4j
  slug: resilience4j
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resilience4j-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resilience4j.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://resilience4j.readme.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://resilience4j.readme.io/docs/getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/resilience4j/resilience4j
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resilience4j
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/resilience4j/resilience4j/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/resilience4j/resilience4j/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/resilience4j/resilience4j/blob/master/LICENSE.txt
- group: other
  title: ''
  type: MavenCentral
  url: https://search.maven.org/search?q=io.github.resilience4j
- group: other
  title: ''
  type: SpringBoot
  url: https://resilience4j.readme.io/docs/getting-started-3
- group: other
  title: ''
  type: Micronaut
  url: https://resilience4j.readme.io/docs/getting-started-4
- group: start
  title: ''
  type: SpringDemo
  url: https://github.com/resilience4j/resilience4j-spring-boot-demo
created: '2026-03-26'
description: Resilience4j is a lightweight fault tolerance library designed for Java 17+ and functional programming, providing higher-order functions to enhance functional interfaces with Circuit Breaker, Rate Limiter, Retry, Bulkhead, TimeLimiter, and Cache patterns. Designed as a replacement for Netflix Hystrix, it integrates with Spring Boot 2 and 3, Micronaut, RxJava, Spring Reactor, Micrometer, Prometheus, and Dropwizard Metrics. Used in production by Deutsche Telekom (400M+ requests/day), PlayStation Network, AOL, and Auto Trader Group.
examples:
- key_count: 5
  name: Resilience4J Circuit Breaker Config Example
  slug: resilience4j-circuit-breaker-config-example
finops:
- name: Resilience4J Finops
  service_category: API
  slug: resilience4j-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resilience4j.png
json_schemas:
- name: Resilience4j Bulkhead Configuration
  property_count: 1
  slug: bulkhead-configuration
- name: Resilience4j Circuit Breaker Configuration
  property_count: 1
  slug: circuit-breaker-configuration
- name: Resilience4j Rate Limiter Configuration
  property_count: 1
  slug: rate-limiter-configuration
- name: Resilience4j Retry Configuration
  property_count: 1
  slug: retry-configuration
- name: Resilience4j Time Limiter Configuration
  property_count: 1
  slug: time-limiter-configuration
json_structures:
- name: Resilience4J Circuit Breaker Structure
  property_count: 0
  slug: resilience4j-circuit-breaker-structure
- name: Resilience4J Retry Structure
  property_count: 0
  slug: resilience4j-retry-structure
jsonld:
- class_count: 26
  name: Resilience4J Context
  property_count: 0
  slug: resilience4j-context
layout: provider
modified: '2026-05-02'
name: Resilience4j
nav: Providers
network: true
overview: 'Resilience4j publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bulkhead, Circuit Breaker, Fault Tolerance, Java, and Microservices.


  The Resilience4j catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Resilience4j''s developer surface includes documentation, getting-started guide, GitHub presence, release notes, and 9 more developer resources.'
plans:
- name: Resilience4J Plans Pricing
  plan_count: 3
  slug: resilience4j-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Resilience4J Rate Limits
  slug: resilience4j-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Resilience4j API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: resilience4j-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 24.0
    developer_ergonomics: 10.7
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 23.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/screenshots/resilience4j-2026-06-20T192943.png
security:
- kind: domain-security
  name: Resilience4J Domain Security
  slug: resilience4j-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resilience4j
tags:
- Bulkhead
- Circuit Breaker
- Fault Tolerance
- Java
- Microservices
- Rate Limiter
- Resilience
- Retry
- Spring Boot
- Functional Programming
website: https://resilience4j.readme.io/
---
