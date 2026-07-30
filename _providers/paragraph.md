---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Paragraph Agentic Access
  operation_count: 45
  slug: paragraph-agentic-access
  summary_line: 45 operations · 14 acting
api_count: 10
apis:
- description: The analytics API from Paragraph — 2 operation(s) for analytics.
  name: Paragraph analytics API
  slug: paragraph-analytics-api
- description: The auth API from Paragraph — 2 operation(s) for auth.
  name: Paragraph auth API
  slug: paragraph-auth-api
- description: Operations related to tokenized content
  name: Paragraph coins API
  slug: paragraph-coins-api
- description: The discover API from Paragraph — 3 operation(s) for discover.
  name: Paragraph discover API
  slug: paragraph-discover-api
- description: The emails API from Paragraph — 1 operation(s) for emails.
  name: Paragraph emails API
  slug: paragraph-emails-api
- description: The me API from Paragraph — 1 operation(s) for me.
  name: Paragraph me API
  slug: paragraph-me-api
- description: Operations related to posts and content
  name: Paragraph posts API
  slug: paragraph-posts-api
- description: Operations related to publications
  name: Paragraph publications API
  slug: paragraph-publications-api
- description: Operations related to subscriber management (requires API key)
  name: Paragraph subscribers API
  slug: paragraph-subscribers-api
- description: Operations related to users and authors
  name: Paragraph users API
  slug: paragraph-users-api
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paragraph.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paragraph.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paragraph.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paragraph.com/getting-started/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paragraph-xyz
- group: company
  title: ''
  type: Blog
  url: https://paragraph.com/@blog
- group: operate
  title: ''
  type: Support
  url: https://docs.paragraph.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://paragraph.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.paragraph.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paragraph.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paragraph.com/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/paragraph-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/paragraph-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paragraph-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/paragraph-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paragraph-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/paragraph-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paragraph-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paragraph-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paragraph-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paragraph-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paragraph-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paragraph-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paragraph-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paragraph-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paragraph-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paragraph-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paragraph.com
created: '2026-07-17'
description: Paragraph is a web3-native publishing and newsletter platform where writers get a website, a newsletter, an owned subscriber list, and an AI agent that drafts, distributes, and maintains their publication. It supports custom domains, Substack import, subscriber management, and onchain monetization through writer coins and post coins. Paragraph ships a full public REST API (public.api.paragraph.com), an official TypeScript SDK, a CLI, a hosted Model Context Protocol server, and published Agent Skills so developers and AI agents can manage posts, publications, subscribers, and coins programmatically. Backed by Union Square Ventures.
image: https://paragraph.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: paragraph-mcp.yml
  slug: paragraph-mcpyml
modified: '2026-07-20'
name: Paragraph
nav: Providers
network: true
overview: 'Paragraph publishes 10 APIs on the [APIs.io](https://apis.io/) network, including analytics API, auth API, coins API, and 7 more. Tagged areas include Company, Publishing, Newsletters, Web3, and Content.


  Paragraph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 51.4
  delta: 1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.2
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Paragraph Authentication
  slug: paragraph-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paragraph Domain Security
  slug: paragraph-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paragraph
tags:
- Company
- Publishing
- Newsletters
- Web3
- Content
- Blogging
- Creator Economy
- API
website: https://paragraph.com
---
