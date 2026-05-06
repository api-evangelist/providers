---
name: Test Suites
description: A collection of organized test cases designed to validate specific functionality or features of software applications and APIs. Test suites group related test cases into logical units that can be executed together, providing comprehensive coverage of a system's behavior. They are widely used by developers to build, maintain, and scale software testing across functional testing, regression testing, contract testing, and compliance validation. Test suites range from unit test collections in JUnit and pytest to API test collection suites in Postman, Bruno, and Karate.
url: https://en.wikipedia.org/wiki/Test_suite
tags:
  - API Testing
  - Collections
  - Quality Assurance
  - Software Development
  - Test Management
  - Testing
created: '2025'
modified: '2026-05-03'
apis:
  - name: Postman Collections API
    description: Postman Collections are the primary organizational unit for grouping API test cases into test suites. The Postman API allows programmatic management of collections, enabling creation, retrieval, and execution of API test suites via the Collections API and Newman CLI runner.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.postman.com/
    baseURL: https://api.getpostman.com
    tags:
      - Collections
      - API Testing
      - Test Management
    properties:
      - type: Documentation
        url: https://learning.postman.com/docs/collections/collections-overview/
      - type: OpenAPI
        url: https://www.postman.com/postman/postman-public-workspace/
  - name: JUnit 5
    description: JUnit 5 is the Java testing framework used to organize test cases into test suites. The @Suite annotation enables test class grouping, tag-based filtering, and hierarchical suite composition, making it the standard Java test suite management solution for unit, integration, and API tests.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://junit.org/junit5/
    baseURL: https://junit.org/junit5/
    tags:
      - Java
      - Test Suite
      - Unit Testing
    properties:
      - type: Documentation
        url: https://junit.org/junit5/docs/current/user-guide/
      - type: GitHubOrg
        url: https://github.com/junit-team/junit5
  - name: pytest
    description: pytest is the Python testing framework supporting test suite organization through test classes, directories, markers, and fixtures. Its plugin architecture enables test suite reporting, parallel execution, and integration with coverage analysis and CI/CD systems.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://pytest.org/
    baseURL: https://pytest.org/
    tags:
      - Python
      - Test Suite
      - Testing
    properties:
      - type: Documentation
        url: https://docs.pytest.org/en/latest/
      - type: GitHubOrg
        url: https://github.com/pytest-dev/pytest
  - name: Jasmine
    description: Jasmine is a behavior-driven JavaScript testing framework that organizes test cases into describe/it suite blocks. It is commonly used for organizing API client test suites in Node.js environments and browser-based JavaScript applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://jasmine.github.io/
    baseURL: https://jasmine.github.io/
    tags:
      - BDD
      - JavaScript
      - Test Suite
    properties:
      - type: Documentation
        url: https://jasmine.github.io/tutorials/your_first_suite
      - type: GitHubOrg
        url: https://github.com/jasmine/jasmine
  - name: Mocha
    description: Mocha is a flexible JavaScript test suite framework supporting both synchronous and asynchronous API tests. It provides describe/it nesting for suite organization, rich reporting, and integration with assertion libraries such as Chai and Sinon.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://mochajs.org/
    baseURL: https://mochajs.org/
    tags:
      - JavaScript
      - Node.js
      - Test Suite
    properties:
      - type: Documentation
        url: https://mochajs.org/#getting-started
      - type: GitHubOrg
        url: https://github.com/mochajs/mocha
  - name: Jest
    description: Jest is a zero-configuration JavaScript testing framework with built-in test suite runner, mocking, coverage reporting, and snapshot testing. Widely used for React applications and Node.js API services, Jest organizes test cases into describe blocks and supports parallel test suite execution.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://jestjs.io/
    baseURL: https://jestjs.io/
    tags:
      - JavaScript
      - React
      - Test Suite
    properties:
      - type: Documentation
        url: https://jestjs.io/docs/getting-started
      - type: GitHubOrg
        url: https://github.com/jestjs/jest
  - name: Bruno
    description: Bruno is an open-source API client and test suite manager that stores API collections as plain files alongside application code. It enables version- controlled test suites in a format designed for git-based collaboration, with scripting support for pre-request and post-request test logic.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.usebruno.com/
    baseURL: https://www.usebruno.com/
    tags:
      - API Testing
      - Collections
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.usebruno.com/
      - type: GitHubOrg
        url: https://github.com/usebruno/bruno
  - name: Hurl
    description: Hurl is a command-line tool that runs HTTP requests defined in a simple plain-text format, enabling lightweight API test suites that can be committed to source control and executed in CI/CD pipelines without additional runtime dependencies.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://hurl.dev/
    baseURL: https://hurl.dev/
    tags:
      - API Testing
      - CLI
      - Test Suite
    properties:
      - type: Documentation
        url: https://hurl.dev/docs/installation.html
      - type: GitHubOrg
        url: https://github.com/Orange-OpenSource/hurl
  - name: TestNG
    description: TestNG is a Java testing framework inspired by JUnit and NUnit that provides advanced test suite configuration including grouping, prioritization, parameterized tests, and parallel execution. It is widely used for API integration test suites alongside REST Assured.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://testng.org/
    baseURL: https://testng.org/
    tags:
      - Java
      - Test Suite
      - Integration Testing
    properties:
      - type: Documentation
        url: https://testng.org/doc/documentation-main.html
      - type: GitHubOrg
        url: https://github.com/testng-team/testng
common:
  - type: GitHubOrg
    url: https://github.com/api-evangelist/test-suites
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/json-schema/test-suites-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/json-structure/test-suites-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/json-ld/test-suites-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/vocabulary/test-suites-vocabulary.yml
---
