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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Airspace Technologies Agentic Access
  operation_count: 33
  slug: airspace-technologies-agentic-access
  summary_line: 33 operations · 15 acting
api_count: 6
apis:
- description: We support listing reusable address entries.
  name: Airspace Technologies Address Books API
  slug: airspace-technologies-address-books-api
- description: We support listing invoices for Orders. Please reach out to account manager for setup
  name: Airspace Technologies Invoices API
  slug: airspace-technologies-invoices-api
- description: We support generating labels for Orders.
  name: Airspace Technologies Labels API
  slug: airspace-technologies-labels-api
- description: We support order creation, updates, cancellation, information, and document upload.
  name: Airspace Technologies Orders API
  slug: airspace-technologies-orders-api
- description: We support listing reusable piece entries.
  name: Airspace Technologies Piece Libraries API
  slug: airspace-technologies-piece-libraries-api
- description: We support generating a Quote for a potential Order as well as confirming that Quote to place an Order.
  name: Airspace Technologies Quotes API
  slug: airspace-technologies-quotes-api
artifact_total: 12
asyncapis:
- description: ''
  name: Airspace Technologies Webhooks
  slug: airspace-technologies-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.airspace.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.airspace.com/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.airspace.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.airspace.com/api-docs/v3
- group: start
  title: ''
  type: GettingStarted
  url: https://api.airspace.com/api-docs/v3
- group: start
  title: ''
  type: Login
  url: https://app.airspacetechnologies.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.airspace.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airspace.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AirspaceTechnologies
- group: operate
  title: ''
  type: StatusPage
  url: https://airspace.statuspage.io
- group: auth
  title: ''
  type: TrustCenter
  url: security/airspace-technologies-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.airspace.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airspace-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airspace-technologies-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airspace-technologies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airspace-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airspace-technologies-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/airspace-technologies-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airspace-technologies-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/airspace-technologies-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airspace-technologies-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airspace-technologies-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airspace-technologies-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airspace-technologies-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Airspace Technologies is a time-critical logistics provider that uses AI-driven routing to move urgent, high-value freight via Next Flight Out (NFO), on-demand ground, charter, and specialty services across 80+ countries. Its public REST API (current V3, prior V2) supports order creation, quote generation, and active shipment monitoring. The API is asynchronous, authenticates with a non-expiring bearer token, paginates lists with page/page_limit, and pushes milestone, delay, and cancellation updates over webhooks correlated by request_id.
image: https://www.airspacetechnologies.com/hubfs/Updated%20logos/Airspace%20horizontal%20logotype%20black%20and%20green%20no%20background%20011321%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: airspace-technologies-mcp.yml
  slug: airspace-technologies-mcpyml
modified: '2026-07-17'
name: Airspace Technologies
nav: Providers
network: true
overview: 'Airspace Technologies publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Address Books API, Invoices API, Labels API, and 3 more. Tagged areas include Company, Logistics, Shipping, Freight, and Supply Chain.


  The Airspace Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airspace Technologies'' developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 19 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 50.9
  delta: -1.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.3
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airspace-technologies/refs/heads/main/screenshots/airspace-technologies-2026-07-25T195443.png
security:
- kind: authentication
  name: Airspace Technologies Authentication
  slug: airspace-technologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airspace Technologies Domain Security
  slug: airspace-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Airspace Technologies Trust Center
  slug: airspace-technologies-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: airspace-technologies
tags:
- Company
- Logistics
- Shipping
- Freight
- Supply Chain
- Transportation
- Webhooks
- Orders
website: https://www.airspace.com/
---
