---
aid: resend
name: Resend
description: Resend is a developer-first email API platform that simplifies sending and managing transactional and marketing emails. It provides a clean REST API with bearer token authentication, supporting email sending, domain management, API key management, audience and contact management, and broadcast campaigns. Resend offers SDKs for Node.js, Python, Go, Ruby, PHP, Java, .NET, Rust, Elixir, and more, along with a React Email library and official MCP server.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Email
  - Developer Tools
  - Transactional Email
  - Marketing Email
url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/apis.yml
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: resend:resend
    name: Resend API
    description: The Resend REST API provides endpoints for sending emails, managing domains, managing API keys, managing audiences and contacts, and sending broadcast campaigns. Authentication uses Bearer tokens. Rate limit is 5 requests per second per team by default. Base URL is https://api.resend.com.
    humanURL: https://resend.com/
    baseURL: https://api.resend.com
    tags:
      - Email
      - Domains
      - API Keys
      - Audiences
      - Contacts
      - Broadcasts
      - Transactional Email
    properties:
      - url: https://resend.com/
        type: Documentation
      - url: openapi/resend-openapi.yml
        type: OpenAPI
      - type: Webhooks
        url: https://resend.com/docs/dashboard/webhooks/introduction
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/json-schema/resend-email-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/json-schema/resend-audience-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/json-schema/resend-domain-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/json-structure/resend-email-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/json-ld/resend-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/rules/resend-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/capabilities/email-delivery.yaml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/resend/refs/heads/main/vocabulary/resend-vocabulary.yml
    contact:
      - FN: Resend Support
        url: https://resend.com/docs/support
common:
  - url: https://github.com/resend
    name: GitHub Organization
    type: GitHubOrganization
  - name: Changelog
    url: https://resend.com/changelog
    type: ChangeLog
  - name: Blog
    url: https://resend.com/blog
    type: Blog
  - name: Migration Guides
    url: https://resend.com/migrate
    type: Migrations
  - name: Customers
    url: https://resend.com/customers
    type: Customers
  - name: About
    url: https://resend.com/about
    type: About
  - name: Security
    url: https://resend.com/security
    type: Security
  - name: Integrations
    url: https://resend.com/docs/integrations
    type: Integrations
  - name: Examples
    url: https://resend.com/docs/examples
    type: Examples
  - name: SDKs
    url: https://resend.com/docs/sdks
    type: SDKs
  - name: Pricing
    url: https://resend.com/pricing
    type: Pricing
  - name: Login
    url: https://resend.com/login
    type: Login
  - name: Sign Up
    url: https://resend.com/signup
    type: SignUp
  - name: Node.js SDK
    url: https://github.com/resend/resend-node
    type: SDK
  - name: Python SDK
    url: https://github.com/resend/resend-python
    type: SDK
  - name: Go SDK
    url: https://github.com/resend/resend-go
    type: SDK
  - name: .NET SDK
    url: https://github.com/resend/resend-dotnet
    type: SDK
  - name: CLI
    url: https://github.com/resend/resend-cli
    type: CLI
  - name: MCP Server
    url: https://github.com/resend/resend-mcp
    type: MCPServer
  - name: React Email
    url: https://github.com/resend/react-email
    type: Library
  - name: Status
    url: https://resend-status.com/
    type: Status
  - name: Rate Limits
    url: https://resend.com/docs/api-reference/introduction
    type: RateLimits
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
