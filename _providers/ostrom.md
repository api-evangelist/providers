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
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ostrom Agentic Access
  operation_count: 18
  slug: ostrom-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 1
apis:
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to authenticate in the api
  name: Ostrom Auth API
  slug: ostrom-auth-api
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to fetch information related with contracts
  name: Ostrom Contracts API
  slug: ostrom-contracts-api
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to fetch information related with orders
  name: Ostrom Orders API
  slug: ostrom-orders-api
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to fetch information related with prices
  name: Ostrom Prices API
  slug: ostrom-prices-api
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to fetch information related with products
  name: Ostrom Products API
  slug: ostrom-products-api
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to fetch information related with users
  name: Ostrom Users API
  slug: ostrom-users-api
- baseURL: https://production.ostrom-api.io
  baseurl_source: declared
  description: Describe how to create webhooks and receive notifications from our system.
  name: Ostrom Webhooks API
  slug: ostrom-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Ostrom Webhooks
  slug: ostrom-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ostrom Auth API
  slug: open-ostrom-auth-api
- collection_type: open
  name: Ostrom Auth Contracts API
  slug: open-ostrom-contracts-api
- collection_type: open
  name: Ostrom Auth Orders API
  slug: open-ostrom-orders-api
- collection_type: open
  name: Ostrom Auth Prices API
  slug: open-ostrom-prices-api
- collection_type: open
  name: Ostrom Auth Products API
  slug: open-ostrom-products-api
- collection_type: open
  name: Ostrom Auth Users API
  slug: open-ostrom-users-api
- collection_type: open
  name: Ostrom Auth Webhooks API
  slug: open-ostrom-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ostrom-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ostrom-api.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ostrom-api.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ostrom-api.io/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ostrom-api.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.ostrom.de/
- group: company
  title: ''
  type: Blog
  url: https://ostrom.de/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ostrom.de/en/strompreis
- group: start
  title: ''
  type: SignUp
  url: https://ostrom.de/en/calculate-tariff
- group: start
  title: ''
  type: Login
  url: https://join.ostrom.de
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ostrom.de/en/terms-and-conditions-overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ostrom.de/en/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/ostrom-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ostrom-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ostrom-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ostrom-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ostrom-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ostrom-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ostrom-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ostrom-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ostrom-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ostrom-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ostrom-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ostrom-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ostrom-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://ostrom.de
created: '2026-07-17'
description: 'Ostrom is a fully digital green-energy provider based in Berlin, Germany, offering variable, fixed, and dynamic electricity tariffs managed entirely through a mobile app, with smart-meter integration, device control, EV-charging optimization, and a NeoGrid virtual power plant. Its developer API lets Ostrom customers and partners integrate with the smart energy-management platform: OAuth2-secured REST endpoints for user data, orders, contracts, smart-meter energy consumption, day-ahead EEX spot prices, product pricing, and partner webhooks.'
image: https://cdn.prod.website-files.com/60ec127477c1e52acb31ae8c/60ffd44f1211be9d43aa3bd7_favicon-256x256.png
layout: provider
mcp_servers:
- description: ''
  name: Ostrom MCP Server
  slug: ostrom-mcp-server
modified: '2026-07-20'
name: Ostrom
nav: Providers
network: true
overview: 'Ostrom publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Contracts API, Orders API, and 4 more. Tagged areas include Company, Energy, Electricity, Green Energy, and Smart Meter.


  The Ostrom catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ostrom''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 60.8
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ostrom/refs/heads/main/screenshots/ostrom-2026-08-07T191022.png
security:
- kind: authentication
  name: Ostrom Authentication
  slug: ostrom-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ostrom Domain Security
  slug: ostrom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ostrom
tags:
- Company
- Energy
- Electricity
- Green Energy
- Smart Meter
- Dynamic Pricing
- Germany
- Sustainability
- Webhook
website: https://ostrom.de
---
