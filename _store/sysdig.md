---
aid: sysdig
name: Sysdig
description: Sysdig is a cloud and container security platform that provides runtime threat detection, vulnerability management, cloud security posture management (CSPM), compliance automation, and observability for containers, Kubernetes, and cloud environments. Sysdig Monitor offers full-stack monitoring and alerting while Sysdig Secure delivers runtime security, vulnerability scanning, policy enforcement, incident response, and compliance reporting.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Security
  - Containers
  - Kubernetes
  - Runtime Security
  - Security
  - Vulnerability Management
  - Monitoring
  - Observability
  - CSPM
  - Compliance
url: https://raw.githubusercontent.com/api-evangelist/sysdig/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: sysdig:sysdig-monitor
    name: Sysdig Monitor
    description: The Sysdig Monitor API provides programmatic access to monitoring and observability capabilities including dashboards, alerts, events, metrics, teams, notification channels, and scanning results for cloud-native environments.
    humanURL: https://docs.sysdig.com/en/developer-tools/sysdig-api/
    baseURL: https://api.us1.sysdig.com
    tags:
      - Monitoring
      - Observability
      - Alerts
      - Dashboards
      - Metrics
      - Events
    properties:
      - type: Documentation
        url: https://docs.sysdig.com/en/developer-tools/sysdig-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sysdig/refs/heads/main/openapi/sysdig-monitor-openapi.yml
      - type: Getting Started
        url: https://docs.sysdig.com/en/getting-started/
      - type: Authentication
        url: https://docs.sysdig.com/en/developer-tools/sysdig-api/
    contact:
      - FN: Sysdig Support
        url: https://sysdig.com/support/
  - aid: sysdig:sysdig-secure
    name: Sysdig Secure
    description: The Sysdig Secure API provides programmatic access to cloud and container security capabilities including vulnerability management, runtime policies, compliance checks, activity audit, incident response, image scanning, SBOM retrieval, and Falco rules management.
    humanURL: https://docs.sysdig.com/en/developer-tools/sysdig-api/
    baseURL: https://api.us1.sysdig.com
    tags:
      - Security
      - Vulnerability Management
      - Compliance
      - Runtime Security
      - Falco
      - Scanning
      - CSPM
    properties:
      - type: Documentation
        url: https://docs.sysdig.com/en/developer-tools/sysdig-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sysdig/refs/heads/main/openapi/sysdig-secure-openapi.yml
      - type: Getting Started
        url: https://docs.sysdig.com/en/getting-started/
    contact:
      - FN: Sysdig Support
        url: https://sysdig.com/support/
common:
  - type: Website
    url: https://sysdig.com/
  - type: Documentation
    url: https://docs.sysdig.com/
  - type: Developer Portal
    url: https://docs.sysdig.com/en/developer-tools/
  - type: Getting Started
    url: https://docs.sysdig.com/en/getting-started/
  - type: GitHub Organization
    url: https://github.com/sysdiglabs
  - type: Blog
    url: https://sysdig.com/blog/
  - type: Pricing
    url: https://sysdig.com/pricing/
  - type: Sign Up
    url: https://sysdig.com/company/free-trial/
  - type: Terraform Provider
    url: https://registry.terraform.io/providers/sysdiglabs/sysdig/latest
  - type: Python SDK
    url: https://github.com/sysdiglabs/sysdig-sdk-python
  - type: CLI
    url: https://sysdiglabs.github.io/sysdig-platform-cli/
  - type: Kubernetes Operator
    url: https://github.com/sysdiglabs/sysdig-operator
  - type: Helm Charts
    url: https://github.com/sysdiglabs/charts
  - type: Spectral Rules
    url: https://raw.githubusercontent.com/api-evangelist/sysdig/refs/heads/main/rules/sysdig-rules.yml
  - type: Naftiko Capabilities
    url: https://raw.githubusercontent.com/api-evangelist/sysdig/refs/heads/main/capabilities/cloud-security-monitoring.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/sysdig/refs/heads/main/vocabulary/sysdig-vocabulary.yml
  - type: Change Log
    url: https://docs.sysdig.com/en/release-notes/
  - type: Support
    url: https://sysdig.com/support/
  - type: Status
    url: https://status.sysdig.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
