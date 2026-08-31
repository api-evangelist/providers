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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ranger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ranger.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ranger.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ranger.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ranger.net/getting-started/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://www.ranger.net/post/why-we-built-a-qa-agent-for-our-background-agent
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ranger.net/pricing
- group: start
  title: ''
  type: Login
  url: https://login.ranger.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ranger.net/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ranger.net/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:howdy@ranger.net
- group: auth
  title: ''
  type: Authentication
  url: authentication/ranger-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ranger-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/ranger-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ranger-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ranger-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ranger-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ranger-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ranger-llms.txt
created: '2026-07-17'
description: 'Ranger is an AI-powered quality-assurance platform that lets coding agents verify their own work in a real browser. Its CLI (@ranger-testing/ranger-cli) sets up a project so an AI coding agent — Claude Code, OpenCode, Cursor, Codex, or any bash-capable agent — can run autonomous end-to-end feature reviews: creating scenarios, driving Chromium, self-maintaining broken tests, auto-scaling parallel browsers, and collecting screenshots, recordings, and traces as evidence, with results reviewed on a shared dashboard. Ranger is agent-native rather than a conventional REST API: it ships a Claude Code plugin (ranger@trailhead), Agent Skills installed to .claude/skills/, slash commands, hooks, and OAuth 2.0 / OpenID Connect authentication (login.ranger.net), with MCP-based auth delegation for managed agent platforms. Backed by General Catalyst and Homebrew.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ranger.png
layout: provider
modified: '2026-07-20'
name: Ranger
nav: Providers
network: true
overview: 'Ranger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quality Assurance, Testing, Browser Automation, and Artificial Intelligence.


  Ranger''s developer surface includes documentation, getting-started guide, engineering blog, pricing, support, authentication, CLI, and 12 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Ranger Authentication
  slug: ranger-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Ranger Domain Security
  slug: ranger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ranger Trust Center
  slug: ranger-trust-center
  summary_line: trust center published
slug: ranger
tags:
- Company
- Quality Assurance
- Testing
- Browser Automation
- Artificial Intelligence
- Agents
- Developer Tools
- DevOps
- CLI
website: https://www.ranger.net
---
