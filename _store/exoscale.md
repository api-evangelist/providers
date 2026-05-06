---
aid: exoscale
name: Exoscale
description: Exoscale is a Swiss cloud infrastructure provider offering secure, reliable, and scalable cloud solutions to businesses of all sizes. Their services include virtual machines, object storage, networking, security, Kubernetes (SKS), Database as a Service (DBaaS), and IAM. Data centers are located in Switzerland, Austria, Germany, and Bulgaria, providing data sovereignty and compliance with European data protection regulations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Infrastructure
  - Compute
  - Storage
  - Kubernetes
  - DBaaS
  - Europe
url: https://raw.githubusercontent.com/api-evangelist/exoscale/refs/heads/main/apis.yml
created: '2025-01-07'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: exoscale:exoscale
    name: Exoscale API
    description: Infrastructure automation API allowing programmatic access to all Exoscale products and services, including Compute, SKS (Kubernetes), DBaaS, IAM, Object Storage, KMS, networking, and load balancing.
    humanURL: https://openapi-v2.exoscale.com/
    baseURL: https://api-ch-gva-2.exoscale.com/v2
    tags:
      - Cloud
      - Compute
      - Kubernetes
      - DBaaS
      - IAM
      - Storage
    properties:
      - type: Documentation
        url: https://openapi-v2.exoscale.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/exoscale/refs/heads/main/openapi/exoscale-openapi.yml
      - type: SignUp
        url: https://portal.exoscale.com/register
      - type: Pricing
        url: https://www.exoscale.com/pricing/
common:
  - type: Website
    url: https://www.exoscale.com
  - type: Documentation
    url: https://community.exoscale.com/documentation/
  - type: Portal
    url: https://portal.exoscale.com/
  - type: SignUp
    url: https://portal.exoscale.com/register
  - type: Pricing
    url: https://www.exoscale.com/pricing/
  - type: TermsOfService
    url: https://www.exoscale.com/terms/
  - type: PrivacyPolicy
    url: https://www.exoscale.com/privacy/
  - type: StatusPage
    url: https://www.exoscalestatus.com/
  - type: Blog
    url: https://www.exoscale.com/syslog/
  - type: GitHubOrganization
    url: https://github.com/exoscale
  - type: Support
    url: https://portal.exoscale.com/tickets
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
