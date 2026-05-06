---
aid: apache-jmeter
name: Apache JMeter
description: Apache JMeter is an open-source Java application designed for load testing functional behavior and measuring performance. It supports web applications, REST APIs, databases, LDAP, FTP, and other protocols. Licensed under Apache 2.0 and governed by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Testing
  - Java
  - Load Testing
  - Open Source
  - Performance Testing
  - Stress Testing
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-jmeter/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-jmeter:rest-api
    name: Apache JMeter REST API
    description: The JMeter REST API provides HTTP endpoints for remotely starting, stopping, and monitoring load tests, as well as retrieving test results and status information.
    humanURL: https://jmeter.apache.org/usermanual/remote-test.html
    tags:
      - Performance Testing
      - REST
      - Test Control
    properties:
      - type: Documentation
        url: https://jmeter.apache.org/usermanual/remote-test.html
      - type: OpenAPI
        url: openapi/apache-jmeter-rest-api.yaml
  - aid: apache-jmeter:cli
    name: Apache JMeter CLI
    description: JMeter command-line interface for running load tests in non-GUI mode for CI/CD integration, including options for test plan execution, result reporting, and distributed testing.
    humanURL: https://jmeter.apache.org/usermanual/get-started.html#non_gui
    tags:
      - CLI
      - Performance Testing
    properties:
      - type: Documentation
        url: https://jmeter.apache.org/usermanual/get-started.html#non_gui
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/jmeter
  - type: Documentation
    url: https://jmeter.apache.org/usermanual/
  - type: GettingStarted
    url: https://jmeter.apache.org/usermanual/get-started.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Blog
    url: https://blogs.apache.org/jmeter/
  - type: Versioning
    url: https://jmeter.apache.org/changes.html
  - type: ReleaseNotes
    url: https://jmeter.apache.org/changes.html
  - type: SpectralRules
    url: rules/apache-jmeter-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-jmeter-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/load-test-management.yaml
  - type: Features
    data:
      - name: HTTP Load Testing
        description: Test web applications and REST APIs with configurable thread groups and ramp-up.
      - name: Protocol Support
        description: Support for HTTP, HTTPS, FTP, JDBC, LDAP, SMTP, TCP, and JMS.
      - name: Distributed Testing
        description: Distributed load generation using JMeter remote testing architecture.
      - name: Rich Reporting
        description: Built-in listeners and HTML dashboard reporting for test results.
      - name: Plugin Ecosystem
        description: Extensive plugin marketplace for additional samplers, listeners, and functions.
      - name: CI/CD Integration
        description: Non-GUI mode and REST API for integration with Jenkins, GitHub Actions, and more.
      - name: Assertions
        description: Response assertion engine for functional validation during load tests.
  - type: UseCases
    data:
      - name: API Performance Testing
        description: Measure REST API response times and throughput under load.
      - name: Web Application Load Testing
        description: Simulate concurrent users on web applications to find performance bottlenecks.
      - name: CI/CD Performance Gates
        description: Integrate performance testing into CI/CD pipelines with automated pass/fail criteria.
      - name: Stress Testing
        description: Determine system breaking points through progressive load increase.
  - type: Integrations
    data:
      - name: Jenkins
        description: JMeter Performance Plugin for integrating load tests in Jenkins pipelines.
      - name: GitHub Actions
        description: Run JMeter tests via CLI in GitHub Actions workflows.
      - name: Grafana and InfluxDB
        description: Stream JMeter results to InfluxDB for real-time Grafana dashboards.
      - name: Maven
        description: JMeter Maven Plugin for running tests as part of Maven builds.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
