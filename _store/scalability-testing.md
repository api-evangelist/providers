---
aid: scalability-testing
name: Scalability Testing
description: A collection of tools, frameworks, APIs, and datasets for performing scalability and load testing of web services, APIs, and distributed systems. Scalability testing evaluates how a system performs as load increases, identifying bottlenecks, capacity limits, and performance degradation points. Key tools include Apache JMeter, k6, Gatling, Locust, and cloud-based platforms like AWS Load Testing, Azure Load Testing, and BlazeMeter.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Testing
  - Load Testing
  - Performance Testing
  - Scalability
  - Stress Testing
url: https://raw.githubusercontent.com/api-evangelist/scalability-testing/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scalability-testing:k6-cloud-api
    name: Grafana k6 Cloud API
    description: The Grafana k6 Cloud REST API provides programmatic access to run, manage, and retrieve results for load tests executed on the k6 cloud platform. k6 is an open-source load testing tool using JavaScript/TypeScript test scripts. The cloud platform adds distributed execution, real-time results, and team collaboration features.
    humanURL: https://grafana.com/docs/grafana-cloud/testing/k6/
    baseURL: https://api.k6.io/v3
    tags:
      - k6
      - Load Testing
      - Performance Testing
    properties:
      - type: Documentation
        url: https://grafana.com/docs/grafana-cloud/testing/k6/reference/rest-api/
  - aid: scalability-testing:blazemeter-api
    name: BlazeMeter API
    description: The BlazeMeter REST API provides access to the BlazeMeter cloud load testing platform. BlazeMeter supports JMeter, Gatling, Locust, Selenium, and custom test plans. The API enables test execution, monitoring, result retrieval, and configuration management.
    humanURL: https://guide.blazemeter.com/hc/en-us/categories/200698715-BlazeMeter-API
    baseURL: https://a.blazemeter.com/api/v4
    tags:
      - BlazeMeter
      - JMeter
      - Load Testing
    properties:
      - type: Documentation
        url: https://guide.blazemeter.com/hc/en-us/categories/200698715-BlazeMeter-API
  - aid: scalability-testing:azure-load-testing
    name: Azure Load Testing API
    description: Azure Load Testing is a fully managed cloud service that enables running high-scale load tests. Based on Apache JMeter, it provides a REST API for creating, running, and analyzing load tests integrated with Azure DevOps and GitHub Actions CI/CD pipelines.
    humanURL: https://learn.microsoft.com/en-us/azure/load-testing/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService
    tags:
      - Azure
      - Cloud Load Testing
      - JMeter
      - Microsoft
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/load-testing/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/loadtestservice/resource-manager/Microsoft.LoadTestService/stable/2022-12-01/loadtestservice.json
  - aid: scalability-testing:jmeter
    name: Apache JMeter
    description: Apache JMeter is the most widely-used open-source load testing tool. It supports HTTP, HTTPS, FTP, JDBC, LDAP, SOAP, REST, and more protocols. JMeter provides a REST API in its distributed mode and integrates with BlazeMeter, Azure Load Testing, and other cloud platforms for scaled execution.
    humanURL: https://jmeter.apache.org/
    tags:
      - Apache
      - JMeter
      - Load Testing
      - Open Source
    properties:
      - type: Documentation
        url: https://jmeter.apache.org/usermanual/index.html
      - type: GitHub
        url: https://github.com/apache/jmeter
  - aid: scalability-testing:locust
    name: Locust Load Testing
    description: Locust is a scalable, distributed open-source load testing framework written in Python. Test scenarios are defined in pure Python code. Locust exposes a REST API and web UI for controlling test execution, viewing real-time metrics, and integrating with CI/CD pipelines.
    humanURL: https://locust.io/
    baseURL: http://localhost:8089
    tags:
      - Load Testing
      - Locust
      - Open Source
      - Python
    properties:
      - type: Documentation
        url: https://docs.locust.io/en/stable/
      - type: GitHub
        url: https://github.com/locustio/locust
  - aid: scalability-testing:gatling
    name: Gatling Load Testing
    description: Gatling is an open-source load testing framework built on Akka and Netty, providing high performance with a Scala/Java/Kotlin DSL for defining test scenarios. The Gatling Enterprise cloud platform provides distributed execution and advanced analytics APIs.
    humanURL: https://gatling.io/
    tags:
      - Gatling
      - Java
      - Load Testing
      - Open Source
      - Scala
    properties:
      - type: Documentation
        url: https://docs.gatling.io/
      - type: GitHub
        url: https://github.com/gatling/gatling
common:
  - type: Website
    url: https://k6.io/
  - type: GitHub
    url: https://github.com/grafana/k6
  - type: GitHub
    url: https://github.com/apache/jmeter
  - type: GitHub
    url: https://github.com/locustio/locust
  - type: GitHub
    url: https://github.com/gatling/gatling
  - type: Documentation
    url: https://grafana.com/docs/grafana-cloud/testing/k6/
  - type: Vocabulary
    url: vocabulary/scalability-testing-vocabulary.yml
  - type: JSONLD
    url: json-ld/scalability-testing-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
