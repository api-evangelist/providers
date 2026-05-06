---
aid: google-cloud-compute-engine
name: Google Cloud Compute Engine
description: Google Cloud Compute Engine delivers virtual machines running in Google's innovative data centers and worldwide fiber network. Compute Engine VMs boot quickly, come with persistent disk storage, and deliver consistent performance. It offers predefined and custom machine types, preemptible VMs, and sole-tenant nodes for specialized workloads.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/google-cloud-compute-engine/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Compute
  - Google Cloud
  - IaaS
  - Infrastructure
  - Virtual Machines
apis:
  - name: Google Compute Engine API
    description: The Compute Engine API allows you to create and manage virtual machine instances, instance groups, disks, networks, firewalls, and other compute resources programmatically within Google Cloud.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/compute/docs/reference/rest/v1
    baseURL: https://compute.googleapis.com
    tags:
      - Disks
      - Firewalls
      - Instances
      - Networks
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://cloud.google.com/compute/docs/reference/rest/v1
      - type: OpenAPI
        url: openapi/compute-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/compute/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/compute/docs/quickstart-linux
      - type: JSONSchema
        url: json-schema/compute-instance.json
common:
  - type: Portal
    url: https://cloud.google.com/compute
  - type: Getting Started
    url: https://cloud.google.com/compute/docs/quickstart-linux
  - type: Documentation
    url: https://cloud.google.com/compute/docs
  - type: Authentication
    url: https://cloud.google.com/compute/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/compute/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/compute/docs/support
  - type: JSON-LD
    url: json-ld/compute-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
