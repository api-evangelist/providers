---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Stainless Api Agentic Access
  operation_count: 22
  slug: stainless-api-agentic-access
  summary_line: 22 operations · 10 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Stainless Platform API is a REST API for programmatically managing Stainless projects, branches, and SDK builds. It exposes the same primitives that power the Stainless Studio web UI and CLI, allo
  name: Stainless Platform API
  slug: stainless-platform-api
- description: The Build Target Outputs API from Stainless — 1 operation(s) for build target outputs.
  name: Stainless Build Target Outputs API
  slug: stainless-api-build-target-outputs-api
- description: The Builds API from Stainless — 4 operation(s) for builds.
  name: Stainless Builds API
  slug: stainless-api-builds-api
- description: The Orgs API from Stainless — 2 operation(s) for orgs.
  name: Stainless Orgs API
  slug: stainless-api-orgs-api
- description: The Projects API from Stainless — 9 operation(s) for projects.
  name: Stainless Projects API
  slug: stainless-api-projects-api
- description: The User API from Stainless — 1 operation(s) for user.
  name: Stainless User API
  slug: stainless-api-user-api
artifact_total: 14
collections:
- collection_type: open
  name: Stainless Platform API
  slug: open-stainless-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stainless-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stainless-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stainless-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stainless-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.stainless.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.stainless.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.stainless.com/docs/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stainless.com/pricing
- group: other
  title: ''
  type: Customers
  url: https://www.stainless.com/customers
- group: company
  title: ''
  type: Blog
  url: https://www.stainless.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.stainless.com/changelog
- group: company
  title: ''
  type: Careers
  url: https://www.stainless.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.stainless.com/contact
- group: other
  title: ''
  type: Studio
  url: https://app.stainless.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stainless-api
- group: build
  title: ''
  type: TypeScriptSDK
  url: https://github.com/stainless-api/stainless-node
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/stainless-api/stainless-python
- group: build
  title: ''
  type: CLI
  url: https://github.com/stainless-api/stainless-cli
- group: agent
  title: ''
  type: MCPFront
  url: https://github.com/stainless-api/mcp-front
- group: other
  title: ''
  type: STLAPI
  url: https://github.com/stainless-api/stl-api
- group: other
  title: ''
  type: Email
  url: mailto:support@stainless.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stainless-api
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StainlessAPI
created: '2026-05-23'
description: Stainless is a New York-based developer-tools company that turns an OpenAPI specification into a portfolio of high-quality, idiomatic SDKs, reference documentation, MCP servers, CLIs, and Terraform providers. The platform was founded by veterans of Stripe, Heroku, and Twilio with the explicit goal of bringing Stripe-quality developer experience to any API, and is used by AI-platform and infrastructure companies including OpenAI, Anthropic, Google DeepMind, Cloudflare, Modern Treasury, Perplexity, Replicate, LangChain, Beeper, and Runway. Stainless supports nine target languages today (TypeScript, Python, Go, Java, Kotlin, Ruby, PHP, C#, plus a CLI) and publishes generated code under the Apache 2.0 license into customer-owned GitHub repositories. The company exposes its own platform as a REST API at api.stainless.com (v0), with endpoints for managing organizations, projects, branches, builds, and the current user, plus a build-compare endpoint and matching client libraries. Stainless
  also ships the Stainless Studio (web-based config UI), the Stainless CLI, a Language Server, GitHub member sync, breaking-change detection, SSO, audit logs, and integrations with documentation hosts (Bump.sh, GitBook, Mintlify, ReadMe).
finops:
- name: Stainless Api Finops
  service_category: API
  slug: stainless-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stainless-api.png
layout: provider
modified: '2026-05-23'
name: Stainless
nav: Providers
network: true
overview: 'Stainless publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Build Target Outputs API, Builds API, Orgs API, and 2 more. Tagged areas include SDK Generation, OpenAPI, API Tooling, Developer Experience, and MCP.


  Stainless'' developer surface includes authentication, documentation, API reference, pricing, engineering blog, changelog, CLI, and 16 more developer resources.'
plans:
- name: Stainless Api Plans Pricing
  plan_count: 1
  slug: stainless-api-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 2
  name: Stainless Api Rate Limits
  slug: stainless-api-rate-limits
score:
  band: thin
  composite: 40.2
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stainless-api/refs/heads/main/screenshots/stainless-api-2026-06-20T194454.png
security:
- kind: authentication
  name: Stainless Api Authentication
  slug: stainless-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stainless Api Domain Security
  slug: stainless-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Stainless Api Vulnerability Disclosure
  slug: stainless-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stainless-api
tags:
- SDK Generation
- OpenAPI
- API Tooling
- Developer Experience
- MCP
- Model Context Protocol
- Documentation
- Code Generation
- Terraform Provider
- API Reference
- DevTools
- API First
website: https://www.stainless.com
---
