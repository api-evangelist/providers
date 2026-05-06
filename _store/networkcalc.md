---
aid: networkcalc
name: NetworkCalc
description: NetworkCalc provides a free RESTful API platform for monitoring and managing business networks and domains. Public APIs include a subnet calculator, DNS tools, security tools, encoder, and binary converter, with additional authenticated APIs for alerts, authorization, domains, reports, and subnets.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Networking
  - DNS
  - Security
  - Subnetting
  - Domains
  - Calculator
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: networkcalc:networkcalc
    name: NetworkCalc
    description: The NetworkCalc API provides RESTful endpoints for subnet calculation (IPv4 and IPv6), DNS lookups, SSL/TLS security inspection, encoding and decoding utilities, and binary/decimal/hex conversion. Responses are JSON over HTTPS. Account-level APIs cover alerts, authorization, domains, reports, and subnets.
    humanURL: https://networkcalc.com/
    baseURL: https://networkcalc.com/api
    tags:
      - Networking
      - DNS
      - Security
      - Subnetting
      - Encoder
    properties:
      - type: Documentation
        url: https://networkcalc.com/api/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/networkcalc/refs/heads/main/openapi/networkcalc-openapi-original.yaml
      - type: Subnet Calculator Docs
        url: https://networkcalc.com/api/docs/subnet-calculator
      - type: DNS Tools Docs
        url: https://networkcalc.com/api/docs/dns
      - type: Security Tools Docs
        url: https://networkcalc.com/api/docs/security
      - type: Encoder Docs
        url: https://networkcalc.com/api/docs/encoder
      - type: Binary Converter Docs
        url: https://networkcalc.com/api/docs/binary-converter
    contact:
      - FN: NetworkCalc
        url: https://networkcalc.com/
common:
  - type: Website
    url: https://networkcalc.com/
  - type: Documentation
    url: https://networkcalc.com/api/docs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
