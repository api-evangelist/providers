---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Token-issuing API on the Centrica FieldOps API Management platform, published on Centrica's Azure API Management developer portal. A single POST /oauth2/token operation exchanges an OAuth2 client_cred
  name: Centrica FieldOps Identity API
  slug: centrica-fieldops-identity-api
artifact_total: 8
collections:
- collection_type: open
  name: Identity API
  slug: open-centrica-fieldops-identity-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/centrica-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centrica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/centrica-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/centrica-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.britishgas.co.uk/global-maintenance/responsible-disclosure.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/centrica-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/centrica-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/centrica-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/centrica-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/centrica-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/centrica-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/centrica-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/centrica-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/centrica-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/centrica-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centrica-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.centrica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-developer.dev.fieldops.centrica.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-developer.dev.fieldops.centrica.com/
- group: start
  title: ''
  type: SignUp
  url: https://api-developer.dev.fieldops.centrica.com/signup
- group: commercial
  title: ''
  type: Plans
  url: https://api-developer.dev.fieldops.centrica.com/products
- group: docs
  title: ''
  type: APIReference
  url: https://api-developer.dev.fieldops.centrica.com/apis
- group: start
  title: ''
  type: Login
  url: https://api-developer.dev.fieldops.centrica.com/signin
- group: company
  title: ''
  type: Blog
  url: https://www.britishgas.co.uk/business/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.britishgas.co.uk/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.britishgas.co.uk/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centrica
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConnectedHomes
created: '2026-07-27'
description: 'Centrica plc is the FTSE-listed British energy and services group behind British Gas, the United Kingdom''s largest household energy supplier, along with Bord Gais Energy in Ireland, Centrica Business Solutions, Centrica Energy (its wholesale power, gas and LNG trading arm) and the Hive connected-home brand. It sits across the whole value chain — upstream gas and storage at Rough, generation and battery flexibility, wholesale trading and route-to-market, retail supply to roughly ten million UK homes, and a field-service engineering business — after exiting North America with the sale of Direct Energy to NRG in January 2021 to refocus on the UK and Ireland. Its API posture is honestly closed: Britain mandated the smart-metering INFRASTRUCTURE (the licensed Smart DCC monopoly and the SMETS2 rollout) rather than a consumer data right, so Centrica has no Consumer Data Right, no Green Button and no standards-conformant consumer usage endpoint. The DESNZ non-domestic smart meter
  data access requirement that does bind it is discharged by a written request answered within ten working days, not by an API. Household consumers reach their own data only through the British Gas app and account login; business customers through the Energy360 DataView portal. The single publicly reachable developer surface found is the Centrica FieldOps Azure API Management developer portal — a partner field-operations platform in its development environment — and Centrica publishes no open grid or market data of its own, leaving that to NESO, Elexon and the DNOs.'
image: https://www.britishgas.co.uk/aem6/etc/designs/britishgas/favicons/favicon-152x152.png
layout: provider
mcp_servers:
- description: Centrica publishes no MCP server. No hosted or remote server was found in the MCP registry, on npm under @modelcontextprotocol or any Centrica scope, in either Centrica GitHub organisation (github.com
  name: Centrica MCP Server
  slug: centrica-mcp-server
modified: '2026-07-27'
name: Centrica
nav: Providers
network: true
overview: 'Centrica publishes 1 API on the [APIs.io](https://apis.io/) network: FieldOps Identity API. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  Centrica''s developer surface includes authentication, sandbox, documentation, signup flow, API reference, engineering blog, and 23 more developer resources.'
plans:
- name: Centrica Plans
  plan_count: 2
  slug: centrica-plans
random_paper: 1
rate_limits:
- limit_count: 3
  name: Centrica Rate Limits
  slug: centrica-rate-limits
score:
  band: strong
  composite: 54.9
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 16.7
    contract_quality: 49.7
    developer_ergonomics: 49.4
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 54.9
  provenance:
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
    score: 52.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centrica/refs/heads/main/screenshots/centrica-2026-08-07T163224.png
security:
- kind: authentication
  name: Centrica Authentication
  slug: centrica-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Centrica Domain Security
  slug: centrica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Centrica Vulnerability Disclosure
  slug: centrica-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: centrica
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Retail
- Energy Markets
- Ireland
- Field Service
website: https://www.centrica.com/
---
