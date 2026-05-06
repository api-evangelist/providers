---
aid: google-cloud-assured-workloads
name: Google Cloud Assured Workloads
description: Google Cloud Assured Workloads enables organizations to create and manage compliance-controlled environments on Google Cloud. It provides guardrails for regulatory compliance frameworks such as FedRAMP, HIPAA, CJIS, ITAR, and others by enforcing organizational policies, data residency requirements, and access controls on cloud resources within designated workload environments.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-assured-workloads/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Compliance
  - Data Residency
  - FedRAMP
  - Governance
  - HIPAA
  - Regulatory
apis:
  - name: Assured Workloads API
    description: The Assured Workloads API enables developers to programmatically create, manage, and monitor compliance-controlled workload environments on Google Cloud. It supports creating workloads with specific compliance regimes, managing organizational policies, monitoring compliance violations, and configuring data residency and access controls. The API helps organizations maintain regulatory compliance across their cloud infrastructure.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/assured-workloads/docs
    baseURL: https://assuredworkloads.googleapis.com
    tags:
      - Compliance Regimes
      - Organizational Policies
      - Violations
      - Workloads
    properties:
      - type: Documentation
        url: https://cloud.google.com/assured-workloads/docs/reference/rest
      - type: OpenAPI
        url: openapi/assured-workloads-api-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/assured-workloads/docs/reference/rest#authentication
      - type: JSONSchema
        url: json-schema/google-cloud-assured-workloads-workload-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/assured-workloads
  - type: Getting Started
    url: https://cloud.google.com/assured-workloads/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/assured-workloads/docs
  - type: Authentication
    url: https://cloud.google.com/assured-workloads/docs/reference/rest#authentication
  - type: Pricing
    url: https://cloud.google.com/assured-workloads/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com
  - type: Support
    url: https://cloud.google.com/assured-workloads/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-assured-workloads-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
