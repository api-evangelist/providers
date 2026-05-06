---
aid: hashicorp
name: HashiCorp
description: HashiCorp is the infrastructure cloud company, helping organizations automate multi-cloud and hybrid environments with Infrastructure Lifecycle Management and Security Lifecycle Management. Their suite of products includes Vault, Terraform, Nomad, Consul, Vagrant, Boundary, and Packer.
url: https://raw.githubusercontent.com/api-evangelist/hashicorp/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - DevOps
  - Infrastructure
  - Platform
created: '2024-02-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hashicorp:hashicorp-vault
    name: HashiCorp Vault
    tags:
      - Secrets Management
      - Security
    humanURL: https://developer.hashicorp.com/vault
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vault/api-docs
      - type: Getting Started
        url: https://developer.hashicorp.com/vault/tutorials
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/hashicorp/refs/heads/main/openapi/hashicorp-vault-openapi.yml
    description: Secure, store, and tightly control access to tokens, passwords, certificates, encryption keys for protecting secrets, and other sensitive data using a UI, CLI, or HTTP API.
  - aid: hashicorp:hashicorp-terraform
    name: HashiCorp Terraform
    tags:
      - Infrastructure as Code
      - Provisioning
    humanURL: https://developer.hashicorp.com/terraform
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/terraform/docs
      - type: Getting Started
        url: https://developer.hashicorp.com/terraform/tutorials
    description: Terraform is an infrastructure as code tool that lets you build, change, and version infrastructure safely and efficiently.
  - aid: hashicorp:hashicorp-nomad
    name: HashiCorp Nomad
    tags:
      - Orchestration
      - Scheduling
    humanURL: https://developer.hashicorp.com/nomad
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/nomad/api-docs
    description: A simple and flexible scheduler and orchestrator to deploy and manage containers and non-containerized applications across on-prem and clouds.
  - aid: hashicorp:hashicorp-consul
    name: HashiCorp Consul
    tags:
      - Service Discovery
      - Service Mesh
    humanURL: https://developer.hashicorp.com/consul
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/api-docs
    description: Consul is a service networking solution that enables teams to manage secure network connectivity between services and across multi-cloud environments.
  - aid: hashicorp:hashicorp-boundary
    name: HashiCorp Boundary
    tags:
      - Access Management
      - Security
    humanURL: https://developer.hashicorp.com/boundary
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/boundary/api-docs
    description: Securely access any system from anywhere based on user identity.
  - aid: hashicorp:hashicorp-vagrant
    name: HashiCorp Vagrant
    tags:
      - Development Environments
      - Virtual Machines
    humanURL: https://developer.hashicorp.com/vagrant
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vagrant/docs
    description: Vagrant is the command line utility for managing the lifecycle of virtual machines for isolated, consistent development environments.
common:
  - type: Portal
    url: https://developer.hashicorp.com/
  - type: Getting Started
    url: https://developer.hashicorp.com/tutorials
  - type: Support
    url: https://support.hashicorp.com/hc/en-us
  - type: Community
    url: https://discuss.hashicorp.com/
  - type: Status
    url: https://status.hashicorp.com/
  - type: Blog
    url: https://www.hashicorp.com/blog
  - type: Terms of Service
    url: https://www.hashicorp.com/terms-of-service
  - type: Privacy Policy
    url: https://www.hashicorp.com/privacy
  - type: GitHub Organization
    url: https://github.com/hashicorp
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
