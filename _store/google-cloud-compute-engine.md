---
aid: google-cloud-compute-engine
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-compute-engine/refs/heads/main/apis.yml
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
name: Google Cloud Compute Engine
tags:
- Compute
- Google Cloud
- IaaS
- Infrastructure
- Virtual Machines
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Compute Engine delivers virtual machines running in Google's innovative data centers and worldwide fiber network. Compute Engine VMs boot quickly, come with persistent disk storage, and deliver consistent performance. It offers predefined and custom machine types, preemptible VMs, and sole-tenant nodes for specialized workloads.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

