---
aid: stainless
url: https://raw.githubusercontent.com/api-evangelist/stainless/refs/heads/main/apis.yml
name: Stainless
description: Stainless is an API developer experience platform that generates best-in-class SDKs, interactive documentation, production-ready CLI tools, MCP servers, and Terraform providers directly from an OpenAPI specification. Trusted by Anthropic, Cloudflare, Google, and OpenAI, Stainless automates the boilerplate of client library development including HTTP requests, retries with exponential backoff, streaming, and pagination. The platform supports TypeScript, Python, Go, Java, Kotlin, Ruby, C#, PHP, and Terraform, with Rust and Swift in development.
tags:
  - Code Generation
  - Documentation
  - Developer Experience
  - MCP
  - Platform
  - SDKs
  - Terraform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-05-02'
position: Consumer
segments:
  - SDKs
  - Developer Tooling
common:
  - url: https://www.stainless.com/
    type: Portal
  - url: https://www.stainless.com/docs/
    type: Documentation
  - url: https://www.stainless.com/pricing
    type: Pricing
  - url: https://www.stainless.com/blog
    type: Blog
  - url: https://www.stainless.com/changelog
    type: Change Log
  - url: https://app.stainless.com/login
    type: Login
  - url: https://www.stainless.com/company
    type: About
  - url: https://github.com/stainless-api
    type: GitHub Organization
  - url: https://www.stainless.com/legal/terms-conditions
    type: TermsOfService
  - url: https://www.stainless.com/customers
    type: Customers
apis:
  - aid: stainless:stainless
    name: Stainless SDK Generator
    tags:
      - Code Generation
      - Developer Experience
      - SDKs
    humanURL: https://www.stainless.com/
    description: Generate production-ready SDKs in TypeScript, Python, Go, Java, Kotlin, Ruby, C#, PHP, and Terraform from an OpenAPI specification. Stainless handles HTTP requests, retries with exponential backoff, streaming, pagination, and idiomatic patterns for each language. Trusted by Anthropic, Cloudflare, Google, and OpenAI.
    properties:
      - url: https://www.stainless.com/
        type: Documentation
      - url: https://www.stainless.com/docs/
        type: GettingStarted
      - url: https://www.stainless.com/pricing
        type: Pricing
      - url: https://www.stainless.com/customers
        type: Customers
      - url: https://github.com/stainless-api/upload-openapi-spec-action
        type: GitHubAction
      - url: https://github.com/stainless-api/build-sdk-action
        type: GitHubAction
  - aid: stainless:stainless-docs-platform
    name: Stainless Docs Platform
    tags:
      - API Reference
      - Developer Experience
      - Documentation
    humanURL: https://www.stainless.com/products/docs
    description: The Stainless Docs Platform combines your API reference, usage examples, and narrative guides into a single, cohesive experience that evolves with your API. Go from an OpenAPI spec to a live, interactive documentation site in minutes with a developer-centric docs-as-code workflow built on Astro. Deploys to Cloudflare or custom clouds.
    properties:
      - url: https://www.stainless.com/products/docs
        type: Documentation
      - url: https://www.stainless.com/docs/docs-platform/
        type: GettingStarted
  - aid: stainless:stainless-mcp-servers
    name: Stainless MCP Servers
    tags:
      - AI Agents
      - Code Generation
      - MCP
    humanURL: https://www.stainless.com/products/mcp
    description: Stainless generates production-ready MCP (Model Context Protocol) servers optimized for agentic coding and context limits directly from an OpenAPI spec. Production-grade capabilities including OAuth, SSE, and remote servers are included by default. Generated MCP servers use a code tool architecture enabling seamless integration with Claude Desktop, Cursor, and other MCP clients.
    properties:
      - url: https://www.stainless.com/products/mcp
        type: Documentation
      - url: https://www.stainless.com/docs/targets/mcp/
        type: GettingStarted
      - url: https://www.stainless.com/mcp
        type: Portal
  - aid: stainless:stainless-cli
    name: Stainless CLI
    tags:
      - CLI
      - Code Generation
      - Developer Tools
    humanURL: https://www.stainless.com/docs/
    description: The Stainless CLI generates production-ready command-line interfaces from an OpenAPI specification. Generated CLIs provide a consistent, typed interface for interacting with any API from the terminal.
    properties:
      - url: https://www.stainless.com/docs/
        type: Documentation
  - aid: stainless:stainless-terraform
    name: Stainless Terraform Providers
    tags:
      - Code Generation
      - Infrastructure as Code
      - Terraform
    humanURL: https://www.stainless.com/docs/
    description: Stainless generates production-ready Terraform providers from an OpenAPI specification, enabling infrastructure-as-code access to any REST API without manual Terraform provider development.
    properties:
      - url: https://www.stainless.com/docs/
        type: Documentation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
