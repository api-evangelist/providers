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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Clevergy Agentic Access
  operation_count: 83
  slug: clevergy-agentic-access
  summary_line: 83 operations · 43 acting
api_count: 1
apis:
- description: Outbound HTTP callbacks that notify an integrator in real time when a Clevergy lifecycle entity changes. Three event surfaces are documented — User, SalesOpportunity and Ticket — with CREATE, UPDATE a
  name: Clevergy Webhooks
  slug: clevergy-webhooks
- description: 'Roughly thirty embeddable UI components — custom elements (web components) rendering a React tree in an isolated container — that bring Clevergy''s end-user energy experiences into an integrator''s own '
  name: Clevergy Microfrontends
  slug: clevergy-microfrontends
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Access control API from Clevergy — 1 operation(s) for access control.
  name: Clevergy Access control API
  slug: clevergy-access-control-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Connections API from Clevergy — 1 operation(s) for connections.
  name: Clevergy Connections API
  slug: clevergy-connections-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Contracts API from Clevergy — 1 operation(s) for contracts.
  name: Clevergy Contracts API
  slug: clevergy-contracts-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Contracts - Deprecated API from Clevergy — 6 operation(s) for contracts - deprecated.
  name: Clevergy Contracts - Deprecated API
  slug: clevergy-contracts-deprecated-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Contracts|Electricity API from Clevergy — 2 operation(s) for contracts|electricity.
  name: Clevergy Contracts|Electricity API
  slug: clevergy-contracts-electricity-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Contracts|Gas API from Clevergy — 2 operation(s) for contracts|gas.
  name: Clevergy Contracts|Gas API
  slug: clevergy-contracts-gas-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Disaggregation API from Clevergy — 1 operation(s) for disaggregation.
  name: Clevergy Disaggregation API
  slug: clevergy-disaggregation-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Energy API from Clevergy — 3 operation(s) for energy.
  name: Clevergy Energy API
  slug: clevergy-energy-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Energy communities API from Clevergy — 3 operation(s) for energy communities.
  name: Clevergy Energy communities API
  slug: clevergy-energy-communities-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Equipments API from Clevergy — 5 operation(s) for equipments.
  name: Clevergy Equipments API
  slug: clevergy-equipments-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Houses API from Clevergy — 6 operation(s) for houses.
  name: Clevergy Houses API
  slug: clevergy-houses-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Integrations API from Clevergy — 4 operation(s) for integrations.
  name: Clevergy Integrations API
  slug: clevergy-integrations-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Invoices API from Clevergy — 5 operation(s) for invoices.
  name: Clevergy Invoices API
  slug: clevergy-invoices-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Invoices - Deprecated API from Clevergy — 2 operation(s) for invoices - deprecated.
  name: Clevergy Invoices - Deprecated API
  slug: clevergy-invoices-deprecated-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Power API from Clevergy — 1 operation(s) for power.
  name: Clevergy Power API
  slug: clevergy-power-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Sales Opportunities API from Clevergy — 3 operation(s) for sales opportunities.
  name: Clevergy Sales Opportunities API
  slug: clevergy-sales-opportunities-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Settings API from Clevergy — 1 operation(s) for settings.
  name: Clevergy Settings API
  slug: clevergy-settings-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Tariffs API from Clevergy — 4 operation(s) for tariffs.
  name: Clevergy Tariffs API
  slug: clevergy-tariffs-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Tickets API from Clevergy — 3 operation(s) for tickets.
  name: Clevergy Tickets API
  slug: clevergy-tickets-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Tips API from Clevergy — 1 operation(s) for tips.
  name: Clevergy Tips API
  slug: clevergy-tips-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Users API from Clevergy — 6 operation(s) for users.
  name: Clevergy Users API
  slug: clevergy-users-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Virtual battery API from Clevergy — 1 operation(s) for virtual battery.
  name: Clevergy Virtual battery API
  slug: clevergy-virtual-battery-api
- baseURL: https://connect.clever.gy
  baseurl_source: declared
  description: The Virtual wallet API from Clevergy — 1 operation(s) for virtual wallet.
  name: Clevergy Virtual wallet API
  slug: clevergy-virtual-wallet-api
artifact_total: 31
asyncapis:
- description: ''
  name: Clevergy Webhooks
  slug: clevergy-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/clevergy-connect-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://clever.gy/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.clever.gy/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clever.gy/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clever.gy/connect-api/clevergy-connect-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clever.gy/developer/getting-started/authentication
- group: operate
  title: ''
  type: Support
  url: https://clever.gy/en/contacto/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.clever.gy/helpdesk
- group: company
  title: ''
  type: Blog
  url: https://clever.gy/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Clevergy
- group: start
  title: ''
  type: Login
  url: https://portal.clever.gy/
- group: start
  title: ''
  type: SignUp
  url: https://clever.gy/en/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clever.gy/en/terms-conditions-web/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clever.gy/en/politica-de-privacidad/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://clever.gy/en/aviso-legal/
- group: operate
  title: ''
  type: FAQ
  url: https://clever.gy/en/faq/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/clevergy/clevergy-public-workspace
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.clever.gy/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clevergy-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/clevergy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clevergy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clevergy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clevergy-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clevergy-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clevergy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clevergy-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clevergy-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/clevergy-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/clevergy-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clevergy-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clevergy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clevergy-domain-security.yml
created: '2026-08-17'
description: 'Clevergy (The Clevergy Solution, SL) is a Madrid-based climate-tech SaaS company, founded in 2022, that sells white-label energy-management software to electricity and gas retailers, solar installers and energy advisors. Its platform ingests household consumption data — pulled directly from Spanish distributors and the Datadis smart-meter hub via the CUPS supply-point code, or from connected solar inverters and smart devices — and turns it into consumption analytics, invoice breakdowns, savings recommendations, appliance-level disaggregation, virtual battery and wallet balances, energy-community shares, and sales leads the retailer can act on. Integrators consume it two ways: the Connect API, a Swagger 2.0 REST API on connect.clever.gy with 83 operations spanning users, houses, contracts, invoices, tariffs, equipment, energy telemetry, tickets and sales opportunities; and a catalog of roughly thirty embeddable "microfrontend" web components that drop Clevergy''s end-user experiences
  straight into the retailer''s own app or webview, authenticated with a short-lived per-user JWT. Clevergy raised a €3.2M round in October 2025 co-led by Racine² (Serena and Makesense) and Axon Partners Group, with Satgana, Wayra and Angels participating.'
image: https://clever.gy/wp-content/uploads/2024/09/cropped-favicon-isotipo-clevergy.png
layout: provider
modified: '2026-08-17'
name: Clevergy
nav: Providers
network: true
overview: 'Clevergy publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Access control API, Connections API, Contracts API, and 20 more. Tagged areas include Company, Climate Tech, Energy, Energy Management, and Utilities.


  The Clevergy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clevergy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, FAQ, and 26 more developer resources.'
plans:
- name: Clevergy Plans Pricing
  plan_count: 2
  slug: clevergy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Clevergy Rate Limits
  slug: clevergy-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 62.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 43.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clevergy/refs/heads/main/screenshots/clevergy-2026-09-02T145107.png
security:
- kind: authentication
  name: Clevergy Authentication
  slug: clevergy-authentication
  summary_line: apiKey/bearer-jwt · 3 schemes
- kind: domain-security
  name: Clevergy Domain Security
  slug: clevergy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clevergy
tags:
- Company
- Climate Tech
- Energy
- Energy Management
- Utilities
- Smart Meter
- Solar
- Home Energy
- Battery Storage
- Electric Vehicle Charging
- Smart Home
- Sustainability
- Spain
- White Label
- Embedded Components
- Webhook
website: https://clever.gy/en/
---
