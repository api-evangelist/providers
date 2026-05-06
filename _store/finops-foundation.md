---
aid: finops-foundation
name: FinOps Foundation
description: The FinOps Foundation aims to help organizations optimize their cloud spending and improve cloud financial management practices. By providing education, tools, and resources, the foundation equips teams with the skills and knowledge needed to effectively manage cloud costs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-28'
position: Consumer
tags:
  - Budgets
  - Costs
  - FinOps
url: https://raw.githubusercontent.com/api-evangelist/finops-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: finops-foundation:focus-cost-and-usage
    name: FOCUS Cost and Usage API
    tags:
      - Billing
      - Budgets
      - Cloud
      - Costs
      - FinOps
      - FOCUS
    humanURL: https://focus.finops.org/
    properties:
      - url: https://focus.finops.org/focus-specification/v1-3/
        type: Documentation
      - url: openapi/finops-foundation-focus-cost-and-usage-openapi.yml
        type: OpenAPI
      - url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec
        type: GitHub Repository
      - url: https://focus.finops.org/focus-columns/
        type: Reference
      - url: json-schema/finops-foundation-cost-and-usage-record-schema.json
        type: JSONSchema
      - url: json-schema/finops-foundation-contract-commitment-record-schema.json
        type: JSONSchema
      - url: json-ld/finops-foundation-context.jsonld
        type: JSONLD
    description: An API modeled on the FinOps Open Cost and Usage Specification (FOCUS) v1.3, the open standard maintained by the FinOps Foundation under the Linux Foundation that defines a common schema for cloud, SaaS, and other technology billing data.
common:
  - type: Website
    url: https://www.finops.org/
  - type: Community
    url: https://www.finops.org/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
