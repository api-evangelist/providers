---
aid: hcp
name: HashiCorp Cloud Platform
description: HashiCorp Cloud Platform (HCP) is a fully managed platform for HashiCorp products including Vault, Consul, Packer, Boundary, Waypoint, and Terraform. HCP provides a unified set of APIs for managing infrastructure, secrets, service networking, and image pipelines across cloud and on-premises environments.
url: https://raw.githubusercontent.com/api-evangelist/hcp/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Infrastructure
  - DevOps
  - Secrets Management
  - Service Networking
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hcp:hcp-vault-secrets
    name: HCP Vault Secrets API
    description: The HCP Vault Secrets API enables programmatic management of applications, secrets, and integrations within HashiCorp Cloud Platform Vault Secrets, a multi-tenant secrets management service.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/vault-secrets
    baseURL: https://api.cloud.hashicorp.com
    tags:
      - Secrets Management
      - Vault
      - Cloud
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/vault-secrets
  - aid: hcp:hcp-packer
    name: HCP Packer API
    description: The HCP Packer API provides programmatic access to manage image buckets, channels, and iterations, enabling automated image pipelines and golden image management across cloud providers.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/packer
    baseURL: https://api.cloud.hashicorp.com
    tags:
      - Packer
      - Images
      - DevOps
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/packer
  - aid: hcp:hcp-consul
    name: HCP Consul API
    description: The HCP Consul API enables management of HCP Consul clusters, including provisioning, scaling, and federation for service networking and service mesh deployments.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/consul
    baseURL: https://api.cloud.hashicorp.com
    tags:
      - Consul
      - Service Mesh
      - Service Networking
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/consul
  - aid: hcp:hcp-boundary
    name: HCP Boundary API
    description: The HCP Boundary API provides programmatic access to identity-based secure remote access for managing users, hosts, sessions, and access policies in HashiCorp Cloud Platform Boundary.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/boundary
    baseURL: https://api.cloud.hashicorp.com
    tags:
      - Boundary
      - Remote Access
      - Identity
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/boundary
  - aid: hcp:hcp-waypoint
    name: HCP Waypoint API
    description: The HCP Waypoint API enables programmatic management of application templates, add-ons, and deployment workflows for delivering golden patterns to developer teams.
    humanURL: https://developer.hashicorp.com/hcp/api-docs/waypoint
    baseURL: https://api.cloud.hashicorp.com
    tags:
      - Waypoint
      - Application Delivery
      - DevOps
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/hcp/api-docs/waypoint
common:
  - type: Website
    url: https://cloud.hashicorp.com
  - type: Developer
    url: https://developer.hashicorp.com/hcp
  - type: Documentation
    url: https://developer.hashicorp.com/hcp/docs
  - type: API Documentation
    url: https://developer.hashicorp.com/hcp/api-docs
  - type: Status
    url: https://status.hashicorp.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
