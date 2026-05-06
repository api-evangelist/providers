---
aid: stackrox
name: StackRox
description: StackRox is the open source upstream project for Red Hat Advanced Cluster Security for Kubernetes. It provides risk analysis, visibility, runtime alerts, and recommendations to proactively improve security by hardening containerized environments across build, deploy, and runtime stages. The platform performs compliance checking against standards like CIS, NIST, and PCI-DSS, and manages security policies across Kubernetes clusters.
url: https://raw.githubusercontent.com/api-evangelist/stackrox/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Compliance
  - Container Security
  - Kubernetes
  - Open Source
  - Runtime Protection
  - Security
type: Index
access: 3rd-Party
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stackrox:stackrox-api
    name: StackRox API
    description: The StackRox REST API provides programmatic access to the StackRox Kubernetes Security Platform. Covers alerts, deployments, images, policies, compliance, clusters, network policies, roles, API tokens, vulnerability management, and system configuration.
    humanURL: https://www.stackrox.io/docs/
    tags:
      - Compliance
      - Container Security
      - Kubernetes
      - Runtime Protection
      - Security
    properties:
      - type: Documentation
        url: https://www.stackrox.io/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stackrox/refs/heads/main/openapi/stackrox-openapi.yml
      - type: GitHub
        url: https://github.com/stackrox/stackrox
common:
  - type: Website
    url: https://www.stackrox.io/
    name: StackRox Community
  - type: Documentation
    url: https://www.stackrox.io/docs/
    name: StackRox Documentation
  - type: Blog
    url: https://www.stackrox.io/blog/
    name: StackRox Blog
  - type: GitHubOrganization
    url: https://github.com/stackrox
    name: StackRox GitHub Organization
  - type: GitHubRepository
    url: https://github.com/stackrox/stackrox
    name: StackRox Main Repository
  - type: RedHatProduct
    url: https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes
    name: Red Hat Advanced Cluster Security
  - type: CommunitySlack
    url: https://cloud-native.slack.com/
    name: Cloud Native Slack
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
