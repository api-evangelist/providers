---
aid: infracost
name: Infracost
description: Infracost is a cloud cost estimation tool for Terraform that shows infrastructure cost breakdowns and diffs directly in pull requests. Infracost provides an API for programmatic access to cloud pricing data and cost estimates.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Cost
  - FinOps
  - Infrastructure
  - Terraform
url: https://raw.githubusercontent.com/api-evangelist/infracost/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: infracost:infracost-api
    name: Infracost Cloud Pricing API
    description: The Infracost Cloud Pricing API provides programmatic access to cloud pricing data for infrastructure cost estimation. It powers the Infracost CLI and CI/CD integrations for showing cost breakdowns in pull requests.
    humanURL: https://www.infracost.io/docs/integrations/infracost_api/
    baseURL: https://pricing.api.infracost.io
    tags:
      - Cloud Cost
      - Infrastructure
      - Pricing
      - Terraform
    properties:
      - type: Documentation
        url: https://www.infracost.io/docs/integrations/infracost_api/
      - type: Getting Started
        url: https://www.infracost.io/docs/
      - type: OpenAPI
        url: openapi/infracost-openapi.yml
common:
  - type: Website
    url: https://www.infracost.io/
  - type: Documentation
    url: https://www.infracost.io/docs/
  - type: GitHub Organization
    url: https://github.com/infracost
  - type: Support
    url: https://www.infracost.io/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
