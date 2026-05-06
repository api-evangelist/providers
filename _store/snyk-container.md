---
aid: snyk-container
name: Snyk Container
description: Snyk Container helps developers find and fix vulnerabilities in container images and Kubernetes workloads. It integrates into existing development workflows to provide continuous security monitoring throughout the container lifecycle, scanning Docker images, Kubernetes manifests, and Helm charts for known CVEs and misconfigurations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Images
  - Containers
  - Kubernetes
  - Security
  - Vulnerability Management
  - DevSecOps
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/snyk-container/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: snyk-container:snyk-container
    name: Snyk Container
    description: Snyk Container helps developers find and fix vulnerabilities in container images and Kubernetes workloads, integrating into existing development workflows to provide continuous security monitoring throughout the container lifecycle.
    humanURL: https://snyk.io/product/container-vulnerability-management/
    tags:
      - Container Images
      - Containers
      - Kubernetes
      - Security
      - Vulnerability Management
      - DevSecOps
    properties:
      - type: Documentation
        url: https://docs.snyk.io/scan-using-snyk/snyk-container
      - type: Getting Started
        url: https://docs.snyk.io/getting-started
      - type: OpenAPI
        url: openapi/snyk-container-openapi.yml
      - type: JSON Schema
        url: json-schema/snyk-container-project-schema.json
      - type: JSON Schema
        url: json-schema/snyk-container-issue-schema.json
      - type: JSON Structure
        url: json-structure/snyk-container-project-structure.json
      - type: JSON-LD Context
        url: json-ld/snyk-container-context.jsonld
      - type: Spectral Rules
        url: rules/snyk-container-rules.yml
      - type: Capabilities
        url: capabilities/container-security.yaml
common:
  - type: Website
    url: https://snyk.io/
  - type: Documentation
    url: https://docs.snyk.io/scan-using-snyk/snyk-container
  - type: Getting Started
    url: https://docs.snyk.io/getting-started
  - type: GitHub Organization
    url: https://github.com/snyk
  - type: Blog
    url: https://snyk.io/blog/
  - type: Pricing
    url: https://snyk.io/plans/
  - type: Sign Up
    url: https://app.snyk.io/signup
  - type: REST API
    url: https://apidocs.snyk.io/
  - type: API Documentation
    url: https://docs.snyk.io/snyk-api
  - type: Changelog
    url: https://docs.snyk.io/snyk-api/changelog
  - type: SDK
    url: https://github.com/snyk/snyk-sdk-java
  - type: CLI
    url: https://github.com/snyk/cli
  - type: Kubernetes Operator
    url: https://github.com/snyk/kubernetes-monitor
  - type: Vocabulary
    url: vocabulary/snyk-container-vocabulary.yml
  - type: Examples
    url: examples/snyk-container-list-projects-example.json
  - type: Examples
    url: examples/snyk-container-list-issues-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
