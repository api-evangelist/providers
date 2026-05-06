---
aid: linode
url: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/apis.yml
apis:
  - aid: linode:api-v4
    name: Linode API V4
    tags:
      - Cloud Computing
      - Infrastructure
      - REST API
      - Virtual Machines
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.linode.com/v4
    humanURL: https://techdocs.akamai.com/linode-api/reference/api
    properties:
      - url: https://techdocs.akamai.com/linode-api/reference/api
        type: Documentation
      - url: openapi/linode-api-v4-openapi.yml
        type: OpenAPI
    description: The Linode API v4 provides programmatic access to the full range of Akamai Connected Cloud (formerly Linode) products and services. It enables developers to create and manage compute instances, deploy Kubernetes clusters, configure NodeBalancers, manage DNS domains, provision Block Storage volumes, control Object Storage buckets, set up firewalls, and administer account settings.
  - aid: linode:cli
    name: Linode CLI
    tags:
      - Automation
      - CLI
      - Command Line
      - DevOps
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://techdocs.akamai.com/cloud-computing/docs/cli
    properties:
      - url: https://techdocs.akamai.com/cloud-computing/docs/cli
        type: Documentation
    description: The Linode CLI is a command-line interface that wraps the Linode API v4, allowing developers and system administrators to manage Akamai Connected Cloud resources directly from the terminal. It supports all API operations including creating and managing compute instances, configuring networking, deploying Kubernetes clusters, and managing storage.
  - aid: linode:python-sdk
    name: Linode Python SDK
    tags:
      - Client Library
      - Python
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://linode-api4.readthedocs.io/en/latest/
    properties:
      - url: https://linode-api4.readthedocs.io/en/latest/
        type: Documentation
    description: The Linode Python SDK (linode_api4) is the official Python client library for interacting with the Linode API v4. It provides a Pythonic interface for managing all Akamai Connected Cloud resources including compute instances, domains, NodeBalancers, volumes, Kubernetes clusters, and account settings. The SDK supports both synchronous operations and includes helper methods for common workflows like deploying instances from StackScripts, managing SSH keys, and configuring networking resources.
  - aid: linode:go-sdk
    name: Linode Go SDK
    tags:
      - Client Library
      - Go
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://pkg.go.dev/github.com/linode/linodego
    properties:
      - url: https://pkg.go.dev/github.com/linode/linodego
        type: Documentation
    description: The Linode Go SDK (linodego) is the official Go client library for the Linode API v4. It provides idiomatic Go interfaces for managing Akamai Connected Cloud infrastructure programmatically, including compute instances, Kubernetes clusters, networking configurations, storage volumes, and DNS domains. The library is used internally by the Linode Terraform Provider and Linode CLI, and supports context-based request cancellation, pagination helpers, and retry logic for robust API interactions.
  - aid: linode:terraform-provider
    name: Linode Terraform Provider
    tags:
      - Automation
      - DevOps
      - Infrastructure as Code
      - Terraform
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://techdocs.akamai.com/terraform/docs/overview
    properties:
      - url: https://techdocs.akamai.com/terraform/docs/overview
        type: Documentation
    description: The Linode Terraform Provider enables infrastructure-as-code management of Akamai Connected Cloud resources using HashiCorp Terraform. It supports provisioning and managing compute instances, Kubernetes clusters, NodeBalancers, firewalls, DNS domains, Block Storage volumes, Object Storage buckets, VPCs, and other cloud resources through declarative configuration files.
common:
  - type: JSON-LD
    url: json-ld/linode-context.jsonld
  - type: JSONSchema
    url: json-schema/linode-instance-schema.json
  - type: Features
    data:
      - Nanode 1 GB at $5/mo (smallest plan)
      - Shared CPU 4 GB at $20/mo (most popular)
      - Dedicated CPU 4 GB at $36/mo
      - High Memory from $60/mo
      - GPU (NVIDIA Blackwell) from ~$1.50/hr
      - Distributed Compute Regions (200+ edge locations)
      - Hourly billing capped at monthly rate
      - 'API v4: 800 req/2-min default'
      - 'Linode create/boot: 25 req/min'
      - 'Object Storage (S3-compatible): $5/250 GB'
      - 'NodeBalancer (load balancer): $10/mo'
      - 'Backups: $2-$60/mo'
      - 'Linode Kubernetes Engine (LKE): control plane free'
      - Managed Databases (Postgres, MySQL, MongoDB)
      - Personal access tokens (PATs)
      - Now Akamai Cloud Computing (Linode brand retired)
    sources:
      - https://www.linode.com/pricing/
    updated: '2026-05-04'
modified: '2026-05-04'
description: Linode is a cloud hosting provider offering virtual private servers, managed databases, object storage, Kubernetes, and other infrastructure-as-a-service products to developers and businesses.
---
