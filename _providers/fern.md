---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Fern transforms a single API source of truth (OpenAPI, AsyncAPI, Protobuf, OpenRPC, or the Fern Definition Language) into type-safe SDKs in nine languages, branded interactive documentation with API e
  name: Fern
  slug: fern
artifact_total: 54
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fern-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fern-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/fern-api/fern
- group: other
  title: ''
  type: Branding
  url: https://brandfetch.com/buildwithfern.com
- group: docs
  title: ''
  type: Documentation
  url: https://buildwithfern.com/learn
- group: build
  title: ''
  type: CLI
  url: https://buildwithfern.com/learn/cli-reference/overview
- group: other
  title: ''
  type: Customers
  url: https://www.buildwithfern.com/showcase
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buildwithfern.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.buildwithfern.com/blog
- group: operate
  title: ''
  type: Support
  url: https://buildwithfern.com/learn#get-support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buildwithfern.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buildwithfern.com/terms-of-service
- group: start
  title: ''
  type: GettingStarted
  url: https://buildwithfern.com/learn/docs/getting-started/quickstart
- group: start
  title: ''
  type: Login
  url: https://dashboard.buildwithfern.com/login
- group: start
  title: ''
  type: Signup
  url: https://dashboard.buildwithfern.com/login
- group: other
  title: ''
  type: X
  url: https://x.com/buildwithfern
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buildwithfern
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.buildwithfern.com/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/fern-api/fern-mcp-server
- group: other
  title: ''
  type: AgentReadinessScore
  url: https://github.com/fern-api/agent-score
- group: operate
  title: ''
  type: ChangeLog
  url: https://buildwithfern.com/learn/changelog
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/fern/refs/heads/main/plans/fern-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/fern/refs/heads/main/rate-limits/fern-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/fern/refs/heads/main/finops/fern-finops.yml
- group: other
  title: ''
  type: Capabilities
  url: https://github.com/api-evangelist/fern/tree/main/capabilities
- group: docs
  title: ''
  type: JSONSchema
  url: https://github.com/api-evangelist/fern/tree/main/json-schema
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/fern/refs/heads/main/json-ld/fern-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/fern/refs/heads/main/vocabulary/fern-vocabulary.yml
- group: company
  title: ''
  type: Partnerships
  url: ''
- group: build
  title: ''
  type: SDKs
  url: ''
- group: build
  title: ''
  type: GitHubRepositories
  url: ''
- group: other
  title: ''
  type: Customers
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2025-01-08'
description: Fern is an SDK generation and documentation platform designed for the AI era. It transforms OpenAPI, AsyncAPI, Protobuf (gRPC), and OpenRPC specifications into idiomatic, production-ready SDKs across nine languages plus auto-generated, branded developer documentation, an AI-first CLI, llms.txt for agent discoverability, Ask Fern AI search, and an MCP server that connects Claude, Cursor, and Windsurf into the workflow. Engineering teams at ElevenLabs, Deepgram, Square, Webflow, Auth0, LaunchDarkly, Cohere, Pinecone, Cash App, and OpenRouter use Fern to deliver world-class developer experiences from a single source of truth.
examples:
- key_count: 8
  name: Fern Api Definition Example
  slug: fern-api-definition-example
- key_count: 8
  name: Fern Docs Config Example
  slug: fern-docs-config-example
- key_count: 4
  name: Fern Mcp Ask Fern Example
  slug: fern-mcp-ask-fern-example
- key_count: 5
  name: Fern Sdk Generator Python Example
  slug: fern-sdk-generator-python-example
- key_count: 5
  name: Fern Sdk Generator Typescript Example
  slug: fern-sdk-generator-typescript-example
features:
- description: Generate production-ready, type-safe SDKs in TypeScript, Python, Go, Java, C#, PHP, Ruby, Swift, and Rust from OpenAPI, AsyncAPI, Protobuf, or the Fern Definition Language.
  name: SDK Generation
- description: Auto-generate beautiful, branded API documentation with interactive API explorer, search, dark mode, SEO, and custom domain support.
  name: API Documentation
- description: AI-powered in-docs search and chatbot that answers developer questions using your API docs, SDKs, and guides as context.
  name: Ask Fern
- description: Purpose-built API definition language as an alternative to OpenAPI for authoring API contracts.
  name: Fern Definition Language
- description: Auto-generated llms.txt markdown artifacts so LLMs and AI agents can consume documentation directly.
  name: llms.txt Generation
- description: Hosted Model Context Protocol server that connects Claude, Cursor, and Windsurf to Ask Fern AI search and the Fern docs and SDK platform.
  name: MCP Server
- description: Open-source tool that rates documentation sites on their agent readiness across structure, semantics, and machine-readable content.
  name: Agent Score
- description: AI-assisted documentation authoring inside the Fern docs platform.
  name: Fern Writer
- description: First-class support for OpenAPI (REST plus Webhooks), AsyncAPI (WebSockets), Protobuf (gRPC), and OpenRPC.
  name: Multi-Protocol Support
- description: Built-in versioning, product switching, and multi-source aggregation across multiple APIs and product surfaces.
  name: Versioning and Multi-Product
- description: Enterprise self-hosting of the Fern docs platform inside a customer environment.
  name: Self-Hosting
- description: JWT and SSO-gated docs for partner-only and internal documentation.
  name: Visitor Authentication
finops:
- name: Fern Finops
  service_category: Developer Tools / API Platform
  slug: fern-finops
image: /assets/icons/fern.png
integrations:
- description: First-party GitHub Actions for SDK generation, OpenAPI sync, and CI/CD publishing workflows.
  name: GitHub Actions
- description: Automatic publishing of generated TypeScript and JavaScript SDKs.
  name: npm Registry
- description: Automatic publishing of generated Python SDKs.
  name: PyPI
- description: Automatic publishing of generated Java SDKs.
  name: Maven Central
- description: Automatic publishing of generated C# SDKs.
  name: NuGet
- description: Automatic publishing of generated Ruby SDKs.
  name: RubyGems
- description: Automatic publishing of generated PHP SDKs.
  name: Packagist
- description: Automatic publishing of generated Rust SDKs.
  name: Crates.io
- description: Distribution of generated Swift SDKs.
  name: Swift Package Manager
- description: Distribution of generated Go SDKs via versioned tags.
  name: Go Modules
- description: Native ingestion of Postman collections as a documentation and SDK source.
  name: Postman
- description: MCP server integration so Claude Desktop and Claude Code can query Ask Fern AI and assist with Fern workflows.
  name: Anthropic Claude
- description: MCP integration plus llms.txt make Fern-generated docs first-class context for the Cursor IDE.
  name: Cursor
- description: MCP server support for Windsurf's AI coding environment.
  name: Windsurf
- description: Documentation indexing and llms.txt artifacts so leading LLMs can answer questions grounded in customer docs.
  name: ChatGPT, Gemini, Microsoft Copilot
json_schemas:
- name: Fern API Definition
  property_count: 8
  slug: fern-api-definition
- name: Fern Docs Configuration
  property_count: 10
  slug: fern-docs-config
- name: Fern MCP Tool Invocation
  property_count: 4
  slug: fern-mcp-tool
- name: Fern SDK Generator
  property_count: 6
  slug: fern-sdk-generator
json_structures:
- name: Fern Api Definition Structure
  property_count: 9
  slug: fern-api-definition-structure
- name: Fern Docs Config Structure
  property_count: 8
  slug: fern-docs-config-structure
- name: Fern Sdk Generator Structure
  property_count: 5
  slug: fern-sdk-generator-structure
jsonld:
- class_count: 31
  name: Fern Context
  property_count: 4
  slug: fern-context
layout: provider
mcp_servers:
- description: ''
  name: fern-mcp-server
  slug: fern-mcp-server
modified: '2026-05-22'
name: Fern
nav: Providers
network: true
overview: 'Fern publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agent Ready, AI, API Definitions, AsyncAPI, and Code Generation.


  The Fern catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fern''s developer surface includes documentation, CLI, pricing, engineering blog, support, getting-started guide, signup flow, and 21 more developer resources.'
plans:
- name: Fern Plans Pricing
  plan_count: 3
  slug: fern-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Fern Rate Limits
  slug: fern-rate-limits
rules:
- name: Fern API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fern-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.8
  delta: -4.8
  facets:
    commercial_clarity: 100.0
    contract_quality: 12.9
    developer_ergonomics: 47.8
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 58.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fern/refs/heads/main/screenshots/fern-2026-06-20T181141.png
security:
- kind: domain-security
  name: Fern Domain Security
  slug: fern-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fern
tags:
- Agent Ready
- AI
- API Definitions
- AsyncAPI
- Code Generation
- Developer Experience
- Developer Portal
- Documentation
- gRPC
- llms.txt
- MCP
- OpenAPI
- OpenRPC
- Platform
- Protobuf
- SDKs
- WebSockets
use_cases:
- description: Transform OpenAPI specifications into idiomatic client libraries across nine programming languages with automated publishing to npm, PyPI, Maven Central, NuGet, and other registries.
  name: SDK Generation from OpenAPI
- description: Replace Docusaurus, Mintlify, GitBook, or ReadMe with a Fern-hosted docs site featuring custom branding and domain.
  name: Developer Documentation Hosting
- description: Define APIs in Fern Definition Language and generate server stubs, SDKs, and documentation from one source of truth.
  name: API-First Development
- description: Auto-update and re-publish SDKs each time an OpenAPI specification changes via GitHub Actions CI/CD.
  name: SDK Maintenance Automation
- description: Make docs consumable by LLMs and AI coding agents through llms.txt, MCP, and structured semantic content.
  name: Agent-Ready Documentation
- description: Document REST plus WebSocket plus gRPC surfaces in a single unified developer experience.
  name: Multi-Protocol Reference Docs
- description: Migrate existing developer docs and SDK pipelines to Fern in days rather than quarters.
  name: Migration From Stainless, ReadMe, Mintlify, or GitBook
---
