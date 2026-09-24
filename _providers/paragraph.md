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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Paragraph Agentic Access
  operation_count: 45
  slug: paragraph-agentic-access
  summary_line: 45 operations · 14 acting
api_count: 1
apis:
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: The analytics API from Paragraph — 2 operation(s) for analytics.
  name: Paragraph Analytics API
  slug: paragraph-analytics-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: The auth API from Paragraph — 2 operation(s) for auth.
  name: Paragraph Auth API
  slug: paragraph-auth-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: Operations related to tokenized content
  name: Paragraph Coins API
  slug: paragraph-coins-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: The discover API from Paragraph — 3 operation(s) for discover.
  name: Paragraph Discover API
  slug: paragraph-discover-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: The emails API from Paragraph — 1 operation(s) for emails.
  name: Paragraph Emails API
  slug: paragraph-emails-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: The me API from Paragraph — 1 operation(s) for me.
  name: Paragraph Me API
  slug: paragraph-me-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: Operations related to posts and content
  name: Paragraph Posts API
  slug: paragraph-posts-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: Operations related to publications
  name: Paragraph Publications API
  slug: paragraph-publications-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: Operations related to subscriber management (requires API key)
  name: Paragraph Subscribers API
  slug: paragraph-subscribers-api
- baseURL: https://public.api.paragraph.com/api
  baseurl_source: declared
  description: Operations related to users and authors
  name: Paragraph Users API
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
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/openapi/_original/paragraph-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/paragraph-openapi-original.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/overlays/paragraph-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/paragraph-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/authentication/paragraph-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paragraph-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/packages/paragraph-packages.yml
  title: ''
  type: Packages
  url: packages/paragraph-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/packages/paragraph-packages.yml
  title: ''
  type: SDKs
  url: packages/paragraph-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/cli/paragraph-cli.yml
  title: ''
  type: CLI
  url: cli/paragraph-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/mcp/paragraph-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/paragraph-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/llms/paragraph-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paragraph-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/well-known/paragraph-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paragraph-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/conventions/paragraph-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paragraph-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/errors/paragraph-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paragraph-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/lifecycle/paragraph-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/paragraph-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/conformance/paragraph-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paragraph-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/data-model/paragraph-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paragraph-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/agentic-access/paragraph-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paragraph-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/security/paragraph-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paragraph-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/scopes/paragraph-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/paragraph-scopes.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/plans/paragraph-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paragraph-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/rate-limits/paragraph-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/paragraph-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/changelog/paragraph-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/paragraph-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/mcp/paragraph-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/paragraph-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paragraph/refs/heads/main/well-known/paragraph-robots.txt
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
overview: 'Paragraph publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Coins API, and 7 more. Tagged areas include Company, Publishing, Newsletters, Web3, and Content.


  Paragraph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Paragraph Plans Pricing
  plan_count: 5
  slug: paragraph-plans-pricing
random_paper: 4
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
  composite: 57.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 57.0
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
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
