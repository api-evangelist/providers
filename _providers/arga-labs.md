---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Public REST API for Arga's testing infrastructure — provision digital twins, deploy branches/PRs into sandboxes, run browser-agent validations, save and replay tests, manage scenarios (seed data), and
  name: Arga API
  slug: arga-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.argalabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.argalabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.argalabs.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.argalabs.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.argalabs.com/get-started
- group: start
  title: ''
  type: Login
  url: https://login.argalabs.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.argalabs.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.argalabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArgaLabs
- group: operate
  title: ''
  type: Support
  url: mailto:contact@argalabs.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arga-labs
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ArgaLabs
- group: auth
  title: ''
  type: Authentication
  url: authentication/arga-labs-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/arga-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/arga-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/arga-labs-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arga-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arga-labs-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/arga-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arga-labs-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arga-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.argalabs.com/api-reference/availability-notes
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arga-labs-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Arga Labs provides testing infrastructure for AI agents and agent-facing software. Its platform spins up isolated, resettable sandboxes wired to stateful "digital twins" of third-party services — Stripe, Slack, GitHub, Salesforce, Notion, Discord, Google Drive, Jira, Box, Dropbox, Gmail, Google Calendar and more — so teams can run browser-agent tests, per-PR preview environments, and CI validation without hitting real APIs, exhausting rate limits, or mutating production data. Developers drive it from a web app, a REST API at api.argalabs.com, the arga CLI, official Python and TypeScript SDKs, and a hosted MCP server that lets coding agents (Cursor, Claude Code, Codex) provision twins and query validation runs directly from the editor.
image: https://www.argalabs.com/logo_black.png
layout: provider
mcp_servers:
- description: ''
  name: Arga Labs MCP Server
  slug: arga-labs-mcp-server
modified: '2026-07-18'
name: Arga Labs
nav: Providers
network: true
overview: 'Arga Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Testing, Sandboxes, Digital Twins, and AI Agents.


  Arga Labs'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 17 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.3
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arga-labs/refs/heads/main/screenshots/arga-labs-2026-07-25T201136.png
security:
- kind: authentication
  name: Arga Labs Authentication
  slug: arga-labs-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Arga Labs Domain Security
  slug: arga-labs-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: arga-labs
tags:
- Company
- API Testing
- Sandboxes
- Digital Twins
- AI Agents
- Developer Tools
- Testing Infrastructure
- CI/CD
- Browser Testing
- MCP
- Mock Services
website: https://docs.argalabs.com/
---
