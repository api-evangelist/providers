---
aid: openfga
name: OpenFGA
description: OpenFGA is a CNCF incubating high-performance authorization system implementing fine-grained access control based on the Zanzibar model. It provides a flexible relationship-based authorization engine that evaluates access decisions using a type system defined in a modeling language. OpenFGA supports authorization checks, relationship queries, and list operations through its API.
url: https://openfga.dev
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Control
  - Authorization
  - Cloud Native
  - Fine-Grained
  - Incubating
  - Zanzibar
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: openfga:openfga-api
    name: OpenFGA Authorization API
    description: The OpenFGA API provides HTTP and gRPC endpoints for fine-grained authorization. Key operations include Check for evaluating access decisions, Write for managing relationship tuples, Read for querying relationships, ListObjects for finding accessible resources, and Expand for debugging authorization models. The API also supports store management and authorization model versioning.
    humanURL: https://openfga.dev/docs/getting-started
    properties:
      - type: Documentation
        url: https://openfga.dev/docs/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openfga/refs/heads/main/openapi/openfga-openapi.json
    tags:
      - Authorization API
      - Fine-Grained Access
      - Relationship Tuples
common:
  - type: Documentation
    name: OpenFGA Documentation
    description: Official OpenFGA documentation.
    url: https://openfga.dev/docs/
  - type: GitHubOrg
    name: OpenFGA GitHub
    description: Source code repository.
    url: https://github.com/openfga
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
