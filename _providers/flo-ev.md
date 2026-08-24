---
access_model:
  confidence: high
  label: No public developer program - partner/commercial integration only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The only live, anonymously callable machine-readable surface in FLO's estate. FLO's hardware and accessories store runs on Shopify, and that platform serves a Model Context Protocol server at https://
  name: FLO Store (Shopify Storefront MCP)
  slug: flo-store-shopify-storefront-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flo-ev-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flo-ev-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flo-ev-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flo-ev-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flo-ev-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flo-ev-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flo-ev-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.flo.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/flo-ev-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flo-ev-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flo-ev-llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.flo.com/support/home
- group: other
  title: ''
  type: Store
  url: https://store.flo.com/
- group: company
  title: ''
  type: Website
  url: https://www.flo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flo.com/ev-charging-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.flo.com/feed/
- group: company
  title: ''
  type: PressRoom
  url: https://www.flo.com/news-press/
- group: other
  title: ''
  type: MediaRoom
  url: https://www.flo.com/media-room/
- group: operate
  title: ''
  type: Support
  url: https://www.flo.com/support/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flo.com/business/product-documentation/
- group: start
  title: ''
  type: Login
  url: https://account.flo.com/
- group: company
  title: ''
  type: Partners
  url: https://www.flo.com/company/partner-networks/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flo.com/insights/ev-charging-roaming/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flo.com/business/utilities/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flo.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flo.com/terms-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/floevcharging/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FLOevcharging
- group: other
  title: ''
  type: Patents
  url: https://www.flo.com/patents/
created: '2026-07-27'
description: 'FLO is a Quebec City headquartered electric vehicle charging company, founded in 2009 as AddEnergie (addenergie.com now redirects to flo.com), that designs and manufactures its own Level 2 and DC fast charging hardware and operates one of the largest public charging networks in North America. FLO sits on the demand side of the electricity value chain rather than inside the regulated utility layer: it is a charge point operator and e-mobility service provider, not a distributor, transmitter or retailer, so Canada''s energy-data obligations do not reach it. Ontario''s Green Button regulation binds Ontario electricity and natural gas utilities, and Australia''s Consumer Data Right for energy is a different jurisdiction entirely; neither applies to FLO, and FLO publishes no consumer energy data API of any kind. Its API posture is closed and partner-mediated. flo.com has no developer subdomain and no published API reference: developer.flo.com, developers.flo.com, api.flo.com, docs.flo.com
  and data.flo.com all fail to resolve, and /developers, /api, /openapi.json, /swagger.json and /api-docs all return 404. FLO does name real interoperability standards on its own pages - OCPP 1.6J on the station-to-network side, OCPI for roaming with partner networks, and OpenADR 2.0 alongside "FLO''s flexible API" for utility demand response and smart grid integration - but each of those is reached through a commercial agreement rather than a signup form. Customer charging and session data is reachable only by the account holder through the account.flo.com login, and FLO publishes no open market, grid or station-location data feed under its own name. A second enrichment round in July 2026 did find live machine-readable surfaces on flo.com hosts, but all of them are platform-provided rather than FLO-authored: a Shopify storefront MCP server with five tools at store.flo.com/api/mcp plus public products.json and collections.json feeds, RFC 8414/9728 and OIDC discovery documents on store.flo.com,
  Salesforce Experience Cloud OIDC discovery on network.flo.com, and a Vanta trust center at trust.flo.com carrying FLO''s SOC 2 Type 2. FLO also runs real but entirely private API infrastructure - auth.flo.com is an AWS API Gateway that answers every path with 403 Missing Authentication Token, alongside csnms.flo.com and an EMS host - so the charging network itself remains closed.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flo-ev.png
layout: provider
mcp_servers:
- description: ''
  name: FLO Store MCP server
  slug: flo-store-mcp-server
modified: '2026-07-27'
name: FLO
nav: Providers
network: true
overview: 'FLO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, EV Charging, Electricity, and Grid.


  FLO''s developer surface includes authentication, engineering blog, support, documentation, and 26 more developer resources.'
random_paper: 18
scopes:
- name: Flo Ev Scopes
  scope_count: 38
  slug: flo-ev-scopes
  summary_line: 38 scopes · authorizationCode
score:
  band: thin
  composite: 29.7
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 29.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flo-ev/refs/heads/main/screenshots/flo-ev-2026-08-07T165350.png
security:
- kind: authentication
  name: Flo Ev Authentication
  slug: flo-ev-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Flo Ev Domain Security
  slug: flo-ev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flo Ev Trust Center
  slug: flo-ev-trust-center
  summary_line: SOC 2 Type 2, SOC 2 Type 1, PCI DSS
slug: flo-ev
tags:
- Energy
- Canada
- EV Charging
- Electricity
- Grid
- Demand Response
- Interoperability
- OCPP
- OCPI
- OpenADR
- Charge Point Operator
- Quebec
website: https://www.flo.com/
---
