---
name: Google Cloud VPC
description: Google Cloud Virtual Private Cloud (VPC) provides networking functionality for Google Cloud resources, enabling you to create and manage virtual networks, subnets, firewall rules, and routes for secure and isolated cloud networking.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-vpc/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Firewall
  - Google Cloud
  - Networking
  - Virtual Networks
  - VPC
apis:
  - name: Google Cloud VPC API
    description: The Google Cloud VPC API enables programmatic management of virtual networks, subnets, firewall rules, routes, and peering connections within Google Cloud Platform.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/vpc/docs
    baseURL: https://compute.googleapis.com/compute/v1
    tags:
      - Firewall Rules
      - Networks
      - Subnets
      - VPC
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLDContext
        url: json-ld/json-ld.yml
common:
  - type: GettingStarted
    url: https://cloud.google.com/vpc/docs/overview
  - type: Pricing
    url: https://cloud.google.com/vpc/network-pricing
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
