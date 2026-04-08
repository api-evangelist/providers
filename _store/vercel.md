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
created: '2025-02-08'
modified: '2026-04-07'
position: Consuming
description: Vercel is a cloud platform that helps developers build, deploy, and scale modern web applications quickly and efficiently. It provides an optimized hosting environment for frontend frameworks like Next.js (which it created), as well as other React, Vue, Angular, and static site projects. Vercel automates workflows for continuous deployment, edge caching, and serverless functions, so developers can push code changes and see them live almost instantly.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

