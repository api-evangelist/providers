---
aid: sophos
name: Sophos
description: Sophos is a global cybersecurity leader delivering advanced endpoint protection, network security, cloud security, and SIEM integration through the Sophos Central platform. The Sophos Central API enables partners, organizations, and tenants to automate security operations including alert management, event retrieval, endpoint policy enforcement, and threat response.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cybersecurity
  - Endpoint Protection
  - Security
  - SIEM
  - Threat Detection
  - Incident Response
created: '2025-02-08'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sophos/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sophos:sophos-central-siem-api
    name: Sophos Central SIEM API
    description: The Sophos Central SIEM API provides access to security alerts and events for automating threat detection, incident response, and SIEM integration workflows. Retrieve real-time alerts and events from Sophos Central to feed into security operations tooling and SIEM platforms.
    humanURL: https://developer.sophos.com/
    baseURL: https://api1.central.sophos.com/gateway
    tags:
      - Cybersecurity
      - SIEM
      - Alerts
      - Events
      - Security Operations
    properties:
      - type: Documentation
        url: https://developer.sophos.com/intro
      - type: Reference
        url: https://developer.sophos.com/apis
      - type: Getting Started
        url: https://developer.sophos.com/getting-started
      - type: Change Log
        url: https://developer.sophos.com/whatsnew
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sophos/refs/heads/main/openapi/sophos-central-siem-openapi.yml
    contact:
      - FN: Sophos Developer Support
        url: https://developer.sophos.com/
        email: ''
common:
  - type: Portal
    url: https://developer.sophos.com/
  - type: Documentation
    url: https://developer.sophos.com/intro
  - type: Website
    url: https://www.sophos.com/
  - type: Community
    url: https://community.sophos.com/sophos-central-api
  - type: GitHub Org
    url: https://github.com/sophos
  - type: Postman Collection
    url: https://github.com/sophos/sophos-central-apis-postman
  - type: Integrations
    url: https://www.sophos.com/en-us/integrations
  - type: Support
    url: https://support.sophos.com/
  - type: Blog
    url: https://news.sophos.com/
  - type: Use Cases
    url: https://www.sophos.com/en-us/use-cases
  - type: Partners
    url: https://www.sophos.com/en-us/partners
  - type: Pricing
    url: https://www.sophos.com/en-us/products
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
