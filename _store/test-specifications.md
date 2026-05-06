---
name: Test Specifications
description: Documentation that defines the requirements, procedures, and expected outcomes for testing software systems and APIs. Test specifications establish the criteria that implementations must satisfy, bridging the gap between product requirements and executable test cases. They include test plans, test case definitions, acceptance criteria, and conformance requirements. Effective use of this practice reduces bugs in production, supports contract testing, and enables a culture of quality-driven development aligned with OpenAPI, AsyncAPI, and JSON Schema standards.
url: https://en.wikipedia.org/wiki/Test_specification
tags:
  - Acceptance Testing
  - Contract Testing
  - Documentation
  - OpenAPI
  - Quality Assurance
  - Testing
created: '2025'
modified: '2026-05-03'
apis:
  - name: OpenAPI Initiative
    description: The OpenAPI Specification (OAS) is the de-facto standard for describing RESTful APIs. OpenAPI documents serve as machine-readable test specifications that tools such as Dredd, Schemathesis, and Postman use to auto-generate and validate test suites against live API implementations.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.openapis.org/
    baseURL: https://spec.openapis.org/oas/v3.1.0
    tags:
      - REST
      - Specification
      - Standards
    properties:
      - type: Documentation
        url: https://spec.openapis.org/oas/v3.1.0
      - type: GitHubOrg
        url: https://github.com/OAI/OpenAPI-Specification
  - name: AsyncAPI Initiative
    description: AsyncAPI is an open specification standard for event-driven and message-based APIs. AsyncAPI documents define the channels, messages, and schemas of asynchronous interfaces, providing a test specification baseline for contract and integration testing of Kafka, WebSocket, AMQP, and MQTT APIs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.asyncapi.com/
    baseURL: https://www.asyncapi.com/
    tags:
      - AsyncAPI
      - Event-Driven
      - Specification
    properties:
      - type: Documentation
        url: https://www.asyncapi.com/docs
      - type: GitHubOrg
        url: https://github.com/asyncapi/spec
  - name: JSON Schema
    description: JSON Schema provides a vocabulary for annotating and validating JSON documents. Used extensively as the payload specification layer in test specifications, JSON Schema enables both human-readable documentation and machine-executable validation of API request and response bodies.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://json-schema.org/
    baseURL: https://json-schema.org/
    tags:
      - JSON
      - Schema Validation
      - Specification
    properties:
      - type: Documentation
        url: https://json-schema.org/learn/getting-started-step-by-step
      - type: GitHubOrg
        url: https://github.com/json-schema-org/json-schema-spec
  - name: Gherkin / Cucumber BDD
    description: Gherkin is a plain-text language used to write behavior-driven test specifications in Given-When-Then format. Cucumber and Karate consume Gherkin feature files as executable test specifications that bridge business requirements and automated test implementation for API testing.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cucumber.io/docs/gherkin/
    baseURL: https://cucumber.io/
    tags:
      - BDD
      - Gherkin
      - Test Specification
    properties:
      - type: Documentation
        url: https://cucumber.io/docs/gherkin/reference/
      - type: GitHubOrg
        url: https://github.com/cucumber/cucumber
  - name: Pact Contract Testing
    description: Pact is a consumer-driven contract testing tool where consumers write test specifications (pacts) that define what responses they expect from provider APIs. Providers then verify their implementation satisfies all consumer-authored specifications via the Pact Broker.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://pact.io/
    baseURL: https://pact.io/
    tags:
      - Consumer-Driven Contracts
      - Contract Testing
      - Specification
    properties:
      - type: Documentation
        url: https://docs.pact.io/
      - type: GitHubOrg
        url: https://github.com/pact-foundation/pact-specification
  - name: Swagger Editor
    description: Swagger Editor is an open-source web-based editor for designing OpenAPI specifications that double as test specifications. It provides real-time validation, mock server generation, and exportable spec files that integrate with testing pipelines.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://editor.swagger.io/
    baseURL: https://editor.swagger.io/
    tags:
      - API Design
      - OpenAPI
      - Test Specification
    properties:
      - type: Documentation
        url: https://swagger.io/docs/specification/about/
      - type: GitHubOrg
        url: https://github.com/swagger-api/swagger-editor
  - name: Optic API
    description: Optic is a developer tool that uses API specifications as the source of truth for testing. It tracks specification changes, generates changelog diffs, and validates live traffic against OpenAPI specs to detect contract drift between specifications and implementations.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.useoptic.com/
    baseURL: https://api.useoptic.com
    tags:
      - API Governance
      - Contract Testing
      - OpenAPI
    properties:
      - type: Documentation
        url: https://www.useoptic.com/docs
      - type: GitHubOrg
        url: https://github.com/opticdev/optic
  - name: Spectral
    description: Spectral is an open-source JSON/YAML linter and specification validator. It evaluates OpenAPI, AsyncAPI, and custom specification documents against rulesets, serving as a static test specification compliance checker integrated into CI/CD pipelines via the Spectral CLI.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://stoplight.io/open-source/spectral
    baseURL: https://stoplight.io/open-source/spectral
    tags:
      - API Governance
      - Linting
      - OpenAPI
      - Specification
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/spectral
      - type: GitHubOrg
        url: https://github.com/stoplightio/spectral
common:
  - type: GitHubOrg
    url: https://github.com/api-evangelist/test-specifications
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/json-schema/test-specifications-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/json-structure/test-specifications-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/json-ld/test-specifications-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/vocabulary/test-specifications-vocabulary.yml
---
