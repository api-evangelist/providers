---
name: Test Scripts
description: Automated scripts used to verify software functionality, validate code behavior, and ensure quality through repeatable testing procedures. Test scripts encode testing logic in executable form, enabling continuous integration pipelines to run validation automatically on every code change. They support unit testing, integration testing, end-to-end testing, contract testing, performance testing, and security scanning across REST, GraphQL, SOAP, and gRPC APIs.
url: https://en.wikipedia.org/wiki/Test_automation
tags:
  - Automation
  - CI/CD
  - Contract Testing
  - Quality Assurance
  - Software Development
  - Testing
created: '2025'
modified: '2026-05-03'
apis:
  - name: Postman API
    description: The Postman API enables programmatic access to Postman collections, environments, monitors, and test scripts. It allows teams to manage and execute API test scripts as part of CI/CD pipelines, retrieve test run results, and integrate Postman with other DevOps tooling.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.postman.com/postman/postman-public-workspace/
    baseURL: https://api.getpostman.com
    tags:
      - API Testing
      - Collections
      - Test Execution
    properties:
      - type: Documentation
        url: https://learning.postman.com/docs/introduction/overview/
      - type: OpenAPI
        url: https://www.postman.com/postman/postman-public-workspace/api/72a32ca1-f3a2-4a5e-91f2-token
  - name: Newman CLI
    description: Newman is the command-line companion for Postman, enabling Postman collections and test scripts to be run directly from the terminal or integrated into CI/CD pipelines such as GitHub Actions, Jenkins, and GitLab CI.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/postmanlabs/newman
    baseURL: https://github.com/postmanlabs/newman
    tags:
      - CLI
      - CI/CD
      - Test Execution
    properties:
      - type: Documentation
        url: https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/
      - type: GitHubOrg
        url: https://github.com/postmanlabs/newman
  - name: Karate API Testing Framework
    description: Karate is an open-source framework that combines API test automation, mocks, performance testing, and UI automation into a single framework. Test scripts are written in plain-text Gherkin syntax, making them readable by non-programmers while offering powerful assertion and data-driven capabilities.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://karatelabs.github.io/karate/
    baseURL: https://karatelabs.github.io/karate/
    tags:
      - BDD
      - Gherkin
      - API Testing
      - Test Automation
    properties:
      - type: Documentation
        url: https://karatelabs.github.io/karate/
      - type: GitHubOrg
        url: https://github.com/karatelabs/karate
  - name: REST Assured
    description: REST Assured is a Java-based DSL for simplifying testing of REST services. It integrates with JUnit and TestNG, and supports BDD-style test scripting with a fluent API for validating HTTP responses, headers, and JSON/XML payloads.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://rest-assured.io/
    baseURL: https://rest-assured.io/
    tags:
      - Java
      - BDD
      - REST
      - Test Automation
    properties:
      - type: Documentation
        url: https://github.com/rest-assured/rest-assured/wiki/Usage
      - type: GitHubOrg
        url: https://github.com/rest-assured/rest-assured
  - name: Dredd API Testing Framework
    description: Dredd is an open-source language-agnostic command-line tool for validating API documentation written in OpenAPI or API Blueprint against its backend implementation. It reads test scripts derived from API specifications and automatically verifies that server responses match documented behavior.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dredd.org/
    baseURL: https://dredd.org/
    tags:
      - Contract Testing
      - OpenAPI
      - Test Automation
    properties:
      - type: Documentation
        url: https://dredd.org/en/latest/
      - type: GitHubOrg
        url: https://github.com/apiaryio/dredd
  - name: k6 Performance Testing
    description: k6 is a modern load-testing tool that uses JavaScript test scripts to simulate concurrent users hitting APIs. Its scripting model allows teams to write reusable, version-controlled performance test scripts that integrate natively with CI/CD pipelines and output detailed performance metrics.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://k6.io/
    baseURL: https://api.k6.io
    tags:
      - Load Testing
      - Performance Testing
      - JavaScript
      - Test Automation
    properties:
      - type: Documentation
        url: https://grafana.com/docs/k6/latest/
      - type: OpenAPI
        url: https://grafana.com/docs/k6/latest/misc/k6-rest-api/
  - name: Playwright Test
    description: Playwright is a cross-browser end-to-end testing framework from Microsoft that supports writing test scripts in JavaScript, TypeScript, Python, Java, and .NET. It is widely used for API testing, browser automation, and full-stack integration test scripting in CI/CD pipelines.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://playwright.dev/
    baseURL: https://playwright.dev/
    tags:
      - End-to-End Testing
      - Browser Automation
      - JavaScript
      - Test Automation
    properties:
      - type: Documentation
        url: https://playwright.dev/docs/intro
      - type: GitHubOrg
        url: https://github.com/microsoft/playwright
  - name: Cypress
    description: Cypress is a JavaScript end-to-end testing framework designed for modern web applications. Its test scripting API supports both API testing and browser automation, with real-time test runner feedback and built-in parallelization for CI/CD environments.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cypress.io/
    baseURL: https://www.cypress.io/
    tags:
      - End-to-End Testing
      - JavaScript
      - Test Automation
    properties:
      - type: Documentation
        url: https://docs.cypress.io/
      - type: GitHubOrg
        url: https://github.com/cypress-io/cypress
  - name: Schemathesis
    description: Schemathesis is a property-based testing tool for web APIs. It reads OpenAPI or GraphQL schemas and automatically generates test scripts to discover edge cases, crashes, and specification violations through stateful, hypothesis-driven testing.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://schemathesis.io/
    baseURL: https://schemathesis.io/
    tags:
      - Property-Based Testing
      - OpenAPI
      - Fuzz Testing
    properties:
      - type: Documentation
        url: https://schemathesis.readthedocs.io/
      - type: GitHubOrg
        url: https://github.com/schemathesis/schemathesis
common:
  - type: GitHubOrg
    url: https://github.com/api-evangelist/test-scripts
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/json-schema/test-scripts-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/json-structure/test-scripts-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/json-ld/test-scripts-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/vocabulary/test-scripts-vocabulary.yml
---
