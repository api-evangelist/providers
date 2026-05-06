---
aid: neuvector
name: NeuVector
description: NeuVector is an open source, full lifecycle container security platform maintained by SUSE. It provides vulnerability scanning, runtime protection, compliance monitoring, and a Layer 7 container firewall for Kubernetes environments. The NeuVector REST API allows automation of scanning, policy management, configuration, user administration, and federated cluster operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Compliance
  - Containers
  - Kubernetes
  - Open Source
  - Runtime Protection
  - Security
  - Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/neuvector/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: neuvector:neuvector
    name: NeuVector
    description: The NeuVector REST API enables automation of container security operations including vulnerability scanning, runtime policy management, configuration import/export, packet capture, container quarantine, CVE database queries, and federated cluster management. Two authentication options are supported - username/password sessions and API key tokens. The published OpenAPI (Swagger 2.0) describes the full surface.
    humanURL: https://open-docs.neuvector.com/
    baseURL: https://localhost:10443
    tags:
      - Compliance
      - Containers
      - Kubernetes
      - Runtime Protection
      - Security
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://open-docs.neuvector.com/
      - type: Getting Started
        url: https://open-docs.neuvector.com/deploying
      - type: API Reference
        url: https://open-docs.neuvector.com/automation/automation
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/neuvector/refs/heads/main/openapi/neuvector-openapi-original.yaml
      - type: Source OpenAPI
        url: https://github.com/neuvector/neuvector/blob/main/controller/api/apis.yaml
      - type: Source Code
        url: https://github.com/neuvector/neuvector
    contact:
      - FN: NeuVector Support
        email: support@neuvector.com
common:
  - type: Website
    url: https://neuvector.com/
  - type: Documentation
    url: https://open-docs.neuvector.com/
  - type: SUSE Documentation
    url: https://documentation.suse.com/en-us/cloudnative/security/
  - type: GitHub Organization
    url: https://github.com/neuvector
  - type: SUSE Product Page
    url: https://www.suse.com/products/neuvector/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
