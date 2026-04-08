---
aid: openfga
url: https://raw.githubusercontent.com/api-evangelist/openfga/refs/heads/main/apis.yml
apis:
- aid: openfga:openfga-api
  name: OpenFGA Authorization API
  description: The OpenFGA API provides HTTP and gRPC endpoints for fine-grained authorization. Key operations include Check for evaluating access decisions, Write for managing relationship tuples, Read for querying relationships, ListObjects for finding accessible resources, and Expand for debugging authorization models. The API also supports store management and authorization model versioning.
  humanURL: https://openfga.dev/docs/getting-started
  properties:
  - type: Documentation
    url: https://openfga.dev/docs/getting-started
  tags:
  - Authorization API
  - Fine-Grained Access
  - Relationship Tuples
name: OpenFGA
tags:
- Access Control
- Authorization
- Cloud Native
- Fine-Grained
- Incubating
- Zanzibar
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: OpenFGA is a CNCF incubating high-performance authorization system implementing fine-grained access control based on the Zanzibar model. It provides a flexible relationship-based authorization engine that evaluates access decisions using a type system defined in a modeling language. OpenFGA supports authorization checks, relationship queries, and list operations through its API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

