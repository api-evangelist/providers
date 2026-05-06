---
aid: reflect
name: Reflect
description: Reflect is an AI-powered automated end-to-end testing platform that enables teams to effortlessly create, execute, and troubleshoot automated browser tests. Reflect provides a no-code test recorder for capturing user workflows and a REST API for integrating test execution into CI/CD pipelines. Tests can be run against any environment using hostname and parameter overrides.
type: Index
image: https://reflect.run/assets/logo.png
url: https://raw.githubusercontent.com/api-evangelist/reflect/refs/heads/main/apis.yml
created: '2024-11-13'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - AI Testing
  - Artificial Intelligence
  - Automated Testing
  - CI/CD
  - End-to-End Testing
  - QA
  - Testing
apis:
  - aid: reflect:reflect
    name: Reflect
    description: REST API for managing and executing automated end-to-end tests in the Reflect platform. Enables listing available tests, triggering test runs with parameter overrides, and polling execution status for CI/CD integration.
    humanURL: https://reflect.run/
    baseURL: https://api.reflect.run/v1
    tags:
      - AI Testing
      - Automated Testing
      - CI/CD
      - End-to-End Testing
    properties:
      - type: Documentation
        url: https://reflect.run/docs/developer-api/documentation/
      - type: OpenAPI
        url: openapi/reflect-openapi.yml
      - type: GettingStarted
        url: https://reflect.run/docs/overview/quick-start/
      - type: Integrations
        url: https://reflect.run/docs/integrations/
common:
  - type: Pricing
    url: https://reflect.run/pricing/
  - type: Articles
    url: https://reflect.run/articles/
  - type: Customers
    url: https://reflect.run/customers/
  - type: Login
    url: https://app.reflect.run/login
  - type: SignUp
    url: https://app.reflect.run/registration
  - type: About
    url: https://reflect.run/about/
  - type: TermsOfService
    url: https://reflect.run/terms-of-service/
  - type: PrivacyPolicy
    url: https://reflect.run/privacy-policy/
  - type: Integrations
    url: https://reflect.run/docs/integrations/
  - type: GettingStarted
    url: https://reflect.run/docs/overview/quick-start/
  - type: OpenAPI
    url: openapi/reflect-openapi.yml
  - type: JSONSchema
    url: json-schema/reflect-test-schema.json
  - type: JSONSchema
    url: json-schema/reflect-execution-schema.json
  - type: JSONStructure
    url: json-structure/reflect-api-structure.json
  - type: JSONLDContext
    url: json-ld/reflect-context.jsonld
  - type: SpectralRules
    url: rules/reflect-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/test-automation.yaml
  - type: Vocabulary
    url: vocabulary/reflect-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
