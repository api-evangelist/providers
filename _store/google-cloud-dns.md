---
aid: google-cloud-dns
name: Google Cloud DNS
description: Google Cloud DNS is a scalable, reliable, and managed authoritative Domain Name System (DNS) service running on the same infrastructure as Google. It provides low-latency, high-availability DNS serving with 100% uptime SLA, supporting both public and private DNS zones for domain name resolution.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/google-cloud-dns/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - DNS
  - Domain Names
  - Google Cloud
  - Name Resolution
  - Networking
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
common:
  - type: Portal
    url: https://cloud.google.com/dns
  - type: Getting Started
    url: https://cloud.google.com/dns/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/dns/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/dns/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/dns/docs/support
  - type: JSON-LD
    url: json-ld/dns-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
