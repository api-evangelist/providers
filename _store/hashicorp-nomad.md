---
aid: hashicorp-nomad
name: HashiCorp Nomad
description: HashiCorp Nomad is a flexible workload orchestrator that enables organizations to deploy and manage containers, non-containerized applications, and batch jobs across on-premises and cloud environments. It provides a single unified workflow for scheduling diverse workloads with high availability and multi-region federation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - HashiCorp
  - Multi-Cloud
  - Orchestration
  - Scheduling
  - Workloads
url: https://raw.githubusercontent.com/api-evangelist/hashicorp-nomad/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hashicorp-nomad:hashicorp-nomad
    name: HashiCorp Nomad
    description: HashiCorp Nomad is a flexible workload orchestrator that deploys and manages containers, legacy applications, microservices, and batch jobs. It supports Docker, Java, VMs, and executables with a single binary architecture that provides high availability, multi-datacenter federation, and a simple operator experience.
    humanURL: https://www.nomadproject.io/
    tags:
      - Containers
      - HashiCorp
      - Multi-Cloud
      - Orchestration
      - Scheduling
      - Workloads
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/nomad/docs
      - type: API Documentation
        url: https://developer.hashicorp.com/nomad/api-docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/hashicorp-nomad/refs/heads/main/openapi/hashicorp-nomad-openapi.yml
      - type: Authentication
        url: https://developer.hashicorp.com/nomad/api-docs#authentication
      - type: Getting Started
        url: https://developer.hashicorp.com/nomad/tutorials/get-started
common:
  - type: Website
    url: https://www.nomadproject.io/
  - type: Documentation
    url: https://developer.hashicorp.com/nomad/docs
  - type: GitHub Organization
    url: https://github.com/hashicorp
  - type: GitHub Repository
    url: https://github.com/hashicorp/nomad
  - type: Blog
    url: https://www.hashicorp.com/blog/products/nomad
  - type: Pricing
    url: https://www.hashicorp.com/products/nomad/pricing
  - type: Sign Up
    url: https://portal.cloud.hashicorp.com/sign-up
  - type: Tutorials
    url: https://developer.hashicorp.com/nomad/tutorials
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
