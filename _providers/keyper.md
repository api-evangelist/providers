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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 26.0
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Retrieve the permission whitelist / blacklist for an Access Control System.
  name: Keyper Permissions API
  slug: keyper-permissions-api
- description: Send access / entry transactions to keyper.
  name: Keyper Transactions API
  slug: keyper-transactions-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.keyper.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.keyper.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.keyper.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.keyper.com
- group: operate
  title: ''
  type: Support
  url: https://support.keyper.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://www.keyper.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keyper
- group: start
  title: ''
  type: Login
  url: https://app.keyper.io/business/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keyper.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keyper.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.keyper.com
- group: build
  title: ''
  type: Packages
  url: packages/keyper-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keyper-packages.yml
- group: design
  title: ''
  type: Components
  url: components/keyper-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/keyper-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keyper-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keyper-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keyper-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keyper-domain-security.yml
created: '2026-07-17'
description: keyper is an Austrian technology company providing connected ticketing and digital access solutions. Its developer platform lets ticketing systems, resellers and access control systems (ACS) deliver e-tickets and exchange access data through the keyper Access API, Connect Provider / Reseller APIs, Ticket Delivery API, native Android and iOS SDKs, and embeddable web components (seatmaps and checkout). The Access API sends entry transactions for keys (ticket barcodes) and their permissions (events), and returns the Grant / Block permission whitelist an access control system enforces at the gate. keyper serves sports, arts and culture organisations across Austria and Central Europe and is backed by Speedinvest.
image: https://www.keyper.com/wp-content/uploads/keyper-logo.png
layout: provider
modified: '2026-07-19'
name: Keyper
nav: Providers
network: true
overview: 'Keyper publishes 2 APIs on the [APIs.io](https://apis.io/) network: Permissions API and Transactions API. Tagged areas include Company, Ticketing, Access Control, Events, and Developer Platform.


  Keyper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 14 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.9
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 44.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Keyper Authentication
  slug: keyper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keyper Domain Security
  slug: keyper-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keyper
tags:
- Company
- Ticketing
- Access Control
- Events
- Developer Platform
- SDK
- Sports
- Arts and Culture
- Austria
website: https://www.keyper.com
---
