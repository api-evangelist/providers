---
aid: kion
url: https://raw.githubusercontent.com/api-evangelist/kion/refs/heads/main/apis.yml
apis:
  - aid: kion:kion-cloud-operations-api
    name: Kion Cloud Operations API
    tags:
      - Cloud Operations
      - Compliance
      - Costs
      - FinOps
      - Governance
      - Multi-Cloud
      - Spend
    humanURL: https://support.kion.io/hc/en-us/sections/4412439670797-Public-API
    baseURL: https://{kion-instance}/api/v3
    properties:
      - url: https://support.kion.io/hc/en-us/articles/360024610491-Getting-Started-with-the-Kion-Public-API
        type: Documentation
      - url: openapi/kion-cloud-operations-api-openapi.yml
        type: OpenAPI
      - url: json-schema/account.json
        type: JSONSchema
      - url: json-schema/project.json
        type: JSONSchema
      - url: json-schema/ou.json
        type: JSONSchema
      - url: json-schema/cloud-rule.json
        type: JSONSchema
      - url: json-schema/compliance-check.json
        type: JSONSchema
      - url: json-schema/compliance-standard.json
        type: JSONSchema
      - url: json-schema/funding-source.json
        type: JSONSchema
      - url: json-schema/label.json
        type: JSONSchema
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/user-group.json
        type: JSONSchema
      - url: json-schema/cloud-access-role.json
        type: JSONSchema
      - url: json-schema/aws-iam-policy.json
        type: JSONSchema
      - url: json-schema/service-control-policy.json
        type: JSONSchema
      - url: json-schema/cloudformation-template.json
        type: JSONSchema
      - url: json-schema/webhook.json
        type: JSONSchema
      - url: json-schema/custom-variable.json
        type: JSONSchema
      - url: json-ld/kion-context.jsonld
        type: JSONLD
    description: The Kion Public API provides programmatic access to manage cloud operations, governance, compliance, and financial management across AWS, Azure, GCP, and OCI.
name: Kion
tags:
  - Cloud Operations
  - Compliance
  - Costs
  - FinOps
  - Governance
  - Spend
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-28'
position: Consuming
description: Kion is a cloud operations platform that provides automated governance and FinOps capabilities across AWS, Azure, GCP, and OCI through a self-hosted deployment model. The platform consolidates multiple point solutions into a comprehensive system that helps organizations allocate and track cloud spending, identify savings opportunities, enforce budgets, and access real-time and forecasted financial data.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Kion – FinOps automated governance, self-hosted in AWS, Azure, GCP, and OCI.
    description: 'null'
    url: https://kion.io/
    type: Website
  - name: Blog – Kion
    description: 'null'
    url: https://kion.io/blog/?Type=blog
    type: Blog
  - name: Case Studies – Kion
    description: 'null'
    url: https://kion.io/resources/case-studies/?Type=case-study
    type: CaseStudies
  - name: The Glossary | Kion – Kion
    description: 'null'
    url: https://kion.io/resources/glossary/
    type: Glossary
  - name: Support – Kion
    description: 'null'
    url: https://kion.io/resources/support/
    type: Support
  - name: Kion | Partners – Kion
    description: 'null'
    url: https://kion.io/partners/providers/
    type: Partners
  - name: Pricing and Licensing | Kion – Kion
    description: 'null'
    url: https://kion.io/why-kion/pricing-and-licensing/
    type: Pricing
  - name: Request Demo of Cloud Operations Software | Kion – Kion
    description: 'null'
    url: https://kion.io/platform/request-a-demo/
    type: RequestDemo
---
