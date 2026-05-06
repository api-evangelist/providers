---
aid: focus-spec
name: FOCUS (FinOps Open Cost and Usage Specification)
description: FOCUS, the FinOps Open Cost and Usage Specification, is an open standard maintained under the FinOps Foundation that normalizes cost and usage data across cloud, SaaS, data center, and other technology vendors. FOCUS defines a common data schema, a controlled vocabulary of column names, allowed values, and pricing attributes so that practitioners can apply a consistent set of FinOps practices regardless of which provider generated the underlying billing dataset. FOCUS is purely a data specification rather than a REST API; conforming providers expose exports of their billing data in the FOCUS format, and tooling consumes those exports against the published column library, data model, and validator.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/focus-spec/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Billing
  - Cost and Usage
  - FinOps
  - Open Standard
  - Specification
apis:
  - aid: focus-spec:focus-spec
    name: FOCUS (FinOps Open Cost and Usage Specification)
    description: FOCUS defines a common normalized data schema for cloud and technology billing data. The specification is delivered as a set of normative documents and supporting artifacts (column library, requirements model, validator, Excel/CSV samples) rather than as a REST API. This entry tracks the specification itself and links to a JSON Schema representation of a single FOCUS-conformant billing record so that data consumers and integrators can validate individual rows produced by FOCUS-aligned exports.
    humanURL: https://focus.finops.org/
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - FinOps
      - Specification
      - Cost and Usage
      - Billing
    properties:
      - type: Documentation
        url: https://focus.finops.org/
      - type: Getting Started
        url: https://focus.finops.org/focus-getting-started/
      - type: GitHubRepository
        url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec
      - type: GitHubOrganization
        url: https://github.com/FinOps-Open-Cost-and-Usage-Spec
      - type: JSONSchema
        url: json-schema/focus-billing-record-schema.json
common:
  - type: Website
    url: https://focus.finops.org/
  - type: Documentation
    url: https://focus.finops.org/
  - type: GitHubRepository
    url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec
  - type: GitHubOrganization
    url: https://github.com/FinOps-Open-Cost-and-Usage-Spec
  - type: JSONSchema
    url: json-schema/focus-billing-record-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
