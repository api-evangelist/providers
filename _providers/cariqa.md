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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Cariqa Agentic Access
  operation_count: 22
  slug: cariqa-agentic-access
  summary_line: 22 operations · 9 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The Billing Details API from Cariqa — 1 operation(s) for billing details.
  name: Cariqa Billing Details API
  slug: cariqa-billing-details-api
- description: The Charging Sessions API from Cariqa — 4 operation(s) for charging sessions.
  name: Cariqa Charging Sessions API
  slug: cariqa-charging-sessions-api
- description: The Debts API from Cariqa — 1 operation(s) for debts.
  name: Cariqa Debts API
  slug: cariqa-debts-api
- description: The Invoices API from Cariqa — 1 operation(s) for invoices.
  name: Cariqa Invoices API
  slug: cariqa-invoices-api
- description: The Payments API from Cariqa — 4 operation(s) for payments.
  name: Cariqa Payments API
  slug: cariqa-payments-api
- description: The Stations API from Cariqa — 4 operation(s) for stations.
  name: Cariqa Stations API
  slug: cariqa-stations-api
- description: The Users API from Cariqa — 2 operation(s) for users.
  name: Cariqa Users API
  slug: cariqa-users-api
artifact_total: 11
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cariqa-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cariqa-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cariqa-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cariqa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cariqa-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cariqa-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cariqa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cariqa-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/cariqa-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cariqa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cariqa-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cariqa-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cariqa-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cariqa-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cariqa-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cariqa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cariqa.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cariqa.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cariqa.com/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.cariqa.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.cariqa.com/en/
- group: company
  title: ''
  type: Blog
  url: https://cariqa.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cariqa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cariqa.com/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cariqa.com/en/privacy
- group: company
  title: ''
  type: Website
  url: https://cariqa.com/
created: '2026-07-17'
description: Cariqa provides backend-to-backend payment and access infrastructure for EV charging across Europe. Its Connect API lets OEMs, mobility services, fleets and platforms offer electric-vehicle charging through a single integration — discovering charging stations and live connector availability, creating and managing users, collecting payment methods via Stripe (PSD2/SCA compliant), starting and stopping charging sessions on 900,000+ charge points, and retrieving session history, debts and invoices. Cariqa removes reseller markups so charge point operators set the price drivers pay, while platforms earn a transaction revenue share. Backed by Anthemis and Techstars.
image: https://cdn.prod.website-files.com/665b067716979bea8b47153d/698ef2f263134d677dd448fd_cariqa-og-home-1200x630-v1.png
layout: provider
mcp_servers:
- description: ''
  name: cariqa-mcp.yml
  slug: cariqa-mcpyml
modified: '2026-07-18'
name: Cariqa
nav: Providers
network: true
overview: 'Cariqa publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Billing Details API, Charging Sessions API, Debts API, and 4 more. Tagged areas include Company, EV Charging, Electric Vehicles, Payments, and Mobility.


  Cariqa''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, quickstart, and 20 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 44.8
  delta: -2.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.8
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cariqa/refs/heads/main/screenshots/cariqa-2026-07-25T204619.png
security:
- kind: authentication
  name: Cariqa Authentication
  slug: cariqa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cariqa Domain Security
  slug: cariqa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cariqa
tags:
- Company
- EV Charging
- Electric Vehicles
- Payments
- Mobility
- e-Mobility
- Charge Point Operator
- Energy
website: https://cariqa.com/
---
