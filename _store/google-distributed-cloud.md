---
aid: google-distributed-cloud
name: Google Distributed Cloud
description: Google Distributed Cloud provides fully managed hardware and software solutions that extend Google Cloud infrastructure and services to the edge and into customer data centers. It supports both connected and air-gapped deployments, enabling organizations to run workloads locally while leveraging Google Cloud management, security, and services.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-distributed-cloud/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Distributed Infrastructure
  - Edge Computing
  - Hardware
  - Hybrid Cloud
  - Kubernetes
  - On-Premises
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
common:
  - type: Portal
    url: https://cloud.google.com/distributed-cloud
  - type: Getting Started
    url: https://cloud.google.com/distributed-cloud/docs/overview
  - type: Documentation
    url: https://cloud.google.com/distributed-cloud/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/distributed-cloud/edge/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/distributed-cloud/docs/support
  - type: JSON-LD
    url: json-ld/google-distributed-cloud-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
