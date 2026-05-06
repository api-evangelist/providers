---
aid: opslevel
name: OpsLevel
segments:
  - Experience
description: OpsLevel is a prescriptive internal developer portal for cataloging, measuring, and scaffolding services according to engineering best practices.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Portal
  - DevOps
  - Experience
  - Internal Developer Portal
  - Microservices
  - Platform Engineering
  - Service Catalog
  - Service Maturity
created: '2026-03-03'
modified: '2026-03-16'
url: https://raw.githubusercontent.com/api-evangelist/opslevel/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: opslevel:graphql-api
    name: OpsLevel GraphQL API
    description: The OpsLevel GraphQL API allows you to integrate OpsLevel with your other operational tools, enrich internal tickets, incidents, and other systems with service and team data pulled from OpsLevel. The API supports queries for data retrieval and mutations for data modification, with cursor-based pagination, bearer token authentication, and a rich data model covering services, teams, users, deployments, and infrastructure.
    humanURL: https://docs.opslevel.com/docs/graphql
    baseURL: https://api.opslevel.com
    tags:
      - Developer Portal
      - GraphQL
      - Platform Engineering
      - Service Catalog
    properties:
      - type: Documentation
        url: https://docs.opslevel.com/docs/graphql
      - type: Authentication
        url: https://docs.opslevel.com/docs/graphql
      - type: Getting Started
        url: https://docs.opslevel.com/docs/getting-started-with-service-creation
common:
  - type: Portal
    url: https://www.opslevel.com/
  - type: Developer Documentation
    url: https://docs.opslevel.com/
  - type: Blog
    url: https://www.opslevel.com/resource/blog
  - type: Sign Up
    url: https://www.opslevel.com/request-a-demo
  - type: Login
    url: https://app.opslevel.com/users/sign_in
  - type: Pricing
    url: https://www.opslevel.com/pricing
  - type: About
    url: https://www.opslevel.com/about
  - type: Status Page
    url: https://opslevelstatus.com/
  - type: Terms of Service
    url: https://www.opslevel.com/legal/t4-terms-of-service
  - type: Privacy Policy
    url: https://www.opslevel.com/legal/privacy
  - type: Security
    url: https://www.opslevel.com/legal/security
  - type: Contact
    url: https://www.opslevel.com/contact
  - type: GitHub Organization
    url: https://github.com/OpsLevel
  - type: LinkedIn
    url: https://www.linkedin.com/company/opslevel
  - type: Terraform Provider
    url: https://registry.terraform.io/providers/OpsLevel/opslevel/latest/docs
  - type: Integrations
    url: https://www.opslevel.com/integrations-overview
  - type: Customers
    url: https://www.opslevel.com/customers
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
