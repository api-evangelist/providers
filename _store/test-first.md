---
name: Test First
description: A software development approach where tests are written before the implementation code, ensuring code quality and driving design decisions through test requirements. Test-first development is the foundational principle behind test-driven development (TDD) and behavior-driven development (BDD), where the specification of expected behavior is captured in executable tests before any production code is written.
url: https://en.wikipedia.org/wiki/Test-driven_development
tags:
  - Behavior-Driven Development
  - Best Practices
  - Methodology
  - Software Design
  - Software Development
  - Testing
created: '2025'
modified: '2026-05-03'
apis:
  - name: Cucumber API
    description: REST API and tooling for Cucumber BDD framework supporting test-first development with Gherkin feature files, scenario definitions, and step implementations.
    humanURL: https://cucumber.io
    baseURL: https://cucumber.io
    tags:
      - Behavior-Driven Development
      - Gherkin
      - Test Automation
      - Testing
    properties:
      - type: Documentation
        url: https://cucumber.io/docs/cucumber/
      - type: GitHubRepository
        url: https://github.com/cucumber/cucumber-js
  - name: Pact Broker API
    description: REST API for Pact Broker contract testing service, enabling consumer-driven contract testing where consumer tests define the API contract before providers implement it.
    humanURL: https://docs.pact.io
    baseURL: https://your-pact-broker.example.com
    tags:
      - Consumer-Driven Contracts
      - Contract Testing
      - Microservices
      - Test-First
    properties:
      - type: Documentation
        url: https://docs.pact.io
      - type: GitHubRepository
        url: https://github.com/pact-foundation/pact_broker
      - type: OpenAPI
        url: https://raw.githubusercontent.com/pact-foundation/pact_broker/master/lib/pact_broker/api/pact_broker.json
  - name: Stoplight API
    description: API design-first platform enabling teams to write API specifications before implementation, supporting test-first development with mock servers, contract testing, and API style guides.
    humanURL: https://stoplight.io
    baseURL: https://api.stoplight.io
    tags:
      - API Design
      - Contract Testing
      - Mock Servers
      - Test-First
    properties:
      - type: Documentation
        url: https://meta.stoplight.io/docs/platform
      - type: APIReference
        url: https://meta.stoplight.io/docs/stoplight-api
  - name: Microcks API
    description: Open-source cloud-native tool for API mocking and contract testing, supporting test-first development by generating mocks from OpenAPI, Postman, and gRPC specifications.
    humanURL: https://microcks.io
    baseURL: https://your-microcks.example.com/api
    tags:
      - API Mocking
      - Contract Testing
      - Open Source
      - Test-First
    properties:
      - type: Documentation
        url: https://microcks.io/documentation/
      - type: GitHubRepository
        url: https://github.com/microcks/microcks
  - name: Dredd API
    description: Command-line HTTP API testing framework that validates API implementations against API Blueprint or OpenAPI descriptions, enabling test-first API development.
    humanURL: https://dredd.org
    baseURL: https://dredd.org
    tags:
      - API Testing
      - Contract Testing
      - OpenAPI
      - Test-First
    properties:
      - type: Documentation
        url: https://dredd.readthedocs.io
      - type: GitHubRepository
        url: https://github.com/apiaryio/dredd
common:
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Test-driven_development
  - type: Documentation
    url: https://www.agilealliance.org/glossary/tdd/
  - type: Features
    data:
      - name: Specification Before Implementation
        description: Write executable test specifications that define expected behavior before writing any production code.
      - name: API Contract Definition
        description: Define the API contract through tests before the implementation exists, ensuring design clarity.
      - name: Mock-First Development
        description: Use mock servers generated from specifications to enable parallel frontend and backend development.
      - name: Living Documentation
        description: Tests serve as up-to-date documentation of how the system is expected to behave.
      - name: Fail Fast Feedback
        description: Discover design issues early by specifying tests before implementation reveals constraints.
      - name: Consumer-Driven Contracts
        description: Let API consumers define their expectations as tests that the API provider must satisfy.
  - type: UseCases
    data:
      - name: API-First Design
        description: Write OpenAPI specifications and generate tests from them before building the implementation.
      - name: Consumer-Driven Contract Testing
        description: API consumers publish test expectations that API providers must verify in their CI pipelines.
      - name: Behavior-Driven Development
        description: Use Gherkin feature files to define expected system behavior before writing implementation.
      - name: Parallel Development
        description: Enable frontend and backend teams to develop in parallel using mock servers from specifications.
      - name: Specification Compliance
        description: Validate that API implementations comply with their published specifications using test-first assertions.
  - type: Integrations
    data:
      - name: OpenAPI
        description: Generate test-first stubs and mocks directly from OpenAPI specifications.
      - name: Cucumber
        description: Use Gherkin scenarios as the test-first specification for behavior-driven development.
      - name: Pact
        description: Apply consumer-driven contract testing where consumer tests define provider expectations.
      - name: Prism
        description: Use Stoplight Prism to mock APIs from OpenAPI specs enabling test-first development.
  - type: JSONSchema
    url: json-schema/test-first-specification-schema.json
  - type: JSONSchema
    url: json-schema/test-first-contract-schema.json
  - type: JSONSchema
    url: json-schema/test-first-mock-schema.json
  - type: JSONLD
    url: json-ld/test-first-context.jsonld
  - type: Vocabulary
    url: vocabulary/test-first-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
