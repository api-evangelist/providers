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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Retrieve the permission whitelist / blacklist for an Access Control System.
  name: Keyper Permissions API
  slug: keyper-permissions-api
- description: Send access / entry transactions to keyper.
  name: Keyper Transactions API
  slug: keyper-transactions-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: keyper Access Permissions API
  slug: open-keyper-permissions-api
- collection_type: open
  name: keyper Access Permissions Transactions API
  slug: open-keyper-transactions-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keyper-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/keyper-access-overlay.yaml
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
mcp_servers:
- description: ''
  name: Keyper MCP Server
  slug: keyper-mcp-server
modified: '2026-07-19'
name: Keyper
nav: Providers
network: true
overview: 'Keyper publishes 2 APIs on the [APIs.io](https://apis.io/) network: Permissions API and Transactions API. Tagged areas include Company, Ticketing, Access Control, Event, and Developer Platform.


  Keyper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 16 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 14.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 32.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keyper/refs/heads/main/screenshots/keyper-2026-07-25T223658.png
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
- Event
- Developer Platform
- SDK
- Sports
- Arts and Culture
- Austria
website: https://www.keyper.com
---
