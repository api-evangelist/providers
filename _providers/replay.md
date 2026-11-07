---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL API for retrieving workspace and user metadata — replays/recordings, team members, and comments on a replay. POST queries to the endpoint with a Replay API key as a bearer token.
  name: Replay GraphQL API
  slug: replay-graphql-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/replay/plans/replay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/replay-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.replay.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.replay.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.replay.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.replay.io/reference/integrations/replay-apis/replay-protocol
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.replay.io/basics/getting-started/record-your-app
- group: company
  title: ''
  type: Blog
  url: https://www.replay.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replayio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.replay.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.replay.io/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@replay.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.replay.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.replay.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replay.io
- group: agent
  href: https://artifacts.apis.io/replay/mcp/replay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/replay-mcp.yml
- group: build
  href: https://artifacts.apis.io/replay/packages/replay-packages.yml
  title: ''
  type: Packages
  url: packages/replay-packages.yml
- group: build
  href: https://artifacts.apis.io/replay/packages/replay-packages.yml
  title: ''
  type: SDKs
  url: packages/replay-packages.yml
- group: build
  href: https://artifacts.apis.io/replay/cli/replay-cli.yml
  title: ''
  type: CLI
  url: cli/replay-cli.yml
- group: agent
  href: https://artifacts.apis.io/replay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/replay/well-known/replay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/replay-well-known.yml
- group: other
  href: https://artifacts.apis.io/replay/well-known/replay-www-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/replay-www-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/replay/authentication/replay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/replay-authentication.yml
- group: design
  href: https://artifacts.apis.io/replay/conventions/replay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/replay-conventions.yml
- group: operate
  href: https://artifacts.apis.io/replay/changelog/replay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/replay-changelog.yml
- group: design
  href: https://artifacts.apis.io/replay/lifecycle/replay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/replay-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/replay/conformance/replay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/replay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.replay.io/blog/replay-achieves-soc2
- group: auth
  href: https://artifacts.apis.io/replay/security/replay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/replay-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/replay/security/replay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/replay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.replay.io/privacy-policy
- group: auth
  href: https://artifacts.apis.io/replay/security/replay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/replay-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/replay/llms/replay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/replay-llms.txt
created: '2026-07-17'
description: Replay is an AI-native QA and time-travel debugging platform for web applications. Replay QA autonomously explores a web app, records every session in a deterministic Replay Browser, finds real bugs, and hands a coding agent the root cause and a suggested fix. The recording is a time-travel database of everything that happened in the browser — sources, console, network, DOM, React renders — inspectable after the fact without reproducing the bug locally. Replay exposes this programmatically through a GraphQL API, a WebSocket Replay Protocol, a published Model Context Protocol (MCP) server for agent debugging, a CLI (replayio), and Playwright/Cypress recording integrations. Backed by a16z and Version One Ventures.
finops:
- has_sources: true
  method: derived
  name: Replay Finops
  primary_unit: subscription
  service_category: ''
  slug: replay-finops
  template: false
image: https://www.replay.io/replayQA_og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at dispatch.replay.io over HTTP; 32 tools listed.
  name: Replay MCP
  slug: replay-mcp
modified: '2026-07-20'
name: Replay
nav: Providers
network: true
overview: 'Replay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Debugging, Testing, Quality Assurance, and Developer Tools.


  Replay''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 25 more developer resources.'
plans:
- name: Replay Plans Pricing
  plan_count: 5
  slug: replay-plans-pricing
- name: Replay Price Estimates
  plan_count: 0
  slug: replay-price-estimates
random_paper: 5
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 52.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/replay/replay-2026-08-17T081521.png
security:
- kind: authentication
  name: Replay Authentication
  slug: replay-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Replay Domain Security
  slug: replay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Replay Vulnerability Disclosure
  slug: replay-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Replay Trust Center
  slug: replay-trust-center
  summary_line: SOC 2 Type 2
skill_count: 4
skills:
- name: replay-cli
  slug: replay-cli
- name: replay-cypress
  slug: replay-cypress
- name: replay-mcp
  slug: replay-mcp
- name: replay-playwright
  slug: replay-playwright
slug: replay
tags:
- Company
- Debugging
- Testing
- Quality Assurance
- Developer Tools
- Time Travel Debugging
- MCP
- GraphQL
- Browser Automation
- Artificial Intelligence
website: https://www.replay.io
---
