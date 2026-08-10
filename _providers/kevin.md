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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'PSD2 open-banking platform API: Authentication, General, Payment Initiation (PIS) and Account Information (AIS) services for account-to-account bank payments, card (hybrid) payments, refunds and accou'
  name: kevin. platform API
  slug: kevin-platform-api
artifact_total: 6
asyncapis:
- description: ''
  name: Kevin Webhooks
  slug: kevin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kevin.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kevin.eu/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.kevin.eu/public/platform/v0.3
- group: build
  title: ''
  type: Packages
  url: packages/kevin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kevin-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kevin-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kevin-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kevin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kevin-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kevin-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kevin-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kevin-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kevin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kevin-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kevin-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kevin-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kevin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kevin-domain-security.yml
created: '2026-07-17'
description: kevin. was a Lithuanian account-to-account (A2A) payments infrastructure company providing PSD2 open-banking Payment Initiation and Account Information services to merchants across 28 European countries. Its platform API let businesses initiate bank (SEPA) and card (hybrid) payments, issue refunds, read account data, and receive signed payment webhooks through a single integration to hundreds of banks, supported by an official Node.js SDK, a CLI, and a React UI component library. Backed by Accel. The company has wound down its public web presence - kevin.eu no longer resolves as of 2026-07 - and this profile is enriched from kevin.'s published npm packages and archived developer reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kevin.png
layout: provider
mcp_servers:
- description: ''
  name: kevin-mcp.yml
  slug: kevin-mcpyml
modified: '2026-07-19'
name: Kevin.
nav: Providers
network: true
overview: 'Kevin. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Open Banking, Account to Account, and PSD2.


  The Kevin. catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kevin.''s developer surface includes documentation, API reference, CLI, authentication, and 15 more developer resources.'
random_paper: 77
scopes:
- name: Kevin Scopes
  scope_count: 2
  slug: kevin-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 32.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Kevin Authentication
  slug: kevin-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Kevin Domain Security
  slug: kevin-domain-security
  summary_line: no transport/DNS hardening detected
slug: kevin
tags:
- Company
- Payments
- Open Banking
- Account to Account
- PSD2
- Fintech
- Bank Payments
- Payment Initiation
- Account Information
- Europe
website: https://www.kevin.eu/
---
