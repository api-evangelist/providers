---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 42
  human_in_the_loop: 5
  name: Coasty Agentic Access
  operation_count: 72
  slug: coasty-agentic-access
  summary_line: 72 operations · 42 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: API key management and usage reporting.
  name: Coasty Keys API
  slug: coasty-keys-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Provision and control managed VMs.
  name: Coasty Machines API
  slug: coasty-machines-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Stateless CUA action prediction and grounding.
  name: Coasty Predict API
  slug: coasty-predict-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Autonomous task runs — the agent drives a task to completion on a machine.
  name: Coasty Runs API
  slug: coasty-runs-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Cron and one-shot scheduled CUA jobs.
  name: Coasty Schedules API
  slug: coasty-schedules-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Stateful CUA sessions with persistent trajectory.
  name: Coasty Sessions API
  slug: coasty-sessions-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Webhook and chain triggers for schedules.
  name: Coasty Triggers API
  slug: coasty-triggers-api
- baseURL: https://coasty.ai
  baseurl_source: declared
  description: Versioned, branching multi-step automations (DSL) and their runs.
  name: Coasty Workflows API
  slug: coasty-workflows-api
artifact_total: 33
asyncapis:
- description: ''
  name: Coasty Webhooks
  slug: coasty-webhooks
collections:
- collection_type: postman
  name: Coasty Public keys API
  slug: postman-coasty-keys-api
- collection_type: postman
  name: Coasty Public keys machines API
  slug: postman-coasty-machines-api
- collection_type: postman
  name: Coasty Public keys predict API
  slug: postman-coasty-predict-api
- collection_type: postman
  name: Coasty Public keys runs API
  slug: postman-coasty-runs-api
- collection_type: postman
  name: Coasty Public keys schedules API
  slug: postman-coasty-schedules-api
- collection_type: postman
  name: Coasty Public keys sessions API
  slug: postman-coasty-sessions-api
- collection_type: postman
  name: Coasty Public keys triggers API
  slug: postman-coasty-triggers-api
- collection_type: postman
  name: Coasty Public keys workflows API
  slug: postman-coasty-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coasty Public keys API
  slug: open-coasty-keys-api
- collection_type: open
  name: Coasty Public keys machines API
  slug: open-coasty-machines-api
- collection_type: open
  name: Coasty Public keys predict API
  slug: open-coasty-predict-api
- collection_type: open
  name: Coasty Public keys runs API
  slug: open-coasty-runs-api
- collection_type: open
  name: Coasty Public keys schedules API
  slug: open-coasty-schedules-api
- collection_type: open
  name: Coasty Public keys sessions API
  slug: open-coasty-sessions-api
- collection_type: open
  name: Coasty Public keys triggers API
  slug: open-coasty-triggers-api
- collection_type: open
  name: Coasty Public keys workflows API
  slug: open-coasty-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coasty/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/security/coasty-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coasty-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://coasty.ai/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/security/coasty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coasty-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/agentic-access/coasty-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coasty-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/authentication/coasty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coasty-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coasty.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coasty.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://coasty.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://coasty.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://coasty.ai/guide?tab=api
- group: company
  title: ''
  type: Blog
  url: https://coasty.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://coasty.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coasty.ai/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coasty.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coasty.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:founders@coasty.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coasty-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coasty.ai
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/openapi/_original/coasty-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/coasty-openapi-original.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/overlays/coasty-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coasty-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/llms/coasty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coasty-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/well-known/coasty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coasty-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/well-known/coasty-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coasty-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/mcp/coasty-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coasty-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/packages/coasty-packages.yml
  title: ''
  type: Packages
  url: packages/coasty-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/conventions/coasty-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coasty-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/conventions/coasty-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coasty-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/errors/coasty-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coasty-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/conformance/coasty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coasty-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/lifecycle/coasty-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coasty-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/lifecycle/coasty-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/coasty-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/sandbox/coasty-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/coasty-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/data-model/coasty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coasty-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/asyncapi/coasty-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coasty-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/plans/coasty-plans.yml
  title: ''
  type: Plans
  url: plans/coasty-plans.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/rate-limits/coasty-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coasty-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Coasty is a computer-use AI agent platform (Y Combinator S26) that operates a full desktop, browser, and terminal like a human — reading the screen with vision, clicking, typing, filling forms, running commands, and verifying its own work across sandboxed virtual machines. It exposes a public REST API at coasty.ai/v1 with a published OpenAPI 3.1 spec (72 operations), a first-party MCP server (npx @coasty/mcp, 26 tools), free sandbox keys, HMAC-SHA256 webhook triggers, an Idempotency-Key contract, per-credit metered billing, and 1,000+ OAuth app integrations via Composio. Core API surfaces are Predict, Sessions, Ground, Parse, Machines, Schedules, Runs, and Workflows. Founded 2025-2026 by Prateek Jannu and Nitish Kovuru; #1 on the OSWorld benchmark among production computer-use agents.'
image: https://coasty.ai/icon-512.svg
layout: provider
mcp_servers:
- description: First-party MCP server (npx -y @coasty/mcp; remote https://api.coasty.ai/mcp) exposing 26 computer-use tools across predict, machines, schedules, account, and discovery groups.
  name: Coasty Computer-Use MCP Server
  slug: coasty-computer-use-mcp-server
modified: '2026-07-18'
name: Coasty
nav: Providers
network: true
overview: 'Coasty publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Keys API, Machines API, Predict API, and 5 more. Tagged areas include Company, Computer Use, AI Agents, Automation, and RPA.


  The Coasty catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coasty''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Coasty Plans
  plan_count: 4
  slug: coasty-plans
random_paper: 21
rate_limits:
- limit_count: 2
  name: Coasty Rate Limits
  slug: coasty-rate-limits
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 67.2
    developer_ergonomics: 55.4
    discoverability: 75.9
    operational_transparency: 52.6
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/screenshots/coasty-2026-07-25T205838.png
security:
- kind: authentication
  name: Coasty Authentication
  slug: coasty-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Coasty Domain Security
  slug: coasty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coasty Vulnerability Disclosure
  slug: coasty-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coasty
tags:
- Company
- Computer Use
- AI Agents
- Automation
- RPA
- Desktop Automation
- Browser Automation
- MCP
- Virtual Machines
- Developer Tools
website: https://coasty.ai
---
