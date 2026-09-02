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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Describes authentication required (`client_credentials` OAuth 2) and refund requests performed by Switchfly application to 3rd party service to cancel redemption components.
  name: Switchfly Machine to Machine (OAuth2 & Refund) API
  slug: switchfly-machine-to-machine-oauth2-refund-api
- description: Switchfly OAuth 2 SSO request to 3rd party
  name: Switchfly OAuth 2 - SSO Authorize API
  slug: switchfly-oauth-2-sso-authorize-api
- description: Information about requests performed by Switchfly system to 3rd party service to fetch Loyalty profile data and redeem points from the customer account.
  name: Switchfly Shopping Flow API
  slug: switchfly-shopping-flow-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Switchfly Loyalty Machine to Machine (OAuth2 & Refund) Machine to Machine (OAuth2 & Refund) Machine to Machine (OAuth2 & Refund) API
  slug: open-switchfly-machine-to-machine-oauth2-refund-api
- collection_type: open
  name: Switchfly Loyalty Machine to Machine (OAuth2 & Refund) Machine to Machine (OAuth2 & Refund) OAuth 2 - SSO Authorize API
  slug: open-switchfly-oauth-2-sso-authorize-api
- collection_type: open
  name: Switchfly Loyalty Machine to Machine (OAuth2 & Refund) Machine to Machine (OAuth2 & Refund) Shopping Flow API
  slug: open-switchfly-shopping-flow-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/switchfly-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/switchfly-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/switchfly-loyalty-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/switchfly-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.switchfly.com/dev/api-documentation/loyalty
- group: docs
  title: ''
  type: Documentation
  url: https://www.switchfly.com/dev/api-documentation/loyalty
- group: docs
  title: ''
  type: APIReference
  url: https://www.switchfly.com/dev/api-documentation/loyalty
- group: company
  title: ''
  type: Blog
  url: https://www.switchfly.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.switchfly.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.switchfly.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.switchfly.com/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/switchfly-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/switchfly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/switchfly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/switchfly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/switchfly-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/switchfly-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/switchfly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/switchfly-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Switchfly is a B2B travel loyalty and commerce technology company that powers white-label travel booking, dynamic packaging, and points-plus-cash redemption for airlines, financial services loyalty programs, and HR/employee-rewards platforms. Its platform connects flights, hotels, cars, and activities to loyalty currencies with real-time pricing, business rules, markups, and 24/7 traveler support, giving partners access to more than 400,000 travel options. Switchfly exposes a REST Loyalty API (v3.4, OpenAPI 3.1) for OAuth2 SSO authentication, traveler-profile retrieval, points redemption, and refunds, plus a family of embeddable travel-search and identity UI widgets with a JavaScript SDK. Headquartered in Denver, Colorado, Switchfly has operated in travel technology for more than twenty years.
image: https://www.switchfly.com/
layout: provider
mcp_servers:
- description: ''
  name: Switchfly MCP Server
  slug: switchfly-mcp-server
modified: '2026-07-21'
name: Switchfly
nav: Providers
network: true
overview: 'Switchfly publishes 3 APIs on the [APIs.io](https://apis.io/) network: Machine to Machine (OAuth2 & Refund) API, OAuth 2 - SSO Authorize API, and Shopping Flow API. Tagged areas include Company, Travel, Loyalty, Travel Technology, and Rewards.


  Switchfly''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 54.9
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Switchfly Authentication
  slug: switchfly-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Switchfly Domain Security
  slug: switchfly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: switchfly
tags:
- Company
- Travel
- Loyalty
- Travel Technology
- Rewards
- Booking
- Dynamic Packaging
- White Label
- Points Redemption
- Travel Commerce
website: https://www.switchfly.com/dev/api-documentation/loyalty
---
