---
aid: google-cloud-security-command-center
name: Google Cloud Security Command Center
description: Google Cloud Security Command Center (SCC) is a security and risk management platform for Google Cloud that helps organizations identify misconfigurations, vulnerabilities, and threats across their cloud assets. It provides centralized visibility into cloud resources, security findings, and compliance status, enabling security teams to detect, investigate, and respond to threats.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-security-command-center/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Cloud Security
  - Compliance
  - Risk Management
  - Security
  - Threat Detection
  - Vulnerability Management
apis:
  - name: Security Command Center API
    description: The Security Command Center API provides programmatic access to security findings, assets, and sources within Google Cloud. Developers can use the API to list and manage security findings, create and manage notification configs, run asset discovery, and configure organization-level security settings.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/security-command-center/docs
    baseURL: https://securitycenter.googleapis.com
    tags:
      - Assets
      - Security Findings
      - Threat Detection
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://cloud.google.com/security-command-center/docs/reference/rest
      - type: OpenAPI
        url: openapi/security-command-center-api-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/security-command-center/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/security-command-center/docs/quickstart
      - type: JSONSchema
        url: json-schema/google-cloud-security-command-center-finding-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/security-command-center
  - type: Getting Started
    url: https://cloud.google.com/security-command-center/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/security-command-center/docs
  - type: Authentication
    url: https://cloud.google.com/security-command-center/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/security-command-center/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/security-command-center/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-security-command-center-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
