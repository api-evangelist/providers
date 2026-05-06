---
aid: schemathesis
name: Schemathesis
description: Schemathesis is a property-based API testing tool that automatically generates test cases from OpenAPI and GraphQL schemas to find bugs and specification violations. It uses the Hypothesis property-based testing framework to generate diverse, edge-case-covering test inputs from schema constraints, detecting server crashes, response schema violations, validation bypasses, and stateful bugs in multi-step workflows. Used by Netflix, SAP, Red Hat, IBM, and JetBrains.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Testing
  - Contract Testing
  - Fuzzing
  - OpenAPI
  - Property-Based Testing
  - Schemathesis
url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: schemathesis:schemathesis
    name: Schemathesis
    description: Schemathesis is a property-based API testing tool that automatically generates test cases from OpenAPI and GraphQL schemas to find bugs and spec violations. It detects server crashes, schema violations, validation bypasses, and integration failures with minimal maintenance overhead—tests adapt automatically as schemas evolve.
    humanURL: https://schemathesis.io
    tags:
      - API Testing
      - Contract Testing
      - Fuzzing
      - GraphQL
      - Hypothesis
      - OpenAPI
      - Property-Based Testing
      - Python
    properties:
      - type: Documentation
        url: https://schemathesis.readthedocs.io
      - type: GitHub Repository
        url: https://github.com/schemathesis/schemathesis
      - type: PyPI Package
        url: https://pypi.org/project/schemathesis/
      - type: Getting Started
        url: https://schemathesis.readthedocs.io/en/stable/getting-started.html
      - type: Docker Image
        url: https://hub.docker.com/r/schemathesis/schemathesis
      - type: GitHub Action
        url: https://github.com/schemathesis/action
      - type: Changelog
        url: https://github.com/schemathesis/schemathesis/releases
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/json-schema/schemathesis-config-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/json-structure/schemathesis-config-structure.json
      - type: JSONLd
        url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/json-ld/schemathesis-context.jsonld
common:
  - type: Website
    url: https://schemathesis.io
  - type: Documentation
    url: https://schemathesis.readthedocs.io
  - type: GitHub Organization
    url: https://github.com/schemathesis
  - type: PyPI Package
    url: https://pypi.org/project/schemathesis/
  - type: Docker Image
    url: https://hub.docker.com/r/schemathesis/schemathesis
  - type: Blog
    url: https://schemathesis.io/blog
  - type: Research
    url: https://dl.acm.org/doi/10.1145/3510003.3510097
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/vocabulary/schemathesis-vocabulary.yml
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/examples/schemathesis-cli-test-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
