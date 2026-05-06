---
aid: cloudchipr
name: CloudChipr
url: https://raw.githubusercontent.com/api-evangelist/cloudchipr/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-27'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Azure
  - Cloud Cost Management
  - Cost Optimization
  - FinOps
  - GCP
  - Multi-Cloud
  - Resource Cleanup
  - Rightsizing
description: CloudChipr is a cloud cost-management and FinOps platform that consolidates AWS, Azure, and GCP spend in a single console and automates resource cleanup, rightsizing, and cost governance. The product surface centres on dashboards, automated workflows, budget alerts, and integrations with email, Slack, Microsoft Teams, Jira, and webhooks. CloudChipr exposes an API Reference at docs.cloudchipr.com/reference for programmatic access; specific endpoints, base URL, and authentication mechanism are documented in that portal.
apis:
  - aid: cloudchipr:cloudchipr-api
    name: CloudChipr API
    tags:
      - Cloud Cost Management
      - FinOps
      - Multi-Cloud
      - Rightsizing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cloudchipr.com/reference
    properties:
      - url: https://docs.cloudchipr.com/reference
        type: Documentation
      - url: https://docs.cloudchipr.com/
        type: GettingStarted
      - url: https://docs.cloudchipr.com/docs/aws-supported-services
        type: Reference
      - url: https://docs.cloudchipr.com/reference/integrations
        type: Integrations
    description: 'CloudChipr publishes a developer API Reference at docs.cloudchipr.com/reference covering the same multi-cloud cost-management capabilities as the web app: connecting cloud provider accounts, viewing inventoried resources and rightsizing recommendations, running automated workflows, and configuring integrations such as Slack, Jira, and webhooks. Specific endpoint paths and authentication details are maintained in that portal and gated by an account login.'
common:
  - type: Website
    url: https://cloudchipr.com/
  - type: Portal
    url: https://docs.cloudchipr.com/
  - type: Documentation
    url: https://docs.cloudchipr.com/reference
  - type: Pricing
    url: https://cloudchipr.com/pricing
  - type: Blog
    url: https://cloudchipr.com/blog
  - type: GitHubOrg
    url: https://github.com/cloudchipr
  - type: FinOpsMember
    url: https://www.finops.org/members/cloudchipr/
  - type: Naftiko Capabilities
    url: capabilities/cloudchipr-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
