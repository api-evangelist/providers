---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 27.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Clevergy Agentic Access
  operation_count: 83
  slug: clevergy-agentic-access
  summary_line: 83 operations · 43 acting
api_count: 3
apis:
- description: 'REST API that lets Clevergy customers build integrations with the Clevergy platform: manage end users and their houses, create and maintain electricity and gas contracts with their energy price tables'
  name: Clevergy Connect API
  slug: clevergy-connect-api
- description: Outbound HTTP callbacks that notify an integrator in real time when a Clevergy lifecycle entity changes. Three event surfaces are documented — User, SalesOpportunity and Ticket — with CREATE, UPDATE a
  name: Clevergy Webhooks
  slug: clevergy-webhooks
- description: 'Roughly thirty embeddable UI components — custom elements (web components) rendering a React tree in an isolated container — that bring Clevergy''s end-user energy experiences into an integrator''s own '
  name: Clevergy Microfrontends
  slug: clevergy-microfrontends
artifact_total: 9
asyncapis:
- description: ''
  name: Clevergy Webhooks
  slug: clevergy-webhooks
common:
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
overview: 'Clevergy publishes 1 API on the [APIs.io](https://apis.io/) network: Connect API. Tagged areas include Company, Climate Tech, Energy, Energy Management, and Utilities.


  The Clevergy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clevergy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, FAQ, and 25 more developer resources.'
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
  composite: 54.1
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 16.7
    contract_quality: 64.6
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 43.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
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
