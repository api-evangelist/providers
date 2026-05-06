---
aid: env0
name: Env0
description: env0 is an infrastructure-as-code automation platform providing cost estimation, policy enforcement, and self-service environments for Terraform, OpenTofu, Pulumi, CloudFormation, and Kubernetes workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FinOps
  - Infrastructure as Code
  - DevOps
  - Cloud
url: https://raw.githubusercontent.com/api-evangelist/env0/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: env0:env0
    name: Env0
    description: env0 is an infrastructure-as-code automation platform providing cost estimation, policy enforcement, and self-service environments. The public REST API is available at https://api.env0.com/ and uses HTTP Basic authentication with API key credentials. Rate limits are 1,000 requests per 60 seconds.
    humanURL: https://www.env0.com/
    baseURL: https://api.env0.com/
    tags:
      - FinOps
      - Infrastructure as Code
    properties:
      - type: Documentation
        url: https://docs.env0.com/
      - type: API Reference
        url: https://docs.env0.com/reference/api-introduction
      - type: Getting Started
        url: https://docs.env0.com/docs/getting-started
      - type: Authentication
        url: https://docs.env0.com/reference/authentication
common:
  - type: Website
    url: https://www.env0.com/
  - type: Documentation
    url: https://docs.env0.com/
  - type: API Reference
    url: https://docs.env0.com/reference/api-introduction
  - type: Pricing
    url: https://www.env0.com/pricing
  - type: Blog
    url: https://www.env0.com/blog
  - type: GitHub
    url: https://github.com/env0
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
