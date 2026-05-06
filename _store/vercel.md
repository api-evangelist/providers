---
aid: vercel
url: https://raw.githubusercontent.com/api-evangelist/vercel/refs/heads/main/apis.yml
apis:
  - aid: vercel:vercel
    name: Vercel
    tags: []
    humanURL: ' https://vercel.com/docs'
    properties:
      - url: ' https://vercel.com/docs'
        type: Documentation
    description: Vercel is a developer cloud to build and deploy web applications.
  - aid: vercel:vercel-rest-api
    name: Vercel REST API
    tags:
      - Access Groups
      - Billing
      - Certificates
      - Deployments
      - DNS
      - Domains
      - Edge Config
      - Environment Variables
      - Projects
      - Teams
      - Webhooks
    humanURL: https://vercel.com/docs/rest-api/reference
    properties:
      - url: https://vercel.com/docs/rest-api/reference
        type: Documentation
      - url: https://openapi.vercel.sh/
        type: OpenAPI
      - url: https://vercel.com/docs/rest-api/reference#rate-limits
        type: RateLimits
      - url: https://vercel.com/docs/rest-api/reference#pagination
        type: Pagination
      - url: https://vercel.com/docs/rest-api/reference#versioning
        type: Versioning
    description: The Vercel REST API provides programmatic access to the Vercel platform. All endpoints live under https://api.vercel.com and follow REST architecture over SSL. The API covers deployments, domains, projects, teams, DNS, certificates, edge config, environment variables, access groups, billing, security, webhooks, and more. Authentication uses Bearer tokens via the Authorization header.
  - aid: vercel:vercel-ai-gateway-api
    name: Vercel AI Gateway API
    tags:
      - AI
      - AI Gateway
      - LLM
      - Machine Learning
      - Models
    humanURL: https://vercel.com/docs/ai-gateway
    properties:
      - url: https://vercel.com/docs/ai-gateway
        type: Documentation
      - url: https://vercel.com/docs/ai-gateway/getting-started
        type: GettingStarted
      - url: https://vercel.com/docs/ai-gateway/models-and-providers
        type: Documentation
      - url: https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-compat
        type: Documentation
      - url: https://vercel.com/docs/ai-gateway/usage
        type: UsageBilling
      - url: https://raw.githubusercontent.com/api-evangelist/vercel/refs/heads/main/openapi/vercel-ai-gateway-openapi.yml
        type: OpenAPI
    description: The Vercel AI Gateway provides a unified API to access hundreds of AI models from multiple providers through a single endpoint at https://ai-gateway.vercel.sh/v1. It offers one key for hundreds of models, spend monitoring, automatic retries and fallbacks, embeddings support, and zero markup on token pricing. Compatible with the AI SDK, OpenAI SDK, and Anthropic SDK.
  - aid: vercel:v0-platform-api
    name: V0 Platform API
    tags:
      - AI
      - App Builder
      - Code Generation
    humanURL: https://v0.dev/docs
    properties:
      - url: https://v0.dev/docs
        type: Documentation
      - url: https://github.com/vercel/v0-sdk
        type: GitHubOrganization
      - url: https://raw.githubusercontent.com/api-evangelist/vercel/refs/heads/main/openapi/vercel-v0-platform-openapi.yml
        type: OpenAPI
    description: The v0 Platform API provides programmatic access to v0's AI-powered app generation pipeline. It is a REST interface that wraps v0's full code generation lifecycle from prompt to project to code files to deployment. Capabilities include generating full-stack web apps from natural language prompts, structured parsing of generated code, automatic error fixing, and linking with rendered previews. A TypeScript SDK is available.
name: Vercel
tags:
  - AI Gateways
  - Gateways
  - Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://vercel.com/marketplace
    name: Vercel Marketplace
    type: Integrations
    description: 'null'
  - url: https://vercel.com/guides
    name: Guides
    type: Guide
    description: 'null'
  - url: https://vercel.com/blog
    name: Blog - Vercel
    type: Blog
    description: 'null'
  - url: https://vercel.com/press
    name: Press - Vercel
    type: PressReleases
    description: 'null'
  - url: https://vercel.com/changelog
    name: Changelog - Vercel
    type: ChangeLog
    description: 'null'
  - url: https://vercel.com/docs
    name: Vercel Documentation
    type: Documentation
    description: 'null'
  - url: https://vercel.com/docs/rest-api/reference#rate-limits
    name: Using the REST API - Vercel API Docs
    type: RateLimits
    description: 'null'
  - url: https://vercel.com/docs/rest-api/reference#versioning
    name: Using the REST API - Vercel API Docs
    type: Versioning
    description: 'null'
  - url: https://vercel.com/docs/rest-api/reference#pagination
    name: Using the REST API - Vercel API Docs
    type: Pagination
    description: 'null'
  - url: https://vercel.com/help
    name: Help
    type: Support
    description: 'null'
  - url: https://vercel.com/pricing
    name: Find a plan to power your projects.
    type: Pricing
    description: 'null'
  - url: https://vercel.com/templates
    name: Find your Template
    type: Templates
    description: 'null'
  - url: https://vercel.com/login
    name: Login  Vercel
    type: Login
    description: 'null'
  - url: https://vercel.com/signup
    name: Sign Up  Vercel
    type: SignUp
    description: 'null'
  - url: https://github.com/vercel/vercel
    name: Vercel GitHub Repository
    type: GitHubOrganization
    description: The main open-source Vercel repository, configured as a monorepo containing the CLI and multiple packages.
  - url: https://community.vercel.com/
    name: Vercel Community Forum
    type: Forum
    description: The online community space for Vercel discussions, including help, feedback, showcase, and announcements.
  - url: https://www.vercel-status.com
    name: Vercel Status
    type: StatusPage
    description: Real-time and historical status information for Vercel platform services including build, deploy, API, and edge network.
  - url: https://vercel.com/legal/terms
    name: Vercel Terms of Service
    type: TermsOfService
    description: The legal terms of service governing use of the Vercel platform and services.
  - url: https://vercel.com/legal/privacy-policy
    name: Vercel Privacy Policy
    type: PrivacyPolicy
    description: The privacy policy covering data collection and processing practices across Vercel platforms.
  - url: https://security.vercel.com
    name: Vercel Trust Center
    type: Security
    description: Security and compliance documentation portal covering SOC 2, ISO 27001, PCI DSS, HIPAA, and GDPR certifications.
  - url: https://vercel.com/docs/cli
    name: Vercel CLI
    type: CLI
    description: Command-line interface for managing and configuring Vercel projects, deployments, domains, DNS, and environment variables from the terminal.
  - url: https://vercel.com/docs/ai-sdk
    name: Vercel AI SDK
    type: SDK
    description: TypeScript toolkit for building AI-powered applications with Next.js, Vue, Svelte, and Node.js, providing a unified API to call any LLM.
  - url: https://vercel.com/docs/vercel-firewall
    name: Vercel Firewall
    type: Security
    description: Web Application Firewall embedded in the Vercel Edge Network to protect applications from malicious attacks and unauthorized access.
  - url: https://vercel.com/docs/vercel-firewall/firewall-api
    name: Vercel Firewall API
    type: Documentation
    description: Documentation for interacting with the security endpoints of the Vercel REST API programmatically.
  - url: https://openapi.vercel.sh/
    name: Vercel REST API OpenAPI Specification
    type: OpenAPI
    description: The OpenAPI 3.0.3 specification for the Vercel REST API, automatically generated from the API repository.
  - url: https://vercel.com/security
    name: Vercel Security
    type: Security
    description: Overview of Vercel security practices, governance program, and compliance certifications.
  - url: https://vercel.com/docs/rest-api/reference
    name: Vercel REST API Reference
    type: APIReference
    description: Complete reference documentation for the Vercel REST API covering all endpoint categories.
  - type: Features
    data:
      - 'Hobby plan (free, non-commercial): 100GB bandwidth, 1M edge req/mo'
      - Pro plan at $20/dev/mo with $20 usage credits and 1TB bandwidth
      - Enterprise with custom limits, SAML SSO, SOC 2/HIPAA
      - Bandwidth overage at $0.15/GB above 1TB
      - Edge requests overage at $2/1M above 10M included
      - Function invocations at $0.60/1M
      - Active CPU at $0.128/hour, Provisioned Memory at $0.0106/GB-hour
      - Image Optimization with on-demand transformations
      - Blob Storage, KV, Postgres, Edge Config
      - REST API for projects, deployments, domains, env vars
      - 'Deployment limits: 100/day Hobby, 6000/day Pro'
      - 'Build concurrency: 1 Hobby, 12 Pro'
      - GitHub/GitLab/Bitbucket auto-deploy
      - Edge Functions and Edge Middleware
      - Speed Insights and Web Analytics
      - AI Gateway for LLM routing and observability
    sources:
      - https://vercel.com/pricing
    updated: '2026-05-04'
created: '2025-02-08'
modified: '2026-05-04'
position: Consuming
segments:
  - Gateways
description: Vercel is a cloud platform that helps developers build, deploy, and scale modern web applications quickly and efficiently. It provides an optimized hosting environment for frontend frameworks like Next.js (which it created), as well as other React, Vue, Angular, and static site projects. Vercel automates workflows for continuous deployment, edge caching, and serverless functions, so developers can push code changes and see them live almost instantly.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
