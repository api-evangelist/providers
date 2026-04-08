---
aid: google-distributed-cloud
url: https://raw.githubusercontent.com/api-evangelist/google-distributed-cloud/refs/heads/main/apis.yml
apis:
- name: Distributed Cloud Edge Network API
  description: The Distributed Cloud Edge Network API provides programmatic access to manage networking resources for Google Distributed Cloud connected deployments at the edge. Developers can use the API to create and manage networks, subnets, routers, and interconnect attachments for edge locations.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/distributed-cloud/edge/latest/docs
  baseURL: https://edgenetwork.googleapis.com
  tags:
  - Edge Network
  - Networking
  - Routers
  - Subnets
  properties:
  - type: Documentation
    url: https://cloud.google.com/distributed-cloud/edge/latest/docs/apis
  - type: OpenAPI
    url: openapi/distributed-cloud-edge-network-api-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/distributed-cloud/docs/overview
  - type: JSONSchema
    url: json-schema/google-distributed-cloud-network-schema.json
- name: GDC Hardware Management API
  description: The GDC Hardware Management API provides programmatic access to manage hardware lifecycle for Google Distributed Cloud deployments. Developers can use the API to track hardware orders, manage hardware groups, monitor hardware status, and handle site-level hardware configurations.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/distributed-cloud/connected/docs
  baseURL: https://gdchardwaremanagement.googleapis.com
  tags:
  - Hardware
  - Infrastructure
  - Provisioning
  properties:
  - type: Documentation
    url: https://cloud.google.com/distributed-cloud/connected/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
name: Google Distributed Cloud
tags:
- Distributed Infrastructure
- Edge Computing
- Hardware
- Hybrid Cloud
- Kubernetes
- On-Premises
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Distributed Cloud provides fully managed hardware and software solutions that extend Google Cloud infrastructure and services to the edge and into customer data centers. It supports both connected and air-gapped deployments, enabling organizations to run workloads locally while leveraging Google Cloud management, security, and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

