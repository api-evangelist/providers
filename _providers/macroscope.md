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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Workspaces API from Macroscope — 2 operation(s) for workspaces.
  name: Macroscope Workspaces API
  slug: macroscope-workspaces-api
artifact_total: 7
asyncapis:
- description: ''
  name: Macroscope Webhooks
  slug: macroscope-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Macroscope Agent Webhook Workspaces API
  slug: open-macroscope-workspaces-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/macroscope-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/macroscope-webhook-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macroscope-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.macroscope.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.macroscope.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.macroscope.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.macroscope.com/setup-instructions
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.macroscope.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.macroscope.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prassoai
- group: operate
  title: ''
  type: Support
  url: https://docs.macroscope.com/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.macroscope.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/macroscope-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/macroscope-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/macroscope-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/macroscope-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/macroscope-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/macroscope-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/macroscope-weekly-changes-digest.md
created: '2026-07-17'
description: Macroscope is an AI code-intelligence platform (GitHub org prassoai) that connects to a team's codebase and workflow tools to review pull requests, answer questions, and take action. Its three surfaces are an Agent (query the codebase and trigger actions via Slack, GitHub, or an HTTP API), Code Review (automatic bug detection, PR descriptions, and fixes on every pull request), and Status (commit summaries, area classification, productivity insights, and sprint reports). Macroscope integrates with GitHub, Slack, Jira, Linear, BigQuery, PostHog, LaunchDarkly, and GCP Cloud Logging, ships a local CLI plus plugins for Claude Code, Codex, Cursor, and OpenCode, and exposes a public agent webhook API. Billing is usage-based (prepaid, Stripe-metered). Macroscope is backed by Lightspeed Venture Partners. Enriched into the API Evangelist network from its public developer documentation.
image: https://macroscope.com/assets/macroscop-logo-black.svg
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from Macroscope's documented agent webhook API. Macroscope publishes local plugins for Claude Code, Codex, Cursor, and OpenCode (see cli/macroscope-cli.yml) but no o
  name: Macroscope MCP Server
  slug: macroscope-mcp-server
modified: '2026-07-20'
name: Macroscope
nav: Providers
network: true
overview: 'Macroscope publishes 1 API on the [APIs.io](https://apis.io/) network: Workspaces API. Tagged areas include Company, AI Code Review, Code Intelligence, Developer Tools, and Pull Requests.


  The Macroscope catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Macroscope''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, changelog, and 12 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 22.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 34.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macroscope/refs/heads/main/screenshots/macroscope-2026-07-25T225824.png
security:
- kind: authentication
  name: Macroscope Authentication
  slug: macroscope-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Macroscope Domain Security
  slug: macroscope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: macroscope
tags:
- Company
- AI Code Review
- Code Intelligence
- Developer Tools
- Pull Requests
- Agents
- Webhook
- DevOps
website: https://docs.macroscope.com
---
