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
api_count: 4
apis:
- description: Cloud-based generator that produces customizable, type-safe SDKs in seven target stacks (TypeScript, Python, Java, .NET, Go, PHP, Terraform) from OpenAPI 2.0/3.0/3.1 or Postman Collections. CLI and CI
  name: Liblab SDK Generator
  slug: liblab
- description: Generates a complete Model Context Protocol (MCP) server from an OpenAPI, Swagger, or Postman spec so AI chat clients (Claude, Cursor, OpenAI) can call the underlying API in natural language. Launched
  name: Liblab MCP Generator
  slug: mcp-generator
- description: Public catalog of pre-generated SDKs (Python, TypeScript, C#, PHP) for popular third-party APIs (Postman, RingCentral, NYT, UPS, NHL, Pinnacle, OpenHue, Skyscanner, Voyado, Booking, etc.) used to demo
  name: Liblab Hub
  slug: hub
- description: Generates a Terraform provider from an OpenAPI specification, enabling Infrastructure-as-Code workflows against any documented API.
  name: Liblab Terraform Provider Generator
  slug: terraform-provider
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liblab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://liblab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://liblab.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://liblab.com/docs/get-started/quickstart-generate-sdk
- group: company
  title: ''
  type: Blog
  url: https://liblab.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://liblab.com/pricing
- group: company
  title: ''
  type: About
  url: https://liblab.com/about
- group: operate
  title: ''
  type: Contact
  url: https://liblab.com/contact
- group: start
  title: ''
  type: Portal
  url: https://app.liblab.com/
- group: start
  title: ''
  type: Signup
  url: https://app.liblab.com/join
- group: other
  title: ''
  type: Developer
  url: https://liblab.com/developer
- group: build
  title: ''
  type: CLI
  url: https://liblab.com/docs/cli/cli-overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liblab.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liblab.com/terms
- group: other
  title: ''
  type: Hub
  url: https://hub.liblab.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liblaber
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LibLaber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liblaber
- group: agent
  title: ''
  type: MCPServer
  url: https://liblab.com/blog/mcp-generator
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/liblaber/liblab-sdk-updates
- group: other
  title: ''
  type: HomebrewTap
  url: https://github.com/liblaber/homebrew-liblab
- group: docs
  title: ''
  type: SampleOpenAPI
  url: https://github.com/liblaber/simple-petstore-openapi
- group: build
  title: ''
  type: AgentExample
  url: https://github.com/liblaber/ai-github-agent-example
- group: other
  title: ''
  type: RAGTemplate
  url: https://github.com/liblaber/build-a-rag-ai-app-template
- group: other
  title: ''
  type: AgentRepo
  url: https://github.com/liblaber/ai
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/liblab/main/plans/liblab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/liblab/main/rate-limits/liblab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/liblab/main/finops/liblab-finops.yml
- group: other
  title: ''
  type: Acquisition
  url: https://liblab.com/blog/liblab-joins-postman-to-complete-the-api-lifecycle
- group: agent
  title: ''
  type: LlmsText
  url: https://liblab.com/llms.txt
created: '2026-03-03'
description: liblab generates and publishes type-safe, idiomatic SDKs in TypeScript, Python, Java, .NET, Go, PHP, and Terraform from OpenAPI/Swagger/Postman specs, plus MCP servers that expose those APIs to AI agents. The platform ships a CLI, hosted portal, and CI/CD GitHub Action that publish SDKs to customer repos via pull requests. liblab joined Postman in November 2025 to complete the API lifecycle.
finops:
- name: Liblab Finops
  service_category: Developer Tools / SDK Generation
  slug: liblab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liblab.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-22'
name: Liblab
nav: Providers
network: true
overview: 'Liblab publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SDKs, SDK Generation, Code Generation, OpenAPI, and Developer Tools.


  Liblab''s developer surface includes documentation, getting-started guide, engineering blog, pricing, developer portal, signup flow, CLI, and 23 more developer resources.'
plans:
- name: Liblab Plans Pricing
  plan_count: 5
  slug: liblab-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 4
  name: Liblab Rate Limits
  slug: liblab-rate-limits
score:
  band: thin
  composite: 34.6
  delta: -2.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liblab/refs/heads/main/screenshots/liblab-2026-06-20T184501.png
security:
- kind: domain-security
  name: Liblab Domain Security
  slug: liblab-domain-security
  summary_line: TLSv1.3 · DMARC
slug: liblab
tags:
- SDKs
- SDK Generation
- Code Generation
- OpenAPI
- Developer Tools
- MCP
- AI Agents
- Postman
- Terraform
- Developer Experience
website: https://liblab.com/
---
