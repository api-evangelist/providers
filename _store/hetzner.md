---
aid: hetzner
url: https://raw.githubusercontent.com/api-evangelist/hetzner/refs/heads/main/apis.yml
apis:
- aid: hetzner:hetzner-dns-api
  name: Hetzner DNS API
  description: The Hetzner DNS API provides programmatic access to manage DNS zones, records, and configurations for domains hosted with Hetzner's DNS service.
  humanURL: https://dns.hetzner.com/api-docs
  baseURL: https://dns.hetzner.com/api/v1
  tags:
  - DNS
  - Domain Management
  properties:
  - type: Documentation
    url: https://dns.hetzner.com/api-docs
  - type: Authentication
    url: https://dns.hetzner.com/api-docs#section/Authentication
- aid: hetzner:hetzner-cloud-api
  name: Hetzner Cloud API
  description: The Hetzner Cloud API allows managing cloud servers, load balancers, networks, firewalls, volumes, and other cloud resources programmatically.
  humanURL: https://docs.hetzner.cloud/
  baseURL: https://api.hetzner.cloud/v1
  tags:
  - Cloud
  - Infrastructure
  - Servers
  properties:
  - type: Documentation
    url: https://docs.hetzner.cloud/
  - type: OpenAPI
    url: https://docs.hetzner.cloud/spec.json
  - type: Getting Started
    url: https://docs.hetzner.cloud/#getting-started
name: Hetzner
tags:
- Cloud Hosting
- DNS
- Infrastructure
- Servers
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-09'
modified: '2026-04-07'
position: Consumer
description: Hetzner Online is a German hosting provider offering cloud servers, dedicated servers, and domain services. Hetzner provides a Cloud API for programmatic management of cloud resources, as well as a DNS API for managing DNS zones and records.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

