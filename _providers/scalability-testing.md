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
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Scalability Testing Agentic Access
  operation_count: 8
  slug: scalability-testing-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: The Grafana k6 Cloud REST API provides programmatic access to run, manage, and retrieve results for load tests executed on the k6 cloud platform. k6 is an open-source load testing tool using JavaScrip
  name: Grafana k6 Cloud API
  slug: k6-cloud-api
- description: The BlazeMeter REST API provides access to the BlazeMeter cloud load testing platform. BlazeMeter supports JMeter, Gatling, Locust, Selenium, and custom test plans. The API enables test execution, mon
  name: BlazeMeter API
  slug: blazemeter-api
- description: Apache JMeter is the most widely-used open-source load testing tool. It supports HTTP, HTTPS, FTP, JDBC, LDAP, SOAP, REST, and more protocols. JMeter provides a REST API in its distributed mode and in
  name: Apache JMeter
  slug: jmeter
- description: Locust is a scalable, distributed open-source load testing framework written in Python. Test scenarios are defined in pure Python code. Locust exposes a REST API and web UI for controlling test execut
  name: Locust Load Testing
  slug: locust
- description: Gatling is an open-source load testing framework built on Akka and Netty, providing high performance with a Scala/Java/Kotlin DSL for defining test scenarios. The Gatling Enterprise cloud platform pro
  name: Gatling Load Testing
  slug: gatling
- description: The Projects API from Scalability Testing — 4 operation(s) for projects.
  name: Scalability Testing Projects API
  slug: scalability-testing-projects-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grafana Cloud k6 REST Projects API
  slug: open-scalability-testing-projects-api
- collection_type: open
  name: Grafana Cloud k6 REST API
  slug: open-scalability-testing
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scalability-testing-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalability-testing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalability-testing-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://k6.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/grafana/k6
- group: build
  title: ''
  type: GitHub
  url: https://github.com/apache/jmeter
- group: build
  title: ''
  type: GitHub
  url: https://github.com/locustio/locust
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gatling/gatling
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana-cloud/testing/k6/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/scalability-testing-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/scalability-testing-context.jsonld
created: '2024-01-15'
description: A collection of tools, frameworks, APIs, and datasets for performing scalability and load testing of web services, APIs, and distributed systems. Scalability testing evaluates how a system performs as load increases, identifying bottlenecks, capacity limits, and performance degradation points. Key tools include Apache JMeter, k6, Gatling, Locust, and cloud-based platforms like AWS Load Testing, Azure Load Testing, and BlazeMeter.
examples:
- key_count: 4
  name: Scalability Testing K6 Test Result Example
  slug: scalability-testing-k6-test-result-example
finops:
- name: Scalability Testing Finops
  service_category: API
  slug: scalability-testing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalability-testing.png
json_schemas:
- name: LoadTestResult
  property_count: 10
  slug: scalability-testing-test-result
json_structures:
- name: Scalability Testing Test Result Structure
  property_count: 0
  slug: scalability-testing-test-result-structure
jsonld:
- class_count: 5
  name: Scalability Testing Context
  property_count: 22
  slug: scalability-testing-context
layout: provider
modified: '2026-05-02'
name: Scalability Testing
nav: Providers
network: true
overview: 'Scalability Testing publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include API Testing, Load Testing, Performance Testing, Scalability, and Stress Testing.


  The Scalability Testing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scalability Testing''s developer surface includes authentication, GitHub presence, documentation, and 8 more developer resources.'
plans:
- name: Scalability Testing Plans Pricing
  plan_count: 3
  slug: scalability-testing-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Scalability Testing Rate Limits
  slug: scalability-testing-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Scalability Testing API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scalability-testing-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 61.2
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalability-testing/refs/heads/main/screenshots/scalability-testing-2026-06-20T193451.png
security:
- kind: authentication
  name: Scalability Testing Authentication
  slug: scalability-testing-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Scalability Testing Domain Security
  slug: scalability-testing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scalability-testing
tags:
- API Testing
- Load Testing
- Performance Testing
- Scalability
- Stress Testing
website: https://k6.io/
---
