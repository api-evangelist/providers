---
aid: wallarm
url: https://raw.githubusercontent.com/api-evangelist/wallarm/refs/heads/main/apis.yml
apis:
  - aid: wallarm:wallarm-api
    name: Wallarm API
    tags:
      - API Security
      - Attack Detection
      - Vulnerability Management
      - WAF
      - Rules
      - IP Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://us1.api.wallarm.com
    humanURL: https://docs.wallarm.com/api/overview/
    properties:
      - url: https://docs.wallarm.com/api/overview/
        type: Documentation
      - url: https://apiconsole.us1.wallarm.com/
        type: SwaggerUI
      - url: https://apiconsole.eu1.wallarm.com/
        type: SwaggerUI
      - url: openapi/wallarm-openapi.yml
        type: OpenAPI
      - url: rules/wallarm-rules.yml
        type: SpectralRules
      - url: capabilities/api-security-operations.yaml
        type: NaftikoCapabilities
      - url: json-schema/wallarm-attack-schema.json
        type: JSONSchema
      - url: json-schema/wallarm-vulnerability-schema.json
        type: JSONSchema
      - url: json-ld/wallarm-context.jsonld
        type: JSONLDContext
      - url: vocabulary/wallarm-vocabulary.yml
        type: Vocabulary
    description: The Wallarm API provides programmatic access to the Wallarm API Security Platform, enabling management of attacks, incidents, vulnerabilities, rules, IP lists, filter nodes, users, and integrations. The API is available on both the US Cloud (us1.api.wallarm.com) and EU Cloud (api.wallarm.com), and uses API token authentication via the X-WallarmApi-Token header.
name: Wallarm
tags:
  - API Security
  - Security Testing
  - WAF
  - Cybersecurity
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-05-03'
position: Consumer
description: Wallarm provides advanced API security and protection solutions for APIs, web applications, and microservices. The platform includes API discovery, real-time attack protection, vulnerability testing, and an open-source API Firewall that enforces OpenAPI specifications as a positive security model. Wallarm supports deployment on Kubernetes, cloud environments, and as an NGINX-based proxy.
common:
  - url: https://www.wallarm.com/
    name: Wallarm - Advanced API Security
    type: Website
  - url: https://docs.wallarm.com/
    name: Wallarm Documentation
    type: Documentation
  - url: https://docs.wallarm.com/api/overview/
    name: Wallarm API Reference
    type: Reference
  - url: https://docs.wallarm.com/api/request-examples/
    name: Wallarm API Request Examples
    type: Examples
  - url: https://apiconsole.us1.wallarm.com/
    name: Wallarm API Console (US)
    type: Console
  - url: https://apiconsole.eu1.wallarm.com/
    name: Wallarm API Console (EU)
    type: Console
  - url: https://github.com/wallarm
    name: Wallarm GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/wallarm/api-firewall
    name: Wallarm API Firewall
    type: OpenSource
  - url: https://github.com/wallarm/wallarm-go
    name: Wallarm Go SDK
    type: SDK
  - url: https://github.com/wallarm/terraform-provider-wallarm
    name: Wallarm Terraform Provider
    type: TerraformProvider
  - url: https://github.com/wallarm/terraform-aws-wallarm
    name: Wallarm Terraform AWS Module
    type: TerraformModule
  - url: https://github.com/wallarm/ingress
    name: Wallarm Kubernetes Ingress Controller
    type: SDK
  - url: https://github.com/wallarm/helm-charts
    name: Wallarm Helm Charts
    type: HelmChart
  - url: https://github.com/wallarm/gotestwaf
    name: GoTestWAF - WAF Security Testing Tool
    type: Tool
  - url: https://www.wallarm.com/product/integrations
    name: Wallarm Integrations
    type: Integrations
features:
  - API Discovery and Inventory
  - Real-Time Attack Detection and Blocking
  - Vulnerability Assessment and Management
  - API Firewall (OpenAPI-based positive security model)
  - Shadow and Zombie API Detection
  - IP List Management (allowlist, denylist, graylist)
  - Custom Security Rules Engine
  - SIEM and SOAR Integrations
  - Kubernetes-Native Deployment (sidecar, ingress)
  - Multi-Cloud and Hybrid Deployment Support
useCases:
  - Protect APIs from OWASP Top 10 attacks
  - Discover and inventory all APIs in a microservices environment
  - Enforce API contract compliance with OpenAPI specifications
  - Detect and respond to zero-day API vulnerabilities
  - Manage IP reputation lists and block malicious traffic
  - Automate security testing in CI/CD pipelines
integrations:
  - Splunk
  - PagerDuty
  - Slack
  - Jira
  - Microsoft Teams
  - OpsGenie
  - DataDog
  - Sumo Logic
  - AWS
  - Azure
  - Google Cloud
  - Kubernetes
  - Terraform
solutions:
  - API Security
  - Web Application Firewall
  - API Discovery
  - DevSecOps
  - Cloud Security
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
