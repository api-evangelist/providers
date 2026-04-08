---
aid: amazon-fsx
url: https://raw.githubusercontent.com/api-evangelist/amazon-fsx/refs/heads/main/apis.yml
apis:
- name: Amazon FSx API
  description: The Amazon FSx API enables programmatic access to create, manage, and monitor fully managed file systems. You can create file systems, manage backups, configure data repositories, create snapshots, and manage storage virtual machines across multiple file system types.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/fsx/
  baseURL: https://fsx.amazonaws.com
  tags:
  - File Systems
  - High Performance
  - Managed Services
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/fsx/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: openapi/amazon-fsx-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/fsx/2018-03-01/openapi.json
  - type: JSON Schema
    url: json-schema/amazon-fsx-schema.json
  - type: JSON-LD
    url: json-ld/amazon-fsx-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/fsx/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/fsx/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/fsx/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html
  - type: API Reference
    url: https://docs.aws.amazon.com/fsx/latest/APIReference/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/fsx/
  - type: Security
    url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/security.html
name: Amazon FSx
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon FSx provides fully managed file systems with the native compatibility and feature sets for workloads that require shared file storage. FSx supports four widely-used file systems including NetApp ONTAP, OpenZFS, Windows File Server, and Lustre, delivering high performance and low latency access to data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

