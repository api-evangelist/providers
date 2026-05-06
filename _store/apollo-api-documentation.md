---
aid: apollo-api-documentation
name: Apollo API Documentation
description: Apollo.io provides a comprehensive REST API for sales intelligence with over 210 million contacts and 35 million companies. The Apollo API enables data enrichment, people and organization search, CRM management, sequences, deals, analytics, and integrations. Authentication is via API keys or OAuth 2.0 for partner integrations. This repository profiles Apollo.io's API documentation as an example of API documentation best practices.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Documentation
  - Best Practices
  - Data Enrichment
  - People Search
  - Sales Intelligence
created: '2025-07-10'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apollo-api-documentation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apollo-api-documentation:apollo-rest-api
    name: Apollo REST API
    description: Apollo's REST API provides programmatic access to Apollo's sales intelligence database of 210M+ contacts and 35M+ companies. The API supports people enrichment, organization enrichment, people search, accounts and contacts management, deals, sequences, tasks, analytics reporting, and calls management. Access is controlled by the customer's Apollo plan tier.
    humanURL: https://docs.apollo.io/
    tags:
      - Analytics
      - CRM
      - Data Enrichment
      - Organization Search
      - People Search
      - REST
      - Sales Intelligence
      - Sequences
    properties:
      - type: Documentation
        url: https://docs.apollo.io/
      - type: GettingStarted
        url: https://docs.apollo.io/docs
      - type: APIReference
        url: https://docs.apollo.io/reference
      - type: Authentication
        url: https://docs.apollo.io/reference/authentication
      - type: RateLimits
        url: https://docs.apollo.io/reference/rate-limits
      - type: Tutorials
        url: https://docs.apollo.io/docs/overview-apollo-api-tutorials
      - type: FAQ
        url: https://docs.apollo.io/docs/apollo-api-faqs
common:
  - type: Documentation
    url: https://docs.apollo.io/
  - type: GettingStarted
    url: https://docs.apollo.io/docs
  - type: APIReference
    url: https://docs.apollo.io/reference
  - type: Authentication
    url: https://docs.apollo.io/reference/authentication
  - type: RateLimits
    url: https://docs.apollo.io/reference/rate-limits
  - type: Features
    data:
      - name: People Enrichment
        description: Enrich contact records with data from Apollo's 210M+ contact database.
      - name: Organization Enrichment
        description: Enrich company records with data from Apollo's 35M+ company database.
      - name: People Search
        description: Search Apollo's contact database to find and identify sales prospects.
      - name: Organization Search
        description: Search Apollo's company database for target accounts and job postings.
      - name: CRM Integration
        description: Manage accounts, contacts, deals, and sequences via the REST API.
      - name: OAuth 2.0 Partner Integration
        description: Partners use OAuth 2.0 to build integrations accessing Apollo data on behalf of customers.
      - name: Interactive Try It
        description: Interactive API testing capability built directly into the documentation.
      - name: Analytics Reporting
        description: Query analytics reports for performance metrics via the API.
  - type: UseCases
    data:
      - name: Sales Intelligence
        description: Access Apollo's contact and company database for prospecting and outreach.
      - name: Data Enrichment Pipelines
        description: Enrich CRM records with contact and organization data at scale.
      - name: Partner Integrations
        description: Build third-party integrations using OAuth 2.0 to access Apollo data for mutual customers.
      - name: Workflow Automation
        description: Automate sales workflows including sequences, tasks, and deal management.
  - type: Integrations
    data:
      - name: OAuth 2.0
        description: Partner integration protocol for accessing Apollo data on behalf of customers.
      - name: API Key Authentication
        description: Direct API key access for customers building internal integrations.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
