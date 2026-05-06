---
aid: configure8
name: Configure8
description: Configure8 is a commercial Internal Developer Portal (IDP) that gives engineering organizations a unified catalog of services, environments, and resources, with dependency mapping across cloud and on-premises infrastructure. It pairs that catalog with scorecards for software health and golden-path compliance, no-code self-service actions for developers, and FinOps-style cloud cost visibility. Configure8 supports SaaS and self-hosted deployments and ships with enterprise features such as RBAC, SCIM, SSO, audit logging, and a public REST API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
tags:
  - Catalog
  - Cloud Cost
  - Developer Experience
  - DevOps
  - Internal Developer Portal
  - Platform Engineering
  - Scorecards
  - Self-Service
  - Service Catalog
  - SRE
apis:
  - aid: configure8:idp-rest-api
    name: Configure8 REST API
    description: The Configure8 REST API gives platform teams programmatic access to the service catalog, scorecards, self-service actions, environments, and cost data. It is used to ingest services and resources from external systems, drive scorecards in CI, trigger self-service actions, and synchronize the portal with source-of-truth systems. The API is part of the Configure8 enterprise feature set alongside RBAC, SSO/SCIM, and audit logging.
    humanURL: https://www.configure8.io/
    baseURL: https://app.configure8.io/api
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Catalog
      - REST
      - Scorecards
      - Self-Service
    properties:
      - type: Documentation
        url: https://docs.configure8.io/
      - type: Website
        url: https://www.configure8.io/
    x-features:
      - Service Catalog
      - Resource Catalog
      - Dependency Mapping
      - Scorecards
      - Self-Service Actions
      - No-Code Workflow Builder
      - Cloud Cost Visibility
      - RBAC and SSO
      - SCIM Provisioning
      - Self-Hosted or SaaS
    x-use-cases:
      - Catalog every service, environment, and resource in one place
      - Score services against production-readiness standards
      - Let developers self-serve infrastructure via the portal
      - Surface cloud spend per service and per team
      - Replace internal wikis with a living developer portal
common:
  - type: Website
    url: https://www.configure8.io/
  - type: Documentation
    url: https://docs.configure8.io/
  - type: Blog
    url: https://www.configure8.io/blog
  - type: Pricing
    url: https://www.configure8.io/pricing
  - type: Demo
    url: https://www.configure8.io/demo
  - type: Login
    url: https://app.configure8.io/
  - type: Platform Engineering
    url: https://platformengineering.org/tools/configur8
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
