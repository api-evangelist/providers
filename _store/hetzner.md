---
aid: hetzner
name: Hetzner
description: Hetzner Online is a German hosting provider offering cloud servers, dedicated servers, and domain services. Hetzner provides a Cloud API for programmatic management of cloud resources, as well as a DNS API for managing DNS zones and records.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Hosting
  - DNS
  - Infrastructure
  - Servers
url: https://raw.githubusercontent.com/api-evangelist/hetzner/refs/heads/main/apis.yml
created: '2025-02-09'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
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
        url: https://raw.githubusercontent.com/api-evangelist/hetzner/refs/heads/main/openapi/hetzner-openapi.yml
      - type: Getting Started
        url: https://docs.hetzner.cloud/#getting-started
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
common:
  - type: Website
    url: https://www.hetzner.com/
  - type: Documentation
    url: https://docs.hetzner.com/
  - type: Sign Up
    url: https://accounts.hetzner.com/signUp
  - type: Login
    url: https://accounts.hetzner.com/login
  - type: Status
    url: https://status.hetzner.com/
  - type: Support
    url: https://www.hetzner.com/support
  - type: Pricing
    url: https://www.hetzner.com/cloud
  - type: Privacy Policy
    url: https://www.hetzner.com/legal/privacy-policy
  - type: Terms of Service
    url: https://www.hetzner.com/legal/terms-and-conditions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
