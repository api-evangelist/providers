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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 52.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Harmony Agentic Access
  operation_count: 9
  slug: harmony-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The tickets API from Harmony — 6 operation(s) for tickets.
  name: Harmony tickets API
  slug: harmony-tickets-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a service-desk ticket, read it back, triage it, and audit the change.
  name: Harmony — create and triage an IT ticket
  slug: harmony-create-and-triage-ticket
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmony-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.harmony.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.harmony.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.harmony.io/api-references/api-documentation/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.harmony.io/getting-started/welcome
- group: operate
  title: ''
  type: Support
  url: mailto:support@harmony.io
- group: company
  title: ''
  type: Blog
  url: https://harmony.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harmonyso
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harmony.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harmony.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harmony.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.harmony.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmony-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harmony-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/harmony-create-and-triage-ticket.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harmony-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harmony-authentication.yml
created: '2026-07-17'
description: Harmony is an agentic enterprise service management (ESM) platform that gives every employee an always-on AI expert for IT, HR, finance, procurement, and legal service requests inside Slack and Microsoft Teams. Its AI agents autonomously resolve requests — password and MFA resets, application access, device recovery, employee onboarding and offboarding — using a context graph that connects each employee's identity, devices, applications, and history, often resolving issues before a ticket is opened. Harmony exposes a public REST Service Desk API for programmatically listing, creating, updating, querying, and bulk-updating tickets along with their custom fields and activity history. Founded in 2025 by Nitzan Shapira and Ran Ribenzaft and backed by Lightspeed Venture Partners.
image: https://harmony.io/favicon.ico
layout: provider
modified: '2026-07-19'
name: Harmony
nav: Providers
network: true
overview: 'Harmony publishes 1 API on the [APIs.io](https://apis.io/) network: tickets API. Tagged areas include IT Service Management, Service Desk, Ticketing, Enterprise Service Management, and AI Agents.


  Harmony''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 2
  name: Harmony Rate Limits
  slug: harmony-rate-limits
score:
  band: thin
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.4
    developer_ergonomics: 58.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 44.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harmony/refs/heads/main/screenshots/harmony-2026-07-25T220731.png
security:
- kind: authentication
  name: Harmony Authentication
  slug: harmony-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Harmony Domain Security
  slug: harmony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harmony
tags:
- IT Service Management
- Service Desk
- Ticketing
- Enterprise Service Management
- AI Agents
- IT Automation
- Help Desk
- Identity
- Company
website: https://docs.harmony.io/
---
