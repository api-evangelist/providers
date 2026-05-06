---
aid: apiclarity
name: APIClarity
description: APIClarity is an open source API security and observability tool that analyzes API traffic to reconstruct OpenAPI specifications, detect shadow and zombie APIs, identify API differences and changes, and provide API security alerts. It is part of the OpenClarity project and works with Kubernetes service meshes and API gateways for cloud-native API traffic observability.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Observability
  - API Security
  - API Traffic Analysis
  - Cisco
  - Kubernetes
  - Open Source
  - OpenAPI Reconstruction
  - OpenClarity
  - Service Mesh
  - Shadow APIs
url: https://raw.githubusercontent.com/api-evangelist/apiclarity/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apiclarity:apiclarity-api
    name: APIClarity API
    description: The APIClarity API provides programmatic access to API traffic analysis, reconstructed OpenAPI specifications, API inventory, and security findings. It allows users to query discovered APIs, review spec diffs between observed and documented API behavior, and manage API security alerts.
    humanURL: https://github.com/openclarity/apiclarity
    tags:
      - API Inventory
      - API Security
      - API Traffic Analysis
      - OpenAPI Reconstruction
      - Shadow APIs
    properties:
      - type: Documentation
        url: https://github.com/openclarity/apiclarity#readme
      - type: OpenAPI
        url: https://github.com/openclarity/apiclarity/blob/master/api/server/restapi/spec.json
      - type: GettingStarted
        url: https://github.com/openclarity/apiclarity#getting-started
      - type: GitHubRepository
        url: https://github.com/openclarity/apiclarity
common:
  - type: Website
    url: https://openclarity.io
  - type: GitHubOrganization
    url: https://github.com/openclarity
  - type: GitHubRepository
    url: https://github.com/openclarity/apiclarity
  - type: Documentation
    url: https://github.com/openclarity/apiclarity#readme
  - type: Issues
    url: https://github.com/openclarity/apiclarity/issues
  - type: Releases
    url: https://github.com/openclarity/apiclarity/releases
  - type: License
    url: https://github.com/openclarity/apiclarity/blob/master/LICENSE
  - type: Slack
    url: https://outshift.slack.com
  - type: Features
    data:
      - name: OpenAPI Spec Reconstruction
        description: Automatically reconstruct OpenAPI specifications from observed live API traffic without code instrumentation.
      - name: Shadow API Detection
        description: Identify undocumented shadow APIs being called in production that are not reflected in official specifications.
      - name: Zombie API Detection
        description: Detect deprecated or decommissioned API endpoints still receiving traffic in production.
      - name: API Diff Analysis
        description: Compare observed API behavior against documented specifications to identify drifts, changes, and violations.
      - name: API Security Alerts
        description: Generate security findings and alerts based on API traffic analysis and specification violations.
      - name: Kubernetes Integration
        description: Deploy as a sidecar or via Helm charts for integration with Kubernetes service meshes and API gateways.
      - name: API Inventory
        description: Automatically build and maintain an inventory of all APIs discovered in the environment.
  - type: UseCases
    data:
      - name: API Discovery
        description: Discover all APIs running in a Kubernetes environment including undocumented and shadow APIs.
      - name: API Security Posture Assessment
        description: Assess API security by detecting shadow APIs, spec violations, and suspicious traffic patterns.
      - name: API Specification Generation
        description: Generate OpenAPI specifications from live traffic for APIs that lack formal documentation.
      - name: API Governance
        description: Enforce API consistency by detecting deviations between actual API behavior and official specifications.
      - name: Incident Response
        description: Investigate API security incidents using traffic analysis, API inventory, and spec diff data.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
