---
aid: upwork
name: Upwork
description: Upwork is a global freelancing platform that connects businesses with independent professionals through a talent marketplace. The Upwork API enables developers to integrate Upwork features into their applications, including job search, contract management, messaging, profile access, and webhook event subscriptions. The API is primarily GraphQL-based at api.upwork.com/graphql, with OAuth 2.0 authentication. Key resources include job postings, contracts, user profiles, messages, and freelancer search. The platform serves over 800,000 clients and 18 million freelancers across 180+ countries.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Freelancing
  - Jobs
  - Talent
  - Marketplace
  - Contracts
  - Hiring
url: https://raw.githubusercontent.com/api-evangelist/upwork/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: upwork:graphql-api
    name: Upwork GraphQL API
    description: The primary Upwork API surface, providing GraphQL queries and mutations for job search, profile access, contract management, and messaging. Authentication uses OAuth 2.0 authorization code flow. The API supports subscriptions for real-time event notifications via webhooks.
    humanURL: https://www.upwork.com/developer/documentation/graphql/api/docs/index.html
    baseURL: https://api.upwork.com/graphql
    tags:
      - GraphQL
      - Jobs
      - Contracts
      - Profiles
      - Messages
      - Freelancing
    properties:
      - type: Documentation
        url: https://www.upwork.com/developer/documentation/graphql/api/docs/index.html
      - type: OpenAPI
        url: openapi/upwork-graphql-api-openapi.yml
      - type: JSONSchema
        url: json-schema/graphql-api-job-schema.json
      - type: JSONSchema
        url: json-schema/graphql-api-contract-schema.json
      - type: JSONSchema
        url: json-schema/graphql-api-freelancer-profile-schema.json
      - type: JSONSchema
        url: json-schema/graphql-api-message-schema.json
  - aid: upwork:rest-api
    name: Upwork REST API
    description: The legacy REST API surface for Upwork, covering job search, contracts, reporting, organization management, and freelancer profiles. OAuth 2.0 authentication is required. Many endpoints have been migrated to GraphQL.
    humanURL: https://developers.upwork.com/
    baseURL: https://www.upwork.com/api
    tags:
      - REST
      - Jobs
      - Contracts
      - Profiles
      - Reports
    properties:
      - type: Documentation
        url: https://developers.upwork.com/
      - type: GettingStarted
        url: https://developers.upwork.com/#get-started
      - type: OpenAPI
        url: openapi/upwork-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/rest-api-report-response-schema.json
      - type: JSONSchema
        url: json-schema/rest-api-engagement-schema.json
common:
  - type: Website
    url: https://www.upwork.com/
  - type: Documentation
    url: https://www.upwork.com/developer/documentation/graphql/api/docs/index.html
  - type: Portal
    url: https://www.upwork.com/developer
  - type: Support
    url: https://support.upwork.com/hc/en-us/sections/17976982721555-Upwork-API
  - type: Authentication
    url: https://support.upwork.com/hc/en-us/articles/115015933448-API-authentication-and-security
  - type: GitHubOrganization
    url: https://github.com/upwork
  - type: GitHubRepository
    url: https://github.com/upwork/python-upwork-oauth2
    title: Python SDK (OAuth2)
  - type: GitHubRepository
    url: https://github.com/upwork/node-upwork-oauth2
    title: Node.js SDK (OAuth2)
  - type: GitHubRepository
    url: https://github.com/upwork/java-upwork-oauth2
    title: Java SDK (OAuth2)
  - type: GitHubRepository
    url: https://github.com/upwork/golang-upwork-oauth2
    title: Go SDK (OAuth2)
  - type: GitHubRepository
    url: https://github.com/upwork/ruby-upwork-oauth2
    title: Ruby SDK (OAuth2)
  - type: GitHubRepository
    url: https://github.com/upwork/php-upwork-oauth2
    title: PHP SDK (OAuth2)
  - type: GitHubRepository
    url: https://github.com/upwork/perl-upwork-oauth2
    title: Perl SDK (OAuth2)
  - type: JSONLD
    url: json-ld/upwork-context.jsonld
  - type: SpectralRules
    url: rules/upwork-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/upwork-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/talent-marketplace.yaml
    title: Talent Marketplace
  - type: NaftikoCapability
    url: capabilities/shared/graphql-api.yaml
    title: GraphQL API (Shared)
  - type: Features
    data:
      - name: Job Search
        description: Search and filter job postings using marketplaceJobPostingsSearch GraphQL query with full-text and faceted search.
      - name: Contract Management
        description: Access active and completed contracts, contract terms, milestones, and time entries.
      - name: Messaging
        description: Read and send messages within active contracts using GraphQL mutations.
      - name: Profile Access
        description: Query freelancer and client profiles, skills, portfolios, and ratings.
      - name: Webhook Subscriptions
        description: Subscribe to events for real-time notifications when contracts, jobs, or messages change.
      - name: OAuth 2.0 Authentication
        description: Secure API access using OAuth 2.0 authorization code grant flow with refresh token support.
      - name: Multi-Language SDKs
        description: Official SDKs for Python, Node.js, Java, Go, Ruby, PHP, and Perl with OAuth2 support.
      - name: GraphQL Explorer
        description: Interactive GraphQL API explorer at upwork.com/developer/explorer for testing queries.
  - type: UseCases
    data:
      - name: Freelancer Management
        description: Agencies and businesses managing a distributed freelancer workforce through programmatic contract and message access.
      - name: Job Monitoring
        description: Applications tracking new job postings matching specific criteria using scheduled search queries.
      - name: Talent Analytics
        description: Platforms building talent scoring, profile analysis, and market intelligence on freelancers.
      - name: CRM Integration
        description: Connecting Upwork client and contract data to CRM systems for unified client management.
      - name: Automated Reporting
        description: Building custom dashboards and reports from Upwork contract, billing, and engagement data.
  - type: Integrations
    data:
      - name: PowerBI Connector
        description: Official Power BI connector for importing Upwork data into business intelligence dashboards.
      - name: OAuth 2.0 Providers
        description: Standard OAuth 2.0 integration with any identity provider supporting authorization code flow.
      - name: Webhook Integration
        description: Real-time event streaming to external systems via Upwork subscription webhooks.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
