---
aid: firecracker
name: Firecracker
description: Firecracker is an open source virtual machine monitor (VMM) built by Amazon Web Services that uses KVM to create and manage lightweight microVMs. Designed for serverless computing and container workloads, it provides the security and isolation of traditional VMs with the speed and resource efficiency of containers. Firecracker exposes a RESTful management API over a Unix Domain Socket, specified in OpenAPI (Swagger 2.0).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Containers
  - MicroVMs
  - Open Source
  - Serverless
  - Virtualization
  - KVM
url: https://raw.githubusercontent.com/api-evangelist/firecracker/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: firecracker:firecracker
    name: Firecracker API
    description: The Firecracker management API is a RESTful public-facing API accessible through HTTP calls over a Unix Domain Socket, carrying JSON modeled data. It is used to configure and control microVMs, including boot source, drives, network interfaces, machine configuration, snapshots, and lifecycle actions. Firecracker powers AWS Lambda and AWS Fargate.
    humanURL: https://github.com/firecracker-microvm/firecracker
    baseURL: http://localhost/
    tags:
      - AWS
      - Containers
      - MicroVMs
      - Open Source
      - Serverless
      - Virtualization
    properties:
      - type: Documentation
        url: https://github.com/firecracker-microvm/firecracker/tree/main/docs
      - type: Getting Started
        url: https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md
      - type: API Requests
        url: https://github.com/firecracker-microvm/firecracker/tree/main/docs/api_requests
      - type: OpenAPI
        url: openapi/firecracker-openapi-original.yaml
      - type: Specification
        url: https://github.com/firecracker-microvm/firecracker/blob/main/SPECIFICATION.md
      - type: Design
        url: https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md
common:
  - type: Website
    url: https://firecracker-microvm.github.io/
  - type: GitHub Organization
    url: https://github.com/firecracker-microvm
  - type: GitHub Repository
    url: https://github.com/firecracker-microvm/firecracker
  - type: Documentation
    url: https://github.com/firecracker-microvm/firecracker/tree/main/docs
  - type: Getting Started
    url: https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md
  - type: ChangeLog
    url: https://github.com/firecracker-microvm/firecracker/blob/main/CHANGELOG.md
  - type: FAQ
    url: https://github.com/firecracker-microvm/firecracker/blob/main/FAQ.md
  - type: Security
    url: https://github.com/firecracker-microvm/firecracker/blob/main/SECURITY.md
  - type: Blog
    url: https://aws.amazon.com/blogs/opensource/tag/firecracker/
  - type: Slack
    url: https://join.slack.com/t/firecracker-microvm/shared_invite/zt-2tc0mfxpc-tU~HYAYSzLDl5XGGJU3YIg
  - type: Email
    url: mailto:firecracker-maintainers@amazon.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
