---
aid: stackshare
name: StackShare
description: StackShare is a platform where developers and companies share information about the technologies and tools they use to build software. The StackShare GraphQL API provides programmatic access to StackShare's database of developer tools and company tech stacks, exposing Leads (find companies using specific tools), Enrichment (retrieve the full tech stack for a domain), Tools (query metadata about technologies), and Search capabilities.
url: https://raw.githubusercontent.com/api-evangelist/stackshare/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Software Discovery
  - Tech Stacks
type: Index
access: 3rd-Party
created: '2026-03-24'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stackshare:stackshare-graphql-api
    name: StackShare GraphQL API
    description: 'The StackShare GraphQL API provides programmatic access to StackShare''s database of developer tools and company tech stacks. It exposes four primary capability areas: Leads (find companies using specific tools), Enrichment (retrieve the full tech stack for a given company), Tools (query metadata about a technology such as description and website URL), and Search (look up companies and retrieve basic company details). Authentication uses an API token passed as a query parameter.'
    humanURL: https://docs.stackshare.io/
    baseURL: https://api.stackshare.io/graphql
    tags:
      - Developer Tools
      - Software Discovery
      - Tech Stacks
    properties:
      - url: https://docs.stackshare.io/
        type: Documentation
      - url: https://docs.stackshare.io/reference/getting-started
        type: GettingStarted
      - url: https://docs.stackshare.io/reference/authentication
        type: Authentication
      - url: https://docs.stackshare.io/docs/the-graphql-endpoint
        type: GraphQL
      - url: https://docs.stackshare.io/docs/enrichment
        type: Documentation
      - url: https://docs.stackshare.io/docs/tools
        type: Documentation
      - url: https://docs.stackshare.io/docs/leads
        type: Documentation
common:
  - url: https://stackshare.io/
    name: StackShare Website
    type: Website
  - url: https://docs.stackshare.io/
    name: API Documentation
    type: Documentation
  - url: https://docs.stackshare.io/reference/getting-started
    name: Getting Started
    type: GettingStarted
  - url: https://stackshare.io/api
    name: Sign Up for API Access
    type: SignUp
  - url: https://stackshare.io/pricing
    name: Pricing
    type: Pricing
  - url: https://stackshare.io/enterprise
    name: Enterprise
    type: Pricing
  - url: https://docs.stackshare.io/reference/authentication
    name: Authentication
    type: Authentication
  - url: https://stackshare.io/terms
    name: Terms of Service
    type: TermsOfService
  - url: https://stackshare.io/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://medium.com/@stackshareio
    name: StackShare Blog
    type: Blog
  - url: https://twitter.com/stackshare
    name: StackShare on X
    type: X
  - url: https://github.com/stackshare
    name: StackShare on GitHub
    type: GitHub
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
