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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Vooma Agentic Access
  operation_count: 35
  slug: vooma-agentic-access
  summary_line: 35 operations · 29 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The Carriers API from Vooma — 2 operation(s) for carriers.
  name: Vooma Carriers API
  slug: vooma-carriers-api
- description: The Contacts API from Vooma — 2 operation(s) for contacts.
  name: Vooma Contacts API
  slug: vooma-contacts-api
- description: The Customers API from Vooma — 3 operation(s) for customers.
  name: Vooma Customers API
  slug: vooma-customers-api
- description: The Locations API from Vooma — 2 operation(s) for locations.
  name: Vooma Locations API
  slug: vooma-locations-api
- description: The Movements API from Vooma — 4 operation(s) for movements.
  name: Vooma Movements API
  slug: vooma-movements-api
- description: The Quotes API from Vooma — 2 operation(s) for quotes.
  name: Vooma Quotes API
  slug: vooma-quotes-api
- description: The Shipments API from Vooma — 3 operation(s) for shipments.
  name: Vooma Shipments API
  slug: vooma-shipments-api
- description: The Tracking Status API from Vooma — 1 operation(s) for tracking status.
  name: Vooma Tracking Status API
  slug: vooma-tracking-status-api
- description: The Webhooks API from Vooma — 10 operation(s) for webhooks.
  name: Vooma Webhooks API
  slug: vooma-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Vooma Webhooks
  slug: vooma-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: api Carriers API
  slug: open-vooma-carriers-api
- collection_type: open
  name: api Carriers Contacts API
  slug: open-vooma-contacts-api
- collection_type: open
  name: api Carriers Customers API
  slug: open-vooma-customers-api
- collection_type: open
  name: api Carriers Locations API
  slug: open-vooma-locations-api
- collection_type: open
  name: api Carriers Movements API
  slug: open-vooma-movements-api
- collection_type: open
  name: api Carriers Quotes API
  slug: open-vooma-quotes-api
- collection_type: open
  name: api Carriers Shipments API
  slug: open-vooma-shipments-api
- collection_type: open
  name: api Carriers Tracking Status API
  slug: open-vooma-tracking-status-api
- collection_type: open
  name: api Carriers Webhooks API
  slug: open-vooma-webhooks-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vooma-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vooma-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vooma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.vooma.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vooma.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vooma.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vooma.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vooma.ai/development
- group: operate
  title: ''
  type: Support
  url: mailto:support@vooma.ai
- group: company
  title: ''
  type: Blog
  url: https://www.vooma.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vooma-ai
- group: start
  title: ''
  type: Login
  url: https://app.vooma.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vooma.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vooma.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vooma.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.vooma.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.vooma.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vooma-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vooma-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vooma-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vooma-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vooma-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vooma-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vooma-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/vooma-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vooma-openapi-overlay.yaml
created: '2026-07-17'
description: Vooma builds AI agents for the freight industry, automating the back office of freight brokers and carriers. Its agents quote loads from email, build orders in the TMS, schedule facility appointments, cover loads with carriers, and track shipments end to end. The Vooma Public API (api.vooma.ai/v0) lets enterprise customers integrate their own TMS, exposing quotes, shipments, movements, carriers, customers, locations, contacts, and tracking status, with webhook events for orders, carriers, customers, locations, appointments, and tracking updates.
image: https://cdn.prod.website-files.com/68ed090d0998c3c224a59e7c/69125b78bbe508e2ec38f42d_vooma-webclip.png
layout: provider
mcp_servers:
- description: ''
  name: vooma-mcp.yml
  slug: vooma-mcpyml
modified: '2026-07-21'
name: Vooma
nav: Providers
network: true
overview: 'Vooma publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Contacts API, Customers API, and 6 more. Tagged areas include Company, AI, Freight, Logistics, and Transportation.


  The Vooma catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vooma''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 99
score:
  band: developing
  composite: 48.1
  delta: -0.8
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 55.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vooma/refs/heads/main/screenshots/vooma-2026-08-17T082822.png
security:
- kind: authentication
  name: Vooma Authentication
  slug: vooma-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Vooma Domain Security
  slug: vooma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vooma Trust Center
  slug: vooma-trust-center
  summary_line: SOC 2
slug: vooma
tags:
- Company
- AI
- Freight
- Logistics
- Transportation
- Brokers
- TMS
- Agents
website: https://www.vooma.com
---
