---
aid: google-cloud-dns
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-dns/refs/heads/main/apis.yml
apis:
- name: Google Cloud DNS API
  description: The Cloud DNS API enables programmatic management of DNS zones and resource record sets, including creating and configuring managed zones, adding and modifying DNS records, and managing DNS policies for private zones.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/dns/docs/reference/v1
  baseURL: https://dns.googleapis.com
  tags:
  - Changes
  - DNS Policies
  - Managed Zones
  - Resource Record Sets
  properties:
  - type: Documentation
    url: https://cloud.google.com/dns/docs/reference/v1
  - type: OpenAPI
    url: openapi/dns-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/dns/docs/quickstart
  - type: JSONSchema
    url: json-schema/dns-managedzone.json
name: Google Cloud DNS
tags:
- DNS
- Domain Names
- Google Cloud
- Name Resolution
- Networking
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud DNS is a scalable, reliable, and managed authoritative Domain Name System (DNS) service running on the same infrastructure as Google. It provides low-latency, high-availability DNS serving with 100% uptime SLA, supporting both public and private DNS zones for domain name resolution.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

