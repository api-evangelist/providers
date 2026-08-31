---
access_model:
  confidence: high
  label: Free tier with self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://docs.paragraph.com/account/plans-and-credits
  - https://paragraph.com/pricing
  - plans/paragraph-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Paragraph Agentic Access
  operation_count: 45
  slug: paragraph-agentic-access
  summary_line: 45 operations · 14 acting
api_count: 1
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paragraph analytics API
  slug: open-paragraph-analytics-api
- collection_type: open
  name: Paragraph analytics auth API
  slug: open-paragraph-auth-api
- collection_type: open
  name: Paragraph analytics coins API
  slug: open-paragraph-coins-api
- collection_type: open
  name: Paragraph analytics discover API
  slug: open-paragraph-discover-api
- collection_type: open
  name: Paragraph analytics emails API
  slug: open-paragraph-emails-api
- collection_type: open
  name: Paragraph analytics me API
  slug: open-paragraph-me-api
- collection_type: open
  name: Paragraph analytics posts API
  slug: open-paragraph-posts-api
- collection_type: open
  name: Paragraph analytics publications API
  slug: open-paragraph-publications-api
- collection_type: open
  name: Paragraph analytics subscribers API
  slug: open-paragraph-subscribers-api
- collection_type: open
  name: Paragraph analytics users API
  slug: open-paragraph-users-api
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
  url: openapi/_original/paragraph-openapi-original.json
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
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paragraph-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paragraph-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paragraph-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paragraph-changelog.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/paragraph-tool-crosswalk.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/paragraph-robots.txt
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
  name: Paragraph MCP Server
  slug: paragraph-mcp-server
modified: '2026-08-13'
name: Paragraph
nav: Providers
network: true
overview: 'Paragraph publishes 10 APIs on the [APIs.io](https://apis.io/) network, including analytics API, auth API, coins API, and 7 more. Tagged areas include Company, Publishing, Newsletters, Web3, and Content.


  Paragraph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Paragraph Plans Pricing
  plan_count: 5
  slug: paragraph-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Paragraph Rate Limits
  slug: paragraph-rate-limits
scopes:
- name: Paragraph Scopes
  scope_count: 0
  slug: paragraph-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/screenshots/paragraph-2026-08-07T191412.png
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
website: https://paragraph.com
---
