---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.0
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://testsprite.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.testsprite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.testsprite.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.testsprite.com/cli/reference/command-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.testsprite.com/mcp/getting-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.testsprite.com/cli/getting-started/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TestSprite
- group: company
  title: ''
  type: Blog
  url: https://www.testsprite.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.testsprite.com/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.testsprite.com/cli/reference/whats-included
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/QQB9tJ973e
- group: commercial
  title: ''
  type: Pricing
  url: https://www.testsprite.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.testsprite.com/auth/cognito/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.testsprite.com/auth/cognito/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.testsprite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.testsprite.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/mcp/testsprite-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/testsprite-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/cli/testsprite-cli.yml
  title: ''
  type: CLI
  url: cli/testsprite-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/packages/testsprite-packages.yml
  title: ''
  type: Packages
  url: packages/testsprite-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/authentication/testsprite-authentication.yml
  title: ''
  type: Authentication
  url: authentication/testsprite-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/scopes/testsprite-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/testsprite-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/errors/testsprite-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/testsprite-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/conventions/testsprite-conventions.yml
  title: ''
  type: Conventions
  url: conventions/testsprite-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/conventions/testsprite-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/testsprite-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/lifecycle/testsprite-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/testsprite-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/security/testsprite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/testsprite-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/conformance/testsprite-conformance.yml
  title: ''
  type: Conformance
  url: conformance/testsprite-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/llms/testsprite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/testsprite-llms.txt
created: '2026-07-17'
description: 'TestSprite is an AI-powered software testing platform (a Techstars-backed company) that gives autonomous coding agents a verification loop: it uses an app like a real user, generates and executes end-to-end UI and backend API tests, and returns actionable failure bundles (screenshots, DOM snapshots, root causes, and fix suggestions) so an agent can repair its own work before bugs ship. It is delivered as an official Model Context Protocol (MCP) server that runs inside AI coding assistants (Cursor, Claude Code, VS Code, Copilot), a first-party command-line interface for terminal and CI/CD use, a browser Web Portal, and a GitHub App that tests every pull request. Authentication is by scoped API key.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testsprite.png
layout: provider
mcp_servers:
- description: TestSprite operates an official Model Context Protocol server that puts its autonomous testing agent inside an AI coding assistant (Cursor, Claude Code, VS Code, Copilot). It runs locally over stdio v
  name: TestSprite
  slug: testsprite
modified: '2026-07-21'
name: TestSprite
nav: Providers
network: true
overview: 'TestSprite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Testing, API Testing, Test Automation, and Artificial Intelligence.


  TestSprite''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, changelog, support, and 22 more developer resources.'
random_paper: 11
scopes:
- name: Testsprite Scopes
  scope_count: 5
  slug: testsprite-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 57.4
    operational_transparency: 23.7
  previous_composite: 31.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/testsprite/refs/heads/main/screenshots/testsprite-2026-09-02T163244.png
security:
- kind: authentication
  name: Testsprite Authentication
  slug: testsprite-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Testsprite Domain Security
  slug: testsprite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: testsprite
tags:
- Company
- Software Testing
- API Testing
- Test Automation
- Artificial Intelligence
- Developer Tools
- MCP
- Quality Assurance
- CI/CD
- Agentic
website: https://testsprite.com/
---
