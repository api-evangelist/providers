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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Apache Jmeter Agentic Access
  operation_count: 4
  slug: apache-jmeter-agentic-access
  summary_line: 4 operations · 2 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: JMeter command-line interface for running load tests in non-GUI mode for CI/CD integration, including options for test plan execution, result reporting, and distributed testing.
  name: Apache JMeter CLI
  slug: cli
- description: Test results access
  name: Apache JMeter Results API
  slug: apache-jmeter-results-api
- description: Test status and monitoring
  name: Apache JMeter Status API
  slug: apache-jmeter-status-api
- description: Test execution management
  name: Apache JMeter Tests API
  slug: apache-jmeter-tests-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-jmeter-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-jmeter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-jmeter-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/jmeter
- group: docs
  title: ''
  type: Documentation
  url: https://jmeter.apache.org/usermanual/
- group: start
  title: ''
  type: GettingStarted
  url: https://jmeter.apache.org/usermanual/get-started.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: company
  title: ''
  type: Blog
  url: https://blogs.apache.org/jmeter/
- group: design
  title: ''
  type: Versioning
  url: https://jmeter.apache.org/changes.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://jmeter.apache.org/changes.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-jmeter-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-jmeter-vocabulary.yaml
created: '2026-03-16'
description: Apache JMeter is an open-source Java application designed for load testing functional behavior and measuring performance. It supports web applications, REST APIs, databases, LDAP, FTP, and other protocols. Licensed under Apache 2.0 and governed by the Apache Software Foundation.
examples:
- key_count: 8
  name: Rest Api Test Results Example
  slug: rest-api-test-results-example
- key_count: 2
  name: Rest Api Test Run Request Example
  slug: rest-api-test-run-request-example
- key_count: 3
  name: Rest Api Test Run Response Example
  slug: rest-api-test-run-response-example
- key_count: 6
  name: Rest Api Test Status Example
  slug: rest-api-test-status-example
features:
- description: Test web applications and REST APIs with configurable thread groups and ramp-up.
  name: HTTP Load Testing
- description: Support for HTTP, HTTPS, FTP, JDBC, LDAP, SMTP, TCP, and JMS.
  name: Protocol Support
- description: Distributed load generation using JMeter remote testing architecture.
  name: Distributed Testing
- description: Built-in listeners and HTML dashboard reporting for test results.
  name: Rich Reporting
- description: Extensive plugin marketplace for additional samplers, listeners, and functions.
  name: Plugin Ecosystem
- description: Non-GUI mode and REST API for integration with Jenkins, GitHub Actions, and more.
  name: CI/CD Integration
- description: Response assertion engine for functional validation during load tests.
  name: Assertions
finops:
- name: Apache Jmeter Finops
  service_category: API
  slug: apache-jmeter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-jmeter.png
integrations:
- description: JMeter Performance Plugin for integrating load tests in Jenkins pipelines.
  name: Jenkins
- description: Run JMeter tests via CLI in GitHub Actions workflows.
  name: GitHub Actions
- description: Stream JMeter results to InfluxDB for real-time Grafana dashboards.
  name: Grafana and InfluxDB
- description: JMeter Maven Plugin for running tests as part of Maven builds.
  name: Maven
json_schemas:
- name: TestResults
  property_count: 8
  slug: rest-api-test-results
- name: TestRunRequest
  property_count: 2
  slug: rest-api-test-run-request
- name: TestRunResponse
  property_count: 3
  slug: rest-api-test-run-response
- name: TestStatus
  property_count: 6
  slug: rest-api-test-status
json_structures:
- name: Rest Api Test Results Structure
  property_count: 8
  slug: rest-api-test-results-structure
- name: Rest Api Test Run Request Structure
  property_count: 2
  slug: rest-api-test-run-request-structure
- name: Rest Api Test Run Response Structure
  property_count: 3
  slug: rest-api-test-run-response-structure
- name: Rest Api Test Status Structure
  property_count: 6
  slug: rest-api-test-status-structure
jsonld:
- class_count: 4
  name: Apache Jmeter Rest Api Context
  property_count: 15
  slug: apache-jmeter-rest-api-context
layout: provider
modified: '2026-05-19'
name: Apache JMeter
nav: Providers
network: true
overview: 'Apache JMeter publishes 3 APIs on the [APIs.io](https://apis.io/) network: Results API, Status API, and Tests API. Tagged areas include API Testing, Java, Load Testing, Open Source, and Performance Testing.


  The Apache JMeter catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache JMeter''s developer surface includes documentation, getting-started guide, engineering blog, release notes, and 9 more developer resources.'
plans:
- name: Apache Jmeter Plans Pricing
  plan_count: 3
  slug: apache-jmeter-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Apache Jmeter Rate Limits
  slug: apache-jmeter-rate-limits
rules:
- name: Apache JMeter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-jmeter-jsonschema-spectral-rules
- name: Apache JMeter API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 4
  slug: apache-jmeter-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.6
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 50.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-jmeter/refs/heads/main/screenshots/apache-jmeter-2026-06-20T172112.png
security:
- kind: domain-security
  name: Apache Jmeter Domain Security
  slug: apache-jmeter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Jmeter Vulnerability Disclosure
  slug: apache-jmeter-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-jmeter
tags:
- API Testing
- Java
- Load Testing
- Open Source
- Performance Testing
- Stress Testing
use_cases:
- description: Measure REST API response times and throughput under load.
  name: API Performance Testing
- description: Simulate concurrent users on web applications to find performance bottlenecks.
  name: Web Application Load Testing
- description: Integrate performance testing into CI/CD pipelines with automated pass/fail criteria.
  name: CI/CD Performance Gates
- description: Determine system breaking points through progressive load increase.
  name: Stress Testing
---
