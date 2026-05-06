---
name: Test-Driven Development
description: A software development approach where tests are written before the actual code, following a red-green-refactor cycle to ensure code quality and maintainability. TDD requires developers to write failing tests first, then write minimal code to make them pass, then refactor. It supports the full software development lifecycle from design through deployment and maintenance and is foundational to agile and extreme programming methodologies.
url: https://en.wikipedia.org/wiki/Test-driven_development
tags:
  - Agile
  - Best Practices
  - Continuous Integration
  - Extreme Programming
  - Methodology
  - Software Development
  - Testing
created: '2025'
modified: '2026-05-03'
apis:
  - name: GitHub Actions API
    description: REST API for GitHub Actions enabling CI/CD workflow automation, test execution, and status checks as part of TDD workflows on pull requests and commits.
    humanURL: https://docs.github.com/en/rest/actions
    baseURL: https://api.github.com
    tags:
      - CI/CD
      - Continuous Integration
      - GitHub
      - Test Automation
    properties:
      - type: Documentation
        url: https://docs.github.com/en/rest/actions
      - type: OpenAPI
        url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - name: CircleCI API
    description: REST API for CircleCI continuous integration platform, supporting pipeline management, test execution, and workflow orchestration as part of TDD CI/CD workflows.
    humanURL: https://circleci.com/docs/api/v2/
    baseURL: https://circleci.com/api/v2
    tags:
      - CI/CD
      - Continuous Integration
      - Pipelines
      - Test Automation
    properties:
      - type: Documentation
        url: https://circleci.com/docs/api/v2/
      - type: OpenAPI
        url: https://circleci.com/api/v2/openapi.json
  - name: Jenkins API
    description: REST API for Jenkins automation server supporting build triggers, test execution, and pipeline management for TDD-based development workflows.
    humanURL: https://www.jenkins.io/doc/book/using/remote-access-api/
    baseURL: https://your-jenkins.example.com
    tags:
      - Automation
      - Build Management
      - CI/CD
      - Continuous Integration
    properties:
      - type: Documentation
        url: https://www.jenkins.io/doc/book/using/remote-access-api/
  - name: SonarQube API
    description: REST API for SonarQube code quality and security analysis platform, supporting test coverage metrics, code smells, and quality gate enforcement in TDD pipelines.
    humanURL: https://docs.sonarsource.com/sonarqube/latest/extension-guide/web-api/
    baseURL: https://your-sonar.example.com/api
    tags:
      - Code Coverage
      - Code Quality
      - Static Analysis
      - Testing
    properties:
      - type: Documentation
        url: https://docs.sonarsource.com/sonarqube/latest/extension-guide/web-api/
  - name: Codecov API
    description: REST API for Codecov code coverage reporting service, enabling programmatic access to coverage reports, branch comparisons, and coverage trends in TDD workflows.
    humanURL: https://docs.codecov.com/reference
    baseURL: https://api.codecov.io/api/v2
    tags:
      - Code Coverage
      - Reporting
      - Testing
    properties:
      - type: Documentation
        url: https://docs.codecov.com/reference
      - type: APIReference
        url: https://docs.codecov.com/reference
  - name: Coveralls API
    description: REST API for Coveralls code coverage history and statistics service, tracking test coverage over time and integrating with GitHub for TDD feedback loops.
    humanURL: https://docs.coveralls.io
    baseURL: https://coveralls.io
    tags:
      - Code Coverage
      - Reporting
      - Testing
    properties:
      - type: Documentation
        url: https://docs.coveralls.io
common:
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Test-driven_development
  - type: Documentation
    url: https://martinfowler.com/bliki/TestDrivenDevelopment.html
  - type: Features
    data:
      - name: Red-Green-Refactor Cycle
        description: Write failing tests first, implement minimal code to pass them, then refactor while keeping tests green.
      - name: Test Coverage Enforcement
        description: Ensure all production code is covered by tests written before implementation.
      - name: Continuous Feedback
        description: Get immediate feedback on code correctness through automated test runs on every change.
      - name: Design by Contract
        description: Use failing tests to define the API contract and behavior before implementation begins.
      - name: Regression Prevention
        description: Build a comprehensive regression suite as a side effect of the TDD development process.
      - name: Refactoring Safety
        description: Refactor code with confidence knowing the full test suite will catch regressions.
  - type: UseCases
    data:
      - name: API Design Validation
        description: Use TDD to validate API contracts before writing implementation code.
      - name: Bug-Driven Development
        description: Write a failing test that reproduces a bug before fixing it to prevent recurrence.
      - name: Legacy Code Modernization
        description: Apply TDD when refactoring legacy code to ensure behavior is preserved.
      - name: Microservice Development
        description: Use TDD to build well-tested microservice APIs with clear contracts.
      - name: Continuous Integration
        description: Run TDD test suites automatically on every commit to maintain code quality.
  - type: Integrations
    data:
      - name: GitHub Actions
        description: Run TDD test suites automatically on pull requests using GitHub Actions workflows.
      - name: Jest
        description: Use Jest for JavaScript TDD with fast test execution and snapshot testing.
      - name: JUnit
        description: Use JUnit for Java TDD with test lifecycle management and assertion libraries.
      - name: pytest
        description: Use pytest for Python TDD with fixtures, parametrize, and plugin ecosystem.
      - name: RSpec
        description: Use RSpec for Ruby TDD with behavior-driven development syntax.
  - type: JSONSchema
    url: json-schema/test-driven-development-cycle-schema.json
  - type: JSONSchema
    url: json-schema/test-driven-development-coverage-report-schema.json
  - type: JSONSchema
    url: json-schema/test-driven-development-test-spec-schema.json
  - type: JSONLD
    url: json-ld/test-driven-development-context.jsonld
  - type: Vocabulary
    url: vocabulary/test-driven-development-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
